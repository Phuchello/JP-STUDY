# JP-STUDY PHASE 3.7 — ADVERSARIAL TEST SUITE & NEGATIVE CONTROLS AUDIT

## 1. EXECUTIVE SUMMARY & TEST METRICS

- **Total Tests Executed**: 19
- **Passed Tests**: 19
- **Failed Tests**: 0
- **Adversarial Gate Verdict**: **PASS (100% Defect Detection)**
- **Coverage**: 12 Production Mutation Integration Scenarios + 7 STAR Negative Controls.

---

## 2. DETAILED TEST EXECUTION MATRIX

| Test Name | Production Function | Injected Mutation / Corruption | Expected Behavior | Actual Behavior | Verdict |
| :--- | :--- | :--- | :--- | :--- | :---: |
| `Negative Control 13: Synthetic Ambiguous STAR` | `audit_star_question` | Tanaka-san free adjunct scrambling (昨日/会議で/その計画について/熱心に) | STAR_SEMANTIC_REVIEW_PENDING / QA_REVIEW_REQUIRED | STAR_SEMANTIC_REVIEW_PENDING / QA_REVIEW_REQUIRED | **PASS** |
| `Negative Control 14: Missing canonical assembly` | `validate_star_structure` | assembledSentence = '' | ok=False with MISSING_CANONICAL_SENTENCE | ok=False (MISSING_CANONICAL_SENTENCE: Question is missing the 'assembledSentence' reference.) | **PASS** |
| `Negative Control 15: Wrong answer key` | `validate_star_structure` | Author key A != Slot 3 D | ok=False with ANSWER_KEY_SLOT3_MISMATCH | ok=False (ANSWER_KEY_SLOT3_MISMATCH: Author key 'A' does not match slot 3 of canonical assembly ('D').) | **PASS** |
| `Negative Control 16: Duplicate chunk usage` | `validate_star_structure` | Option A and C both have '会いに' | ok=False with DUPLICATE_CHUNKS | ok=False (DUPLICATE_CHUNKS: Options contain duplicate text strings.) | **PASS** |
| `Negative Control 17: Invalid slot count` | `validate_star_structure` | 3 options instead of 4 | ok=False with INVALID_SLOT_COUNT | ok=False (INVALID_SLOT_COUNT: Question has 3 options, expected exactly 4.) | **PASS** |
| `Negative Control 18: Particle collision` | `check_generic_structural_constraints` | Chunk junction creates 'をを' | is_valid=False with Double case-particle collision | is_valid=False (STRUCTURAL_REJECT: Double case-particle collision 'をを' detected across chunk boundary.) | **PASS** |
| `Negative Control 19: Unknown question ID` | `audit_star_question` | Question ID not in any database or ledger | Handles gracefully without crash; gate1=PASS, gate2=PENDING | gate1=PASS, gate2=STAR_SEMANTIC_REVIEW_PENDING | **PASS** |
| `Scenario 10: Fake deployment URL` | `reconcile_practice_set_status` | Non-Google Forms URL passed with isDeployed=True | readinessStatus=QA_PASSED_NOT_DEPLOYED | QA_PASSED_NOT_DEPLOYED | **PASS** |
| `Scenario 11: Multi-tier hash invariance` | `compute_all_question_fingerprints` | Comparing bank items to manifest across 4 hash tiers | 0 mismatches | 0 mismatches | **PASS** |
| `Scenario 12: Pipeline consistency` | `run_reconciliation` | Verifying bank and practice sets counts | 104 verified, 16 star pending, 11 ready sets, 9 blocked sets, 3 mock | 104 verified, 16 pending, 11 ready, 9 blocked, 3 mock | **PASS** |
| `Scenario 1: Stem mutation` | `evaluate_question_qa_gate` | Changed 散歩 to 買い物 in stem | QA_REVIEW_REQUIRED with FINGERPRINT_MISMATCH | QA_REVIEW_REQUIRED (Content fingerprint mismatch (...) | **PASS** |
| `Scenario 2: Choice mutation` | `evaluate_question_qa_gate` | Changed option A to よからば | QA_REVIEW_REQUIRED with FINGERPRINT_MISMATCH | QA_REVIEW_REQUIRED (Content fingerprint mismatch (...) | **PASS** |
| `Scenario 3: Batch duplicate detection` | `load_all_blind_reviews` | Duplicate ID in raw_blind_review_n4.json | ValueError('Duplicate review record detected...') | Duplicate review record detected in raw_blind_review_n4.json for question N4-TEST-001 | **PASS** |
| `Scenario 4: Missing reviewer record` | `check_review_integrity` | Removed review for N4-TEST-MISSING | ok=False, missing=['N4-TEST-MISSING'] | ok=False, missing=['N4-TEST-MISSING'] | **PASS** |
| `Scenario 5: Answer disagreement` | `evaluate_question_qa_gate` | Reviewer answer C != Author answer A | QUARANTINED with disagreement=True | QUARANTINED (disagreement=True) | **PASS** |
| `Scenario 6: Alternative defensible answer` | `evaluate_question_qa_gate` | Injected alternativeDefensibleAnswers=['B'] | QA_REVIEW_REQUIRED | QA_REVIEW_REQUIRED (Reviewer identified alternative defensible answer(s): ['B']) | **PASS** |
| `Scenario 7: Corrupt STAR key` | `audit_star_question` | Changed correctAnswer from D to B | ok=False with ANSWER_KEY_SLOT3_MISMATCH | ok=False (Gate 1 Failed: ANSWER_KEY_SLOT3_MISMATCH: Author key 'B' does not match slot 3 of canonical assembly ('D').) | **PASS** |
| `Scenario 8: Hallucinated STAR ID` | `audit_star_report_against_bank` | Report contains N2-GR-STAR-005 | ok=False with hallucinated=['N2-GR-STAR-005'] | ok=False, hallucinated=['N2-GR-STAR-005'] | **PASS** |
| `Scenario 9: Corrupt set reference` | `reconcile_practice_set_status` | Referenced quarantined item Q2 | readinessStatus=CONTENT_QA_BLOCKED | CONTENT_QA_BLOCKED (Referenced questions unverified: [('Q2', 'QUARANTINED')]) | **PASS** |

---

## 3. REAL NEGATIVE-CONTROL SPOTLIGHT: SYNTHETIC AMBIGUOUS STAR

### Linguistic Specification of Negative Control 13
- **Japanese Stem**: `田中さんは（　　）（　　） ★ （　　）話しました。`
- **Options**:
  - `A`: `昨日` (temporal adverbial adjunct)
  - `B`: `会議で` (locative postpositional adjunct)
  - `C`: `その計画について` (topical/prepositional adjunct)
  - `D`: `熱心に` (manner adverb)
- **Linguistic Analysis**:
  - In Japanese syntax, free adverbial adjuncts before the verb phrase can scramble without altering core propositional semantics.
  - **Arrangement 1**: `田中さんは 昨日(A) 会議で(B) ★ その計画について(C) 熱心に(D) 話しました。` -> Slot 3 = `C`.
  - **Arrangement 2**: `田中さんは 昨日(A) その計画について(C) ★ 会議で(B) 熱心に(D) 話しました。` -> Slot 3 = `B`.
- **Audit Verdict**: Both arrangements are 100% natural, grammatically flawless Japanese. The production two-gate auditor successfully **refuses to self-certify** the question as coherent, returning `STAR_SEMANTIC_REVIEW_PENDING` and holding the item as `QA_REVIEW_REQUIRED`.

---

## 4. REPEATABLE TEST COMMAND

```powershell
python scripts/tests/test_qa_adversarial_mutations.py
```
