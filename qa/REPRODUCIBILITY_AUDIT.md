# JP-STUDY PHASE 3.7 — P0 REPRODUCIBILITY & INVARIANCE AUDIT REPORT

## 1. EXECUTIVE SUMMARY & VERDICT

- **Audit Status**: PASS
- **Total Questions Evaluated**: 120
- **Run 1 vs Baseline Mismatches**: 0
- **Run 2 vs Run 1 Mismatches**: 0
- **Six Repaired Items Status**: 100% PRESERVED & INVARIANT
- **Historical Evidence Files Status**: 100% IMMUTABLE & PRESERVED
- **Evaluation Environment**: Isolated disposable sandbox (`tmp/jp_study_rebuild_sandbox_*`)

---

## 2. METHODOLOGY & SANDBOX ISOLATION

To satisfy the non-negotiable directive that destructive tests must not run directly against the production tree:
1. An isolated, clean sandbox directory was instantiated via Python `tempfile.mkdtemp`.
2. The entire project source, curriculum, and QA evidence were copied to the sandbox.
3. Baseline cryptographic content fingerprints (Unicode NFC SHA-256) were recorded for all 120 questions from the accepted checkpoint.
4. `python scripts/curriculum/build_expanded_bank.py` was executed completely (Run 1).
5. Canonical fingerprints were re-extracted and compared key-by-key and chunk-by-chunk against the accepted baseline.
6. `python scripts/curriculum/build_expanded_bank.py` was executed a second time (Run 2) to test idempotency and lack of state corruption.
7. Hashes of historical reviewer batches (`qa/blind_review_n*.json`, `qa/raw_blind_review_*.json`) were verified for immutability.

---

## 3. AUDIT OF THE SIX REPAIRED QUESTIONS

All 6 questions repaired during Phase 3.7 ambiguity resolution were integrated into the canonical source definition in `scripts/curriculum/rebuild_and_repair_bank.py` and verified for zero drift across both rebuild runs:

| Question ID | Level | Correct Key | Canonical Fingerprint (SHA-256) | Run 1 Match | Run 2 Match | Invariant |
| :--- | :--- | :---: | :--- | :---: | :---: | :---: |
| `N4-GR-FORM-010` | N4 | `A` | `7eeec32b9584542d...` | PASS | PASS | PASS |
| `N4-GR-STAR-002` | N4 | `D` | `a7de6f437d0ba643...` | PASS | PASS | PASS |
| `N4-GR-STAR-006` | N4 | `A` | `8effaa221d34a725...` | PASS | PASS | PASS |
| `N3-GR-FORM-006` | N3 | `B` | `1b1c6582253c5acd...` | PASS | PASS | PASS |
| `N3-GR-STAR-001` | N3 | `A` | `1a78d433d822942c...` | PASS | PASS | PASS |
| `N2-GR-FORM-003` | N2 | `A` | `d968908774862c24...` | PASS | PASS | PASS |

### Detailed Verification of Repaired Items
- **`N4-GR-FORM-010`**: Condition `天気がよければ` (Option A: よければ). Distractors `['いいば', 'よくて', 'よくても']`. Explanation correctly targets i-adjective conditional. Content invariant across both rebuild runs.
- **`N4-GR-STAR-002`**: Assembly `北海道に住んでいる友達に会いに行く`. Star slot 3 = `友達に` (Option D). Invariant across both rebuild runs.
- **`N4-GR-STAR-006`**: Assembly `留学するためにお金をためようと思っている`. Star slot 3 = `お金を` (Option A). Invariant across both rebuild runs.
- **`N3-GR-FORM-006`**: Context `約束の時間に遅れないはずだ`. Single defensible choice: `はず` (Option B: はず). Invariant across both rebuild runs.
- **`N3-GR-STAR-001`**: Assembly `経験の有無にかかわらず意欲があれば`. Star slot 3 = `意欲が` (Option A). Invariant across both rebuild runs.
- **`N2-GR-FORM-003`**: Context `地球温暖化が世界規模で深刻化しつつある`. Single defensible formal aspectual auxiliary: `しつつある` (Option A: しつつある). Invariant across both rebuild runs.

---

## 4. HISTORICAL BLIND-REVIEW EVIDENCE INTEGRITY

The rebuild pipeline guarantees that historical evidence files are read-only and never overwritten by generation runs:

| Evidence File Path | SHA-256 Before Rebuild | SHA-256 After 2 Rebuilds | Integrity Status |
| :--- | :--- | :--- | :---: |
| `qa\blind_review_n4.json` | `45edd284a70fa522...` | `45edd284a70fa522...` | IMMUTABLE (PASS) |
| `qa\blind_review_n3.json` | `c6920aaf8d236aa2...` | `c6920aaf8d236aa2...` | IMMUTABLE (PASS) |
| `qa\blind_review_n2.json` | `9797fb4af47bc0e6...` | `9797fb4af47bc0e6...` | IMMUTABLE (PASS) |
| `qa\blind_review_repaired_6.json` | `0df362a545946ed3...` | `0df362a545946ed3...` | IMMUTABLE (PASS) |
| `qa\raw_blind_review_n4.json` | `bec76912b721b1a3...` | `bec76912b721b1a3...` | IMMUTABLE (PASS) |
| `qa\raw_blind_review_n3.json` | `69dc6a89876faf54...` | `69dc6a89876faf54...` | IMMUTABLE (PASS) |
| `qa\raw_blind_review_n2.json` | `98e979716eb04d67...` | `98e979716eb04d67...` | IMMUTABLE (PASS) |
| `qa\raw_blind_review_repaired_6.json` | `0ca90b7ddec2a903...` | `0ca90b7ddec2a903...` | IMMUTABLE (PASS) |

---

## 5. REPRODUCIBILITY GUARANTEE & CONCLUSION

1. **Deterministic Generator**: `scripts/curriculum/rebuild_and_repair_bank.py` uses deterministic raw item definitions and a fixed pseudo-random seed (`seed-clean-audit`).
2. **Idempotence**: Successive rebuild executions generate exact byte-for-byte identical content.
3. **Zero Destruction**: Existing review files, status ledgers, and practice set statuses are cryptographically reconciled, never wiped or overwritten with dummy values.
4. **P0 Invariance Gate**: **PASS (120/120 items verified)**.
