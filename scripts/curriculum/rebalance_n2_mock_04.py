# -*- coding: utf-8 -*-
"""
JP-STUDY: N2-MOCK-04 Section 1 Answer Key Rebalancing Utility
Safely removes option-position bias (59/75 'A') without altering semantic correctness.
Preserves:
  - Exact question IDs
  - Exact correct answer text and distractor texts
  - Correct distractor explanation mapping to permuted letters
  - Unmodified star questions (Mondai 8)
Produces balanced target distribution:
  A: 19, B: 19, C: 19, D: 18 (Total: 75)
"""
import json
import copy
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOCK_04_PATH = ROOT / "data/mock_exams/n2_mock_04.json"
RECORD_PATH = ROOT / "qa/N2_MOCK_04_REBALANCING_RECORD.json"

def rebalance_item(item, target_new_letter):
    """
    Permutes options of item so that the correct answer moves to target_new_letter.
    Swaps the option at target_new_letter with the option at current correct letter.
    Remaps distractorExplanations to follow the moved texts.
    """
    orig_key = item['correctAnswer']
    if orig_key == target_new_letter:
        return item, False, None

    orig_options = {o['id']: o['text'] for o in item['options']}
    correct_text = orig_options[orig_key]
    swap_distractor_text = orig_options[target_new_letter]

    orig_dist_exp = copy.deepcopy(item.get('distractorExplanations', {}))

    # Construct new options
    new_options = []
    for o in item['options']:
        lid = o['id']
        if lid == target_new_letter:
            new_options.append({"id": lid, "text": correct_text})
        elif lid == orig_key:
            new_options.append({"id": lid, "text": swap_distractor_text})
        else:
            new_options.append({"id": lid, "text": o['text']})

    # Remap distractorExplanations
    # The distractor that was at target_new_letter is now at orig_key
    new_dist_exp = {}
    for lid in ['A', 'B', 'C', 'D']:
        if lid == target_new_letter:
            continue # Correct answer has no distractor explanation
        elif lid == orig_key:
            # Took the explanation of the option previously at target_new_letter
            new_dist_exp[lid] = orig_dist_exp.get(target_new_letter, f"Giải thích cho phương án {lid}.")
        else:
            new_dist_exp[lid] = orig_dist_exp.get(lid, f"Giải thích cho phương án {lid}.")

    # Update letter references in distractor explanations if any
    for lid, exp_text in new_dist_exp.items():
        # Replace prefix if it had "X: " with new letter
        for old_l in ['A', 'B', 'C', 'D']:
            if exp_text.startswith(f"{old_l}: "):
                # If it had letter prefix, strip it or adjust
                exp_text = exp_text[3:]
                new_dist_exp[lid] = exp_text

    item_rebalanced = copy.deepcopy(item)
    item_rebalanced['options'] = new_options
    item_rebalanced['correctAnswer'] = target_new_letter
    item_rebalanced['distractorExplanations'] = new_dist_exp

    permutation_record = {
        "questionId": item['id'],
        "originalCorrectAnswer": orig_key,
        "newCorrectAnswer": target_new_letter,
        "correctText": correct_text,
        "swappedDistractorText": swap_distractor_text,
        "originalOptions": orig_options,
        "newOptions": {o['id']: o['text'] for o in new_options}
    }

    return item_rebalanced, True, permutation_record

def run_rebalance():
    assert MOCK_04_PATH.exists(), f"Missing mock 04 path: {MOCK_04_PATH}"
    with open(MOCK_04_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    sec1 = data['sections'][0]['items']
    before_counts = Counter(it['correctAnswer'] for it in sec1)

    # Star items: Q43 - Q47 (N2_04_M8_01 to N2_04_M8_05)
    star_ids = {f"N2_04_M8_{i:02d}" for i in range(1, 6)}

    # Target non-star allocations:
    # We need 11 more 'B', 12 more 'C', 17 more 'D' from items currently 'A'
    needed_b = 11
    needed_c = 12
    needed_d = 17

    permutations = []
    new_sec1 = []

    for it in sec1:
        qid = it['id']
        curr_key = it['correctAnswer']

        if qid in star_ids:
            # Preserve star questions exactly
            new_sec1.append(it)
            continue

        if curr_key == 'A':
            target_key = 'A'
            if needed_d > 0:
                target_key = 'D'
                needed_d -= 1
            elif needed_b > 0:
                target_key = 'B'
                needed_b -= 1
            elif needed_c > 0:
                target_key = 'C'
                needed_c -= 1
            
            rebalanced, changed, rec = rebalance_item(it, target_key)
            new_sec1.append(rebalanced)
            if changed:
                permutations.append(rec)
        else:
            new_sec1.append(it)

    data['sections'][0]['items'] = new_sec1
    after_counts = Counter(it['correctAnswer'] for it in new_sec1)

    with open(MOCK_04_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    with open(RECORD_PATH, 'w', encoding='utf-8') as f:
        json.dump({
            "totalItems": len(new_sec1),
            "beforeDistribution": before_counts,
            "afterDistribution": after_counts,
            "totalReordered": len(permutations),
            "reorderedItems": permutations
        }, f, ensure_ascii=False, indent=2)

    print("=== N2-MOCK-04 SECTION 1 REBALANCING COMPLETE ===")
    print(f"Before: {dict(before_counts)}")
    print(f"After:  {dict(after_counts)}")
    print(f"Total reordered: {len(permutations)}")

if __name__ == "__main__":
    run_rebalance()
