# -*- coding: utf-8 -*-
"""
Export all 105 questions from N2-MOCK-03 into blind evaluation datasets:
  - qa/blind_items_m03_s1_p1.json (38 items: Vocab + Grammar part 1)
  - qa/blind_items_m03_s1_p2.json (37 items: Grammar part 2 + Reading)
  - qa/blind_items_m03_s2.json (30 items: Listening comprehension)

Contains ONLY stems, options, and contextPassage / scripts.
Excludes correctAnswer, explanationVi, distractorExplanations.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def export_blind_m03():
    mock_file = ROOT / "data/mock_exams/n2_mock_03.json"
    with open(mock_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    sec1_items = []
    for q in data['sections'][0]['items']:
        sec1_items.append({
            "id": q["id"],
            "examId": "N2-MOCK-03",
            "section": 1,
            "skill": q.get("skill", "Language Knowledge"),
            "typeId": q.get("typeId", "Unknown"),
            "category": q.get("category", ""),
            "stem": q.get("stem", ""),
            "contextPassage": q.get("contextPassage", None),
            "options": [{"id": o["id"], "text": o["text"]} for o in q.get("options", [])],
        })

    sec2_items = []
    for q in data['sections'][1]['items']:
        sec2_items.append({
            "id": q["id"],
            "examId": "N2-MOCK-03",
            "section": 2,
            "skill": "Listening",
            "typeId": q.get("typeId", "Unknown"),
            "category": q.get("category", ""),
            "stem": q.get("stem", ""),
            "contextPassage": q.get("contextPassage") or q.get("script", ""),
            "script": q.get("script", ""),
            "options": [{"id": o["id"], "text": o["text"]} for o in q.get("options", [])],
            "audioUrl": q.get("audioUrl", "")
        })

    assert len(sec1_items) == 75, f"Expected 75 Sec 1 items, got {len(sec1_items)}"
    assert len(sec2_items) == 30, f"Expected 30 Sec 2 items, got {len(sec2_items)}"

    p1 = sec1_items[:38]
    p2 = sec1_items[38:]

    (ROOT / "qa/blind_items_m03_s1_p1.json").write_text(json.dumps(p1, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT / "qa/blind_items_m03_s1_p2.json").write_text(json.dumps(p2, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT / "qa/blind_items_m03_s2.json").write_text(json.dumps(sec2_items, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"Exported blind items for Mock 03: Part 1 ({len(p1)}), Part 2 ({len(p2)}), Sec 2 ({len(sec2_items)}).")

if __name__ == '__main__':
    export_blind_m03()
