# -*- coding: utf-8 -*-
"""Build a private IN_DEVELOPMENT payload for N2-MOCK-13 after audio QA."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.curriculum.acoustic_assurance import evaluate_audio_track_assurance
from scripts.curriculum.question_fingerprint import compute_spoken_content_fingerprint
from scripts.curriculum.bank_data.n2_mock_13_data import get_n2_mock_13_sec1_items
from scripts.curriculum.bank_data.n2_mock_13_listening import get_n2_mock_13_listening_items


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_full_mock_13() -> Path:
    sec1 = get_n2_mock_13_sec1_items()
    sec2 = get_n2_mock_13_listening_items()
    all_items = sec1 + sec2
    if len(sec1) != 75 or len(sec2) != 30 or len({q["id"] for q in all_items}) != 105:
        raise ValueError(f"M13 blueprint failure: section1={len(sec1)}, section2={len(sec2)}")

    for q in sec1:
        q["skill"] = "Reading" if q["typeId"].startswith("N2-RD-") else "Language Knowledge"
    for q in sec2:
        if not q.get("script"):
            raise ValueError(f"Listening transcript is missing for {q['id']}")
        q["contextPassage"] = q["script"]
        q["skill"] = "Listening"

    for q in all_items:
        options = q.get("options", [])
        if len(options) not in (3, 4) or q.get("correctAnswer") not in {o.get("id") for o in options}:
            raise ValueError(f"Invalid answer binding: {q['id']}")
        if not q.get("explanationVi") or q["explanationVi"] == q.get("explanationEn"):
            raise ValueError(f"Vietnamese explanation missing for {q['id']}")
        if len(q.get("distractorExplanations", {})) != len(options) - 1:
            raise ValueError(f"Distractor rationale missing for {q['id']}")

    manifest_path = ROOT / "data/mock_exams/n2_mock_13_audio_manifest.json"
    if not manifest_path.is_file():
        raise FileNotFoundError("M13 audio manifest is missing; generate the 30 original tracks first")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if len(manifest) != 30 or set(manifest) != {q["id"] for q in sec2}:
        raise ValueError("M13 audio manifest must cover the exact 30 listening IDs")

    receipt_path = ROOT / "qa/N2_MOCK_13_AUDIO_PLAYBACK_RECEIPT.json"
    receipt_tracks = {}
    if receipt_path.is_file():
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt_tracks = {row.get("questionId"): row for row in receipt.get("results", [])
                          if isinstance(row, dict) and row.get("questionId")}

    for q in sec2:
        meta = manifest[q["id"]]
        asset = ROOT / "docs" / meta["audioUrl"]
        actual = sha256(asset) if asset.is_file() else ""
        if not actual or actual != meta.get("audioSha256"):
            raise ValueError(f"Audio file/hash mismatch for {q['id']}")
        if meta.get("spokenContentSha256") != compute_spoken_content_fingerprint(q):
            raise ValueError(f"Audio is stale for the current script, prompt, or spoken-option order: {q['id']}")
        q.update({key: meta[key] for key in (
            "audioUrl", "audioDurationSec", "audioSha256", "audioSourceType", "speakerVoices"
        )})
        assurance = evaluate_audio_track_assurance(
            {"questionId": q["id"], "audioSha256": meta["audioSha256"]},
            receipt_tracks.get(q["id"], {}), asset,
        )
        q["audioVerificationStatus"] = "BROWSER_PLAYBACK_VERIFIED" if assurance["BROWSER_PLAYBACK_VERIFIED"] else "PLAYBACK_QA_PENDING"

    all_playback = all(q["audioVerificationStatus"] == "BROWSER_PLAYBACK_VERIFIED" for q in sec2)
    exam = {
        "examId": "N2-MOCK-13",
        "title": "JLPT N2 Practice Mock Exam #13 — Education, Media & Technology (đang phát triển)",
        "level": "N2", "status": "IN_DEVELOPMENT",
        "releaseGateStatus": "PENDING_INDEPENDENT_REVIEW_AND_BROWSER_E2E",
        "durationMinutes": 155, "totalQuestions": 105,
        "sections": [
            {"sectionId": "sec-1", "sectionName": "Phần 1: Kiến thức ngôn ngữ & Đọc hiểu", "durationMinutes": 105, "itemCount": 75, "items": sec1},
            {"sectionId": "sec-2", "sectionName": "Phần 2: Nghe hiểu", "durationMinutes": 50, "itemCount": 30,
             "audioStatus": "BROWSER_PLAYBACK_VERIFIED" if all_playback else "PLAYBACK_QA_PENDING",
             "audioNoticeVi": "Audio tiếng Nhật dùng giọng TTS tổng hợp; 30/30 track đã qua phát thử thực tế trên trình duyệt." if all_playback else "Audio tiếng Nhật dùng giọng TTS tổng hợp; MP3 đã hash-check, chờ phát thử thật trên trình duyệt.",
             "items": sec2},
        ],
    }
    out_dir = ROOT / "tmp/phase7"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "n2_mock_13_draft.json"
    out.write_text(json.dumps(exam, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Built private IN_DEVELOPMENT M13 draft: 75 + 30; playback={'verified' if all_playback else 'pending'}")
    print(f"Output: {out}")
    return out


if __name__ == "__main__":
    build_full_mock_13()
