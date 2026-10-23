# Phase 7.1 — candidate content audit and release gate

> Historical snapshot from 2026-10-22. Its counts, starting SHA, and release concerns describe that checkpoint. The final 2026-10-23 findings and current gate decision are in [`PHASE_7_1_FINAL_CLOSURE_20261023.md`](PHASE_7_1_FINAL_CLOSURE_20261023.md); this historical record is preserved unchanged below.

**Snapshot:** 2026-10-22
**Starting `HEAD` / verified remote `main`:** `46fbd3bfcbbac6f56f8ce0263ce4d85b437c9316`
**Gate:** **BLOCKED — candidate only; not approved for release**

## Scope and preservation

GitHub's commit listing verified that `origin/main` and the local starting `HEAD` were both `46fbd3bfcbbac6f56f8ce0263ce4d85b437c9316`. A local `git fetch origin main` could not complete because DNS/network access was unavailable, so the remote check used the connected GitHub integration. This checkpoint updates candidate authoring sources, focused tests, review packets/responses, and QA evidence only. It does not change `data/mock_exams/*.json`, published JS/runtime, catalog pages, audio manifests, audio files, or the active exam bank. No M15 work began. Existing sealed review inputs and historic fingerprints were not edited. The exact v2 raw response is retained under ignored local `tmp/phase71_private_review_archive/` because it contains a machine-local absolute path; the public v2 derivative changes only that path and records the raw SHA-256. Historic blind reviews do not certify the current candidate version.

No Edge TTS request, audio regeneration, playback of private M14 audio, or audio redistribution occurred in this checkpoint. The prior Phase 7 status text described previous audio work; this gate does not treat TTS authorization or public redistribution rights as resolved.

## M14 Word Usage repair

The five candidate items are `N2_14_M1_28` (見込む), `_29` (妥当), `_30` (見合わせる), `_31` (余裕), and `_32` (負担). Every stem asks for the most natural use without defining the target meaning. IDs and keyed answer text are preserved; shuffled display letters are checked against exact option text. Each item has a Vietnamese explanation for the keyed use and all three distractors.

| Item | Defect found | Candidate repair | Remaining concern |
|---|---|---|---|
| `_28` 見込む | Several wrong options treated a report, a comment, or a document as something to forecast, with generic explanations. | Distractors distinguish forecasting a future count from consulting last year's report, incorporating collected comments, and checking identity documents; the explanations name the better verbs (`参照する`, `踏まえる`, `確認する`). | v6 blind review selected the forecast sentence as unique and clear. |
| `_29` 妥当 | Previous options relied on invalid 「妥当している」「妥当を」「妥当の」 forms that could be rejected as elementary morphology. | All alternatives are grammatical sentences; the keyed choice evaluates a price after comparing estimates and effects, while the others apply 妥当 despite safety, legal-limit, or evidence defects. The Vietnamese explanation treats 妥当 as a na-adjective meaning appropriate/reasonable. | **`CONTENT_REVIEW_REQUIRED`.** v6 selected the keyed price judgment but noted the other propositions are easy to eliminate by contradiction and that 「複数の見積もりと効果を比べた」 is awkward; suggested 「見積額と期待される効果を比べた」. [Dictionary: 妥当](https://kotobank.jp/word/%E5%A6%A5%E5%BD%93-93764). |
| `_30` 見合わせる | Distractors repeated a near-identical single-source pattern and used 「だけ」 to make the missing comparison obvious. | Wrong choices now use a resident request (should be taken into account), a prior report (should be consulted), and one ID document (should be checked); the key suspends rail operations for safety. | **`CONTENT_REVIEW_REQUIRED`.** v6 selected the suspension sentence, but noted option C about the prior report and current results could imply an unstated comparison, a second sense of 見合わせる. A Japanese-language editor should resolve this. [Dictionary: 見合せ](https://kotobank.jp/word/%E8%A6%8B%E5%90%88%E3%81%9B-637014). |
| `_31` 余裕 | The earlier alternative set had a second natural use; the present set replaced it with complete sentences. | The keyed sentence uses 「時間に余裕をもって」 naturally, and each alternative is grammatically complete. | **`CONTENT_REVIEW_REQUIRED`.** v6 found the three distractors each contradict their own time, budget, or seating facts, so a learner can answer without discriminating the lexical use. 余裕 has time/space/surplus and composure senses ([Dictionary: 余裕](https://kotobank.jp/word/%E4%BD%99%E8%A3%95-655079)); a stronger natural distractor set is unresolved. |
| `_32` 負担 | Previous choices confused who bears a cost, misassigned an object particle, or applied 負担 to anxiety. | Wrong choices now treat a burden as a payment received, an invoice to mail, or a person's anxiety; explanations distinguish monetary expense, the document/amount, and emotional support from the accepted administrative burden. | v6 selected the keyed collocation 「利用者の負担を軽くする」 and found the alternatives distinguishable. [Dictionary: 負担](https://kotobank.jp/word/%E8%B2%A0%E6%8B%85-618874). |

Reference for `_28`: [Digital Daijisen / 精選版 日本国語大辞典: 見込む](https://kotobank.jp/word/%E8%A6%8B%E8%BE%BC%E3%82%80-637550) distinguishes anticipating/counting in expected results from relying on or consulting a source. None of the dictionary checks alone certifies item quality.

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

The fresh v6 key-free AI review independently selected the current answer for all 51 Reading items; a local exact-option comparison found 0 key mismatches. It found no defensible second Reading answer. It did note weaker short-reading distractors that directly reverse stated facts, plus minor wording concerns in `N2_12_M10_05` (arrival-time sentence) and `N2_13_M11_01` (the phrase “logical flow” is broader than the passage's two evaluation criteria). These remain disclosed editorial concerns; no further change was made without evidence of an answer or naturalness defect.

## M11 STAR audit

The five items `N2_11_M8_01–05` each display four actual fragment slots and one ★ in slot three. Structural enumeration confirms 24 possible fragment permutations per item, and the authored order reconstructs the complete stem sentence with the keyed fragment at ★. A fresh key-free reviewer confirmed the intended order for all five, including that no defensible alternative order remains in repaired Q04. Q04 was substantively restructured after v4 review exposed a second viable order: its current fragments bind 「申請書に記された数字が」 to 「原本の記録と一致するかどうかを」, then 「項目ごとに確かめ、」, then the discrepancy response. The key remains D. This is editorial AI review, not linguistic certification.

The duplicated invoice scenario is gone: `_01` concerns invoice-content verification; `_03` concerns checking facts internally before responding to a partner; `_04` concerns mismatched application and source-document figures. The candidate browser E2E rendered all five STAR items.

## Fresh review packet and provenance

The versioned key-free packet series is preserved at `qa/PHASE_7_1_FRESH_REVIEW_PACKET_20261022_v2.json` through `_v6.json`; each records source hashes and per-item fingerprints and passed the sealed-item purity check. The current v6 packet contains all 51 Reading items, five M11 STAR items, and five M14 Usage items, with no answer keys or explanations. Its SHA-256 is `7da03d691cc94c6f9cdbd5620ea57b1a1c4b9c8b046704a8114690b74d5ce`; it binds the current candidate source hashes and per-item fingerprints. The exporter is `scripts/curriculum/export_phase_71_candidate_packet.py`.

**Independent review: v6 completed; qualified Japanese-language review remains pending.** A separate clean AI reviewer received only the v6 key-free packet, verified its SHA-256, and returned an item-by-item review without inspecting keys, explanations, authoring source, repository, or earlier responses. The raw response is preserved at `qa/PHASE_7_1_INDEPENDENT_REVIEW_RESPONSE_20261022_v6.md`; SHA-256 `dd7be49427875f5dcdb7c946d47bc03b9ca5e1a146e34e814fddd3f5c2414331`. It reviewed all 61 questions; a local exact-option comparison against the current candidate found zero key mismatches. It confirmed the repaired M11 Q04 order and distinguished the invoice scenarios, and selected the keyed option for each M14 item. It also left the concerns above for M14 Q29–31 and minor Reading wording/discrimination. Packets v2–v5 remain unchanged; v3–v5 raw responses remain verbatim; the v2 raw response is retained locally with a public path-redacted derivative at `qa/PHASE_7_1_INDEPENDENT_REVIEW_RESPONSE_20261022_v2_PUBLIC_REDACTED.json`. The v6 review does not retroactively update older packets. This is attributable independent AI editorial review, not external human review, native-speaker certification, or JLPT psychometric validation. No consensus is claimed.

## Tests and browser evidence

- Focused M14 authoring tests: `python -m pytest -q scripts/tests/test_n2_mock_14_draft_authoring.py` — **5 passed**.
- Focused Phase 7.1 candidate tests: `python -m unittest scripts.tests.test_phase_71_candidate_content` — **4 passed**. They bind candidate QIDs, keys, revised options and rationales, and STAR reconstruction.
- Complete local pytest regression: `python -m pytest -q scripts/tests` — **215 passed, 126 subtests passed**. Complete local CI-equivalent discovery: `python -m unittest discover -s scripts/tests` — **210 tests, OK**. Both ran with `TEMP` and `TMP` pointed inside the workspace because Windows denied test fixture writes to its default sandbox temp location. The unittest suite regenerated only the timestamp in `qa/CI_QA_SUMMARY.json`; that generated timestamp was restored to preserve historical evidence.
- Hosted-count reconciliation: Actions run [39726575918](https://github.com/Phuchello/JP-STUDY/actions/runs/39726575918), commit `c830f3a`, ran exactly `python -m unittest discover -s scripts/tests` and recorded **206 tests, OK**. Current unittest discovery is 210: four unittest methods were added since that hosted run. Current pytest is 215 because pytest additionally collects five pytest-style functions. Thus the counts refer to different discovery methods and code versions; the difference does not indicate four failed hosted tests.
- Candidate Chromium E2E: [`PHASE_7_1_CANDIDATE_E2E_REPORT.json`](PHASE_7_1_CANDIDATE_E2E_REPORT.json), SHA-256 `00266f831b736ff7c68346eda8f373593fc2148d859f280f343913af2cc269b3`. It injected current authoring candidates into the local practice engine, rendered 61 target items (M11 22, M12 17, M13 17, M14 Usage 5), and ran synthetic section-1 answers on each 75-item fixture: 73/75, one wrong, one unanswered, 75 review cards, feedback present, no horizontal overflow at 390px, and zero browser page or console errors at desktop and mobile widths. Network calls were stubbed; no audio or live deployment was tested. This is local interaction and answer-feedback wiring evidence only.
- `python -m py_compile` passed for changed Python sources and tests. After regenerating `FILE_INDEX.md` and `MANIFEST.json`, `python scripts/validate_release.py` passed **28/28** public-snapshot integrity checks (file inventory, hash/size, statuses, relative links, and privacy heuristics); this does not certify language quality or release readiness.

A broad repository-root `pytest --collect-only -q` is not the regression command: it hits an archived helper, `archive/source-scripts/jlpt-phase3/fix_edge_test.py`, that executes on import and references the absent `test_edge_flows.cjs`. An initial scoped pytest run also hit 27 `PermissionError` failures because the sandbox denied writes to its default temp path outside the workspace. Reruns with tests scoped to `scripts/tests` and `TEMP`/`TMP` set to `.phase71-test-tmp` passed. The generated `qa/CI_QA_SUMMARY.json` timestamp was restored so historical CI evidence stayed unchanged.

## Release gate decision

**BLOCKED — keep these changes candidate-only.** v6 AI blind review and local validation are complete, but M14 `_31` remains too easy through factual contradictions; `_29` relies on contradiction cues and has a wording issue; `_30` option C may imply a valid comparison sense. These need focused Japanese-language editorial resolution before promotion. Human/native-speaker review and psychometric calibration are absent. M14 TTS authorization provenance and public redistribution rights remain unresolved; this checkpoint performed no TTS, audio, or private-media operation. Tests and E2E establish local structural and interaction evidence only, not linguistic certification, live deployment, official JLPT equivalence, or release readiness.
