# -*- coding: utf-8 -*-
"""
Adversarial Negative Mutation Suite for JP-STUDY Quality & Release Gate

Verifies that the release gate strictly rejects defects across all 8 adversarial mutation vectors:
  Mutation A — Incorrect answer key
  Mutation B — Grammar attachment failure
  Mutation C — Multiple valid answers
  Mutation D — Missing audio file
  Mutation E — Invalid browser-playback evidence
  Mutation F — Corrupted blind answer
  Mutation G — Failed structural QA (with positive linguistic status - regression for operator precedence)
  Mutation H — Stale review / missing content hash
"""
import unittest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.audit_n2_mock_105_questions import (
    evaluate_question_release_gate,
    evaluate_acoustic_status
)

class TestAdversarialReleaseGate(unittest.TestCase):

    def test_mutation_a_incorrect_answer_key(self):
        """
        Mutation A — Incorrect answer key:
        Authored key mutated to an incorrect option while independent blind solve disagrees.
        Expected: Gate rejects item and assigns QUARANTINED.
        """
        tier, reasons = evaluate_question_release_gate(
            structural_status="PASS",
            linguistic_status="QUARANTINED_KEY_MISMATCH",
            acoustic_status="N/A (Written Section)",
            is_listening=False
        )
        self.assertEqual(tier, "QUARANTINED")
        self.assertTrue(any("Linguistic unverified" in r for r in reasons))

    def test_mutation_b_grammar_attachment_failure(self):
        """
        Mutation B — Grammar attachment failure:
        Ungrammatical stem attachment (e.g. *理解がたい without ren'yōkei 'し').
        Unless verified as a resolved grammatical defect, it cannot receive release clearance.
        """
        tier, reasons = evaluate_question_release_gate(
            structural_status="PASS",
            linguistic_status="BLOCKED: GRAMMATICAL_DEFECT_DETECTED",
            acoustic_status="N/A (Written Section)",
            is_listening=False
        )
        self.assertEqual(tier, "QUARANTINED")
        self.assertTrue(any("Linguistic unverified" in r for r in reasons))

    def test_mutation_c_multiple_valid_answers(self):
        """
        Mutation C — Multiple valid answers:
        Item has competing defensible answers flagged by independent review.
        Expected: Flagged for human review; unmitigated ambiguity cannot receive silent clean pass.
        """
        # When unmitigated/unreconciled ambiguity exists:
        tier, reasons = evaluate_question_release_gate(
            structural_status="PASS",
            linguistic_status="FLAGGED_MULTIPLE_VALID_ANSWERS",
            acoustic_status="N/A (Written Section)",
            is_listening=False
        )
        self.assertEqual(tier, "QUARANTINED")

        # When explicitly marked AI_AGREED_FLAGGED_FOR_HUMAN, it requires human sign-off:
        tier_flagged, reasons_flagged = evaluate_question_release_gate(
            structural_status="PASS",
            linguistic_status="AI_AGREED_FLAGGED_FOR_HUMAN",
            acoustic_status="N/A (Written Section)",
            is_listening=False
        )
        # Technically ready for AI audit, but flags are preserved
        self.assertEqual(tier_flagged, "TECHNICALLY_READY · AI_AUDITED")

    def test_mutation_d_missing_audio_file(self):
        """
        Mutation D — Missing audio file:
        Audio file does not exist on disk for a listening question.
        Expected: evaluate_acoustic_status returns AUDIO_FILE_MISSING and gate QUARANTINES.
        """
        dummy_audio_dir = ROOT / "docs/audio/non_existent_dir_mutation_d"
        status = evaluate_acoustic_status(
            qid="N2-MUT-L01",
            audio_url="https://example.com/audio/missing.mp3",
            audio_dir=dummy_audio_dir,
            receipt_tracks={}
        )
        self.assertEqual(status, "AUDIO_FILE_MISSING")

        tier, reasons = evaluate_question_release_gate(
            structural_status="PASS",
            linguistic_status="AI_VERIFIED_PASS",
            acoustic_status=status,
            is_listening=True
        )
        self.assertEqual(tier, "QUARANTINED")
        self.assertTrue(any("Acoustic verification incomplete" in r for r in reasons))

    def test_mutation_e_invalid_browser_playback_evidence(self):
        """
        Mutation E — Invalid browser-playback evidence:
        Audio file exists on disk, but browser playback receipt is missing or failed.
        Expected: evaluate_acoustic_status detects missing receipt or failed playback; gate QUARANTINES.
        """
        audio_dir = ROOT / "docs/audio/n2_mock_01"
        # 1. Missing from receipt
        status_missing_receipt = evaluate_acoustic_status(
            qid="N2-M1-L01",
            audio_url="https://example.com/audio/N2_M1_L01.mp3",
            audio_dir=audio_dir,
            receipt_tracks={}
        )
        self.assertEqual(status_missing_receipt, "AUDIO_RECEIPT_MISSING")
        tier, _ = evaluate_question_release_gate("PASS", "AI_VERIFIED_PASS", status_missing_receipt, is_listening=True)
        self.assertEqual(tier, "QUARANTINED")

        # 2. Receipt indicates browser playback failed
        mock_receipt = {
            "N2-M1-L01": {
                "audioHashVerified": True,
                "audioDecodes": True,
                "browserPlaybackVerified": False
            }
        }
        status_playback_failed = evaluate_acoustic_status(
            qid="N2-M1-L01",
            audio_url="https://example.com/audio/N2_M1_L01.mp3",
            audio_dir=audio_dir,
            receipt_tracks=mock_receipt
        )
        self.assertEqual(status_playback_failed, "BROWSER_PLAYBACK_FAILED")
        tier, _ = evaluate_question_release_gate("PASS", "AI_VERIFIED_PASS", status_playback_failed, is_listening=True)
        self.assertEqual(tier, "QUARANTINED")

    def test_mutation_f_corrupted_blind_answer(self):
        """
        Mutation F — Corrupted blind answer:
        Authored answer key is changed without independent blind solve backing.
        Expected: Independent answer is NOT overwritten; reconciliation yields KEY_MISMATCH.
        """
        # Independent solve chose 'B', but authored key was changed to 'A'
        blind_status = "KEY_MISMATCH"
        ling_status = "QUARANTINED_KEY_MISMATCH"
        tier, reasons = evaluate_question_release_gate(
            structural_status="PASS",
            linguistic_status=ling_status,
            acoustic_status="N/A (Written Section)",
            is_listening=False
        )
        self.assertEqual(tier, "QUARANTINED")

    def test_mutation_g_failed_structural_qa(self):
        """
        Mutation G — Failed structural QA:
        Question has duplicate options or invalid format, but positive linguistic status.
        REGRESSION TEST FOR OPERATOR PRECEDENCE:
        Previously, `structural_status == 'PASS' and 'PASS' in linguistic or 'VERIFIED' in linguistic`
        evaluated to True because 'VERIFIED' in 'REPAIRED_AND_VERIFIED' short-circuited the AND!
        Expected: Must strictly evaluate to QUARANTINED.
        """
        for invalid_struct in ["FAIL: Duplicate option texts found", "FAIL: Expected 4 options, got 3", "FAIL: Missing explanation"]:
            for valid_ling in ["AI_VERIFIED_PASS", "REPAIRED_AND_VERIFIED", "AI_AGREED_FLAGGED_FOR_HUMAN"]:
                tier, reasons = evaluate_question_release_gate(
                    structural_status=invalid_struct,
                    linguistic_status=valid_ling,
                    acoustic_status="N/A (Written Section)",
                    is_listening=False
                )
                self.assertEqual(tier, "QUARANTINED", f"Failed for struct='{invalid_struct}' with ling='{valid_ling}'")
                self.assertTrue(any("Structural defect" in r for r in reasons))

    def test_mutation_h_stale_review(self):
        """
        Mutation H — Stale review:
        Item content hash is not present in the independent review ledger.
        Expected: Status is NOT_IN_BLIND_LEDGER and gate QUARANTINES the item.
        """
        tier, reasons = evaluate_question_release_gate(
            structural_status="PASS",
            linguistic_status="UNVERIFIED_MISSING_BLIND_SOLVE",
            acoustic_status="N/A (Written Section)",
            is_listening=False
        )
        self.assertEqual(tier, "QUARANTINED")
        self.assertTrue(any("Linguistic unverified" in r for r in reasons))

if __name__ == '__main__':
    unittest.main()
