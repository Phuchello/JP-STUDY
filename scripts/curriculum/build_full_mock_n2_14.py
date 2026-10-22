# -*- coding: utf-8 -*-
"""Build a private IN_DEVELOPMENT M14 payload; never promotes or publishes it."""
from __future__ import annotations

import json
import sys
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.bank_data.n2_mock_14_data import get_n2_mock_14_sec1_items
from scripts.curriculum.bank_data.n2_mock_14_listening import get_n2_mock_14_listening_items
from scripts.curriculum.content_quality_checks import (
    pattern_defects,
    validate_answer_letter_references,
    validate_vietnamese_explanations,
)
from scripts.curriculum.mock_exam_release_checks import (
    validate_full_mock_blueprint,
    validate_star_fragment_integrity,
)
from scripts.curriculum.audit_star_permutations import validate_star_structure
from scripts.curriculum.acoustic_assurance import evaluate_audio_track_assurance
from scripts.curriculum.question_fingerprint import compute_spoken_content_fingerprint


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_draft() -> Path:
    sec1 = get_n2_mock_14_sec1_items()
    sec2 = get_n2_mock_14_listening_items()
    for item in sec2:
        # The published practice engine receives no transcript during the
        # active listening section; the same Japanese script is retained here
        # only for authoring, fingerprints and review.
        item["script"] = item.get("script") or item.get("contextPassage") or ""
        item["contextPassage"] = item["script"]
        item["skill"] = "Listening"

    manifest_path = ROOT / "data/mock_exams/n2_mock_14_audio_manifest.json"
    receipt_path = ROOT / "qa/N2_MOCK_14_AUDIO_PLAYBACK_RECEIPT.json"
    receipt_tracks = {}
    if receipt_path.is_file():
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt_tracks = {
            row.get("questionId"): row for row in receipt.get("results", [])
            if isinstance(row, dict) and row.get("questionId")
        }

    audio_status = "NOT_GENERATED"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        expected_ids = {item["id"] for item in sec2}
        if len(manifest) != 30 or set(manifest) != expected_ids:
            raise ValueError("M14 audio manifest must cover exactly the 30 current Listening IDs")
        all_playback = True
        for item in sec2:
            meta = manifest[item["id"]]
            audio_url = meta.get("audioUrl", "")
            expected_url = f"audio/n2_mock_14/{item['id']}.mp3"
            if audio_url != expected_url:
                raise ValueError(f"Unexpected M14 audio URL for {item['id']}: {audio_url}")
            asset = ROOT / "docs" / audio_url
            actual = _sha256(asset) if asset.is_file() else ""
            if not actual or actual != meta.get("audioSha256"):
                raise ValueError(f"M14 audio file/hash mismatch for {item['id']}")
            if meta.get("spokenContentSha256") != compute_spoken_content_fingerprint(item):
                raise ValueError(f"M14 audio is stale for current script, prompt, or spoken-choice order: {item['id']}")
            item.update({key: meta[key] for key in (
                "audioUrl", "audioDurationSec", "audioSha256", "audioSizeBytes",
                "audioSourceType", "speakerVoices", "spokenContentSha256",
            )})
            assurance = evaluate_audio_track_assurance(
                {"questionId": item["id"], "audioSha256": meta["audioSha256"]},
                receipt_tracks.get(item["id"], {}), asset,
            )
            item["audioVerificationStatus"] = (
                "BROWSER_PLAYBACK_VERIFIED"
                if assurance["BROWSER_PLAYBACK_VERIFIED"] else "PLAYBACK_QA_PENDING"
            )
            all_playback = all_playback and assurance["BROWSER_PLAYBACK_VERIFIED"]
        audio_status = "BROWSER_PLAYBACK_VERIFIED" if all_playback else "PLAYBACK_QA_PENDING"

    exam = {
        "examId": "N2-MOCK-14",
        "title": "JLPT N2 Practice Mock Exam #14 — Comprehensive Challenge (đang phát triển)",
        "level": "N2",
        "status": "IN_DEVELOPMENT",
        "releaseGateStatus": "PENDING_INDEPENDENT_CONTENT_REVIEW_AND_RELEASE_QA",
        "durationMinutes": 155,
        "totalQuestions": 105,
        "sections": [
            {"sectionId": "sec-1", "sectionName": "Phần 1: Kiến thức ngôn ngữ & Đọc hiểu",
             "durationMinutes": 105, "itemCount": 75, "items": sec1},
            {"sectionId": "sec-2", "sectionName": "Phần 2: Nghe hiểu",
             "durationMinutes": 50, "itemCount": 30,
             "audioStatus": audio_status,
             "audioNoticeVi": (
                 "Bản phát triển: audio đã phát thử trong Chromium trên máy tính và chế độ di động. "
                 "Đây vẫn chưa phải bản phát hành; nội dung đang chờ rà soát độc lập."
                 if audio_status == "BROWSER_PLAYBACK_VERIFIED" else
                 "Bản phát triển: audio cần hoàn tất kiểm tra phát thử trên trình duyệt. "
                 "Đây chưa phải bài thi nghe đã qua QA phát hành."
                 if audio_status == "PLAYBACK_QA_PENDING" else
                 "Bản đang phát triển: 30 kịch bản chưa có MP3. Đây chưa phải bài thi nghe có thể làm."
             ),
             "items": sec2},
        ],
    }
    errors = []
    errors.extend(validate_full_mock_blueprint(exam))
    errors.extend(validate_vietnamese_explanations(exam))
    errors.extend(validate_answer_letter_references(exam))
    errors.extend(validate_star_fragment_integrity(exam))
    errors.extend(pattern_defects({"N2-MOCK-14": exam}))
    all_items = [item for section in exam["sections"] for item in section["items"]]
    star_items = [item for item in all_items if item.get("typeId") == "N2-GR-STAR"]
    if len(star_items) != 5:
        errors.append(f"M14 must contain five STAR items, got {len(star_items)}")
    for item in star_items:
        valid, reason, permutation_data = validate_star_structure(item)
        if not valid or len(permutation_data.get("permutations", [])) != 24:
            errors.append(f"{item['id']}: strict STAR structure/permutation check failed: {reason}")
    if len({item["id"] for item in all_items}) != 105:
        errors.append("M14 question IDs are not unique")
    for item in all_items:
        if len({option["text"] for option in item.get("options", [])}) != len(item.get("options", [])):
            errors.append(f"{item.get('id')}: duplicate options")
        if item.get("correctAnswer") not in {option.get("id") for option in item.get("options", [])}:
            errors.append(f"{item.get('id')}: answer key is not bound to a displayed option")
    if errors:
        raise ValueError("M14 draft validation failed:\n- " + "\n- ".join(errors))
    out = ROOT / "tmp/phase7/n2_mock_14_draft.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(exam, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Built private IN_DEVELOPMENT M14 draft: {len(sec1)} Section 1 items + {len(sec2)} listening scripts")
    print(f"Output: {out}")
    return out


if __name__ == "__main__":
    build_draft()
