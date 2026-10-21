import hashlib
import unittest

from scripts.curriculum.validate_n2_mock_10_blind_review import compatible_text_sha256


class SealedInputHashTests(unittest.TestCase):
    def test_lf_and_crlf_checkouts_share_the_same_approved_hash_variants(self):
        lf = b"[{\n  \"id\": \"Q1\"\n}]\n"
        crlf = lf.replace(b"\n", b"\r\n")
        self.assertIn(hashlib.sha256(crlf).hexdigest(), compatible_text_sha256(lf))
        self.assertIn(hashlib.sha256(lf).hexdigest(), compatible_text_sha256(crlf))

    def test_content_change_is_not_accepted_as_a_line_ending_variant(self):
        reviewed = b"[{\n  \"id\": \"Q1\"\n}]\n"
        changed = b"[{\n  \"id\": \"Q2\"\n}]\n"
        self.assertNotIn(hashlib.sha256(reviewed).hexdigest(), compatible_text_sha256(changed))


if __name__ == "__main__":
    unittest.main()
