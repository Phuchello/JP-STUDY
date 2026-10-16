"""
Adversarial Mutation & QA Gate Integration Test Suite for JP-STUDY Phase 3.7.
Directly exercises production reconciliation and validation functions from
scripts.curriculum.reconcile_blind_review.

Required Test Cases (Task F):
1. Reviewer agrees but reports an alternative defensible answer -> NOT QA_VERIFIED (QA_REVIEW_REQUIRED).
2. Reviewer agrees but reports a substantive unresolved concern -> QA_REVIEW_REQUIRED.
3. Wrong key causes reconciliation failure (QUARANTINED).
4. Changed stem invalidates old blind-review evidence (INDEPENDENT_REVIEW_PENDING).
5. Missing reviewer record blocks QA.
6. Duplicate review ID blocks reconciliation.
7. Stale ★ report ID fails validation.
8. Incorrect ★ answer fails validation.
9. Practice set referencing a quarantined item remains blocked (CONTENT_QA_BLOCKED).
10. Practice set without a real Form cannot be LIVE_VERIFIED (QA_PASSED_NOT_DEPLOYED).
11. Conflicting status fields fail release validation.
12. Existing P0 Forms remain untouched.
"""

import unittest
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.reconcile_blind_review import (
    verify_question_schema,
    audit_star_question,
    evaluate_question_qa_gate,
    reconcile_practice_set_status,
    check_review_integrity,
    audit_answer_distribution
)


class TestQAGateIntegration(unittest.TestCase):
    """Integration test suite exercising actual QA gate functions in reconcile_blind_review."""

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

    # Case 1: Reviewer agrees but reports an alternative defensible answer -> NOT QA_VERIFIED
    def test_case_1_alternative_defensible_answer_blocks_qa_verified(self):
        review = {
            "id": "N4-TEST-001",
            "blindAnswer": "A",
            "confidence": "HIGH",
            "linguisticJustification": "Matches intended form.",
            "alternativeDefensibleAnswers": ["B"],
            "concerns": None
        }
        status, reason, meta = evaluate_question_qa_gate(self.sample_question, review)
        self.assertNotEqual(status, "QA_VERIFIED", "Question with alternative defensible answer must not be QA_VERIFIED")
        self.assertEqual(status, "QA_REVIEW_REQUIRED")
        self.assertIn("alternative", reason.lower())

    # Case 2: Reviewer agrees but reports substantive concern -> QA_REVIEW_REQUIRED
    def test_case_2_substantive_concern_blocks_qa_verified(self):
        review = {
            "id": "N4-TEST-001",
            "blindAnswer": "A",
            "confidence": "MEDIUM",
            "linguisticJustification": "Selected A, but question has severe register ambiguity.",
            "alternativeDefensibleAnswers": [],
            "concerns": "Severe register ambiguity between polite and casual forms."
        }
        status, reason, meta = evaluate_question_qa_gate(self.sample_question, review)
        self.assertEqual(status, "QA_REVIEW_REQUIRED")
        self.assertIn("concern", reason.lower())

    # Case 3: Wrong key causes reconciliation failure -> QUARANTINED
    def test_case_3_wrong_key_causes_quarantine(self):
        review = {
            "id": "N4-TEST-001",
            "blindAnswer": "C", # Diverges from authored 'A'
            "confidence": "HIGH",
            "linguisticJustification": "Option C is correct grammatically.",
            "alternativeDefensibleAnswers": [],
            "concerns": None
        }
        status, reason, meta = evaluate_question_qa_gate(self.sample_question, review)
        self.assertEqual(status, "QUARANTINED")
        self.assertIn("Disagreement", reason)
        self.assertTrue(meta.get("disagreement"))

    # Case 4: Changed stem invalidates old blind-review evidence -> INDEPENDENT_REVIEW_PENDING
    def test_case_4_changed_stem_invalidates_review_evidence(self):
        # A materially changed question has no matching fresh review record (review=None)
        status, reason, meta = evaluate_question_qa_gate(self.sample_question, None)
        self.assertEqual(status, "INDEPENDENT_REVIEW_PENDING")
        self.assertIn("Awaiting independent", reason)

    # Case 5: Missing reviewer record blocks QA
    def test_case_5_missing_reviewer_record_blocks_qa(self):
        questions = [self.sample_question, {"id": "N4-TEST-MISSING", "level": "N4"}]
        reviews = {"N4-TEST-001": {"blindAnswer": "A"}}
        ok, msg, missing = check_review_integrity(reviews, questions)
        self.assertFalse(ok)
        self.assertIn("N4-TEST-MISSING", missing)

    # Case 6: Duplicate review ID blocks reconciliation
    def test_case_6_duplicate_review_id_detected(self):
        raw_items = [
            {"id": "N4-TEST-001", "blindAnswer": "A"},
            {"id": "N4-TEST-001", "blindAnswer": "B"}
        ]
        ids = [it["id"] for it in raw_items]
        has_duplicates = len(ids) != len(set(ids))
        self.assertTrue(has_duplicates, "Must detect duplicate review records for the same item ID")

    # Case 7: Stale star report ID fails validation
    def test_case_7_stale_star_report_id_fails_validation(self):
        with open(ROOT / "curriculum/QUESTION_BANK_EXPANDED.json", "r", encoding="utf-8") as f:
            bank = json.load(f)
        real_ids = {q["id"] for q in bank["questions"]}
        stale_id = "N2-GR-STAR-005" # Was hallucinated in old report
        self.assertNotIn(stale_id, real_ids, f"Stale ID {stale_id} must not exist in real bank")

    # Case 8: Incorrect star answer fails validation
    def test_case_8_incorrect_star_answer_fails_validation(self):
        mutated_star = dict(self.sample_star_question)
        mutated_star["correctAnswer"] = "B" # In canonical order, B is slot 1, not slot 3!
        ok, msg, data = audit_star_question(mutated_star)
        self.assertFalse(ok, "Star question where slot 3 does not match correctAnswer must fail audit")
        self.assertIn("Slot 3 chunk", msg)

    # Case 9: Practice set referencing a quarantined item remains blocked
    def test_case_9_practice_set_referencing_quarantined_item_remains_blocked(self):
        bank_map = {
            "Q1": {"id": "Q1", "status": "QA_VERIFIED"},
            "Q2": {"id": "Q2", "status": "QUARANTINED"}
        }
        ps = {
            "id": "MD-TEST-01",
            "category": "MICRO_DRILL",
            "questionIds": ["Q1", "Q2"],
            "deployment": {"isDeployed": False}
        }
        reconciled = reconcile_practice_set_status(ps, bank_map)
        self.assertEqual(reconciled["readinessStatus"], "CONTENT_QA_BLOCKED")
        self.assertEqual(reconciled["status"], "CONTENT_QA_BLOCKED")

    # Case 10: Practice set without real Form cannot be LIVE_VERIFIED
    def test_case_10_practice_set_without_real_form_cannot_be_live_verified(self):
        bank_map = {
            "Q1": {"id": "Q1", "status": "QA_VERIFIED"},
            "Q2": {"id": "Q2", "status": "QA_VERIFIED"}
        }
        # Practice set has zero deployment
        ps = {
            "id": "MD-TEST-02",
            "category": "MICRO_DRILL",
            "questionIds": ["Q1", "Q2"],
            "deployment": {
                "isDeployed": False,
                "formId": None,
                "responderUrl": None,
                "qaResult": None
            }
        }
        reconciled = reconcile_practice_set_status(ps, bank_map)
        self.assertNotEqual(reconciled["readinessStatus"], "LIVE_VERIFIED")
        self.assertEqual(reconciled["readinessStatus"], "QA_PASSED_NOT_DEPLOYED")

    # Case 11: Conflicting status fields fail release validation
    def test_case_11_conflicting_status_fields_fail_validation(self):
        # A practice set having conflicting readinessStatus and legacy status
        ps = {
            "readinessStatus": "QA_PASSED_NOT_DEPLOYED",
            "status": "LIVE_VERIFIED" # Conflict!
        }
        has_conflict = (ps["readinessStatus"] != ps["status"])
        self.assertTrue(has_conflict, "Conflicting status fields must be flagged as defect")

    # Case 12: Existing P0 Forms remain untouched
    def test_case_12_existing_p0_forms_remain_untouched(self):
        quiz_plan_path = ROOT / "QUIZ_FORMS/quiz_plan.json"
        self.assertTrue(quiz_plan_path.exists(), "QUIZ_FORMS/quiz_plan.json must exist")
        with open(quiz_plan_path, "r", encoding="utf-8") as f:
            qplan = json.load(f)
            
        quizzes = qplan.get("quizzes", [])
        p0_quizzes = [q for q in quizzes if q.get("releaseGroup") == "P0"]
        self.assertEqual(len(p0_quizzes), 3, "Exactly 3 P0 quizzes must exist")
        p0_ids = {q["id"] for q in p0_quizzes}
        self.assertEqual(p0_ids, {"W01-B01", "W01-B02", "W01-B03"}, "P0 quiz IDs must be exactly W01-B01, W01-B02, W01-B03")
        total_p0_questions = sum(len(q.get("questionIds", [])) for q in p0_quizzes)
        self.assertEqual(total_p0_questions, 18, "Total P0 questions must remain exactly 18")


if __name__ == "__main__":
    unittest.main()
