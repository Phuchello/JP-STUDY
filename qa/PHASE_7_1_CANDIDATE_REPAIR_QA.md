# Phase 7.1 — candidate content and technical QA

**Snapshot date:** 2026-10-22

**Starting commit:** `2e9e93fe75e815734704846c99876c0ec8406de7`
**Status:** `QA_PENDING`; revised M11–M14 candidates are not active-bank or catalog releases.

## Scope and source guidance

This checkpoint changes the tracked authoring sources, not the published exam JSON or browser bank. The official [JLPT N2 item-purpose guide](https://jlpt.jp/e/guideline/pdf/n2_e.pdf) describes example scales of about 200 Japanese characters for short passages, 500 for mid-size passages, 900 for long passages, 600 total for integrated reading, and 700 for information retrieval. These are descriptions, not cutoffs or a calibration rubric. The [official practice workbook page](https://www.jlpt.jp/e/samples/sampleindex.html) also warns that specified N2 reading and listening material includes third-party works; no official passage or audio was copied here.

## Reading candidate changes

Lengths below count Unicode code points in each distinct short/medium/long passage (shared passages counted once), including punctuation and headings. They are internal comparisons only.

| Mock | Type | Distinct passages | Before min / mean / max | Candidate min / mean / max |
|---|---|---:|---:|---:|
| M11 | Short | 5 | 56 / 62.2 / 67 | 206 / 215.6 / 225 |
| M11 | Medium | 3 | 238 / 242.0 / 250 | 387 / 407.3 / 421 |
| M11 | Long | 3 | 283 / 314.3 / 343 | 601 / 618.3 / 629 |
| M12 | Short | 5 | 67 / 75.8 / 79 | 189 / 199.8 / 209 |
| M12 | Medium | 3 | 218 / 246.0 / 263 | 385 / 390.7 / 400 |
| M12 | Long | 1 | 516 / 516.0 / 516 | 731 / 731.0 / 731 |
| M13 | Short | 5 | 92 / 99.4 / 107 | 182 / 199.8 / 209 |
| M13 | Medium | 9 | 152 / 163.3 / 173 | 342 / 365.0 / 384 |
| M13 | Long | 1 | 469 / 469.0 / 469 | 672 / 672.0 / 672 |

Across the three mocks, 51 Reading items changed: 17 per mock (all short, medium, and long item IDs). This is 35 distinct passages; 12 integrated/comparative and information-retrieval items were reviewed and left unchanged. M11 has 8 items with rewritten stems, option sets, and rationales; 24 distractor texts were replaced. Their answer letters did not change. The M11 invoice-comparison overlap was removed by changing `N2_11_M8_03` to a separate internal fact-checking scenario.

The edits add meaningful context, counter-considerations, process details, evidence limits, or decision criteria. M11 now explains why checklists, meeting preparation, failure reporting, and staged process automation matter. M12 adds trade-offs and evaluation limits to food-waste, rural transport, library, and river-planning texts. M13 adds practical constraints and uncertainty to technology and research topics. Length alone does not establish N2 difficulty. Several candidate mid-size and long passages remain shorter than the guide's approximate examples, especially M13 medium (mean 365) and M11 long (mean 618); the passages were expanded without padding, and need independent editorial review before promotion.

## STAR integrity and rendering

- M11's five stems now show context followed by four actual arrangement positions, with one ★ at position three; the third ordered fragment matches the key. Complete reconstructed sentences preserve the stem prefix/suffix.
- M11 `N2_11_M8_03` no longer repeats the invoice-checking scenario in `N2_11_M8_01`.
- M12, M13, and M14 retain five STAR items each; all 20 current candidate items have context, four displayed slots, one ★, and four fragments.
- Strict structural checks enumerated 24 fragment orders per item (480 total). Chromium rendered 20/20 candidate STAR items correctly.

Permutation enumeration and structural rendering do not prove semantic uniqueness. No fresh independent linguistic review was available; all changed STAR content remains pending review.

Fresh key-free, fingerprint-bound packets were prepared for possible independent review and stored only under ignored `tmp/phase7/`: M11 SHA-256 `916024dd38cfebd88c77c226ef93ff7032d3d1405e3012555aacbb7c95443bca`; M12 `df19e99e7006c11d058360022afd50efa62cfd408badaa41f817dbfb12361a8d`; M13 `d87bb66e4556838baf27616b36110f4dafa0730f7055790e1ca0ec7197585514`; M14 `e21577a6e6b4c6f31b81b055988732d0a44a97e616ff5021bb8c2c3ac964117e`. Each contains 105 unique key-free items. These are inputs only; no reviewer responses or independent decisions were produced. Existing versioned review inputs and preserved raw response artifacts were not edited.

## Audio evidence

M11 and M13 manifests changed from `PLAYBACK_QA_PENDING` to `BROWSER_PLAYBACK_VERIFIED` for 30/30 tracks each, based on matching track IDs/URLs, actual files and SHA-256, and matching desktop/mobile Chromium playback receipts. M12 already had the verified status. This is technical playback evidence, not a pronunciation or native-speaker assessment.

M14 has 105 candidate questions, 105 Vietnamese explanations, and five revised Word Usage items. The user explicitly approved sending only M14 Japanese scripts/prompts/choices and minimal voice settings to Edge TTS. Thirty MP3s were generated and checked for actual file hashes, manifest and source fingerprints, full decode, duration, and desktop/mobile Chromium playback (30/30 each). The 16 choice-bearing tracks' synthesis inputs preserve the current spoken-choice order; Mondai 4 has three choices on all 11 items. Local candidate E2E passed 7/7 checks, including hidden transcripts, scoring, mistake review, 390px mobile layout, and zero browser page errors. No human acoustic/pronunciation review was performed.

The M14 MP3s and audio manifest are retained under ignored `tmp/phase7/n2_mock_14_audio_private/` and are not in the public repository snapshot. Microsoft materials do not clearly grant public redistribution rights for Edge Read Aloud output; a Microsoft moderator says there is no public documentation that explicitly addresses `edge-tts` usage rights ([Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/6032190/commercial-use-rights-for-microsoft-edge-read-alou)). The [Microsoft Services Agreement](https://www.microsoft.com/en-us/servicesagreement) reserves rights over distributing its software/services unless authorized; this does not by itself decide generated-audio rights. Rights remain unconfirmed, so this checkpoint does not publish those files.

## Validation and release state

- Full Python regression suite: **210 passed**.
- Private M11–M14 candidate builders: **4/4 passed**.
- Updated M11–M13 browser E2E: **7/7 per mock**, using synthetic QA answers; M14 local browser E2E: **7/7**.
- STAR Chromium render: **20/20 passed**.
- M14 playback receipt: [`N2_MOCK_14_AUDIO_PLAYBACK_RECEIPT.json`](N2_MOCK_14_AUDIO_PLAYBACK_RECEIPT.json).
- M14 local E2E report: [`N2_MOCK_14_E2E_REPORT.json`](N2_MOCK_14_E2E_REPORT.json).

M14 is not in the published bank or catalog. The revised M11–M13 content has not replaced the live exams. No current-version independent blind review, native-speaker review, or psychometric calibration is claimed. Public release remains blocked on current-version content review and confirmation of audio redistribution rights; CI and Pages results for this checkpoint will be reported only after push and verification.
