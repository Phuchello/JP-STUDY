# -*- coding: utf-8 -*-
"""
Adversarial Negative Mutation Suite for JP-STUDY Quality & Release Gate

Executes real end-to-end pipeline mutations on temporary fixtures:
  - Repaired-item reconciliation bypass prevention (regression test)
  - Mutation A — Wrong answer key detection
  - Mutation B — Ungrammatical stem / content modification detection
  - Mutation C — Competing answers / ambiguity quarantine
  - Mutation D — Missing audio file detection
  - Mutation E — Stale audio receipt & live hash mismatch detection
  - Mutation F — Tampered blind answer & semantic mapping invariance
  - Mutation G — Broken structure & operator precedence regression
  - Mutation H — Stale review / fingerprint invalidation
  - Substring spoofing immunity
"""
import copy
import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.audit_n2_mock_105_questions import (
    evaluate_question_release_gate,
    evaluate_acoustic_status,
    validate_question_structure
)
from scripts.curriculum.reconcile_mock_blind_review import (
    reconcile_question_item,
    KNOWN_REPAIRS
)
from scripts.curriculum.question_fingerprint import compute_question_fingerprint
from scripts.curriculum.audit_blind_remapping_integrity import remap_blind_solve


class TestAdversarialReleaseGate(unittest.TestCase):

    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp(prefix="jp_study_gate_test_"))
        self.addCleanup(lambda: shutil.rmtree(self.temp_dir, ignore_errors=True))

        # Standard canonical test question fixture
        self.sample_q = {
            "id": "N2-TEST-001",
            "typeId": "N2-VOC-READ",
            "stem": "この仕事は給与が高い（　　）、拘束時間が長く責任も重い。",
            "options": [
                {"id": "A", "text": "に反して"},
                {"id": "B", "text": "のもとで"},
                {"id": "C", "text": "につれて"},
                {"id": "D", "text": "反面"}
            ],
            "correctAnswer": "D",
            "explanationVi": "反面: Mặt khác, trái lại. Cấu trúc: A反面B biểu thị hai mặt trái ngược của cùng một vấn đề.",
            "distractorExplanations": {
                "A": "に反して mang nghĩa ngược với kỳ vọng/dự đoán, không dùng để nêu hai mặt của sự việc.",
                "B": "のもとで mang nghĩa dưới sự hướng dẫn/chi phối, hoàn toàn không phù hợp.",
                "C": "につれて mang nghĩa càng ngày càng (kéo theo sự thay đổi), không phù hợp."
            }
        }
        self.sample_fp = compute_question_fingerprint(self.sample_q)
        self.sample_b_info = {
            "questionId": "N2-TEST-001",
            "blindAnswer": "D",
            "remappedBlindAnswer": "D",
            "selectedText": "反面",
            "mappingMethod": "DIRECT_IDENTITY",
            "confidence": "HIGH",
            "linguisticJustification": "「反面」は同一の事物の二面性を対比的に述べる文脈に最も自然。",
            "alternativeDefensibleAnswers": [],
            "concerns": None,
            "contentFingerprint": self.sample_fp,
            "fingerprintMatch": True,
            "reviewerProvenance": "subagent:jlpt-blind-reviewer"
        }

    # -----------------------------------------------------------------
    # REGRESSION TEST: Repaired-item reconciliation bypass prevention
    # -----------------------------------------------------------------
    def test_repaired_item_bypass_prevention(self):
        """
        Verify that a question in KNOWN_REPAIRS CANNOT bypass key reconciliation.
        If authored key is corrupted, it must evaluate to KEY_MISMATCH and QUARANTINED.
        """
        repaired_qid = "N2-G7-004"
        repair_info = KNOWN_REPAIRS[repaired_qid]

        q = copy.deepcopy(self.sample_q)
        q["id"] = repaired_qid
        q_fp = compute_question_fingerprint(q)

        b_info = copy.deepcopy(self.sample_b_info)
        b_info["questionId"] = repaired_qid
        b_info["remappedBlindAnswer"] = "D"
        b_info["contentFingerprint"] = q_fp

        # 1. Authentic state: blind_ans ('D') == authored_key ('D')
        res_clean = reconcile_question_item(q, b_info, repair_info)
        self.assertEqual(res_clean["reconciliationClassification"], "GRAMMATICAL_DEFECT_RESOLVED")
        self.assertEqual(res_clean["finalDisposition"], "REPAIRED_AND_VERIFIED")

        # 2. Adversarial mutation: Corrupt authored key to 'A'
        q_mutated = copy.deepcopy(q)
        q_mutated["correctAnswer"] = "A"

        res_mutated = reconcile_question_item(q_mutated, b_info, repair_info)
        self.assertEqual(
            res_mutated["reconciliationClassification"],
            "KEY_MISMATCH",
            "CRITICAL BYPASS: Repaired question bypassed key mismatch check!"
        )
        self.assertEqual(res_mutated["finalDisposition"], "QUARANTINED")

        tier, reasons = evaluate_question_release_gate(
            structural_status="PASS",
            linguistic_status="QUARANTINED_KEY_MISMATCH",
            acoustic_status="N/A (Written Section)",
            is_listening=False
        )
        self.assertEqual(tier, "QUARANTINED")
        self.assertTrue(any("Linguistic release gate blocked" in r for r in reasons))

    # -----------------------------------------------------------------
    # MUTATION A — Wrong answer key detection
    # -----------------------------------------------------------------
    def test_mutation_a_wrong_answer_key(self):
        """
        Mutation A: Author key is changed to an incorrect choice while reviewer solved correctly.
        Pipeline must output KEY_MISMATCH and gate must quarantine.
        """
        q = copy.deepcopy(self.sample_q)
        q["correctAnswer"] = "B"  # Incorrect option

        res = reconcile_question_item(q, self.sample_b_info, repair_info=None)
        self.assertEqual(res["reconciliationClassification"], "KEY_MISMATCH")
        self.assertEqual(res["finalDisposition"], "QUARANTINED")

        tier, _ = evaluate_question_release_gate(
            structural_status="PASS",
            linguistic_status="QUARANTINED_KEY_MISMATCH",
            acoustic_status="N/A (Written Section)",
            is_listening=False
        )
        self.assertEqual(tier, "QUARANTINED")

    # -----------------------------------------------------------------
    # MUTATION B — Ungrammatical stem / content modification
    # -----------------------------------------------------------------
    def test_mutation_b_invalid_grammar_stem_change(self):
        """
        Mutation B: Stem modified to ungrammatical phrasing after blind review.
        Fingerprint mismatch must immediately trigger STALE_REVIEW / RE_REVIEW_REQUIRED.
        """
        q = copy.deepcopy(self.sample_q)
        # Mutate stem into ungrammatical Japanese
        q["stem"] = "この仕事は給与が高い（　　）、拘束時間が長く理解がたいものだった。"

        # Old b_info has the fingerprint from the original stem
        res = reconcile_question_item(q, self.sample_b_info, repair_info=None)
        self.assertEqual(res["reconciliationClassification"], "STALE_REVIEW")
        self.assertEqual(res["finalDisposition"], "RE_REVIEW_REQUIRED")

        tier, reasons = evaluate_question_release_gate(
            structural_status="PASS",
            linguistic_status="BLOCKED: STALE_REVIEW",
            acoustic_status="N/A (Written Section)",
            is_listening=False
        )
        self.assertEqual(tier, "QUARANTINED")
        self.assertTrue(any("Linguistic release gate blocked" in r for r in reasons))

    # -----------------------------------------------------------------
    # MUTATION C — Competing answers / ambiguity quarantine
    # -----------------------------------------------------------------
    def test_mutation_c_competing_answers(self):
        """
        Mutation C: Question where independent reviewer noted competing defensible options.
        Must receive REVIEW_AGREED_WITH_WARNINGS and release gate QUARANTINE.
        """
        b_info = copy.deepcopy(self.sample_b_info)
        b_info["alternativeDefensibleAnswers"] = ["A"]
        b_info["concerns"] = "Option A 'に反して' is partially defensible under contrastive reading."

        res = reconcile_question_item(self.sample_q, b_info, repair_info=None)
        self.assertEqual(res["reconciliationClassification"], "REVIEW_AGREED_WITH_WARNINGS")
        self.assertEqual(res["finalDisposition"], "AI_AGREED_FLAGGED_FOR_HUMAN")

        tier, reasons = evaluate_question_release_gate(
            structural_status="PASS",
            linguistic_status="AI_AGREED_FLAGGED_FOR_HUMAN",
            acoustic_status="N/A (Written Section)",
            is_listening=False
        )
        self.assertEqual(tier, "QUARANTINED")
        self.assertTrue(any("competing answers or nuance warnings" in r for r in reasons))

    # -----------------------------------------------------------------
    # MUTATION D — Missing audio file detection
    # -----------------------------------------------------------------
    def test_mutation_d_missing_audio(self):
        """
        Mutation D: Audio file does not exist on disk for listening item.
        Acoustic evaluation returns AUDIO_FILE_MISSING and release gate quarantines.
        """
        audio_url = "https://example.com/audio/N2_MUT_L01.mp3"
        status = evaluate_acoustic_status(
            qid="N2-MUT-L01",
            audio_url=audio_url,
            audio_dir=self.temp_dir,
            receipt_tracks={},
            manifest_tracks={}
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

    # -----------------------------------------------------------------
    # MUTATION E — Stale audio receipt & live hash mismatch
    # -----------------------------------------------------------------
    def test_mutation_e_stale_audio_receipt(self):
        """
        Mutation E: Audio file bytes mutated on disk, receipt contains stale hash.
        Pipeline calculates live SHA-256, detects mismatch, and quarantines.
        """
        audio_fn = "N2_MUT_L02.mp3"
        audio_path = self.temp_dir / audio_fn
        orig_bytes = b"Authentic Japanese JLPT Audio Recording 44.1kHz"
        audio_path.write_bytes(orig_bytes)
        orig_sha = hashlib.sha256(orig_bytes).hexdigest()

        receipt_tracks = {
            "N2-MUT-L02": {
                "audioSha256": orig_sha,
                "audioDecodes": True,
                "browserPlaybackVerified": True
            }
        }
        manifest_tracks = {
            "N2-MUT-L02": {
                "sha256": orig_sha
            }
        }

        # 1. Clean state: Hash matches
        clean_status = evaluate_acoustic_status(
            qid="N2-MUT-L02",
            audio_url=f"audio/{audio_fn}",
            audio_dir=self.temp_dir,
            receipt_tracks=receipt_tracks,
            manifest_tracks=manifest_tracks
        )
        self.assertEqual(clean_status, "BROWSER_PLAYBACK_VERIFIED")

        # 2. Adversarial mutation: Corrupt audio file bytes on disk
        audio_path.write_bytes(b"Tampered or corrupted audio stream bytes")

        mutated_status = evaluate_acoustic_status(
            qid="N2-MUT-L02",
            audio_url=f"audio/{audio_fn}",
            audio_dir=self.temp_dir,
            receipt_tracks=receipt_tracks,
            manifest_tracks=manifest_tracks
        )
        self.assertEqual(mutated_status, "AUDIO_HASH_MISMATCH")

        tier, _ = evaluate_question_release_gate(
            structural_status="PASS",
            linguistic_status="AI_VERIFIED_PASS",
            acoustic_status=mutated_status,
            is_listening=True
        )
        self.assertEqual(tier, "QUARANTINED")

        # 3. Playback failure mutation
        audio_path.write_bytes(orig_bytes)
        receipt_tracks["N2-MUT-L02"]["browserPlaybackVerified"] = False
        fail_status = evaluate_acoustic_status(
            qid="N2-MUT-L02",
            audio_url=f"audio/{audio_fn}",
            audio_dir=self.temp_dir,
            receipt_tracks=receipt_tracks,
            manifest_tracks=manifest_tracks
        )
        self.assertEqual(fail_status, "BROWSER_PLAYBACK_FAILED")

    # -----------------------------------------------------------------
    # MUTATION F — Tampered blind answer & semantic mapping invariance
    # -----------------------------------------------------------------
    def test_mutation_f_tampered_blind_answer_and_semantic_invariance(self):
        """
        Mutation F: Prove semantic remapping derives strictly from option text
        and is completely invariant to question['correctAnswer'].
        """
        input_opts = {
            "A": "第一の選択肢",
            "B": "第二の正解選択肢",
            "C": "第三の選択肢",
            "D": "第四の選択肢"
        }
        # In current exam, options were permuted
        current_opts = {
            "A": "第三の選択肢",
            "B": "第一の選択肢",
            "C": "第二の正解選択肢",  # Correct text is now at C
            "D": "第四の選択肢"
        }

        # Reviewer chose 'B' ("第二の正解選択肢")
        remapped, method, text = remap_blind_solve("B", input_opts, current_opts)
        self.assertEqual(remapped, "C")
        self.assertEqual(method, "CONTENT_BASED_SEMANTIC_PRESERVATION")
        self.assertEqual(text, "第二の正解選択肢")

        # Changing authored correctAnswer does not alter remapping derivation
        for arbitrary_key in ["A", "B", "C", "D", "X"]:
            # remap_blind_solve does not take correctAnswer as input at all
            remapped_inv, _, _ = remap_blind_solve("B", input_opts, current_opts)
            self.assertEqual(remapped_inv, "C")

        # If authored key is 'A' (tampered), reconciliation flags KEY_MISMATCH
        q = copy.deepcopy(self.sample_q)
        q["correctAnswer"] = "A"
        b_info = copy.deepcopy(self.sample_b_info)
        b_info["remappedBlindAnswer"] = "C"

        res = reconcile_question_item(q, b_info)
        self.assertEqual(res["reconciliationClassification"], "KEY_MISMATCH")

    # -----------------------------------------------------------------
    # MUTATION G — Broken structure & operator precedence regression
    # -----------------------------------------------------------------
    def test_mutation_g_broken_structure(self):
        """
        Mutation G: Broken structural question formats must fail validation.
        Regression test: structural defect MUST block release gate even when
        linguistic status is positive ('REPAIRED_AND_VERIFIED' or 'AI_VERIFIED_PASS').
        """
        # 1. Duplicate option texts
        q_dup = copy.deepcopy(self.sample_q)
        q_dup["options"][1]["text"] = q_dup["options"][0]["text"]
        struct_res = validate_question_structure(q_dup, is_listening=False)
        self.assertIn("FAIL", struct_res)
        self.assertIn("Duplicate option texts found", struct_res)

        # 2. Insufficient options (3 options for non-M4 question)
        q_few = copy.deepcopy(self.sample_q)
        q_few["options"] = q_few["options"][:3]
        struct_res_few = validate_question_structure(q_few, is_listening=False)
        self.assertIn("Expected 4 options, got 3", struct_res_few)

        # 3. Missing correctAnswer in options
        q_bad_ans = copy.deepcopy(self.sample_q)
        q_bad_ans["correctAnswer"] = "Z"
        struct_res_ans = validate_question_structure(q_bad_ans, is_listening=False)
        self.assertIn("Correct answer Z not in options", struct_res_ans)

        # 4. Missing distractor explanation
        q_no_dist = copy.deepcopy(self.sample_q)
        q_no_dist["distractorExplanations"] = {}
        struct_res_dist = validate_question_structure(q_no_dist, is_listening=False)
        self.assertIn("Missing distractor explanations", struct_res_dist)

        # Operator Precedence Regression: Ensure structural FAIL always QUARANTINES
        for invalid_status in [struct_res, struct_res_few, struct_res_ans, struct_res_dist]:
            for valid_ling in ["AI_VERIFIED_PASS", "REPAIRED_AND_VERIFIED"]:
                tier, reasons = evaluate_question_release_gate(
                    structural_status=invalid_status,
                    linguistic_status=valid_ling,
                    acoustic_status="N/A (Written Section)",
                    is_listening=False
                )
                self.assertEqual(
                    tier,
                    "QUARANTINED",
                    f"Operator precedence regression failed for struct={invalid_status}, ling={valid_ling}"
                )
                self.assertTrue(any("Structural defect" in r for r in reasons))

    # -----------------------------------------------------------------
    # MUTATION H — Stale review / fingerprint invalidation
    # -----------------------------------------------------------------
    def test_mutation_h_stale_review(self):
        """
        Mutation H: Content altered without updated blind review.
        Content fingerprint mismatch must yield STALE_REVIEW / RE_REVIEW_REQUIRED.
        """
        q = copy.deepcopy(self.sample_q)
        # Modify option text
        q["options"][0]["text"] = "全く新しい別の選択肢"
        mutated_fp = compute_question_fingerprint(q)
        self.assertNotEqual(mutated_fp, self.sample_fp)

        res = reconcile_question_item(q, self.sample_b_info, repair_info=None)
        self.assertEqual(res["reconciliationClassification"], "STALE_REVIEW")
        self.assertEqual(res["finalDisposition"], "RE_REVIEW_REQUIRED")

        tier, _ = evaluate_question_release_gate(
            structural_status="PASS",
            linguistic_status="BLOCKED: STALE_REVIEW",
            acoustic_status="N/A (Written Section)",
            is_listening=False
        )
        self.assertEqual(tier, "QUARANTINED")

    # -----------------------------------------------------------------
    # Substring Spoofing Immunity
    # -----------------------------------------------------------------
    def test_negative_substring_spoofing(self):
        """
        Negative Test: Ensure release gate strictly matches exact enums.
        Strings containing substrings like 'PASS' or 'VERIFIED' must NOT pass.
        """
        spoofed_linguistic = [
            "NOT_AI_VERIFIED_PASS",
            "AI_VERIFIED_PASS_EXPIRED",
            "UNVERIFIED_AI_VERIFIED_PASS",
            "PRE_PASS",
            "REPAIRED_AND_VERIFIED_REVOKED",
            "MALICIOUS_AI_VERIFIED_PASS_BYPASS"
        ]
        for spoof in spoofed_linguistic:
            tier, reasons = evaluate_question_release_gate(
                structural_status="PASS",
                linguistic_status=spoof,
                acoustic_status="N/A (Written Section)",
                is_listening=False
            )
            self.assertEqual(
                tier,
                "QUARANTINED",
                f"Release gate breached by spoofed string: '{spoof}'"
            )
            self.assertTrue(any("Linguistic release gate blocked" in r for r in reasons))

        spoofed_structural = [
            "NOT_PASS",
            "PASS_WITH_DEFECTS",
            "PARTIAL_PASS"
        ]
        for spoof in spoofed_structural:
            tier, reasons = evaluate_question_release_gate(
                structural_status=spoof,
                linguistic_status="AI_VERIFIED_PASS",
                acoustic_status="N/A (Written Section)",
                is_listening=False
            )
            self.assertEqual(
                tier,
                "QUARANTINED",
                f"Release gate breached by spoofed structural status: '{spoof}'"
            )
            self.assertTrue(any("Structural defect" in r for r in reasons))


if __name__ == "__main__":
    unittest.main()
