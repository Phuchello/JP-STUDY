# -*- coding: utf-8 -*-
"""Integrate a fully gated N2-MOCK-12 payload into the playable bank and catalog."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.curriculum.add_mock_11_to_bank import remove_data_entry, replace_html_card, replace_js_object

BANK_PATH = ROOT / "docs/widgets/mock_exam_bank.js"
HTML_PATH = ROOT / "docs/widgets/jlpt_exam_catalog.html"
EXAM_PATH = ROOT / "data/mock_exams/n2_mock_12.json"
KEY = "N2-MOCK-12"


def main() -> None:
    exam = json.loads(EXAM_PATH.read_text(encoding="utf-8"))
    sections = exam.get("sections", [])
    items = [q for section in sections for q in section.get("items", [])]
    if exam.get("examId") != KEY or exam.get("status") != "FULL_MOCK":
        raise ValueError("Only a promoted FULL_MOCK may be added to the playable bank")
    if exam.get("releaseGateStatus") != "REVIEW_CONTENT_VERSION_VERIFIED":
        raise ValueError("M12 current-version content review gate has not passed")
    if [len(section.get("items", [])) for section in sections] != [75, 30] or len(items) != 105:
        raise ValueError("M12 integration requires exactly 75 + 30 questions")
    if any(q.get("audioVerificationStatus") != "BROWSER_PLAYBACK_VERIFIED" for q in sections[1]["items"]):
        raise ValueError("All 30 tracks must have exact-asset browser playback evidence")

    source = BANK_PATH.read_text(encoding="utf-8")
    catalog_entry = {
        "mockId": KEY,
        "title": exam["title"],
        "level": "N2",
        "status": "FULL_MOCK",
        "badgeText": "PRACTICE MOCK · AI BLIND-REVIEWED · 105 CÂU",
        "badgeClass": "status-ready",
        "durationMinutes": 155,
        "totalQuestions": 105,
        "section1Count": 75,
        "section2Count": 30,
        "releaseDate": "22/10/2026",
        "description": "Đề luyện tập nguyên bản về xã hội, môi trường và đời sống công cộng, gồm 32 câu Từ vựng/Kanji, 22 Ngữ pháp, 21 Đọc hiểu và 30 câu Nghe với giọng TTS tổng hợp. AI đã rà soát mù theo phiên bản; không phải đề JLPT chính thức, chưa có chứng nhận người bản ngữ hoặc hiệu chuẩn tâm trắc.",
        "playable": True,
    }
    source = replace_js_object(source, f'"mockId": "{KEY}"', json.dumps(catalog_entry, ensure_ascii=False, indent=6))
    source = remove_data_entry(source, KEY)
    marker = "  'N3-MOCK-01': {"
    if marker not in source:
        raise ValueError("Could not locate N3 data entry in the mock bank")
    entry = f"  '{KEY}': " + json.dumps(exam, ensure_ascii=False, indent=2) + ",\n"
    BANK_PATH.write_text(source.replace(marker, entry + marker, 1), encoding="utf-8", newline="\n")

    card = '''<div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">JLPT N2</span>
          <span class="status-badge status-ready">PRACTICE MOCK · AI BLIND-REVIEWED · 105 CÂU</span>
        </div>
        <div class="card-title">JLPT N2 | Practice Mock Exam #12</div>
        <div class="card-meta">105 câu hỏi · 155 phút · Bố cục luyện tập JP-STUDY</div>
        <div class="card-desc">
          Đề luyện tập nguyên bản về xã hội, môi trường và đời sống công cộng, gồm 32 câu Từ vựng/Kanji, 22 Ngữ pháp, 21 Đọc hiểu và 30 câu Nghe bằng giọng TTS tổng hợp. AI đã rà soát mù theo phiên bản. Đây không phải đề JLPT chính thức; chưa có chứng nhận người bản ngữ hoặc hiệu chuẩn tâm trắc.
        </div>
        <div class="section-tags">
          <span class="sec-tag">Từ vựng (32c)</span>
          <span class="sec-tag">Ngữ pháp (22c)</span>
          <span class="sec-tag">Đọc hiểu (21c)</span>
          <span class="sec-tag">Nghe hiểu (30c)</span>
        </div>
      </div>
      <div style="display:flex; flex-direction:column; gap:6px; margin-top:12px;">
        <a href="https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mock&amp;mockId=N2-MOCK-12" target="_blank" rel="noopener noreferrer" class="btn-start">
          🚀 BẮT ĐẦU ĐỀ LUYỆN TẬP ĐẦY ĐỦ (105 CÂU / 155 PHÚT) ▶
        </a>
        <a href="https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mock&amp;mockId=N2-MOCK-12&amp;section=2" target="_blank" rel="noopener noreferrer" class="btn-mat" style="justify-content:center; padding:8px; font-size:0.8rem;">
          🎧 Làm riêng Phần 2 Nghe hiểu (30 câu / 50 phút) ↗
        </a>
      </div>
    </div>'''
    html = HTML_PATH.read_text(encoding="utf-8")
    existing_title = next((title for title in ("JLPT N2 | Full Mock Exam #12", "JLPT N2 | Practice Mock Exam #12") if title in html), None)
    if not existing_title:
        raise ValueError("Could not locate the current #12 catalog card title")
    html = replace_html_card(html, existing_title, card)
    HTML_PATH.write_text(html, encoding="utf-8", newline="\n")
    print("Integrated FULL_MOCK N2-MOCK-12 into the playable bank and static catalog.")


if __name__ == "__main__":
    main()
