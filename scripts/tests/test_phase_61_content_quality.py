"""Regression fixtures for Phase 6.1 localization, answer positions and audio mapping."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.curriculum.content_quality_checks import (
    pattern_defects,
    remap_review_selection,
    validate_answer_letter_references,
    validate_semantic_remap,
    validate_spoken_audio,
    validate_vietnamese_explanations,
)
from scripts.curriculum.audit_blind_remapping_integrity import derive_normalized_m07_selection
from scripts.curriculum.question_fingerprint import compute_question_fingerprint


def make_exam(exam_id: str, sequence: str, star_answers: str = "") -> dict:
    items = []
    for index, answer in enumerate(sequence):
        items.append({
            "id": f"{exam_id}-{index + 1:03}",
            "typeId": "N2-GR-STAR" if index < len(star_answers) else "N2-GR-FORM",
            "correctAnswer": star_answers[index] if index < len(star_answers) else answer,
            "options": [{"id": label, "text": f"option-{label}"} for label in "ABCD"],
        })
    return {"examId": exam_id, "sections": [{"sectionId": "sec-1", "items": items[:75]},
                                                {"sectionId": "sec-2", "items": items[75:]}]}


class TestPhase61ContentQuality(unittest.TestCase):
    def test_m07_normalized_review_uses_exact_text_and_source_provenance(self):
        source = {
            "id": "N2_07_M1_01", "typeId": "N2-GR-FORM", "stem": "穴埋め問題",
            "options": [
                {"id": "A", "text": "こうふ"}, {"id": "B", "text": "こうぶ"},
                {"id": "C", "text": "ごうふ"}, {"id": "D", "text": "きょうふ"},
            ],
        }
        current = {
            **source,
            "options": [
                {"id": "A", "text": "きょうふ"}, {"id": "B", "text": "こうふ"},
                {"id": "C", "text": "こうぶ"}, {"id": "D", "text": "ごうふ"},
            ],
        }
        review = {
            "originalReviewerSelection": "A", "selectedOptionText": "こうふ",
            "sourceContentFingerprint": compute_question_fingerprint(source),
            "contentFingerprint": compute_question_fingerprint(current),
        }
        evidence = derive_normalized_m07_selection(review, [source], current)
        self.assertEqual(evidence["currentLabel"], "B")
        self.assertEqual(evidence["mappingMethod"], "EXACT_OPTION_TEXT_DERIVATION")

    def test_m07_normalized_review_rejects_unproven_source_text(self):
        source = {
            "id": "N2_07_M1_01", "typeId": "N2-GR-FORM", "stem": "穴埋め問題",
            "options": [{"id": label, "text": label} for label in "ABCD"],
        }
        current = {**source}
        review = {
            "originalReviewerSelection": "A", "selectedOptionText": "A",
            "sourceContentFingerprint": "0" * 64,
            "contentFingerprint": compute_question_fingerprint(current),
        }
        with self.assertRaisesRegex(ValueError, "source fingerprint"):
            derive_normalized_m07_selection(review, [source], current)

    def test_105_japanese_only_explanations_fail_localization(self):
        exam = make_exam("N2-MOCK-08", "AABBC" * 21)
        for question in exam["sections"][0]["items"] + exam["sections"][1]["items"]:
            question["explanationVi"] = "正しい答えは文脈に合います。"
        errors = validate_vietnamese_explanations(exam)
        self.assertEqual(sum(": explanationVi" in error for error in errors), 105)

    def test_44_answer_abcd_cycle_fails(self):
        sequence = "ABCD" * 11 + "B" + "AABCBDD" * 8 + "AABC"
        defects = pattern_defects({"N2-MOCK-07": make_exam("N2-MOCK-07", sequence)})
        self.assertTrue(any("repeated period-4 pattern spans 44" in error for error in defects), defects)

    def test_reverse_dcba_cycle_fails(self):
        sequence = "DCBA" * 3 + "C" + "AABCBDD" * 13 + "A"
        defects = pattern_defects({"N2-MOCK-07": make_exam("N2-MOCK-07", sequence)})
        self.assertTrue(any("repeated period-4 pattern spans 12" in error for error in defects), defects)

    def test_five_star_answers_at_c_are_flagged(self):
        exam = make_exam("N2-MOCK-09", "AABBC" * 21, "CCCCC")
        defects = pattern_defects({"N2-MOCK-09": exam})
        self.assertTrue(any("all five STAR answers use C" in error for error in defects), defects)

    def test_answer_letter_change_without_semantic_move_fails(self):
        original = {"id": "q", "typeId": "N2-GR-FORM", "correctAnswer": "A",
                    "options": [{"id": "A", "text": "correct Japanese answer"},
                                {"id": "B", "text": "distractor one"},
                                {"id": "C", "text": "distractor two"},
                                {"id": "D", "text": "distractor three"}]}
        revised = {"id": "q", "typeId": "N2-GR-FORM", "correctAnswer": "A",
                   "options": [{"id": "A", "text": "distractor one"},
                               {"id": "B", "text": "correct Japanese answer"},
                               {"id": "C", "text": "distractor two"},
                               {"id": "D", "text": "distractor three"}]}
        self.assertTrue(validate_semantic_remap(original, revised,
                                                {"originalCorrectText": "correct Japanese answer"}))

    def test_old_review_letter_maps_by_exact_option_text(self):
        original = {"id": "q", "options": [{"id": "A", "text": "semantic answer"},
                                               {"id": "B", "text": "distractor"}]}
        revised = {"id": "q", "options": [{"id": "A", "text": "distractor"},
                                              {"id": "B", "text": "semantic answer"}]}
        mapping = remap_review_selection(original, revised, "A")
        self.assertEqual(mapping["newId"], "B")
        self.assertEqual(mapping["optionText"], "semantic answer")
        self.assertEqual(mapping["mappingMethod"], "EXACT_OPTION_TEXT_DERIVATION")

    def test_stale_explanation_answer_letter_fails(self):
        exam = {"sections": [{"items": [{"id": "q", "correctAnswer": "B",
                                           "options": [{"id": label, "text": label} for label in "ABCD"],
                                           "explanationVi": "Đáp án A đúng vì nội dung phù hợp."}]}]}
        self.assertTrue(validate_answer_letter_references(exam))
        exam["sections"][0]["items"][0]["explanationVi"] = "Đáp án B đúng vì nội dung phù hợp."
        self.assertEqual(validate_answer_letter_references(exam), [])

    def test_spoken_option_reorder_without_audio_evidence_fails(self):
        question = {"id": "listen", "typeId": "N2-LIS-RESP",
                    "options": [{"id": "A", "text": "はい"}, {"id": "B", "text": "いいえ"}]}
        self.assertTrue(validate_spoken_audio(question, None))
        evidence = {"status": "VERIFIED", "orderedOptionTexts": ["いいえ", "はい"],
                    "audioSha256": "a" * 64, "audioWasRegenerated": True}
        self.assertTrue(validate_spoken_audio(question, evidence))
        evidence["orderedOptionTexts"] = ["はい", "いいえ"]
        self.assertEqual(validate_spoken_audio(question, evidence), [])

    def test_valid_non_cyclic_exam_passes(self):
        exam = make_exam("N2-MOCK-07", "AABCBDD" * 15)
        self.assertEqual(pattern_defects({"N2-MOCK-07": exam}), [])

    def test_cross_exam_alignment_over_50_positions_is_flagged(self):
        sequence = "AABCBDD" * 15
        defects = pattern_defects({"N2-MOCK-07": make_exam("N2-MOCK-07", sequence),
                                   "N2-MOCK-08": make_exam("N2-MOCK-08", sequence)})
        self.assertTrue(any("75/75 section-1 positions align" in error for error in defects), defects)

    def test_real_n2_mock_10_passes_new_quality_screens(self):
        path = ROOT / "data/mock_exams/n2_mock_10.json"
        exam = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(validate_vietnamese_explanations(exam), [])
        self.assertEqual(pattern_defects({"N2-MOCK-10": exam}), [])


if __name__ == "__main__":
    unittest.main()
