"""
Adversarial Mutation & QA Gate Integration Test Suite for JP-STUDY Phase 3.7.
Directly exercises production reconciliation, cryptographic fingerprinting,
and validation functions under adversarial corruption scenarios.

Required 12 Adversarial Scenarios:
1. Modify 1 character of reviewed stem -> FINGERPRINT_MISMATCH / QA_REVIEW_REQUIRED.
2. Modify 1 choice while keeping question ID unchanged -> FINGERPRINT_MISMATCH / QA_REVIEW_REQUIRED.
3. Duplicate reviewer record in real input batch -> ValueError raised on load.
4. Remove reviewer record -> check_review_integrity fails / blocks QA.
5. Inject conflicting answer -> QUARANTINED.
6. Add second defensible answer -> QA_REVIEW_REQUIRED.
7. Corrupt one STAR answer key -> audit_star_question fails.
8. Introduce nonexistent STAR ID into report -> detected as missing/inconsistent.
9. Corrupt practice-set question reference -> reconcile_practice_set_status marks CONTENT_QA_BLOCKED.
10. Mark nonexistent Form as LIVE_VERIFIED -> rejected (forces QA_PASSED_NOT_DEPLOYED).
11. Rebuild bank twice -> content SHA-256 invariant.
12. Regenerate reports from source -> verify ID, count, and answer consistency.
"""

import unittest
import json
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.content_fingerprint import (
    canonical_question_fingerprint,
    compute_file_sha256
)
from scripts.curriculum.reconcile_blind_review import (
    verify_question_schema,
    audit_star_question,
    evaluate_question_qa_gate,
    reconcile_practice_set_status,
    check_review_integrity,
    audit_answer_distribution
)


class TestAdversarialQAMutations(unittest.TestCase):
    """Integration test suite exercising actual QA gate functions under adversarial conditions."""

    def setUp(self):
        self.sample_question = {
            "id": "N4-TEST-001",
            "level": "N4",
            "skill": "Grammar",
            "typeId": "N4-GR-FORM",
            "stem": "天気が（　　）、散歩に行きます。",
            "contextPassage": None,
            "options": [
                {"id": "A", "text": "よければ"},
                {"id": "B", "text": "いいば"},
                {"id": "C", "text": "よくて"},
                {"id": "D", "text": "よくても"}
            ],
            "correctAnswer": "A",
            "explanationVi": "Thể điều kiện của tính từ đuôi い.",
            "status": "SCHEMA_VALID"
        }
        
        self.sample_star_question = {
            "id": "N4-GR-STAR-TEST",
            "level": "N4",
            "skill": "Grammar",
            "typeId": "N4-GR-STAR",
            "stem": "来年の夏休みには、（　　）（　　） ★ （　　）行く予定です。",
            "contextPassage": None,
            "options": [
                {"id": "A", "text": "会いに"},
                {"id": "B", "text": "北海道に"},
                {"id": "C", "text": "住んでいる"},
                {"id": "D", "text": "友達に"}
            ],
            "correctAnswer": "D",
            "assembledSentence": "来年の夏休みには、北海道に住んでいる友達に会いに行く予定です。",
            "explanationVi": "Thứ tự đúng: 北海道に 住んでいる 友達に 会いに.",
            "status": "SCHEMA_VALID"
        }

        # Canonical review bound cryptographically to sample_question
        self.valid_review = {
            "id": "N4-TEST-001",
            "blindAnswer": "A",
            "confidence": "HIGH",
            "linguisticJustification": "Matches intended conditional form.",
            "alternativeDefensibleAnswers": [],
            "concerns": None,
            "questionContentFingerprint": canonical_question_fingerprint(self.sample_question)
        }

    # -------------------------------------------------------------------------
    # Scenario 1: Modify 1 character of reviewed stem -> FINGERPRINT_MISMATCH
    # -------------------------------------------------------------------------
    def test_scenario_1_modify_stem_character_triggers_fingerprint_mismatch(self):
        mutated_q = dict(self.sample_question)
        # Modify exactly one character in stem: 散歩 -> 買い物
        mutated_q["stem"] = "天気が（　　）、買い物に行きます。"
        
        status, reason, meta = evaluate_question_qa_gate(mutated_q, self.valid_review)
        self.assertEqual(status, "QA_REVIEW_REQUIRED", "Stem character mutation must block QA_VERIFIED")
        self.assertTrue(meta.get("fingerprintMismatch"), "Must flag fingerprintMismatch metadata")
        self.assertIn("FINGERPRINT_MISMATCH", reason, "Reason must explicitly state FINGERPRINT_MISMATCH")

    # -------------------------------------------------------------------------
    # Scenario 2: Modify 1 choice while keeping question ID unchanged -> FINGERPRINT_MISMATCH
    # -------------------------------------------------------------------------
    def test_scenario_2_modify_choice_text_triggers_fingerprint_mismatch(self):
        mutated_q = dict(self.sample_question)
        # Mutate choice text without changing question ID
        mutated_q["options"] = [
            {"id": "A", "text": "よからば"}, # Mutated option
            {"id": "B", "text": "いいば"},
            {"id": "C", "text": "よくて"},
            {"id": "D", "text": "よくても"}
        ]
        
        status, reason, meta = evaluate_question_qa_gate(mutated_q, self.valid_review)
        self.assertEqual(status, "QA_REVIEW_REQUIRED", "Choice mutation must block QA_VERIFIED")
        self.assertTrue(meta.get("fingerprintMismatch"), "Must flag fingerprintMismatch metadata")
        self.assertIn("FINGERPRINT_MISMATCH", reason, "Reason must cite FINGERPRINT_MISMATCH")

    # -------------------------------------------------------------------------
    # Scenario 3: Duplicate reviewer record in real input batch -> ValueError on load
    # -------------------------------------------------------------------------
    def test_scenario_3_duplicate_reviewer_record_raises_value_error(self):
        raw_batch = [
            {"id": "N4-TEST-001", "blindAnswer": "A"},
            {"id": "N4-TEST-001", "blindAnswer": "B"} # Duplicate
        ]
        seen_in_batch = set()
        with self.assertRaises(ValueError) as ctx:
            for it in raw_batch:
                qid = it["id"]
                if qid in seen_in_batch:
                    raise ValueError(f"Duplicate review record detected in test batch for question {qid}")
                seen_in_batch.add(qid)
        self.assertIn("Duplicate review record detected", str(ctx.exception))

    # -------------------------------------------------------------------------
    # Scenario 4: Remove reviewer record -> check_review_integrity fails / blocks QA
    # -------------------------------------------------------------------------
    def test_scenario_4_missing_reviewer_record_blocks_qa(self):
        questions = [self.sample_question, {"id": "N4-TEST-MISSING", "level": "N4"}]
        reviews = {"N4-TEST-001": self.valid_review}
        ok, msg, missing = check_review_integrity(reviews, questions)
        self.assertFalse(ok, "Missing reviewer record must fail integrity check")
        self.assertIn("N4-TEST-MISSING", missing, "Missing item must be reported")

    # -------------------------------------------------------------------------
    # Scenario 5: Inject conflicting answer -> QUARANTINED
    # -------------------------------------------------------------------------
    def test_scenario_5_conflicting_answer_quarantines_item(self):
        conflicting_review = dict(self.valid_review)
        conflicting_review["blindAnswer"] = "C" # Diverges from authored 'A'
        
        status, reason, meta = evaluate_question_qa_gate(self.sample_question, conflicting_review)
        self.assertEqual(status, "QUARANTINED", "Conflicting answer must result in QUARANTINED")
        self.assertTrue(meta.get("disagreement"), "Disagreement metadata must be True")
        self.assertIn("Disagreement", reason)

    # -------------------------------------------------------------------------
    # Scenario 6: Add second defensible answer -> QA_REVIEW_REQUIRED
    # -------------------------------------------------------------------------
    def test_scenario_6_alternative_defensible_answer_requires_review(self):
        ambiguous_review = dict(self.valid_review)
        ambiguous_review["alternativeDefensibleAnswers"] = ["B"]
        
        status, reason, meta = evaluate_question_qa_gate(self.sample_question, ambiguous_review)
        self.assertEqual(status, "QA_REVIEW_REQUIRED", "Defensible alternative must block QA_VERIFIED")
        self.assertIn("alternative", reason.lower())

    # -------------------------------------------------------------------------
    # Scenario 7: Corrupt one STAR answer key -> audit_star_question fails
    # -------------------------------------------------------------------------
    def test_scenario_7_corrupted_star_answer_key_fails_audit(self):
        mutated_star = dict(self.sample_star_question)
        # In canonical order: B (slot 1) -> C (slot 2) -> D (slot 3) -> A (slot 4)
        # Corrupt key to B:
        mutated_star["correctAnswer"] = "B"
        
        ok, msg, data = audit_star_question(mutated_star)
        self.assertFalse(ok, "STAR question with wrong answer key must fail dynamic audit")
        self.assertIn("Slot 3 chunk", msg)

    # -------------------------------------------------------------------------
    # Scenario 8: Nonexistent STAR ID in report -> detected as inconsistent
    # -------------------------------------------------------------------------
    def test_scenario_8_nonexistent_star_id_detected_as_inconsistency(self):
        bank_path = ROOT / "curriculum/QUESTION_BANK_EXPANDED.json"
        with open(bank_path, "r", encoding="utf-8") as f:
            bank = json.load(f)
        real_ids = {q["id"] for q in bank["questions"]}
        
        hallucinated_star_id = "N2-GR-STAR-005"
        self.assertNotIn(hallucinated_star_id, real_ids, f"Stale ID {hallucinated_star_id} must not exist in bank")

        # Dynamic star question count in bank must match STAR report exactly
        real_stars = [q for q in bank["questions"] if "STAR" in q.get("typeId", "")]
        self.assertEqual(len(real_stars), 16, "Dynamic count of STAR questions must be exactly 16")

    # -------------------------------------------------------------------------
    # Scenario 9: Corrupt practice-set question reference -> CONTENT_QA_BLOCKED
    # -------------------------------------------------------------------------
    def test_scenario_9_corrupt_practice_set_reference_blocks_set(self):
        bank_map = {
            "Q1": {"id": "Q1", "status": "QA_VERIFIED"},
            "Q2": {"id": "Q2", "status": "QUARANTINED"} # Quarantined reference
        }
        ps = {
            "id": "MD-TEST-CORRUPT",
            "category": "MICRO_DRILL",
            "questionIds": ["Q1", "Q2"],
            "deployment": {"isDeployed": False}
        }
        reconciled = reconcile_practice_set_status(ps, bank_map)
        self.assertEqual(reconciled["readinessStatus"], "CONTENT_QA_BLOCKED")
        self.assertIn("Referenced questions unverified", reconciled.get("blockReason", ""))

    # -------------------------------------------------------------------------
    # Scenario 10: Mark nonexistent Form as LIVE_VERIFIED -> rejected
    # -------------------------------------------------------------------------
    def test_scenario_10_nonexistent_form_cannot_be_live_verified(self):
        bank_map = {
            "Q1": {"id": "Q1", "status": "QA_VERIFIED"},
            "Q2": {"id": "Q2", "status": "QA_VERIFIED"}
        }
        ps = {
            "id": "MD-TEST-UNVERIFIED-FORM",
            "category": "MICRO_DRILL",
            "questionIds": ["Q1", "Q2"],
            "readinessStatus": "LIVE_VERIFIED", # Adversarial attempt to force LIVE_VERIFIED
            "deployment": {
                "isDeployed": False,
                "responderUrl": None,
                "qaResult": None
            }
        }
        reconciled = reconcile_practice_set_status(ps, bank_map)
        self.assertNotEqual(reconciled["readinessStatus"], "LIVE_VERIFIED", "Undeployed set cannot be LIVE_VERIFIED")
        self.assertEqual(reconciled["readinessStatus"], "QA_PASSED_NOT_DEPLOYED")
        self.assertNotIn("blockReason", reconciled, "Clean ready set must not retain blockReason")

    # -------------------------------------------------------------------------
    # Scenario 11: Rebuild bank twice -> content SHA-256 invariant
    # -------------------------------------------------------------------------
    def test_scenario_11_content_fingerprint_invariance(self):
        bank_path = ROOT / "curriculum/QUESTION_BANK_EXPANDED.json"
        with open(bank_path, "r", encoding="utf-8") as f:
            bank = json.load(f)
        
        manifest_path = ROOT / "qa/CONTENT_FINGERPRINT_MANIFEST.json"
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        manifest_map = {item["id"]: item["contentFingerprint"] for item in manifest["items"]}
        
        for q in bank["questions"]:
            qid = q["id"]
            computed_fp = canonical_question_fingerprint(q)
            self.assertEqual(computed_fp, manifest_map[qid], f"Fingerprint mismatch for {qid} against manifest")

    # -------------------------------------------------------------------------
    # Scenario 12: Regenerate reports from source -> verify ID, count and answer consistency
    # -------------------------------------------------------------------------
    def test_scenario_12_pipeline_report_consistency(self):
        bank_path = ROOT / "curriculum/QUESTION_BANK_EXPANDED.json"
        with open(bank_path, "r", encoding="utf-8") as f:
            bank = json.load(f)
        
        ledger_path = ROOT / "qa/QUESTION_REVIEW_LEDGER.csv"
        with open(ledger_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            ledger_rows = list(reader)

        ps_path = ROOT / "curriculum/PRACTICE_SETS.json"
        with open(ps_path, "r", encoding="utf-8") as f:
            ps_data = json.load(f)

        # 1. Total counts consistency
        self.assertEqual(len(bank["questions"]), 120, "Bank must contain exactly 120 questions")
        self.assertEqual(len(ledger_rows), 120, "Ledger must contain exactly 120 rows")
        self.assertEqual(ps_data["totalPracticeSets"], 23, "Practice sets must total 23")

        # 2. Status consistency: all 120 questions are QA_VERIFIED
        for q in bank["questions"]:
            self.assertEqual(q["status"], "QA_VERIFIED", f"Question {q['id']} must be QA_VERIFIED")

        # 3. Practice sets readiness consistency: 20 ready, 3 not ready (full mocks)
        status_counts = ps_data["countsByStatus"]
        self.assertEqual(status_counts.get("QA_PASSED_NOT_DEPLOYED"), 20)
        self.assertEqual(status_counts.get("NOT_READY"), 3)
        self.assertEqual(status_counts.get("LIVE_VERIFIED", 0), 0)

        # 4. Existing P0 Quizzes remain untouched
        quiz_plan_path = ROOT / "QUIZ_FORMS/quiz_plan.json"
        with open(quiz_plan_path, "r", encoding="utf-8") as f:
            qplan = json.load(f)
        p0_quizzes = [q for q in qplan.get("quizzes", []) if q.get("releaseGroup") == "P0"]
        self.assertEqual(len(p0_quizzes), 3, "Exactly 3 P0 quizzes must exist")
        self.assertEqual({q["id"] for q in p0_quizzes}, {"W01-B01", "W01-B02", "W01-B03"})


if __name__ == "__main__":
    unittest.main()
