# -*- coding: utf-8 -*-
"""Build a private, explicitly in-development JSON for N2-MOCK-10."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.curriculum.acoustic_assurance import evaluate_audio_track_assurance
from scripts.curriculum.bank_data.n2_mock_10_data import get_n2_mock_10_sec1_items
from scripts.curriculum.bank_data.n2_mock_10_listening import get_n2_mock_10_listening_items


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_full_mock_10() -> Path:
    sec1 = get_n2_mock_10_sec1_items()
    sec2 = get_n2_mock_10_listening_items()
    all_items = sec1 + sec2
    if len(sec1) != 75 or len(sec2) != 30 or len({q["id"] for q in all_items}) != 105:
        raise ValueError(f"M10 blueprint failure: section1={len(sec1)}, section2={len(sec2)}")

    for q in sec1:
        type_id = q.get("typeId", "")
        if type_id.startswith("N2-RD-"):
            q["skill"] = "Reading"
        elif type_id.startswith(("N2-MO-", "N2-GR-")):
            q["skill"] = "Language Knowledge"
        else:
            raise ValueError(f"Unmapped section 1 type: {q.get('id')} {type_id}")
    for q in sec2:
        if not q.get("typeId", "").startswith("N2-LIS-"):
            raise ValueError(f"Unmapped listening type: {q.get('id')} {q.get('typeId')}")
        if not q.get("script"):
            raise ValueError(f"Listening transcript is missing for {q.get('id')}")
        # Bind the reviewed transcript to the current question fingerprint;
        # the browser UI must still keep this transcript hidden during a test.
        q["contextPassage"] = q["script"]
        q["skill"] = "Listening"

    for q in all_items:
        answer_ids = {option.get("id") for option in q.get("options", [])}
        if q.get("correctAnswer") not in answer_ids:
            raise ValueError(f"Invalid answer key in {q['id']}")
        if not q.get("explanationVi") or q["explanationVi"] == q.get("explanation"):
            raise ValueError(f"Vietnamese explanation is missing for {q['id']}")

    manifest_path = ROOT / "data/mock_exams/n2_mock_10_audio_manifest.json"
    if not manifest_path.is_file():
        raise FileNotFoundError("M10 audio manifest is missing")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if len(manifest) != 30 or {q["id"] for q in sec2} != set(manifest):
        raise ValueError(f"M10 audio manifest must cover the exact 30 tracks; got {len(manifest)}")

    receipt_path = ROOT / "qa/N2_MOCK_10_AUDIO_PLAYBACK_RECEIPT.json"
    receipt_tracks = {}
    if receipt_path.is_file():
        receipt_data = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt_tracks = {
            row.get("questionId"): row
            for row in receipt_data.get("results", [])
            if isinstance(row, dict) and row.get("questionId")
        }

    for q in sec2:
        meta = manifest[q["id"]]
        asset = ROOT / "docs" / meta["audioUrl"]
        actual_hash = sha256(asset) if asset.is_file() else ""
        if not actual_hash or actual_hash != meta.get("audioSha256"):
            raise ValueError(f"Audio file/hash mismatch for {q['id']}")
        q.update({
            "audioUrl": meta["audioUrl"],
            "audioDurationSec": meta["audioDurationSec"],
            "audioSha256": meta["audioSha256"],
            "audioSourceType": meta["audioSourceType"],
            "speakerVoices": meta["speakerVoices"],
        })
        assurance = evaluate_audio_track_assurance(
            {"questionId": q["id"], "audioSha256": meta["audioSha256"]},
            receipt_tracks.get(q["id"], {}),
            asset,
        )
        q["audioVerificationStatus"] = (
            "BROWSER_PLAYBACK_VERIFIED" if assurance["BROWSER_PLAYBACK_VERIFIED"] else "PLAYBACK_QA_PENDING"
        )

    all_playback_verified = all(q["audioVerificationStatus"] == "BROWSER_PLAYBACK_VERIFIED" for q in sec2)
    exam = {
        "examId": "N2-MOCK-10",
        "title": "JLPT N2 Full Mock Exam #10 — Đề thi thử (đang phát triển)",
        "level": "N2",
        "status": "IN_DEVELOPMENT",
        "releaseGateStatus": "PENDING_INDEPENDENT_REVIEW_AND_BROWSER_E2E",
        "durationMinutes": 155,
        "totalQuestions": 105,
        "sections": [
            {
                "sectionId": "sec-1",
                "sectionName": "Phần 1: Kiến thức ngôn ngữ & Đọc hiểu",
                "durationMinutes": 105,
                "itemCount": 75,
                "items": sec1,
            },
            {
                "sectionId": "sec-2",
                "sectionName": "Phần 2: Nghe hiểu",
                "durationMinutes": 50,
                "itemCount": 30,
                "audioStatus": "BROWSER_PLAYBACK_VERIFIED" if all_playback_verified else "PLAYBACK_QA_PENDING",
                "audioNoticeVi": (
                    "Các tệp có hash khớp và đã có bằng chứng phát thực tế trên trình duyệt."
                    if all_playback_verified
                    else "30 tệp MP3 đã được tạo và khớp hash manifest; kiểm tra phát thực tế trên trình duyệt đang chờ."
                ),
                "items": sec2,
            },
        ],
    }
    out = ROOT / "data/mock_exams/n2_mock_10.json"
    out.write_text(json.dumps(exam, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Built IN_DEVELOPMENT N2-MOCK-10: 75 + 30 questions, 30 hash-verified MP3 files")
    print(f"Output: {out}")
    print(f"Browser playback: {'verified' if all_playback_verified else 'pending'}")
    return out


if __name__ == "__main__":
    build_full_mock_10()
