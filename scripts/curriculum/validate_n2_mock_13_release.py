# -*- coding: utf-8 -*-
"""Fail-closed current-version content, blind-review, browser, and audio gate for M13."""
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

EXAM_PATH = ROOT / "data/mock_exams/n2_mock_13.json"
_EXAM = json.loads(EXAM_PATH.read_text(encoding="utf-8")) if EXAM_PATH.is_file() else {}
_PHASE71_RECEIPT = ROOT / "qa/N2_MOCK_13_PHASE71_CANDIDATE_RECONCILIATION.json"
_PHASE71 = (_EXAM.get("releaseGateStatus") == "REVIEW_CONTENT_VERSION_VERIFIED" and _PHASE71_RECEIPT.is_file()
            and hashlib.sha256(EXAM_PATH.read_bytes()).hexdigest() == json.loads(_PHASE71_RECEIPT.read_text(encoding="utf-8")).get("candidateExamSha256AtBuild"))
SEALED_PATH = ROOT / ("qa/blind_items_m13_phase71_candidate.json" if _PHASE71 else "qa/blind_items_m13_final.json")
REVIEW_PATH = ROOT / ("qa/N2_MOCK_13_PHASE71_CANDIDATE_RECONCILIATION.json" if _PHASE71 else "qa/N2_MOCK_13_BLIND_RECONCILIATION.json")
MANIFEST_PATH = ROOT / "data/mock_exams/n2_mock_13_audio_manifest.json"
RECEIPT_PATH = ROOT / "qa/N2_MOCK_13_AUDIO_PLAYBACK_RECEIPT.json"
ORIGINALITY_PATH = ROOT / "qa/N2_MOCK_13_ORIGINALITY_AUDIT.json"
E2E_PATH = ROOT / "qa/N2_MOCK_13_E2E_REPORT.json"

EXPECTED_TYPES = {
    "N2-MO-READ": 5, "N2-MO-ORTH": 5, "N2-MO-FORM": 5,
    "N2-MO-CONT": 7, "N2-MO-PARA": 5, "N2-MO-USE": 5,
    "N2-GR-FORM": 12, "N2-GR-STAR": 5, "N2-GR-PARA": 5,
    "N2-RD-SHORT": 5, "N2-RD-MED": 9, "N2-RD-PAIR": 2,
    "N2-RD-LONG": 3, "N2-RD-INFO": 2,
    "N2-LIS-TASK": 5, "N2-LIS-POINT": 6, "N2-LIS-SUMM": 5,
    "N2-LIS-RESP": 11, "N2-LIS-INTEG": 3,
}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    required = [EXAM_PATH, SEALED_PATH, REVIEW_PATH, MANIFEST_PATH, RECEIPT_PATH, ORIGINALITY_PATH, E2E_PATH]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.is_file()]
    if missing:
        print("FAIL M13 release gate: missing evidence: " + ", ".join(missing))
        return 1

    exam, sealed, review = read_json(EXAM_PATH), read_json(SEALED_PATH), read_json(REVIEW_PATH)
    manifest, receipt = read_json(MANIFEST_PATH), read_json(RECEIPT_PATH)
    originality, e2e = read_json(ORIGINALITY_PATH), read_json(E2E_PATH)
    errors: list[str] = []
    if exam.get("examId") != "N2-MOCK-13" or exam.get("status") != "FULL_MOCK":
        errors.append("Exam must be N2-MOCK-13 with status FULL_MOCK")
    if exam.get("releaseGateStatus") != "REVIEW_CONTENT_VERSION_VERIFIED":
        errors.append("releaseGateStatus must bind the release to the current text review")
    errors.extend(validate_full_mock_blueprint(exam))
    errors.extend(validate_vietnamese_explanations(exam))
    errors.extend(validate_answer_letter_references(exam))
    errors.extend(validate_star_fragment_integrity(exam))
    errors.extend(pattern_defects({"N2-MOCK-13": exam}))
    errors.extend(validate_current_version_reconciliation(review, exam, sealed))

    sections = exam.get("sections", [])
    if len(sections) == 2:
        actual_types = Counter(q.get("typeId") for section in sections for q in section.get("items", []))
        if dict(actual_types) != EXPECTED_TYPES:
            errors.append(f"Question type allocation differs from the 75/30 blueprint: {dict(actual_types)}")
        if [sections[0].get("durationMinutes"), sections[1].get("durationMinutes")] != [105, 50]:
            errors.append("Section durations must remain 105 and 50 minutes")
        if sections[1].get("audioStatus") != "BROWSER_PLAYBACK_VERIFIED":
            errors.append("Listening section is not marked as browser-playback verified")

    listening = sections[1].get("items", []) if len(sections) == 2 else []
    manifest_tracks = manifest if isinstance(manifest, dict) else {row.get("id"): row for row in manifest}
    receipt_tracks = {row.get("questionId"): row for row in receipt.get("results", []) if isinstance(row, dict)}
    if len(manifest_tracks) != 30 or set(manifest_tracks) != {q.get("id") for q in listening}:
        errors.append("Manifest must cover exactly the current 30 listening IDs")
    if receipt.get("overallPlaybackVerified") is not True or receipt.get("verifiedPlaybackCount") != 30 or len(receipt_tracks) != 30:
        errors.append("Playback receipt must verify exactly 30 unique current tracks")
    for question in listening:
        qid = question.get("id")
        meta, row = manifest_tracks.get(qid, {}), receipt_tracks.get(qid, {})
        asset = ROOT / "docs" / str(meta.get("audioUrl", ""))
        assurance = evaluate_audio_track_assurance(meta, row, asset)
        if not assurance.get("BROWSER_PLAYBACK_VERIFIED"):
            errors.append(f"{qid}: manifest, bytes, decode, and desktop/mobile playback evidence disagree")
        if question.get("audioUrl") != meta.get("audioUrl") or question.get("audioSha256") != meta.get("audioSha256"):
            errors.append(f"{qid}: exam audio metadata differs from its manifest")
        if meta.get("spokenContentSha256") != compute_spoken_content_fingerprint(question):
            errors.append(f"{qid}: audio is stale for the current transcript, prompt, or spoken-choice order")

    summary = originality.get("exactDistractorSetMatches", {})
    if originality.get("status") != "VERIFIED_CROSS_EXAM_AUDIT":
        errors.append("Cross-exam originality audit is missing or not marked verified")
    if originality.get("readingPassageOverlaps", {}).get("count") != 0 or originality.get("listeningScriptOverlaps", {}).get("count") != 0:
        errors.append("Cross-exam audit found a reading-passage or listening-script overlap")
    if summary.get("count") != 0:
        errors.append("Cross-exam audit found a repeated exact distractor set")
    if e2e.get("status") != "PASS_LOCAL_E2E" or e2e.get("allPassed") is not True or not all(row.get("passed") for row in e2e.get("checks", [])):
        errors.append("Local browser E2E report does not show every candidate check passing")

    raw_info = review.get("rawEvidence", {})
    raw_rel = str(raw_info.get("rawOutputFile", ""))
    required_raw_prefix = "qa/" if _PHASE71 else "tmp/"
    if raw_info.get("rawResponsePreservedLocally") is not True or not raw_rel.startswith(required_raw_prefix):
        errors.append("Review must reference the immutable raw response in its declared evidence location")
    else:
        raw_path = (ROOT / raw_rel).resolve()
        if not raw_path.is_file() or sha256(raw_path) != raw_info.get("rawOutputSha256"):
            errors.append("Available local raw review file does not match its recorded SHA-256")

    if errors:
        print("FAIL M13 release gate:\n- " + "\n- ".join(errors))
        return 1
    print("PASS M13 release gate: 105 questions, 105 Vietnamese explanations, current-version key-isolated review, balanced answers, STAR, 30 current audio fingerprints, integrity/decode, Chromium playback, originality, and candidate E2E.")
    print(f"Exam SHA-256: {sha256(EXAM_PATH)}")
    print(f"Sealed input SHA-256: {sha256(SEALED_PATH)}")
    print(f"Audio tracks: {len(listening)}/30; browser verified: {receipt.get('verifiedPlaybackCount')}/30")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
