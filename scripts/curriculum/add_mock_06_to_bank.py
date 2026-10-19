# -*- coding: utf-8 -*-
"""
Add N2-MOCK-06 to docs/widgets/mock_exam_bank.js:
1. Update N2 registry entry: FULL_MOCK, playable: true, releaseDate: 19/10/2026.
2. Insert N2-MOCK-06 full exam JSON into window.JP_MOCK_DATA.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
bank_path = ROOT / "docs/widgets/mock_exam_bank.js"
m6_path = ROOT / "data/mock_exams/n2_mock_06.json"

content = bank_path.read_text(encoding='utf-8')
m6_data = json.loads(m6_path.read_text(encoding='utf-8'))

# 1. Update Registry Entry
old_reg = """    {
      "mockId": "N2-MOCK-06",
      "title": "JLPT N2 Full Mock Exam #06",
      "level": "N2",
      "status": "IN_DEVELOPMENT",
      "badgeText": "IN DEVELOPMENT · ĐANG BIÊN SOẠN",
      "badgeClass": "status-dev",
      "durationMinutes": 155,
      "totalQuestions": 105,
      "section1Count": 75,
      "section2Count": 30,
      "releaseDate": "Kỳ thi 12/2026 (Đợt 2)",
      "description": "Bộ đề mô phỏng đợt thi số 06. Đang trong quy trình biên soạn chuẩn hóa ngữ cảnh và kịch bản nghe hiểu.",
      "playable": false
    }"""

new_reg = """    {
      "mockId": "N2-MOCK-06",
      "title": "JLPT N2 Full Mock Exam #06 — Kiến thức ngôn ngữ, Đọc hiểu & Nghe hiểu",
      "level": "N2",
      "status": "FULL_MOCK",
      "badgeText": "FULL MOCK · 105 CÂU · 30 AUDIO PHÒNG THI",
      "badgeClass": "status-ready",
      "durationMinutes": 155,
      "totalQuestions": 105,
      "section1Count": 75,
      "section2Count": 30,
      "releaseDate": "19/10/2026",
      "description": "Bộ đề thi thử số 06 mô phỏng toàn diện bám sát cấu trúc JLPT N2: Phần 1 (75 câu / 105 phút: 32 câu Từ vựng, 22 câu Ngữ pháp, 21 câu Đọc hiểu) + Nghỉ giải lao 10 phút + Phần 2 (30 câu / 50 phút: Đầy đủ 5 Mondai Nghe hiểu kèm audio phòng thi đa nhân vật và transcript phân vai). Báo cáo điểm số gốc minh bạch và chẩn đoán năng lực.",
      "playable": true
    }"""

assert old_reg in content, "Could not find N2-MOCK-06 registry block in mock_exam_bank.js"
content = content.replace(old_reg, new_reg)

# 2. Insert N2-MOCK-06 into JP_MOCK_DATA before N3-MOCK-01
n3_token = "  'N3-MOCK-01': {"
assert n3_token in content, "Could not find 'N3-MOCK-01': { in mock_exam_bank.js"

m6_json_str = "  'N2-MOCK-06': " + json.dumps(m6_data, ensure_ascii=False, indent=2) + ",\n\n"
content = content.replace(n3_token, m6_json_str + n3_token)

bank_path.write_text(content, encoding='utf-8')
print("Successfully integrated N2-MOCK-06 into docs/widgets/mock_exam_bank.js")
