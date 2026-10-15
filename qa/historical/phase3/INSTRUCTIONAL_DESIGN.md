# Checkpoint 1 - design decisions

## Scope inherited and protected
All 13 source artifacts from Phases 1, 2 and 2.1 are hashed before edits. FINAL_PHASE3 is separate. Reuse the five-sheet Phase 2.1 tracker, diagnostic logic, portable tutor rules, official resource links and cautious N4→N3→N2 gates. There are no new learner diagnostic scores.

## Evidence workstreams
19 distinct Exa queries, 170 returned candidates, 166 unique URLs. Seven workstreams: memory/guidance/sleep; Japanese grammar; listening; speaking/anxiety; reading/vocabulary; short sessions; learner community. Full reads and verified DOI metadata are separately logged. Search results are discovery, not validation. Publisher metadata occasionally has incorrect author attribution in search extracts; primary pages and Crossref used for cross-checking. Crossref 429/404 is retained as a metadata limitation, not called a positive verification.

## Pilot blueprint and release gates
Target 80 original N4 objective questions plus 4 separate speaking roleplays, not official JLPT items. Categories: vocab/kanji 8; particles 10; conjugation 10; grammar choice 12; ordering 8; interpretation 6; short reading 8; medium reading 6; listening 8; practical communication 4. Foundational grammar/reading/listening receive priority; no forced N2. Target level and difficulty are pedagogical estimates, not calibrated JLPT item parameters.

Gate 1: schema completeness, unique IDs/options, immutable key digest, source concept mapping, original wording.
Gate 2: a separate content review pass with answer key hidden, followed by every distractor and passage-evidence check; resolve ambiguities before release. Document identity and limitations of reviewers accurately; no false claim of native-teacher calibration.
Gate 3: deterministic scoring tests, including invalid, skipped, partial, seen stimuli, hinted/reviewed and interrupted sessions.
Do not expand to 300–500 until pilot passes. If independent linguistic verification capacity remains insufficient, deliver a clearly bounded pilot and identify expansion gaps; never pad counts with superficial permutations.

## Item contract
ID, level, category, objective/concept ID, difficulty estimate, original stem, options, correct option, Vietnamese rationale, per-distractor rationale, error code, prerequisites, concept source URL, estimated seconds, review task; reading evidence quote; original audio script/provenance for listening. Four speaking roleplays have a separate communication rubric, no deterministic language score or fabricated pronunciation score.

## Learning versus measurement
QUICK: 3–5 items in one objective, immediate feedback; training, not independent improvement evidence. STANDARD: 8–12, unseen first then review, feedback only after submission. DEEP: 25–40 minutes, multiple skills, timed assessment with no hints/translation/answer previews. Rest is always valid. Fatigue≥4 or sleepy means rest or old-item review, no new diagnostic. No history on an exhausted day: two worked examples or rest, not a new test.

## History and adaptation
Persist exposures when presented, item answers, first-submit answers, assistance, guessed flag, active response duration, interruptions, score key version, session ID and local calendar date/timezone. Preserve unanswered separately from incorrect. Same passage/script counts as previously seen stimulus even if its second question is new. Only first unseen item AND stimulus, unassisted, unguessed, uninterrupted STANDARD/DEEP responses enter the independent-practice view. This is not an official proficiency measurement.

Start conservatively from prerequisite gaps. Review due errors, inspect hint dependence and time only with sample counts, and choose new related items to check transfer. Latency thresholds and spacing schedule 1/3/7/14 days are explicit heuristics, not validated personal optimums. No passing probability. Hold out one item per suitable objective for later unseen concept checks; report when new items run out. Same-concept new checks after a delay are delayed transfer, distinct from retaining an old item.

## Listening delivery
Original short scripts with validated text/key. Use browser Japanese speech synthesis only if a ja voice exists; label as synthetic practice, never official audio. No Japanese voice means exclude listening from scored selection and provide transcript-assisted study, with no listening credit. Do not pretend TTS is native audio or that voice availability/offline operation is universal. Official MP3 links remain for the existing external diagnostic workflow.

## Local experience and portability
No framework, account, API key or paid API. Classic JS scripts and inline/preloaded bank avoid file:// fetch restrictions. One index.html, large touch targets, keyboard choices, one question per screen, optional soft timer. localStorage is opportunistic and tested in the desktop browser; private mode/file origin can vary. Fail visibly to memory-only mode. Versioned JSON export/import, strict schema limits, merge by IDs, CSV for an added workbook import sheet. No automatic Excel writing, Gemini control or cross-device synchronization. Error package only copies text; use textarea fallback if clipboard API unavailable.

## Checkpoint milestones
1. Evidence synthesis + schema/design.
2. Reviewed pilot + scoring.
3. Adaptive selection + Gemini review.
4. Bank expansion (conditional) + existing workbook integration.
5. End-to-end tests and final report, explicitly naming the last fully validated milestone and incomplete stages.
