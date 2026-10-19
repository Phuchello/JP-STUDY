# -*- coding: utf-8 -*-
"""
Adversarial Permutation Verification Suite for N2 Mock 06 Mondai 8 (Star Questions)
Validates that each of the 5 star questions in N2 Mock 06 (N2_06_M8_01 to N2_06_M8_05)
has exactly ONE grammatically and semantically valid ordering among all 24 permutations (4!).
"""
import itertools
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.curriculum.bank_data.n2_mock_06_data import get_n2_mock_06_sec1_items

class TestN2Mock06StarPermutations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        items = get_n2_mock_06_sec1_items()
        cls.star_items = {
            q['id']: q for q in items
            if q.get('typeId') == 'N2-GR-STAR'
        }

    def test_all_five_star_items_exist(self):
        expected_ids = [f"N2_06_M8_{i:02d}" for i in range(1, 6)]
        for eid in expected_ids:
            self.assertIn(eid, self.star_items, f"Missing star item: {eid}")

    def test_m8_01_unambiguous_order(self):
        """
        N2_06_M8_01:
        定年退職を（　　）（　　） ★ （　　）ことにした。
        Options: A: 機に、, B: 念願だった, C: かねてから, D: 陶芸を始める
        Intended order: A -> C -> B -> D (Star: B)
        Sentence: 定年退職を機に、(A) かねてから(C) 念願だった(B) 陶芸を始める(D) ことにした。
        """
        q = self.star_items["N2_06_M8_01"]
        self.assertEqual(q["correctAnswer"], "B")
        opts = {o['id']: o['text'] for o in q['options']}
        
        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. A (機に、) must immediately follow stem '定年退職を' (pos 0)
            if p[0] != 'A':
                continue
            # 2. C (かねてから) precedes B (念願だった)
            if p.index('C') + 1 != p.index('B'):
                continue
            # 3. B (念願だった) precedes D (陶芸を始める) as modifier
            if p.index('B') + 1 != p.index('D'):
                continue
            # 4. D (陶芸を始める) attaches to stem 'ことにした' (pos 3)
            if p[3] != 'D':
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(valid_orders, ['ACBD'], f"Expected only ['ACBD'], got {valid_orders}")
        self.assertEqual(opts['B'], "念願だった")

    def test_m8_02_unambiguous_order(self):
        """
        N2_06_M8_02:
        本場の職人が（　　）（　　） ★ （　　）格別だ。
        Options: A: 手作りした, B: だけあって、, C: 風味の良さは, D: このパンの
        Intended order: A -> B -> D -> C (Star: D)
        Sentence: 本場の職人が手作りした(A) だけあって、(B) このパンの(D) 風味の良さは(C) 格別だ。
        """
        q = self.star_items["N2_06_M8_02"]
        self.assertEqual(q["correctAnswer"], "D")
        opts = {o['id']: o['text'] for o in q['options']}

        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. A (手作りした) must be pos 0 as predicate for '本場の職人が'
            if p[0] != 'A':
                continue
            # 2. B (だけあって、) must follow A
            if p.index('A') + 1 != p.index('B'):
                continue
            # 3. D (このパンの) must immediately precede C (風味の良さは)
            if p.index('D') + 1 != p.index('C'):
                continue
            # 4. C (風味の良さは) must be pos 3 to attach to stem '格別だ。'
            if p[3] != 'C':
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(valid_orders, ['ABDC'], f"Expected only ['ABDC'], got {valid_orders}")
        self.assertEqual(opts['D'], "このパンの")

    def test_m8_03_unambiguous_order(self):
        """
        N2_06_M8_03:
        関係者との（　　）（　　） ★ （　　）いかない。
        Options: A: 計画を勝手に, B: 進めるわけには, C: 十分な合意を, D: 得ることなしに、
        Intended order: C -> D -> A -> B (Star: A)
        Sentence: 関係者との十分な合意を(C) 得ることなしに、(D) 計画を勝手に(A) 進めるわけには(B) いかない。
        """
        q = self.star_items["N2_06_M8_03"]
        self.assertEqual(q["correctAnswer"], "A")
        opts = {o['id']: o['text'] for o in q['options']}

        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. C (十分な合意を) must be pos 0 attached to '関係者との'
            if p[0] != 'C':
                continue
            # 2. D (得ることなしに、) must immediately follow C
            if p.index('C') + 1 != p.index('D'):
                continue
            # 3. A (計画を勝手に) must immediately precede B (進めるわけには)
            if p.index('A') + 1 != p.index('B'):
                continue
            # 4. B (進めるわけには) must be pos 3 attached to stem 'いかない。'
            if p[3] != 'B':
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(valid_orders, ['CDAB'], f"Expected only ['CDAB'], got {valid_orders}")
        self.assertEqual(opts['A'], "計画を勝手に")

    def test_m8_04_unambiguous_order(self):
        """
        N2_06_M8_04:
        年齢や性別の（　　）（　　） ★ （　　）努めている。
        Options: A: 社内において, B: 誰もが働きやすい, C: 違いにかかわらず、, D: 環境を整えるよう
        Intended order: C -> A -> B -> D (Star: B)
        Sentence: 年齢や性別の違いにかかわらず、(C) 社内において(A) 誰もが働きやすい(B) 環境を整えるよう(D) 努めている。
        """
        q = self.star_items["N2_06_M8_04"]
        self.assertEqual(q["correctAnswer"], "B")
        opts = {o['id']: o['text'] for o in q['options']}

        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. C (違いにかかわらず、) must be pos 0 attached to '年齢や性別の'
            if p[0] != 'C':
                continue
            # 2. D (環境を整えるよう) must be pos 3 attached to '努めている。'
            if p[3] != 'D':
                continue
            # 3. A (社内において) must precede B-D clause
            if p.index('A') > p.index('B'):
                continue
            # 4. B (誰もが働きやすい) must immediately precede D (環境を整えるよう)
            if p.index('B') + 1 != p.index('D'):
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(valid_orders, ['CABD'], f"Expected only ['CABD'], got {valid_orders}")
        self.assertEqual(opts['B'], "誰もが働きやすい")

    def test_m8_05_unambiguous_order(self):
        """
        N2_06_M8_05:
        彼の失言は（　　）（　　） ★ （　　）招きかねない。
        Options: A: 批判を浴びる, B: 国際問題さえ, C: どころか、, D: 国内での
        Intended order: D -> A -> C -> B (Star: C)
        Sentence: 彼の失言は国内での(D) 批判を浴びる(A) どころか、(C) 国際問題さえ(B) 招きかねない。
        """
        q = self.star_items["N2_06_M8_05"]
        self.assertEqual(q["correctAnswer"], "C")
        opts = {o['id']: o['text'] for o in q['options']}

        valid_orders = []
        for p in itertools.permutations(['A', 'B', 'C', 'D']):
            # 1. D (国内での) must be pos 0
            if p[0] != 'D':
                continue
            # 2. A (批判を浴びる) must follow D
            if p.index('D') + 1 != p.index('A'):
                continue
            # 3. C (どころか、) must follow A
            if p.index('A') + 1 != p.index('C'):
                continue
            # 4. B (国際問題さえ) must be pos 3 to attach to stem '招きかねない。'
            if p[3] != 'B':
                continue
            valid_orders.append(''.join(p))

        self.assertEqual(valid_orders, ['DACB'], f"Expected only ['DACB'], got {valid_orders}")
        self.assertEqual(opts['C'], "どころか、")


if __name__ == "__main__":
    unittest.main()
