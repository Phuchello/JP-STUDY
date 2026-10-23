# -*- coding: utf-8 -*-
"""Focused integrity checks for the unreleased Phase 7.1 content candidates."""
import json
import unittest
import copy
from pathlib import Path

from scripts.curriculum.audit_star_permutations import validate_star_structure
from scripts.curriculum.bank_data.n2_mock_11_data import get_n2_mock_11_sec1_items
from scripts.curriculum.bank_data.n2_mock_12_data import get_n2_mock_12_sec1_items
from scripts.curriculum.bank_data.n2_mock_13_data import get_n2_mock_13_sec1_items
from scripts.curriculum.bank_data.n2_mock_14_data import get_n2_mock_14_sec1_items
from scripts.curriculum.phase_71_reading_repairs import QUESTION_REVISIONS
from scripts.curriculum.phase_71_reading_rationales import (
    DISTRACTOR_RATIONALES,
    validate_distractor_rationales,
)
from scripts.curriculum.export_phase_71_final_delta_packet import (
    TARGET_IDS as FINAL_DELTA_IDS,
    build_final_delta_packet,
)
from scripts.curriculum.question_fingerprint import compute_question_fingerprint


ROOT = Path(__file__).resolve().parents[2]
READING_TYPES = {"N2-RD-SHORT", "N2-RD-MED", "N2-RD-LONG"}


class Phase71CandidateContentTests(unittest.TestCase):
    def test_final_delta_blind_packet_contains_only_clean_version_bound_items(self):
        packet = build_final_delta_packet()
        self.assertIsInstance(packet, list)
        self.assertEqual({item["id"] for item in packet}, FINAL_DELTA_IDS)
        allowed_fields = {
            "id", "skill", "category", "taskInstructions", "contextPassage",
            "stem", "options", "contentFingerprint",
        }
        self.assertTrue(all(set(item) == allowed_fields for item in packet))
        forbidden_fields = {
            "correctAnswer", "answerKey", "explanation", "explanationVi",
            "distractorExplanations", "knownEditorialConcern", "sourceSha256",
            "reviewStatus", "reviewerSelections", "intendedDistractorLogic",
        }
        candidate_items = {
            q["id"]: q
            for builder in (get_n2_mock_12_sec1_items, get_n2_mock_13_sec1_items,
                            get_n2_mock_14_sec1_items)
            for q in builder()
            if q["id"] in FINAL_DELTA_IDS
        }
        for item in packet:
            with self.subTest(question_id=item["id"]):
                self.assertFalse(forbidden_fields.intersection(item))
                self.assertEqual(len(item["options"]), 4)
                self.assertEqual(item["contentFingerprint"],
                                 compute_question_fingerprint(candidate_items[item["id"]]))

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
        self.assertEqual(len(QUESTION_REVISIONS), 36)
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

    def test_all_105_revised_reading_distractor_explanations_are_specific_and_option_bound(self):
        builders = {
            11: get_n2_mock_11_sec1_items,
            12: get_n2_mock_12_sec1_items,
            13: get_n2_mock_13_sec1_items,
        }
        reviewed_items = []
        reviewed_revisions = {}
        explanation_count = 0
        for qid, revision in QUESTION_REVISIONS.items():
            number = int(qid.split("_")[1])
            item = next(x for x in builders[number]() if x["id"] == qid)
            reviewed_items.append(item)
            reviewed_revisions[qid] = revision
            wrong_ids = {option["id"] for option in item["options"]} - {item["correctAnswer"]}
            explanations = item.get("distractorExplanations", {})
            with self.subTest(question_id=qid):
                self.assertEqual(set(explanations), wrong_ids)
                for option_id in wrong_ids:
                    record = DISTRACTOR_RATIONALES[qid][option_id]
                    option_text = next(option["text"] for option in item["options"]
                                       if option["id"] == option_id)
                    self.assertEqual(record[0], option_text)
                    self.assertEqual(explanations[option_id], record[1])
                    self.assertGreaterEqual(len(explanations[option_id]), 25)
                explanation_count += len(explanations)
        self.assertEqual(explanation_count, 108)
        self.assertEqual(validate_distractor_rationales(reviewed_items, reviewed_revisions), [])

        stale_item = copy.deepcopy(reviewed_items[0])
        stale_wrong_id = next(option["id"] for option in stale_item["options"]
                              if option["id"] != stale_item["correctAnswer"])
        next(option for option in stale_item["options"]
             if option["id"] == stale_wrong_id)["text"] += "（変更）"
        self.assertTrue(validate_distractor_rationales([stale_item], {stale_item["id"]: reviewed_revisions[stale_item["id"]]}))

        generic_item = copy.deepcopy(reviewed_items[0])
        generic_item["distractorExplanations"][stale_wrong_id] = (
            "Phương án này không phù hợp với bài đọc. " + generic_item["explanationVi"]
        )
        generic_errors = validate_distractor_rationales(
            [generic_item], {generic_item["id"]: reviewed_revisions[generic_item["id"]]}
        )
        self.assertTrue(any("generic candidate feedback" in error for error in generic_errors))

        repeated_item = copy.deepcopy(reviewed_items[0])
        repeated_item["distractorExplanations"][stale_wrong_id] = repeated_item["explanationVi"]
        repeated_errors = validate_distractor_rationales(
            [repeated_item], {repeated_item["id"]: reviewed_revisions[repeated_item["id"]]}
        )
        self.assertTrue(any("only repeats the answer explanation" in error for error in repeated_errors))

        crossbound_item = copy.deepcopy(reviewed_items[0])
        first_wrong, second_wrong = list(crossbound_item["distractorExplanations"])[:2]
        crossbound_item["distractorExplanations"][first_wrong], crossbound_item["distractorExplanations"][second_wrong] = (
            crossbound_item["distractorExplanations"][second_wrong],
            crossbound_item["distractorExplanations"][first_wrong],
        )
        crossbound_errors = validate_distractor_rationales(
            [crossbound_item], {crossbound_item["id"]: reviewed_revisions[crossbound_item["id"]]}
        )
        self.assertTrue(any("bound to the wrong option" in error for error in crossbound_errors))

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
        figure_check = next(x for x in stars if x["id"] == "N2_11_M8_04")
        self.assertIn("請求内容", invoice_check["contextPassage"])
        self.assertIn("事実関係", fact_check["contextPassage"])
        self.assertNotIn("請求書", fact_check["contextPassage"])
        self.assertEqual(figure_check["correctAnswer"], "D")
        self.assertEqual(figure_check["assembledSentence"],
                         "担当者は、申請書に記された数字が原本の記録と一致するかどうかを項目ごとに確かめ、違いがあれば申請者に確認する必要があると判断した。")
        self.assertEqual(figure_check["starredOptionText"], "項目ごとに確かめ、")

    def test_phase_71_reading_follow_up_repairs_preserve_causal_and_criterion_alignment(self):
        q12 = next(item for item in get_n2_mock_12_sec1_items()
                   if item["id"] == "N2_12_M10_05")
        self.assertIn("迂回で移動時間が延びても各地区の到着予定時刻を保てるよう", q12["contextPassage"])
        self.assertIn("出発時刻をこれまでより十五分早める", q12["contextPassage"])
        self.assertIn("滞在時間は変えない", q12["contextPassage"])
        self.assertEqual(q12["correctAnswer"], "B")

        q13 = next(item for item in get_n2_mock_13_sec1_items()
                   if item["id"] == "N2_13_M11_01")
        options = {option["id"]: option["text"] for option in q13["options"]}
        self.assertEqual(options["B"], "初学者が要点を追えるか、根拠を示して説明しているか")
        self.assertIn("初学者が要点を追えるか", q13["contextPassage"])
        self.assertIn("根拠を示して説明しているか", q13["contextPassage"])
        self.assertEqual(q13["correctAnswer"], "B")


if __name__ == "__main__":
    unittest.main()
