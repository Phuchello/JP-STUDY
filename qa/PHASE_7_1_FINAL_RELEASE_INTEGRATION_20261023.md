# Phase 7.1 final release integration — 2026-10-23

**Current state:** local release gates passed; GitHub push, hosted CI, and live-site verification are pending. This report is updated after those checks.

## Repository and exact payloads

- Starting local HEAD and independently verified GitHub `main`: `1c3a3c99c2c395bf1e1d18e10f4a59161f0e4873`. Direct `git fetch` was blocked by DNS, so the authenticated GitHub integration was used to verify the starting remote SHA.
- Three exact pre-release exam snapshots were captured before promotion and are retained at `qa/n2_mock_11_phase71_pre_release_baseline.json`, `qa/n2_mock_12_phase71_pre_release_baseline.json`, and `qa/n2_mock_13_phase71_pre_release_baseline.json`. Their hashes are recorded in each candidate receipt.
- The final local exam hashes are M11 `f57af9b6e12806a380c3fe8a894a4ebc86b7a71b36458c02d356552e8c56f232`, M12 `24f7eefd7c51d0c1913aa1be0fb9e2c3b9cb886899af307cf6a80582cce139c2`, and M13 `b9765ae9bd09cf313ab1ae323b281655c41f28933cbc9ec4ac36219bedb7d0b6`. Final candidate receipt hashes after path-redaction provenance: M11 `06249f8558245a1a4ed5be23cee59f01d10ed9494b2cb705bc5376ecad256d79`, M12 `c7d48fc50d1441f80ac120aa158975842b0ef91cce8cf582586c9e9c86c9263f`, M13 `4ae213e1fb918f02b2eb71418cbb0fd98705454f64e2d6e1c48ee93ed01e3ec8`.
- Each exam remains 75 Section 1 + 30 Listening; stable exam/question IDs, keys, timing, and all 30 Listening item payloads are preserved. The three titles had the obsolete “đang phát triển” suffix removed. No audio or TTS was generated.

## Candidate review reconciliation

The machine-readable receipts are `qa/N2_MOCK_11_PHASE71_CANDIDATE_RECONCILIATION.json`, `qa/N2_MOCK_12_PHASE71_CANDIDATE_RECONCILIATION.json`, and `qa/N2_MOCK_13_PHASE71_CANDIDATE_RECONCILIATION.json`. Their paired key-free snapshots are `qa/blind_items_m11_phase71_candidate.json`, `qa/blind_items_m12_phase71_candidate.json`, and `qa/blind_items_m13_phase71_candidate.json`.

| Exam | Rows | Reused exact released version | Changed, freshly reviewed | Pending / invalid | Open answer ambiguity | Disclosed reviewer concerns |
|---|---:|---:|---:|---:|---:|---:|
| M11 | 105 | 83 | 22 | 0 | 0 | 2 |
| M12 | 105 | 83 | 22 | 0 | 0 | 2 |
| M13 | 105 | 83 | 22 | 0 | 0 | 4 |
| **Total** | **315** | **249** | **66** | **0** | **0** | **8** |

For each exam, the 22 changed question IDs are `M8_01–05`, `M10_01–05`, `M11_01–09`, and `M13_01–03`, with the exam prefix `N2_11`, `N2_12`, or `N2_13`. That is 51 changed Reading items and 15 changed STAR items. Other explanation-only updates do not alter answer-review fingerprints; all 108 option-specific Vietnamese distractor explanations are independently checked for current option binding and preserved in the JSON/JS output.

Changed-row source counts are bound in the receipts: M11 uses 22 rows from the preserved v6 packet; M12 uses 16 v6, four M12/M13 STAR-delta, one final-integration-delta, and one v8 row; M13 uses 15 v6, three STAR-delta, three final-integration-delta, and one v8 row. Raw response files remain attributable and hash-checked. The separate reviewer was an AI reviewer in a distinct task, not a human language specialist; there is no portable execution attestation, native-speaker certification, or JLPT psychometric calibration.

Two raw JSON review envelopes contained absolute local-profile paths in metadata fields. Before publication, their original exact bytes were retained under ignored local `tmp/phase7/phase71_original_raw/`; the public copies replace only those path fields with repository-relative packet paths. The reviewer answer/result payload hashes are unchanged and recorded with both original and published envelope hashes in the adjacent `*.redaction_provenance.json` files, which the candidate receipts also hash-bind. Three stale current-delta raw envelopes were likewise retained locally and excluded from publication; their packets were superseded by the version-matched review sources listed above.

Reviewer concerns are disclosed, not treated as second answers: M11 has notes on `N2_11_M2_05` (保障/保証 nuance) and `N2_11_M9_02` (ものの is grammatically possible but contrastive); M12 notes a somewhat heavy but clear STAR clause at `N2_12_M8_02` and v8 packet skill-label metadata at `N2_12_M10_05`; M13 notes possible topicalized order at `N2_13_M8_01`, a natural contextual extension at `N2_13_M8_02`, low inference at `N2_13_M11_01`, and low inference/easy distractor rejection at `N2_13_M11_03`. None records an answer-changing alternative. The M12/M13 packet metadata concern is not present in the promoted question skill values; the final candidate browser fixture displays `Reading`.

The earlier `PHASE_7_1_M11_CURRENT_DELTA_*`, `M12_CURRENT_DELTA_*`, and `M13_CURRENT_DELTA_*` packets were built against stale ignored drafts. They are preserved but marked **SUPERSEDED_VERSION_MISMATCH** here and are not used by the final receipts; their raw envelopes remain only in ignored local storage. The v6, v8, final-integration, and STAR-delta packets are preserved. For the two path-bearing JSON raw envelopes used by the receipts, only the machine-local path metadata was replaced; the reviewer answer/result payload hashes are unchanged and sidecar-bound. Historical M11 revision layers and the earlier M11–M13 sealed/reconciliation files were not overwritten. M11’s old validator replays the preserved pre-Phase-7.1 baseline; the new candidate receipt is checked separately. The shared generic reconciliation checker was not weakened.

## Content and integration changes

- The 51 Reading revisions are focused edits to passage/question inference and answer alignment; no arbitrary passage padding was introduced. The exact before/after inventory remains in `qa/PHASE_7_1_CANDIDATE_REPAIR_QA.md`.
- The 15 STAR candidates retain four displayed slots and the keyed third-fragment answer. M12 `N2_12_M8_05` clarifies `だけで…ず…も` and its predicate; M13 `N2_13_M8_02` anchors `だけでなく…も` scope; M13 `N2_13_M8_05` distinguishes the article as the object and multiple sources as the comparison set. The earlier duplicated invoice scenario remains absent.
- The published JSON, `docs/widgets/mock_exam_bank.js`, and catalog cards were regenerated from the same promoted payloads. The #12/#13 integration scripts now accept the current “Practice Mock Exam” catalog titles and #11 enforces the version review gate too.
- New additive receipt validation checks exact current exam hash, 105 unique item fingerprints, raw/packet file digests, exact option text and answer IDs, and zero unresolved alternatives. Existing sealed M11–M13 release layers remain available for historical verification.

## Local test evidence

- `python scripts/curriculum/build_phase_71_candidate_reconciliation.py --validate published`: **315/315 pass**.
- M11 historical replay, M12 and M13 strict release validators: **pass**; all 30 current audio tracks per exam remain hash/decode/browser verified.
- Originality audits: M11 and M13 found zero passage/script/audio overlap and zero repeated complete distractor sets; M12 reports three repeated complete distractor sets, matching its prior disclosed audit count. No new overlap defect was introduced.
- `python -m pytest -q scripts/tests`: **219 passed, 131 subtests passed**.
- `python -m unittest discover -s scripts/tests`: **214 tests, OK**. The earlier 15-test adversarial mutation suite also passed.
- Post-redaction checks: `python -m unittest scripts.tests.test_phase_71_candidate_content` **6/6**; M11 historical replay and M12/M13 strict release validators **pass**. Manifest generation indexed **1,197** public files, and `python scripts/validate_release.py` passed **28/28** checks. An earlier unittest attempt hit Windows temporary-directory ACL errors; rerunning with `TEMP` and `TMP` set to the ignored workspace `tmp/phase71-test-temp/` passed.
- Dynamic active-exam audit: **13/13 exams**, each 105/105; CI summary: **1,365/1,365 rows**, zero review-required, fingerprint-mismatch, or key-mismatch rows; 390/390 audio tracks verified.
- Candidate Reading Chromium E2E used synthetic responses on local Chromium: `N2_11_M10_01`, `N2_12_M11_01`, `N2_13_M11_01` all passed two distinct wrong-answer rationales, correct-answer/general feedback after submission, no pre-submit disclosure, 1280px desktop, 390px mobile, and zero page/console errors. Evidence is in `qa/PHASE_7_1_READING_FEEDBACK_E2E_20261023.json`; it is local synthetic evidence, not live-site verification.
- Browser smoke: **15/15** critical flows. Full mock browser regressions for M07–M13 and Phase 6.1 runtime semantics: passed. Deep audio browser checks for M07–M13: **30/30 tracks each**, including desktop/mobile playback, unchanged bytes.
- Local release validation is complete. GitHub push, hosted Content QA/Pages, and direct live-site checks remain pending.

## Release decision and boundaries

Local evidence supports controlled publication of the M11–M13 practice-content revisions; it does not support a claim of linguistic certification. Final release status remains pending until the exact commit passes hosted Content QA and Pages and the live catalog/routes show these question versions and feedback. The live feedback check must use the deployed questions, not synthetic fixtures.

`N2-MOCK-14_PUBLIC_RELEASE: BLOCKED` — TTS authorization provenance and public audio redistribution rights remain unresolved. No M14 text was sent to TTS during this integration. `N2-MOCK-15: NOT_STARTED`.
