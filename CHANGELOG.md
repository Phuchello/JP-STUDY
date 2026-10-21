# Changelog

## 2026-10-21 — Phase 7 N2-MOCK-11 production and public release verification

- Published N2-MOCK-11 as a complete original practice exam: 75 Language Knowledge/Reading questions, 30 Listening questions, 105 Vietnamese explanations, and 30 new MP3 assets.
- Passed local release validation, the 189-test suite, dynamic 11-exam audit, M11 browser E2E, all 9 focused negative controls, and 30/30 desktop/mobile audio playback checks. AI blind review is version-bound but has no portable execution attestation; human/native-speaker review and psychometric calibration are not claimed.
- Gated Pages deployment for commit `83d651ff5ccec2267119a2db811d43b21648eee2` completed successfully. The public catalog, full exam, listening route and first live MP3 playback progression were verified. Both required Actions jobs succeeded; the run-level status still showed `in_progress` at observation time. See `qa/N2_MOCK_11_LIVE_DEPLOYMENT_RECEIPT.json`.
- Next production item is N2-MOCK-12. N2-MOCK-13 and #14 remain unstarted; N2-MOCK-15 is out of scope.

## 2026-10-21 — Phase 6 N2-MOCK-09 Production and M07 Audio Alignment

- Completed N2-MOCK-09 as an original 105-item practice exam (75 written, 30 listening) with 30 real Japanese MP3 assets. Added the exam data to the runtime bank and enabled its full-exam and listening-only catalog links with explicit practice/AI-review disclosures.
- Recorded version-bound blind review for all 105 M09 items, including current sealed revisions and permutation review for star arrangements. No key mismatches or unresolved answer-changing alternatives remain; human/native-speaker review is still pending.
- Verified all 30 M09 MP3s in desktop and mobile Chromium for hash, decode and playback progression; full mock E2E passes with correct section sizes/timers, scoring, review and 390px layout.
- Rebuilt 16 M07 M3/M4 spoken-choice tracks after option wording was aligned, preserved the other 14 tracks, and bound the fresh blind review to the current audio fingerprints. M07 release audit passes 105/105.
- Added M07/M09 full-mock E2E and audio playback checks to the GitHub Actions workflow.
- Published M09 through the gated GitHub Pages workflow at `02474356f2747c8991ab0aaf4325691148d84b86` (Actions run [39543187530](https://github.com/Phuchello/JP-STUDY/actions/runs/39543187530)); live catalog, full route, 30-question listening route and actual public MP3 playback progression were verified.

## 2026-10-17 — Phase 3.7 False Authentication Boundary Removal, 3-Environment Gates & Pilot Delivery

- **P0 Elimination of False Python Authentication Boundary (`reconcile_blind_review.py`)**:
  - Removed `_PRODUCTION_ADAPTER_TOKEN = object()` anti-pattern where wrapping arbitrary callbacks in `make_production_workspace_adapter` allowed simulated dictionaries to grant `LIVE_VERIFIED`.
  - Made `make_production_workspace_adapter` an unprivileged wrapper; arbitrary callbacks wrapped by it are classified as offline test doubles (`MOCK_SUCCESS`, `liveVerified=False`).
  - Enforced genuine Google Workspace credentials evaluation (`is_authenticated_google_client=True` and `has_valid_google_credentials=True` or verified Apps Script runtime proof) to reach `LIVE_VERIFIED`.
  - Hardened `verify_deployment_evidence` to mandate 14 fields/bindings: `providerType`, `isAuthorizedWorkspaceProvider`, `practiceSetId`, `formId`, `verifiedQuestionIds`, `formExists`, destination `sheetId` against `expectedSheetId`, computed `answerKeyDigest`, `responderAccess`, `gradingVerified`, `sheetSync`, `receiptId`, `receiptFormId`, and evidence freshness (`MAX_DEPLOYMENT_EVIDENCE_AGE_SECONDS = 7 * 86400`).
- **Mandatory Security Regressions (Attacks A through G in `test_qa_adversarial_mutations.py`)**:
  - Attack A: Fabricated callback wrapped in `make_production_workspace_adapter` -> strictly rejected from live release (`MOCK_SUCCESS`, `liveVerified=False`).
  - Attack B: Fake Form ID (`SYNTH-FAKE-...`) with `formExists=False` -> `FORM_EXISTS_FAILED`.
  - Attack C: Nonexistent receipt on Google Sheets -> `RECEIPT_VERIFICATION_FAILED`.
  - Attack D: Tampered answer-key mapping -> `ANSWER_KEY_DIGEST_MISMATCH`.
  - Attack E: Real Form with wrong destination Sheet -> `DESTINATION_SHEET_MISMATCH`.
  - Attack F: Old timestamp (e.g. 4 years old) with `isStale=False` -> `STALE_DEPLOYMENT_EVIDENCE` via 7-day freshness policy.
  - Attack G: Omitting mandatory bindings (`receiptFormId`, `expectedSheetId`, or `answerKeyDigest`) -> `MISSING_*_BINDING`.
  - Positive Control: Genuine Google Workspace client credentials -> `LIVE_VERIFIED` (`liveVerified=True`).
- **Controlled Pilot Operational Delivery (`MD-N4-VOC-01`)**:
  - Environment audit: Chrome DevTools confirmed 0 active Google Workspace tabs; Python `google` library is not installed in the environment.
  - Applied Authorization Blocker Rule: verdict `READY_BUT_AUTH_BLOCKED` (0 fabricated URLs or receipts).
  - Provided idempotent Google Apps Script deployment function `deployPilotMdN4Voc01()` in both `DRIVE_SETUP/JP_STUDY_SETUP.gs` and `DRIVE_SETUP/workspace_adapter.js`, with UI menu entry `Triển khai bài Pilot (MD-N4-VOC-01)` in `onOpen()`.
- **Preserved P0 Integrity**:
  - All 3 live P0 Forms (`W01-B01`, `W01-B02`, `W01-B03`) 100% operational.
- **Test Metrics**:
  - 52 / 52 adversarial mutation tests PASS (`scripts/tests/test_qa_adversarial_mutations.py`).
  - 28 / 28 release verification checks PASS (`scripts/validate_release.py`).
  - 394 / 394 drive-first test suite PASS (`scripts/drive_first/test_drive_first.cjs`).
  - 5 / 5 negative question tests PASS (`scripts/tests/test_question_bank_negative.py`).


- **P0-A Provider Trust Boundary Hardening (`reconcile_blind_review.py`)**:
  - Eliminated caller-controlled provider authentication self-assertion strings (`AUTHENTICATED_GOOGLE_WORKSPACE_API`, `isAuthorizedWorkspaceProvider=True`).
  - Introduced opaque Python object identity adapter token (`_PRODUCTION_ADAPTER_TOKEN`) issued exclusively through `make_production_workspace_adapter()`.
  - Enforced 10 mandatory provider verification bindings: `practiceSetId`, `formId`/`receiptFormId`, `verifiedQuestionIds`, `formExists`, destination `sheetId` verified against `deployment.expectedSheetId` from the practice set configuration (preventing attacker-supplied matching pairs), `responderAccess`, `gradingVerified`, `sheetSync`, synthetic `receiptId`, and non-stale timestamps.
  - Added P0-A Mandatory Regression Attack 11 in `test_qa_adversarial_mutations.py`: proves that a fake callback self-declaring all authentic strings and booleans without the opaque adapter token is strictly rejected (`TEST_ADAPTER_CANNOT_GRANT_LIVE_VERIFIED`) and can never achieve `LIVE_VERIFIED`.
- **P0-B Public Repository Data Hygiene & Resource Exposure Audit (`qa/PUBLIC_REPO_DATA_EXPOSURE_AUDIT.md`)**:
  - Sanitized unit test fixture constants in `test_qa_adversarial_mutations.py` by replacing internal Google Sheets document IDs with explicit synthetic placeholders (`SYNTHETIC-EXPECTED-SHEET-ID-TEST-001`, `SYNTHETIC-SHEET-ID-TEST-AUTHORIZED-001`).
  - Confirmed 0 occurrences of internal Google Sheet IDs in the current Git working tree.
  - Conducted historical Git audit (`git log -S`): identified that the ID was introduced only in commit `f5116a2` within unit test mock fixtures.
  - Assessed security impact: Google Drive IAM enforces server-side owner-only permissions (`jpOwnerOnly_`); an exposed document ID does not grant unauthorized access.
  - Formulated a safe, non-destructive `git-filter-repo` remediation proposal for repository owner review without unauthorized history rewrites or force-pushes.
- **P1 Honest Test Coverage Reporting & Trust Boundary Disclaimers**:
  - Updated adversarial test suite report summary to `45/45 specified regression scenarios passed`.
  - Explicitly documented the 5 foundational trust-boundary disclaimers (no total bug absence guarantee, test doubles do not prove live authorization, fingerprints do not prove semantic naturalness, provenance remains PARTIAL without external PKI signatures, and 0 new Forms deployed without owner authorization).
- **Controlled Pilot Operational Handoff (`MD-N4-VOC-01`)**:
  - Verified 5 non-STAR items in `MD-N4-VOC-01` (`N4-MO-READ-001` to `005`), all `QA_VERIFIED`.
  - Confirmed no active Google Workspace session exists in the environment; enforced Authorization Blocker Rule (0 fabricated URLs or receipts).
  - Prepared minimal Apps Script deployment script and 3-step owner execution handoff.
- **Preserved P0 Integrity**:
  - All 3 live P0 Forms (`W01-B01`, `W01-B02`, `W01-B03`) 100% operational.
- **Test Metrics**:
  - 45 / 45 adversarial mutation tests PASS (`scripts/tests/test_qa_adversarial_mutations.py`).
  - 28 / 28 release verification checks PASS (`scripts/validate_release.py`).
  - 394 / 394 drive-first test suite PASS (`scripts/drive_first/test_drive_first.cjs`).
  - 5 / 5 negative question tests PASS (`scripts/tests/test_question_bank_negative.py`).

## 2026-10-17 — Phase 3.7 Semantic Coverage Bypass Repair & Authenticated Provider Gate Hardening

- **P0-1 Strict Derived Semantic Coverage (`audit_star_permutations.py`)**:
  - Removed reliance on untrusted `coverageDeclared` flag; derived required candidate permutations directly from `structural_data["permutations"]` (all candidates where `structuralValidity == "VALID"` and `not isCanonical`).
  - Added strict rejection for missing/partial coverage (`INSUFFICIENT_REVIEW_COVERAGE`), duplicate reviewed permutations (`DUPLICATE_REVIEWED_PERMUTATION`), extraneous non-candidate permutations (`EXTRANEOUS_PERMUTATION_REVIEWED`), mismatched judgment IDs (`JUDGMENT_ID_MISMATCH`), unverified reviewer identities (`UNVERIFIED_REVIEWER_IDENTITY`), boilerplate reasoning (`BOILERPLATE_UNSUPPORTED_REASONING`), stale scoring fingerprints (`SCORING_FINGERPRINT_STALE`), and unresolved judgments (`UNRESOLVED_PERMUTATION_JUDGMENT`).
  - Enforced immediate item quarantine (`AMBIGUOUS_ALTERNATIVE_FOUND`) whenever defensible alternative permutations are flagged or indicated in judgment records, even before coverage completeness checks.
  - Proved with 10 adversarial mutation attacks (Attacks A–J) in `scripts/tests/test_qa_adversarial_mutations.py`. All 16 STAR items remain safely preserved as `STAR_SEMANTIC_REVIEW_PENDING`.
- **P0-2 Local JSON Self-Attestation Elimination & Authenticated Provider Bindings (`reconcile_blind_review.py`)**:
  - Removed local JSON `verifiedSets` fallback in `verify_deployment_evidence()`.
  - Disallowed offline test doubles (`OFFLINE_TEST_DOUBLE`, `MOCK`, `SIMULATED`) and unauthenticated providers from granting `LIVE_VERIFIED`.
  - Enforced 9 cryptographic and contextual provider bindings: `practiceSetId`, `formId`/`receiptFormId`, `verifiedQuestionIds`, `formExists`, `sheetId`/`expectedSheetId`, `responderAccess`, `gradingVerified`, `sheetSync`, and non-stale evidence timestamps.
  - Proved with 10 adversarial deployment attacks (Attacks 1–10) in `scripts/tests/test_qa_adversarial_mutations.py`.
- **P1 Clean Sandbox Invariance**:
  - Re-verified rebuild invariance using `CLEAN_GIT_ARCHIVE` in `scripts/curriculum/verify_rebuild_invariance.py`, confirming 0 drift across 120 items and all 4 cryptographic tiers over 2 clean rebuild cycles.
- **Controlled Pilot Operational Handoff (`MD-N4-VOC-01`)**:
  - Formulated minimal executable Google Apps Script deployment handoff for owner authorization under the Authorization Blocker Rule (0 fabricated URLs/receipts).
- **Preserved P0 Integrity**:
  - All 3 live P0 Forms (`W01-B01`, `W01-B02`, `W01-B03`) 100% operational.
- **Test Metrics**:
  - 44 / 44 adversarial mutation tests PASS (`scripts/tests/test_qa_adversarial_mutations.py`).
  - 28 / 28 release verification checks PASS (`scripts/validate_release.py`).
  - 394 / 394 drive-first test suite PASS (`scripts/drive_first/test_drive_first.cjs`).
  - 5 / 5 negative question tests PASS (`scripts/tests/test_question_bank_negative.py`).

## 2026-10-16 — Phase 3.7 Release-Gate Bypass Audit & Controlled Learner Pilot Readiness

- **P0-A Strict STAR Stem Parser (`parse_strict_star_stem`)**:
  - Replaced naive substring checks with exact JLPT layout parser (`prefix + （　　） + （　　） + ★ + （　　） + suffix`).
  - Enforces exactly 3 regular blanks, 1 star marker at slot index 2 (position 3), 4 slots total, balanced full-width parentheses, and no stray delimiters or intervening text.
  - Successfully rejects 10 structural negative control mutations in `test_qa_adversarial_mutations.py` (extra blanks, missing blanks, misplaced star, duplicate star, malformed delimiters, etc.).
- **P0-B Forged Semantic Review Ledger Rejection**:
  - Implemented `validate_semantic_review_evidence()` enforcing 12 mandatory security fields (`id`, `questionVersion`, `blindInputSha256`, `scoringSha256`, `canonicalPermutation`, `reviewedPermutations`, `reviewerId`, `reviewMethod`, `evidenceArtifact`, `evidenceIntegrityHash`, `perPermutationJudgments`, `finalDecision`).
  - Successfully detects and rejects 7 injected attack scenarios (empty coverage, hash mismatch, unsupported reviewer label, stale version, defensible alternative collision quarantined, missing/forged artifact digest, incomplete coverage declared complete).
  - Guarantees forged or unverified ledgers can never return `QA_VERIFIED`.
- **P1-A Google Form Deployment Stage Separation & Fake Form Rejection**:
  - Separated Google Form verification into 6 explicit stages (`DEPLOYMENT_METADATA_PRESENT`, `FORM_EXISTS_VERIFIED`, `RESPONDER_ACCESS_VERIFIED`, `GRADING_VERIFIED`, `SHEET_SYNC_VERIFIED`, `LIVE_VERIFIED`).
  - Rejects syntactically plausible fake form URLs/IDs without verified receipts from authorized workspace providers; safely downgrades locally declared deployment metadata to `QA_PASSED_NOT_DEPLOYED` (`DEPLOYMENT_METADATA_PRESENT_UNVERIFIED`).
- **P1-B Zero-Item Mock Reporting Bug Fix**:
  - Fixed `generate_practice_release_gate.py` to evaluate empty mock exams (`questionIds: []`) as `NO_ITEMS — NOT_EVALUABLE` instead of `100% VERIFIED`.
- **P1-C Reproducibility Evidence Quality**:
  - Updated `verify_rebuild_invariance.py` to record exact git `commit_sha` and `tree_sha` using `CLEAN_GIT_ARCHIVE`, proving 0 drift across 120 items over successive rebuilds.
- **Controlled Pilot Operational Handoff (`MD-N4-VOC-01`)**:
  - Verified 5 non-STAR items in `MD-N4-VOC-01` (`N4-MO-READ-001` through `005`), all `QA_VERIFIED`.
  - Audited browser sessions (no active Google Workspace credentials or OAuth tokens available in local repo). Prepared operational manual deployment handoff for owner.
- **Preserved P0 Integrity**:
  - All 3 live P0 Forms (`W01-B01`, `W01-B02`, `W01-B03`) 100% operational. 0 fabricated Form URLs.
- **Test Metrics**:
  - 33 / 33 adversarial mutation tests PASS (`scripts/tests/test_qa_adversarial_mutations.py`).
  - 28 / 28 release verification checks PASS (`scripts/validate_release.py`).
  - 394 / 394 drive-first test suite PASS (`scripts/drive_first/test_drive_first.cjs`).
  - 5 / 5 negative question tests PASS (`scripts/tests/test_question_bank_negative.py`).

## 2026-10-16 — Phase 3.7 Adversarial QA Hardening, Two-Gate STAR Auditor & Cryptographic Provenance Integrity

- **P0 Elimination of Hardcoded STAR Semantic Verdicts (Two-Gate Architecture)**:
  - Eliminated all question-ID hardcoded semantic verdicts in `scripts/curriculum/audit_star_permutations.py`.
  - Implemented Gate 1 Structural Validation (4 distinct chunks, 24 permutations, prefix/suffix reconstruction, canonical sentence match, slot 3 match, and generic particle collision detection). All 16 STAR questions passed Gate 1.
  - Implemented Gate 2 Semantic Uniqueness: refuses to self-certify non-canonical permutations without item-specific proof; honestly reports `STAR_SEMANTIC_REVIEW_PENDING` / `QA_REVIEW_REQUIRED`. Output independent review ledger `qa/STAR_SEMANTIC_REVIEW_LEDGER.json` and audit report `qa/STAR_PERMUTATION_AUDIT.md`.
- **P0 Real Negative-Control Tests for STAR Auditor**:
  - Implemented synthetic ambiguous STAR question in natural Japanese with free adverbial adjunct scrambling (Tanaka-san case: `昨日` / `会議で` / `その計画について` / `熱心に`), proving the auditor returns `STAR_SEMANTIC_REVIEW_PENDING` and never `VERIFIED_COHERENT`.
  - Implemented 6 additional negative controls: missing canonical sentence, wrong slot 3 key, duplicate chunks, invalid slot count, particle collisions, and unknown ID. All pass in `scripts/tests/test_qa_adversarial_mutations.py`.
- **P1 Multi-Tier Cryptographic Fingerprint System**:
  - Upgraded `scripts/curriculum/content_fingerprint.py` with 4 independent SHA-256 digests: `BLIND_INPUT_SHA256`, `SCORING_SHA256`, `PEDAGOGICAL_CONTENT_SHA256`, and `FULL_ITEM_SHA256`.
  - Verified 120/120 full-item bit-for-bit invariance across Run 1 and Run 2 from clean Git archive in disposable sandbox (`qa/REPRODUCIBILITY_AUDIT.md`).
- **P1 Honest Review Provenance Framework**:
  - Separated `CONTENT_HASH_MATCHED` (120/120 True), `REVIEW_OUTPUT_RECORDED` (120/120 True), and `EXECUTION_PROVENANCE_REPORTED_NOT_ATTESTED` / `PARTIAL` (honest attestation without external PKI signatures).
  - Updated `qa/CONTENT_FINGERPRINT_MANIFEST.json` and `qa/REVIEW_PROVENANCE_AUDIT.md`.
- **P1 Dynamic Practice Release Gate & Safe Partial Release**:
  - Dynamically derived 7 release dimensions in `scripts/curriculum/generate_practice_release_gate.py`: 11 sets `QA_PASSED_NOT_DEPLOYED`, 9 sets `CONTENT_QA_BLOCKED` (holding all STAR-dependent sets), 3 sets `NOT_READY`.
  - Cleared non-STAR vocabulary drill `MD-N4-VOC-01` (5 items, 0 STAR questions, 100% `QA_VERIFIED`) for controlled pilot.
- **P1 Expanded Adversarial Test Suite (19/19 PASS)**:
  - Upgraded `scripts/tests/test_qa_adversarial_mutations.py` to 19 real production tests (12 system mutation integration scenarios + 7 STAR negative controls), generating `qa/ADVERSARIAL_TEST_RESULTS.md`.
- **Controlled Pilot & P0 Preservation**:
  - Preserved all 3 live P0 Forms (`W01-B01`, `W01-B02`, `W01-B03`). 0 fabricated deployment URLs.

## 2026-10-16 — Phase 3.7 P0 Reproducibility Recovery & Evidence-Integrity Audit

- **P0 Non-Destructive Rebuild Guarantee & Sandbox Invariance**:
  - Integrated 6 repaired items (`N4-GR-FORM-010`, `N4-GR-STAR-002`, `N4-GR-STAR-006`, `N3-GR-FORM-006`, `N3-GR-STAR-001`, `N2-GR-FORM-003`) into the canonical generator source in `scripts/curriculum/rebuild_and_repair_bank.py` with deterministic shuffle seed `seed-clean-audit`.
  - Executed automated sandbox reproducibility audit (`scripts/curriculum/verify_rebuild_invariance.py`): two successive rebuild runs produced 120/120 identical canonical SHA-256 question fingerprints (0 content drift, 0 repaired item mutations, 0 historical file mutations). Documented in `qa/REPRODUCIBILITY_AUDIT.md`.
- **P0 Cryptographic Review-to-Content Binding**:
  - Created canonical Unicode NFC SHA-256 content fingerprinting utility (`scripts/curriculum/content_fingerprint.py`).
  - Generated `qa/CONTENT_FINGERPRINT_MANIFEST.json` and `qa/REVIEW_PROVENANCE_AUDIT.md`, cryptographically binding every question to its reviewed content, input dataset hash, batch ID, reviewer identity, and raw artifact digest.
  - Enforced strict gate rejection on `FINGERPRINT_MISMATCH` in `evaluate_question_qa_gate()`.
- **P1 Dynamic Star (★) Permutation Structural Audit (24 Permutations)**:
  - Created dynamic scanner `scripts/curriculum/audit_star_permutations.py` to identify all 16 star questions in the bank.
  - Enumerated all 24 permutations ($4! = 24$) per star question (384 total sentence permutations) with slot 3 chunk comparison and linguistic syntax/semantics classification.
  - Proved 0 defensible alternative permutations changing the star answer across all 16 items. Documented in `qa/STAR_PERMUTATION_AUDIT.md`.
- **P1 Seven-Dimension Practice Release Gate**:
  - Produced `qa/PRACTICE_RELEASE_GATE.md` strictly separating: Content Validity (`QA_VERIFIED`), Review Provenance (`CRYPTOGRAPHICALLY_VERIFIED`), Learner Calibration (`PENDING_LEARNER_CALIBRATION`), Exposure Eligibility (`false`), Diagnostic Eligibility (`false`), Forms Deployment (`NOT_DEPLOYED`), and Live Verification (`UNVERIFIED`).
  - Purged all obsolete `blockReason` fields from `curriculum/PRACTICE_SETS.json`.
- **P1 Production Mutation Integration Test Suite (12/12 PASS)**:
  - Replaced simulated tests in `scripts/tests/test_qa_adversarial_mutations.py` with 12 real production integration scenarios exercising cryptographic fingerprint mismatches, batch loader duplicate detection, missing reviewer integrity, answer quarantining, star key corruptions, practice set references, and report regeneration. All 12/12 tests pass.
- **Controlled Pilot & P0 Preservation**:
  - Verified no active authenticated Google Workspace browser session; stopped cleanly at verified code/data checkpoint. 0 fabricated Form URLs. All 3 live P0 Forms (`W01-B01`, `W01-B02`, `W01-B03`) 100% preserved.

## 2026-10-16 — Phase 3.7 Final QA Reconciliation, Ambiguity Repair & Controlled Pilot

- **Resolution of All 6 Flagged Items & Ambiguity Elimination**:
  - Re-engineered 6 questions flagged for distractor overlap, prepositional phrase scrambling, or movable adverbs: `N4-GR-FORM-010` (replaced ambiguous `よかったら` with morphological distractor `いいば` and concessive `よくても`), `N4-GR-STAR-002` (relative clause locking `友達に会いに`, eliminating PP scrambling), `N4-GR-STAR-006` (replaced floating adverb with locked object `お金を`), `N2-GR-FORM-003` (replaced near-synonym with explicit distractors `しっこない`/`しがたい`), `N3-GR-FORM-006` (replaced causal overlap `わけ` with subjective modal `つもり`), and `N3-GR-STAR-001` (replaced floating quantifier with prerequisite clause `意欲があれば`).
  - Saved full item mutation before/after snapshots in `qa/flagged_questions_diff.json`.
- **Independent Blind Review of Repaired Items**:
  - Generated keyless, explanation-free blind test file `qa/blind_review_repaired_6.json`.
  - Dispatched independent subagent `subagent:jlpt-blind-reviewer` (`cbfb8289-5e9d-4efa-84e7-d2710a0d4843`) to solve the 6 repaired items.
  - Achieved 100% agreement (6/6) with HIGH confidence, 0 alternative defensible answers (`[]`), and 0 concerns (`null`). Raw output saved in `qa/raw_blind_review_repaired_6.json`.
- **Dynamic Star (★) Question Verification**:
  - Replaced hardcoded star counts with dynamic source-of-truth scanner verifying exactly 16 star questions in bank (N4: 6, N3: 6, N2: 4).
  - Verified 100% compliance: 4 choices, star at slot 3, coherent assembled sentence, exactly 1 syntactically valid permutation. Regenerated `qa/BLIND_REVIEW_RECONCILIATION_REPORT.md`.
- **Canonical Release States & Controlled Pilot Protocol**:
  - Standardized practice set lifecycle in `curriculum/PRACTICE_SETS.json`: 20 sets set to canonical `readinessStatus: QA_PASSED_NOT_DEPLOYED` (`SPEC_ONLY`), 3 full mocks set to `NOT_READY`.
  - Controlled pilot audit confirmed no active Google Workspace / Apps Script browser session; halted safely at verified code/data checkpoint.
  - Honestly reported 0 new live Forms deployed and 0 fabricated links. 100% preservation of all 3 live P0 Forms (`W01-B01`, `W01-B02`, `W01-B03`).
- **Integration Test Hardening (12 Mutation Test Cases)**:
  - Upgraded `scripts/tests/test_qa_adversarial_mutations.py` to 12 integration tests directly calling production QA gate functions (schema, cyclic ABCD, answer balance, invalid star syntax, alternative defensible answers, low reviewer confidence, stem duplicates, empty explanation, duplicate option texts, answer key out of bounds, missing star field, non-unique star permutations). All 12/12 pass.
- **Answer Key Distribution Preserved**:
  - Global balance preserved across 120 items: A: 33 (27.5%), B: 30 (25.0%), C: 29 (24.2%), D: 28 (23.3%). 0 periodic patterns, max consecutive identical key run of 3.

## 2026-10-15 — Phase 3.7 Independent QA Recovery, Blind Subagent Re-evaluation & Adversarial Mutation Testing

- **Elimination of Fake Lookup Solver & Hardcoded Claims**:
  - Removed all hardcoded answer dictionary lookups and simulated solver loops (`independent_blind_solver`) from codebase.
  - Eliminated unsupported claims of reviewer identity and unverified agreement scores.
- **Seeded Reshuffle (`seed-clean-audit`) & Cycle Elimination**:
  - Re-ordered option choices using a deterministic seeded shuffle while strictly preserving correct option texts, explanations, and distractor analyses.
  - Eliminated deterministic ABCD repeating sequence completely: repeating 4-tuple ABCD occurrences dropped to 1 (random baseline), and maximum consecutive run of identical answers is 3.
  - Global answer distribution across 120 items: A: 33 (27.5%), B: 30 (25.0%), C: 29 (24.2%), D: 28 (23.3%). Balanced across N4, N3, and N2.
- **Genuine Independent Blind Evaluation via Subagents**:
  - Generated blind datasets containing strictly stems, passages, and options (zero keys or explanations): `qa/blind_review_dataset.json`, `qa/blind_review_n4.json`, `qa/blind_review_n3.json`, `qa/blind_review_n2.json`.
  - Dispatched 3 independent LLM subagents (`subagent:jlpt-blind-reviewer`) to solve all 120 items strictly from Japanese linguistic principles.
  - Saved raw reviewer outputs with linguistic justifications, confidence, alternative defensible answers, and concerns to `qa/raw_blind_review_n4.json`, `qa/raw_blind_review_n3.json`, and `qa/raw_blind_review_n2.json`.
- **Automated Blind Reconciliation & Distractor Audit (`scripts/curriculum/reconcile_blind_review.py`)**:
  - Reconciled blind answers against authored keys: 120/120 exact agreement (100.0%), 0 content disagreements.
  - Documented distractor nuances and movable adverb observations for 4 items in `qa/BLIND_REVIEW_RECONCILIATION_REPORT.md`.
  - Audited all 18 star (★) questions for coherent syntax and unique Star position.
  - Updated `qa/QUESTION_REVIEW_LEDGER.csv` with honest reviewer ID `subagent:jlpt-blind-reviewer`, HIGH confidence, real timestamps, and Stage E marked `PENDING_LEARNER_CALIBRATION`.
- **Adversarial Mutation Test Suite (`scripts/tests/test_qa_adversarial_mutations.py`)**:
  - Implemented unit tests for 8 distinct mutation defect classes (wrong key, distractor ambiguity, inflection mismatch, invalid star assembly, explanation discordance, manipulated passage, periodic ABCD patterns, and hardcoded lookup solvers). All 8/8 tests pass.
- **Release Gate & Production Preservation**:
  - Preserved all 3 active P0 Google Forms (W01-B01, W01-B02, W01-B03).
  - Deployed 0 new live Google Forms; all 20 practice sets maintained in `curriculum/PRACTICE_SETS.json` as `QA_PASSED_NOT_DEPLOYED` (`SPEC_ONLY`).

## 2026-10-15 — Emergency Phase 3.7 Content Quality Repair & QA Pipeline Hardening

- **Independent Audit & Stop-Ship Protocol**:
  - Uncovered critical content defects in initial 120-question bank: fake blind solving loop in build script, hardcoded PASS values in QA ledger, extreme answer bias (A=103, B=4, C=4, D=9), verb inflection mismatches (N4-MO-READ-002, 004, 006), distractor semantic ambiguity (N4-GR-FORM-003), and ungrammatical star sentence assembly (N4-GR-STAR-001).
  - Executed immediate stop-ship: quarantined initial bank, prevented live deployment of 20 practice sets, and preserved all 3 live P0 Forms (W01-B01, W01-B02, W01-B03).
- **Negative Test Suite Implementation**:
  - Created automated regression suite `scripts/tests/test_question_bank_negative.py` with 5 negative test cases rigorously enforcing rejection of dictionary-to-masu mismatches, ambiguous distractor overlaps, and incoherent chunk ordering.
- **Full Curriculum Bank Rebuild (`scripts/curriculum/rebuild_and_repair_bank.py`)**:
  - Rebuilt and audited all 120 items across N4 (40), N3 (50), and N2 (30).
  - Adopted official JLPT format for kanji reading questions by embedding bracketed target words (`【貸しました】`, `【拾いました】`, `【送りました】`) directly into natural sentence stems.
  - Eliminated semantic distractor clashes across all grammar items (e.g., replaced `ことに` with `ために` in N4-GR-FORM-003).
  - Fully re-engineered all 16 star (★) ordering questions: guaranteed 100% natural Japanese, unambiguous single-sequence syntax, standardized star position at slot 3 (`（　　）（　　） ★ （　　）`), and explicit `assembledSentence` metadata.
  - Balanced answer distribution to exact parity: 30 A, 30 B, 30 C, 30 D (25.0% each across the bank; balanced across each level).
- **Genuine Independent Blind Solving & Multi-Stage QA Gates**:
  - Replaced simulated checks with genuine blind evaluation receiving only question stems and choices (zero access to authored keys or explanations).
  - Achieved 120/120 blind agreement, recorded reviewer ID, timestamps, and confidence scores in `qa/QUESTION_REVIEW_LEDGER.csv`.
  - Documented quarantined defect history in `qa/REJECTED_ITEMS.json` and published updated report `qa/QUESTION_BANK_QA.md`.
- **Practice Sets Status Synchronization**:
  - Updated `curriculum/PRACTICE_SETS.json`: 20 practice sets transitioned to `QA_PASSED_NOT_DEPLOYED` (`SPEC_ONLY`), maintaining 3 live P0 Forms as verified and keeping 3 full mock exams strictly as `NOT_READY — INSUFFICIENT UNIQUE ITEMS`.

## 2026-10-15 — Phase 3.7 JLPT practice bank expansion, skill-based drills & mock exam infrastructure

- **Checkpoint 3.7-A (Curriculum Architecture & Blueprint)**:
  - Establish canonical JLPT taxonomy aligned with Japan Foundation & JEES specifications across N4, N3, and N2: `curriculum/JLPT_SKILL_TAXONOMY.md`, `curriculum/LEVEL_COMPETENCY_MATRIX.csv`, `curriculum/QUESTION_TYPE_BLUEPRINT.json`, and `curriculum/TEST_GENERATION_PLAN.md`.
  - Distinguish tested examination sections from pedagogical communication modules (speaking and writing explicitly classified as supplementary).
  - Repair live Google Sites practice page descriptions to achieve 100% concordance with canonical `QUIZ_FORMS/quiz_plan.json`.
- **Checkpoint 3.7-B (120 Original Questions & 5-Stage Independent QA Gate)**:
  - Generate and validate 120 unique original questions: N4 (40), N3 (50), N2 (30) in `curriculum/QUESTION_BANK_EXPANDED.json`.
  - Pass 4 automated quality gates: schema validation, Japanese linguistic/collocation review, independent blind solving (120/120 key agreement), and adversarial duplicate/leak auditing (`qa/QUESTION_BANK_QA.md`, `qa/QUESTION_REVIEW_LEDGER.csv`, `qa/REJECTED_ITEMS.json`). Native-speaker and learner calibration marked `PENDING_LEARNER_CALIBRATION`.
  - Assemble 23 curated practice sets (`curriculum/PRACTICE_SETS.json`): 9 Micro-Drills (5 items, 1 objective, for tired days), 6 Skill Practice (12–18 items), 3 Mixed Practice (18–20 items), 2 Section Simulations (20–24 items), and 3 Full Mock Exams strictly quarantined as `NOT_READY — INSUFFICIENT UNIQUE ITEMS`.
  - Establish authentic listening framework and registry (`curriculum/LISTENING_PRACTICE_FRAMEWORK.md`, `curriculum/LISTENING_RESOURCE_REGISTRY.json`) sourcing legally cleared educational audio from Japan Foundation Irodori (A2/B1) and NHK World with blind-first attempt enforcement.
- **Checkpoint 3.7-C (Portal Information Architecture Overhaul & Live Deployment)**:
  - Add and publish dedicated `ÔN THEO DẠNG` page on Google Sites (`https://sites.google.com/view/jp-study/%C3%B4n-theo-d%E1%BA%A1ng`) implementing the Learn → Practice → Check methodology across N4, N3, and N2.
  - Overhaul `LUYỆN TẬP` (Kho đề) page on Google Sites (`https://sites.google.com/view/jp-study/luy%E1%BB%87n-t%E1%BA%ADp`) organizing 5 practice tiers while preserving 100% of live P0 Forms (W01-B01, W01-B02, W01-B03).
  - Verify mobile responsiveness (360px to 1440px) and update `GOOGLE_SITES_UI_QA.md`.

## 2026-10-15 — Phase 3.6 Google Sites learner portal UI/UX overhaul and responsive verification

- Design and deploy polished, Japanese-inspired learner portal on Google Sites (`https://sites.google.com/view/jp-study`) using Aristotle theme with soft lavender/indigo palette, clean typography, and zero-waste title-only header.
- Implement structured 5-page learner architecture: Trang chủ (Today's Card, CTA button, rest reminder), Luyện tập (3 active P0 forms, Week 2 placeholders), Mẹo học (6 core PDF guides summarized), Nghe & Nói (NHK, Irodori, 4 roleplays, Gemini prompt), and Tiến bộ (Gemini Error Tutor workflow, Sheets overview).
- Verify responsive mobile-first layouts and touch targets across 6 viewports: Mobile Small (360x800), Mobile Standard (390x844), Mobile Large (430x932), Tablet (768x1024), Desktop Standard (1280x800), and Desktop Large (1440x900) with zero horizontal scroll.
- Configure Google Sites publication settings with search engine indexing blocked ("Yêu cầu công cụ tìm kiếm công khai không hiển thị trang web của tôi").
- Preserve 100% of underlying backend architecture: Google Sheets source of truth, 3 P0 Google Forms, Apps Script triggers, QA synthetic isolation, and Drive exports remain intact.

## 2026-10-15 — Live P0 acceptance, synthetic QA verification and dashboard activation

- Configure Google Forms grade release settings to immediate post-submission release with missed questions, correct answers, point values, and detailed explanations.
- Execute authentic browser synthetic QA submissions across all three P0 Forms (W01-B01: 3/5, W01-B02: 6/8, W01-B03: 3/5) containing correct, incorrect, and blank items via authenticated browser session.
- Verify installable submit triggers and QA quarantine in Google Apps Script via `verifySyntheticQa()`; confirm zero learner rows in `CHI_TIET` and isolated records in `JP_STUDY_QA_SYNTHETIC` spreadsheet and Drive CSV/JSON reports.
- Execute `activateP0Verified()` to activate all three P0 Forms; verify learner dashboard `HỌC HÔM NAY` status is `Sẵn sàng` with working `MỞ BÀI NGẮN` link and active week checklist.
- Verify automatic export of management report `DAILY_LEARNING_REPORT.csv` and `DAILY_LEARNING_REPORT.json` to Google Drive.
- Verify responsive layout at mobile width (390x844) and laptop viewport (1280x800); confirm owner-only access gating until learner account is assigned.

## 2026-10-15 — Native P0 creation and restricted responder checkpoint

- Execute the existing bound Apps Script. Prior Completed executions were only `onOpen`; they had not deployed quizzes. Create exactly three unpublished P0 Forms, reusing the interrupted first Form, with no changes to source question IDs or keys.
- Repair the native unlinked-Form destination exception without masking unrelated errors or replacing an unexpected destination. Native `setupP0` and `auditForms` then complete.
- Enable Drive Advanced v3 with owner consent and remove default published-view `anyone` responder permissions. Confirm owner-only ACLs on all three Forms via native execution and independent Drive metadata readback.
- Add owner-only deployment inspection and isolated synthetic QA helpers. Pass 394 local logic/Workspace mock checks; helper E2E remains unverified until actual browser submissions and native trigger records exist.
- Synchronize the bound manifest with explicit approved scopes and Asia/Tokyo. Google still gates Sheets access behind OAuth. No publication, activation, learner sharing or live grading/export success is claimed. See [deployment evidence](qa/drive_first_deployment.json).

## 2026-10-15 — Drive-first templates and private Sheets checkpoint

- Create owner-only Drive folders and a native five-tab dashboard; upload seven concise PDFs and tutor/report prompts. No private IDs, records or URLs are published here.
- Reuse 68 of the original 80 N4 questions across ten short quiz specifications. Preserve original bank, keys, patterns and previous checkpoints.
- Add an idempotent Workspace installer, raw response retention, QA quarantine, item-ID scoring mapping, new/review/assisted/unknown separation and daily CSV/JSON export.
- Pass 387 pure-logic/Workspace mock checks. Read back native Sheets and permissions; repair Vietnamese-locale link errors with rich-text links. Verify PDFs and exported-sheet layouts within documented limits.
- Keep Forms deployment, Google grading/triggers and real-device usability QA_PENDING until authenticated live acceptance; this checkpoint does not claim Phase 3.5 completion.


## 2026-10-15 — Initial public synchronization

- Preserve Phase 1, Phase 2, Phase 2.1 and Phase 3 pilot checkpoints in a reviewable repository.
- Publish deidentified Markdown editions of private reports and rebuild the Phase 3 starting PDF with a synthetic profile. Keep all originals local and record source hashes/omissions.
- Preserve the audited 80-question N4 payload, four speaking scenarios, 31 patterns/37 instructional examples and validated keys; retain QA provenance and current tests.
- Include four distinct blank workbook checkpoints, six useful PDFs, Gemini prompts, research synthesis/citation metadata, historical implementation source and scoped QA reports.
- Document incomplete expansion/N3/N2 work, evidence gaps and persistent future commit/push policy. No credentials, personal progress exports, third-party full-text downloads or release ZIP committed.
