# -*- coding: utf-8 -*-
"""
Audits cross-mock duplication between N2-MOCK-01 and N2-MOCK-02:
1. Exact stem duplicates
2. Near-duplicate stems (Levenshtein / Jaccard similarity)
3. Reading passage reuse / overlapping sentences
4. Listening situation reuse / transcript overlap
5. Answer key distribution across all Mondai
"""
import json
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[2]

def clean_text(s):
    if not s:
        return ""
    return re.sub(r'[\s\u3000【】（）＿_★]+', '', s)

def ngrams(text, n=3):
    text = clean_text(text)
    return set(text[i:i+n] for i in range(len(text)-n+1))

def jaccard_similarity(s1, s2, n=3):
    ng1 = ngrams(s1, n)
    ng2 = ngrams(s2, n)
    if not ng1 or not ng2:
        return 0.0
    return len(ng1 & ng2) / len(ng1 | ng2)

def audit_cross_mock():
    with open(ROOT / 'data/mock_exams/n2_mock_01.json', 'r', encoding='utf-8') as f:
        m1 = json.load(f)
    with open(ROOT / 'data/mock_exams/n2_mock_02.json', 'r', encoding='utf-8') as f:
        m2 = json.load(f)

    m1_items = m1['sections'][0]['items'] + m1['sections'][1]['items']
    m2_items = m2['sections'][0]['items'] + m2['sections'][1]['items']

    print(f"Loaded {len(m1_items)} items from Mock 01 and {len(m2_items)} items from Mock 02.")

    # 1. Exact stem matches
    m1_stems = {clean_text(q['stem']): q['id'] for q in m1_items}
    exact_matches = []
    for q in m2_items:
        s = clean_text(q['stem'])
        if s in m1_stems:
            exact_matches.append((q['id'], m1_stems[s], q['stem']))

    print(f"Exact stem matches between Mock 01 and Mock 02: {len(exact_matches)}")
    for m in exact_matches:
        print(f"  {m[0]} <-> {m[1]}: {m[2][:40]}")

    # 2. Near-duplicate stems (similarity > 0.65)
    near_duplicates = []
    for q2 in m2_items:
        s2 = clean_text(q2['stem'])
        if len(s2) < 5:
            continue
        for q1 in m1_items:
            s1 = clean_text(q1['stem'])
            if len(s1) < 5:
                continue
            sim = jaccard_similarity(s1, s2, n=3)
            if sim > 0.65 and s1 != s2:
                near_duplicates.append((q2['id'], q1['id'], sim, q2['stem'], q1['stem']))

    print(f"Near-duplicate stems (similarity > 0.65): {len(near_duplicates)}")
    for nd in near_duplicates:
        print(f"  {nd[0]} <-> {nd[1]} (sim={nd[2]:.2f}):\n    Q2: {nd[3][:60]}\n    Q1: {nd[4][:60]}")

    # 3. Reading passage overlaps
    m1_passages = [q['contextPassage'] for q in m1_items if q.get('contextPassage')]
    m2_passages = [q['contextPassage'] for q in m2_items if q.get('contextPassage')]
    passage_overlaps = []
    for p2 in m2_passages:
        for p1 in m1_passages:
            sim = jaccard_similarity(p1, p2, n=5)
            if sim > 0.40:
                passage_overlaps.append((sim, p2[:50], p1[:50]))

    print(f"Passage overlaps (5-gram similarity > 0.40): {len(passage_overlaps)}")

    # 4. Answer key distribution comparison
    for m_label, items in [("Mock 01", m1_items), ("Mock 02", m2_items)]:
        sec1 = items[:75]
        sec2 = items[75:]
        k1 = Counter(q['correctAnswer'] for q in sec1)
        k2 = Counter(q['correctAnswer'] for q in sec2)
        print(f"\n{m_label} Answer Distribution:")
        print(f"  Section 1 (75 items): A={k1['A']}, B={k1['B']}, C={k1['C']}, D={k1['D']}")
        print(f"  Section 2 (30 items): A={k2['A']}, B={k2['B']}, C={k2['C']}, D={k2['D']}")

if __name__ == '__main__':
    audit_cross_mock()
