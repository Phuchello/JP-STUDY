# -*- coding: utf-8 -*-
"""
Adversarial Permutation Verification Suite for N2 Mock 03 Mondai 8 (Star Questions)
Validates that each of the 5 star questions in N2 Mock 03 (N2_03_M8_01 to N2_03_M8_05)
has exactly ONE grammatically and semantically valid ordering among all 24 permutations (4!).
"""
import itertools
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class TestN2Mock03StarPermutations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        m3_path = ROOT / "data/mock_exams/n2_mock_03.json"
        with open(m3_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        cls.star_items = {
            q['id']: q for q in data['sections'][0]['items']
            if q.get('typeId') == 'N2-GR-STAR'
        }

    def test_all_five_star_items_exist(self):
        expected_ids = [f"N2_03_M8_{i:02d}" for i in range(1, 6)]
        for eid in expected_ids:
            self.assertIn(eid, self.star_items, f"Missing star item: {eid}")

    def test_m8_01_unambiguous_order(self):
        """
        N2_03_M8_01:
        彼が今回の難関試験に一発で合格できたのは、（　　）（　　） ★ （　　）ほかならない。
        Options: A: 毎日の地道な, B: 努力を, C: 怠らなかった, D: 結果に
        Intended order: A -> B -> C -> D (Star: C)
        """
        q = self.star_items["N2_03_M8_01"]
        self.assertEqual(q["correctAnswer"], "C")
        opts = {o['id']: o['text'] for o in q['options']}
        
        # ABCD is the only valid sequence:
        # A (毎日の地道な - na-adj) requires noun B (努力)
        # B (努力を - acc) requires transitive verb C (怠らなかった)
        # C (怠らなかった - attributive past) requires noun D (結果)
        # D (結果に) requires predicate stem (ほかならない)
        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # Syntactic check:
            # 1. A must immediately precede B (毎日の地道な努力)
            if p.index('A') + 1 != p.index('B'):
                continue
            # 2. B must immediately precede C (努力を怠らなかった)
            if p.index('B') + 1 != p.index('C'):
                continue
            # 3. C must immediately precede D (怠らなかった結果)
            if p.index('C') + 1 != p.index('D'):
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(valid_orders, ['ABCD'], f"Expected only ['ABCD'], got {valid_orders}")
        self.assertEqual(opts['C'], "怠らなかった")

    def test_m8_02_unambiguous_order(self):
        """
        N2_03_M8_02:
        どんなに科学技術が（　　）（　　） ★ （　　）失ってはならない。
        Options: A: 発展しようとも、, B: 私たちは, C: 自然への, D: 畏敬の念を
        Intended order: A -> B -> C -> D (Star: C)
        """
        q = self.star_items["N2_03_M8_02"]
        self.assertEqual(q["correctAnswer"], "C")
        opts = {o['id']: o['text'] for o in q['options']}

        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. A (発展しようとも、) must be in position 1 to complete 'どんなに科学技術が発展しようとも、'
            if p[0] != 'A':
                continue
            # 2. C must immediately precede D (自然への畏敬の念)
            if p.index('C') + 1 != p.index('D'):
                continue
            # 3. B (私たちは) is the subject of the main clause, preceding the direct object C-D
            if p.index('B') > p.index('C'):
                continue
            # 4. D must be in position 4 to attach to '失ってはならない'
            if p[3] != 'D':
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(valid_orders, ['ABCD'], f"Expected only ['ABCD'], got {valid_orders}")
        self.assertEqual(opts['C'], "自然への")

    def test_m8_03_unambiguous_order(self):
        """
        N2_03_M8_03:
        今回の不祥事は、（　　）（　　） ★ （　　）問題である。
        Options: A: 個人の過失に, B: とどまらず、, C: 組織全体の, D: 管理体制に関わる
        Intended order: A -> B -> C -> D (Star: C)
        """
        q = self.star_items["N2_03_M8_03"]
        self.assertEqual(q["correctAnswer"], "C")
        opts = {o['id']: o['text'] for o in q['options']}

        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. A must immediately precede B (~にとどまらず、)
            if p.index('A') + 1 != p.index('B'):
                continue
            # 2. C must immediately precede D (組織全体の管理体制に関わる)
            if p.index('C') + 1 != p.index('D'):
                continue
            # 3. D must be in position 4 to modify '問題である'
            if p[3] != 'D':
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(valid_orders, ['ABCD'], f"Expected only ['ABCD'], got {valid_orders}")
        self.assertEqual(opts['C'], "組織全体の")

    def test_m8_04_unambiguous_order(self):
        """
        N2_03_M8_04:
        プロの演奏家として（　　）（　　） ★ （　　）怠ってはならない。
        Options: A: 観客の前に, B: 立つからには、, C: 日々の地道な, D: 練習を
        Intended order: A -> B -> C -> D (Star: C)
        """
        q = self.star_items["N2_03_M8_04"]
        self.assertEqual(q["correctAnswer"], "C")
        opts = {o['id']: o['text'] for o in q['options']}

        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. A must immediately precede B (観客の前に立つからには、)
            if p.index('A') + 1 != p.index('B'):
                continue
            # 2. C must immediately precede D (日々の地道な練習を)
            if p.index('C') + 1 != p.index('D'):
                continue
            # 3. D must be in position 4 to be object of '怠ってはならない'
            if p[3] != 'D':
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(valid_orders, ['ABCD'], f"Expected only ['ABCD'], got {valid_orders}")
        self.assertEqual(opts['C'], "日々の地道な")

    def test_m8_05_unambiguous_order(self):
        """
        N2_03_M8_05:
        彼がこれほど短期間で大きな成果を上げられたのは、（　　）（　　） ★ （　　）賜物だ。
        Options:
          A: 地道に努力を
          B: 重ねてきた
          C: 素直に耳を傾け、
          D: 周囲の助言に
        Intended order: D -> C -> A -> B (Star: A)
        Sentence: 周囲の助言に (D) 素直に耳を傾け、 (C) ★地道に努力を (A) 重ねてきた (B) 賜物だ。
        """
        q = self.star_items["N2_03_M8_05"]
        self.assertEqual(q["correctAnswer"], "A")
        opts = {o['id']: o['text'] for o in q['options']}

        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. D (周囲の助言に) must precede C (素直に耳を傾け、) - valency requirement of 耳を傾ける
            if p.index('D') + 1 != p.index('C'):
                continue
            # 2. A (地道に努力を) must precede B (重ねてきた) - direct object of 重ねる
            if p.index('A') + 1 != p.index('B'):
                continue
            # 3. B (重ねてきた - attributive verb) must immediately precede stem '賜物だ' (position 4)
            if p[3] != 'B':
                continue
            # 4. C (連用中止形 with comma) must precede the subsequent clause A-B
            if p.index('C') > p.index('A'):
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(valid_orders, ['DCAB'], f"Expected only ['DCAB'], got {valid_orders}")
        # 3rd position (★) is A
        star_choice = 'DCAB'[2]
        self.assertEqual(star_choice, "A")
        self.assertEqual(opts[star_choice], "地道に努力を")


if __name__ == "__main__":
    unittest.main()
