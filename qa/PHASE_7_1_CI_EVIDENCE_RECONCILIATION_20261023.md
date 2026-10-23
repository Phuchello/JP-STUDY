# Phase 7.1 CI evidence reconciliation — 2026-10-23

## Scope and starting state

This is a targeted recovery of the Phase 7.1 integrity failure; it does not revise exam content, released JavaScript/JSON payloads, audio, M14, or M15. Local `HEAD` and authenticated GitHub `main` both started at `7743a18f08b2f4efb228a411acf99f78afe4a0c5`. The failing hosted run was [Content QA run #44](https://github.com/Phuchello/JP-STUDY/actions/runs/39961665474). Its first failing step was `python scripts/curriculum/audit_blind_remapping_integrity.py`; later M11–M13 strict validators, tests, browser checks and Pages deployment were skipped.

## Byte-provenance findings

| Evidence | Recorded/captured SHA-256 | Git blob SHA-256 | Exact difference | Finding |
|---|---|---|---|---|
| M11 pre-release JSON baseline | `6cc5a46a65a8b44ca886901a9dc26a355854c9cf349f8eee8b629b6edea248fc` (308,893 bytes) | `7ddbab1a9c5773ab34c4bc4d9c3d552c5267cc0904949d5222d971ac93a256b1` (304,643 bytes) | The local capture has 4,250 CRLF pairs; the committed Git blob has the same 4,250 line breaks as LF. Replacing CRLF with LF makes the decoded bytes identical. No BOM; final LF present. | Line-ending representation mismatch, not substantive baseline tampering. The old receipt correctly identifies the captured CRLF bytes. |
| M12 pre-release JSON baseline | `40ef9bf626bdb69df502fa8549b87b94c2add680bc316fcbb23fa8719975ac76` (286,413 bytes) | Same SHA | LF-only, no BOM, final LF. | No representation discrepancy. |
| M13 pre-release JSON baseline | `c6d92cb8f541a9d7815fa348103e021437d0742b2f57df0e8bb1d9e507d9d001` (307,073 bytes) | Same SHA | LF-only, no BOM, final LF. | No representation discrepancy. |
| v6 reviewer response | Recorded capture SHA `dd7be49427875f5dcdb7c946d47bc03b9ca5e1a146e34e814fddd3f5c2414331` (13,586 bytes) | `c33d85efbdcd51428a32df561b02cf9e91acf8db675e4344f8846debadb90807` (13,585 bytes) | Exactly one CR byte at line 102 was normalized away: one CRLF in the captured bytes became LF in the Git blob. Canonical CRLF/CR-to-LF bytes are identical. No BOM; final LF present. | The recorded digest is recoverable from the original local byte stream preserved at recovery start. It is not an unverified text/key change. |

The response names packet SHA-256 `7da03d691cc94c6f9cdbd5620ea57b1a1c4b9c49c8b046704a8114690b74d5ce`, which matches the preserved v6 packet; the response contains 60 keyed-free response records. Existing item-level mapping, answer-text and current-fingerprint checks are retained. No packet was resent and no reviewer response was regenerated. The repository can verify bytes and bindings; it does not provide a portable execution attestation for the AI editorial review, nor native-speaker/JLPT psychometric certification.

## Repair and fail-closed contract

Four exact byte captures were preserved in `qa/phase71_immutable_originals/` using exclusive-create before the evidence paths were normalized by Git: the three pre-release baselines and the v6 response. Their hashes are recorded above and in the receipts. `.gitattributes` applies `-text -diff` only to these `.raw` captures so Git cannot rewrite them on checkout. The existing readable text/JSON remains ordinary repository text.

The receipt builder now checks both: (1) the exact raw archive digest against the digest already recorded by the receipt or the fixed v6 capture digest, and (2) byte equality after a declared UTF-8 CRLF/CR-to-LF canonicalization between the capture and readable Git companion. It records both the original capture digest and canonical companion digest. A missing archive, wrong digest, invalid UTF-8, or any substantive canonical-content difference fails validation. Packet/raw paths are constrained to the repository and missing or changed source files fail closed. The prior `releasedBaselineSha256` is preserved; it was not replaced with a hash selected merely to pass CI.

Automated regression coverage exercises LF and CRLF pairs, lone-CR conversion, substantive content changes, missing snapshots/archives/responses, incorrect recorded hashes, packet mutation, stale question fingerprints, answer mutation and selected-option text mismatch. The original adversarial release suite remains unchanged.

## Receipt and reviewer reconciliation

| Exam | Rows | Reused historical | Current-version reviewed | Fingerprint mismatches | Missing/invalid evidence | Semantic mismatches | Unresolved answer-changing alternatives | Preserved reviewer concerns |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| M11 | 105 | 83 | 22 | 0 | 0 | 0 | 0 | 2 |
| M12 | 105 | 83 | 22 | 0 | 0 | 0 | 0 | 2 |
| M13 | 105 | 83 | 22 | 0 | 0 | 0 | 0 | 4 |

The concerns are retained in the receipts; a zero answer mismatch does not imply that every editorial concern is absent. M11's historic revision layers and the M12/M13 current-version gates are unchanged in policy. All three published receipts validate 315/315 rows locally after the repair.

## Collateral historical QA audit

The integration delta from `1c3a3c99c2c395bf1e1d18e10f4a59161f0e4873` to `7743a18f08b2f4efb228a411acf99f78afe4a0c5` was inspected for playback receipts, independent audit reports, originality output, derived blind-review rows, question ledgers, M11 layers and manifest/index outputs. Refreshed playback timestamps and transient playback positions do not change the recorded MP3 hashes, 30/30 track coverage or durations; no MP3 or audio ordering was edited. Derived M11–M13 audit and review outputs are current-version products and are not represented as original reviewer transcripts. The M13 exact-stem count reduction from 27 to 2 is attributable to five M13 STAR prompt frames changing; the two remaining exact matches are generic listening instruction stems. Current originality verification reports no repeated reading passage/listening script/distractor set. Historical raw reviewer responses and sealed review layers were not rewritten in this recovery; no historical file needed restoration.

## Verification record

Commands completed locally on Windows:

- `python scripts/curriculum/audit_blind_remapping_integrity.py` — pass; 1,050 historic raw rows and 315 current-version Phase 7.1 rows validated; zero unrecoverable rows.
- `python scripts/curriculum/build_phase_71_candidate_reconciliation.py --validate published` — pass, 315/315.
- `python scripts/curriculum/validate_n2_mock_11_blind_review.py` — pass; 105 current fingerprints and exact semantic mappings, 120 retained STAR permutation judgments.
- `python scripts/curriculum/validate_n2_mock_12_release.py` and `python scripts/curriculum/validate_n2_mock_13_release.py` — pass.
- M11/M12/M13 originality audits — pass. M13 audio integrity — 30/30 SHA-256, decode and duration checks. Question fingerprints — 525 valid.
- `python -m unittest scripts.tests.test_adversarial_release_gate` — 15 passed, including fail-closed key/content/audio/provenance mutations.
- `python -m pytest -q scripts/tests` — **230 passed, 131 subtests passed**.
- `python -m unittest discover -s scripts/tests` — **225 tests passed**. The dynamic active audit in the suite checked 13 mocks / 1,365 items, with zero fingerprint/key/review-required failures.
- `python scripts/update_manifest.py` followed by `python scripts/validate_release.py` — manifest rebuilt; **28/28 release snapshot checks passed** (1,204 files).
- Candidate Chromium E2E via `node scripts/tests/test_phase_71_candidate_reading_feedback.cjs` — passed 3 synthetic IDs (`N2_11_M10_01`, `N2_12_M11_01`, `N2_13_M11_01`) at desktop and mobile widths; answer feedback appeared only after submission; no page/console errors. The result is preserved in `qa/PHASE_7_1_CI_RECOVERY_BROWSER_E2E_20261023.json` (SHA-256 `d0bb896b541680003c0d45e0d89c99564353345577282fdb958cea923e8f9910`). This is local synthetic E2E, not public-site verification.

Test-count reconciliation: hosted run #39 at `c830f3a0c3759cca861be7b6125a6c440c7a0011` logged `Ran 206 tests`. Static discovery of committed `unittest.TestCase.test*` methods matches 206 at `c830`; it rises to 209 at `46fbd3b`, 210 at `312b5b3`, 212 at `611b18f` and `1c3a3c9`, and 214 at `7743`. Thus the previously reported local 210 corresponds to a later source tree than the 206-test hosted run; it is not a count disagreement on one revision. The current recovery adds 11 unittest methods and 5 pytest-collected functions, giving 225 unittest tests and 230 pytest tests plus 131 subtests.

## Hosted release and live-site verification

The recovery commit was pushed without rewriting history. Authenticated GitHub reports `main` at `dcb737f059ffa8caa3530ec44eecdd215d9a1d90`. [Content QA run #45](https://github.com/Phuchello/JP-STUDY/actions/runs/39971096214) for that exact SHA completed successfully, including the formerly failing integrity step, M11–M13 gates, adversarial tests, full regression, all browser mock regressions, audio playback checks, and QA artifact upload. The separate gated GitHub Pages deployment job also completed successfully. Run #44 remains a historical failure; its skipped steps are not counted as passing.

After deployment, the live catalog and routes were inspected in the in-app browser. N2-MOCK-01 through #13 have active launch links; #14 appears only as an in-development card with a disabled control. The site also has disabled #15–20 catalog placeholders; no M15 exam content was created or published. The live engine displayed the revised items `N2_11_M10_01` (55/75), `N2_12_M11_01` (60/75), and `N2_13_M11_01` (60/75) with their reading passages and options; no correctness marker or feedback appeared before submission. All five M11 STAR items `N2_11_M8_01`–`_05` loaded in positions 45–49 with four slots and all four fragments displayed. The separate M11 strict validator and hosted browser regression passed answer/permutation alignment. The live M11 listening route loaded track `N2_11_M1_L01` (35.584 seconds), and its player entered the playing state.

No submission was made in the owner's existing browser because the app persists attempts and mistake state to that browser's `localStorage`; protecting learner history took priority over creating a live synthetic record. The candidate feedback E2E passed locally and in hosted run #45 for the exact recovery SHA, confirming after-submit answer/explanation rendering against versioned candidate fixtures. A separate shell-launched browser could not resolve `phuchello.github.io` in this network-restricted environment; no DNS workaround was used. Accordingly, the live payload and routes are verified, and post-submit behavior is covered by CI E2E; a post-submit interaction was not performed on the owner's live browser profile.

Release status: M11, M12 and M13 revisions are `RELEASED_AND_LIVE_VERIFIED` for deployed learner-visible content. M14 remains `BLOCKED` because TTS provenance/authorization and public audio redistribution rights are unresolved. M15 is `NOT_STARTED` (its disabled catalog placeholder predates this recovery).
