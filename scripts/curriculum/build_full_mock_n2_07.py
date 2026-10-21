# -*- coding: utf-8 -*-
"""
JP-STUDY: BUILD COMPLETE JLPT N2 FULL MOCK #07
- Section 1: Language Knowledge & Reading (75 original items, 105 mins)
- Section 2: Listening Comprehension (30 original items, 50 mins) with verified Neural TTS audio
- Compiles into data/mock_exams/n2_mock_07.json
"""
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.curriculum.bank_data.n2_mock_07_data import get_n2_mock_07_sec1_items
from scripts.curriculum.bank_data.n2_mock_07_listening import get_n2_mock_07_listening_items
from scripts.curriculum.acoustic_assurance import evaluate_audio_track_assurance

def build_full_mock_07():
    print("=== Compiling JLPT N2 Full Mock #07 ===")
    sec1_items = get_n2_mock_07_sec1_items()
    print(f"Loaded {len(sec1_items)} items for Section 1.")

    sec2_items = get_n2_mock_07_listening_items()
    print(f"Loaded {len(sec2_items)} items for Section 2.")

    # The practice engine uses this field to split the section score into
    # Language Knowledge and Reading. Without it, Reading is reported as 0/0.
    for q in sec1_items:
        type_id = q.get("typeId", "")
        if type_id.startswith("N2-RD-"):
            q["skill"] = "Reading"
        elif type_id.startswith(("N2-MO-", "N2-GR-")):
            q["skill"] = "Language Knowledge"
        else:
            raise ValueError(f"Unmapped N2-MOCK-07 Section 1 typeId: {type_id!r} ({q.get('id')})")
    for q in sec2_items:
        if not q.get("typeId", "").startswith("N2-LIS-"):
            raise ValueError(f"Unmapped N2-MOCK-07 Section 2 typeId: {q.get('typeId')!r} ({q.get('id')})")
        q["skill"] = "Listening"

    for q in sec1_items + sec2_items:
        # The source bank uses `explanation`; the app and release gate consume
        # `explanationVi`. Keep the source text and expose the canonical field.
        if not q.get("explanationVi") and q.get("explanation"):
            q["explanationVi"] = q["explanation"]
        if len(str(q.get("explanationVi", "")).strip()) < 15:
            raise ValueError(f"Missing Vietnamese explanation for {q.get('id')}")

    # Load audio manifest if available
    manifest_path = ROOT / 'data/mock_exams/n2_mock_07_audio_manifest.json'
    audio_manifest = {}
    if manifest_path.exists():
        with open(manifest_path, 'r', encoding='utf-8') as f:
            audio_manifest = json.load(f)
        print(f"Loaded audio manifest with {len(audio_manifest)} entries.")
    else:
        print("Audio manifest not found yet, applying default audio paths.")

    receipt_path = ROOT / 'qa/N2_MOCK_07_AUDIO_PLAYBACK_RECEIPT.json'
    receipt_tracks = {}
    if receipt_path.exists():
        with open(receipt_path, 'r', encoding='utf-8') as f:
            receipt_data = json.load(f)
        receipt_tracks = {
            row.get('questionId'): row
            for row in receipt_data.get('results', [])
            if isinstance(row, dict) and row.get('questionId')
        }

    for q in sec2_items:
        qid = q['id']
        if qid in audio_manifest:
            meta = audio_manifest[qid]
            q['audioUrl'] = meta['audioUrl']
            q['audioDurationSec'] = meta['audioDurationSec']
            q['audioSha256'] = meta['audioSha256']
            q['audioSourceType'] = meta['audioSourceType']
            q['speakerVoices'] = meta['speakerVoices']
        else:
            q['audioUrl'] = f"audio/n2_mock_07/{qid}.mp3"
            q['audioSourceType'] = "NEURAL_TTS_MULTI_VOICE"
            q['speakerVoices'] = ["ja-JP-NanamiNeural", "ja-JP-KeitaNeural"]
        meta = audio_manifest.get(qid, {})
        receipt = receipt_tracks.get(qid, {})
        asset_path = ROOT / 'docs' / q['audioUrl']
        assurance = evaluate_audio_track_assurance(
            {"questionId": qid, "audioSha256": meta.get('audioSha256', q.get('audioSha256', ''))},
            receipt,
            asset_path,
        )
        q['audioVerificationStatus'] = (
            "BROWSER_PLAYBACK_VERIFIED" if assurance["BROWSER_PLAYBACK_VERIFIED"] else "PLAYBACK_QA_PENDING"
        )

    mock = {
        "examId": "N2-MOCK-07",
        "title": "JLPT N2 Full Mock Exam #07 — Đề thi thử hoàn chỉnh (Kiến thức ngôn ngữ, Đọc hiểu & Nghe hiểu)",
        "level": "N2",
        "status": "FULL_MOCK",
        "durationMinutes": 155,
        "totalQuestions": 105,
        "sections": [
            {
                "sectionId": "sec-1",
                "sectionName": "Phần 1: Kiến thức ngôn ngữ & Đọc hiểu (Language Knowledge & Reading)",
                "durationMinutes": 105,
                "itemCount": len(sec1_items),
                "items": sec1_items
            },
            {
                "sectionId": "sec-2",
                "sectionName": "Phần 2: Nghe hiểu (Listening Comprehension)",
                "durationMinutes": 50,
                "itemCount": len(sec2_items),
                "audioStatus": (
                    "BROWSER_PLAYBACK_VERIFIED"
                    if sec2_items and all(q.get("audioVerificationStatus") == "BROWSER_PLAYBACK_VERIFIED" for q in sec2_items)
                    else "PLAYBACK_QA_PENDING"
                ),
                "audioNoticeVi": (
                    "30 tệp đã khớp SHA-256, giải mã và ghi nhận tiến triển phát trên trình duyệt máy tính và di động; chưa có chứng nhận chuyên gia về phát âm."
                    if sec2_items and all(q.get("audioVerificationStatus") == "BROWSER_PLAYBACK_VERIFIED" for q in sec2_items)
                    else "Một số tệp chưa có đủ bằng chứng hash và phát thực tế trên trình duyệt."
                ),
                "items": sec2_items
            }
        ]
    }

    out_file = ROOT / 'data/mock_exams/n2_mock_07.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(mock, f, ensure_ascii=False, indent=2)

    print(f"Successfully compiled N2-MOCK-07 to {out_file} (105 items).")

if __name__ == '__main__':
    build_full_mock_07()
