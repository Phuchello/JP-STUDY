import tempfile
import unittest
from pathlib import Path

from scripts.curriculum.reconcile_mock_blind_review import bind_private_raw_review_digest


class PrivateRawReviewBindingTests(unittest.TestCase):
    def test_existing_private_tmp_raw_is_hash_bound(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            raw = root / "tmp" / "reviews" / "raw.json"
            raw.parent.mkdir(parents=True)
            raw.write_text("synthetic review payload", encoding="utf-8")
            binding = bind_private_raw_review_digest(
                "tmp/reviews/raw.json",
                {"rawResponsePreservedLocally": True, "portableExecutionAttestationAvailable": False},
                root,
            )
            self.assertEqual(binding, {"rawOutputSha256": raw})

    def test_missing_private_tmp_raw_is_allowed_only_with_explicit_limits(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            evidence = {"rawResponsePreservedLocally": True, "portableExecutionAttestationAvailable": False}
            self.assertIsNone(bind_private_raw_review_digest("tmp/reviews/raw.json", evidence, root))
            with self.assertRaises(ValueError):
                bind_private_raw_review_digest("qa/raw.json", evidence, root)
            with self.assertRaises(ValueError):
                bind_private_raw_review_digest("tmp/reviews/raw.json", {"rawResponsePreservedLocally": True}, root)
            with self.assertRaises(ValueError):
                bind_private_raw_review_digest("tmp/../qa/raw.json", evidence, root)

    def test_raw_path_cannot_escape_repository_root(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(ValueError):
                bind_private_raw_review_digest(
                    "../outside.json",
                    {"rawResponsePreservedLocally": True, "portableExecutionAttestationAvailable": False},
                    Path(temp),
                )


if __name__ == "__main__":
    unittest.main()
