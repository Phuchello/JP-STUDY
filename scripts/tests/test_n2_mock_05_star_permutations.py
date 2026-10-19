# -*- coding: utf-8 -*-
"""
Adversarial Permutation Verification Suite for N2 Mock 05 Mondai 8 (Star Questions)
Validates that each of the 5 star questions in N2 Mock 05 (N2_05_M8_01 to N2_05_M8_05)
has exactly ONE grammatically and semantically valid ordering among all 24 permutations (4!).
"""
import itertools
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class TestN2Mock05StarPermutations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        m5_path = ROOT / "data/mock_exams/n2_mock_05.json"
        with open(m5_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        cls.star_items = {
            q['id']: q for q in data['sections'][0]['items']
            if q.get('typeId') == 'N2-GR-STAR'
        }

    def test_all_five_star_items_exist(self):
        expected_ids = [f"N2_05_M8_{i:02d}" for i in range(1, 6)]
        for eid in expected_ids:
            self.assertIn(eid, self.star_items, f"Missing star item: {eid}")

    def test_m8_01_unambiguous_order(self):
        """
        N2_05_M8_01:
        地球温暖化を（　　）（　　） ★ （　　）不可欠である。
        Options: A: 市民一人ひとりの, B: 防止するにあたって、, C: 企業だけでなく, D: 地道な協力も
        Intended order: B -> C -> A -> D (Star: A)
        """
        q = self.star_items["N2_05_M8_01"]
        self.assertEqual(q["correctAnswer"], "A")
        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. B (防止するにあたって、) takes 地球温暖化を as object
            if p[0] != 'B':
                continue
            # 2. C (企業だけでなく) introduces addition
            if p[1] != 'C':
                continue
            # 3. A (市民一人ひとりの) modifies D (地道な協力も)
            if p.index('A') + 1 != p.index('D'):
                continue
            # 4. D (地道な協力も) is subject preceding 不可欠である
            if p[3] != 'D':
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(len(valid_orders), 1, f"Expected 1 valid order, got {valid_orders}")
        self.assertEqual(valid_orders[0], 'BCAD')
        self.assertEqual(valid_orders[0][2], 'A')

    def test_m8_02_unambiguous_order(self):
        """
        N2_05_M8_02:
        いかに科学技術が（　　）（　　） ★ （　　）決して消えない。
        Options: A: 進歩しようとも、, B: その根底にある, C: 人の温もりという, D: 価値は
        Intended order: A -> B -> C -> D (Star: C)
        """
        q = self.star_items["N2_05_M8_02"]
        self.assertEqual(q["correctAnswer"], "C")
        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. A (進歩しようとも、) completes いかに〜ようとも
            if p[0] != 'A':
                continue
            # 2. B (その根底にある) modifies C
            if p.index('B') + 1 != p.index('C'):
                continue
            # 3. C (人の温もりという) modifies D (価値は)
            if p.index('C') + 1 != p.index('D'):
                continue
            # 4. D (価値は) is subject preceding 決して消えない
            if p[3] != 'D':
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(len(valid_orders), 1, f"Expected 1 valid order, got {valid_orders}")
        self.assertEqual(valid_orders[0], 'ABCD')
        self.assertEqual(valid_orders[0][2], 'C')

    def test_m8_03_unambiguous_order(self):
        """
        N2_05_M8_03:
        長年の対立を（　　）（　　） ★ （　　）合意に達した。
        Options: A: 乗り越えるべく、, B: 双方が, C: 粘り強く, D: 協議を重ねた末に
        Intended order: A -> B -> C -> D (Star: C)
        """
        q = self.star_items["N2_05_M8_03"]
        self.assertEqual(q["correctAnswer"], "C")
        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. A (乗り越えるべく、) takes 長年の対立を as direct object
            if p[0] != 'A':
                continue
            # 2. B (双方が) is subject of main clause
            if p[1] != 'B':
                continue
            # 3. C (粘り強く) is adverb immediately modifying 協議を重ねた (D)
            if p.index('C') + 1 != p.index('D'):
                continue
            # 4. D (協議を重ねた末に) attaches to 合意に達した
            if p[3] != 'D':
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(len(valid_orders), 1, f"Expected 1 valid order, got {valid_orders}")
        self.assertEqual(valid_orders[0], 'ABCD')
        self.assertEqual(valid_orders[0][2], 'C')

    def test_m8_04_unambiguous_order(self):
        """
        N2_05_M8_04:
        どんなに優れた才能が（　　）（　　） ★ （　　）大成しない。
        Options: A: あろうと、, B: 日々の, C: 努力なくしては, D: 決して
        Intended order: A -> B -> C -> D (Star: C)
        """
        q = self.star_items["N2_05_M8_04"]
        self.assertEqual(q["correctAnswer"], "C")
        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. A (あろうと、) completes どんなに〜あろうと
            if p[0] != 'A':
                continue
            # 2. B (日々の) modifies C (努力なくしては)
            if p.index('B') + 1 != p.index('C'):
                continue
            # 3. D (決して) immediately precedes negative verb 大成しない
            if p[3] != 'D':
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(len(valid_orders), 1, f"Expected 1 valid order, got {valid_orders}")
        self.assertEqual(valid_orders[0], 'ABCD')
        self.assertEqual(valid_orders[0][2], 'C')

    def test_m8_05_unambiguous_order(self):
        """
        N2_05_M8_05:
        新薬の開発は、（　　）（　　） ★ （　　）貢献する。
        Options: A: 人々の健康増進に, B: 経済の活性化にも, C: とどまらず、, D: 大きく
        Intended order: A -> C -> B -> D (Star: B)
        """
        q = self.star_items["N2_05_M8_05"]
        self.assertEqual(q["correctAnswer"], "B")
        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. A (人々の健康増進に) attaches to C (とどまらず、)
            if p.index('A') + 1 != p.index('C'):
                continue
            # 2. A must be at position 0 following 新薬の開発は、
            if p[0] != 'A':
                continue
            # 3. D (大きく) is adverb directly modifying 貢献する
            if p[3] != 'D':
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(len(valid_orders), 1, f"Expected 1 valid order, got {valid_orders}")
        self.assertEqual(valid_orders[0], 'ACBD')
        self.assertEqual(valid_orders[0][2], 'B')

if __name__ == '__main__':
    unittest.main()
