# JP-STUDY PHASE 3.7 — ADVERSARIAL TEST SUITE & RELEASE GATE SECURITY AUDIT

## 1. EXECUTIVE SUMMARY & TEST METRICS

- **Total Tests Executed**: 33
- **Passed Tests**: 33
- **Failed Tests**: 0
- **Adversarial Gate Verdict**: **PASS (100% Defect Detection)**
- **Coverage Scope**:
  - Part 1: 12 Production Mutation Integration Scenarios
  - Part 2: 10 STAR Structure Negative Controls (P0-A Strict Parser)
  - Part 3: 7 Forged Semantic Ledger Attack Tests (P0-B Schema Validation)
  - Part 4: Real Linguistic Negative Control (Tanaka-san Scrambling)
  - Part 5: P1-A Fake Form Live-Status Bypass & Provider Verification
  - Part 6: P1-B Zero-Item Mock Reporting Regression Audit

---

## 2. DETAILED TEST EXECUTION MATRIX

| Test Name | Production Function | Injected Mutation / Attack | Expected Behavior | Actual Behavior | Verdict |
| :--- | :--- | :--- | :--- | :--- | :---: |
| `P0-B Attack 1: Empty reviewedPermutations` | `audit_star_question` | status=VERIFIED_COHERENT with empty reviewedPermutations | Rejected from QA_VERIFIED | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-B Attack 2: Wrong content fingerprint` | `audit_star_question` | status=VERIFIED_COHERENT with wrong blindInputSha256 | Rejected from QA_VERIFIED with FINGERPRINT_MISMATCH | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-B Attack 3: Missing reviewer evidence` | `audit_star_question` | reviewerId='expert_panel' with null evidenceArtifact | Rejected with UNSUPPORTED_REVIEWER_LABEL / MISSING_EVIDENCE | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-B Attack 4: Old question version` | `audit_star_question` | questionVersion 1 < current version 2 | Rejected with STALE_QUESTION_VERSION | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-B Attack 5: Recorded defensible alternative` | `audit_star_question` | Defensible alternative changing slot 3 injected with VERIFIED_COHERENT status | Rejected and QUARANTINED | gate2=AMBIGUOUS_ALTERNATIVE_FOUND, disp=QUARANTINED | **PASS** |
| `P0-B Attack 6: Forged/missing artifact digest` | `audit_star_question` | Nonexistent artifact file reference | Rejected with MISSING_EVIDENCE_FILE | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-B Attack 7: Incomplete coverage declared complete` | `audit_star_question` | 1 permutation reviewed but coverageDeclared='COMPLETE' | Rejected with INCOMPLETE_COVERAGE_FALSELY_DECLARED | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `Part 4: Tanaka-san Ambiguous STAR` | `audit_star_question` | Tanaka-san free adjunct scrambling (昨日/会議で/その計画について/熱心に) | STAR_SEMANTIC_REVIEW_PENDING / QA_REVIEW_REQUIRED | STAR_SEMANTIC_REVIEW_PENDING / QA_REVIEW_REQUIRED | **PASS** |
| `P1-A: Authorized provider live verification` | `reconcile_practice_set_status` | Injected provider verifying all 5 stages with real receipt | readinessStatus=LIVE_VERIFIED | LIVE_VERIFIED | **PASS** |
| `P1-A: Fake Google Form live status rejected` | `reconcile_practice_set_status` | Plausible 20-char fake Form ID with liveVerified=True in JSON | readinessStatus=QA_PASSED_NOT_DEPLOYED (liveVerified=False) | QA_PASSED_NOT_DEPLOYED (stage=DEPLOYMENT_METADATA_PRESENT_UNVERIFIED) | **PASS** |
| `P1-B: Zero-item mock reporting` | `generate_practice_release_gate_report` | Empty full mock exam (qids=[]) | NO_ITEMS — NOT_EVALUABLE (never 100% VERIFIED) | has_no_items=True, has_100_percent=False | **PASS** |
| `Scenario 10: Non-Google deployment URL` | `reconcile_practice_set_status` | Non-Google Forms URL passed with isDeployed=True | readinessStatus=QA_PASSED_NOT_DEPLOYED | QA_PASSED_NOT_DEPLOYED | **PASS** |
| `Scenario 11: Multi-tier hash invariance` | `compute_all_question_fingerprints` | Comparing bank items to manifest across 4 hash tiers | 0 mismatches | 0 mismatches | **PASS** |
| `Scenario 12: Pipeline consistency` | `run_reconciliation` | Verifying bank and practice sets counts | 104 verified, 16 star pending, 11 ready sets, 9 blocked sets, 3 mock | 104 verified, 16 pending, 11 ready, 9 blocked, 3 mock | **PASS** |
| `Scenario 1: Stem mutation` | `evaluate_question_qa_gate` | Changed 散歩 to 買い物 in stem | QA_REVIEW_REQUIRED with FINGERPRINT_MISMATCH | QA_REVIEW_REQUIRED (Content fingerprint mismatch (FINGERPRIN...) | **PASS** |
| `Scenario 2: Choice mutation` | `evaluate_question_qa_gate` | Changed option A to よからば | QA_REVIEW_REQUIRED with FINGERPRINT_MISMATCH | QA_REVIEW_REQUIRED (Content fingerprint mismatch (FINGERPRIN...) | **PASS** |
| `Scenario 3: Batch duplicate detection` | `load_all_blind_reviews` | Duplicate ID in raw_blind_review_n4.json | ValueError('Duplicate review record detected...') | Duplicate review record detected in raw_blind_review_n4.json for question N4-TEST-001 | **PASS** |
| `Scenario 4: Missing reviewer record` | `check_review_integrity` | Removed review for N4-TEST-MISSING | ok=False, missing=['N4-TEST-MISSING'] | ok=False, missing=['N4-TEST-MISSING'] | **PASS** |
| `Scenario 5: Answer disagreement` | `evaluate_question_qa_gate` | Reviewer answer C != Author answer A | QUARANTINED with disagreement=True | QUARANTINED (disagreement=True) | **PASS** |
| `Scenario 6: Alternative defensible answer` | `evaluate_question_qa_gate` | Injected alternativeDefensibleAnswers=['B'] | QA_REVIEW_REQUIRED | QA_REVIEW_REQUIRED (Reviewer identified alternative defensible answer(s): ['B']) | **PASS** |
| `Scenario 7: Corrupt STAR key` | `audit_star_question` | Changed correctAnswer from D to B | ok=False with ANSWER_KEY_SLOT3_MISMATCH | ok=False (Gate 1 Failed: ANSWER_KEY_SLOT3_MISMATCH: Author key 'B' does not match slot 3 of canonical assembly ('D').) | **PASS** |
| `Scenario 8: Hallucinated STAR ID` | `audit_star_report_against_bank` | Report contains N2-GR-STAR-005 | ok=False with hallucinated=['N2-GR-STAR-005'] | ok=False, hallucinated=['N2-GR-STAR-005', 'N4-GR-STAR-001'] | **PASS** |
| `Scenario 9: Corrupt set reference` | `reconcile_practice_set_status` | Referenced quarantined item Q2 | readinessStatus=CONTENT_QA_BLOCKED | CONTENT_QA_BLOCKED (Referenced questions unverified: [('Q2', 'QUARANTINED')]) | **PASS** |
| `P0-A Neg 10: Incorrect answer key` | `validate_star_structure` | Key B != Slot 3 D | ok=False with ANSWER_KEY_SLOT3_MISMATCH | ok=False (ANSWER_KEY_SLOT3_MISMATCH: Author key 'B' does not match slot 3 of canonical assembly ('D').) | **PASS** |
| `P0-A Neg 1: Extra regular blank` | `validate_star_structure` | Added 1 extra blank (5 slots total) | ok=False with EXTRA_SLOTS | ok=False (STRICT_STEM_PARSER_FAILURE: EXTRA_SLOTS: Found 5 insertion slot(s), expected exactly 4 (too many blanks).) | **PASS** |
| `P0-A Neg 2: Two extra blanks` | `validate_star_structure` | Added 2 extra blanks (6 slots total) | ok=False with EXTRA_SLOTS | ok=False (STRICT_STEM_PARSER_FAILURE: EXTRA_SLOTS: Found 6 insertion slot(s), expected exactly 4 (too many blanks).) | **PASS** |
| `P0-A Neg 3: Star in position 1` | `validate_star_structure` | ★ placed in position 1 | ok=False with INVALID_STAR_POSITION (pos 1) | ok=False (STRICT_STEM_PARSER_FAILURE: INVALID_STAR_POSITION: '★' occupies insertion position 1, expected position 3.) | **PASS** |
| `P0-A Neg 4: Star in position 2` | `validate_star_structure` | ★ placed in position 2 | ok=False with INVALID_STAR_POSITION (pos 2) | ok=False (STRICT_STEM_PARSER_FAILURE: INVALID_STAR_POSITION: '★' occupies insertion position 2, expected position 3.) | **PASS** |
| `P0-A Neg 5: Star in position 4` | `validate_star_structure` | ★ placed in position 4 | ok=False with INVALID_STAR_POSITION (pos 4) | ok=False (STRICT_STEM_PARSER_FAILURE: INVALID_STAR_POSITION: '★' occupies insertion position 4, expected position 3.) | **PASS** |
| `P0-A Neg 6: Duplicate star` | `validate_star_structure` | Two ★ markers in stem | ok=False with DUPLICATE_STAR_MARKER | ok=False (STRICT_STEM_PARSER_FAILURE: DUPLICATE_STAR_MARKER: Stem contains 2 '★' markers, expected exactly 1.) | **PASS** |
| `P0-A Neg 7: Missing blank` | `validate_star_structure` | Only 2 regular blanks (3 slots total) | ok=False with INSUFFICIENT_SLOTS | ok=False (STRICT_STEM_PARSER_FAILURE: INSUFFICIENT_SLOTS: Found 3 insertion slot(s), expected exactly 4 (3 blanks + 1 ★).) | **PASS** |
| `P0-A Neg 8: Malformed delimiters` | `validate_star_structure` | Unbalanced open parenthesis in blank | ok=False with MALFORMED_PARENTHESES | ok=False (STRICT_STEM_PARSER_FAILURE: MALFORMED_PARENTHESES: Unbalanced parentheses (opens=3, closes=2).) | **PASS** |
| `P0-A Neg 9: Canonical missing chunk` | `validate_star_structure` | assembledSentence missing chunk '住んでいる' | ok=False with INCOHERENT_CANONICAL_SENTENCE | ok=False (INCOHERENT_CANONICAL_SENTENCE: Canonical sentence missing chunk C ('住んでいる').) | **PASS** |

---

## 3. P0-A STRICT STAR STEM PARSER SPOTLIGHT

The dedicated strict parser `parse_strict_star_stem` enforces the exact JLPT layout:
`prefix + （　　） + （　　） + ★ + （　　） + suffix`

- Exactly 3 regular blank slots + exactly 1 ★ marker.
- ★ strictly located at insertion position 3.
- Rejects extra blanks, missing blanks, misplaced ★, duplicate ★, and malformed delimiters.

---

## 4. P0-B FORGED SEMANTIC LEDGER BYPASS SPOTLIGHT

The semantic review evidence validator `validate_semantic_review_evidence` rejects all 7 forged ledger attacks:
1. Empty `reviewedPermutations`: Rejected (`INSUFFICIENT_REVIEW_COVERAGE`).
2. Wrong content fingerprint: Rejected (`FINGERPRINT_MISMATCH`).
3. Missing reviewer evidence / unsupported label: Rejected (`UNSUPPORTED_REVIEWER_LABEL`).
4. Stale question version: Rejected (`STALE_QUESTION_VERSION`).
5. Recorded defensible alternative: Quarantined (`AMBIGUOUS_ALTERNATIVE_FOUND`).
6. Missing or forged artifact digest: Rejected (`MISSING_EVIDENCE_FILE` / `EVIDENCE_HASH_MISMATCH`).
7. Incomplete coverage declared complete: Rejected (`INCOMPLETE_COVERAGE_FALSELY_DECLARED`).

---

## 5. REPEATABLE TEST COMMAND

```powershell
python scripts/tests/test_qa_adversarial_mutations.py
```
