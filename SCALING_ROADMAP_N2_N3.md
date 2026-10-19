# JP-STUDY — STRATEGIC SCALING ROADMAP: 20 N2 & 10 N3 FULL MOCK EXAMS

**Target Scope:**  
- **JLPT N2:** 20 Full Mock Examinations (2,100 questions · 600 Neural TTS Audio Assets)  
- **JLPT N3:** 10 Full Mock Examinations (950 questions · 280 Neural TTS Audio Assets)  
- **Total Platform Bank:** **3,050 original questions · 880 studio-grade audio assets**

---

## 1. Executive Summary & Production Status

JP-STUDY operates an institutional-grade, automated examination production factory and adversarial QA gate for the Japanese-Language Proficiency Test (JLPT).

### Current Completed Baseline (Phase 4):

| Examination | Language Knowledge & Reading | Listening Comprehension | Total Questions | Audio Tracks (MP3) | Verification Status |
|:---|:---:|:---:|:---:|:---:|:---:|
| **N2-MOCK-01** | 75 items (105 min) | 30 items (50 min) | 105 items | 30 tracks | `TECHNICALLY_READY · AI_AUDITED` |
| **N2-MOCK-02** | 75 items (105 min) | 30 items (50 min) | 105 items | 30 tracks | `TECHNICALLY_READY · AI_AUDITED` |
| **N2-MOCK-03** | 75 items (105 min) | 30 items (50 min) | 105 items | 30 tracks | `TECHNICALLY_READY · AI_AUDITED` |
| **N2-MOCK-04** | 75 items (105 min) | 30 items (50 min) | 105 items | 30 tracks | `TECHNICALLY_READY · AI_AUDITED` |
| **Subtotal** | **300 items** | **120 items** | **420 items** | **120 tracks** | **100% Release Gate Pass** |

---

## 2. Examination Blueprints (Official JEES / Japan Foundation Standards)

### 2.1. JLPT N2 Standard Blueprint (105 items · 155 minutes)

#### Section 1: 言語知識・読解 (Language Knowledge & Reading — 75 items / 105 minutes)
- **Mondai 1: 漢字読み (Kanji Reading)** — 5 items
- **Mondai 2: 表記 (Orthography)** — 5 items
- **Mondai 3: 語形成 (Word Formation)** — 5 items
- **Mondai 4: 文脈規定 (Context Vocabulary)** — 7 items
- **Mondai 5: 言い換え類義 (Paraphrases)** — 5 items
- **Mondai 6: 用法 (Usage)** — 5 items
- **Mondai 7: 文法形式の判断 (Grammar Forms)** — 12 items
- **Mondai 8: 文の組み立て ★ (Star Sentence Composition)** — 5 items ($4! = 24$ permutations verified)
- **Mondai 9: 文章の文法 (Text Grammar)** — 5 items
- **Mondai 10: 短文読解 (Short Passages)** — 5 items
- **Mondai 11: 中文読解 (Medium Passages)** — 9 items (3 passages $\times$ 3 items)
- **Mondai 12: 統合理解 (Comparative Reading)** — 2 items (1 pair of passages $\times$ 2 items)
- **Mondai 13: 長文読解 (Thematic Long Passage)** — 3 items (1 passage $\times$ 3 items)
- **Mondai 14: 情報検索 (Information Retrieval)** — 2 items (1 flyer/notice $\times$ 2 items)

#### Intermission Break: 10 minutes (Countdown timer, auto-saved Section 1 draft)

#### Section 2: 聴解 (Listening Comprehension — 30 items / 50 minutes)
- **Mondai 1: 課題理解 (Task-Based Comprehension)** — 5 items (4 options)
- **Mondai 2: ポイント理解 (Key Points Comprehension)** — 6 items (4 options, 6-second reading pause)
- **Mondai 3: 概要理解 (General Outline / Gist)** — 5 items (4 spoken options)
- **Mondai 4: 即時応答 (Quick Response)** — 11 items (**STRICTLY 3 SPOKEN CHOICES: `1番`, `2番`, `3番`**)
- **Mondai 5: 統合理解 (Integrated Comprehension)** — 3 items (Scenario 1: 2 items, Scenario 2: 1 item)

---

### 2.2. JLPT N3 Standard Blueprint (95 items · 140 minutes)

#### Section 1: 言語知識 (Language Knowledge: Vocab & Grammar) & 読解 (Reading) — 67 items / 100 minutes
- **Kanji Reading & Orthography:** 14 items
- **Context Vocabulary & Paraphrases:** 15 items
- **Usage:** 6 items
- **Grammar Forms & Star Arrangements:** 18 items
- **Text Grammar:** 4 items
- **Reading Comprehension (Short, Mid, Long, Info):** 10 items

#### Section 2: 聴解 (Listening Comprehension — 28 items / 40 minutes)
- **Mondai 1: 課題理解:** 6 items
- **Mondai 2: ポイント理解:** 6 items
- **Mondai 3: 概要理解:** 3 items
- **Mondai 4: 発話表現 (Utterance Expression):** 4 items (3 spoken choices)
- **Mondai 5: 即時応答 (Quick Response):** 9 items (3 spoken choices)

---

## 3. The Industrial Content & QA Production Pipeline

Every single new exam produced undergoes the following 6-step lifecycle before release:

```
[Step 1: Authoring]
  ├── Bank data creation: n2_mock_XX_data.py (75 Sec 1 items)
  ├── Listening script: n2_mock_XX_listening.py (30 Sec 2 items)
  └── Non-boilerplate distractor rationale & pedagogical Vietnamese explanations
         │
[Step 2: Neural Synthesis]
  ├── Multi-character Neural TTS (ja-JP-NanamiNeural & ja-JP-KeitaNeural)
  ├── Silence cues: 0.8s intro, 6.0s reading pause, 0.4s turns, 1.5s post-item
  └── Manifest generation with SHA-256 and ffprobe durations
         │
[Step 3: Cryptographic Fingerprinting]
  ├── Canonical SHA-256 question fingerprinting: {id, typeId, stem, passage, options, audioUrl}
  └── Guaranteed immutability: any edit invalidates previous review
         │
[Step 4: Independent Blind Review]
  ├── Blind export: qa/blind_items_mXX_*.json (zero answers/explanations)
  ├── Independent Japanese linguistic solving by autonomous AI reviewers
  └── Semantic remapping & reconciliation against authored keys
         │
[Step 5: Chromium Playwright Verification]
  ├── Real browser headless decoding & playback (timeupdate > 0.05s)
  ├── Desktop (1280x800) and Mobile (390x844) viewport parity
  └── Signed cryptographic playback receipt: qa/N2_MOCK_XX_AUDIO_PLAYBACK_RECEIPT.json
         │
[Step 6: Release Gate & Fail-Closed CI/CD]
  ├── Uniqueness check across all exams (zero stem, passage, or ID collisions)
  ├── Adversarial negative mutation tests (13 test cases)
  ├── Machine-readable summary: qa/CI_QA_SUMMARY.json
  └── GitHub Actions deployment strictly blocked on gate status == "PASS"
```

---

## 4. Phased Delivery Roadmap

```
Phase 4 (CURRENT):
  ✅ N2-MOCK-01, N2-MOCK-02, N2-MOCK-03, N2-MOCK-04 (420 questions, 120 audio)
  ✅ Complete fail-closed CI/CD and deployment gating

Phase 5:
  🎯 N2-MOCK-05 to N2-MOCK-08 (420 new questions, 120 new audio)
  🎯 N3-MOCK-01 to N3-MOCK-03 (285 new questions, 84 new audio)
  Milestone: 1,125 total questions · 324 audio tracks

Phase 6:
  🎯 N2-MOCK-09 to N2-MOCK-12 (420 new questions, 120 new audio)
  🎯 N3-MOCK-04 to N3-MOCK-06 (285 new questions, 84 new audio)
  Milestone: 1,830 total questions · 528 audio tracks

Phase 7:
  🎯 N2-MOCK-13 to N2-MOCK-16 (420 new questions, 120 new audio)
  🎯 N3-MOCK-07 to N3-MOCK-08 (190 new questions, 56 new audio)
  Milestone: 2,440 total questions · 704 audio tracks

Phase 8:
  🎯 N2-MOCK-17 to N2-MOCK-20 (420 new questions, 120 new audio)
  🎯 N3-MOCK-09 to N3-MOCK-10 (190 new questions, 56 new audio)
  Milestone: 3,050 total questions · 880 audio tracks (Full Target Achieved)
```

---

## 5. Governance & Pedagogical Transparency Rules

1. **Anti-Hallucination & Provenance:** No blind solve answer may be synchronized or overwritten from the authored key. Review fingerprints must match canonical content hashes.
2. **Scoring Equivalence:** The platform prominently displays raw scores ($X/105$, $X/75$, $X/30$). Any converted scaled scores carry the mandatory notice: *'Điểm quy đổi tham khảo của JP-STUDY — KHÔNG phải điểm chuẩn hóa JLPT chính thức'*.
3. **Modality Purity:** Spoken scripts and prompts are 100% masked in active test mode, revealed only in post-test review mode.
4. **Mondai 4 Invariance:** Quick Response items must strictly present 3 spoken choices (`1番`, `2番`, `3番`) across all N2 and N3 listening examinations.
5. **Fail-Closed Release:** Any single quarantined question, missing playback receipt, or stale review immediately terminates the release pipeline and aborts deployment.
