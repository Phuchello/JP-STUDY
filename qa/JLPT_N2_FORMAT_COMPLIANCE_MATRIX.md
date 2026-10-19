# JLPT N2 FORMAT COMPLIANCE MATRIX & SPECIFICATION

**Document Version:** 1.0.0  
**Author:** Technical Lead & Japanese Language Assessment Specialist, JP-STUDY  
**Reference Source:** [JEES / Japan Foundation JLPT Test Sections & Guidelines](https://www.jlpt.jp/e/guideline/testsections.html)

---

## 1. Official Test Structure Overview

The official Japanese-Language Proficiency Test (JLPT) Level N2 consists of two separately timed test sections:

| Section | Content | Official Time | Official Points |
|---|---|---|---|
| **Section 1** | 言語知識（文字・語彙・文法）・読解<br>Language Knowledge (Vocabulary / Grammar) & Reading | 105 minutes | 120 scaled points<br>(0–60 Language, 0–60 Reading) |
| **Section 2** | 聴解<br>Listening Comprehension | ~50 minutes | 60 scaled points |
| **Total** | Full Examination | ~155 minutes | 180 scaled points |

### Official Scoring vs Practice Exam Reality
- **Official Scoring:** The JLPT uses Item Response Theory (IRT) scaled scoring. Raw scores (number of correct answers) are **never** multiplied by a simple linear factor. Scaled scores are statistically equated across test forms to ensure that a score of 90 represents the same level of ability regardless of form difficulty.
- **Practice Platform Reality:** Because IRT parameters require sample data from tens of thousands of real examinees, any practice platform that multiplies raw accuracy by a constant is providing an **illustrative estimate**, NOT official scaled scoring.
- **JP-STUDY Standard:** 
  1. Priority is given to transparent **raw scores** per section ($X / 54$ for Language, $X / 21$ for Reading, $X / 30$ for Listening, $X / 105$ Total) and percentages.
  2. Any 0–180 summary score must be labeled:  
     `Điểm quy đổi tham khảo của JP-STUDY — KHÔNG phải điểm chuẩn hóa JLPT chính thức.`

---

## 2. Listening Section Breakdown (聴解 50 Phút)

The official N2 Listening section contains five distinct task types (Mondai 1 to 5):

| Mondai | Japanese Title | Task Objective | Official Question Count | Test Booklet Modality | Audio Sequence | Number of Choices |
|---|---|---|---|---|---|---|
| **Mondai 1** | 課題理解<br>(Task-based Comprehension) | Understand necessary information to solve a concrete task; determine what action the character will take next. | 5 questions | 4 printed answer choices (text or illustrations). Question text is **not** printed. | 1. Situation explanation & question<br>2. Dialogue / Announcement<br>3. Question repeated | 4 choices |
| **Mondai 2** | ポイント理解<br>(Key Points Comprehension) | Understand specific details, reasons, causes, or conditions based on prior clues. | 6 questions | 4 printed answer choices. Designated reading pause (~20s in official audio). | 1. Situation explanation & question<br>2. Reading pause<br>3. Dialogue<br>4. Question repeated | 4 choices |
| **Mondai 3** | 概要理解<br>(General Outline Comprehension) | Understand the speaker's main theme, overall message, argument, or intent in a monologue/speech. | 5 questions | **Nothing printed** in booklet except question number! | 1. Situation explanation<br>2. Monologue / Speech<br>3. Question spoken<br>4. Spoken choices 1, 2, 3, 4 | 4 choices<br>(Spoken) |
| **Mondai 4** | 即時応答<br>(Quick Response) | Listen to a short utterance (greeting, request, honorific phrasing, complaint, daily conversation) and select the most appropriate response. | 11–12 questions | **Nothing printed** in booklet except question number! | 1. Short utterance spoken<br>2. Spoken choices 1, 2, 3 (with brief pause between each) | **3 choices**<br>(Spoken only) |
| **Mondai 5** | 統合理解<br>(Integrated Comprehension) | Compare, synthesize, and evaluate information from longer, complex conversations with multiple conditions/alternatives. | 3–4 questions | Printed choices on test sheet (sometimes comparison notes or flyer). | 1. Intro / Context<br>2. Long dialogue or monologue<br>3. Questions & options | 4 choices |

---

## 3. Critical Compliance Corrections for JP-STUDY N2-MOCK-01

Based on this official specification, the following structural corrections are mandated for N2-MOCK-01:

### 1. Mondai 4 Choice Count & Presentation
- **Previous Defect:** Displayed 4 written options (`A, B, C, D`), revealing the prompt utterance and responses in plaintext before audio playback.
- **Required Correction:**
  - Exactly **3 choices** (1, 2, 3 / A, B, C).
  - The utterance and all 3 choices are **spoken aloud in the audio recording**.
  - During test-taking, question stem shows no spoiler text.
  - Options appear as choice buttons without leaking the spoken text.
  - Full transcript and linguistic explanations appear only after submission in review mode.

### 2. Mondai 3 Spoken Options
- **Previous Defect:** Exposed full speech text during examination via `<details open>`.
- **Required Correction:**
  - No passage transcript visible during test.
  - Spoken options (1, 2, 3, 4) included in audio recording.

### 3. Transcript Masking
- **Previous Defect:** All 30 listening questions rendered `<details open>` containing the full dialogue transcript directly in the question passage box during active test taking!
- **Required Correction:**
  - Absolute transcript masking during active examination.
  - Replaced by a dedicated audio player with Play/Pause, timeline scrubber, and volume controls.
  - Post-submission review mode unlocks full color-coded Japanese dialogue scripts, speaker turns, Vietnamese translations, and distractor breakdowns.

### 4. Multi-Speaker Audio Production
- Every listening item must map to a playable, durable MP3 asset.
- Dialogue items must use distinct voices for male and female characters (`ja-JP-KeitaNeural` for male, `ja-JP-NanamiNeural` for female).
- Natural conversational pacing, turn-taking pauses (300–500ms), and prompt repetition.
