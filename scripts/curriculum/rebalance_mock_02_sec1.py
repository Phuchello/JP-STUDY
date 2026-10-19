# -*- coding: utf-8 -*-
"""
Rebalance Mock 02 Section 1 answer keys to eliminate author placement bias (35 B's and 6 D's).
Safely permutes option choices and re-maps distractor explanations with 100% semantic fidelity.
Does NOT touch Star questions (Mondai 8).
"""
import sys
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.curriculum.bank_data.n2_mock_02_data import get_n2_mock_02_sec1_items

# Items to swap B <-> D (move correct answer B to D)
SWAP_B_D = [
    "N2_02_M4_01",  # しょぼしょぼ
    "N2_02_M4_04",  # 綿密
    "N2_02_M4_07",  # 閉じ込め
    "N2_02_M5_03",  # 偶然に
    "N2_02_M6_01",  # 手薄
    "N2_02_M7_03",  # せざるを得ない
    "N2_02_M7_07",  # どころか
    "N2_02_M7_10",  # ご覧になりました
    "N2_02_M11_01", # 接合部がわずかに滑る
    "N2_02_M11_04", # 未知の体験が多く
    "N2_02_M13_01", # あらかじめ正解が決まっており
    "N2_02_M14_02", # 高度DX枠
]

# Items to swap B <-> A (move correct answer B to A)
SWAP_B_A = [
    "N2_02_M4_03",  # 大幅に
    "N2_02_M5_01",  # おおまかに
    "N2_02_M11_02", # 傷んだ部材だけを取り替える
    "N2_02_M11_08", # 信頼関係の土台を築き
    "N2_02_M14_01", # 市内に本社があり
]

# Items to swap B <-> C (move correct answer B to C)
SWAP_B_C = [
    "N2_02_M7_09",  # に応じて
    "N2_02_M13_03", # 予測困難な時代を乗り越えるには
]

def swap_options(item, opt1, opt2):
    orig_opts = {o['id']: o['text'] for o in item['options']}
    orig_dist = dict(item.get('distractorExplanations', {}))
    orig_key = item['correctAnswer']

    target_text = orig_opts[orig_key]

    # Swap option texts
    new_text_opt1 = orig_opts[opt2]
    new_text_opt2 = orig_opts[opt1]

    new_options = []
    for o in item['options']:
        if o['id'] == opt1:
            new_options.append({'id': opt1, 'text': new_text_opt1})
        elif o['id'] == opt2:
            new_options.append({'id': opt2, 'text': new_text_opt2})
        else:
            new_options.append(dict(o))

    # Determine new key
    if orig_key == opt1:
        new_key = opt2
    elif orig_key == opt2:
        new_key = opt1
    else:
        new_key = orig_key

    assert new_text_opt1 != new_text_opt2
    # Verify new key matches target text
    new_opts_map = {o['id']: o['text'] for o in new_options}
    assert new_opts_map[new_key] == target_text, f"Key mapping failed for {item['id']}"

    # Re-map distractor explanations
    # For any distractor, its explanation must match the text at that option
    new_dist = {}
    for oid, text in new_opts_map.items():
        if oid == new_key:
            continue
        # Find which old option had this text
        old_oid = [k for k, v in orig_opts.items() if v == text][0]
        if old_oid in orig_dist:
            new_dist[oid] = orig_dist[old_oid]
        else:
            print(f"Warning: no distractor explanation for {item['id']} text {text}")

    item['options'] = new_options
    item['correctAnswer'] = new_key
    item['distractorExplanations'] = new_dist
    return item

def rebalance_items():
    items = get_n2_mock_02_sec1_items()
    print(f"Loaded {len(items)} items from Mock 02 Section 1.")

    initial_c = Counter(q['correctAnswer'] for q in items)
    print(f"Initial keys: {dict(initial_c)}")

    for q in items:
        qid = q['id']
        if qid in SWAP_B_D:
            swap_options(q, 'B', 'D')
        elif qid in SWAP_B_A:
            swap_options(q, 'B', 'A')
        elif qid in SWAP_B_C:
            swap_options(q, 'B', 'C')

    final_c = Counter(q['correctAnswer'] for q in items)
    print(f"Rebalanced keys: {dict(final_c)}")

    # Verify every item
    for q in items:
        opts = [o['id'] for o in q['options']]
        assert opts == ['A', 'B', 'C', 'D'], f"Invalid option IDs in {q['id']}"
        assert q['correctAnswer'] in opts, f"Invalid key in {q['id']}"
        expected_dist = set(opts) - {q['correctAnswer']}
        assert set(q['distractorExplanations'].keys()) == expected_dist, f"Distractor keys mismatch in {q['id']}"

    print("All 75 items verified with perfect option and distractor integrity!")
    return items

if __name__ == '__main__':
    rebalance_items()
