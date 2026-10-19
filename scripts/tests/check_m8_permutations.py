# -*- coding: utf-8 -*-
import sys
import itertools

sys.stdout.reconfigure(encoding='utf-8')

items = [
    {
        'id': 'N2_03_M8_01',
        'stem_pre': '彼が今回の難関試験に一発で合格できたのは、',
        'stem_post': 'ほかならない。',
        'chunks': {'A': '毎日の地道な', 'B': '努力を', 'C': '怠らなかった', 'D': '結果に'},
        'intended': 'ABCD',
        'star_pos': 3 # 1-based
    },
    {
        'id': 'N2_03_M8_02',
        'stem_pre': 'どんなに科学技術が',
        'stem_post': '失ってはならない。',
        'chunks': {'A': '発展しようとも、', 'B': '私たちは', 'C': '自然への', 'D': '畏敬の念を'},
        'intended': 'ABCD',
        'star_pos': 3
    },
    {
        'id': 'N2_03_M8_03',
        'stem_pre': '今回の不祥事は、',
        'stem_post': '問題である。',
        'chunks': {'A': '個人の過失に', 'B': 'とどまらず、', 'C': '組織全体の', 'D': '管理体制に関わる'},
        'intended': 'ABCD',
        'star_pos': 3
    },
    {
        'id': 'N2_03_M8_04',
        'stem_pre': 'プロの演奏家として',
        'stem_post': '怠ってはならない。',
        'chunks': {'A': '観客の前に', 'B': '立つからには、', 'C': '日々の地道な', 'D': '練習を'},
        'intended': 'ABCD',
        'star_pos': 3
    },
    {
        'id': 'N2_03_M8_05',
        'stem_pre': '彼がこれほど短期間で',
        'stem_post': '努力の賜物だ。',
        'chunks': {'A': '大きな成果を上げられたのは、', 'B': '誰よりも', 'C': '真摯に積み重ねた', 'D': '本人の'},
        'intended': 'ADBC',
        'star_pos': 3
    }
]

def analyze_permutations(stem_pre, chunks, stem_post):
    results = []
    for p in itertools.permutations(['A', 'B', 'C', 'D']):
        p_str = ''.join(p)
        sent = stem_pre + ''.join(chunks[k] for k in p) + stem_post
        star = p[2]
        results.append((p_str, star, sent))
    return results

print("--- CANDIDATE 3 ---")
c3_chunks = {
    'A': '周囲の助言に',
    'B': '素直に耳を傾け、',
    'C': '地道に努力を',
    'D': '重ねてきた'
}
cand3_stem_pre = '彼がこれほど短期間で大きな成果を上げられたのは、'
cand3_stem_post = '賜物だ。'
for p_str, star, sent in analyze_permutations(cand3_stem_pre, c3_chunks, cand3_stem_post):
    if p_str in ['ABCD', 'BACD', 'CABD', 'ACBD']:
        print(f"{p_str} (Star: {star}): {sent}")
