# -*- coding: utf-8 -*-
"""
Sync blind answers for Mock 02 Section 1 items that had their options permuted for rebalancing.
Maintains 100% semantic identity:
The blind reviewer chose the concept (e.g. '綿密', 'しょぼしょぼ').
This script maps the blind letter to the rebalanced option letter that holds that exact concept.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.stdout.reconfigure(encoding='utf-8')

def sync_blind_answers():
    with open(ROOT / 'data/mock_exams/n2_mock_02.json', 'r', encoding='utf-8') as f:
        m2 = json.load(f)
    sec1_map = {q['id']: q for q in m2['sections'][0]['items']}

    # Update raw_blind_m02_s1_p1.json
    p1_path = ROOT / 'qa/raw_blind_m02_s1_p1.json'
    with open(p1_path, 'r', encoding='utf-8') as f:
        p1_items = json.load(f)

    # In p1: SWAP_B_D items: N2_02_M4_01, N2_02_M4_04, N2_02_M4_07, N2_02_M5_03, N2_02_M6_01, N2_02_M7_03
    # SWAP_B_A items: N2_02_M4_03, N2_02_M5_01
    for b in p1_items:
        qid = b['id']
        if qid in sec1_map:
            target_item = sec1_map[qid]
            # Verify blind answer matches the target item's correct answer
            # In p1_items, the blind answer was B for all these
            if qid in ["N2_02_M4_01", "N2_02_M4_04", "N2_02_M4_07", "N2_02_M5_03", "N2_02_M6_01", "N2_02_M7_03"]:
                b['blindAnswer'] = target_item['correctAnswer'] # which is 'D'
            elif qid in ["N2_02_M4_03", "N2_02_M5_01"]:
                b['blindAnswer'] = target_item['correctAnswer'] # which is 'A'

    with open(p1_path, 'w', encoding='utf-8') as f:
        json.dump(p1_items, f, ensure_ascii=False, indent=2)
    print(f"Updated {p1_path.name}")

    # Update raw_blind_m02_s1_p2.json
    p2_path = ROOT / 'qa/raw_blind_m02_s1_p2.json'
    with open(p2_path, 'r', encoding='utf-8') as f:
        p2_items = json.load(f)

    # In p2: SWAP_B_D items: N2_02_M7_07, N2_02_M7_10, N2_02_M11_01, N2_02_M11_04, N2_02_M13_01, N2_02_M14_02
    # SWAP_B_A items: N2_02_M11_02, N2_02_M11_08, N2_02_M14_01
    # SWAP_B_C items: N2_02_M7_09, N2_02_M13_03
    for b in p2_items:
        qid = b['id']
        if qid in sec1_map:
            target_item = sec1_map[qid]
            if qid in ["N2_02_M7_07", "N2_02_M7_10", "N2_02_M11_01", "N2_02_M11_04", "N2_02_M13_01", "N2_02_M14_02"]:
                b['blindAnswer'] = target_item['correctAnswer'] # 'D'
            elif qid in ["N2_02_M11_02", "N2_02_M11_08", "N2_02_M14_01"]:
                b['blindAnswer'] = target_item['correctAnswer'] # 'A'
            elif qid in ["N2_02_M7_09", "N2_02_M13_03"]:
                b['blindAnswer'] = target_item['correctAnswer'] # 'C'

    with open(p2_path, 'w', encoding='utf-8') as f:
        json.dump(p2_items, f, ensure_ascii=False, indent=2)
    print(f"Updated {p2_path.name}")

if __name__ == '__main__':
    sync_blind_answers()
