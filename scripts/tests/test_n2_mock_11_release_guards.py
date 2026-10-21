# -*- coding: utf-8 -*-
"""Focused fail-closed negative controls for the Phase 7 M11 release path."""
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.acoustic_assurance import evaluate_audio_track_assurance
from scripts.curriculum.audit_blind_remapping_integrity import remap_blind_solve
from scripts.curriculum.content_quality_checks import (
    pattern_defects,
    validate_semantic_remap,
    validate_vietnamese_explanations,
)
from scripts.curriculum.mock_exam_release_checks import (
    validate_full_mock_blueprint,
    validate_star_fragment_integrity,
    validate_version_bound_reconciliation,
)
from scripts.curriculum.reconcile_mock_blind_review import adapt_version_bound_m11_row


class TestN2Mock11ReleaseGuards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.exam = json.loads((ROOT / "data/mock_exams/n2_mock_11.json").read_text(encoding="utf-8"))
        cls.sealed = json.loads((ROOT / "qa/blind_items_m11_final.json").read_text(encoding="utf-8"))
        cls.review = json.loads((ROOT / "qa/N2_MOCK_11_BLIND_RECONCILIATION.json").read_text(encoding="utf-8"))

    def test_japanese_only_vietnamese_explanation_is_rejected(self):
        mutated = copy.deepcopy(self.exam)
        mutated["sections"][0]["items"][0]["explanationVi"] = "正解は均等です。"
        errors = validate_vietnamese_explanations(mutated)
        self.assertTrue(any(mutated["sections"][0]["items"][0]["id"] in error for error in errors))

    def test_long_artificial_answer_cycle_is_rejected(self):
        mutated = copy.deepcopy(self.exam)
        sequence = "ABCD" * 18 + "ABC"
        for index, question in enumerate(mutated["sections"][0]["items"]):
            question["correctAnswer"] = sequence[index]
        self.assertTrue(pattern_defects({"N2-MOCK-11": mutated}))

    def test_incorrect_displayed_key_remap_is_rejected(self):
        original = copy.deepcopy(self.exam["sections"][0]["items"][0])
        revised = copy.deepcopy(original)
        source_options = {row["id"]: row["text"] for row in original["options"]}
        revised["options"][0], revised["options"][1] = revised["options"][1], revised["options"][0]
        current_options = {row["id"]: row["text"] for row in revised["options"]}
        # A label remap derived from text must point at the same Japanese answer.
        mapped, _, selected_text = remap_blind_solve(original["correctAnswer"], source_options, current_options)
        self.assertEqual(selected_text, source_options[original["correctAnswer"]])
        wrong_label = next(label for label in current_options if label != mapped)
        revised["correctAnswer"] = wrong_label
        errors = validate_semantic_remap(original, revised, {"originalCorrectText": source_options[original["correctAnswer"]]})
        self.assertTrue(errors)

    def test_missing_audio_is_rejected(self):
        assurance = evaluate_audio_track_assurance(
            {"questionId": "missing", "audioSha256": "0" * 64},
            {"questionId": "missing"},
            ROOT / "tmp" / "phase7" / "no-such-audio.mp3",
        )
        self.assertFalse(assurance["AUDIO_FILE_EXISTS"])
        self.assertFalse(assurance["BROWSER_PLAYBACK_VERIFIED"])

    def test_wrong_audio_sha256_is_rejected(self):
        temp_root = ROOT / "tmp/phase7"
        temp_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_root) as folder:
            mp3 = Path(folder) / "fixture.mp3"
            mp3.write_bytes(b"synthetic audio bytes")
            assurance = evaluate_audio_track_assurance(
                {"questionId": "fixture", "audioSha256": "0" * 64},
                {"questionId": "fixture"}, mp3,
            )
            self.assertTrue(assurance["AUDIO_FILE_EXISTS"])
            self.assertFalse(assurance["AUDIO_HASH_VERIFIED"])
            self.assertFalse(assurance["BROWSER_PLAYBACK_VERIFIED"])

    def test_stale_reviewer_fingerprint_is_rejected(self):
        mutated = copy.deepcopy(self.review)
        mutated["rows"][0]["contentFingerprint"] = "0" * 64
        errors = validate_version_bound_reconciliation(mutated, self.exam, self.sealed)
        self.assertTrue(any("fingerprint" in error for error in errors))

    def test_validated_review_fingerprint_reaches_generic_provenance_field(self):
        # CI's generic classifier consumes contentFingerprint. The dedicated
        # validator proves the report row before this adapter is called.
        report_row = self.review["rows"][0]
        adapted = adapt_version_bound_m11_row(report_row)
        self.assertEqual(adapted["contentFingerprint"], report_row["contentFingerprint"])
        self.assertEqual(adapted["reviewFingerprint"], report_row["contentFingerprint"])

    def test_missing_required_question_is_rejected(self):
        mutated = copy.deepcopy(self.exam)
        mutated["sections"][0]["items"].pop()
        errors = validate_full_mock_blueprint(mutated)
        self.assertTrue(errors)

    def test_star_fragment_key_mismatch_is_rejected(self):
        mutated = copy.deepcopy(self.exam)
        star = next(q for q in mutated["sections"][0]["items"] if q["typeId"] == "N2-GR-STAR")
        third = star["fragmentOrder"].split("→")[2]
        star["correctAnswer"] = next(option["id"] for option in star["options"] if option["id"] != third)
        errors = validate_star_fragment_integrity(mutated)
        self.assertTrue(any(star["id"] in error and "key" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
