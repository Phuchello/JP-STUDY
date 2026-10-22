# -*- coding: utf-8 -*-
"""Focused integrity checks for the unreleased Phase 7.1 content candidates."""
import json
import unittest
from pathlib import Path

from scripts.curriculum.audit_star_permutations import validate_star_structure
from scripts.curriculum.bank_data.n2_mock_11_data import get_n2_mock_11_sec1_items
from scripts.curriculum.bank_data.n2_mock_12_data import get_n2_mock_12_sec1_items
from scripts.curriculum.bank_data.n2_mock_13_data import get_n2_mock_13_sec1_items
from scripts.curriculum.phase_71_reading_repairs import QUESTION_REVISIONS


ROOT = Path(__file__).resolve().parents[2]
READING_TYPES = {"N2-RD-SHORT", "N2-RD-MED", "N2-RD-LONG"}


class Phase71CandidateContentTests(unittest.TestCase):
    def test_all_51_reading_items_keep_ids_keys_and_complete_bindings(self):
        for number, builder in (
            (11, get_n2_mock_11_sec1_items),
            (12, get_n2_mock_12_sec1_items),
            (13, get_n2_mock_13_sec1_items),
        ):
            candidate = {
                item["id"]: item for item in builder()
                if item.get("typeId") in READING_TYPES
            }
            published = json.loads(
                (ROOT / f"data/mock_exams/n2_mock_{number:02}.json").read_text(encoding="utf-8")
            )
            previous = {
                item["id"]: item
                for section in published["sections"]
                for item in section["items"]
            }
            expected = {
                *(f"N2_{number}_M10_{index:02}" for index in range(1, 6)),
                *(f"N2_{number}_M11_{index:02}" for index in range(1, 10)),
                *(f"N2_{number}_M13_{index:02}" for index in range(1, 4)),
            }
            self.assertEqual(set(candidate), expected)
            for question_id, item in candidate.items():
                with self.subTest(question_id=question_id):
                    option_ids = {option["id"] for option in item["options"]}
                    self.assertEqual(len(item["options"]), 4)
                    self.assertEqual(len({option["text"] for option in item["options"]}), 4)
                    self.assertIn(item["correctAnswer"], option_ids)
                    self.assertEqual(item["correctAnswer"], previous[question_id]["correctAnswer"])
                    self.assertTrue(item.get("contextPassage") or item.get("passage"))
                    self.assertTrue(item.get("explanationVi"))

    def test_question_revisions_are_applied_by_option_id_without_rekeying(self):
        builders = {
            11: get_n2_mock_11_sec1_items,
            12: get_n2_mock_12_sec1_items,
            13: get_n2_mock_13_sec1_items,
        }
        self.assertEqual(len(QUESTION_REVISIONS), 35)
        for question_id, revision in QUESTION_REVISIONS.items():
            number = int(question_id.split("_")[1])
            item = next(x for x in builders[number]() if x["id"] == question_id)
            with self.subTest(question_id=question_id):
                if "stem" in revision:
                    self.assertEqual(item["stem"], revision["stem"])
                if "optionsById" in revision:
                    actual = {option["id"]: option["text"] for option in item["options"]}
                    self.assertEqual(actual, revision["optionsById"])
                    self.assertIn(item["correctAnswer"], actual)

    def test_m11_star_slots_reconstruct_the_keyed_sentence_and_invoice_overlap_is_gone(self):
        items = get_n2_mock_11_sec1_items()
        stars = [item for item in items if item.get("typeId") == "N2-GR-STAR"]
        self.assertEqual([item["id"] for item in stars], [f"N2_11_M8_{n:02}" for n in range(1, 6)])
        for item in stars:
            with self.subTest(question_id=item["id"]):
                valid, reason, data = validate_star_structure(item)
                self.assertTrue(valid, reason)
                self.assertEqual(len(data["permutations"]), 24)
                self.assertEqual(item["stem"].count("（"), 4)
                self.assertEqual(item["stem"].count("★"), 1)
                self.assertEqual(item["starPosition"], 3)
                self.assertEqual(item["starredOptionText"],
                                 next(o["text"] for o in item["options"] if o["id"] == item["correctAnswer"]))
                option_map = {option["id"]: option["text"] for option in item["options"]}
                reconstructed = data["prefix"] + "".join(option_map[key] for key in data["canonicalOrder"]) + data["suffix"]
                self.assertEqual(reconstructed, item["assembledSentence"])
                self.assertEqual(item["fragmentOrder"].split("→"), data["canonicalOrder"])

        invoice_check = next(x for x in stars if x["id"] == "N2_11_M8_01")
        fact_check = next(x for x in stars if x["id"] == "N2_11_M8_03")
        self.assertIn("請求内容", invoice_check["contextPassage"])
        self.assertIn("事実関係", fact_check["contextPassage"])
        self.assertNotIn("請求書", fact_check["contextPassage"])


if __name__ == "__main__":
    unittest.main()
