# -*- coding: utf-8 -*-
"""Export only the sealed, key-free N2-MOCK-07 star items for blind review."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.blind_review_exporter import validate_sealed_item_purity
from scripts.curriculum.question_fingerprint import compute_question_fingerprint

EXAM_PATH = ROOT / "data/mock_exams/n2_mock_07.json"
FINAL_TWO = "--final-two" in sys.argv
OUT_PATH = ROOT / ("qa/blind_items_m07_star_revision_12.json" if FINAL_TWO else "qa/blind_items_m07_star_revision_5.json")
TARGET_IDS = ({"N2_07_M8_04", "N2_07_M8_05"} if FINAL_TWO
              else {f"N2_07_M8_0{i}" for i in range(1, 6)})


def main():
    exam = json.loads(EXAM_PATH.read_text(encoding="utf-8"))
    items = [q for q in exam["sections"][0]["items"] if q.get("id") in TARGET_IDS]
    if {q["id"] for q in items} != TARGET_IDS:
        raise ValueError(f"Could not locate all {len(TARGET_IDS)} revised star questions")
    sealed = []
    for q in items:
        item = {
            "id": q["id"],
            "examId": exam["examId"],
            "section": 1,
            "skill": q.get("skill", "Language Knowledge"),
            "typeId": q.get("typeId"),
            "category": q.get("category", ""),
            "taskInstructions": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
            "stem": q.get("stem", ""),
            "contextPassage": q.get("contextPassage") or q.get("passage") or None,
            "options": [{"id": o["id"], "text": o["text"]} for o in q.get("options", [])],
            "contentFingerprint": compute_question_fingerprint(q),
        }
        validate_sealed_item_purity(item)
        sealed.append(item)
    OUT_PATH.write_text(json.dumps(sealed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(sealed)} key-free star items to {OUT_PATH.name}")


if __name__ == "__main__":
    main()
