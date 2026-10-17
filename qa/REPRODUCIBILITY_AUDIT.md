# JP-STUDY PHASE 3.7 — P0 FULL-ITEM REPRODUCIBILITY & INVARIANCE AUDIT REPORT

## 1. EXECUTIVE SUMMARY & VERDICT

- **Overall Audit Verdict**: **PASS**
- **Total Questions Evaluated**: 120
- **Full-Item Hash Mismatches (Run 1 vs Baseline)**: 0
- **Full-Item Hash Mismatches (Run 2 vs Run 1)**: 0
- **Blind Input SHA-256 Stability**: **PASS (100% Invariant)**
- **Scoring SHA-256 Stability**: **PASS (100% Invariant)**
- **Pedagogical Content SHA-256 Stability**: **PASS (100% Invariant)**
- **Six Repaired Items Invariance**: **100% PRESERVED & INVARIANT**
- **Historical Evidence Files Invariance**: **100% IMMUTABLE & PRESERVED**
- **Sandbox Isolation Mode**: `CLEAN_GIT_ARCHIVE (tree: ad0c9e896007, commit: 95215b38)`
- **Source Git Commit**: `95215b382fa04edc0d4736391ddd6a1e9a1d01bf`
- **Source Tree SHA**: `ad0c9e8960076a3f1335c1d60046581cb25fb681`

---

## 2. MULTI-TIER CRYPTOGRAPHIC INVARIANCE MATRIX

The rebuild pipeline guarantees bit-for-bit determinism across all 4 cryptographic hash tiers:

| Hash Tier | Covered Scope | Run 1 Matches | Run 2 Matches | Status |
| :--- | :--- | :---: | :---: | :---: |
| **BLIND_INPUT_SHA256** | ID, level, typeId, stem, passage, choices | 120 / 120 | 120 / 120 | **PASS** |
| **SCORING_SHA256** | ID, level, typeId, correctAnswer, option bindings | 120 / 120 | 120 / 120 | **PASS** |
| **PEDAGOGICAL_SHA256** | explanationVi, distractorExplanations, remediation, assembledSentence | 120 / 120 | 120 / 120 | **PASS** |
| **FULL_ITEM_SHA256** | All release-critical item fields combined | 120 / 120 | 120 / 120 | **PASS** |

---

## 3. AUDIT OF THE SIX REPAIRED QUESTIONS

All 6 repaired questions integrated into `scripts/curriculum/rebuild_and_repair_bank.py` were verified across both rebuild runs:

| Question ID | Level | Correct Key | Status | Blind Input SHA-256 | Full Item SHA-256 | Invariant |
| :--- | :---: | :---: | :--- | :--- | :--- | :---: |
| `N4-GR-FORM-010` | N4 | `A` | `QA_VERIFIED` | `7eeec32b9584...` | `acc934a46cdb...` | **PASS** |
| `N4-GR-STAR-002` | N4 | `D` | `STAR_SEMANTIC_REVIEW_PENDING` | `a7de6f437d0b...` | `92bc822f3d91...` | **PASS** |
| `N4-GR-STAR-006` | N4 | `A` | `STAR_SEMANTIC_REVIEW_PENDING` | `8effaa221d34...` | `b084d4e4a177...` | **PASS** |
| `N3-GR-FORM-006` | N3 | `B` | `QA_VERIFIED` | `1b1c6582253c...` | `16ac994eee36...` | **PASS** |
| `N3-GR-STAR-001` | N3 | `A` | `STAR_SEMANTIC_REVIEW_PENDING` | `1a78d433d822...` | `4b8d898ae78b...` | **PASS** |
| `N2-GR-FORM-003` | N2 | `A` | `QA_VERIFIED` | `d96890877486...` | `2cd54aed3909...` | **PASS** |

---

## 4. HISTORICAL BLIND-REVIEW EVIDENCE INTEGRITY

| Evidence File Path | SHA-256 Before Rebuild | SHA-256 After 2 Rebuilds | Integrity Status |
| :--- | :--- | :--- | :---: |
| `qa\blind_review_n4.json` | `45edd284a70fa522...` | `45edd284a70fa522...` | **IMMUTABLE (PASS)** |
| `qa\blind_review_n3.json` | `c6920aaf8d236aa2...` | `c6920aaf8d236aa2...` | **IMMUTABLE (PASS)** |
| `qa\blind_review_n2.json` | `9797fb4af47bc0e6...` | `9797fb4af47bc0e6...` | **IMMUTABLE (PASS)** |
| `qa\blind_review_repaired_6.json` | `c73a57604167f9c2...` | `c73a57604167f9c2...` | **IMMUTABLE (PASS)** |
| `qa\raw_blind_review_n4.json` | `bec76912b721b1a3...` | `bec76912b721b1a3...` | **IMMUTABLE (PASS)** |
| `qa\raw_blind_review_n3.json` | `1014d71abca05462...` | `1014d71abca05462...` | **IMMUTABLE (PASS)** |
| `qa\raw_blind_review_n2.json` | `98e979716eb04d67...` | `98e979716eb04d67...` | **IMMUTABLE (PASS)** |
| `qa\raw_blind_review_repaired_6.json` | `0ca90b7ddec2a903...` | `0ca90b7ddec2a903...` | **IMMUTABLE (PASS)** |

---

## 5. REPEATABLE VERIFICATION COMMAND

```powershell
python scripts/curriculum/verify_rebuild_invariance.py
```
