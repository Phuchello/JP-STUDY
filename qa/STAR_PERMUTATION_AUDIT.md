# JP-STUDY PHASE 3.7 — DYNAMIC STAR (★) TWO-GATE PERMUTATION AUDIT REPORT

## 1. EXECUTIVE SUMMARY & TWO-GATE ARCHITECTURE

- **Total Star Questions Audited**: 16 questions (N4: 6, N3: 6, N2: 4). Derived dynamically from source bank.
- **Gate 1: Structural Validation**: **16 / 16 PASS** (100% deterministic structural compliance).
  - Exactly 4 distinct chunks per item.
  - Exactly 24 permutations generated ($4! = 24$, total 384 permutations evaluated).
  - Prefix and suffix boundaries reconstructed.
  - Canonical assembled sentences verified with slot 3 chunk matching `correctAnswer`.
- **Gate 2: Semantic Uniqueness**: **16 / 16 STAR_SEMANTIC_REVIEW_PENDING**.
  - In accordance with adversarial QA standards, Gate 1 structural compliance **NEVER implies Gate 2 semantic compliance**.
  - Hardcoded non-canonical permutation rejection logic (`if qid == ... return GRAMMATICALLY_INVALID`) has been **completely eliminated**.
  - All candidate permutations without explicit human/expert panel review are marked honestly as `STAR_SEMANTIC_REVIEW_PENDING`.
- **Release Disposition for Star Items**: **`QA_REVIEW_REQUIRED (HELD_SAFE)`**.
  - Practice sets containing Star questions (`MD-N4-ORD-01`, `SK-N4-GR-01`, `SK-N3-GR-01`, `SK-N2-GR-01`, etc.) remain `CONTENT_QA_BLOCKED`.
  - Non-Star practice sets (e.g. `MD-N4-VOC-01`) remain eligible for controlled pilot.

---

## 2. STAR QUESTION AUDIT SUMMARY (16 ITEMS)

| Question ID | Level | Canonical Order (A-D) | Structural Rejections | Structurally Plausible | Defensible Alts | Gate 1 (Structural) | Gate 2 (Semantic) | Final Disposition |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `N4-GR-STAR-001` | N4 | `C -> A -> D -> B` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N4-GR-STAR-002` | N4 | `B -> C -> D -> A` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N4-GR-STAR-003` | N4 | `D -> B -> A -> C` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N4-GR-STAR-004` | N4 | `C -> D -> A -> B` | 18 | 6 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N4-GR-STAR-005` | N4 | `C -> A -> B -> D` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N4-GR-STAR-006` | N4 | `B -> D -> A -> C` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N3-GR-STAR-001` | N3 | `B -> D -> A -> C` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N3-GR-STAR-002` | N3 | `B -> A -> C -> D` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N3-GR-STAR-003` | N3 | `B -> C -> A -> D` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N3-GR-STAR-004` | N3 | `A -> D -> B -> C` | 24 | 0 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N3-GR-STAR-005` | N3 | `A -> B -> C -> D` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N3-GR-STAR-006` | N3 | `D -> B -> A -> C` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N2-GR-STAR-001` | N2 | `A -> D -> B -> C` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N2-GR-STAR-002` | N2 | `D -> C -> B -> A` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N2-GR-STAR-003` | N2 | `A -> C -> D -> B` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |
| `N2-GR-STAR-004` | N2 | `B -> A -> C -> D` | 0 | 24 | 0 | **PASS** | `STAR_SEMANTIC_REVIEW_PENDING` | `QA_REVIEW_REQUIRED (HELD_SAFE)` |

---

## 3. PROVABLE STRUCTURAL CONSTRAINTS CHECKED (GATE 1)

Gate 1 applies generic, non-question-specific morphosyntactic rules to detect provably impossible permutations:
1. **Double Case-Particle Collision**: Sequences where two non-cooccurring case particles are adjacent across chunk boundaries (e.g., `をを`, `がが`, `にを`, `でが`).
2. **Sentence-Initial Particle Violations**: Permutations where an unattached case particle begins a clause (`を`, `が`, `で`).
3. **Sentence-Terminal Open Particle Violations**: Permutations where an open case particle terminates the sentence before a final period.

---

## 4. GATE 2 SEMANTIC REVIEW POLICY

- **Zero Self-Certification**: Non-canonical permutations are NEVER assumed to be grammatically invalid simply because they differ from the author's preferred assembly.
- **Ambiguity Trap Detection**: If an independent linguistic audit discovers any defensible alternative arrangement that places a different chunk at the ★ position, the item is immediately quarantined with `AMBIGUOUS_ALTERNATIVE_FOUND`.
- **Preservation of Learning Assets**: Unresolved Star questions remain held in staging while allowing independent practice sets (such as `MD-N4-VOC-01`) to advance.
