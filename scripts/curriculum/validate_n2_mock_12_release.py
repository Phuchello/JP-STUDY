# -*- coding: utf-8 -*-
"""Fail-closed content, review, and audio gate for the current N2-MOCK-12 version."""
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.acoustic_assurance import evaluate_audio_track_assurance
from scripts.curriculum.content_quality_checks import (
    pattern_defects,
    validate_answer_letter_references,
    validate_vietnamese_explanations,
)
from scripts.curriculum.mock_exam_release_checks import (
    validate_current_version_reconciliation,
    validate_full_mock_blueprint,
    validate_star_fragment_integrity,
)
from scripts.curriculum.question_fingerprint import compute_spoken_content_fingerprint

EXAM_PATH = ROOT / "data/mock_exams/n2_mock_12.json"
SEALED_PATH = ROOT / "qa/blind_items_m12_final.json"
REVIEW_PATH = ROOT / "qa/N2_MOCK_12_BLIND_RECONCILIATION.json"
MANIFEST_PATH = ROOT / "data/mock_exams/n2_mock_12_audio_manifest.json"
RECEIPT_PATH = ROOT / "qa/N2_MOCK_12_AUDIO_PLAYBACK_RECEIPT.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    errors: list[str] = []
    required = [EXAM_PATH, SEALED_PATH, REVIEW_PATH, MANIFEST_PATH, RECEIPT_PATH]
    for path in required:
        if not path.is_file():
            errors.append(f"Missing release evidence: {path.relative_to(ROOT)}")
    if errors:
        print("FAIL M12 release gate:\n- " + "\n- ".join(errors))
        return 1

    exam, sealed, review = read_json(EXAM_PATH), read_json(SEALED_PATH), read_json(REVIEW_PATH)
    manifest, receipt = read_json(MANIFEST_PATH), read_json(RECEIPT_PATH)
    if exam.get("examId") != "N2-MOCK-12" or exam.get("status") != "FULL_MOCK":
        errors.append("Exam must be N2-MOCK-12 with status FULL_MOCK")
    if exam.get("releaseGateStatus") != "REVIEW_CONTENT_VERSION_VERIFIED":
        errors.append("Exam releaseGateStatus must be REVIEW_CONTENT_VERSION_VERIFIED")
    errors.extend(validate_full_mock_blueprint(exam))
    errors.extend(validate_vietnamese_explanations(exam))
    errors.extend(validate_answer_letter_references(exam))
    errors.extend(validate_star_fragment_integrity(exam))
    errors.extend(pattern_defects({"N2-MOCK-12": exam}))
    raw_output = review.get("rawEvidence", {}).get("rawOutputFile")
    if not isinstance(raw_output, str) or not raw_output:
        errors.append("Current-version review is missing its preserved raw-output path")
    else:
        raw_path = (ROOT / raw_output).resolve()
        if ROOT.resolve() not in raw_path.parents or not raw_path.is_file():
            errors.append("Current-version raw-output file is missing or outside the repository")
        else:
            errors.extend(validate_current_version_reconciliation(
                review, exam, sealed, raw_sha256={"rawOutputSha256": raw_path}
            ))

    sections = exam.get("sections", [])
    if len(sections) == 2:
        expected_types = {
            "N2-MO-READ": 5, "N2-MO-ORTH": 5, "N2-MO-FORM": 5,
            "N2-MO-CONT": 7, "N2-MO-PARA": 5, "N2-MO-USE": 5,
            "N2-GR-FORM": 12, "N2-GR-STAR": 5, "N2-GR-PARA": 5,
            "N2-RD-SHORT": 5, "N2-RD-MED": 9, "N2-RD-PAIR": 2,
            "N2-RD-LONG": 3, "N2-RD-INFO": 2,
            "N2-LIS-TASK": 5, "N2-LIS-POINT": 6, "N2-LIS-SUMM": 5,
            "N2-LIS-RESP": 11, "N2-LIS-INTEG": 3,
        }
        actual_types = Counter(q.get("typeId") for section in sections for q in section.get("items", []))
        if dict(actual_types) != expected_types:
            errors.append(f"Question type allocation differs from the 75/30 blueprint: {dict(actual_types)}")
        if sections[0].get("durationMinutes") != 105 or sections[1].get("durationMinutes") != 50:
            errors.append("Section timers must remain 105 and 50 minutes")

    listening = sections[1].get("items", []) if len(sections) > 1 else []
    manifest_tracks = manifest if isinstance(manifest, dict) else {row.get("id"): row for row in manifest}
    receipt_rows = receipt.get("results", [])
    receipt_tracks = {row.get("questionId"): row for row in receipt_rows if isinstance(row, dict)}
    if len(manifest_tracks) != 30 or set(manifest_tracks) != {q.get("id") for q in listening}:
        errors.append("Audio manifest must cover exactly the 30 current listening items")
    if receipt.get("overallPlaybackVerified") is not True or len(receipt_tracks) != 30:
        errors.append("Playback receipt must verify exactly 30 unique current tracks")
    for q in listening:
        qid = q.get("id")
        meta = manifest_tracks.get(qid, {})
        row = receipt_tracks.get(qid, {})
        audio_path = ROOT / "docs" / str(meta.get("audioUrl", ""))
        assurance = evaluate_audio_track_assurance(meta, row, audio_path)
        if not assurance.get("BROWSER_PLAYBACK_VERIFIED"):
            errors.append(f"{qid}: current manifest, audio bytes, and Chromium playback evidence do not agree")
        if q.get("audioUrl") != meta.get("audioUrl") or q.get("audioSha256") != meta.get("audioSha256"):
            errors.append(f"{qid}: exam audio metadata differs from its manifest")
        if meta.get("spokenContentSha256") != compute_spoken_content_fingerprint(q):
            errors.append(f"{qid}: audio is not bound to the current script, prompt, and spoken-option order")

    if errors:
        print("FAIL M12 release gate:\n- " + "\n- ".join(errors))
        return 1
    print("PASS M12 release gate: 105 questions, current-version blind review, Vietnamese explanations, answer patterns, STAR, 30 hashes, decode and desktop/mobile Chromium playback.")
    print(f"Exam SHA-256: {sha256(EXAM_PATH)}")
    print(f"Sealed-input SHA-256: {sha256(SEALED_PATH)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
