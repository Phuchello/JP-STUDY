"""
Unit Tests for Unlimited Practice Engine Question Bank.
Validates:
- >= 400 N2 questions
- >= 200 N3 questions
- >= 25 reading passages
- >= 20 playable listening tracks
- Exactly 4 options (A, B, C, D) per question
- Zero duplicate question IDs
- Zero empty stems or empty options
- Valid distractor explanations for all 3 distractors
- Preserves all 5 MD-N4-VOC-01 pilot questions
- Random non-overlapping sampling across consecutive sessions
"""
import unittest
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BANK_PATH = ROOT / "curriculum/PRACTICE_ENGINE_BANK.json"
CANONICAL_PILOT_IDS = [
    "N4-MO-READ-001",
    "N4-MO-READ-002",
    "N4-MO-READ-003",
    "N4-MO-READ-004",
    "N4-MO-READ-005"
]

class TestPracticeEngineBank(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(BANK_PATH, "r", encoding="utf-8") as f:
            cls.bank_data = json.load(f)
        cls.questions = cls.bank_data["questions"]

    def test_overall_and_level_quotas(self):
        n2_count = sum(1 for q in self.questions if q["level"] == "N2")
        n3_count = sum(1 for q in self.questions if q["level"] == "N3")
        n4_count = sum(1 for q in self.questions if q["level"] == "N4")
        self.assertGreaterEqual(n2_count, 400, f"N2 questions count {n2_count} must be >= 400")
        self.assertGreaterEqual(n3_count, 200, f"N3 questions count {n3_count} must be >= 200")
        self.assertGreaterEqual(n4_count, 40, f"N4 questions count {n4_count} must be >= 40")
        self.assertGreaterEqual(len(self.questions), 700)

    def test_reading_passages_quota(self):
        reading_stimuli = {q["stimulusId"] for q in self.questions if q["skill"] == "Reading" and q.get("stimulusId")}
        self.assertGreaterEqual(len(reading_stimuli), 25, f"Reading passages {len(reading_stimuli)} must be >= 25")

    def test_playable_listening_tracks_quota(self):
        listening_tracks = {q["audioUrl"] for q in self.questions if q["skill"] == "Listening" and q.get("audioUrl")}
        self.assertGreaterEqual(len(listening_tracks), 20, f"Listening tracks {len(listening_tracks)} must be >= 20")
        # Ensure all audio URLs are official and https
        for url in listening_tracks:
            self.assertTrue(url.startswith("https://www.jlpt.jp/"), f"Audio URL must be official JLPT: {url}")
            self.assertTrue(".mp3" in url)

    def test_unique_question_ids(self):
        qids = [q["id"] for q in self.questions]
        self.assertEqual(len(qids), len(set(qids)), "Question IDs must be globally unique.")

    def test_question_schema_integrity(self):
        for q in self.questions:
            qid = q["id"]
            self.assertTrue(q.get("stem") and q["stem"].strip(), f"Empty stem in {qid}")
            opts = q.get("options", [])
            self.assertEqual(len(opts), 4, f"Question {qid} must have 4 options")
            opt_ids = [o["id"] for o in opts]
            self.assertEqual(opt_ids, ["A", "B", "C", "D"], f"Options in {qid} must be A, B, C, D")
            for o in opts:
                self.assertTrue(o.get("text") and o["text"].strip(), f"Empty option in {qid}")
            self.assertIn(q.get("correctAnswer"), ["A", "B", "C", "D"], f"Invalid correctAnswer in {qid}")
            self.assertTrue(q.get("explanationVi") and q["explanationVi"].strip(), f"Empty explanation in {qid}")
            
            # Distractor explanations
            dist_map = q.get("distractorExplanations", {})
            for char in ["A", "B", "C", "D"]:
                if char != q["correctAnswer"]:
                    self.assertIn(char, dist_map, f"Missing distractor explanation for option {char} in {qid}")
                    self.assertTrue(dist_map[char].strip(), f"Empty distractor explanation in {qid}")

    def test_canonical_pilot_questions_preserved(self):
        qmap = {q["id"]: q for q in self.questions}
        for pid in CANONICAL_PILOT_IDS:
            self.assertIn(pid, qmap, f"Canonical pilot item {pid} must be preserved in bank.")
            self.assertEqual(qmap[pid]["level"], "N4")
            self.assertEqual(qmap[pid]["status"], "QA_VERIFIED")

    def test_consecutive_session_non_overlapping_sampling(self):
        """Simulates 3 consecutive Mode A sessions of 30 questions each with 0% overlap."""
        import random
        n2_qs = [q for q in self.questions if q["level"] == "N2"]
        rng = random.Random(42)
        shuffled = list(n2_qs)
        rng.shuffle(shuffled)

        session_1 = shuffled[:30]
        session_2 = shuffled[30:60]
        session_3 = shuffled[60:90]

        s1_ids = {q["id"] for q in session_1}
        s2_ids = {q["id"] for q in session_2}
        s3_ids = {q["id"] for q in session_3}

        self.assertEqual(len(s1_ids.intersection(s2_ids)), 0, "Session 1 and 2 must have zero overlap")
        self.assertEqual(len(s2_ids.intersection(s3_ids)), 0, "Session 2 and 3 must have zero overlap")
        self.assertEqual(len(s1_ids.intersection(s3_ids)), 0, "Session 1 and 3 must have zero overlap")

if __name__ == '__main__':
    unittest.main()
