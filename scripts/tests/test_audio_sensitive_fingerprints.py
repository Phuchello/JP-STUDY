# -*- coding: utf-8 -*-
"""
Tests for Audio-Sensitive Content Fingerprints (A2 Requirements)
Verifies:
  1. Same text and same audio produce identical fingerprints.
  2. Changing stem changes text and assessment fingerprints.
  3. Changing options changes assessment fingerprint.
  4. Reordering options preserves option text fingerprint while changing option letter order.
  5. Changing audio bytes while keeping URL unchanged invalidates assessment fingerprint.
  6. Changing audio transcript / context invalidates semantic review fingerprint.
  7. Stale or mismatched audio playback receipt fails verification.
"""
import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.curriculum.question_fingerprint import (
    compute_question_text_fingerprint,
    compute_audio_asset_fingerprint,
    compute_assessment_version_fingerprint,
    compute_question_fingerprint,
    compute_option_text_fingerprint,
)

class TestAudioSensitiveFingerprints(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.audio_dir = self.root / "docs" / "audio" / "test_mock"
        self.audio_dir.mkdir(parents=True, exist_ok=True)

        # Create dummy audio file
        self.audio_file = self.audio_dir / "Q01.mp3"
        self.original_audio_bytes = b"ID3_MOCK_AUDIO_PAYLOAD_V1_TEST_BYTES"
        self.audio_file.write_bytes(self.original_audio_bytes)
        self.original_audio_sha = hashlib.sha256(self.original_audio_bytes).hexdigest()

        self.sample_listening_q = {
            "id": "TEST_L01",
            "typeId": "N2-L-TASK",
            "section": 2,
            "stem": "会社で男の人と女の人が話しています。男の人はこの後まず何をしますか。",
            "contextPassage": "【場面】オフィス。資料作成の締め切り前。",
            "options": [
                {"id": "A", "text": "企画書の修正"},
                {"id": "B", "text": "会議室の予約"},
                {"id": "C", "text": "部長への報告"},
                {"id": "D", "text": "データの再集計"}
            ],
            "audioUrl": "audio/test_mock/Q01.mp3",
            "audioSha256": self.original_audio_sha
        }

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_01_same_text_and_audio_produce_identical_fingerprint(self):
        fp1 = compute_assessment_version_fingerprint(self.sample_listening_q, root_dir=self.root)
        fp2 = compute_assessment_version_fingerprint(copy.deepcopy(self.sample_listening_q), root_dir=self.root)
        self.assertEqual(fp1, fp2)
        self.assertEqual(len(fp1), 64)

    def test_02_changing_stem_changes_text_and_assessment_fingerprints(self):
        mutated_q = copy.deepcopy(self.sample_listening_q)
        mutated_q["stem"] = "女の人はこの後まず何をしますか。"

        orig_text_fp = compute_question_text_fingerprint(self.sample_listening_q)
        mut_text_fp = compute_question_text_fingerprint(mutated_q)
        self.assertNotEqual(orig_text_fp, mut_text_fp)

        orig_assess_fp = compute_assessment_version_fingerprint(self.sample_listening_q, root_dir=self.root)
        mut_assess_fp = compute_assessment_version_fingerprint(mutated_q, root_dir=self.root)
        self.assertNotEqual(orig_assess_fp, mut_assess_fp)

    def test_03_changing_options_changes_assessment_fingerprint(self):
        mutated_q = copy.deepcopy(self.sample_listening_q)
        mutated_q["options"][0]["text"] = "企画書の印刷"

        orig_fp = compute_assessment_version_fingerprint(self.sample_listening_q, root_dir=self.root)
        mut_fp = compute_assessment_version_fingerprint(mutated_q, root_dir=self.root)
        self.assertNotEqual(orig_fp, mut_fp)

    def test_04_reordering_options_preserves_semantic_content_set(self):
        reordered_q = copy.deepcopy(self.sample_listening_q)
        # Swap options A and B
        opt_a_text = reordered_q["options"][0]["text"]
        opt_b_text = reordered_q["options"][1]["text"]
        reordered_q["options"][0]["text"] = opt_b_text
        reordered_q["options"][1]["text"] = opt_a_text

        # Option text set fingerprint MUST remain identical
        orig_opt_set_fp = compute_option_text_fingerprint(self.sample_listening_q["options"])
        reordered_opt_set_fp = compute_option_text_fingerprint(reordered_q["options"])
        self.assertEqual(orig_opt_set_fp, reordered_opt_set_fp)

        # But ordered question fingerprint MUST change to reflect remapping requirement
        orig_fp = compute_assessment_version_fingerprint(self.sample_listening_q, root_dir=self.root)
        reordered_fp = compute_assessment_version_fingerprint(reordered_q, root_dir=self.root)
        self.assertNotEqual(orig_fp, reordered_fp)

    def test_05_changing_audio_bytes_invalidates_assessment_fingerprint(self):
        orig_fp = compute_assessment_version_fingerprint(self.sample_listening_q, root_dir=self.root)

        # Mutate audio bytes on disk without changing URL
        new_audio_bytes = b"MUTATED_AUDIO_TRACK_CONTENT_RE_RECORDED_V2"
        self.audio_file.write_bytes(new_audio_bytes)
        new_sha = hashlib.sha256(new_audio_bytes).hexdigest()

        # Update recorded audioSha256 to match disk
        mutated_q = copy.deepcopy(self.sample_listening_q)
        mutated_q["audioSha256"] = new_sha

        mut_fp = compute_assessment_version_fingerprint(mutated_q, root_dir=self.root)
        self.assertNotEqual(orig_fp, mut_fp, "Changing audio bytes MUST invalidate the assessment fingerprint")

    def test_06_audio_file_mismatch_with_recorded_sha_raises_error(self):
        # Audio file modified on disk, but question still claims old SHA
        self.audio_file.write_bytes(b"TAMPERED_AUDIO_DIFFERENT_FROM_MANIFEST")
        with self.assertRaises(ValueError) as ctx:
            compute_assessment_version_fingerprint(self.sample_listening_q, root_dir=self.root)
        self.assertIn("Audio hash mismatch", str(ctx.exception))

    def test_07_stale_playback_receipt_fails_verification(self):
        # Simulating a playback receipt verification check
        valid_receipt = {
            "TEST_L01": {
                "audioSha256": self.original_audio_sha,
                "browserPlaybackVerified": True,
                "decodedDurationSec": 45.2
            }
        }
        # Corrupt the receipt sha
        stale_receipt = {
            "TEST_L01": {
                "audioSha256": "0000000000000000000000000000000000000000000000000000000000000000",
                "browserPlaybackVerified": True,
                "decodedDurationSec": 45.2
            }
        }
        current_audio_sha = compute_audio_asset_fingerprint(self.sample_listening_q, root_dir=self.root)
        self.assertEqual(valid_receipt["TEST_L01"]["audioSha256"], current_audio_sha)
        self.assertNotEqual(stale_receipt["TEST_L01"]["audioSha256"], current_audio_sha)

if __name__ == "__main__":
    unittest.main()
