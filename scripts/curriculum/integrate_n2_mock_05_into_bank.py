# -*- coding: utf-8 -*-
"""
Integrate JLPT N2 Full Mock #05 into docs/widgets/mock_exam_bank.js
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BANK_JS_PATH = ROOT / "docs/widgets/mock_exam_bank.js"
MOCK_05_JSON_PATH = ROOT / "data/mock_exams/n2_mock_05.json"

def integrate_mock_05():
    assert BANK_JS_PATH.exists(), "mock_exam_bank.js must exist"
    assert MOCK_05_JSON_PATH.exists(), "n2_mock_05.json must exist"

    content = BANK_JS_PATH.read_text(encoding='utf-8')
    mock_05_data = json.loads(MOCK_05_JSON_PATH.read_text(encoding='utf-8'))

    # 1. Update Catalog entry
    old_catalog_entry = '''    {
      "mockId": "N2-MOCK-05",
      "title": "JLPT N2 Full Mock Exam #05",
      "level": "N2",
      "status": "IN_DEVELOPMENT",
      "badgeText": "IN DEVELOPMENT · ĐANG BIÊN SOẠN",
      "badgeClass": "status-dev",
      "durationMinutes": 155,
      "totalQuestions": 105,
      "section1Count": 75,
      "section2Count": 30,
      "releaseDate": "Kỳ thi 12/2026 (Đợt 2)",
      "description": "Bộ đề mô phỏng đợt thi số 05. Đang trong quy trình biên soạn chuẩn hóa ngữ cảnh và kịch bản nghe hiểu.",
      "playable": false
    },'''

    new_catalog_entry = '''    {
      "mockId": "N2-MOCK-05",
      "title": "JLPT N2 Full Mock Exam #05 — Kiến thức ngôn ngữ, Đọc hiểu & Nghe hiểu",
      "level": "N2",
      "status": "FULL_MOCK",
      "badgeText": "FULL MOCK · 105 CÂU · 30 AUDIO PHÒNG THI",
      "badgeClass": "status-ready",
      "durationMinutes": 155,
      "totalQuestions": 105,
      "section1Count": 75,
      "section2Count": 30,
      "releaseDate": "19/10/2026",
      "description": "Bộ đề thi thử số 05 mô phỏng toàn diện bám sát cấu trúc JLPT N2: Phần 1 (75 câu / 105 phút: 32 câu Từ vựng, 22 câu Ngữ pháp, 21 câu Đọc hiểu) + Nghỉ giải lao 10 phút + Phần 2 (30 câu / 50 phút: Đầy đủ 5 Mondai Nghe hiểu kèm audio phòng thi đa nhân vật và transcript phân vai). Báo cáo điểm số gốc minh bạch và chẩn đoán năng lực.",
      "playable": true
    },'''

    assert old_catalog_entry in content, "Could not find old catalog entry for N2-MOCK-05"
    content = content.replace(old_catalog_entry, new_catalog_entry, 1)

    # 2. Insert into MOCK_EXAM_BANK dictionary before 'N3-MOCK-01'
    target_anchor = "  'N3-MOCK-01': {"
    assert target_anchor in content, "Could not find target anchor 'N3-MOCK-01' in mock_exam_bank.js"

    mock_05_formatted = "  'N2-MOCK-05': " + json.dumps(mock_05_data, ensure_ascii=False, indent=2) + ",\n\n"

    content = content.replace(target_anchor, mock_05_formatted + target_anchor, 1)

    BANK_JS_PATH.write_text(content, encoding='utf-8')
    print("Successfully integrated N2-MOCK-05 into docs/widgets/mock_exam_bank.js")

if __name__ == "__main__":
    integrate_mock_05()
