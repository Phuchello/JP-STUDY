# -*- coding: utf-8 -*-
"""
JP-STUDY: Targeted Linguistic & Structural Regression Tests for N2-MOCK-06
Verifies the permanent remediation of the 4 flagged ambiguous questions:
  1. N2_06_M7_02: に先立ち vs に際して ambiguity resolved
  2. N2_06_M7_07: 終日運休を余儀なくされた vs 強いられた ambiguity resolved
  3. N2_06_M7_08: できっこない vs できそうもない ambiguity resolved
  4. N2_06_M9_04: 踏み出すことなしに vs 踏み出すことなくして competitor eliminated
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class TestN2Mock06GrammarRegressions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        exam_path = ROOT / "data/mock_exams/n2_mock_06.json"
        cls.exam_data = json.loads(exam_path.read_text(encoding='utf-8'))
        cls.items_by_id = {}
        for sec in cls.exam_data["sections"]:
            for item in sec["items"]:
                cls.items_by_id[item["id"]] = item

    def test_n2_06_m7_02_temporal_clarity_and_no_ni_saishite(self):
        """N2_06_M7_02: Must have explicit pre-launch temporal context and no ambiguous に際して."""
        q = self.items_by_id.get("N2_06_M7_02")
        self.assertIsNotNone(q, "N2_06_M7_02 must exist")
        self.assertIn("来月に控えた", q["stem"], "Stem must establish explicit pre-launch event")
        self.assertEqual(q["correctAnswer"], "C")
        
        opts = {o["id"]: o["text"] for o in q["options"]}
        self.assertEqual(opts["C"], "に先立ち")
        self.assertNotIn("に際して", opts.values(), "Ambiguous competitor に際して must be eliminated")
        self.assertIn("に応じて", opts.values(), "Unambiguous distractor に応じて must be present")

    def test_n2_06_m7_07_passive_colocation_and_no_shiirareta(self):
        """N2_06_M7_07: Must require idiomatic 〜を余儀なくされた and reject 強いられた."""
        q = self.items_by_id.get("N2_06_M7_07")
        self.assertIsNotNone(q, "N2_06_M7_07 must exist")
        self.assertIn("終日運休を", q["stem"])
        self.assertEqual(q["correctAnswer"], "D")
        
        opts = {o["id"]: o["text"] for o in q["options"]}
        self.assertEqual(opts["D"], "余儀なくされた")
        self.assertNotIn("強いられた", opts.values(), "Ambiguous competitor 強いられた must be eliminated")
        self.assertIn("余儀なくさせた", opts.values(), "Grammatical voice trap 余儀なくさせた must be present")

    def test_n2_06_m7_08_conversational_potency_and_no_sou_mo_nai(self):
        """N2_06_M7_08: Must frame emphatic spoken impossibility できっこない without そうもない."""
        q = self.items_by_id.get("N2_06_M7_08")
        self.assertIsNotNone(q, "N2_06_M7_08 must exist")
        self.assertIn("でき（　　）よ", q["stem"], "Stem must frame spoken conversational exclamation")
        self.assertEqual(q["correctAnswer"], "C")
        
        opts = {o["id"]: o["text"] for o in q["options"]}
        self.assertEqual(opts["C"], "っこない")
        self.assertNotIn("そうもない", opts.values(), "Defensible alternative そうもない must be eliminated")
        self.assertNotIn("そうにない", opts.values())
        self.assertIn("がたい", opts.values(), "Grammatically invalid distractor がたい must be present")

    def test_n2_06_m9_04_prerequisite_without_kotonakushite(self):
        """N2_06_M9_04: Blank 53 must have 踏み出すことなしに with no competing 踏み出すことなくして."""
        q = self.items_by_id.get("N2_06_M9_04")
        self.assertIsNotNone(q, "N2_06_M9_04 must exist")
        self.assertEqual(q["correctAnswer"], "C")
        
        opts = {o["id"]: o["text"] for o in q["options"]}
        self.assertEqual(opts["C"], "踏み出すことなしに")
        self.assertNotIn("踏み出すことなくして", opts.values(), "Synonymous competitor 踏み出すことなくして must be eliminated")
        self.assertIn("踏み出すにつれて", opts.values(), "Semantically incompatible distractor must be present")

if __name__ == "__main__":
    unittest.main()
