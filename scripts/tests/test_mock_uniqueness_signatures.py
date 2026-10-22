import unittest

from scripts.curriculum.validate_mock_uniqueness import stem_collision_signature


class MockUniquenessSignatureTests(unittest.TestCase):
    def star(self, fragments):
        return {
            "typeId": "N2-GR-STAR",
            "stem": "次の文を完成させるとき、★に入る部分はどれか。\n（　　）（　　）★（　　）",
            "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(fragments)],
        }

    def test_shared_star_instruction_does_not_hide_distinct_content(self):
        first = self.star(["予定を", "調整する", "必要がある", "早めに"])
        second = self.star(["資料を", "確認して", "から", "提出する"])
        self.assertNotEqual(stem_collision_signature(first), stem_collision_signature(second))

    def test_star_option_reordering_keeps_same_content_signature(self):
        first = self.star(["予定を", "調整する", "必要がある", "早めに"])
        reordered = self.star(["早めに", "必要がある", "予定を", "調整する"])
        self.assertEqual(stem_collision_signature(first), stem_collision_signature(reordered))

    def test_regular_duplicate_stem_still_collides(self):
        first = {"typeId": "N2-GR-FORM", "stem": "彼は計画を変更した。", "options": []}
        second = {"typeId": "N2-GR-FORM", "stem": "彼は計画を変更した。", "options": []}
        self.assertEqual(stem_collision_signature(first), stem_collision_signature(second))


if __name__ == "__main__":
    unittest.main()
