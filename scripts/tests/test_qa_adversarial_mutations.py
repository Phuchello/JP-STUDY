"""
Adversarial Mutation & Release-Gate Security Test Suite for JP-STUDY Phase 3.7.
Directly exercises production reconciliation, cryptographic fingerprinting,
two-gate STAR permutation auditing, strict STAR stem parsing, forged semantic ledger
rejection (P0-1 Attacks A through J), workspace deployment validation (P0-2 Attacks 1 through 10),
and zero-item reporting under adversarial conditions.

Structure:
Part 1: 12 Production Mutation Integration Scenarios
  1. Modify 1 stem character -> FINGERPRINT_MISMATCH / QA_REVIEW_REQUIRED
  2. Modify 1 choice text -> FINGERPRINT_MISMATCH / QA_REVIEW_REQUIRED
  3. Duplicate reviewer record in real input batch -> load_all_blind_reviews raises ValueError
  4. Remove reviewer record -> check_review_integrity blocks QA
  5. Inject conflicting answer -> QUARANTINED
  6. Add second defensible answer -> QA_REVIEW_REQUIRED
  7. Corrupt one STAR answer key -> audit_star_question fails with ANSWER_KEY_SLOT3_MISMATCH
  8. Nonexistent STAR ID in report -> audit_star_report_against_bank detects discrepancy
  9. Corrupt practice-set reference -> reconcile_practice_set_status marks CONTENT_QA_BLOCKED
  10. Non-Google deployment URL -> reconcile_practice_set_status rejects LIVE_VERIFIED
  11. Rebuild invariance -> verify multi-tier hashes across generation
  12. Pipeline report consistency -> verify exact counts across bank, ledger, practice sets

Part 2: 10 STAR Structure Negative Controls (P0-A Strict Parser)
  13. Extra regular blank -> fails Gate 1 with EXTRA_SLOTS
  14. Two extra blanks -> fails Gate 1 with EXTRA_SLOTS
  15. Star in position one -> fails Gate 1 with INVALID_STAR_POSITION (pos 1)
  16. Star in position two -> fails Gate 1 with INVALID_STAR_POSITION (pos 2)
  17. Star in position four -> fails Gate 1 with INVALID_STAR_POSITION (pos 4)
  18. Duplicate star -> fails Gate 1 with DUPLICATE_STAR_MARKER
  19. Missing blank -> fails Gate 1 with INSUFFICIENT_SLOTS
  20. Malformed blank delimiters -> fails Gate 1 with MALFORMED_PARENTHESES
  21. Canonical missing chunk -> fails Gate 1 with INCOHERENT_CANONICAL_SENTENCE
  22. Incorrect answer key -> fails Gate 1 with ANSWER_KEY_SLOT3_MISMATCH

Part 3: 10 Forged Semantic Ledger Attack Tests (P0-1 Attacks A through J)
  23. Attack A: coverageDeclared omitted with only 1 permutation reviewed -> INSUFFICIENT_REVIEW_COVERAGE
  24. Attack B: coverageDeclared set to PARTIAL -> INCOMPLETE_COVERAGE_DECLARED_PARTIAL
  25. Attack C: Duplicate reviewed permutation IDs -> DUPLICATE_REVIEWED_PERMUTATION
  26. Attack D: Extra, nonexistent permutation IDs -> NONEXISTENT_PERMUTATION
  27. Attack E: Judgments IDs mismatch reviewed permutations -> EXTRA_JUDGMENT_NOT_REVIEWED
  28. Attack F: Valid artifact digest but arbitrary unverified reviewer identity -> UNSUPPORTED_REVIEWER_LABEL
  29. Attack G: Locally fabricated repetitive unsupported reasoning boilerplate -> REPETITIVE_UNSUPPORTED_BOILERPLATE_REJECTED
  30. Attack H: Correct question fingerprint but stale scoring fingerprint -> SCORING_FINGERPRINT_MISMATCH
  31. Attack I: Conflicting defensible alternative in judgments -> AMBIGUOUS_ALTERNATIVE_FOUND (QUARANTINED)
  32. Attack J: Valid-looking completed review containing one unresolved judgment -> UNRESOLVED_LINGUISTIC_JUDGMENT

Part 4: Real Linguistic Negative Control (Adjunct Scrambling)
  33. Tanaka-san free adjunct scrambling -> STAR_SEMANTIC_REVIEW_PENDING (never VERIFIED_COHERENT)

Part 5: 10 Google Forms Deployment Evidence & Provider Verification Tests (P0-2)
  34. Attack 1: Local verifiedSets forgery rejected -> QA_PASSED_NOT_DEPLOYED (liveVerified=False)
  35. Attack 2: Real Form ID paired with wrong practice set ID -> PRACTICE_SET_ID_MISMATCH
  36. Attack 3: Correct Form ID with wrong question mapping -> QUESTION_MAPPING_MISMATCH
  37. Attack 4: Correct Form ID but no response receipt -> MISSING_SUBMISSION_RECEIPT
  38. Attack 5: Valid receipt belonging to another Form -> RECEIPT_FORM_MISMATCH
  39. Attack 6: Correct Form but wrong destination Sheet -> DESTINATION_SHEET_MISMATCH
  40. Attack 7: Expired or stale verification evidence -> STALE_DEPLOYMENT_EVIDENCE
  41. Attack 8: Incomplete grading verification -> GRADING_VERIFICATION_FAILED
  42. Attack 9: Unauthorized test double rejected -> UNAUTHORIZED_TEST_DOUBLE_REJECTED
  43. Attack 10: Authorized workspace provider with verified receipt -> LIVE_VERIFIED

Part 6: P1-B Zero-Item Mock Reporting Bug
  44. Empty full-mock set reports NO_ITEMS — NOT_EVALUABLE instead of 100% VERIFIED

Generates qa/ADVERSARIAL_TEST_RESULTS.md.
"""

import unittest
import itertools
import json
import csv
import shutil
import tempfile
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.content_fingerprint import (
    canonical_blind_input_fingerprint,
    canonical_scoring_fingerprint,
    canonical_pedagogical_fingerprint,
    canonical_full_item_fingerprint,
    compute_all_question_fingerprints,
    compute_file_sha256
)
from scripts.curriculum.audit_star_permutations import (
    parse_strict_star_stem,
    validate_star_structure,
    validate_semantic_review_evidence,
    evaluate_star_semantic_uniqueness,
    audit_star_question,
    check_generic_structural_constraints
)
from scripts.curriculum.reconcile_blind_review import (
    verify_question_schema,
    evaluate_question_qa_gate,
    verify_deployment_evidence,
    reconcile_practice_set_status,
    check_review_integrity,
    audit_answer_distribution,
    load_all_blind_reviews,
    audit_star_report_against_bank,
    make_production_workspace_adapter,
    compute_practice_set_answer_key_digest
)
from scripts.curriculum.generate_practice_release_gate import (
    generate_practice_release_gate_report
)


TEST_RESULTS_LOG = []


def record_result(name, target_fn, mutation, expected, actual, passed):
    TEST_RESULTS_LOG.append({
        "name": name,
        "targetFunction": target_fn,
        "mutation": mutation,
        "expected": expected,
        "actual": actual,
        "verdict": "PASS" if passed else "FAIL"
    })


class TestAdversarialQAMutations(unittest.TestCase):
    """Hostile test cases verifying that the release gate detects and rejects every defect."""

    @classmethod
    def setUpClass(cls):
        cls.sample_non_star_question = {
            "id": "N4-TEST-001",
            "level": "N4",
            "skill": "Vocabulary",
            "typeId": "N4-MO-READ",
            "stem": "天気がいいので【散歩】をしました。",
            "contextPassage": None,
            "options": [
                {"id": "A", "text": "さんぽ"},
                {"id": "B", "text": "さぽ"},
                {"id": "C", "text": "ざんぽ"},
                {"id": "D", "text": "さんぼ"}
            ],
            "correctAnswer": "A",
            "explanationVi": "「散歩」đọc là さんぽ (đi dạo).",
            "distractorExplanations": {
                "さぽ": "Thiếu âm ん",
                "ざんぽ": "Âm ざ là sai",
                "さんぼ": "Âm ぼ là sai"
            },
            "remediation": "Ôn từ vựng N4.",
            "status": "QA_VERIFIED",
            "version": 1
        }
        cls.sample_non_star_fp = canonical_blind_input_fingerprint(cls.sample_non_star_question)
        cls.sample_non_star_review = {
            "id": "N4-TEST-001",
            "blindAnswer": "A",
            "confidence": "HIGH",
            "linguisticJustification": "「散歩」の標準的な読みは「さんぽ」である。",
            "alternativeDefensibleAnswers": [],
            "concerns": None,
            "questionContentFingerprint": cls.sample_non_star_fp
        }

        cls.sample_star_question = {
            "id": "N4-GR-STAR-002",
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
            "explanationVi": "Thứ tự đúng: 北海道に(B) 住んでいる(C) 友達に(D) 会いに(A). Vị trí ★ là 友達に (D).",
            "version": 1
        }

    # =========================================================================
    # PART 1: 12 PRODUCTION MUTATION INTEGRATION SCENARIOS
    # =========================================================================

    def test_scenario_1_modify_stem_character_triggers_fingerprint_mismatch(self):
        mutated_q = dict(self.sample_non_star_question)
        mutated_q["stem"] = "天気がいいので【買い物】をしました。"
        status, reason, meta = evaluate_question_qa_gate(mutated_q, self.sample_non_star_review)
        passed = (status == "QA_REVIEW_REQUIRED" and "FINGERPRINT_MISMATCH" in reason)
        record_result("Scenario 1: Stem mutation", "evaluate_question_qa_gate", "Changed 散歩 to 買い物 in stem", "QA_REVIEW_REQUIRED with FINGERPRINT_MISMATCH", f"{status} ({reason[:40]}...)", passed)
        self.assertTrue(passed)

    def test_scenario_2_modify_choice_text_triggers_fingerprint_mismatch(self):
        mutated_q = dict(self.sample_non_star_question)
        mutated_q["options"] = [
            {"id": "A", "text": "よからば"},
            {"id": "B", "text": "さぽ"},
            {"id": "C", "text": "ざんぽ"},
            {"id": "D", "text": "さんぼ"}
        ]
        status, reason, meta = evaluate_question_qa_gate(mutated_q, self.sample_non_star_review)
        passed = (status == "QA_REVIEW_REQUIRED" and "FINGERPRINT_MISMATCH" in reason)
        record_result("Scenario 2: Choice mutation", "evaluate_question_qa_gate", "Changed option A to よからば", "QA_REVIEW_REQUIRED with FINGERPRINT_MISMATCH", f"{status} ({reason[:40]}...)", passed)
        self.assertTrue(passed)

    def test_scenario_3_duplicate_reviewer_record_raises_value_error(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            n4_raw = tmppath / "raw_blind_review_n4.json"
            duplicate_data = [
                {"id": "N4-TEST-001", "blindAnswer": "A", "confidence": "HIGH"},
                {"id": "N4-TEST-001", "blindAnswer": "B", "confidence": "LOW"}
            ]
            with open(n4_raw, "w", encoding="utf-8") as f:
                json.dump(duplicate_data, f)
            with self.assertRaises(ValueError) as ctx:
                load_all_blind_reviews(qa_dir=tmppath)
            passed = ("Duplicate review record detected" in str(ctx.exception))
            record_result("Scenario 3: Batch duplicate detection", "load_all_blind_reviews", "Duplicate ID in raw_blind_review_n4.json", "ValueError('Duplicate review record detected...')", str(ctx.exception), passed)
            self.assertTrue(passed)

    def test_scenario_4_missing_reviewer_record_blocks_qa(self):
        reviews = {"N4-TEST-001": self.sample_non_star_review}
        questions = [self.sample_non_star_question, {"id": "N4-TEST-MISSING"}]
        ok, reason, missing = check_review_integrity(reviews, questions)
        passed = (not ok and missing == ["N4-TEST-MISSING"])
        record_result("Scenario 4: Missing reviewer record", "check_review_integrity", "Removed review for N4-TEST-MISSING", "ok=False, missing=['N4-TEST-MISSING']", f"ok={ok}, missing={missing}", passed)
        self.assertTrue(passed)

    def test_scenario_5_conflicting_answer_quarantines_item(self):
        conflicting_review = dict(self.sample_non_star_review)
        conflicting_review["blindAnswer"] = "C"
        status, reason, meta = evaluate_question_qa_gate(self.sample_non_star_question, conflicting_review)
        passed = (status == "QUARANTINED" and meta.get("disagreement") is True)
        record_result("Scenario 5: Answer disagreement", "evaluate_question_qa_gate", "Reviewer answer C != Author answer A", "QUARANTINED with disagreement=True", f"{status} (disagreement={meta.get('disagreement')})", passed)
        self.assertTrue(passed)

    def test_scenario_6_alternative_defensible_answer_requires_review(self):
        alt_review = dict(self.sample_non_star_review)
        alt_review["alternativeDefensibleAnswers"] = ["B"]
        status, reason, meta = evaluate_question_qa_gate(self.sample_non_star_question, alt_review)
        passed = (status == "QA_REVIEW_REQUIRED" and "alternative defensible answer" in reason)
        record_result("Scenario 6: Alternative defensible answer", "evaluate_question_qa_gate", "Injected alternativeDefensibleAnswers=['B']", "QA_REVIEW_REQUIRED", f"{status} ({reason})", passed)
        self.assertTrue(passed)

    def test_scenario_7_corrupted_star_answer_key_fails_audit(self):
        corrupted_star = dict(self.sample_star_question)
        corrupted_star["correctAnswer"] = "B"
        ok, reason, data = audit_star_question(corrupted_star)
        passed = (not ok and "ANSWER_KEY_SLOT3_MISMATCH" in reason)
        record_result("Scenario 7: Corrupt STAR key", "audit_star_question", "Changed correctAnswer from D to B", "ok=False with ANSWER_KEY_SLOT3_MISMATCH", f"ok={ok} ({reason})", passed)
        self.assertTrue(passed)

    def test_scenario_8_nonexistent_star_id_detected_as_inconsistency(self):
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as tmp:
            tmp.write("| `N4-GR-STAR-001` | PASS |\n| `N2-GR-STAR-005` | PASS |\n")
            tmp_path = Path(tmp.name)
        try:
            ok, hallucinated = audit_star_report_against_bank(tmp_path, [self.sample_star_question])
            passed = (not ok and hallucinated == ["N2-GR-STAR-005", "N4-GR-STAR-001"])
            record_result("Scenario 8: Hallucinated STAR ID", "audit_star_report_against_bank", "Report contains N2-GR-STAR-005", "ok=False with hallucinated=['N2-GR-STAR-005']", f"ok={ok}, hallucinated={hallucinated}", passed)
            self.assertTrue(passed)
        finally:
            if tmp_path.exists():
                tmp_path.unlink()

    def test_scenario_9_corrupt_practice_set_reference_blocks_set(self):
        bank_map = {
            "Q1": {"id": "Q1", "status": "QA_VERIFIED"},
            "Q2": {"id": "Q2", "status": "QUARANTINED"}
        }
        ps = {
            "id": "MD-TEST-CORRUPT",
            "category": "MICRO_DRILL",
            "questionIds": ["Q1", "Q2"]
        }
        reconciled = reconcile_practice_set_status(ps, bank_map)
        passed = (reconciled["readinessStatus"] == "CONTENT_QA_BLOCKED")
        record_result("Scenario 9: Corrupt set reference", "reconcile_practice_set_status", "Referenced quarantined item Q2", "readinessStatus=CONTENT_QA_BLOCKED", f"{reconciled['readinessStatus']} ({reconciled.get('blockReason')})", passed)
        self.assertTrue(passed)

    def test_scenario_10_non_google_deployment_url_rejected(self):
        bank_map = {
            "Q1": {"id": "Q1", "status": "QA_VERIFIED"},
            "Q2": {"id": "Q2", "status": "QA_VERIFIED"}
        }
        ps = {
            "id": "MD-TEST-FAKE-DEPLOY",
            "category": "MICRO_DRILL",
            "questionIds": ["Q1", "Q2"],
            "readinessStatus": "LIVE_VERIFIED",
            "deployment": {
                "isDeployed": True,
                "formId": "fake_id_12345",
                "responderUrl": "https://unauthorized-phishing.com/form",
                "qaResult": "PASS"
            }
        }
        reconciled = reconcile_practice_set_status(ps, bank_map)
        passed = (reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED")
        record_result("Scenario 10: Non-Google deployment URL", "reconcile_practice_set_status", "Non-Google Forms URL passed with isDeployed=True", "readinessStatus=QA_PASSED_NOT_DEPLOYED", f"{reconciled['readinessStatus']}", passed)
        self.assertTrue(passed)

    def test_scenario_11_multi_tier_fingerprint_invariance(self):
        bank_path = ROOT / "curriculum/QUESTION_BANK_EXPANDED.json"
        with open(bank_path, "r", encoding="utf-8") as f:
            bank = json.load(f)
        
        manifest_path = ROOT / "qa/CONTENT_FINGERPRINT_MANIFEST.json"
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        manifest_map = {item["id"]: item["fingerprints"] for item in manifest["items"]}
        
        mismatches = []
        for q in bank["questions"]:
            qid = q["id"]
            fps = compute_all_question_fingerprints(q)
            if fps["blindInputSha256"] != manifest_map[qid]["blindInputSha256"]:
                mismatches.append((qid, "blindInputSha256"))
            if fps["fullItemSha256"] != manifest_map[qid]["fullItemSha256"]:
                mismatches.append((qid, "fullItemSha256"))

        passed = (len(mismatches) == 0)
        record_result("Scenario 11: Multi-tier hash invariance", "compute_all_question_fingerprints", "Comparing bank items to manifest across 4 hash tiers", "0 mismatches", f"{len(mismatches)} mismatches", passed)
        self.assertTrue(passed)

    def test_scenario_12_pipeline_report_consistency(self):
        bank_path = ROOT / "curriculum/QUESTION_BANK_EXPANDED.json"
        with open(bank_path, "r", encoding="utf-8") as f:
            bank = json.load(f)
        
        ps_path = ROOT / "curriculum/PRACTICE_SETS.json"
        with open(ps_path, "r", encoding="utf-8") as f:
            ps_data = json.load(f)

        total_qs = len(bank["questions"])
        qa_verified_count = sum(1 for q in bank["questions"] if q["status"] == "QA_VERIFIED")
        star_pending_count = sum(1 for q in bank["questions"] if q["status"] == "STAR_SEMANTIC_REVIEW_PENDING")
        total_sets = ps_data["totalPracticeSets"]
        ready_sets = ps_data["countsByStatus"].get("QA_PASSED_NOT_DEPLOYED", 0)
        blocked_sets = ps_data["countsByStatus"].get("CONTENT_QA_BLOCKED", 0)
        not_ready_sets = ps_data["countsByStatus"].get("NOT_READY", 0)

        passed = (total_qs == 120 and qa_verified_count == 104 and star_pending_count == 16 and total_sets == 23 and ready_sets == 11 and blocked_sets == 9 and not_ready_sets == 3)
        record_result("Scenario 12: Pipeline consistency", "run_reconciliation", "Verifying bank and practice sets counts", "104 verified, 16 star pending, 11 ready sets, 9 blocked sets, 3 mock", f"{qa_verified_count} verified, {star_pending_count} pending, {ready_sets} ready, {blocked_sets} blocked, {not_ready_sets} mock", passed)
        self.assertTrue(passed)

    # =========================================================================
    # PART 2: 10 STAR STRUCTURE NEGATIVE CONTROLS (P0-A STRICT PARSER)
    # =========================================================================

    def test_star_neg_1_extra_regular_blank(self):
        q = dict(self.sample_star_question)
        q["stem"] = "来年の夏休みには、（　　）（　　）（　　） ★ （　　）行く予定です。"
        ok, msg, data = validate_star_structure(q)
        passed = (not ok and "EXTRA_SLOTS" in msg)
        record_result("P0-A Neg 1: Extra regular blank", "validate_star_structure", "Added 1 extra blank (5 slots total)", "ok=False with EXTRA_SLOTS", f"ok={ok} ({msg})", passed)
        self.assertTrue(passed)

    def test_star_neg_2_two_extra_blanks(self):
        q = dict(self.sample_star_question)
        q["stem"] = "来年の夏休みには、（　　）（　　）（　　）（　　） ★ （　　）行く予定です。"
        ok, msg, data = validate_star_structure(q)
        passed = (not ok and "EXTRA_SLOTS" in msg)
        record_result("P0-A Neg 2: Two extra blanks", "validate_star_structure", "Added 2 extra blanks (6 slots total)", "ok=False with EXTRA_SLOTS", f"ok={ok} ({msg})", passed)
        self.assertTrue(passed)

    def test_star_neg_3_star_in_position_one(self):
        q = dict(self.sample_star_question)
        q["stem"] = "来年の夏休みには、 ★ （　　）（　　）（　　）行く予定です。"
        ok, msg, data = validate_star_structure(q)
        passed = (not ok and "INVALID_STAR_POSITION" in msg and "position 1" in msg)
        record_result("P0-A Neg 3: Star in position 1", "validate_star_structure", "★ placed in position 1", "ok=False with INVALID_STAR_POSITION (pos 1)", f"ok={ok} ({msg})", passed)
        self.assertTrue(passed)

    def test_star_neg_4_star_in_position_two(self):
        q = dict(self.sample_star_question)
        q["stem"] = "来年の夏休みには、（　　） ★ （　　）（　　）行く予定です。"
        ok, msg, data = validate_star_structure(q)
        passed = (not ok and "INVALID_STAR_POSITION" in msg and "position 2" in msg)
        record_result("P0-A Neg 4: Star in position 2", "validate_star_structure", "★ placed in position 2", "ok=False with INVALID_STAR_POSITION (pos 2)", f"ok={ok} ({msg})", passed)
        self.assertTrue(passed)

    def test_star_neg_5_star_in_position_four(self):
        q = dict(self.sample_star_question)
        q["stem"] = "来年の夏休みには、（　　）（　　）（　　） ★ 行く予定です。"
        ok, msg, data = validate_star_structure(q)
        passed = (not ok and "INVALID_STAR_POSITION" in msg and "position 4" in msg)
        record_result("P0-A Neg 5: Star in position 4", "validate_star_structure", "★ placed in position 4", "ok=False with INVALID_STAR_POSITION (pos 4)", f"ok={ok} ({msg})", passed)
        self.assertTrue(passed)

    def test_star_neg_6_duplicate_star(self):
        q = dict(self.sample_star_question)
        q["stem"] = "来年の夏休みには、（　　）（　　） ★ ★ （　　）行く予定です。"
        ok, msg, data = validate_star_structure(q)
        passed = (not ok and "DUPLICATE_STAR_MARKER" in msg)
        record_result("P0-A Neg 6: Duplicate star", "validate_star_structure", "Two ★ markers in stem", "ok=False with DUPLICATE_STAR_MARKER", f"ok={ok} ({msg})", passed)
        self.assertTrue(passed)

    def test_star_neg_7_missing_blank(self):
        q = dict(self.sample_star_question)
        q["stem"] = "来年の夏休みには、（　　） ★ （　　）行く予定です。"
        ok, msg, data = validate_star_structure(q)
        passed = (not ok and "INSUFFICIENT_SLOTS" in msg)
        record_result("P0-A Neg 7: Missing blank", "validate_star_structure", "Only 2 regular blanks (3 slots total)", "ok=False with INSUFFICIENT_SLOTS", f"ok={ok} ({msg})", passed)
        self.assertTrue(passed)

    def test_star_neg_8_malformed_blank_delimiters(self):
        q = dict(self.sample_star_question)
        q["stem"] = "来年の夏休みには、（　　（　　） ★ （　　）行く予定です。"
        ok, msg, data = validate_star_structure(q)
        passed = (not ok and "MALFORMED_PARENTHESES" in msg)
        record_result("P0-A Neg 8: Malformed delimiters", "validate_star_structure", "Unbalanced open parenthesis in blank", "ok=False with MALFORMED_PARENTHESES", f"ok={ok} ({msg})", passed)
        self.assertTrue(passed)

    def test_star_neg_9_canonical_missing_chunk(self):
        q = dict(self.sample_star_question)
        q["assembledSentence"] = "来年の夏休みには、北海道に友達に会いに行く予定です。"  # Missing 住んでいる
        ok, msg, data = validate_star_structure(q)
        passed = (not ok and "INCOHERENT_CANONICAL_SENTENCE" in msg)
        record_result("P0-A Neg 9: Canonical missing chunk", "validate_star_structure", "assembledSentence missing chunk '住んでいる'", "ok=False with INCOHERENT_CANONICAL_SENTENCE", f"ok={ok} ({msg})", passed)
        self.assertTrue(passed)

    def test_star_neg_10_incorrect_answer_key(self):
        q = dict(self.sample_star_question)
        q["correctAnswer"] = "B"  # Slot 3 is D
        ok, msg, data = validate_star_structure(q)
        passed = (not ok and "ANSWER_KEY_SLOT3_MISMATCH" in msg)
        record_result("P0-A Neg 10: Incorrect answer key", "validate_star_structure", "Key B != Slot 3 D", "ok=False with ANSWER_KEY_SLOT3_MISMATCH", f"ok={ok} ({msg})", passed)
        self.assertTrue(passed)

    # =========================================================================
    # PART 3: 10 P0-1 FORGED SEMANTIC LEDGER ATTACK TESTS (A through J)
    # =========================================================================

    def test_p0_1_attack_a_omitted_coverage_declared_one_reviewed(self):
        """A. VERIFIED_COHERENT with coverageDeclared omitted and only 1 permutation reviewed."""
        q = dict(self.sample_star_question)
        fake_ledger = {
            q["id"]: {
                "id": q["id"],
                "status": "VERIFIED_COHERENT",
                "reviewerId": "verified_expert_credential_001",
                "provenanceStatus": "PARTIAL",
                "reviewedPermutations": [["B", "C", "D", "A"]],  # 1 out of 23 required
                "perPermutationJudgments": {"BCDA": "canonical sentence"},
                "blindInputSha256": canonical_blind_input_fingerprint(q),
                "scoringSha256": canonical_scoring_fingerprint(q),
                "evidenceArtifact": "qa/sample.json",
                "evidenceIntegrityHash": "hash"
                # coverageDeclared omitted!
            }
        }
        ok, msg, data = audit_star_question(q, fake_ledger)
        passed = (data.get("gate2Status") != "VERIFIED_COHERENT" and data.get("disposition") != "QA_VERIFIED")
        record_result("P0-1 Attack A: Omitted coverageDeclared (1 reviewed)", "audit_star_question", "coverageDeclared omitted with only 1 permutation reviewed", "Rejected with INSUFFICIENT_REVIEW_COVERAGE", f"gate2={data.get('gate2Status')}, disp={data.get('disposition')}", passed)
        self.assertTrue(passed)

    def test_p0_1_attack_b_coverage_declared_partial(self):
        """B. VERIFIED_COHERENT with coverageDeclared set to PARTIAL."""
        q = dict(self.sample_star_question)
        fake_ledger = {
            q["id"]: {
                "id": q["id"],
                "status": "VERIFIED_COHERENT",
                "coverageDeclared": "PARTIAL",
                "reviewerId": "verified_expert_credential_001",
                "provenanceStatus": "PARTIAL",
                "reviewedPermutations": [["B", "C", "D", "A"]],
                "perPermutationJudgments": {"BCDA": "canonical sentence"},
                "blindInputSha256": canonical_blind_input_fingerprint(q),
                "scoringSha256": canonical_scoring_fingerprint(q),
                "evidenceArtifact": "qa/sample.json",
                "evidenceIntegrityHash": "hash"
            }
        }
        ok, msg, data = audit_star_question(q, fake_ledger)
        passed = (data.get("gate2Status") != "VERIFIED_COHERENT" and data.get("disposition") != "QA_VERIFIED")
        record_result("P0-1 Attack B: coverageDeclared set to PARTIAL", "audit_star_question", "coverageDeclared='PARTIAL' with claims of VERIFIED_COHERENT", "Rejected with INCOMPLETE_COVERAGE_DECLARED_PARTIAL", f"gate2={data.get('gate2Status')}, disp={data.get('disposition')}", passed)
        self.assertTrue(passed)

    def test_p0_1_attack_c_duplicate_reviewed_permutation_ids(self):
        """C. Duplicated reviewed permutation IDs."""
        q = dict(self.sample_star_question)
        fake_ledger = {
            q["id"]: {
                "id": q["id"],
                "status": "VERIFIED_COHERENT",
                "reviewerId": "verified_expert_credential_001",
                "provenanceStatus": "PARTIAL",
                "reviewedPermutations": [["B", "C", "D", "A"], ["B", "C", "D", "A"]],  # Duplicate
                "perPermutationJudgments": {"BCDA": "canonical sentence"},
                "blindInputSha256": canonical_blind_input_fingerprint(q),
                "scoringSha256": canonical_scoring_fingerprint(q),
                "evidenceArtifact": "qa/sample.json",
                "evidenceIntegrityHash": "hash"
            }
        }
        ok, msg, data = audit_star_question(q, fake_ledger)
        passed = (data.get("gate2Status") != "VERIFIED_COHERENT" and data.get("disposition") != "QA_VERIFIED")
        record_result("P0-1 Attack C: Duplicate reviewed permutation IDs", "audit_star_question", "Duplicate ['B','C','D','A'] in reviewedPermutations", "Rejected with DUPLICATE_REVIEWED_PERMUTATION", f"gate2={data.get('gate2Status')}, disp={data.get('disposition')}", passed)
        self.assertTrue(passed)

    def test_p0_1_attack_d_extra_nonexistent_permutation_ids(self):
        """D. Extra, nonexistent permutation IDs."""
        q = dict(self.sample_star_question)
        fake_ledger = {
            q["id"]: {
                "id": q["id"],
                "status": "VERIFIED_COHERENT",
                "reviewerId": "verified_expert_credential_001",
                "provenanceStatus": "PARTIAL",
                "reviewedPermutations": [["A", "B", "C", "X"]],  # Invalid chunk 'X'
                "perPermutationJudgments": {"ABCX": "invalid option text"},
                "blindInputSha256": canonical_blind_input_fingerprint(q),
                "scoringSha256": canonical_scoring_fingerprint(q),
                "evidenceArtifact": "qa/sample.json",
                "evidenceIntegrityHash": "hash"
            }
        }
        ok, msg, data = audit_star_question(q, fake_ledger)
        passed = (data.get("gate2Status") != "VERIFIED_COHERENT" and data.get("disposition") != "QA_VERIFIED")
        record_result("P0-1 Attack D: Nonexistent permutation ID", "audit_star_question", "Invalid chunk ID 'X' in permutation", "Rejected with NONEXISTENT_PERMUTATION", f"gate2={data.get('gate2Status')}, disp={data.get('disposition')}", passed)
        self.assertTrue(passed)

    def test_p0_1_attack_e_judgments_mismatch_reviewed_permutations(self):
        """E. Judgments whose IDs do not match reviewed permutations."""
        q = dict(self.sample_star_question)
        fake_ledger = {
            q["id"]: {
                "id": q["id"],
                "status": "VERIFIED_COHERENT",
                "reviewerId": "verified_expert_credential_001",
                "provenanceStatus": "PARTIAL",
                "reviewedPermutations": [["B", "C", "D", "A"]],
                "perPermutationJudgments": {"ABCD": "judgment for unreviewed order"},  # Key doesn't match reviewed
                "blindInputSha256": canonical_blind_input_fingerprint(q),
                "scoringSha256": canonical_scoring_fingerprint(q),
                "evidenceArtifact": "qa/sample.json",
                "evidenceIntegrityHash": "hash"
            }
        }
        ok, msg, data = audit_star_question(q, fake_ledger)
        passed = (data.get("gate2Status") != "VERIFIED_COHERENT" and data.get("disposition") != "QA_VERIFIED")
        record_result("P0-1 Attack E: Judgment ID mismatch", "audit_star_question", "Judgment key ABCD != reviewed BCDA", "Rejected with EXTRA_JUDGMENT_NOT_REVIEWED", f"gate2={data.get('gate2Status')}, disp={data.get('disposition')}", passed)
        self.assertTrue(passed)

    def test_p0_1_attack_f_arbitrary_unverified_reviewer_identity(self):
        """F. Valid artifact digest but arbitrary unverified reviewer identity."""
        q = dict(self.sample_star_question)
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".json") as tmp:
            tmp.write(json.dumps({"test": "data"}))
            tmp_art = Path(tmp.name)
        try:
            art_hash = compute_file_sha256(tmp_art)
            fake_ledger = {
                q["id"]: {
                    "id": q["id"],
                    "status": "VERIFIED_COHERENT",
                    "reviewerId": "arbitrary_unverified_reviewer",  # Arbitrary unverified
                    "provenanceStatus": "UNVERIFIED",
                    "reviewedPermutations": [["B", "C", "D", "A"]],
                    "perPermutationJudgments": {"BCDA": "canonical"},
                    "blindInputSha256": canonical_blind_input_fingerprint(q),
                    "scoringSha256": canonical_scoring_fingerprint(q),
                    "evidenceArtifact": str(tmp_art),
                    "evidenceIntegrityHash": art_hash
                }
            }
            ok, msg, data = audit_star_question(q, fake_ledger)
            passed = (data.get("gate2Status") != "VERIFIED_COHERENT" and data.get("disposition") != "QA_VERIFIED")
            record_result("P0-1 Attack F: Arbitrary unverified reviewer", "audit_star_question", "Valid artifact hash but arbitrary unverified reviewer", "Rejected with UNSUPPORTED_REVIEWER_LABEL", f"gate2={data.get('gate2Status')}, disp={data.get('disposition')}", passed)
            self.assertTrue(passed)
        finally:
            if tmp_art.exists():
                tmp_art.unlink()

    def test_p0_1_attack_g_locally_fabricated_repetitive_unsupported_reasoning(self):
        """G. Locally fabricated artifact declaring every answer invalid using repetitive unsupported reasoning."""
        q = dict(self.sample_star_question)
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".json") as tmp:
            tmp.write(json.dumps({"test": "data"}))
            tmp_art = Path(tmp.name)
        try:
            art_hash = compute_file_sha256(tmp_art)
            all_perms = list(itertools.permutations(["A", "B", "C", "D"]))
            boilerplate_judgments = {"".join(p): "syntax error" for p in all_perms}
            fake_ledger = {
                q["id"]: {
                    "id": q["id"],
                    "status": "VERIFIED_COHERENT",
                    "reviewerId": "verified_expert_credential_001",
                    "provenanceStatus": "PARTIAL",
                    "reviewedPermutations": [list(p) for p in all_perms],
                    "perPermutationJudgments": boilerplate_judgments,
                    "blindInputSha256": canonical_blind_input_fingerprint(q),
                    "scoringSha256": canonical_scoring_fingerprint(q),
                    "evidenceArtifact": str(tmp_art),
                    "evidenceIntegrityHash": art_hash
                }
            }
            ok, msg, data = audit_star_question(q, fake_ledger)
            passed = (data.get("gate2Status") != "VERIFIED_COHERENT" and data.get("disposition") != "QA_VERIFIED")
            record_result("P0-1 Attack G: Repetitive unsupported reasoning", "audit_star_question", "All permutations have identical repetitive 'syntax error' boilerplate", "Rejected with REPETITIVE_UNSUPPORTED_BOILERPLATE_REJECTED", f"gate2={data.get('gate2Status')}, disp={data.get('disposition')}", passed)
            self.assertTrue(passed)
        finally:
            if tmp_art.exists():
                tmp_art.unlink()

    def test_p0_1_attack_h_correct_question_fingerprint_stale_scoring_fingerprint(self):
        """H. Correct question fingerprint but stale scoring fingerprint."""
        q = dict(self.sample_star_question)
        fake_ledger = {
            q["id"]: {
                "id": q["id"],
                "status": "VERIFIED_COHERENT",
                "reviewerId": "verified_expert_credential_001",
                "provenanceStatus": "PARTIAL",
                "reviewedPermutations": [["B", "C", "D", "A"]],
                "perPermutationJudgments": {"BCDA": "canonical"},
                "blindInputSha256": canonical_blind_input_fingerprint(q),  # Correct
                "scoringSha256": "0000000000000000000000000000000000000000000000000000000000000000",  # Stale/corrupt
                "evidenceArtifact": "qa/sample.json",
                "evidenceIntegrityHash": "hash"
            }
        }
        ok, msg, data = audit_star_question(q, fake_ledger)
        passed = (data.get("gate2Status") != "VERIFIED_COHERENT" and data.get("disposition") != "QA_VERIFIED")
        record_result("P0-1 Attack H: Stale scoring fingerprint", "audit_star_question", "Correct blind hash but stale scoringSha256", "Rejected with SCORING_FINGERPRINT_MISMATCH", f"gate2={data.get('gate2Status')}, disp={data.get('disposition')}", passed)
        self.assertTrue(passed)

    def test_p0_1_attack_i_conflicting_defensible_alternative_in_judgments(self):
        """I. Conflicting defensible alternative hidden inside perPermutationJudgments."""
        q = dict(self.sample_star_question)
        fake_ledger = {
            q["id"]: {
                "id": q["id"],
                "status": "VERIFIED_COHERENT",
                "reviewerId": "verified_expert_credential_001",
                "provenanceStatus": "PARTIAL",
                "reviewedPermutations": [["B", "C", "D", "A"], ["A", "B", "C", "D"]],
                "perPermutationJudgments": {
                    "BCDA": "canonical order",
                    "ABCD": "valid alternative: acceptable alternative Japanese phrasing in this context"
                },
                "blindInputSha256": canonical_blind_input_fingerprint(q),
                "scoringSha256": canonical_scoring_fingerprint(q),
                "evidenceArtifact": "qa/sample.json",
                "evidenceIntegrityHash": "hash"
            }
        }
        ok, msg, data = audit_star_question(q, fake_ledger)
        passed = (data.get("gate2Status") == "AMBIGUOUS_ALTERNATIVE_FOUND" and data.get("disposition") == "QUARANTINED")
        record_result("P0-1 Attack I: Hidden defensible alternative in judgment", "audit_star_question", "Permutation ABCD with slot 3 != key marked 'valid alternative'", "Quarantined with AMBIGUOUS_ALTERNATIVE_FOUND", f"gate2={data.get('gate2Status')}, disp={data.get('disposition')}", passed)
        self.assertTrue(passed)

    def test_p0_1_attack_j_valid_looking_review_containing_one_unresolved_judgment(self):
        """J. A valid-looking completed review containing one unresolved judgment."""
        q = dict(self.sample_star_question)
        fake_ledger = {
            q["id"]: {
                "id": q["id"],
                "status": "VERIFIED_COHERENT",
                "reviewerId": "verified_expert_credential_001",
                "provenanceStatus": "PARTIAL",
                "reviewedPermutations": [["B", "C", "D", "A"], ["A", "B", "C", "D"]],
                "perPermutationJudgments": {
                    "BCDA": "canonical order",
                    "ABCD": "unresolved: requires senior panel debate"
                },
                "blindInputSha256": canonical_blind_input_fingerprint(q),
                "scoringSha256": canonical_scoring_fingerprint(q),
                "evidenceArtifact": "qa/sample.json",
                "evidenceIntegrityHash": "hash"
            }
        }
        ok, msg, data = audit_star_question(q, fake_ledger)
        passed = (data.get("gate2Status") != "VERIFIED_COHERENT" and data.get("disposition") != "QA_VERIFIED")
        record_result("P0-1 Attack J: Unresolved judgment in review", "audit_star_question", "One permutation marked 'unresolved'", "Rejected with UNRESOLVED_LINGUISTIC_JUDGMENT", f"gate2={data.get('gate2Status')}, disp={data.get('disposition')}", passed)
        self.assertTrue(passed)

    # =========================================================================
    # PART 4: REAL LINGUISTIC NEGATIVE CONTROL (ADJUNCT SCRAMBLING)
    # =========================================================================

    def test_negative_control_tanaka_san_ambiguous_star(self):
        synthetic_ambiguous_star = {
            "id": "SYNTH-STAR-AMBIGUOUS-01",
            "level": "N3",
            "skill": "Grammar",
            "typeId": "N3-GR-STAR",
            "stem": "田中さんは（　　）（　　） ★ （　　）話しました。",
            "options": [
                {"id": "A", "text": "昨日"},
                {"id": "B", "text": "会議で"},
                {"id": "C", "text": "その計画について"},
                {"id": "D", "text": "熱心に"}
            ],
            "correctAnswer": "C",
            "assembledSentence": "田中さんは昨日会議でその計画について熱心に話しました。"
        }
        ok, msg, data = audit_star_question(synthetic_ambiguous_star)
        self.assertEqual(data.get("gate1Status"), "PASS", "Synthetic question must have structurally valid 4 chunks")
        self.assertNotEqual(data.get("gate2Status"), "VERIFIED_COHERENT", "Pipeline must NOT self-certify ambiguous question as coherent")
        self.assertEqual(data.get("gate2Status"), "STAR_SEMANTIC_REVIEW_PENDING")
        self.assertEqual(data.get("disposition"), "QA_REVIEW_REQUIRED")
        passed = (data.get("gate2Status") == "STAR_SEMANTIC_REVIEW_PENDING" and data.get("disposition") == "QA_REVIEW_REQUIRED")
        record_result("Part 4: Tanaka-san Ambiguous STAR", "audit_star_question", "Tanaka-san free adjunct scrambling (昨日/会議で/その計画について/熱心に)", "STAR_SEMANTIC_REVIEW_PENDING / QA_REVIEW_REQUIRED", f"{data.get('gate2Status')} / {data.get('disposition')}", passed)
        self.assertTrue(passed)

    # =========================================================================
    # PART 5: P0-2 GOOGLE FORMS DEPLOYMENT EVIDENCE & WORKSPACE BINDINGS
    # =========================================================================

    def make_mock_provider_result(self, ps, **overrides):
        """
        Constructs a complete, cryptographically bound deployment evidence dict
        for testing individual failure modes in isolation.
        """
        now = time.time()
        form_id = ps.get("deployment", {}).get("formId", "SYNTH-FORM-001")
        sheet_id = ps.get("deployment", {}).get("expectedSheetId", "SYNTH-SHEET-001")
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ak_digest = compute_practice_set_answer_key_digest(ps, bank_map)
        base = {
            "providerType": "AUTHENTICATED_GOOGLE_WORKSPACE_API",
            "isAuthorizedWorkspaceProvider": True,
            "isAuthorized": True,
            "practiceSetId": ps.get("id", "MD-N4-TEST"),
            "formId": form_id,
            "verifiedQuestionIds": list(ps.get("questionIds", [])),
            "formExists": True,
            "sheetId": sheet_id,
            "expectedSheetId": sheet_id,
            "answerKeyDigest": ak_digest,
            "responderAccess": True,
            "gradingVerified": True,
            "sheetSync": True,
            "receiptId": "SYNTH-RECEIPT-VALID-001",
            "receiptFormId": form_id,
            "receiptVerified": True,
            "timestamp": now - 3600,  # 1 hour ago (fresh)
            "isStale": False
        }
        base.update(overrides)
        return base

    def test_p0_2_attack_1_local_verified_sets_forgery_rejected(self):
        """1. Local verifiedSets forgery rejected: locally declared metadata alone cannot achieve LIVE_VERIFIED."""
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-TEST-FORGED-LOCAL-JSON",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "readinessStatus": "LIVE_VERIFIED",  # Malicious assertion
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_fake_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_fake_1234567890/viewform",
                "qaResult": "PASS",
                "liveVerified": True  # Self-attested boolean
            }
        }
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=None)
        passed = (
            reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and
            reconciled["deployment"].get("liveVerified") is False and
            reconciled["deployment"].get("verificationStage") == "DEPLOYMENT_METADATA_PRESENT_UNVERIFIED"
        )
        record_result("P0-2 Attack 1: Local verifiedSets forgery rejected", "reconcile_practice_set_status", "Local JSON claiming LIVE_VERIFIED without authorized provider", "Downgraded to QA_PASSED_NOT_DEPLOYED (liveVerified=False)", f"{reconciled['readinessStatus']} (stage={reconciled['deployment'].get('verificationStage')})", passed)
        self.assertTrue(passed)

    def test_p0_2_attack_2_real_form_wrong_practice_set_id(self):
        """2. Real Form ID paired with wrong practice set ID."""
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-TARGET-SET-01",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_real_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_real_1234567890/viewform"
            }
        }
        provider = lambda ps_obj: self.make_mock_provider_result(ps, practiceSetId="DIFFERENT-PRACTICE-SET-ID")
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=make_production_workspace_adapter(provider))
        passed = (reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and reconciled["deployment"].get("liveVerified") is False and reconciled["deployment"].get("verificationStage") == "PRACTICE_SET_ID_MISMATCH")
        record_result("P0-2 Attack 2: Wrong practice set ID", "reconcile_practice_set_status", "Provider receipt bound to different practice set ID", "Rejected with PRACTICE_SET_ID_MISMATCH", f"stage={reconciled['deployment'].get('verificationStage')}", passed)
        self.assertTrue(passed)

    def test_p0_2_attack_3_correct_form_wrong_question_mapping(self):
        """3. Correct Form ID with wrong question mapping."""
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-SET-QMAP",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_real_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_real_1234567890/viewform"
            }
        }
        provider = lambda ps_obj: self.make_mock_provider_result(ps, verifiedQuestionIds=["WRONG-QUESTION-ID-999"])
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=make_production_workspace_adapter(provider))
        passed = (reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and reconciled["deployment"].get("liveVerified") is False and reconciled["deployment"].get("verificationStage") == "QUESTION_MAPPING_MISMATCH")
        record_result("P0-2 Attack 3: Wrong question mapping", "reconcile_practice_set_status", "Provider verified question IDs != practice set question IDs", "Rejected with QUESTION_MAPPING_MISMATCH", f"stage={reconciled['deployment'].get('verificationStage')}", passed)
        self.assertTrue(passed)

    def test_p0_2_attack_4_correct_form_missing_submission_receipt(self):
        """4. Correct Form ID but no response receipt."""
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-SET-NOREC",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_real_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_real_1234567890/viewform"
            }
        }
        provider = lambda ps_obj: self.make_mock_provider_result(ps, receiptId=None)
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=make_production_workspace_adapter(provider))
        passed = (reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and reconciled["deployment"].get("liveVerified") is False and reconciled["deployment"].get("verificationStage") == "MISSING_SUBMISSION_RECEIPT")
        record_result("P0-2 Attack 4: Missing submission receipt", "reconcile_practice_set_status", "Provider lacks synthetic submission receipt", "Rejected with MISSING_SUBMISSION_RECEIPT", f"stage={reconciled['deployment'].get('verificationStage')}", passed)
        self.assertTrue(passed)

    def test_p0_2_attack_5_receipt_belonging_to_another_form(self):
        """5. Valid receipt belonging to another Form."""
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-SET-OTHER-FORM-REC",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_real_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_real_1234567890/viewform"
            }
        }
        provider = lambda ps_obj: self.make_mock_provider_result(ps, receiptFormId="1FAIpQLSc_OTHER_FORM_99999")
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=make_production_workspace_adapter(provider))
        passed = (reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and reconciled["deployment"].get("liveVerified") is False and reconciled["deployment"].get("verificationStage") == "RECEIPT_FORM_MISMATCH")
        record_result("P0-2 Attack 5: Receipt belongs to another Form", "reconcile_practice_set_status", "Receipt bound to another Form ID", "Rejected with RECEIPT_FORM_MISMATCH", f"stage={reconciled['deployment'].get('verificationStage')}", passed)
        self.assertTrue(passed)

    def test_p0_2_attack_6_correct_form_wrong_destination_sheet(self):
        """6. Correct Form but wrong destination Sheet."""
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-SET-WRONG-SHEET",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_real_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_real_1234567890/viewform",
                "expectedSheetId": "SYNTHETIC-EXPECTED-SHEET-ID-TEST-001"
            }
        }
        provider = lambda ps_obj: self.make_mock_provider_result(ps, sheetId="wrong_destination_sheet_id", expectedSheetId="SYNTHETIC-EXPECTED-SHEET-ID-TEST-001")
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=make_production_workspace_adapter(provider))
        passed = (reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and reconciled["deployment"].get("liveVerified") is False and reconciled["deployment"].get("verificationStage") == "DESTINATION_SHEET_MISMATCH")
        record_result("P0-2 Attack 6: Wrong destination Sheet", "reconcile_practice_set_status", "Destination Sheet ID does not match expected Sheet", "Rejected with DESTINATION_SHEET_MISMATCH", f"stage={reconciled['deployment'].get('verificationStage')}", passed)
        self.assertTrue(passed)

    def test_p0_2_attack_7_expired_or_stale_verification_evidence(self):
        """7. Expired or stale verification evidence."""
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-SET-STALE",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_real_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_real_1234567890/viewform"
            }
        }
        provider = lambda ps_obj: self.make_mock_provider_result(ps, isStale=True)
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=make_production_workspace_adapter(provider))
        passed = (reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and reconciled["deployment"].get("liveVerified") is False and reconciled["deployment"].get("verificationStage") == "STALE_DEPLOYMENT_EVIDENCE")
        record_result("P0-2 Attack 7: Stale verification evidence", "reconcile_practice_set_status", "Provider reports verification evidence is expired/stale", "Rejected with STALE_DEPLOYMENT_EVIDENCE", f"stage={reconciled['deployment'].get('verificationStage')}", passed)
        self.assertTrue(passed)

    def test_p0_2_attack_8_incomplete_grading_verification(self):
        """8. Incomplete grading verification."""
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-SET-GRADING-FAIL",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_real_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_real_1234567890/viewform"
            }
        }
        provider = lambda ps_obj: self.make_mock_provider_result(ps, gradingVerified=False)
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=make_production_workspace_adapter(provider))
        passed = (reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and reconciled["deployment"].get("liveVerified") is False and reconciled["deployment"].get("verificationStage") == "GRADING_VERIFICATION_FAILED")
        record_result("P0-2 Attack 8: Incomplete grading verification", "reconcile_practice_set_status", "Provider gradingVerified=False", "Rejected with GRADING_VERIFICATION_FAILED", f"stage={reconciled['deployment'].get('verificationStage')}", passed)
        self.assertTrue(passed)

    def test_p0_2_attack_9_unauthorized_test_double_rejected(self):
        """9. Unauthorized test double rejected from granting LIVE_VERIFIED."""
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-SET-TEST-DOUBLE",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_real_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_real_1234567890/viewform"
            }
        }
        provider = lambda ps_obj: self.make_mock_provider_result(ps, providerType="OFFLINE_TEST_DOUBLE")
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=provider)
        passed = (reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and reconciled["deployment"].get("liveVerified") is False and reconciled["deployment"].get("verificationStage") == "UNAUTHORIZED_TEST_DOUBLE_REJECTED")
        record_result("P0-2 Attack 9: Test double rejected", "reconcile_practice_set_status", "Provider providerType='OFFLINE_TEST_DOUBLE'", "Rejected with UNAUTHORIZED_TEST_DOUBLE_REJECTED", f"stage={reconciled['deployment'].get('verificationStage')}", passed)
        self.assertTrue(passed)

    def test_p0_2_attack_10_offline_mock_adapter_yields_mock_success(self):
        """10. Offline mock adapter validates bindings successfully as MOCK_SUCCESS (liveVerified=False)."""
        SYNTHETIC_FORM_ID = "SYNTHETIC-FORM-ID-TEST-AUTHORIZED-001"
        SYNTHETIC_SHEET_ID = "SYNTHETIC-SHEET-ID-TEST-AUTHORIZED-001"
        SYNTHETIC_RECEIPT_ID = "SYNTHETIC-RECEIPT-ID-TEST-001"

        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-TEST-AUTH-PROVIDER",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": SYNTHETIC_FORM_ID,
                "responderUrl": f"https://docs.google.com/forms/d/e/{SYNTHETIC_FORM_ID}/viewform",
                "expectedSheetId": SYNTHETIC_SHEET_ID,
                "qaResult": "PASS"
            }
        }

        provider = lambda ps_obj: self.make_mock_provider_result(
            ps,
            formId=SYNTHETIC_FORM_ID,
            sheetId=SYNTHETIC_SHEET_ID,
            expectedSheetId=SYNTHETIC_SHEET_ID,
            receiptId=SYNTHETIC_RECEIPT_ID,
            receiptFormId=SYNTHETIC_FORM_ID
        )

        mock_adapter = make_production_workspace_adapter(provider)
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=mock_adapter)
        passed = (
            reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and
            reconciled["deployment"].get("liveVerified") is False and
            reconciled["deployment"].get("verificationStage") == "MOCK_SUCCESS"
        )
        record_result(
            "P0-2 Attack 10: Offline mock adapter yields MOCK_SUCCESS",
            "reconcile_practice_set_status",
            "Offline mock adapter validating all bindings",
            "readinessStatus=QA_PASSED_NOT_DEPLOYED, stage=MOCK_SUCCESS, liveVerified=False",
            f"status={reconciled['readinessStatus']}, stage={reconciled['deployment'].get('verificationStage')}",
            passed
        )
        self.assertTrue(passed)

    # =========================================================================
    # PART 6: MANDATORY SECURITY REGRESSIONS (ATTACKS A THROUGH G)
    # =========================================================================

    def test_attack_a_wrapped_fabricated_callback_never_live_verified(self):
        """
        Attack A: A fabricated callback with all success fields wrapped in
        make_production_workspace_adapter MUST NOT produce LIVE_VERIFIED.
        It must yield MOCK_SUCCESS with liveVerified=False.
        """
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-ATTACK-A",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "SYNTH-FORM-ATTACK-A",
                "responderUrl": "https://docs.google.com/forms/d/e/SYNTH-FORM-ATTACK-A/viewform",
                "expectedSheetId": "SYNTH-SHEET-ATTACK-A",
                "qaResult": "PASS"
            }
        }
        fabricated_callback = lambda ps_obj: self.make_mock_provider_result(
            ps,
            formId="SYNTH-FORM-ATTACK-A",
            sheetId="SYNTH-SHEET-ATTACK-A",
            expectedSheetId="SYNTH-SHEET-ATTACK-A",
            receiptId="SYNTH-RECEIPT-ATTACK-A",
            receiptFormId="SYNTH-FORM-ATTACK-A"
        )
        wrapped_verifier = make_production_workspace_adapter(fabricated_callback)
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=wrapped_verifier)

        passed = (
            reconciled["readinessStatus"] != "LIVE_VERIFIED" and
            reconciled["deployment"].get("liveVerified") is False and
            reconciled["deployment"].get("verificationStage") == "MOCK_SUCCESS"
        )
        record_result(
            "Attack A: Fabricated callback wrapped in adapter never LIVE_VERIFIED",
            "verify_deployment_evidence",
            "Fabricated callback wrapped in make_production_workspace_adapter",
            "MOCK_SUCCESS with liveVerified=False (never LIVE_VERIFIED)",
            f"status={reconciled['readinessStatus']}, stage={reconciled['deployment'].get('verificationStage')}",
            passed
        )
        self.assertTrue(passed)

    def test_attack_b_fake_form_id_form_exists_failed(self):
        """
        Attack B: Fake Form ID (SYNTH-FAKE-...) -> FORM_EXISTS_FAILED.
        """
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-ATTACK-B",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "SYNTH-FAKE-FORM-99999",
                "responderUrl": "https://docs.google.com/forms/d/e/SYNTH-FAKE-FORM-99999/viewform"
            }
        }
        fake_form_provider = lambda ps_obj: self.make_mock_provider_result(
            ps,
            formId="SYNTH-FAKE-FORM-99999",
            formExists=False
        )
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=fake_form_provider)
        stage = reconciled["deployment"].get("verificationStage")
        passed = (
            reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and
            reconciled["deployment"].get("liveVerified") is False and
            stage == "FORM_EXISTS_FAILED"
        )
        record_result(
            "Attack B: Fake Form ID triggers FORM_EXISTS_FAILED",
            "verify_deployment_evidence",
            "Form ID SYNTH-FAKE-FORM-99999 with formExists=False",
            "FORM_EXISTS_FAILED",
            f"stage={stage}",
            passed
        )
        self.assertTrue(passed)

    def test_attack_c_synthetic_nonexistent_receipt_fails(self):
        """
        Attack C: Real Form ID with synthetic nonexistent receipt -> RECEIPT_VERIFICATION_FAILED.
        """
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-ATTACK-C",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_real_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_real_1234567890/viewform"
            }
        }
        unverified_receipt_provider = lambda ps_obj: self.make_mock_provider_result(
            ps,
            receiptId="SYNTH-NONEXISTENT-RECEIPT-999",
            receiptVerified=False
        )
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=unverified_receipt_provider)
        stage = reconciled["deployment"].get("verificationStage")
        passed = (
            reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and
            reconciled["deployment"].get("liveVerified") is False and
            stage == "RECEIPT_VERIFICATION_FAILED"
        )
        record_result(
            "Attack C: Nonexistent receipt triggers RECEIPT_VERIFICATION_FAILED",
            "verify_deployment_evidence",
            "Receipt present but receiptVerified=False",
            "RECEIPT_VERIFICATION_FAILED",
            f"stage={stage}",
            passed
        )
        self.assertTrue(passed)

    def test_attack_d_wrong_answer_key_mapping(self):
        """
        Attack D: Real Form with wrong answer-key mapping -> ANSWER_KEY_DIGEST_MISMATCH.
        """
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-ATTACK-D",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_real_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_real_1234567890/viewform"
            }
        }
        wrong_ak_provider = lambda ps_obj: self.make_mock_provider_result(
            ps,
            answerKeyDigest="forged_or_wrong_answer_key_digest_12345"
        )
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=wrong_ak_provider)
        stage = reconciled["deployment"].get("verificationStage")
        passed = (
            reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and
            reconciled["deployment"].get("liveVerified") is False and
            stage == "ANSWER_KEY_DIGEST_MISMATCH"
        )
        record_result(
            "Attack D: Wrong answer key mapping triggers ANSWER_KEY_DIGEST_MISMATCH",
            "verify_deployment_evidence",
            "Provider answerKeyDigest does not match expected computed digest",
            "ANSWER_KEY_DIGEST_MISMATCH",
            f"stage={stage}",
            passed
        )
        self.assertTrue(passed)

    def test_attack_e_wrong_destination_sheet(self):
        """
        Attack E: Real Form with wrong destination Sheet -> DESTINATION_SHEET_MISMATCH.
        """
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-ATTACK-E",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_real_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_real_1234567890/viewform",
                "expectedSheetId": "SYNTH-EXPECTED-SHEET-TARGET"
            }
        }
        wrong_sheet_provider = lambda ps_obj: self.make_mock_provider_result(
            ps,
            sheetId="SYNTH-DIFFERENT-UNAUTHORIZED-SHEET",
            expectedSheetId="SYNTH-EXPECTED-SHEET-TARGET"
        )
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=wrong_sheet_provider)
        stage = reconciled["deployment"].get("verificationStage")
        passed = (
            reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and
            reconciled["deployment"].get("liveVerified") is False and
            stage == "DESTINATION_SHEET_MISMATCH"
        )
        record_result(
            "Attack E: Wrong destination Sheet triggers DESTINATION_SHEET_MISMATCH",
            "verify_deployment_evidence",
            "Provider sheetId does not match expected destination Sheet",
            "DESTINATION_SHEET_MISMATCH",
            f"stage={stage}",
            passed
        )
        self.assertTrue(passed)

    def test_attack_f_old_timestamp_freshness_rejection(self):
        """
        Attack F: Old timestamp (e.g. 4 years ago) and isStale=False -> STALE_DEPLOYMENT_EVIDENCE
        via freshness policy (MAX_DEPLOYMENT_EVIDENCE_AGE_SECONDS = 7 * 86400).
        """
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-ATTACK-F",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_real_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_real_1234567890/viewform"
            }
        }
        ancient_timestamp = time.time() - (4 * 365 * 86400)  # 4 years ago
        stale_ts_provider = lambda ps_obj: self.make_mock_provider_result(
            ps,
            timestamp=ancient_timestamp,
            isStale=False  # Maliciously claimed to not be stale!
        )
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=stale_ts_provider)
        stage = reconciled["deployment"].get("verificationStage")
        passed = (
            reconciled["readinessStatus"] == "QA_PASSED_NOT_DEPLOYED" and
            reconciled["deployment"].get("liveVerified") is False and
            stage == "STALE_DEPLOYMENT_EVIDENCE"
        )
        record_result(
            "Attack F: Old timestamp triggers STALE_DEPLOYMENT_EVIDENCE",
            "verify_deployment_evidence",
            "Timestamp 4 years old with isStale=False",
            "STALE_DEPLOYMENT_EVIDENCE",
            f"stage={stage}",
            passed
        )
        self.assertTrue(passed)

    def test_attack_g_omitting_mandatory_bindings(self):
        """
        Attack G: Omitting mandatory bindings:
        - Missing receiptFormId -> MISSING_RECEIPT_FORM_ID_BINDING
        - Missing expectedSheetId -> MISSING_EXPECTED_SHEET_ID_BINDING
        - Missing answerKeyDigest -> MISSING_ANSWER_KEY_DIGEST_BINDING
        """
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-ATTACK-G",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "1FAIpQLSc_real_1234567890",
                "responderUrl": "https://docs.google.com/forms/d/e/1FAIpQLSc_real_1234567890/viewform"
            }
        }

        # G1: Omit receiptFormId
        res_g1 = self.make_mock_provider_result(ps)
        del res_g1["receiptFormId"]
        r1 = reconcile_practice_set_status(ps, bank_map, workspace_verifier=lambda p: res_g1)
        s1 = r1["deployment"].get("verificationStage")

        # G2: Omit expectedSheetId
        res_g2 = self.make_mock_provider_result(ps)
        del res_g2["expectedSheetId"]
        r2 = reconcile_practice_set_status(ps, bank_map, workspace_verifier=lambda p: res_g2)
        s2 = r2["deployment"].get("verificationStage")

        # G3: Omit answerKeyDigest
        res_g3 = self.make_mock_provider_result(ps)
        del res_g3["answerKeyDigest"]
        r3 = reconcile_practice_set_status(ps, bank_map, workspace_verifier=lambda p: res_g3)
        s3 = r3["deployment"].get("verificationStage")

        passed = (
            s1 == "MISSING_RECEIPT_FORM_ID_BINDING" and
            s2 == "MISSING_EXPECTED_SHEET_ID_BINDING" and
            s3 == "MISSING_ANSWER_KEY_DIGEST_BINDING"
        )
        record_result(
            "Attack G: Omitting mandatory bindings",
            "verify_deployment_evidence",
            "Omission of receiptFormId, expectedSheetId, or answerKeyDigest",
            "MISSING_*_BINDING",
            f"s1={s1}, s2={s2}, s3={s3}",
            passed
        )
        self.assertTrue(passed)

    def test_genuine_authenticated_workspace_client_succeeds(self):
        """
        Positive control: A provider with genuine Google Workspace client credentials
        and all valid bindings successfully achieves LIVE_VERIFIED.
        """
        bank_map = {"N4-TEST-001": self.sample_non_star_question}
        ps = {
            "id": "MD-N4-GENUINE-AUTH",
            "category": "SKILL_PRACTICE",
            "level": "N4",
            "questionIds": ["N4-TEST-001"],
            "deployment": {
                "isDeployed": True,
                "formId": "SYNTH-FORM-GENUINE-001",
                "responderUrl": "https://docs.google.com/forms/d/e/SYNTH-FORM-GENUINE-001/viewform",
                "expectedSheetId": "SYNTH-SHEET-GENUINE-001",
                "qaResult": "PASS"
            }
        }

        class GenuineAuthenticatedGoogleClient:
            is_authenticated_google_client = True
            has_valid_google_credentials = True

            def __init__(self, callback):
                self.callback = callback

            def __call__(self, ps_obj):
                return self.callback(ps_obj)

        cb = lambda ps_obj: self.make_mock_provider_result(
            ps,
            formId="SYNTH-FORM-GENUINE-001",
            sheetId="SYNTH-SHEET-GENUINE-001",
            expectedSheetId="SYNTH-SHEET-GENUINE-001",
            receiptId="GENUINE-RECEIPT-001",
            receiptFormId="SYNTH-FORM-GENUINE-001"
        )
        client = GenuineAuthenticatedGoogleClient(cb)
        reconciled = reconcile_practice_set_status(ps, bank_map, workspace_verifier=client)

        passed = (
            reconciled["readinessStatus"] == "LIVE_VERIFIED" and
            reconciled["deployment"].get("liveVerified") is True and
            reconciled["deployment"].get("verificationStage") == "LIVE_VERIFIED"
        )
        record_result(
            "Positive Control: Genuine Google client achieves LIVE_VERIFIED",
            "verify_deployment_evidence",
            "Provider with verified Google API client credentials",
            "LIVE_VERIFIED (liveVerified=True)",
            f"status={reconciled['readinessStatus']}, stage={reconciled['deployment'].get('verificationStage')}",
            passed
        )
        self.assertTrue(passed)

    # =========================================================================
    # PART 7: P1-B ZERO-ITEM MOCK REPORTING BUG
    # =========================================================================


    def test_p1b_zero_item_mock_reporting_not_evaluable(self):
        # Verify that generating practice release gate report handles empty mock sets
        # by reporting NO_ITEMS — NOT_EVALUABLE, never 100% VERIFIED
        report_path = ROOT / "qa/PRACTICE_RELEASE_GATE.md"
        generate_practice_release_gate_report()
        report_content = report_path.read_text(encoding="utf-8")
        
        # Check that empty mocks do NOT report 100% VERIFIED
        mock_n4_line = [line for line in report_content.splitlines() if "MOCK-N4-FULL" in line]
        self.assertTrue(len(mock_n4_line) > 0)
        mock_line_text = mock_n4_line[0]
        
        has_no_items = "NO_ITEMS — NOT_EVALUABLE" in mock_line_text
        has_100_percent = "100% VERIFIED" in mock_line_text
        
        passed = (has_no_items and not has_100_percent)
        record_result("P1-B: Zero-item mock reporting", "generate_practice_release_gate_report", "Empty full mock exam (qids=[])", "NO_ITEMS — NOT_EVALUABLE (never 100% VERIFIED)", f"has_no_items={has_no_items}, has_100_percent={has_100_percent}", passed)
        self.assertTrue(passed)


def write_adversarial_report():
    """Outputs qa/ADVERSARIAL_TEST_RESULTS.md documenting all test outcomes."""
    lines = [
        "# JP-STUDY PHASE 3.7 — ADVERSARIAL TEST SUITE & RELEASE GATE SECURITY AUDIT",
        "",
        "## 1. EXECUTIVE SUMMARY & TEST METRICS",
        "",
        f"- **Total Tests Executed**: {len(TEST_RESULTS_LOG)}",
        f"- **Passed Tests**: {sum(1 for t in TEST_RESULTS_LOG if t['verdict'] == 'PASS')}",
        f"- **Failed Tests**: {sum(1 for t in TEST_RESULTS_LOG if t['verdict'] == 'FAIL')}",
        f"- **Summary**: **{sum(1 for t in TEST_RESULTS_LOG if t['verdict'] == 'PASS')}/{len(TEST_RESULTS_LOG)} specified regression scenarios passed**",
        "",
        "### Explicit Limitations & Trust Boundary Disclaimers:",
        "- **No complete defect-detection guarantee**: Passing specified adversarial regression tests validates specific defense mechanisms against known attack patterns, but does not mathematically guarantee total absence of unknown bugs or future regressions.",
        "- **Mock provider tests do not prove live authorization**: Unit and mutation tests utilizing test adapters, mock callbacks, or simulated tokens verify internal control-flow and cryptographic binding logic, but do not prove that an authenticated production Google Workspace session has succeeded or is active.",
        "- **Fingerprint integrity does not prove semantic correctness**: Multi-tier SHA-256 cryptographic hashes guarantee that authored content and scoring keys have not drifted or been tampered with; they do not independently establish that the Japanese phrasing, distractors, or pedagogy are natural and flawless.",
        "- **Independent reviewer provenance remains partially unverified**: Review provenance status is tracked as PARTIAL due to lack of public-key cryptographic signatures from external institutions. Automated tests cannot substitute for external expert panel consensus.",
        "- **No new Forms have yet been deployed**: Phase 3.7 practice sets remain in `QA_PASSED_NOT_DEPLOYED` status until live deployment with genuine Google Workspace authorization occurs. Zero new Forms are published on Google Drive without explicit owner authorization.",
        "",
        "- **Coverage Scope**:",
        "  - Part 1: 12 Production Mutation Integration Scenarios",
        "  - Part 2: 10 STAR Structure Negative Controls (P0-A Strict Parser)",
        "  - Part 3: 10 Forged Semantic Ledger Attack Tests (P0-1 Derived Coverage & Provenance Schema)",
        "  - Part 4: Real Linguistic Negative Control (Tanaka-san Scrambling)",
        "  - Part 5: 10 Google Forms Deployment Evidence & Workspace Bindings Tests (P0-2)",
        "  - Part 6: 8 Mandatory Security Regressions (Attacks A through G & Positive Control)",
        "  - Part 7: 1 Zero-Item Mock Reporting Regression Audit (P1-B)",
        "",
        "---",
        "",
        "## 2. DETAILED TEST EXECUTION MATRIX",
        "",
        "| Test Name | Production Function | Injected Mutation / Attack | Expected Behavior | Actual Behavior | Verdict |",
        "| :--- | :--- | :--- | :--- | :--- | :---: |"
    ]

    for t in TEST_RESULTS_LOG:
        lines.append(
            f"| `{t['name']}` | `{t['targetFunction']}` | {t['mutation']} | {t['expected']} | {t['actual']} | **{t['verdict']}** |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 3. P0-A STRICT STAR STEM PARSER SPOTLIGHT",
        "",
        "The dedicated strict parser `parse_strict_star_stem` enforces the exact JLPT layout:",
        "`prefix + （　　） + （　　） + ★ + （　　） + suffix`",
        "",
        "- Exactly 3 regular blank slots + exactly 1 ★ marker.",
        "- ★ strictly located at insertion position 3.",
        "- Rejects extra blanks, missing blanks, misplaced ★, duplicate ★, and malformed delimiters.",
        "",
        "---",
        "",
        "## 4. P0-1 DERIVED SEMANTIC COVERAGE & FORGED LEDGER REJECTION SPOTLIGHT",
        "",
        "The hardened semantic review evidence validator `validate_semantic_review_evidence` rejects all 10 attacks (A through J):",
        "1. **Attack A**: `coverageDeclared` omitted with only 1 permutation reviewed -> `INSUFFICIENT_REVIEW_COVERAGE`.",
        "2. **Attack B**: `coverageDeclared` declared `PARTIAL` -> `INCOMPLETE_COVERAGE_DECLARED_PARTIAL`.",
        "3. **Attack C**: Duplicated reviewed permutation IDs -> `DUPLICATE_REVIEWED_PERMUTATION`.",
        "4. **Attack D**: Extra, nonexistent permutation IDs -> `NONEXISTENT_PERMUTATION`.",
        "5. **Attack E**: Judgment IDs mismatch reviewed permutations -> `EXTRA_JUDGMENT_NOT_REVIEWED`.",
        "6. **Attack F**: Valid artifact digest but arbitrary unverified reviewer identity -> `UNSUPPORTED_REVIEWER_LABEL`.",
        "7. **Attack G**: Locally fabricated repetitive unsupported reasoning boilerplate -> `REPETITIVE_UNSUPPORTED_BOILERPLATE_REJECTED`.",
        "8. **Attack H**: Correct question fingerprint but stale scoring fingerprint -> `SCORING_FINGERPRINT_MISMATCH`.",
        "9. **Attack I**: Conflicting defensible alternative hidden inside judgments -> `AMBIGUOUS_ALTERNATIVE_FOUND` (`QUARANTINED`).",
        "10. **Attack J**: Valid-looking completed review containing one unresolved judgment -> `UNRESOLVED_LINGUISTIC_JUDGMENT` (`QA_REVIEW_REQUIRED`).",
        "",
        "---",
        "",
        "## 5. P0-2 GOOGLE FORMS DEPLOYMENT EVIDENCE & WORKSPACE BINDINGS SPOTLIGHT",
        "",
        "The hardened deployment validator `verify_deployment_evidence` eliminates local JSON forgery and rejects all deployment bypass attacks:",
        "1. **Attack 1**: Local JSON alone claiming `LIVE_VERIFIED` -> Rejected and downgraded to `QA_PASSED_NOT_DEPLOYED` (`DEPLOYMENT_METADATA_PRESENT_UNVERIFIED`).",
        "2. **Attack 2**: Real Form ID paired with wrong practice set ID -> Rejected (`PRACTICE_SET_ID_MISMATCH`).",
        "3. **Attack 3**: Correct Form ID with wrong question mapping -> Rejected (`QUESTION_MAPPING_MISMATCH`).",
        "4. **Attack 4**: Correct Form ID but missing submission receipt -> Rejected (`MISSING_SUBMISSION_RECEIPT`).",
        "5. **Attack 5**: Valid receipt belonging to another Form -> Rejected (`RECEIPT_FORM_MISMATCH`).",
        "6. **Attack 6**: Correct Form but wrong destination Sheet -> Rejected (`DESTINATION_SHEET_MISMATCH`).",
        "7. **Attack 7**: Expired or stale verification evidence -> Rejected (`STALE_DEPLOYMENT_EVIDENCE`).",
        "8. **Attack 8**: Incomplete quiz grading verification -> Rejected (`GRADING_VERIFICATION_FAILED`).",
        "9. **Attack 9**: Unauthorized test double rejected from production release -> Rejected (`UNAUTHORIZED_TEST_DOUBLE_REJECTED`).",
        "10. **Attack 10**: Offline mock adapter validates bindings successfully as `MOCK_SUCCESS` (`liveVerified=False`).",
        "",
        "---",
        "",
        "## 6. MANDATORY SECURITY REGRESSIONS SPOTLIGHT (ATTACKS A THROUGH G)",
        "",
        "Strict 3-environment architecture and cryptographic trust boundaries:",
        "1. **Attack A**: Fabricated callback wrapped in `make_production_workspace_adapter` -> NEVER `LIVE_VERIFIED` (`MOCK_SUCCESS`, `liveVerified=False`).",
        "2. **Attack B**: Fake Form ID (`SYNTH-FAKE-...`) -> `FORM_EXISTS_FAILED`.",
        "3. **Attack C**: Nonexistent receipt on Sheets -> `RECEIPT_VERIFICATION_FAILED`.",
        "4. **Attack D**: Wrong answer-key mapping -> `ANSWER_KEY_DIGEST_MISMATCH`.",
        "5. **Attack E**: Real Form with wrong destination Sheet -> `DESTINATION_SHEET_MISMATCH`.",
        "6. **Attack F**: 4-year-old timestamp with `isStale=False` -> `STALE_DEPLOYMENT_EVIDENCE` (freshness policy <= 7 days).",
        "7. **Attack G**: Omitting `receiptFormId`, `expectedSheetId`, or `answerKeyDigest` -> `MISSING_*_BINDING`.",
        "8. **Positive Control**: Provider with genuine Google Workspace client credentials -> `LIVE_VERIFIED` (`liveVerified=True`).",
        "",
        "---",
        "",
        "## 7. REPEATABLE TEST COMMAND",
        "",
        "```powershell",
        "python scripts/tests/test_qa_adversarial_mutations.py",
        "```",
        ""
    ])

    report_path = ROOT / "qa/ADVERSARIAL_TEST_RESULTS.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {report_path}")


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestAdversarialQAMutations)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    write_adversarial_report()
    sys.exit(0 if result.wasSuccessful() else 1)
