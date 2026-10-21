# Phase 7 — coverage baseline and production gates

Snapshot: repository `main` at `a9228a2dc336a62b6683a847c59771ea44c7b797` (2026-10-21).

## Official format versus the JP-STUDY blueprint

The official N2 has two scored sections: Language Knowledge (Vocabulary/Grammar) and Reading, 105 minutes; Listening, 50 minutes. The item-type guide includes kanji reading, orthography, contextual expressions, paraphrases, usage, grammar selection/composition/text grammar, short/mid/long and integrated reading, information retrieval, task-based listening, key points, outline, quick response and integrated listening. The official site gives item-type purposes and samples; it does not certify this repository's exact 75/30 allocation or its internal question counts. The 75 + 30 split below is a JP-STUDY practice blueprint inherited from prior mocks, not an official item-count claim. [JLPT section and item types](https://www.jlpt.jp/e/guideline/testsections.html) · [Official sample-question caveat](https://www.jlpt.jp/e/samples/forlearners.html)

## Mocks 01–11: observed coverage and repetition

The repository baseline had ten 105-item payloads. N2-MOCK-11 now uses the same broad internal allocation: 32 vocabulary/kanji, 22 grammar, 21 reading and 30 listening items. Listening repeats the same five task families in the same 5/6/5/11/3 allocation. Reading repeats 5 short, 9 medium, 2 integrated/paired, 3 long and 2 information-retrieval questions. This makes timing and task familiarity comparable, but raises content/template repetition risk; it is not evidence that the real JLPT always uses these counts.

| Mock | Vocabulary/kanji form (32) | Grammar (22) | Reading (21) | Listening (30) | Representative observed theme / note |
|---|---|---|---|---|---|
| 01 | read 5; orthography 5; word formation 5; context 7; paraphrase 5; usage 5 | form 12; sentence order 5; text cloze 5 | short 5; medium 9; integrated 2; long 3; info 2 | task 5; point 6; outline 5; response 11; integrated 3 | Conversation silence and cultural interpretation; older taxonomy. |
| 02 | read 5; orthography 5; word formation 5; context 7; paraphrase 5; usage 5 | form 12; sentence order 5; text grammar 5 | 5/9/2/3/2 | 5/6/5/11/3 | Reading empathy and long-form reading; structure repeats 01. |
| 03 | read 5; write 5; context 12; synonym 5; usage 5 | sentence grammar 12; order 5; text grammar 5 | 5/9/2/3/2 | 5/6/5/11/3 | Remote work and concentration; language task taxonomy differs. |
| 04 | read 5; write 5; form 5; context 7; paraphrase 5; usage 5 | sentence grammar 12; order 5; text grammar 5 | 5/9/2/3/2 | 5/6/5/11/3 | Workplace AI; same broad blueprint. |
| 05 | read 5; orthography 5; form 5; context 7; synonym 5; usage 5 | sentence grammar 12; order 5; text grammar 5 | 5/9/2/3/2 | 5/6/5/11/3 | Architecture and behavioral design; repeated counts. |
| 06 | read 10; form 5; context 7; paraphrase 5; usage 5 | form 12; order 5; text grammar 5 | 5/9/2/3/2 | 5/6/5/11/3 | Procrastination; 10 reading items increase reading-form exposure. |
| 07 | read 5; orthography 5; form 5; context 7; paraphrase 5; usage 5 | form 12; order 5; text grammar 5 | 5/9/2/3/2 | 5/6/5/11/3 | Public-office and workplace listening scenarios. |
| 08 | same as 07 | same as 07 | 5/9/2/3/2 | 5/6/5/11/3 | Research ethics and lab scheduling in sampled listening. |
| 09 | same as 07 | form 12; order 5; text grammar 5 | 5/9/2/3/2 | 5/6/5/11/3 | Local services/community; paired reading replaces generic integrated label. |
| 10 | same as 07 | same as 09 | 5/9/2/3/2 | 5/6/5/11/3 | Broad public-service/workplace scenarios and evidence interpretation. |
| 11 | 5 read; 5 orthography; 5 formation; 7 context; 5 paraphrase; 5 usage | form 12; STAR 5; text grammar 5 | 5/9/2/3/2 | 5/6/5/11/3 | Workplace/professional communication; full blueprint; item-specific distractor sets differ from #01–10. |

**Limits in the source data:** Difficulty is not calibrated against candidate response statistics. Distractors have per-item rationale in later banks, but there is no consistent machine-readable distractor-strategy taxonomy across 01–10, so a defensible cross-exam count of distractor types cannot be reported. Themes above are representative samples, not exhaustive topic inventories. Several older files use different `typeId` spellings for the same task family. The next authoring bank should use a controlled topic and distractor tag vocabulary, fingerprint every item, and audit exact/near duplicates before release.

## N2-MOCK-11 observed release evidence (2026-10-21)

- **Content:** 105/105 questions have Vietnamese explanations; 75/75 Section 1 and 30/30 listening questions match the internal blueprint. Editorial difficulty is 102 accessible-N2 and 3 challenging-N2 tags; these are not calibrated candidate statistics. Section 1 answer positions are A19/B18/C20/D18; longest same-letter run is 3 (DDD), longest detected repeated short-period segment is length 6, period 3 (`DAA`). STAR answer labels are `ACCDC`; all 120 fragment permutations were retained in review evidence. The 9 focused negative-control release tests pass.
- **Review:** 105/105 exact semantic mappings match current fingerprints. Evidence is version-bound AI blind review with no portable execution attestation; there is no native-speaker or human panel certification. A minor wording/style note on M9_02 was retained after a second blind pass; neither reviewer proposed a competing answer.
- **Originality:** Compared with #01–10, 0 reading-passage 5-gram overlaps, 0 listening-script 5-gram overlaps, 0 exact distractor-set repeats and 0 audio SHA-256 repeats. Three exact stems and five near-stem hits are generic JLPT prompt frames; these are disclosed, not counted as repeated passages/scripts. The two repeated wrong-option sets initially found were repaired and the final audit reports zero.
- **Audio and runtime:** 30 original MP3s have manifest hashes and passed desktop/mobile Chromium decode and playback-progress checks (30/30); this verifies file mapping/playback, not pronunciation or prosody. Full player E2E passed with scoring, history, review/explanations, timer flow, transcript hiding and narrow viewport checks. Local automated regression: 189/189 unit tests passed after redirecting temp files into the workspace. Public catalog, full and listening routes were opened. The first CDN MP3 reached 13.063/35.584 seconds during playback. Both required jobs in [Actions run 39613376720](https://github.com/Phuchello/JP-STUDY/actions/runs/39613376720) completed successfully, including Pages deployment; the run-level API still returned `in_progress`, so that overall conclusion is left pending. Evidence: [`N2_MOCK_11_LIVE_DEPLOYMENT_RECEIPT.json`](N2_MOCK_11_LIVE_DEPLOYMENT_RECEIPT.json).

## Phase 7 gates and status

| Exam | Intended theme | Production state |
|---|---|---|
| 11 | Workplace and professional communication | `VERIFIED` deployed practice resource: 105/105 items and Vietnamese explanations, 30 MP3s, version-bound blind reconciliation, originality audit, player E2E, deep audio playback, local gates, both required Actions jobs, Pages deployment, and public routes pass. Run-level finalization remains reported as in progress. |
| 12 | Society, environment and public life | Not started; next in sequence. |
| 13 | Education, media and technology | Not started. |
| 14 | Comprehensive, higher challenge | Not started. |

Release is fail-closed: exact 105-item blueprint, unique IDs, four-option/key integrity, Vietnamese explanations and distractor rationales; key-free sealed review tied to current fingerprints; listening transcript/audio exact correspondence; 30 original TTS files with MP3 decode, SHA-256 and real browser playback; dashboard/catalog discovery and mock-specific end-to-end checks; CI green. A test being structurally complete or a generated MP3 having a hash does not imply content review or real playback. M11 is integrated locally but remains unpublished until CI, Pages and public-route checks complete.

## Checkpoint for continuation

Continue with #12 (society, environment and public life), #13 (education, media and technology), and #14 (comprehensive challenge) sequentially. Do not begin #15. #11 is a deployed practice resource; its route/audio evidence and run-level finalization caveat are recorded above.
