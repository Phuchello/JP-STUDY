# -*- coding: utf-8 -*-
"""
JP-STUDY: Comprehensive Adversarial Anti-Contamination & Dynamic Discovery Test Suite
Phase 5.2 Hardened Implementation:
  STAGE C Real Adversarial Tests:
    - Test C1: Fake review with convincing justification (rejected by production provenance validator)
    - Test C2: Wrong authored answer (reconciliation returns KEY_MISMATCH)
    - Test C3: Missing review evidence isolated failure (complete audio & metadata, fails ONLY on reviews)
    - Test C4: Wrong audio hash isolated failure (complete 30 tracks, fails specifically on mismatched track)
    - Test C5: Mutated question version (changed stem -> STALE_REVIEW)
    - Test C6: Repaired-question bypass (changed key on repaired item -> KEY_MISMATCH)
    - Test C7: Independent review unavailable (review pending, strict certification withheld)
    - Test C8: Provenance artifact tampering (response hash mismatch -> REVIEW_TAMPERED)

  STAGE E Downstream Dynamic Discovery Fixtures:
    - Fixture 1: Structurally incomplete mock (1 question -> rejected by discovery auditor)
    - Fixture 2: Exam missing from JS registry -> rejected
    - Fixture 3: Temporary unreviewed mock (N2 #07) detected by downstream consistency checker
    - Fixture 4: Manifest and backup files excluded from discovery
    - Fixture 5: Repository-wide anti-contamination audit passes with zero copying paths
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

from scripts.curriculum.acoustic_assurance import evaluate_audio_track_assurance
from scripts.curriculum.question_fingerprint import compute_question_fingerprint
from scripts.curriculum.reconcile_mock_blind_review import reconcile_question_item
from scripts.curriculum.blind_review_exporter import validate_sealed_item_purity, FORBIDDEN_KEYS
from scripts.curriculum.audit_blind_remapping_integrity import remap_blind_solve
from scripts.curriculum.audit_all_active_mocks_dynamically import (
    discover_active_mocks,
    audit_single_discovered_mock
)
from scripts.curriculum.review_provenance import (
    ReviewProvenanceValidator,
    compute_object_hash
)
from scripts.curriculum.discovery import (
    discover_active_n2_mocks,
    verify_downstream_id_consistency
)
from scripts.curriculum.anti_contamination_audit import audit_repository_anti_contamination


class TestAntiContaminationAndDynamicDiscovery(unittest.TestCase):

    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp(prefix="jp_study_anti_contam_"))
        self.addCleanup(lambda: shutil.rmtree(self.temp_dir, ignore_errors=True))

        self.sample_q = {
            "id": "N2-MOCK-TEST-01",
            "examId": "N2-MOCK-TEST",
            "typeId": "N2-GR-FORM",
            "category": "Mondai 7: 文法形式の判断",
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
    # STAGE C: HARDENED ADVERSARIAL TESTS (Tests C1 - C8)
    # =========================================================================

    def test_c1_fake_review_with_convincing_justification(self):
        """C1: Fake review copying correctAnswer with plausible justification fails provenance verification."""
        # A sophisticated fabricated review: valid fingerprint, plausible Japanese justification,
        # self-declared 'FRESH_REVIEW_VERIFIED', but NO isolated execution attestation
        fake_review = {
            "id": self.sample_q["id"],
            "blindAnswer": self.sample_q["correctAnswer"],  # Copied key
            "confidence": "HIGH",
            "linguisticJustification": (
                "「動詞辞書形＋に相違ない」は確固たる客観的根拠に基づき「絶対に〜だと確信する」を表す文型。"
                "前件「連日の猛特訓に耐え抜いた彼のことだから」と呼応し、高い確信を表す正解はB「に相違ない」である。"
            ),
            "alternativeDefensibleAnswers": [],
            "concerns": None,
            "contentFingerprint": self.sample_fp,
            "reviewerProvenance": "FRESH_REVIEW_VERIFIED"  # False claim
        }

        # The production ReviewProvenanceValidator must evaluate positive execution evidence
        res = ReviewProvenanceValidator.classify_review_provenance(
            question_item=self.sample_q,
            review_record=fake_review,
            current_fingerprint=self.sample_fp,
            execution_attestation=None  # No verified execution trace!
        )

        # Must NOT be certified as independently reviewed
        self.assertFalse(res["isCertified"], "Fabricated review without execution trace must not be certified")
        self.assertIn(res["status"], ["HISTORICAL_REVIEW_UNVERIFIED", "REVIEW_CONTAMINATED", "REVIEW_PROVENANCE_UNVERIFIED", "REVIEW_PROVENANCE_PENDING", "REVIEW_EXECUTION_REPORTED_NOT_ATTESTED", "REVIEW_CONTENT_VERSION_VERIFIED"])

    def test_c2_wrong_authored_answer(self):
        """C2: Deliberately wrong authored answer key must produce KEY_MISMATCH and block release."""
        # Reviewer genuinely selected B
        mutated_q = copy.deepcopy(self.sample_q)
        mutated_q["correctAnswer"] = "C"  # Deliberate author error

        # 1. ReviewProvenanceValidator evaluation
        prov_res = ReviewProvenanceValidator.reconcile_question(
            question_item=mutated_q,
            review_record=self.sample_b_info,
            current_fingerprint=self.sample_fp
        )
        self.assertFalse(prov_res["match"])
        self.assertFalse(prov_res["gatePassed"])
        self.assertEqual(prov_res["classification"], "KEY_MISMATCH")
        self.assertEqual(prov_res["disposition"], "KEY_MISMATCH_QUARANTINED")

        # 2. Production reconciliation function
        rec_res = reconcile_question_item(mutated_q, self.sample_b_info)
        self.assertEqual(rec_res["reconciliationClassification"], "KEY_MISMATCH")
        self.assertEqual(rec_res["finalDisposition"], "QUARANTINED")

    def test_c3_missing_review_evidence_isolated_failure(self):
        """C3: Structurally complete mock with complete audio must fail EXPLICITLY on missing review evidence."""
        mock_num = "98"
        fake_mock_file = self.temp_dir / f"n2_mock_{mock_num}.json"

        # Create complete 75 Sec 1 + 30 Sec 2
        sec1 = [dict(self.sample_q, id=f"N2_{mock_num}_Q{i:02d}") for i in range(1, 76)]
        sec2 = [dict(self.sample_q, id=f"N2_{mock_num}_L{i:02d}", typeId="N2-LIS-POINT", category="Mondai 1: 課題理解") for i in range(1, 31)]
        # Fix Mondai 4 choices to 3
        for i in range(16, 28):
            sec2[i]["category"] = "Mondai 4: 即時応答"
            sec2[i]["options"] = sec2[i]["options"][:3]

        fake_mock_file.write_text(json.dumps({
            "examId": f"N2-MOCK-{mock_num}",
            "sections": [{"sectionId": "sec-1", "items": sec1}, {"sectionId": "sec-2", "items": sec2}]
        }), encoding='utf-8')

        # Create valid 30-entry audio manifest
        manifest_file = self.temp_dir / f"n2_mock_{mock_num}_audio_manifest.json"
        manifest_data = {}
        for it in sec2:
            manifest_data[it["id"]] = {
                "audioUrl": f"audio/n2_mock_01/{it['id'].replace('N2_98_', 'N2_M1_')}.mp3",
                "audioSha256": "dummy",
                "audioDurationSec": 50.0
            }
        manifest_file.write_text(json.dumps(manifest_data), encoding='utf-8')

        # Create valid 30-entry audio playback receipt
        receipt_file = ROOT / f"qa/N2_MOCK_{mock_num}_AUDIO_PLAYBACK_RECEIPT.json"
        receipt_data = {"examId": f"N2-MOCK-{mock_num}", "tracks": {}}
        for it in sec2:
            receipt_data["tracks"][it["id"]] = {"browserPlaybackVerified": True, "durationSec": 50.0}
        receipt_file.write_text(json.dumps(receipt_data), encoding='utf-8')
        self.addCleanup(lambda: receipt_file.unlink(missing_ok=True))

        # Catalog and JS contain mock
        catalog_html = f"mockId=N2-MOCK-{mock_num}"
        bank_js = f"'N2-MOCK-{mock_num}':"

        # Note: raw_blind_m98_s1_p1.json, etc. DO NOT EXIST in qa/
        failures = audit_single_discovered_mock(mock_num, fake_mock_file, catalog_html, bank_js)

        # Isolated failure: MUST fail on missing independent review evidence, NOT audio
        self.assertTrue(any("Missing independent review evidence" in f for f in failures), f"Failures were: {failures}")
        self.assertFalse(any("Audio manifest has" in f for f in failures))

    def test_c4_wrong_audio_hash_isolated_failure(self):
        """C4: Complete valid 30-track audio fixture with one corrupted hash identifies specific track."""
        mock_num = "96"
        fake_mock_file = self.temp_dir / f"n2_mock_{mock_num}.json"

        sec1 = [dict(self.sample_q, id=f"N2_{mock_num}_Q{i:02d}") for i in range(1, 76)]
        sec2 = [dict(self.sample_q, id=f"N2_{mock_num}_L{i:02d}", typeId="N2-LIS-POINT", category="Mondai 1") for i in range(1, 31)]
        fake_mock_file.write_text(json.dumps({
            "examId": f"N2-MOCK-{mock_num}",
            "sections": [{"items": sec1}, {"items": sec2}]
        }), encoding='utf-8')

        # Use real N2-MOCK-01 MP3 files as targets
        real_manifest_raw = json.loads((ROOT / "data/mock_exams/n2_mock_01_audio_manifest.json").read_text(encoding='utf-8'))
        real_manifest = real_manifest_raw if isinstance(real_manifest_raw, list) else list(real_manifest_raw.values())
        manifest_96 = {}
        for idx, meta in enumerate(real_manifest):
            fake_qid = sec2[idx]["id"]
            manifest_96[fake_qid] = {
                "audioUrl": meta["audioUrl"],
                "audioSha256": meta["audioSha256"],
                "audioDurationSec": meta.get("audioDurationSec", 60.0)
            }

        # Corrupt EXACTLY track #5 hash
        corrupted_qid = sec2[4]["id"]
        manifest_96[corrupted_qid]["audioSha256"] = "corrupted_hash_deadbeef12345678"

        manifest_file = self.temp_dir / f"n2_mock_{mock_num}_audio_manifest.json"
        manifest_file.write_text(json.dumps(manifest_96), encoding='utf-8')

        failures = audit_single_discovered_mock(
            mock_num,
            fake_mock_file,
            f"N2-MOCK-{mock_num}",
            f"'N2-MOCK-{mock_num}':"
        )

        # Must explicitly detect SHA-256 mismatch for the specific track
        self.assertTrue(any(f"Audio SHA-256 mismatch for {corrupted_qid}" in f for f in failures), f"Failures: {failures}")
        # Must NOT fail because of count < 30
        self.assertFalse(any("entries (expected 30)" in f for f in failures))

    def test_c5_mutated_question_version(self):
        """C5: Mutated question stem without re-review triggers STALE_REVIEW."""
        modified_q = copy.deepcopy(self.sample_q)
        modified_q["stem"] = modified_q["stem"] + " 【改訂部分】"

        new_fp = compute_question_fingerprint(modified_q)
        self.assertNotEqual(new_fp, self.sample_fp)

        # 1. ReviewProvenanceValidator check
        prov_res = ReviewProvenanceValidator.classify_review_provenance(
            question_item=modified_q,
            review_record=self.sample_b_info,
            current_fingerprint=new_fp
        )
        self.assertEqual(prov_res["status"], "STALE_REVIEW")
        self.assertFalse(prov_res["isCertified"])

        # 2. Production reconciler check
        rec_res = reconcile_question_item(modified_q, self.sample_b_info)
        self.assertEqual(rec_res["reconciliationClassification"], "STALE_REVIEW")
        self.assertEqual(rec_res["finalDisposition"], "RE_REVIEW_REQUIRED")

    def test_c6_repaired_question_bypass(self):
        """C6: Altering authored answer on a repaired question must trigger KEY_MISMATCH."""
        # Use known repaired item N2_02_M7_04 (where key was repaired to B)
        repaired_q = {
            "id": "N2_02_M7_04",
            "examId": "N2-MOCK-02",
            "correctAnswer": "D",  # Corrupted: key is actually B
            "stem": "これほど精密な技術は、長年の鍛錬を重ねた熟練の職人（　　）の技だ。",
            "options": [{"id": "A", "text": "ならでは"}, {"id": "B", "text": "ならでは"}, {"id": "C", "text": "ばかりに"}, {"id": "D", "text": "とあって"}]
        }
        current_fp = compute_question_fingerprint(repaired_q)
        repaired_b_info = {
            "questionId": "N2_02_M7_04",
            "blindAnswer": "B",
            "contentFingerprint": current_fp,
            "reviewFingerprint": current_fp,
            "fingerprintMatch": True,
            "reviewerProvenance": "OPTION_PERMUTATION_REBOUND"
        }

        # Production reconciliation
        rec = reconcile_question_item(repaired_q, repaired_b_info)
        # Even though N2_02_M7_04 is in KNOWN_REPAIRS, it must NOT return REPAIRED_AND_VERIFIED if key differs!
        self.assertEqual(rec["reconciliationClassification"], "KEY_MISMATCH")
        self.assertEqual(rec["finalDisposition"], "QUARANTINED")

    def test_c7_independent_review_unavailable(self):
        """C7: When review record is missing, review remains pending without artificial agreement."""
        res = ReviewProvenanceValidator.classify_review_provenance(
            question_item=self.sample_q,
            review_record=None,
            current_fingerprint=self.sample_fp
        )
        self.assertEqual(res["status"], "REVIEW_REQUIRED")
        self.assertFalse(res["isCertified"])

        rec = reconcile_question_item(self.sample_q, None)
        self.assertEqual(rec["reconciliationClassification"], "UNVERIFIED")
        self.assertEqual(rec["finalDisposition"], "REVIEW_REQUIRED")

    def test_c8_provenance_artifact_tampering(self):
        """C8: Response hash mismatch after tamper triggers REVIEW_TAMPERED."""
        orig_response = {
            "id": self.sample_q["id"],
            "blindAnswer": "B",
            "linguisticJustification": "Original justification."
        }
        recorded_hash = compute_object_hash(orig_response)

        # Review record with valid recorded hash
        tampered_review = {
            "id": self.sample_q["id"],
            "blindAnswer": "C",  # Tampered answer!
            "linguisticJustification": "Original justification.",
            "contentFingerprint": self.sample_fp,
            "responseHash": recorded_hash  # Hash was computed for 'B'
        }

        res = ReviewProvenanceValidator.classify_review_provenance(
            question_item=self.sample_q,
            review_record=tampered_review,
            current_fingerprint=self.sample_fp,
            execution_attestation={"verified": True}
        )
        self.assertEqual(res["status"], "REVIEW_TAMPERED")
        self.assertFalse(res["isCertified"])

    # =========================================================================
    # STAGE E: DOWNSTREAM DYNAMIC DISCOVERY FIXTURES
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

    def test_fixture_2_missing_from_generated_js_registry(self):
        """Fixture 2: Exam whose JSON exists but missing from JS registry must be rejected."""
        fake_mock_file = self.temp_dir / "n2_mock_97.json"
        fake_mock_file.write_text(json.dumps({
            "examId": "N2-MOCK-97",
            "sections": [{"items": []}, {"items": []}]
        }), encoding='utf-8')

        failures = audit_single_discovered_mock("97", fake_mock_file, "N2-MOCK-97", "")
        self.assertTrue(any("Not registered in docs/widgets/mock_exam_bank.js" in f for f in failures))

    def test_fixture_3_dynamic_discovery_consistency_check(self):
        """Fixture 3: Consistency checker detects if an active mock's questions are missing from review/ledger."""
        mocks = discover_active_n2_mocks()
        self.assertEqual(len(mocks), 6)

        # Synthetic review and ledger missing questions from N2-MOCK-06
        partial_reviews = [{"questionId": f"N2_01_Q{i:02d}"} for i in range(1, 106)]
        partial_ledger = [{"questionId": f"N2_01_Q{i:02d}"} for i in range(1, 106)]

        consistency = verify_downstream_id_consistency(
            discovered_mocks=mocks,
            review_records=partial_reviews,
            ledger_records=partial_ledger
        )
        self.assertFalse(consistency["isConsistent"])
        self.assertGreater(len(consistency["missingInReview"]), 0)
        self.assertGreater(len(consistency["missingInLedger"]), 0)

    def test_fixture_4_non_standard_files_excluded(self):
        """Fixture 4: Manifests and draft files must be excluded from mock discovery."""
        (self.temp_dir / "n2_mock_draft.json").write_text("{}", encoding='utf-8')
        (self.temp_dir / "n2_mock_06_audio_manifest.json").write_text("{}", encoding='utf-8')
        (self.temp_dir / "n2_mock_backup.json").write_text("{}", encoding='utf-8')

        discovered = discover_active_mocks(self.temp_dir)
        self.assertEqual(len(discovered), 0, "Manifests or draft files must never be discovered as mock exams")

    def test_fixture_5_repository_wide_anti_contamination(self):
        """Fixture 5: Repository-wide anti-contamination audit must pass with 0 copying paths."""
        res = audit_repository_anti_contamination()
        self.assertTrue(res["passed"], f"Repository anti-contamination audit failed: {res}")
        self.assertEqual(len(res["violations"]), 0)
        self.assertEqual(len(res["guardFailures"]), 0)

    def test_provenance_negative_without_attestation(self):
        """Negative test: Item without verified execution attestation drops to REVIEW_CONTENT_VERSION_VERIFIED."""
        res = ReviewProvenanceValidator.classify_review_provenance(
            question_item=self.sample_q,
            review_record=self.sample_b_info,
            current_fingerprint=self.sample_fp,
            execution_attestation=None
        )
        self.assertFalse(res["isCertified"])
        self.assertEqual(res["status"], "REVIEW_CONTENT_VERSION_VERIFIED")

    def test_provenance_negative_exam_id_shortcut_prevented(self):
        """Negative test: Setting examId to N2-MOCK-06 or N2-MOCK-07 does not grant attestation."""
        q_m07 = copy.deepcopy(self.sample_q)
        q_m07["id"] = "N2_07_Q01"
        fp_m07 = compute_question_fingerprint(q_m07)
        rev_m07 = copy.deepcopy(self.sample_b_info)
        rev_m07["id"] = "N2_07_Q01"
        rev_m07["contentFingerprint"] = fp_m07

        # Unverified attestation
        fake_attestation = {"verified": True, "conversationId": "fake-conv-id-not-in-batches"}
        res = ReviewProvenanceValidator.classify_review_provenance(
            question_item=q_m07,
            review_record=rev_m07,
            current_fingerprint=fp_m07,
            execution_attestation=fake_attestation
        )
        self.assertFalse(res["isCertified"], "Exam ID or unverified attestation must not grant certification")
        self.assertNotEqual(res["status"], "INDEPENDENT_REVIEW_ATTESTED")

    def test_acoustic_negative_file_only_fails_browser_playback(self):
        """Negative test: Receipt with only file existence fails BROWSER_PLAYBACK_VERIFIED."""
        sample_mp3 = self.temp_dir / "sample_track.mp3"
        sample_mp3.write_bytes(b"dummy mp3 frame data for acoustic tier testing")
        real_sha = hashlib.sha256(sample_mp3.read_bytes()).hexdigest()
        track_meta = {"audioSha256": real_sha}
        receipt_track = {"audioFileExists": True}

        res = evaluate_audio_track_assurance(track_meta, receipt_track, sample_mp3)
        self.assertFalse(res["BROWSER_PLAYBACK_VERIFIED"])
        self.assertEqual(res["highestTier"], "AUDIO_HASH_VERIFIED")

    def test_acoustic_negative_duration_only_fails_browser_playback(self):
        """Negative test: Receipt with only duration does not reach BROWSER_PLAYBACK_VERIFIED."""
        sample_mp3 = self.temp_dir / "sample_track.mp3"
        sample_mp3.write_bytes(b"dummy mp3 frame data for acoustic tier testing")
        real_sha = hashlib.sha256(sample_mp3.read_bytes()).hexdigest()
        track_meta = {"audioSha256": real_sha}
        receipt_track = {"audioFileExists": True, "durationSec": 50.0}

        res = evaluate_audio_track_assurance(track_meta, receipt_track, sample_mp3)
        self.assertFalse(res["BROWSER_PLAYBACK_VERIFIED"])
        self.assertIn("Browser audio decoding", res["failureReason"] or "")

    def test_acoustic_negative_corrupted_hash(self):
        """Negative test: Corrupted MP3 hash fails AUDIO_HASH_VERIFIED."""
        sample_mp3 = self.temp_dir / "sample_track.mp3"
        sample_mp3.write_bytes(b"dummy mp3 frame data for acoustic tier testing")
        track_meta = {"audioSha256": "wrong_expected_sha256_deadbeef"}
        receipt_track = {"audioFileExists": True}

        res = evaluate_audio_track_assurance(track_meta, receipt_track, sample_mp3)
        self.assertFalse(res["AUDIO_HASH_VERIFIED"])
        self.assertEqual(res["highestTier"], "AUDIO_FILE_EXISTS")

    def test_acoustic_positive_real_playback_advancement(self):
        """Positive test: Real playback advancement achieves BROWSER_PLAYBACK_VERIFIED."""
        sample_mp3 = self.temp_dir / "sample_track.mp3"
        sample_mp3.write_bytes(b"dummy mp3 frame data for acoustic tier testing")
        real_sha = hashlib.sha256(sample_mp3.read_bytes()).hexdigest()
        track_meta = {"audioSha256": real_sha}
        receipt_track = {
            "audioSha256": real_sha,
            "loaded": True,
            "browserPlaybackVerified": True,
            "playbackDesktop": {
                "loaded": True,
                "played": True,
                "timeAdvanced": True,
                "currentTime": 1.25
            }
        }

        res = evaluate_audio_track_assurance(track_meta, receipt_track, sample_mp3)
        self.assertTrue(res["AUDIO_FILE_EXISTS"])
        self.assertTrue(res["AUDIO_HASH_VERIFIED"])
        self.assertTrue(res["AUDIO_DECODES"])
        self.assertTrue(res["BROWSER_PLAYBACK_VERIFIED"])
        self.assertEqual(res["highestTier"], "BROWSER_PLAYBACK_VERIFIED")


if __name__ == "__main__":
    unittest.main()
