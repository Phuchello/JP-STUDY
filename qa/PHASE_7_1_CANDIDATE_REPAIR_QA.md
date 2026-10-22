# Phase 7.1 — candidate content audit and release gate

**Snapshot:** 2026-10-22
**Baseline fetched from `origin/main`:** `c830f3a0c3759cca861be7b6125a6c440c7a0011`
**Gate:** **BLOCKED — candidate only; not approved for release**

## Scope and preservation

The baseline was fetched and matched local `HEAD` on `main`; the worktree was clean before edits. This checkpoint updates authoring sources, a focused test, and QA evidence only. It does not change `data/mock_exams/*.json`, published JS/runtime, catalog pages, audio manifests, audio files, or the active exam bank. No M15 work began. Existing sealed review inputs, historic fingerprints, and raw reviewer responses were not edited. Historic blind reviews do not certify the current candidate version.

No Edge TTS request, audio regeneration, playback of private M14 audio, or audio redistribution occurred in this checkpoint. The prior Phase 7 status text described previous audio work; this gate does not treat TTS authorization or public redistribution rights as resolved.

## M14 Word Usage repair

The five candidate items are `N2_14_M1_28` (見込む), `_29` (妥当), `_30` (見合わせる), `_31` (余裕), and `_32` (負担). Their stems now ask for the most natural use of the target word and no longer define its meaning. The IDs and answer mapping remain intact; the builder and focused checks bind each key to the intended sentence.

For `_29`, the earlier candidate gave a second potentially acceptable use of 妥当. The dictionary entry for 妥当 lists 妥当する as a valid form, including an example with に; the revision now makes the competing option use the mismatched を object particle, removes a missing-complement construction, and explains the distinction accurately. See [Digital Daijisen / 精選版 日本国語大辞典: 妥当](https://kotobank.jp/word/%E5%A6%A5%E5%BD%93-93764). `_31` now uses recognizable particle and attributive-form near misses rather than semantically unrelated sentences. The remaining distractors in these items still need blind review for difficulty and naturalness; no native-speaker certification is claimed.

## M11–M13 Reading audit

All 51 candidate items were checked for passage/question alignment, inferential demand, option plausibility, and Japanese naturalness. The scope is exactly:

- M11: `N2_11_M10_01–05`, `N2_11_M11_01–09`, `N2_11_M13_01–03`
- M12: `N2_12_M10_01–05`, `N2_12_M11_01–09`, `N2_12_M13_01–03`
- M13: `N2_13_M10_01–05`, `N2_13_M11_01–09`, `N2_13_M13_01–03`

Question stems/options were substantively revised for 35 items: M11 `M10_01–05`, `M11_01–09`, `M13_01–03`; M12 `M11_01–09`, `M13_01–03`; M13 `M10_03`, `M11_03`, `M11_07–09`, `M13_03`. The 16 other stems/options were retained after review: M12 `M10_01–05`; M13 `M10_01–02`, `M10_04–05`, `M11_01–02`, `M11_04–06`, `M13_01–02`. The `correctAnswer` option ID stayed bound to the same keyed option across the candidate-to-published comparison for every Reading item; each item still has four distinct choices.

Six short-text continuations that repeated facts or padded notices were removed: M11 `M10_03–04`, M12 `M10_02–05`. These remain answerable from the shorter notices. Other short passages keep only useful context, conditions, privacy limits, or process detail. Most short and several medium questions still test direct retrieval, which is appropriate for notice/information tasks; the medium/long sets add cause, trade-off, evidence-limit, and synthesis questions. Some distractors remain easy to eliminate because they contradict an explicit passage detail. Difficulty and discrimination have not been calibrated.

Lengths below count Unicode code points in each distinct short/medium/long passage, including headings and punctuation. Shared passages count once. The JLPT's [N2 item-purpose guide](https://jlpt.jp/e/guideline/pdf/n2_e.pdf) publishes example lengths as descriptive guidance, not cutoffs; shortness by itself was not treated as a defect.

| Mock | Type | Distinct passages | Before min / mean / max | Current candidate min / mean / max |
|---|---|---:|---:|---:|
| M11 | Short | 5 | 56 / 62.2 / 67 | 125 / 183.6 / 225 |
| M11 | Medium | 3 | 238 / 242.0 / 250 | 387 / 407.3 / 421 |
| M11 | Long | 3 | 283 / 314.3 / 343 | 601 / 618.3 / 629 |
| M12 | Short | 5 | 67 / 75.8 / 79 | 104 / 132.8 / 206 |
| M12 | Medium | 3 | 218 / 246.0 / 263 | 385 / 390.7 / 400 |
| M12 | Long | 1 | 516 / 516.0 / 516 | 731 / 731.0 / 731 |
| M13 | Short | 5 | 92 / 99.4 / 107 | 182 / 199.8 / 209 |
| M13 | Medium | 9 | 152 / 163.3 / 173 | 342 / 365.0 / 384 |
| M13 | Long | 1 | 469 / 469.0 / 469 | 672 / 672.0 / 672 |

Several mid-size/long passages remain shorter than the JLPT example scales, especially M13 medium and M11 long. They were kept concise where the decision chain was complete rather than expanded to a target count. Japanese text was reviewed editorially in this pass only; no independent language panel or native-speaker sign-off is available.

## M11 STAR audit

The five items `N2_11_M8_01–05` each display four actual fragment slots and one ★ in slot three. Structural enumeration confirms 24 possible fragment permutations per item, and the authored order reconstructs the complete stem sentence with the keyed fragment at ★. Manual order review found no competing order that preserves both grammar and the stated context, but enumeration is not semantic certification and no independent reviewer confirmed this judgment.

The duplicated invoice scenario is gone: `_01` concerns invoice-content verification; `_03` now concerns checking facts internally before responding to a partner; `_04` concerns mismatched application and source-document figures. The current candidate E2E rendered all five STAR items. No STAR source change was needed in this checkpoint.

## Fresh review packet and provenance

A new key-free, item-fingerprinted packet is available at [`PHASE_7_1_FRESH_REVIEW_PACKET_20261022.json`](PHASE_7_1_FRESH_REVIEW_PACKET_20261022.json). It contains 51 Reading items, five M11 STAR items, and five M14 Usage items. SHA-256: `3415c73ccea8d24a4440b6885c7f02c8d73792b5189198484c4aeb21be278802`. Per-source SHA-256 values and per-question content fingerprints are embedded in the packet. The packet passed the repository's sealed-item purity check.

**Independent review: PENDING.** No independent reviewer was available in this run; no packet was represented as reviewed, no reviewer response was created, and no consensus was fabricated. The historic packets/responses remain untouched. The packet is prepared for a future reviewer, not evidence of review.

## Tests and browser evidence

- Focused M14 authoring tests: `python -m pytest -q scripts/tests/test_n2_mock_14_draft_authoring.py` — **5 passed**.
- Focused Phase 7.1 candidate tests: `python -m unittest scripts.tests.test_phase_71_candidate_content` — **3 passed**. They cover all 51 IDs/keys, all 35 option revisions, and M11 STAR slot/key reconstruction.
- Complete local pytest regression: **214 passed** using `pytest` scoped to `scripts/tests` and a workspace-local temp directory.
- Local CI-equivalent unittest discovery: **209 passed** using the same `unittest discover -s scripts/tests` discovery as CI, with a workspace-local temp directory.
- Hosted baseline reconciliation: Actions run [39726575918](https://github.com/Phuchello/JP-STUDY/actions/runs/39726575918), commit `c830f3a`, ran `python -m unittest discover -s scripts/tests` and recorded **206 passed**. The earlier local **210** was the pytest count at that baseline: 206 unittest methods plus four pytest-style functions in `test_n2_mock_14_draft_authoring.py`. This checkpoint adds one more pytest-style M14 test and three unittest candidate tests, so current local totals are 214 pytest / 209 unittest. The counts differ by discovery method and added tests, not by four failing CI tests.
- Candidate Chromium E2E: [`PHASE_7_1_CANDIDATE_E2E_REPORT.json`](PHASE_7_1_CANDIDATE_E2E_REPORT.json), SHA-256 `68436263ec075dbc0144abf606e14a835bd510ecbc0c488f06fc1dd96f2739d0`. It injected current authoring candidates into the local practice engine, rendered 61 target items (M11 22, M12 17, M13 17, M14 Usage 5), and ran synthetic section-1 answers on each 75-item fixture: 73/75, one wrong, one unanswered, 75 review cards, feedback present, no horizontal overflow at 390px, and zero browser page errors. This is local interaction evidence only; it is not a live-site check or audio playback check.
- `python -m py_compile` passed for changed Python sources and tests. After regenerating `FILE_INDEX.md` and `MANIFEST.json`, `python scripts/validate_release.py` passed **28/28** public-snapshot integrity checks (file inventory, hash/size, statuses, relative links, and privacy heuristics); this does not certify language quality or release readiness.

A broad repository-root `pytest --collect-only -q` is not the regression command: it hits an archived helper, `archive/source-scripts/jlpt-phase3/fix_edge_test.py`, that executes on import and references the absent `test_edge_flows.cjs`. An initial scoped pytest run also hit 27 `PermissionError` failures because the sandbox denied writes to its default temp path outside the workspace. Both limits were isolated; reruns with tests scoped to `scripts/tests` and temp data inside ignored `tmp/phase7/` passed. The generated `qa/CI_QA_SUMMARY.json` timestamp was restored after test execution so historical CI evidence stayed unchanged.

## Release gate decision

**BLOCKED — do not publish M14 or promote these candidate revisions to the active bank.** Required current-version independent content review is pending. No official linguistic certification or psychometric calibration exists. Separately, M14 TTS authorization evidence and public redistribution rights remain unresolved; this checkpoint performed no TTS or audio operation. The candidate E2E and tests establish local software/content binding only. They do not establish live deployment, public access, official JLPT equivalence, or release readiness.
