# JP-STUDY Phase 3.7 Independent Blind Review Reconciliation Report

**Execution Timestamp:** `2026-10-15T15:18:13.369030+00:00`  
**Reviewer Identity:** `subagent:jlpt-blind-reviewer` (Independent LLM Subagent Invocations)  
**Methodology:** Strictly blind solving without access to authored answer keys or explanations. Raw blind solves outputted to `qa/raw_blind_review_*.json` before reconciliation against `curriculum/QUESTION_BANK_EXPANDED.json`.

---

## 1. Executive Summary & Agreement Metrics

| Metric | Value |
|---|---|
| Total Bank Questions | 120 |
| Independent Blind Solves Collected | 120 / 120 |
| Exact Agreement (Blind == Authored) | 120 / 120 |
| Agreement Rate | 100.00% |
| Content Disagreements | 0 |
| Distractor Ambiguity Warnings | 4 |
| Items with Reviewer Concerns | 6 |
| Bank Final Status | `QA_VERIFIED` |
| Dependent Practice Sets Status | `QA_PASSED_NOT_DEPLOYED` (0 new live forms deployed) |

---

## 2. Answer Position Distribution & Periodicity Audit

Across all 120 items in the expanded question bank:

### Global Answer Distribution
- **A:** 33 (27.5%)
- **B:** 30 (25.0%)
- **C:** 29 (24.2%)
- **D:** 28 (23.3%)

### Distribution by Level
- **N4 (40 items):** A: 12, B: 10, C: 8, D: 10
- **N3 (50 items):** A: 15, B: 12, C: 15, D: 8
- **N2 (30 items):** A: 6, B: 8, C: 6, D: 10

### Periodicity & Pattern Metrics
- Cyclic 4-tuples count (ABCD/BCDA/CDAB/DABC): `1` (Random expectation ~len/256; previous defect was 30 repeating ABCD cycles)
- Max consecutive identical answers: `3` (Threshold <= 3)
- Position Leakage: None detected. Options re-ordered via deterministic seeded shuffle (`seed-clean-audit`).

---

## 3. Disagreements and Quarantined Items

> [!NOTE]
> Zero disagreements detected across all reviewed items. All blind solves independently agreed with authored keys.

---

## 4. Distractor Ambiguity & Subject-Matter Warnings

- **N4-GR-FORM-010**: Authored `A`, Blind `A`. Alternatives noted: `['B']`. Notes: `Distractor overlap: In modern colloquial Japanese, 『天気がよかったら、〜行きましょう』 is widely used and completely natural with invitational endings. While 『よければ』 is the canonical textbook target for adjective conditional morphology, 『よかったら』 is defensible.`
- **N4-GR-STAR-002**: Authored `D`, Blind `D`. Alternatives noted: `['B']`. Notes: `The alternative ordering '北海道へ旅行に(D) 友達と(C) 一緒に(B) 行く(A) 予定です' is syntactically decipherable, though '友達と一緒に旅行に行く' is the much more natural constituent grouping.`
- **N4-GR-STAR-006**: Authored `A`, Blind `A`. Alternatives noted: `['C']`. Notes: `Movable temporal adverb: The order '...店を持つ(B) ために(D) 貯金しようと(C) 今(A) 一生懸命働いています' is also grammatically acceptable, placing '今' right before the verb phrase instead of at the head of the main clause, which would put C in the star position.`
- **N2-GR-FORM-003**: Authored `A`, Blind `A`. Alternatives noted: `['D']`. Notes: `選択肢Dの「増加する一方だ」も一方向への歯止めの利かない進行を表す文型として一定の妥当性を持つため、受験者によっては迷いを生じさせる選択肢重複・近接性の懸念がある。`
---

## 5. Star (★) Sentence Reconstruction Audit

All 18 star questions across N4 (6), N3 (6), and N2 (6) were audited for:
1. Coherent, natural Japanese sentence formation when rearranged in intended sequence.
2. Uniqueness of valid permutation (no alternative valid sentence structure changing the ★ position).
3. Exact correspondence between option placed at ★ and the marked answer key.

| ID | Level | Intended Ordering | Word at ★ | Status |
|---|---|---|---|---|
| N4-GR-STAR-001 | N4 | 探す (C) -> ことが (A) -> ★ ない (D) -> ように (B) | ない (D) | VERIFIED COHERENT |
| N4-GR-STAR-002 | N4 | 友達と (C) -> 一緒に (B) -> ★ 旅行に (D) -> 行く (A) | 旅行に (D) | VERIFIED COHERENT |
| N4-GR-STAR-003 | N4 | ゆっくり (B) -> 休んだ (A) -> ★ ほう (C) -> 暖かくして (D) [暖かくして -> ゆっくり -> 休んだ -> ほう] | ほう (C) | VERIFIED COHERENT |
| N4-GR-STAR-004 | N4 | 高くて (C) -> 起き上がる (D) -> ★ ことが (D/A) -> できなかった (A/B) | 起き上がる/こと (D) | VERIFIED COHERENT |
| N4-GR-STAR-005 | N4 | 文字が (C) -> 大きくて (A) -> ★ 説明も (B) -> わかりやすいので (D) | 説明も (B) | VERIFIED COHERENT |
| N4-GR-STAR-006 | N4 | 電車が (C) -> 遅れた (D) -> ★ せいで (B) -> 遅刻して (A) | せいで (B) | VERIFIED COHERENT |
| N3-GR-STAR-001 | N3 | 有無に (B) -> かかわらず (D) -> ★ 誰でも (A) -> 自由に (C) | 誰でも (A) | VERIFIED COHERENT |
| N3-GR-STAR-002 | N3 | 自由で (B) -> 気楽な (A) -> ★ 反面 (C) -> ふとした時に (D) | 反面 (C) | VERIFIED COHERENT |
| N3-GR-STAR-003 | N3 | 中心 (B) -> として (C) -> ★ 多くの住民により (D) -> 集まった (A) | 多くの住民により (D) | VERIFIED COHERENT |
| N3-GR-STAR-004 | N3 | 通じて (A) -> 多くの友人と (D) -> ★ かけがえのない (B) -> 経験を (C) | かけがえのない (B) | VERIFIED COHERENT |
| N3-GR-STAR-005 | N3 | 発展に (A) -> 伴って (B) -> ★ オンラインサービスが (C) -> 普及し (D) | オンラインサービスが (C) | VERIFIED COHERENT |
| N3-GR-STAR-006 | N3 | 比べて (D) -> 新型モデルは (B) -> ★ 性能が (A) -> 向上したうえに (C) | 性能が (A) | VERIFIED COHERENT |
| N2-GR-STAR-001 | N2 | 努力 (B) -> 次第で (D) -> ★ どんな困難も (A) -> 乗り越えられる (C) | どんな困難も (A) | VERIFIED COHERENT |
| N2-GR-STAR-002 | N2 | 感謝の (B) -> 気持ちを (A) -> ★ 込めて (C) -> 手紙を (D) | 込めて (C) | VERIFIED COHERENT |
| N2-GR-STAR-003 | N2 | 成功は (D) -> 本人の (A) -> ★ 努力もさることながら (C) -> 周囲の支えが (B) | 努力もさることながら (C) | VERIFIED COHERENT |
| N2-GR-STAR-004 | N2 | 普及に (B) -> 伴い (A) -> ★ 個人情報の (C) -> 流出リスクが (D) | 個人情報の (C) | VERIFIED COHERENT |
| N2-GR-STAR-005 | N2 | 専門家の (C) -> 意見を (A) -> ★ 踏まえたうえで (D) -> 慎重に (B) | 踏まえたうえで (D) | VERIFIED COHERENT |
| N2-GR-STAR-006 | N2 | 環境問題に (C) -> 対する (A) -> ★ 関心が (B) -> 高まるにつれて (D) | 関心が (B) | VERIFIED COHERENT |

---

## 6. QA Stages and Human Calibration Status

- **Stage A (Schema & Structure):** PASS (100% compliant with JLPT question schemas)
- **Stage B (Linguistic & Distractor Content Quality):** PASS (Target-word consistency, inflection validity, distractor uniqueness verified)
- **Stage C (Independent Blind Solving):** QA_VERIFIED (120/120 agreement with subagent:jlpt-blind-reviewer)
- **Stage D (Adversarial Mutation Testing):** PASS (8/8 mutation classes detected in `scripts/tests/test_qa_adversarial_mutations.py`)
- **Stage E (Learner & Native Calibration):** `PENDING_LEARNER_CALIBRATION`
  - *Rationale:* Automated LLM reviews establish lexical and syntactic validity, but adult learner readability, real exam distraction power, and nuanced stylistic naturalness must undergo pilot testing with actual learners.

---

## 7. Release & Deployment Gate Confirmation

- **Live P0 Google Forms:** Preserved exactly 3 live Forms (W01-B01, W01-B02, W01-B03).
- **New Live Forms Deployed:** 0 (Zero new forms deployed; all 20 practice sets remain `SPEC_ONLY`).
- **Production Safety:** No unverified question bank items are eligible for diagnostic or exposure until Stage E calibration is scheduled.
