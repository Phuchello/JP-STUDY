# -*- coding: utf-8 -*-
"""
Export all 210 questions from N2-MOCK-01 and N2-MOCK-02 into a clean blind dataset:
qa/blind_review_dataset_210.json
Contains ONLY stems, options, and context passages (reading/listening transcripts).
Excludes correctAnswer, explanationVi, distractorExplanations, and QA status.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def export_blind_dataset():
    items = []
    for mock_id in ["01", "02"]:
        exam_id = f"N2-MOCK-{mock_id}"
        json_path = ROOT / f"data/mock_exams/n2_mock_{mock_id}.json"
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for sec_idx, sec in enumerate(data['sections'], 1):
            for q in sec['items']:
                item = {
                    "id": q["id"],
                    "examId": exam_id,
                    "section": sec_idx,
                    "skill": q.get("skill", "Unknown"),
                    "typeId": q.get("typeId", "Unknown"),
                    "mondaiTitle": q.get("mondaiTitle", "Unknown"),
                    "stem": q.get("stem", ""),
                    "contextPassage": q.get("contextPassage", None),
                    "options": [{"id": o["id"], "text": o["text"]} for o in q.get("options", [])],
                }
                if sec_idx == 2:
                    item["audioUrl"] = q.get("audioUrl", "")
                items.append(item)

    out_path = ROOT / "qa/blind_review_dataset_210.json"
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    print(f"Exported {len(items)} items to {out_path}")

if __name__ == "__main__":
    export_blind_dataset()
