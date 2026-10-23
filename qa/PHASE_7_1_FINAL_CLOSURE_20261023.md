# Phase 7.1 final closure and controlled release decision

> **Current update:** The candidate-only/blocked decision below predates final release integration and is superseded. Current receipt reconciliation, local test results, and release state are in [`PHASE_7_1_FINAL_RELEASE_INTEGRATION_20261023.md`](PHASE_7_1_FINAL_RELEASE_INTEGRATION_20261023.md). Hosted CI and live verification are still pending.

## Prior candidate-only closure (superseded by final integration)

**Date:** 2026-10-23
**Starting `main` / local `HEAD`:** `312b5b39f8e1d3d06548e6945a6b7f4ee7365b15`
**Scope:** M11–M13 Reading/STAR candidate closure and M14 Q29–31 Word Usage repair.
**Decision:** M11–M13 revision release **BLOCKED**; M14 remains an unreleased draft.

## A. Repository and verification

The GitHub API confirmed `origin/main` at the starting SHA above. Local `git fetch origin main` was unavailable because this environment could not resolve `github.com`; no divergent remote head was found through the authenticated GitHub connector. Only candidate sources, tests, workflow coverage, and QA documentation/evidence were changed. Published exam payloads, active-bank data, deployed JSON/JS, and audio bytes were not changed. No TTS request was made.

The starting hosted run, [Content QA & Adversarial Release Gate #41](https://github.com/Phuchello/JP-STUDY/actions/runs/39794593993), is tied to the starting SHA and completed successfully. Its hosted unittest log reports **210 tests**, not 206. After the final Q31 explanation-binding correction, the complete local pytest suite reported **217 passed, 131 subtests passed**, and unittest discovery reported **212 tests, OK**. The focused authoring/content rerun reported **11 passed, 131 subtests passed**. The first pytest invocation used Windows' default temp folder and 27 tests failed because the sandbox denied writes there; rerunning the same suite with Python's temporary directory inside the writable repo completed successfully. These are separate runs and counts; the candidate browser run described below is also separate.

The repository integrity checks passed against the unchanged released baseline: 1,365 active questions across 13 mocks; blind-remapping integrity; current M10, M11, M12 and M13 release checks; 525 question fingerprints; 15 adversarial release-guard tests; dynamic audit 13/13; and Phase 6.1 content-quality validation. These baseline passes do not certify candidate publication. Final manifest regeneration and `scripts/validate_release.py` validation completed **28/28 checks** after all closure artifacts were recorded.

Targeted local Chromium E2E used synthetic candidate fixtures and tested revised Reading IDs `N2_11_M10_01`, `N2_12_M11_01`, and `N2_13_M11_01`. For each, it selected a wrong option, confirmed the selected and another wrong option displayed their exact distinct rationales, checked the correct answer and general explanation after submission, verified there was no pre-submit answer/explanation leak, and checked 1280px desktop plus 390px mobile without horizontal overflow. All three passed, with no page or console errors. Scores were synthetic 73/75; no learner record was involved. Reproducible hashes and per-item evidence are in [`PHASE_7_1_READING_FEEDBACK_E2E_20261023.json`](PHASE_7_1_READING_FEEDBACK_E2E_20261023.json). This is local candidate-injected browser evidence, not public-site verification.

The current public site and published exam data were not changed to include these candidates, so there is no claim that revised Reading feedback was verified on the live website. The pushed source checkpoint `611b18f3056343d93e68f8289c127336e7b909bd` passed [GitHub Actions run #42](https://github.com/Phuchello/JP-STUDY/actions/runs/39945141527): the hosted full regression reported **212 unittest tests, OK**, the targeted revised-Reading Chromium step completed successfully, and the gated GitHub Pages deployment job completed successfully for `https://phuchello.github.io/JP-STUDY/`. The Pages job confirms deployment of the repository checkpoint; it does not prove that candidate questions or feedback are live, because the published exam payloads were not changed. Candidate content remains unverified on the public site.

## B. M14 Word Usage repairs

The prompts remain ordinary 用法 questions and do not define the target word. The displayed options and current keys are:

### `N2_14_M1_29` — 妥当, key A

Stem: `次の文の【妥当】の使い方として、最も自然なものはどれか。`

- A — `複数社の見積額と各案に期待される効果を比べた結果、この価格設定は妥当だと判断した。`
- B — `料理人は塩を控え、スープに妥当な味をつけて客に出した。`
- C — `新しい香水は、年代を問わず使いやすい妥当な香りが長く続く。`
- D — `会場の後方にも聞こえるよう、司会者は妥当な声で参加者に説明した。`

The previous distractors were natural sentences about decisions that seemed unreasonable; factual implausibility let test takers eliminate them without knowing the word. The revised key evaluates a pricing judgment against estimates and expected effects. B needs a sensory phrase such as `ちょうどよい味`; C needs a fragrance description such as `心地よい香り`; D needs `適切な声量` or `聞き取りやすい声`. These are collocation/semantic-category contrasts, not absurd factual claims. The Digital Daijisen definition describes 妥当 as fitting the actual circumstances and being appropriate, with examples such as a method and conclusion: [Kotobank — 妥当](https://kotobank.jp/word/%E5%A6%A5%E5%BD%93-93764).

### `N2_14_M1_30` — 見合わせる, key B

Stem: `次の文の【見合わせる】の使い方として、最も自然なものはどれか。`

- A — `係員は一枚の申請書を見合わせ、必要事項が記入されているか確かめた。`
- B — `安全を確認するため、鉄道会社は一部路線の運行を見合わせた。`
- C — `受付係は掲示された案内図を見合わせ、来場者に会場までの道を説明した。`
- D — `写真家は展望台から雲の動きを見合わせ、撮影した写真を整理した。`

The former distractor that said the photographer waited for a good shooting moment could use a dictionary-listed sense of 見合わせる. It was replaced. Digital Daijisen lists mutual looking, comparison, withholding action after considering circumstances, and awaiting an opportunity; its comparison example explicitly compares a ledger **with** an account book. The 精選版 also gives an explicit comparison target. B uses the established “suspend service” construction. A and C contain one stated object and no second comparison object; the reviewer noted that a comparison partner might be inferred from context, but did not find either as natural as B. D uses 見合わせる as if it meant simply observe one thing; `眺める` or `観察する` is natural there. No reviewer selected or defended a second answer. Sources: [Kotobank — 見合わせる](https://kotobank.jp/word/%E8%A6%8B%E5%90%88%E3%82%8F%E3%81%9B%E3%82%8B-637015) (the site’s canonical page title is 見合せる).

### `N2_14_M1_31` — 余裕, key A

Stem: `次の文の【余裕】の使い方として、最も自然なものはどれか。`

- A — `集合時刻に間に合うよう、移動時間に三十分の余裕を持たせた。`
- B — `資料の印刷で不良が出ても配れるよう、担当者は余裕を二十部多く刷った。`
- C — `参加者が増えた場合に備え、受付では余裕の名札を十枚ほど用意した。`
- D — `急な故障に備えて、技師は余裕の電池を三本用意した。`

This redesign tests the lexical distinction between an abstract margin/buffer and a spare physical item or a count of printed copies. B treats 余裕 as the thing printed; C and D use it as if it named spare name tags or batteries. More natural forms are `二十部余分に印刷する`, `予備の名札`, and `予備の電池`. The dictionary gives “more than needed” and “margin before the limit,” including money, time, and seat-capacity examples: [Kotobank — 余裕](https://kotobank.jp/word/%E4%BD%99%E8%A3%95-655079). The fresh reviewer judged A clear, while noting C and D are parallel and somewhat repetitive. That is retained as an editorial limitation; it does not create another valid reading.

The keyed option text is still bound to A/B/A after deterministic option shuffling. A final focused test also found and repaired a separate explanation-binding defect in Q31: after shuffling, the displayed print-copy distractor had received the name-tag rationale. Each wrong option now has its own correct Vietnamese explanation, and the test binds explanation to exact displayed option text. This correction did not change the learner-facing stem/options fingerprint and does not alter the reviewer input.

## C. Reading and STAR

All **51** Reading items across M11–M13 were audited for passage/question fit, inference, distractors, and Japanese naturalness. The candidate contains **36 current revision mappings**; this includes follow-up repairs to M12 `N2_12_M10_05` (road detour, departure shift, unchanged district dwell time) and M13 `N2_13_M11_01` (the keyed paraphrase now names both explicit evaluation criteria: whether beginners can follow the main points and whether explanations show their basis). That M13 item’s three option-specific Vietnamese rationales were added; the candidate now has **108** option-bound Reading distractor explanations. The established set of 105 was retained and validated; the three additional rationales correspond to that focused follow-up item. A stale-rationale mutation is rejected by the current validator.

The five M11 STAR items have all four displayed slots, reconstruct the keyed sentence at ★, and pass 24-permutation validation each (120 checks total). The duplicate invoice scenario is absent. The independent AI response for the current STAR text selects the intended third fragment for all five; Q04 is the only coherent order in the review. This does not constitute native-speaker certification.

Remaining editorial limitation: the independent Reading review described some short-reading distractors as weak because they are unrelated actions or direct reversals. The author audit found no second defensible keyed answer or current key/text mismatch, so no broad rewrite was made solely to improve stylistic preference. No unresolved substantive Reading or STAR defect was confirmed in this closure. This is an editorial assessment, not a linguistic certification.

## D. Blind review and provenance

Final clean packet: [`PHASE_7_1_FRESH_REVIEW_PACKET_20261023_v11.json`](PHASE_7_1_FRESH_REVIEW_PACKET_20261023_v11.json). SHA-256: `a2fa45738792769fe52bfe035a05155f2a322d4fa0ac829c307d8cac93963727`.

It contains only Q29–31, task/category, stem, options, and nonrevealing content fingerprints; no keys, explanations, known concerns, intended distractor logic, source hashes, or prior selections. The v10 packet is preserved unchanged but superseded because its Q30 still contained the valid “wait for opportunity” reading. The exact current fingerprints are:

| QID | Fingerprint | Blind selection |
|---|---|---|
| `N2_14_M1_29` | `704dcf862f0ce894a4e91dff8a6df71a35cbebcf690b4853e9266c4a53d84da9` | A |
| `N2_14_M1_30` | `696fed8601845c2ec7004f99f5b19f833ca2c25683ca8eb88f9b582552f91c8f` | B |
| `N2_14_M1_31` | `d0a5ac58d5d68dc0ddf3c9619589977982cecbb3b61f00e85ede9d65f58be49f` | A |

The unmodified raw response is [`PHASE_7_1_FRESH_REVIEW_RAW_20261023_v11.md`](PHASE_7_1_FRESH_REVIEW_RAW_20261023_v11.md), SHA-256 `9be97c4df021deb67d5de364f1350f9ef01fda2cd23a4b16cc9cb9491ea2c635`. Reviewer provenance and the captured concerns are in [`PHASE_7_1_FINAL_REVIEW_PROVENANCE_20261023.json`](PHASE_7_1_FINAL_REVIEW_PROVENANCE_20261023.json). Reviewer: separate Codex AI QA agent `/root/phase71_m14_final_blind_review_v11`, supplied only the clean packet. It selected A/B/A, found no defensible alternate, and noted Q29 collocation awkwardness in B–D, a weak implicit comparison inference in Q30 A/C, and repetitive C/D distractors for Q31. These findings are preserved rather than presented as unanimous linguistic consensus. This is independent AI review only; no qualified human or native-speaker review is claimed.

Earlier v2–v6 packets and reviewer-response bytes remain unchanged. The v6 full-set packet included a `knownEditorialConcern` about M14 Q31 and is not used to certify those three M14 questions. The Q29–31 result above is the clean, current-version review.

## E. Release results

| Track | Status | Evidence and blocker |
|---|---|---|
| `M11_M13_REVISION_RELEASE` | **BLOCKED** | Current exam payloads and active-bank representation are still the published versions. The candidate-specific review does not yet have a complete composite 105-row sealed/reconciliation receipt for each changed exam. M12/M13 release validators require exact current fingerprints across all 105 rows; M11’s validator is pinned to the existing sealed revision 8 and fixed revision 5–8 layers. The required gates therefore fail closed for these candidate edits. No gate was weakened and no public payload was changed. |
| `M14_CONTENT` | **READY_FOR_NEXT_GATE** | Q29–31 have corrected lexical contrasts, exact answer bindings and specific rationales; clean blind review chose A/B/A. Remaining editorial notes above are recorded. This is readiness for a later content gate, not release approval or certification. |
| `M14_PUBLIC_RELEASE` | **BLOCKED** | TTS authorization provenance and public redistribution rights for any private/generated audio remain unresolved. No TTS call, audio regeneration, or public audio manifest was made. |
| `M15` | **NOT_STARTED** | No M15 authoring or publication work was begun. |

## F. Next action

Create and validate a candidate-specific, immutable 105-row review receipt for each M11–M13 exam (including a new explicit M11 review layer) before attempting promotion. Until those existing fail-closed checks accept exact candidate fingerprints, keep all revisions candidate-only. M14 public release separately requires documented audio authorization and redistribution rights.
