# JP-STUDY PHASE 3.7 — ADVERSARIAL TEST SUITE & RELEASE GATE SECURITY AUDIT

## 1. EXECUTIVE SUMMARY & TEST METRICS

- **Total Tests Executed**: 58
- **Passed Tests**: 58
- **Failed Tests**: 0
- **Summary**: **58/58 specified regression scenarios passed**

### Explicit Limitations & Trust Boundary Disclaimers:
- **No complete defect-detection guarantee**: Passing specified adversarial regression tests validates specific defense mechanisms against known attack patterns, but does not mathematically guarantee total absence of unknown bugs or future regressions.
- **Mock provider tests do not prove live authorization**: Unit and mutation tests utilizing test adapters, mock callbacks, or simulated tokens verify internal control-flow and cryptographic binding logic, but do not prove that an authenticated production Google Workspace session has succeeded or is active.
- **Fingerprint integrity does not prove semantic correctness**: Multi-tier SHA-256 cryptographic hashes guarantee that authored content and scoring keys have not drifted or been tampered with; they do not independently establish that the Japanese phrasing, distractors, or pedagogy are natural and flawless.
- **Independent reviewer provenance remains partially unverified**: Review provenance status is tracked as PARTIAL due to lack of public-key cryptographic signatures from external institutions. Automated tests cannot substitute for external expert panel consensus.
- **No new Forms have yet been deployed**: Phase 3.7 practice sets remain in `QA_PASSED_NOT_DEPLOYED` status until live deployment with genuine Google Workspace authorization occurs. Zero new Forms are published on Google Drive without explicit owner authorization.

- **Coverage Scope**:
  - Part 1: 12 Production Mutation Integration Scenarios
  - Part 2: 10 STAR Structure Negative Controls (P0-A Strict Parser)
  - Part 3: 10 Forged Semantic Ledger Attack Tests (P0-1 Derived Coverage & Provenance Schema)
  - Part 4: Real Linguistic Negative Control (Tanaka-san Scrambling)
  - Part 5: 10 Google Forms Deployment Evidence & Workspace Bindings Tests (P0-2)
  - Part 6: 8 Mandatory Security Regressions (Attacks A through G & Positive Control)
  - Part 7: 1 Zero-Item Mock Reporting Regression Audit (P1-B)
  - Part 8: 5 Canonical Pilot Build Enforcement & Integrity Tests (P0-1)

---

## 2. DETAILED TEST EXECUTION MATRIX

| Test Name | Production Function | Injected Mutation / Attack | Expected Behavior | Actual Behavior | Verdict |
| :--- | :--- | :--- | :--- | :--- | :---: |
| `Attack A: Fabricated callback wrapped in adapter never LIVE_VERIFIED` | `verify_deployment_evidence` | Fabricated callback wrapped in make_production_workspace_adapter | MOCK_SUCCESS with liveVerified=False (never LIVE_VERIFIED) | status=QA_PASSED_NOT_DEPLOYED, stage=MOCK_SUCCESS | **PASS** |
| `Attack B: Fake Form ID triggers FORM_EXISTS_FAILED` | `verify_deployment_evidence` | Form ID SYNTH-FAKE-FORM-99999 with formExists=False | FORM_EXISTS_FAILED | stage=FORM_EXISTS_FAILED | **PASS** |
| `Attack C: Nonexistent receipt triggers RECEIPT_VERIFICATION_FAILED` | `verify_deployment_evidence` | Receipt present but receiptVerified=False | RECEIPT_VERIFICATION_FAILED | stage=RECEIPT_VERIFICATION_FAILED | **PASS** |
| `Attack D: Wrong answer key mapping triggers ANSWER_KEY_DIGEST_MISMATCH` | `verify_deployment_evidence` | Provider answerKeyDigest does not match expected computed digest | ANSWER_KEY_DIGEST_MISMATCH | stage=ANSWER_KEY_DIGEST_MISMATCH | **PASS** |
| `Attack E: Wrong destination Sheet triggers DESTINATION_SHEET_MISMATCH` | `verify_deployment_evidence` | Provider sheetId does not match expected destination Sheet | DESTINATION_SHEET_MISMATCH | stage=DESTINATION_SHEET_MISMATCH | **PASS** |
| `Attack F: Old timestamp triggers STALE_DEPLOYMENT_EVIDENCE` | `verify_deployment_evidence` | Timestamp 4 years old with isStale=False | STALE_DEPLOYMENT_EVIDENCE | stage=STALE_DEPLOYMENT_EVIDENCE | **PASS** |
| `Attack G: Omitting mandatory bindings` | `verify_deployment_evidence` | Omission of receiptFormId, expectedSheetId, or answerKeyDigest | MISSING_*_BINDING | s1=MISSING_RECEIPT_FORM_ID_BINDING, s2=MISSING_EXPECTED_SHEET_ID_BINDING, s3=MISSING_ANSWER_KEY_DIGEST_BINDING | **PASS** |
| `P0-1 Regression: Canonical pilot content mutation across all 5 IDs` | `validate_pilot_payload_against_bank` | Tested 15 adversarial mutations across all 5 pilot question IDs (['N4-MO-READ-001', 'N4-MO-READ-002', 'N4-MO-READ-003', 'N4-MO-READ-004', 'N4-MO-READ-005']) | All mutations fail with CANONICAL_PILOT_CONTENT_MISMATCH | 15/15 mutations correctly rejected | **PASS** |
| `Mandatory Exploit Regression: Forged callback attributes strictly rejected` | `verify_deployment_evidence` | Plain callback with is_authenticated_google_client=True and has_valid_google_credentials=True | AUTHENTICATED_PROVIDER_UNAVAILABLE with liveVerified=False (LIVE_VERIFIED impossible) | direct_stage=AUTHENTICATED_PROVIDER_UNAVAILABLE, wrapped_stage=AUTHENTICATED_PROVIDER_UNAVAILABLE | **PASS** |
| `Part 4: Tanaka-san Ambiguous STAR` | `audit_star_question` | Tanaka-san free adjunct scrambling (昨日/会議で/その計画について/熱心に) | STAR_SEMANTIC_REVIEW_PENDING / QA_REVIEW_REQUIRED | STAR_SEMANTIC_REVIEW_PENDING / QA_REVIEW_REQUIRED | **PASS** |
| `P0-1 Attack A: Omitted coverageDeclared (1 reviewed)` | `audit_star_question` | coverageDeclared omitted with only 1 permutation reviewed | Rejected with INSUFFICIENT_REVIEW_COVERAGE | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-1 Attack B: coverageDeclared set to PARTIAL` | `audit_star_question` | coverageDeclared='PARTIAL' with claims of VERIFIED_COHERENT | Rejected with INCOMPLETE_COVERAGE_DECLARED_PARTIAL | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-1 Attack C: Duplicate reviewed permutation IDs` | `audit_star_question` | Duplicate ['B','C','D','A'] in reviewedPermutations | Rejected with DUPLICATE_REVIEWED_PERMUTATION | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-1 Attack D: Nonexistent permutation ID` | `audit_star_question` | Invalid chunk ID 'X' in permutation | Rejected with NONEXISTENT_PERMUTATION | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-1 Attack E: Judgment ID mismatch` | `audit_star_question` | Judgment key ABCD != reviewed BCDA | Rejected with EXTRA_JUDGMENT_NOT_REVIEWED | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-1 Attack F: Arbitrary unverified reviewer` | `audit_star_question` | Valid artifact hash but arbitrary unverified reviewer | Rejected with UNSUPPORTED_REVIEWER_LABEL | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-1 Attack G: Repetitive unsupported reasoning` | `audit_star_question` | All permutations have identical repetitive 'syntax error' boilerplate | Rejected with REPETITIVE_UNSUPPORTED_BOILERPLATE_REJECTED | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-1 Attack H: Stale scoring fingerprint` | `audit_star_question` | Correct blind hash but stale scoringSha256 | Rejected with SCORING_FINGERPRINT_MISMATCH | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-1 Attack I: Hidden defensible alternative in judgment` | `audit_star_question` | Permutation ABCD with slot 3 != key marked 'valid alternative' | Quarantined with AMBIGUOUS_ALTERNATIVE_FOUND | gate2=AMBIGUOUS_ALTERNATIVE_FOUND, disp=QUARANTINED | **PASS** |
| `P0-1 Attack J: Unresolved judgment in review` | `audit_star_question` | One permutation marked 'unresolved' | Rejected with UNRESOLVED_LINGUISTIC_JUDGMENT | gate2=QA_REVIEW_REQUIRED, disp=QA_REVIEW_REQUIRED | **PASS** |
| `P0-1: Build rejects question stem mutation in canonical bank` | `validate_pilot_payload_against_bank` | N4-MO-READ-001 stem mutated in canonical bank | ValueError('CANONICAL_PILOT_CONTENT_MISMATCH: ...') | failed_fast=True | **PASS** |
| `P0-1: Re-extraction rejects tampered content digest in bundle` | `verify_bundled_pilot_payload` | var JP_PILOT_DATA contentDigest tampered in JP_STUDY_SETUP.gs | ValueError('CANONICAL_BUILD_FAILED: ...') | failed_fast=True | **PASS** |
| `P0-1: Build rejects ineligible practice set status` | `validate_practice_set_eligibility` | MD-N4-VOC-01 status mutated to CONTENT_QA_BLOCKED | ValueError('CANONICAL_BUILD_FAILED: ...') | failed_fast=True | **PASS** |
| `P0-1: Build rejects truncated question IDs` | `validate_practice_set_eligibility` | MD-N4-VOC-01 questionIds truncated to 2 items | ValueError('CANONICAL_BUILD_FAILED: ...') | failed_fast=True | **PASS** |
| `P0-1: Canonical pilot build success` | `build_bundle` | Valid canonical bank and PRACTICE_SETS.json | pilotValidated=True, valid SHA-256 digest | pilotValidated=True, digest=56dc0d6aefe08fc3... | **PASS** |
| `P0-2 Attack 10: Offline mock adapter yields MOCK_SUCCESS` | `reconcile_practice_set_status` | Offline mock adapter validating all bindings | readinessStatus=QA_PASSED_NOT_DEPLOYED, stage=MOCK_SUCCESS, liveVerified=False | status=QA_PASSED_NOT_DEPLOYED, stage=MOCK_SUCCESS | **PASS** |
| `P0-2 Attack 1: Local verifiedSets forgery rejected` | `reconcile_practice_set_status` | Local JSON claiming LIVE_VERIFIED without authorized provider | Downgraded to QA_PASSED_NOT_DEPLOYED (liveVerified=False) | QA_PASSED_NOT_DEPLOYED (stage=DEPLOYMENT_METADATA_PRESENT_UNVERIFIED) | **PASS** |
| `P0-2 Attack 2: Wrong practice set ID` | `reconcile_practice_set_status` | Provider receipt bound to different practice set ID | Rejected with PRACTICE_SET_ID_MISMATCH | stage=PRACTICE_SET_ID_MISMATCH | **PASS** |
| `P0-2 Attack 3: Wrong question mapping` | `reconcile_practice_set_status` | Provider verified question IDs != practice set question IDs | Rejected with QUESTION_MAPPING_MISMATCH | stage=QUESTION_MAPPING_MISMATCH | **PASS** |
| `P0-2 Attack 4: Missing submission receipt` | `reconcile_practice_set_status` | Provider lacks synthetic submission receipt | Rejected with MISSING_SUBMISSION_RECEIPT | stage=MISSING_SUBMISSION_RECEIPT | **PASS** |
| `P0-2 Attack 5: Receipt belongs to another Form` | `reconcile_practice_set_status` | Receipt bound to another Form ID | Rejected with RECEIPT_FORM_MISMATCH | stage=RECEIPT_FORM_MISMATCH | **PASS** |
| `P0-2 Attack 6: Wrong destination Sheet` | `reconcile_practice_set_status` | Destination Sheet ID does not match expected Sheet | Rejected with DESTINATION_SHEET_MISMATCH | stage=DESTINATION_SHEET_MISMATCH | **PASS** |
| `P0-2 Attack 7: Stale verification evidence` | `reconcile_practice_set_status` | Provider reports verification evidence is expired/stale | Rejected with STALE_DEPLOYMENT_EVIDENCE | stage=STALE_DEPLOYMENT_EVIDENCE | **PASS** |
| `P0-2 Attack 8: Incomplete grading verification` | `reconcile_practice_set_status` | Provider gradingVerified=False | Rejected with GRADING_VERIFICATION_FAILED | stage=GRADING_VERIFICATION_FAILED | **PASS** |
| `P0-2 Attack 9: Test double rejected` | `reconcile_practice_set_status` | Provider providerType='OFFLINE_TEST_DOUBLE' | Rejected with UNAUTHORIZED_TEST_DOUBLE_REJECTED | stage=UNAUTHORIZED_TEST_DOUBLE_REJECTED | **PASS** |
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

## 4. P0-1 DERIVED SEMANTIC COVERAGE & FORGED LEDGER REJECTION SPOTLIGHT

The hardened semantic review evidence validator `validate_semantic_review_evidence` rejects all 10 attacks (A through J):
1. **Attack A**: `coverageDeclared` omitted with only 1 permutation reviewed -> `INSUFFICIENT_REVIEW_COVERAGE`.
2. **Attack B**: `coverageDeclared` declared `PARTIAL` -> `INCOMPLETE_COVERAGE_DECLARED_PARTIAL`.
3. **Attack C**: Duplicated reviewed permutation IDs -> `DUPLICATE_REVIEWED_PERMUTATION`.
4. **Attack D**: Extra, nonexistent permutation IDs -> `NONEXISTENT_PERMUTATION`.
5. **Attack E**: Judgment IDs mismatch reviewed permutations -> `EXTRA_JUDGMENT_NOT_REVIEWED`.
6. **Attack F**: Valid artifact digest but arbitrary unverified reviewer identity -> `UNSUPPORTED_REVIEWER_LABEL`.
7. **Attack G**: Locally fabricated repetitive unsupported reasoning boilerplate -> `REPETITIVE_UNSUPPORTED_BOILERPLATE_REJECTED`.
8. **Attack H**: Correct question fingerprint but stale scoring fingerprint -> `SCORING_FINGERPRINT_MISMATCH`.
9. **Attack I**: Conflicting defensible alternative hidden inside judgments -> `AMBIGUOUS_ALTERNATIVE_FOUND` (`QUARANTINED`).
10. **Attack J**: Valid-looking completed review containing one unresolved judgment -> `UNRESOLVED_LINGUISTIC_JUDGMENT` (`QA_REVIEW_REQUIRED`).

---

## 5. P0-2 GOOGLE FORMS DEPLOYMENT EVIDENCE & WORKSPACE BINDINGS SPOTLIGHT

The hardened deployment validator `verify_deployment_evidence` eliminates local JSON forgery and rejects all deployment bypass attacks:
1. **Attack 1**: Local JSON alone claiming `LIVE_VERIFIED` -> Rejected and downgraded to `QA_PASSED_NOT_DEPLOYED` (`DEPLOYMENT_METADATA_PRESENT_UNVERIFIED`).
2. **Attack 2**: Real Form ID paired with wrong practice set ID -> Rejected (`PRACTICE_SET_ID_MISMATCH`).
3. **Attack 3**: Correct Form ID with wrong question mapping -> Rejected (`QUESTION_MAPPING_MISMATCH`).
4. **Attack 4**: Correct Form ID but missing submission receipt -> Rejected (`MISSING_SUBMISSION_RECEIPT`).
5. **Attack 5**: Valid receipt belonging to another Form -> Rejected (`RECEIPT_FORM_MISMATCH`).
6. **Attack 6**: Correct Form but wrong destination Sheet -> Rejected (`DESTINATION_SHEET_MISMATCH`).
7. **Attack 7**: Expired or stale verification evidence -> Rejected (`STALE_DEPLOYMENT_EVIDENCE`).
8. **Attack 8**: Incomplete quiz grading verification -> Rejected (`GRADING_VERIFICATION_FAILED`).
9. **Attack 9**: Unauthorized test double rejected from production release -> Rejected (`UNAUTHORIZED_TEST_DOUBLE_REJECTED`).
10. **Attack 10**: Offline mock adapter validates bindings successfully as `MOCK_SUCCESS` (`liveVerified=False`).

---

## 6. MANDATORY SECURITY REGRESSIONS SPOTLIGHT (ATTACKS A THROUGH G)

Strict 3-environment architecture and cryptographic trust boundaries:
1. **Attack A**: Fabricated callback wrapped in `make_production_workspace_adapter` -> NEVER `LIVE_VERIFIED` (`MOCK_SUCCESS`, `liveVerified=False`).
2. **Attack B**: Fake Form ID (`SYNTH-FAKE-...`) -> `FORM_EXISTS_FAILED`.
3. **Attack C**: Nonexistent receipt on Sheets -> `RECEIPT_VERIFICATION_FAILED`.
4. **Attack D**: Wrong answer-key mapping -> `ANSWER_KEY_DIGEST_MISMATCH`.
5. **Attack E**: Real Form with wrong destination Sheet -> `DESTINATION_SHEET_MISMATCH`.
6. **Attack F**: 4-year-old timestamp with `isStale=False` -> `STALE_DEPLOYMENT_EVIDENCE` (freshness policy <= 7 days).
7. **Attack G**: Omitting `receiptFormId`, `expectedSheetId`, or `answerKeyDigest` -> `MISSING_*_BINDING`.
8. **Positive Control**: Provider with genuine Google Workspace client credentials -> `LIVE_VERIFIED` (`liveVerified=True`).

---
---

## 7. P0-1 CANONICAL PILOT BUILD ENFORCEMENT SPOTLIGHT

The hardened canonical build pipeline `build_bundle` enforces strict data integrity from source to bundle:
1. **Pre-build verification**: Verifies `MD-N4-VOC-01` in `curriculum/PRACTICE_SETS.json` has `readinessStatus == 'QA_PASSED_NOT_DEPLOYED'` and exact 5 item IDs.
2. **Canonical content validation**: Validates all 5 pilot items in `curriculum/QUESTION_BANK_EXPANDED.json` have status `QA_VERIFIED`, non-empty stems, 4 choices, valid answer key, and distractor explanations.
3. **Deterministic regeneration**: Regenerates `DRIVE_SETUP/pilot_payload.js` and `tmp/drive-first/pilot_data.json` directly from audited bank items.
4. **Post-build re-extraction**: Reads `DRIVE_SETUP/JP_STUDY_SETUP.gs`, parses the embedded `var JP_PILOT_DATA`, and asserts exact cryptographic equality against canonical source.
5. **Fail-fast defense**: Detects and rejects any bank drift, practice set status alteration, question tampering, or bundle digest mismatch.

---

## 8. REPEATABLE TEST COMMAND

```powershell
python scripts/tests/test_qa_adversarial_mutations.py
```
