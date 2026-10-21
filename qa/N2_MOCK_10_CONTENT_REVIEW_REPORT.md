# N2-MOCK-10 — content and release evidence

**Local release status:** `VERIFIED` practice resource; GitHub Pages publication is pending the authorized checkpoint push and gated deployment. This is an original practice mock, not an official JLPT paper.

## Content and review

- 105 items: 32 Vocabulary/Kanji, 22 Grammar, 21 Reading, and 30 Listening; 155 minutes total.
- Current sealed blind-input SHA-256: `7dd0851b58c2039c9367aeb1c50bdbc49722787f89b44656b3dd9d6611f0eac6`.
- The independent AI blind reviewer returned 105 unique answer mappings with exact option-text matches. Reconciliation against the authored keys found 105/105 agreements, zero mismatches, and zero unresolved answer concerns. The unmodified response is retained outside the repository; its SHA-256 is recorded in `N2_MOCK_10_BLIND_REVIEW_PROVENANCE.json`.
- All five ★ items have 24 recorded candidate permutations (120 total). No permutation classified as natural or marginal changes the keyed ★ answer. M8_03 now explicitly marks the first step and refers back to the created minutes draft.
- Section 1 answer distribution: A 18, B 19, C 20, D 18.
- Independent AI review is not human/native-speaker certification, official JLPT approval, or psychometric calibration.

## Audio and platform validation

- All 30 original Japanese MP3 tracks exist, match the manifest SHA-256 values, decode, and show playback progression in desktop and 390px mobile-emulated Chromium. The receipt is `N2_MOCK_10_AUDIO_PLAYBACK_RECEIPT.json`. Playback checks do not certify pronunciation.
- The M10 browser E2E passed section timers and counts, transcript hiding, scoring, answer review, unanswered items, history persistence, Vietnamese explanations, and 390px mobile layout with zero page errors. Test responses are synthetic QA data.
- The dynamic release audit and structural validator passed all ten N2 mocks: 1,050 questions, 300 mapped MP3s, zero ID collisions, and zero duplicate stems or passages.
- Automated release tests: 165/165 unit tests, 15/15 adversarial tests, 7/7 audio-sensitive fingerprint tests, and 15/15 browser smoke flows passed.

## Scope and limitations

Listening content review used the sealed Japanese scripts/options; the separate browser receipt verifies file hashes and playback. The assessment remains a practice resource with no human/native-speaker review or psychometric calibration. Local integration is complete; public access is not claimed until GitHub Actions and the live Pages URLs are verified.
