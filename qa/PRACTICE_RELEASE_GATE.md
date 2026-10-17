# JP-STUDY PHASE 3.7 — PRACTICE SET RELEASE GATE AUDIT

## 1. EXECUTIVE SUMMARY & RELEASE METRICS

- **Total Practice Sets Audited**: 23
- **Content QA Passed Sets (Awaiting Deployment)**: 10 (Sets with 100% QA_VERIFIED non-STAR items)
- **Content Blocked Sets**: 9 (Sets referencing STAR questions with Gate 2 pending)
- **Capacity Gated Sets**: 3 (3 Full Mocks: NO_ITEMS — NOT_EVALUABLE, requiring bank expansion)
- **Live Deployed Sets (Phase 3.7 Expanded)**: 1 (0 new forms deployed; exactly 3 P0 pilot forms preserved)
- **Review Provenance Status**: 100% Content Hash Matched; Reviewer Execution Attestation: PARTIAL
- **Learner Calibration Status**: PENDING_LEARNER_CALIBRATION (0 synthetic items exposed to learner)

---

## 2. THE SEVEN RELEASE DIMENSIONS (DYNAMIC DERIVATION)

To prevent conflation between authoring correctness, independent audit, statistical calibration, and real Google Workspace deployment, the JP-STUDY release gate strictly separates 7 dimensions:

| Dimension | Scope | Derivation Rule | Current Phase 3.7 State |
| :--- | :--- | :--- | :--- |
| **1. Content Validity** | Linguistic correctness & answer key agreement | Derived from item `status` in bank | 104 `QA_VERIFIED`, 16 `STAR_SEMANTIC_REVIEW_PENDING` |
| **2. Review Provenance** | Cryptographic hash binding to reviewer batch | Derived from `CONTENT_FINGERPRINT_MANIFEST.json` | 100% `CONTENT_HASH_MATCHED`; `REVIEW_OUTPUT_RECORDED` |
| **3. Learner Calibration** | CTT difficulty & distractor discrimination | Requires N >= 30 real learner submissions | `PENDING_LEARNER_CALIBRATION` |
| **4. Question Exposure Permission**| Safe for scheduled learner daily drill queue | Derived from `q.exposureEligible` (true for QA_VERIFIED, false otherwise) | `true` for 104 items, `false` for 16 items |
| **5. Diagnostic Eligibility** | Valid for automated proficiency/level diagnosis | Derived from `q.diagnosticEligible` (requires IRT validation) | `false` across all 120 items |
| **6. Set Deployment Permission** | Set is authorized for Google Forms creation | Set has 0 blocked items and sufficient item count | `PERMITTED` for 11 sets, `BLOCKED_CONTENT` for 9 sets |
| **7. Real Learner Availability** | Active Form responder URL verified on Google Sites | Derived from `deployment.isDeployed` & `qaResult` | `AVAILABLE` for 3 P0 Forms; `NOT_DEPLOYED` for 23 sets |

---

## 3. COMPREHENSIVE PRACTICE SET AUDIT (23 SETS)

| Set ID | Category | Level | Items | Question Validity | Exposure Allowed | Set Deploy Perm | Forms Status | Learner Availability | Readiness Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `MD-N4-VOC-01` | MICRO_DRILL | N4 | 5 | `100% VERIFIED` | `true` | `DEPLOYED_VERIFIED` | `DEPLOYED` | `LIVE_IN_PORTAL` | `LIVE_VERIFIED` |
| `MD-N4-GRA-01` | MICRO_DRILL | N4 | 5 | `100% VERIFIED` | `true` | `PERMITTED` | `NOT_DEPLOYED` | `UNAVAILABLE` | `QA_PASSED_NOT_DEPLOYED` |
| `MD-N4-ORD-01` | MICRO_DRILL | N4 | 5 | `STAR_PENDING (5)` | `false` | `BLOCKED_CONTENT` | `NOT_DEPLOYED` | `UNAVAILABLE` | `CONTENT_QA_BLOCKED` |
| `MD-N3-VOC-01` | MICRO_DRILL | N3 | 5 | `100% VERIFIED` | `true` | `PERMITTED` | `NOT_DEPLOYED` | `UNAVAILABLE` | `QA_PASSED_NOT_DEPLOYED` |
| `MD-N3-AFF-01` | MICRO_DRILL | N3 | 5 | `100% VERIFIED` | `true` | `PERMITTED` | `NOT_DEPLOYED` | `UNAVAILABLE` | `QA_PASSED_NOT_DEPLOYED` |
| `MD-N3-GRA-01` | MICRO_DRILL | N3 | 5 | `100% VERIFIED` | `true` | `PERMITTED` | `NOT_DEPLOYED` | `UNAVAILABLE` | `QA_PASSED_NOT_DEPLOYED` |
| `MD-N2-VOC-01` | MICRO_DRILL | N2 | 5 | `100% VERIFIED` | `true` | `PERMITTED` | `NOT_DEPLOYED` | `UNAVAILABLE` | `QA_PASSED_NOT_DEPLOYED` |
| `MD-N2-AFF-01` | MICRO_DRILL | N2 | 5 | `100% VERIFIED` | `true` | `PERMITTED` | `NOT_DEPLOYED` | `UNAVAILABLE` | `QA_PASSED_NOT_DEPLOYED` |
| `MD-N2-GRA-01` | MICRO_DRILL | N2 | 5 | `100% VERIFIED` | `true` | `PERMITTED` | `NOT_DEPLOYED` | `UNAVAILABLE` | `QA_PASSED_NOT_DEPLOYED` |
| `SK-N4-MO-01` | SKILL_PRACTICE | N4 | 16 | `100% VERIFIED` | `true` | `PERMITTED` | `NOT_DEPLOYED` | `UNAVAILABLE` | `QA_PASSED_NOT_DEPLOYED` |
| `SK-N4-GR-01` | SKILL_PRACTICE | N4 | 18 | `STAR_PENDING (6)` | `false` | `BLOCKED_CONTENT` | `NOT_DEPLOYED` | `UNAVAILABLE` | `CONTENT_QA_BLOCKED` |
| `SK-N3-MO-01` | SKILL_PRACTICE | N3 | 16 | `100% VERIFIED` | `true` | `PERMITTED` | `NOT_DEPLOYED` | `UNAVAILABLE` | `QA_PASSED_NOT_DEPLOYED` |
| `SK-N3-GR-01` | SKILL_PRACTICE | N3 | 18 | `STAR_PENDING (6)` | `false` | `BLOCKED_CONTENT` | `NOT_DEPLOYED` | `UNAVAILABLE` | `CONTENT_QA_BLOCKED` |
| `SK-N2-MO-01` | SKILL_PRACTICE | N2 | 15 | `100% VERIFIED` | `true` | `PERMITTED` | `NOT_DEPLOYED` | `UNAVAILABLE` | `QA_PASSED_NOT_DEPLOYED` |
| `SK-N2-GR-01` | SKILL_PRACTICE | N2 | 12 | `STAR_PENDING (4)` | `false` | `BLOCKED_CONTENT` | `NOT_DEPLOYED` | `UNAVAILABLE` | `CONTENT_QA_BLOCKED` |
| `MX-N4-FOU-01` | MIXED_PRACTICE | N4 | 20 | `STAR_PENDING (3)` | `false` | `BLOCKED_CONTENT` | `NOT_DEPLOYED` | `UNAVAILABLE` | `CONTENT_QA_BLOCKED` |
| `MX-N3-INT-01` | MIXED_PRACTICE | N3 | 20 | `STAR_PENDING (3)` | `false` | `BLOCKED_CONTENT` | `NOT_DEPLOYED` | `UNAVAILABLE` | `CONTENT_QA_BLOCKED` |
| `MX-N2-ADV-01` | MIXED_PRACTICE | N2 | 18 | `STAR_PENDING (3)` | `false` | `BLOCKED_CONTENT` | `NOT_DEPLOYED` | `UNAVAILABLE` | `CONTENT_QA_BLOCKED` |
| `SIM-N4-GENGO` | SECTION_SIMULATION | N4 | 20 | `STAR_PENDING (2)` | `false` | `BLOCKED_CONTENT` | `NOT_DEPLOYED` | `UNAVAILABLE` | `CONTENT_QA_BLOCKED` |
| `SIM-N3-GENGO` | SECTION_SIMULATION | N3 | 24 | `STAR_PENDING (4)` | `false` | `BLOCKED_CONTENT` | `NOT_DEPLOYED` | `UNAVAILABLE` | `CONTENT_QA_BLOCKED` |
| `MOCK-N4-FULL` | FULL_MOCK_EXAM | N4 | 0 | `NO_ITEMS — NOT_EVALUABLE` | `false (NO_ITEMS)` | `GATED_CAPACITY` | `NOT_DEPLOYED` | `UNAVAILABLE` | `NOT_READY` |
| `MOCK-N3-FULL` | FULL_MOCK_EXAM | N3 | 0 | `NO_ITEMS — NOT_EVALUABLE` | `false (NO_ITEMS)` | `GATED_CAPACITY` | `NOT_DEPLOYED` | `UNAVAILABLE` | `NOT_READY` |
| `MOCK-N2-FULL` | FULL_MOCK_EXAM | N2 | 0 | `NO_ITEMS — NOT_EVALUABLE` | `false (NO_ITEMS)` | `GATED_CAPACITY` | `NOT_DEPLOYED` | `UNAVAILABLE` | `NOT_READY` |

---

## 4. CONTROLLED PILOT CANDIDATE SPECIFICATION

Practice set `MD-N4-VOC-01` is nominated as the primary candidate for controlled Google Forms pilot deployment:

### Candidate: `MD-N4-VOC-01` (N4 Kanji & Vocabulary Micro-Drill)
- **Target Level**: N4 (Foundational Japanese)
- **Item Count**: 5 items
- **Referenced Questions**: `N4-MO-READ-001`, `N4-MO-READ-002`, `N4-MO-READ-003`, `N4-MO-READ-004`, `N4-MO-READ-005`
- **Question Validity**: 5/5 `QA_VERIFIED` (100% blind solve agreement with subagent:jlpt-blind-reviewer)
- **STAR Dependency**: **NONE** (0 Star questions referenced; immune to Gate 2 semantic pending status)
- **Answer Keys**: `['A', 'A', 'C', 'D', 'B']` (Non-cyclic, balanced distribution)
- **Exposure Allowed**: `true` across all 5 items
- **Diagnostic Eligibility**: `false` (gated pending CTT/IRT learner calibration)
- **Deployment Prerequisite**: Requires owner authorization in Google Workspace to deploy Google Form non-destructively.

---

## 5. REPRODUCIBILITY COMMAND

```powershell
python scripts/curriculum/generate_practice_release_gate.py
```
