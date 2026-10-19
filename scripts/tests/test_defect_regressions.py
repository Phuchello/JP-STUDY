# -*- coding: utf-8 -*-
"""
Regression tests for confirmed grammatical defects:
- DEFECT A: N2_02_M7_05 (理解しがたい vs *理解がたい)
- DEFECT B: N2_02_M7_04 (職人ならではの技 vs *職人ならでは可能だ)
Ensures that the defective versions are rejected and the repaired versions are structurally
and grammatically sound with unambiguous distractor behavior.
"""
import unittest
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class TestDefectRegressions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mock_file = ROOT / "data/mock_exams/n2_mock_02.json"
        with open(mock_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        cls.sec1_items = {q['id']: q for q in data['sections'][0]['items']}

        mock_file_01 = ROOT / "data/mock_exams/n2_mock_01.json"
        with open(mock_file_01, 'r', encoding='utf-8') as f:
            data_01 = json.load(f)
        cls.m01_sec1_items = {q['id']: q for q in data_01['sections'][0]['items']}

    def test_defect_a_m7_05_repaired(self):
        """DEFECT A: N2_02_M7_05 must require '理解し' stem and reject bare '理解'."""
        self.assertIn('N2_02_M7_05', self.sec1_items)
        q = self.sec1_items['N2_02_M7_05']

        # 1. Stem must have '理解し' before the blank
        self.assertIn("理解し（　　）ものだった", q['stem'],
                      "Stem must have '理解し' (ren'yokei) to attach grammatically to 'がたい'")
        self.assertNotIn("理解（　　）ものだった", q['stem'],
                         "Defective stem with uninflected '理解（　　）' must not be present")

        # 2. Correct answer is C ('がたい')
        self.assertEqual(q['correctAnswer'], 'C')
        opts = {o['id']: o['text'] for o in q['options']}
        self.assertEqual(opts['C'], 'がたい')

        # 3. Assembled correct form
        correct_phrase = "理解し" + opts['C'] + "ものだった"
        self.assertEqual(correct_phrase, "理解しがたいものだった")

        # 4. Verify distractors
        self.assertIn('A', q['distractorExplanations'])
        self.assertIn('B', q['distractorExplanations'])
        self.assertIn('D', q['distractorExplanations'])

    def test_defect_b_m7_04_repaired(self):
        """DEFECT B: N2_02_M7_04 must use 'ならではの技' construction and reject '*ならでは可能だ'."""
        self.assertIn('N2_02_M7_04', self.sec1_items)
        q = self.sec1_items['N2_02_M7_04']

        # 1. Stem must have 'ならではの技だ' pattern
        self.assertIn("（　　）の技だ", q['stem'],
                      "Stem must use the noun-modifying 'ならではの' pattern")
        self.assertNotIn("（　　）可能だ", q['stem'],
                         "Defective stem with '*ならでは可能だ' must not be present")

        # 2. Correct answer is B ('ならでは')
        self.assertEqual(q['correctAnswer'], 'B')
        opts = {o['id']: o['text'] for o in q['options']}
        self.assertEqual(opts['B'], 'ならでは')

        # 3. Assembled correct form
        correct_phrase = "熟練の職人" + opts['B'] + "の技だ"
        self.assertEqual(correct_phrase, "熟練の職人ならではの技だ")

        # 4. Verify distractors
        self.assertIn('A', q['distractorExplanations'])
        self.assertIn('C', q['distractorExplanations'])
        self.assertIn('D', q['distractorExplanations'])

    def test_defect_c_g7_004_repaired(self):
        """KEY DEFECT: N2-G7-004 must have correct key 'C' ('のみならず') and reject defective 'D' ('どころか')."""
        self.assertIn('N2-G7-004', self.m01_sec1_items)
        q = self.m01_sec1_items['N2-G7-004']

        # 1. Key must be C ('のみならず')
        self.assertEqual(q['correctAnswer'], 'C', "Correct answer must be 'C' (のみならず), not defective 'D' (どころか)")
        opts = {o['id']: o['text'] for o in q['options']}
        self.assertEqual(opts['C'], 'のみならず')

        # 2. Ambiguous distractor 'どころか' replaced with unambiguous 'を契機に'
        self.assertEqual(opts['D'], 'を契機に')
        self.assertNotIn('どころか', opts.values())
        self.assertIn("を契機に", q['distractorExplanations']['D'])

        # 3. Distractor A must be '反面' to eliminate duplicate distractor overlap with 'ばかりか'
        self.assertEqual(opts['A'], '反面')
        self.assertNotIn('ばかりか', opts.values())

        # 4. Assembled correct form
        self.assertIn("英語のみならず", q['explanationVi'])

if __name__ == '__main__':
    unittest.main()

