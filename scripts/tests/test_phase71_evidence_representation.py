"""Cross-platform integrity tests for preserved Phase 7.1 evidence bytes."""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEST_TEMP_ROOT = ROOT / "tmp" / "phase71-test-temp"
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum import build_phase_71_candidate_reconciliation as reconciliation
from scripts.curriculum.build_phase_71_candidate_reconciliation import (
    canonical_text_bytes,
    changed_source_for,
    digest_bytes,
    validate_file_digest,
    validate_preserved_text_pair,
)
from scripts.curriculum.question_fingerprint import compute_question_fingerprint


class TestPhase71EvidenceRepresentation(unittest.TestCase):
    @contextmanager
    def isolated_repository(self):
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT) as folder:
            root = Path(folder)
            previous_root = reconciliation.ROOT
            reconciliation.ROOT = root
            try:
                yield root
            finally:
                reconciliation.ROOT = previous_root

    @staticmethod
    def candidate_source_fixture(root: Path):
        question = {
            "id": "N2_FIXTURE_01",
            "typeId": "N2-MO-READ",
            "stem": "本文の内容と合うものはどれか。",
            "contextPassage": "資料を確認してから提出してください。",
            "options": [
                {"id": "A", "text": "資料を確認して提出する。"},
                {"id": "B", "text": "確認せずに提出する。"},
            ],
            "correctAnswer": "A",
        }
        fingerprint = compute_question_fingerprint(question)
        packet_row = {key: question[key] for key in ("id", "typeId", "stem", "contextPassage", "options")}
        packet_row["contentFingerprint"] = fingerprint
        packet_path, raw_path = root / "packet.json", root / "response.raw"
        packet_path.write_text(json.dumps({"items": [packet_row]}, ensure_ascii=False), encoding="utf-8")
        raw_path.write_bytes(b"synthetic reviewer response")
        source = {
            "kind": "current_review",
            "packetPath": "packet.json",
            "rawPath": "response.raw",
            "packetSha256": hashlib.sha256(packet_path.read_bytes()).hexdigest(),
            "rawSha256": hashlib.sha256(raw_path.read_bytes()).hexdigest(),
            "selectedOptionId": "A",
            "selectedExactText": question["options"][0]["text"],
            "reviewer": "Synthetic QA reviewer",
            "concerns": [],
            "alternatives": [],
        }
        return question, source, packet_path, raw_path

    def test_lf_checkout_matches_crlf_original_capture(self):
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT) as folder:
            root = Path(folder)
            readable = root / "snapshot.json"
            archive = root / "snapshot.raw"
            archive.write_bytes(b'{\r\n  "key": "value"\r\n}\r\n')
            readable.write_bytes(b'{\n  "key": "value"\n}\n')
            self.assertEqual(
                validate_preserved_text_pair(readable, archive, hashlib.sha256(archive.read_bytes()).hexdigest()),
                [],
            )

    def test_crlf_checkout_matches_lf_original_capture(self):
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT) as folder:
            root = Path(folder)
            readable = root / "response.md"
            archive = root / "response.raw"
            archive.write_bytes(b"line one\nline two\n")
            readable.write_bytes(b"line one\r\nline two\r\n")
            self.assertEqual(
                validate_preserved_text_pair(readable, archive, hashlib.sha256(archive.read_bytes()).hexdigest()),
                [],
            )

    def test_substantive_snapshot_tampering_fails(self):
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT) as folder:
            root = Path(folder)
            readable = root / "snapshot.json"
            archive = root / "snapshot.raw"
            archive.write_bytes(b'{"answer":"A"}\n')
            readable.write_bytes(b'{"answer":"B"}\n')
            errors = validate_preserved_text_pair(
                readable, archive, hashlib.sha256(archive.read_bytes()).hexdigest()
            )
            self.assertTrue(any("differs from preserved capture" in error for error in errors))

    def test_missing_snapshot_or_archive_fails(self):
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT) as folder:
            root = Path(folder)
            readable = root / "missing.json"
            archive = root / "missing.raw"
            self.assertTrue(validate_preserved_text_pair(readable, archive, "0" * 64))
            readable.write_bytes(b"{}\n")
            errors = validate_preserved_text_pair(readable, archive, "0" * 64)
            self.assertTrue(any("archive is missing" in error for error in errors))

    def test_incorrect_recorded_archive_digest_fails(self):
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT) as folder:
            root = Path(folder)
            readable = root / "snapshot.json"
            archive = root / "snapshot.raw"
            readable.write_bytes(b"{}\n")
            archive.write_bytes(b"{}\r\n")
            errors = validate_preserved_text_pair(readable, archive, "0" * 64)
            self.assertTrue(any("archive digest mismatch" in error for error in errors))

    def test_lone_carriage_return_is_an_explicit_line_ending_conversion(self):
        self.assertEqual(canonical_text_bytes(b"a\rb\r\n"), b"a\nb\n")
        self.assertEqual(digest_bytes(canonical_text_bytes(b"a\rb\r\n")), digest_bytes(b"a\nb\n"))

    def test_missing_raw_reviewer_response_fails_closed(self):
        with self.isolated_repository() as root:
            errors = validate_file_digest(root / "missing-response.raw", "0" * 64, "raw reviewer response")
            self.assertTrue(any("is missing" in error for error in errors))

    def test_mutated_review_packet_fails_its_digest_binding(self):
        with self.isolated_repository() as root:
            question, source, packet_path, _ = self.candidate_source_fixture(root)
            packet_path.write_bytes(packet_path.read_bytes() + b" ")
            with self.assertRaisesRegex(ValueError, "packet SHA differs"):
                changed_source_for(question["id"], 11, question, {question["id"]: source})

    def test_stale_packet_question_fingerprint_fails_closed(self):
        with self.isolated_repository() as root:
            question, source, _, _ = self.candidate_source_fixture(root)
            question["stem"] += "追加"
            with self.assertRaisesRegex(ValueError, "fingerprint does not match"):
                changed_source_for(question["id"], 11, question, {question["id"]: source})

    def test_mutated_reviewer_answer_fails_exact_key_text_check(self):
        with self.isolated_repository() as root:
            question, source, _, _ = self.candidate_source_fixture(root)
            source["selectedOptionId"] = "B"
            source["selectedExactText"] = question["options"][1]["text"]
            with self.assertRaisesRegex(ValueError, "reviewer answer disagrees"):
                changed_source_for(question["id"], 11, question, {question["id"]: source})

    def test_mismatched_selected_option_text_fails_closed(self):
        with self.isolated_repository() as root:
            question, source, _, _ = self.candidate_source_fixture(root)
            source["selectedExactText"] = question["options"][1]["text"]
            with self.assertRaisesRegex(ValueError, "exact option text differs"):
                changed_source_for(question["id"], 11, question, {question["id"]: source})


if __name__ == "__main__":
    unittest.main()
