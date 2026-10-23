# -*- coding: utf-8 -*-
"""Focused release-negative controls for N2-MOCK-12."""
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
from scripts.curriculum.content_quality_checks import (
    pattern_defects,
    validate_semantic_remap,
    validate_vietnamese_explanations,
)
from scripts.curriculum.mock_exam_release_checks import (
    validate_current_version_reconciliation,
    validate_full_mock_blueprint,
    validate_star_fragment_integrity,
)
from scripts.curriculum.build_phase_71_candidate_reconciliation import (
    response_registry,
    validate_receipt as validate_phase71_receipt,
)
from scripts.curriculum.question_fingerprint import compute_spoken_content_fingerprint


class TestN2Mock12ReleaseGuards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.exam = json.loads((ROOT / "data/mock_exams/n2_mock_12.json").read_text(encoding="utf-8"))
        if cls.exam.get("releaseGateStatus") == "REVIEW_CONTENT_VERSION_VERIFIED":
            cls.sealed = json.loads((ROOT / "qa/blind_items_m12_phase71_candidate.json").read_text(encoding="utf-8"))
            cls.review = json.loads((ROOT / "qa/N2_MOCK_12_PHASE71_CANDIDATE_RECONCILIATION.json").read_text(encoding="utf-8"))
        else:
            cls.sealed = json.loads((ROOT / "qa/blind_items_m12_final.json").read_text(encoding="utf-8"))
            cls.review = json.loads((ROOT / "qa/N2_MOCK_12_BLIND_RECONCILIATION.json").read_text(encoding="utf-8"))

    def test_current_review_is_fingerprint_bound_and_key_free(self):
        raw_path = ROOT / self.review["rawEvidence"]["rawOutputFile"]
        self.assertEqual(validate_current_version_reconciliation(
            self.review, self.exam, self.sealed, raw_sha256={"rawOutputSha256": raw_path}
        ), [])

    def test_phase71_packet_and_raw_evidence_bind_each_current_row(self):
        self.assertEqual(validate_phase71_receipt(12, response_registry(), source="published"), [])

    def test_historical_review_is_preserved_against_its_original_snapshot(self):
        baseline = json.loads((ROOT / "qa/n2_mock_12_phase71_pre_release_baseline.json").read_text(encoding="utf-8"))
        old_sealed = json.loads((ROOT / "qa/blind_items_m12_final.json").read_text(encoding="utf-8"))
        old_review = json.loads((ROOT / "qa/N2_MOCK_12_BLIND_RECONCILIATION.json").read_text(encoding="utf-8"))
        self.assertEqual(validate_current_version_reconciliation(old_review, baseline, old_sealed), [])

    def test_mutated_raw_review_bytes_fail_the_release_digest_check(self):
        raw_path = ROOT / self.review["rawEvidence"]["rawOutputFile"]
        mutated = copy.deepcopy(self.review)
        mutated["rawEvidence"]["rawOutputSha256"] = "0" * 64
        errors = validate_current_version_reconciliation(
            mutated, self.exam, self.sealed, raw_sha256={"rawOutputSha256": raw_path}
        )
        self.assertTrue(any("captured raw response digest" in error for error in errors))

    def test_japanese_only_vietnamese_explanation_is_rejected(self):
        mutated = copy.deepcopy(self.exam)
        item = mutated["sections"][0]["items"][0]
        item["explanationVi"] = "正解は均等です。"
        self.assertTrue(validate_vietnamese_explanations(mutated))

    def test_long_artificial_answer_cycle_is_rejected(self):
        mutated = copy.deepcopy(self.exam)
        sequence = "ABCD" * 18 + "ABC"
        for index, question in enumerate(mutated["sections"][0]["items"]):
            question["correctAnswer"] = sequence[index]
        self.assertTrue(pattern_defects({"N2-MOCK-12": mutated}))

    def test_incorrect_displayed_key_remap_is_rejected(self):
        original = copy.deepcopy(self.exam["sections"][0]["items"][0])
        revised = copy.deepcopy(original)
        revised["options"][0], revised["options"][1] = revised["options"][1], revised["options"][0]
        revised["correctAnswer"] = next(option["id"] for option in revised["options"]
                                         if option["text"] != next(row["text"] for row in original["options"]
                                                                   if row["id"] == original["correctAnswer"]))
        errors = validate_semantic_remap(
            original, revised,
            {"originalCorrectText": next(row["text"] for row in original["options"]
                                         if row["id"] == original["correctAnswer"])},
        )
        self.assertTrue(errors)

    def test_missing_audio_is_rejected(self):
        assurance = evaluate_audio_track_assurance(
            {"questionId": "missing", "audioSha256": "0" * 64},
            {"questionId": "missing"},
            ROOT / "tmp/phase7/no-such-m12-audio.mp3",
        )
        self.assertFalse(assurance["AUDIO_FILE_EXISTS"])
        self.assertFalse(assurance["BROWSER_PLAYBACK_VERIFIED"])

    def test_incorrect_audio_sha256_is_rejected(self):
        temp_root = ROOT / "tmp/phase7"
        temp_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_root) as folder:
            audio = Path(folder) / "synthetic-fixture.mp3"
            audio.write_bytes(b"synthetic QA bytes")
            assurance = evaluate_audio_track_assurance(
                {"questionId": "fixture", "audioSha256": "0" * 64},
                {"questionId": "fixture"}, audio,
            )
            self.assertTrue(assurance["AUDIO_FILE_EXISTS"])
            self.assertFalse(assurance["AUDIO_HASH_VERIFIED"])
            self.assertFalse(assurance["BROWSER_PLAYBACK_VERIFIED"])

    def test_spoken_choice_reorder_invalidates_audio_source_fingerprint(self):
        item = copy.deepcopy(next(q for q in self.exam["sections"][1]["items"]
                                  if q["id"] == "N2_12_M4_L01"))
        original = compute_spoken_content_fingerprint(item)
        item["options"][0], item["options"][1] = item["options"][1], item["options"][0]
        self.assertNotEqual(original, compute_spoken_content_fingerprint(item))

    def test_stale_current_version_review_fingerprint_is_rejected(self):
        mutated = copy.deepcopy(self.review)
        mutated["rows"][0]["contentFingerprint"] = "0" * 64
        errors = validate_current_version_reconciliation(mutated, self.exam, self.sealed)
        self.assertTrue(any("fingerprint is stale" in error for error in errors))

    def test_missing_required_question_is_rejected(self):
        mutated = copy.deepcopy(self.exam)
        mutated["sections"][0]["items"].pop()
        self.assertTrue(validate_full_mock_blueprint(mutated))

    def test_star_fragment_key_mismatch_is_rejected(self):
        mutated = copy.deepcopy(self.exam)
        star = next(q for q in mutated["sections"][0]["items"] if q["typeId"] == "N2-GR-STAR")
        order = star["fragmentOrder"].split("→")
        third = order[2]
        star["correctAnswer"] = next(option["id"] for option in star["options"] if option["id"] != third)
        self.assertTrue(validate_star_fragment_integrity(mutated))


if __name__ == "__main__":
    unittest.main()
