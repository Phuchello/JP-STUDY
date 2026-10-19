# -*- coding: utf-8 -*-
"""
Split qa/blind_review_dataset_210.json into 6 focused batches for reliable blind subagent reviews:
1. qa/blind_items_m01_s1_p1.json (38 items: Vocab + Grammar)
2. qa/blind_items_m01_s1_p2.json (37 items: Reading)
3. qa/blind_items_m01_s2.json (30 items: Listening)
4. qa/blind_items_m02_s1_p1.json (38 items: Vocab + Grammar)
5. qa/blind_items_m02_s1_p2.json (37 items: Reading)
6. qa/blind_items_m02_s2.json (30 items: Listening)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def split_blind_items():
    dataset_path = ROOT / "qa/blind_review_dataset_210.json"
    with open(dataset_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    m01 = [q for q in items if q["examId"] == "N2-MOCK-01"]
    m02 = [q for q in items if q["examId"] == "N2-MOCK-02"]

    batches = {
        "m01_s1_p1": [q for q in m01 if q["section"] == 1][:38],
        "m01_s1_p2": [q for q in m01 if q["section"] == 1][38:],
        "m01_s2": [q for q in m01 if q["section"] == 2],
        "m02_s1_p1": [q for q in m02 if q["section"] == 1][:38],
        "m02_s1_p2": [q for q in m02 if q["section"] == 1][38:],
        "m02_s2": [q for q in m02 if q["section"] == 2],
    }

    for name, batch_items in batches.items():
        out_file = ROOT / f"qa/blind_items_{name}.json"
        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(batch_items, f, ensure_ascii=False, indent=2)
        print(f"Created {out_file.name} with {len(batch_items)} items.")

if __name__ == "__main__":
    split_blind_items()
