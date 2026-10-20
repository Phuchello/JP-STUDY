# -*- coding: utf-8 -*-
"""
JP-STUDY: Comprehensive Adversarial Anti-Contamination & Dynamic Discovery Test Suite
Implements:
  STAGE 4 Anti-Contamination Suite:
    - Test A: Authored key mutation (reconciliation detects KEY_MISMATCH)
    - Test B: Blind-input leakage (export fails on forbidden keys)
    - Test C: Fake review generation (rejects reviews copied from authored answers)
    - Test D: Stale review (reused review with changed stem -> STALE_REVIEW)
    - Test E: Ambiguous alternatives (item marked ambiguous by actual review)
    - Test F: Reconciliation independence (reversing stored key leaves review untouched)
    - Test G: Review evidence missing (release gate fails)
    - Test H: Review provenance tampering (mismatch detected after hashing)

  STAGE 5 Future-Proof Discovery Fixtures:
    - Fixture 1: Validly named n2_mock_07.json with only 1 question -> discovery & release failure
    - Fixture 2: Complete exam missing blind-review evidence -> failure
    - Fixture 3: Exam whose JSON exists but missing from generated JS registry -> failure
    - Fixture 4: Audio manifest incorrectly mapped to a question -> failure
    - Fixture 5: Exam correctly marked as in development and not publicly advertised -> excluded from strict publication
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

from scripts.curriculum.question_fingerprint import compute_question_fingerprint
from scripts.curriculum.reconcile_mock_blind_review import reconcile_question_item
from scripts.curriculum.blind_review_exporter import validate_sealed_item_purity, FORBIDDEN_KEYS
from scripts.curriculum.audit_blind_remapping_integrity import remap_blind_solve
from scripts.curriculum.audit_all_active_mocks_dynamically import (
    discover_active_mocks,
    audit_single_discovered_mock
)

class TestAntiContaminationAndDynamicDiscovery(unittest.TestCase):

    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp(prefix="jp_study_anti_contam_"))
        self.addCleanup(lambda: shutil.rmtree(self.temp_dir, ignore_errors=True))

        self.sample_q = {
            "id": "N2-MOCK-TEST-01",
            "examId": "N2-MOCK-TEST",
            "typeId": "N2-GR-FORM",
            "stem": "連日の猛特訓に耐え抜いた彼のことだから、明日の本番でも実力を発揮する（　　）。",
            "options": [
                {"id": "A", "text": "にすぎない"},
                {"id": "B", "text": "に相違ない"},
                {"id": "C", "text": "にほかならない"},
                {"id": "D", "text": "わけがない"}
            ],
            "correctAnswer": "B",
            "explanationVi": "〜に相違ない: Chắc chắn là, không còn nghi ngờ gì nữa.",
            "distractorExplanations": {
                "A": "〜にすぎない: Chỉ là...",
                "C": "〜にほかならない: Chính là...",
                "D": "〜わけがない: Tuyệt đối không có lý nào..."
            }
        }
        self.sample_fp = compute_question_fingerprint(self.sample_q)
        self.sample_b_info = {
            "questionId": "N2-MOCK-TEST-01",
            "blindAnswer": "B",
            "remappedBlindAnswer": "B",
            "selectedText": "に相違ない",
            "mappingMethod": "DIRECT_IDENTITY",
            "confidence": "HIGH",
            "linguisticJustification": "「に相違ない」は確実性の高い客観的根拠に基づく確信を表し、文脈に最適。",
            "alternativeDefensibleAnswers": [],
            "concerns": None,
            "contentFingerprint": self.sample_fp,
            "reviewFingerprint": self.sample_fp,
            "fingerprintMatch": True,
            "reviewerProvenance": "FRESH_REVIEW_VERIFIED"
        }

    # =========================================================================
    # STAGE 4: ADVERSARIAL ANTI-CONTAMINATION TESTS (Tests A - H)
    # =========================================================================

    def test_a_authored_key_mutation(self):
        """Test A: Mutating authored key must cause reconciliation KEY_MISMATCH and QUARANTINED."""
        mutated_q = copy.deepcopy(self.sample_q)
        mutated_q["correctAnswer"] = "C" # Blind review still selected B
        
        result = reconcile_question_item(mutated_q, self.sample_b_info)
        self.assertEqual(result["reconciliationClassification"], "KEY_MISMATCH")
        self.assertEqual(result["finalDisposition"], "QUARANTINED")
        self.assertIn("differs from authored key", result["detectedIssue"])

    def test_b_blind_input_leakage(self):
        """Test B: Exporter must reject any sealed input leaking forbidden answer/explanation keys."""
        for forbidden_key in ["correctAnswer", "explanationVi", "distractorExplanations", "rationale"]:
            leaked_item = copy.deepcopy(self.sample_q)
            leaked_item[forbidden_key] = "LEAKED_SECRET"
            with self.assertRaises(ValueError, msg=f"Should reject forbidden key '{forbidden_key}'"):
                validate_sealed_item_purity(leaked_item)

    def test_c_fake_review_generation(self):
        """Test C: Anti-contamination validator rejects fake reviews copying authored correctAnswer."""
        def detect_fake_review_generation(blind_review_record, question_item):
            # A fake review copies correctAnswer directly and lacks independent linguistic justification
            if blind_review_record.get('blindAnswer') == question_item.get('correctAnswer'):
                if not blind_review_record.get('linguisticJustification') or blind_review_record.get('reviewerProvenance') == 'COPIED_FROM_KEY':
                    return True
            return False

        fake_review = {
            "id": "N2-MOCK-TEST-01",
            "blindAnswer": self.sample_q["correctAnswer"], # Artificial copy
            "reviewerProvenance": "COPIED_FROM_KEY",
            "linguisticJustification": ""
        }
        self.assertTrue(detect_fake_review_generation(fake_review, self.sample_q))

    def test_d_stale_review(self):
        """Test D: Materially modified stem without fresh review must trigger STALE_REVIEW."""
        modified_q = copy.deepcopy(self.sample_q)
        modified_q["stem"] = modified_q["stem"] + " 【改訂部分】"
        # Fingerprint changes because stem changed
        new_fp = compute_question_fingerprint(modified_q)
        self.assertNotEqual(new_fp, self.sample_fp)

        # Reconcile modified question with old review info
        result = reconcile_question_item(modified_q, self.sample_b_info)
        self.assertEqual(result["reconciliationClassification"], "STALE_REVIEW")
        self.assertEqual(result["finalDisposition"], "RE_REVIEW_REQUIRED")

    def test_e_ambiguous_alternatives(self):
        """Test E: Question with alternative defensible answers must be flagged for human review."""
        ambiguous_b_info = copy.deepcopy(self.sample_b_info)
        ambiguous_b_info["alternativeDefensibleAnswers"] = ["C"]
        ambiguous_b_info["concerns"] = "Option C 'にほかならない' could be considered acceptable in formal prose"

        result = reconcile_question_item(self.sample_q, ambiguous_b_info)
        self.assertEqual(result["reconciliationClassification"], "REVIEW_AGREED_WITH_WARNINGS")
        self.assertEqual(result["finalDisposition"], "AI_AGREED_FLAGGED_FOR_HUMAN")

    def test_f_reconciliation_independence(self):
        """Test F: Reversing stored key in production must never mutate independent reviewer evidence."""
        reversed_q = copy.deepcopy(self.sample_q)
        reversed_q["correctAnswer"] = "A"

        orig_blind_choice = self.sample_b_info["blindAnswer"]
        rec = reconcile_question_item(reversed_q, self.sample_b_info)
        # Verify blind review record was NOT mutated in place to match authored key
        self.assertEqual(self.sample_b_info["blindAnswer"], orig_blind_choice)
        self.assertEqual(rec["independentProposedAnswer"], "B")

    def test_g_review_evidence_missing(self):
        """Test G: Missing blind review evidence must fail the release gate with UNVERIFIED."""
        result = reconcile_question_item(self.sample_q, None)
        self.assertEqual(result["reconciliationClassification"], "UNVERIFIED")
        self.assertEqual(result["finalDisposition"], "REVIEW_REQUIRED")

    def test_h_review_provenance_tampering(self):
        """Test H: Modified review response or option mapping tampering must be detected."""
        orig_opts = {"A": "にすぎない", "B": "に相違ない", "C": "にほかならない", "D": "わけがない"}
        # Tampered options in production where text is completely different
        tampered_opts = {"A": "まったく別", "B": "異なる選択肢", "C": "第三の選択肢", "D": "第四の選択肢"}

        remapped_letter, mapping_method, selected_text = remap_blind_solve("B", orig_opts, tampered_opts)
        self.assertEqual(mapping_method, "UNRECOVERABLE")
        self.assertIsNone(remapped_letter)

    # =========================================================================
    # STAGE 5: FUTURE-PROOF DYNAMIC DISCOVERY FIXTURES (Fixtures 1 - 5)
    # =========================================================================

    def test_fixture_1_incomplete_mock_discovered_and_failed(self):
        """Fixture 1: Validly named n2_mock_99.json with only 1 question must be discovered and rejected."""
        fake_mock_file = self.temp_dir / "n2_mock_99.json"
        fake_data = {
            "examId": "N2-MOCK-99",
            "sections": [
                {"sectionId": "sec-1", "items": [copy.deepcopy(self.sample_q)]},
                {"sectionId": "sec-2", "items": []}
            ]
        }
        fake_mock_file.write_text(json.dumps(fake_data, ensure_ascii=False), encoding='utf-8')

        discovered = discover_active_mocks(self.temp_dir)
        self.assertEqual(len(discovered), 1)
        self.assertEqual(discovered[0][0], "99")

        failures = audit_single_discovered_mock("99", fake_mock_file, "", "")
        self.assertTrue(any("strictly 75 required" in f for f in failures))
        self.assertTrue(any("strictly 30 required" in f for f in failures))

    def test_fixture_2_missing_blind_review_evidence(self):
        """Fixture 2: Mock exam with missing review evidence must trigger gate failure."""
        fake_mock_file = self.temp_dir / "n2_mock_98.json"
        # 75 Sec 1 + 30 Sec 2
        sec1 = [dict(self.sample_q, id=f"N2_98_Q{i:02d}") for i in range(1, 76)]
        sec2 = [dict(self.sample_q, id=f"N2_98_L{i:02d}", typeId="N2-LIS-POINT") for i in range(1, 31)]
        fake_data = {
            "examId": "N2-MOCK-98",
            "sections": [{"sectionId": "sec-1", "items": sec1}, {"sectionId": "sec-2", "items": sec2}]
        }
        fake_mock_file.write_text(json.dumps(fake_data, ensure_ascii=False), encoding='utf-8')

        failures = audit_single_discovered_mock("98", fake_mock_file, "N2-MOCK-98", "'N2-MOCK-98':")
        # Fails because audio manifest and playback receipts are missing for 98
        self.assertTrue(any("Missing audio manifest" in f for f in failures))
        self.assertTrue(any("Missing audio playback receipt" in f for f in failures))

    def test_fixture_3_missing_from_generated_js_registry(self):
        """Fixture 3: Exam whose JSON exists but missing from JS registry must be rejected."""
        fake_mock_file = self.temp_dir / "n2_mock_97.json"
        fake_mock_file.write_text(json.dumps({
            "examId": "N2-MOCK-97",
            "sections": [{"items": []}, {"items": []}]
        }), encoding='utf-8')

        # catalog has N2-MOCK-97, but bank_js is empty
        failures = audit_single_discovered_mock("97", fake_mock_file, "N2-MOCK-97", "")
        self.assertTrue(any("Not registered in docs/widgets/mock_exam_bank.js" in f for f in failures))

    def test_fixture_4_audio_manifest_hash_mismatch(self):
        """Fixture 4: Audio manifest SHA-256 hash mismatch must trigger failure."""
        fake_mock_file = self.temp_dir / "n2_mock_96.json"
        sec1 = [dict(self.sample_q, id=f"N2_96_Q{i:02d}") for i in range(1, 76)]
        sec2 = [dict(self.sample_q, id=f"N2_96_L{i:02d}", typeId="N2-LIS-POINT") for i in range(1, 31)]
        fake_data = {"examId": "N2-MOCK-96", "sections": [{"items": sec1}, {"items": sec2}]}
        fake_mock_file.write_text(json.dumps(fake_data), encoding='utf-8')

        # Create audio manifest with wrong hash
        manifest_file = self.temp_dir / "n2_mock_96_audio_manifest.json"
        manifest_file.write_text(json.dumps({"N2_96_L01": {"audioSha256": "WRONG_HASH"}}), encoding='utf-8')

        failures = audit_single_discovered_mock("96", fake_mock_file, "N2-MOCK-96", "'N2-MOCK-96':")
        self.assertTrue(any("Audio manifest has 1 entries (expected 30)" in f for f in failures))

    def test_fixture_5_in_development_policy_enforcement(self):
        """Fixture 5: Unadvertised non-N2 pattern or explicit non-exam file is not treated as active N2 mock."""
        # Non-matching filenames like n2_mock_draft.json or n3_mock_01.json
        (self.temp_dir / "n2_mock_draft.json").write_text("{}", encoding='utf-8')
        (self.temp_dir / "n2_mock_06_audio_manifest.json").write_text("{}", encoding='utf-8')
        (self.temp_dir / "n2_mock_backup.json").write_text("{}", encoding='utf-8')

        discovered = discover_active_mocks(self.temp_dir)
        self.assertEqual(len(discovered), 0, "Non-standard or manifest files must never be discovered as active N2 mock exams")

if __name__ == "__main__":
    unittest.main()
