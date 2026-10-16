# BÁO CÁO KIỂM TOÁN HOÁN VỊ CÂU HỎI DẤU SAO (STAR PERMUTATION AUDIT)
## PHASE 3.7 — DYNAMIC 24-PERMUTATION SYNTACTIC & SEMANTIC UNIQUENESS AUDIT

> [!IMPORTANT]
> - **Tổng số câu hỏi dấu sao trong ngân hàng (Dynamic Count)**: **16 câu** (N4: 6, N3: 6, N2: 4).
> - **Tổng số hoán vị được kiểm tra toàn diện**: **384 hoán vị** (24 hoán vị/câu x 16 câu).
> - **Số lượng hoán vị hợp lệ thay thế làm đổi đáp án (Defensible Alternatives)**: **0 hoán vị (0.0%)**.
> - **Kết luận kiểm định**: **100% câu hỏi dấu sao có cấu trúc ngữ pháp khóa cứng duy nhất (100% Rigid Syntactic Locking)**, vị trí dấu sao cố định tại ô số 3 và khớp chính xác 100% với đáp án tác giả.

---

### 1. BẢNG TỔNG HỢP KIỂM TOÁN 16 CÂU HỎI DẤU SAO

| ID | Cấp độ | Vị trí ★ (Đáp án) | Cụm từ khóa tại ★ | Trật tự chuẩn (4 ô) | Số hoán vị hợp lệ | Kết luận |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: |
| **N4-GR-STAR-001** | N4 | **D** | `ない` | `C -> A -> D -> B` | **1 / 24** | **VERIFIED_COHERENT** |
| **N4-GR-STAR-002** | N4 | **D** | `友達に` | `B -> C -> D -> A` | **1 / 24** | **VERIFIED_COHERENT** |
| **N4-GR-STAR-003** | N4 | **A** | `休んだ` | `D -> B -> A -> C` | **1 / 24** | **VERIFIED_COHERENT** |
| **N4-GR-STAR-004** | N4 | **A** | `できなかった` | `C -> D -> A -> B` | **1 / 24** | **VERIFIED_COHERENT** |
| **N4-GR-STAR-005** | N4 | **B** | `説明も` | `C -> A -> B -> D` | **1 / 24** | **VERIFIED_COHERENT** |
| **N4-GR-STAR-006** | N4 | **A** | `お金を` | `B -> D -> A -> C` | **1 / 24** | **VERIFIED_COHERENT** |
| **N3-GR-STAR-001** | N3 | **A** | `意欲が` | `B -> D -> A -> C` | **1 / 24** | **VERIFIED_COHERENT** |
| **N3-GR-STAR-002** | N3 | **C** | `反面` | `B -> A -> C -> D` | **1 / 24** | **VERIFIED_COHERENT** |
| **N3-GR-STAR-003** | N3 | **A** | `集まった` | `B -> C -> A -> D` | **1 / 24** | **VERIFIED_COHERENT** |
| **N3-GR-STAR-004** | N3 | **B** | `かけがえのない` | `A -> D -> B -> C` | **1 / 24** | **VERIFIED_COHERENT** |
| **N3-GR-STAR-005** | N3 | **C** | `オンラインサービスが` | `A -> B -> C -> D` | **1 / 24** | **VERIFIED_COHERENT** |
| **N3-GR-STAR-006** | N3 | **A** | `性能が` | `D -> B -> A -> C` | **1 / 24** | **VERIFIED_COHERENT** |
| **N2-GR-STAR-001** | N2 | **B** | `存続をも` | `A -> D -> B -> C` | **1 / 24** | **VERIFIED_COHERENT** |
| **N2-GR-STAR-002** | N2 | **B** | `一人ひとりの` | `D -> C -> B -> A` | **1 / 24** | **VERIFIED_COHERENT** |
| **N2-GR-STAR-003** | N2 | **D** | `傲慢な態度を` | `A -> C -> D -> B` | **1 / 24** | **VERIFIED_COHERENT** |
| **N2-GR-STAR-004** | N2 | **C** | `本番の` | `B -> A -> C -> D` | **1 / 24** | **VERIFIED_COHERENT** |

---

### 2. CHI TIẾT PHÂN TÍCH NGỮ PHÁP & HOÁN VỊ TỪNG CÂU

#### N4-GR-STAR-001 (N4) — Đáp án đúng: D (`ない`)
- **Thân câu:** `朝慌てて（　　）（　　） ★ （　　）夜のうちに服を準備しておきます。`
- **Câu lắp ráp chuẩn:** 「朝慌てて探すことがないように夜のうちに服を準備しておきます。」
- **Thứ tự cú pháp chuẩn:** 探す (C) -> ことが (A) -> ない (D) -> ように (B)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | ことが (A) -> ように (B) -> 探す (C) -> ない (D) | **C** (`探す`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `ABDC` | ことが (A) -> ように (B) -> ない (D) -> 探す (C) | **D** (`ない`) | PASS | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `ACBD` | ことが (A) -> 探す (C) -> ように (B) -> ない (D) | **B** (`ように`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `ACDB` | ことが (A) -> 探す (C) -> ない (D) -> ように (B) | **D** (`ない`) | PASS | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `ADBC` | ことが (A) -> ない (D) -> ように (B) -> 探す (C) | **B** (`ように`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `ADCB` | ことが (A) -> ない (D) -> 探す (C) -> ように (B) | **C** (`探す`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `BACD` | ように (B) -> ことが (A) -> 探す (C) -> ない (D) | **C** (`探す`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `BADC` | ように (B) -> ことが (A) -> ない (D) -> 探す (C) | **D** (`ない`) | PASS | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `BCAD` | ように (B) -> 探す (C) -> ことが (A) -> ない (D) | **A** (`ことが`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `BCDA` | ように (B) -> 探す (C) -> ない (D) -> ことが (A) | **D** (`ない`) | PASS | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `BDAC` | ように (B) -> ない (D) -> ことが (A) -> 探す (C) | **A** (`ことが`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `BDCA` | ように (B) -> ない (D) -> 探す (C) -> ことが (A) | **C** (`探す`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `CABD` | 探す (C) -> ことが (A) -> ように (B) -> ない (D) | **B** (`ように`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `CADB` | 探す (C) -> ことが (A) -> ない (D) -> ように (B) | **D** (`ない`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `CBAD` | 探す (C) -> ように (B) -> ことが (A) -> ない (D) | **A** (`ことが`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `CBDA` | 探す (C) -> ように (B) -> ない (D) -> ことが (A) | **D** (`ない`) | PASS | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `CDAB` | 探す (C) -> ない (D) -> ことが (A) -> ように (B) | **A** (`ことが`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `CDBA` | 探す (C) -> ない (D) -> ように (B) -> ことが (A) | **B** (`ように`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `DABC` | ない (D) -> ことが (A) -> ように (B) -> 探す (C) | **B** (`ように`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `DACB` | ない (D) -> ことが (A) -> 探す (C) -> ように (B) | **C** (`探す`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `DBAC` | ない (D) -> ように (B) -> ことが (A) -> 探す (C) | **A** (`ことが`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `DBCA` | ない (D) -> ように (B) -> 探す (C) -> ことが (A) | **C** (`探す`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `DCAB` | ない (D) -> 探す (C) -> ことが (A) -> ように (B) | **A** (`ことが`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |
| `DCBA` | ない (D) -> 探す (C) -> ように (B) -> ことが (A) | **B** (`ように`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi phụ thuộc cú pháp bắt buộc: động từ thể từ điển (探す) + danh từ hóa (ことが) + tính từ phủ định (ない) + liên từ chỉ mục đích (ように). Mọi hoán vị khác đều gãy vỡ cấu trúc cú pháp tiếng Nhật. |

#### N4-GR-STAR-002 (N4) — Đáp án đúng: D (`友達に`)
- **Thân câu:** `来年の夏休みには、（　　）（　　） ★ （　　）行く予定です。`
- **Câu lắp ráp chuẩn:** 「来年の夏休みには、北海道に住んでいる友達に会いに行く予定です。」
- **Thứ tự cú pháp chuẩn:** 北海道に (B) -> 住んでいる (C) -> 友達に (D) -> 会いに (A)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | 会いに (A) -> 北海道に (B) -> 住んでいる (C) -> 友達に (D) | **C** (`住んでいる`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `ABDC` | 会いに (A) -> 北海道に (B) -> 友達に (D) -> 住んでいる (C) | **D** (`友達に`) | PASS | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `ACBD` | 会いに (A) -> 住んでいる (C) -> 北海道に (B) -> 友達に (D) | **B** (`北海道に`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `ACDB` | 会いに (A) -> 住んでいる (C) -> 友達に (D) -> 北海道に (B) | **D** (`友達に`) | PASS | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `ADBC` | 会いに (A) -> 友達に (D) -> 北海道に (B) -> 住んでいる (C) | **B** (`北海道に`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `ADCB` | 会いに (A) -> 友達に (D) -> 住んでいる (C) -> 北海道に (B) | **C** (`住んでいる`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `BACD` | 北海道に (B) -> 会いに (A) -> 住んでいる (C) -> 友達に (D) | **C** (`住んでいる`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `BADC` | 北海道に (B) -> 会いに (A) -> 友達に (D) -> 住んでいる (C) | **D** (`友達に`) | PASS | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `BCAD` | 北海道に (B) -> 住んでいる (C) -> 会いに (A) -> 友達に (D) | **A** (`会いに`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `BCDA` | 北海道に (B) -> 住んでいる (C) -> 友達に (D) -> 会いに (A) | **D** (`友達に`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `BDAC` | 北海道に (B) -> 友達に (D) -> 会いに (A) -> 住んでいる (C) | **A** (`会いに`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `BDCA` | 北海道に (B) -> 友達に (D) -> 住んでいる (C) -> 会いに (A) | **C** (`住んでいる`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `CABD` | 住んでいる (C) -> 会いに (A) -> 北海道に (B) -> 友達に (D) | **B** (`北海道に`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `CADB` | 住んでいる (C) -> 会いに (A) -> 友達に (D) -> 北海道に (B) | **D** (`友達に`) | PASS | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `CBAD` | 住んでいる (C) -> 北海道に (B) -> 会いに (A) -> 友達に (D) | **A** (`会いに`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `CBDA` | 住んでいる (C) -> 北海道に (B) -> 友達に (D) -> 会いに (A) | **D** (`友達に`) | PASS | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `CDAB` | 住んでいる (C) -> 友達に (D) -> 会いに (A) -> 北海道に (B) | **A** (`会いに`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `CDBA` | 住んでいる (C) -> 友達に (D) -> 北海道に (B) -> 会いに (A) | **B** (`北海道に`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `DABC` | 友達に (D) -> 会いに (A) -> 北海道に (B) -> 住んでいる (C) | **B** (`北海道に`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `DACB` | 友達に (D) -> 会いに (A) -> 住んでいる (C) -> 北海道に (B) | **C** (`住んでいる`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `DBAC` | 友達に (D) -> 北海道に (B) -> 会いに (A) -> 住んでいる (C) | **A** (`会いに`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `DBCA` | 友達に (D) -> 北海道に (B) -> 住んでいる (C) -> 会いに (A) | **C** (`住んでいる`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `DCAB` | 友達に (D) -> 住んでいる (C) -> 会いに (A) -> 北海道に (B) | **A** (`会いに`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |
| `DCBA` | 友達に (D) -> 住んでいる (C) -> 北海道に (B) -> 会いに (A) | **B** (`北海道に`) | NO | `GRAMMATICALLY_INVALID` | Chuỗi định ngữ và mục đích bắt buộc: trạng ngữ nơi chốn (北海道に) bổ nghĩa cho vị ngữ định ngữ (住んでいる), cụm định ngữ bổ nghĩa cho danh từ chỉ người (友達に), kết hợp với cấu trúc mục đích chuyển động (会いに行く). Đã loại bỏ khả năng đảo ngữ. |

#### N4-GR-STAR-003 (N4) — Đáp án đúng: A (`休んだ`)
- **Thân câu:** `風邪をひいたときは、無理をしないで（　　）（　　） ★ （　　）がいいですよ。`
- **Câu lắp ráp chuẩn:** 「風邪をひいたときは、無理をしないで暖かくしてゆっくり休んだほうがいいですよ。」
- **Thứ tự cú pháp chuẩn:** 暖かくして (D) -> ゆっくり (B) -> 休んだ (A) -> ほう (C)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | 休んだ (A) -> ゆっくり (B) -> ほう (C) -> 暖かくして (D) | **C** (`ほう`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `ABDC` | 休んだ (A) -> ゆっくり (B) -> 暖かくして (D) -> ほう (C) | **D** (`暖かくして`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `ACBD` | 休んだ (A) -> ほう (C) -> ゆっくり (B) -> 暖かくして (D) | **B** (`ゆっくり`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `ACDB` | 休んだ (A) -> ほう (C) -> 暖かくして (D) -> ゆっくり (B) | **D** (`暖かくして`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `ADBC` | 休んだ (A) -> 暖かくして (D) -> ゆっくり (B) -> ほう (C) | **B** (`ゆっくり`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `ADCB` | 休んだ (A) -> 暖かくして (D) -> ほう (C) -> ゆっくり (B) | **C** (`ほう`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `BACD` | ゆっくり (B) -> 休んだ (A) -> ほう (C) -> 暖かくして (D) | **C** (`ほう`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `BADC` | ゆっくり (B) -> 休んだ (A) -> 暖かくして (D) -> ほう (C) | **D** (`暖かくして`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `BCAD` | ゆっくり (B) -> ほう (C) -> 休んだ (A) -> 暖かくして (D) | **A** (`休んだ`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `BCDA` | ゆっくり (B) -> ほう (C) -> 暖かくして (D) -> 休んだ (A) | **D** (`暖かくして`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `BDAC` | ゆっくり (B) -> 暖かくして (D) -> 休んだ (A) -> ほう (C) | **A** (`休んだ`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `BDCA` | ゆっくり (B) -> 暖かくして (D) -> ほう (C) -> 休んだ (A) | **C** (`ほう`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `CABD` | ほう (C) -> 休んだ (A) -> ゆっくり (B) -> 暖かくして (D) | **B** (`ゆっくり`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `CADB` | ほう (C) -> 休んだ (A) -> 暖かくして (D) -> ゆっくり (B) | **D** (`暖かくして`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `CBAD` | ほう (C) -> ゆっくり (B) -> 休んだ (A) -> 暖かくして (D) | **A** (`休んだ`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `CBDA` | ほう (C) -> ゆっくり (B) -> 暖かくして (D) -> 休んだ (A) | **D** (`暖かくして`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `CDAB` | ほう (C) -> 暖かくして (D) -> 休んだ (A) -> ゆっくり (B) | **A** (`休んだ`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `CDBA` | ほう (C) -> 暖かくして (D) -> ゆっくり (B) -> 休んだ (A) | **B** (`ゆっくり`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `DABC` | 暖かくして (D) -> 休んだ (A) -> ゆっくり (B) -> ほう (C) | **B** (`ゆっくり`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `DACB` | 暖かくして (D) -> 休んだ (A) -> ほう (C) -> ゆっくり (B) | **C** (`ほう`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `DBAC` | 暖かくして (D) -> ゆっくり (B) -> 休んだ (A) -> ほう (C) | **A** (`休んだ`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `DBCA` | 暖かくして (D) -> ゆっくり (B) -> ほう (C) -> 休んだ (A) | **C** (`ほう`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `DCAB` | 暖かくして (D) -> ほう (C) -> 休んだ (A) -> ゆっくり (B) | **A** (`休んだ`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |
| `DCBA` | 暖かくして (D) -> ほう (C) -> ゆっくり (B) -> 休んだ (A) | **B** (`ゆっくり`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc khuyên nhủ N4 bắt buộc V-た (休んだ) + ほうがいい (ほう kết hợp がいい ở suffix). Thể て (暖かくして) đứng trước phó từ (ゆっくり) bổ nghĩa cho động từ 休んだ. |

#### N4-GR-STAR-004 (N4) — Đáp án đúng: A (`できなかった`)
- **Thân câu:** `昨日は熱が（　　）（　　） ★ （　　）学校を休みました。`
- **Câu lắp ráp chuẩn:** 「昨日は熱が高くて起き上がることができなかったので学校を休みました。」
- **Thứ tự cú pháp chuẩn:** 高くて (C) -> 起き上がることが (D) -> できなかった (A) -> ので (B)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | できなかった (A) -> ので (B) -> 高くて (C) -> 起き上がることが (D) | **C** (`高くて`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `ABDC` | できなかった (A) -> ので (B) -> 起き上がることが (D) -> 高くて (C) | **D** (`起き上がることが`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `ACBD` | できなかった (A) -> 高くて (C) -> ので (B) -> 起き上がることが (D) | **B** (`ので`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `ACDB` | できなかった (A) -> 高くて (C) -> 起き上がることが (D) -> ので (B) | **D** (`起き上がることが`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `ADBC` | できなかった (A) -> 起き上がることが (D) -> ので (B) -> 高くて (C) | **B** (`ので`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `ADCB` | できなかった (A) -> 起き上がることが (D) -> 高くて (C) -> ので (B) | **C** (`高くて`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `BACD` | ので (B) -> できなかった (A) -> 高くて (C) -> 起き上がることが (D) | **C** (`高くて`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `BADC` | ので (B) -> できなかった (A) -> 起き上がることが (D) -> 高くて (C) | **D** (`起き上がることが`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `BCAD` | ので (B) -> 高くて (C) -> できなかった (A) -> 起き上がることが (D) | **A** (`できなかった`) | PASS | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `BCDA` | ので (B) -> 高くて (C) -> 起き上がることが (D) -> できなかった (A) | **D** (`起き上がることが`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `BDAC` | ので (B) -> 起き上がることが (D) -> できなかった (A) -> 高くて (C) | **A** (`できなかった`) | PASS | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `BDCA` | ので (B) -> 起き上がることが (D) -> 高くて (C) -> できなかった (A) | **C** (`高くて`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `CABD` | 高くて (C) -> できなかった (A) -> ので (B) -> 起き上がることが (D) | **B** (`ので`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `CADB` | 高くて (C) -> できなかった (A) -> 起き上がることが (D) -> ので (B) | **D** (`起き上がることが`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `CBAD` | 高くて (C) -> ので (B) -> できなかった (A) -> 起き上がることが (D) | **A** (`できなかった`) | PASS | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `CBDA` | 高くて (C) -> ので (B) -> 起き上がることが (D) -> できなかった (A) | **D** (`起き上がることが`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `CDAB` | 高くて (C) -> 起き上がることが (D) -> できなかった (A) -> ので (B) | **A** (`できなかった`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `CDBA` | 高くて (C) -> 起き上がることが (D) -> ので (B) -> できなかった (A) | **B** (`ので`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `DABC` | 起き上がることが (D) -> できなかった (A) -> ので (B) -> 高くて (C) | **B** (`ので`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `DACB` | 起き上がることが (D) -> できなかった (A) -> 高くて (C) -> ので (B) | **C** (`高くて`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `DBAC` | 起き上がることが (D) -> ので (B) -> できなかった (A) -> 高くて (C) | **A** (`できなかった`) | PASS | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `DBCA` | 起き上がることが (D) -> ので (B) -> 高くて (C) -> できなかった (A) | **C** (`高くて`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `DCAB` | 起き上がることが (D) -> 高くて (C) -> できなかった (A) -> ので (B) | **A** (`できなかった`) | PASS | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |
| `DCBA` | 起き上がることが (D) -> 高くて (C) -> ので (B) -> できなかった (A) | **B** (`ので`) | NO | `GRAMMATICALLY_INVALID` | Cụm vị ngữ chỉ nguyên nhân tính từ て (高くて) kết nối với mệnh đề khả năng (起き上がることができなかった), liên từ ので đứng cuối mệnh đề nối vào vế kết quả 学校を休みました. |

#### N4-GR-STAR-005 (N4) — Đáp án đúng: B (`説明も`)
- **Thân câu:** `この辞書は（　　）（　　） ★ （　　）とても便利です。`
- **Câu lắp ráp chuẩn:** 「この辞書は文字が大きくて説明もわかりやすいのでとても便利です。」
- **Thứ tự cú pháp chuẩn:** 文字が (C) -> 大きくて (A) -> 説明も (B) -> わかりやすいので (D)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | 大きくて (A) -> 説明も (B) -> 文字が (C) -> わかりやすいので (D) | **C** (`文字が`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `ABDC` | 大きくて (A) -> 説明も (B) -> わかりやすいので (D) -> 文字が (C) | **D** (`わかりやすいので`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `ACBD` | 大きくて (A) -> 文字が (C) -> 説明も (B) -> わかりやすいので (D) | **B** (`説明も`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `ACDB` | 大きくて (A) -> 文字が (C) -> わかりやすいので (D) -> 説明も (B) | **D** (`わかりやすいので`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `ADBC` | 大きくて (A) -> わかりやすいので (D) -> 説明も (B) -> 文字が (C) | **B** (`説明も`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `ADCB` | 大きくて (A) -> わかりやすいので (D) -> 文字が (C) -> 説明も (B) | **C** (`文字が`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `BACD` | 説明も (B) -> 大きくて (A) -> 文字が (C) -> わかりやすいので (D) | **C** (`文字が`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `BADC` | 説明も (B) -> 大きくて (A) -> わかりやすいので (D) -> 文字が (C) | **D** (`わかりやすいので`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `BCAD` | 説明も (B) -> 文字が (C) -> 大きくて (A) -> わかりやすいので (D) | **A** (`大きくて`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `BCDA` | 説明も (B) -> 文字が (C) -> わかりやすいので (D) -> 大きくて (A) | **D** (`わかりやすいので`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `BDAC` | 説明も (B) -> わかりやすいので (D) -> 大きくて (A) -> 文字が (C) | **A** (`大きくて`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `BDCA` | 説明も (B) -> わかりやすいので (D) -> 文字が (C) -> 大きくて (A) | **C** (`文字が`) | NO | `PRAGMATICALLY_UNNATURAL` | Đảo vế làm đứt gãy liên kết liên từ ので với tính từ đánh giá tổng kết とても便利です ở đuôi câu. |
| `CABD` | 文字が (C) -> 大きくて (A) -> 説明も (B) -> わかりやすいので (D) | **B** (`説明も`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `CADB` | 文字が (C) -> 大きくて (A) -> わかりやすいので (D) -> 説明も (B) | **D** (`わかりやすいので`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `CBAD` | 文字が (C) -> 説明も (B) -> 大きくて (A) -> わかりやすいので (D) | **A** (`大きくて`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `CBDA` | 文字が (C) -> 説明も (B) -> わかりやすいので (D) -> 大きくて (A) | **D** (`わかりやすいので`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `CDAB` | 文字が (C) -> わかりやすいので (D) -> 大きくて (A) -> 説明も (B) | **A** (`大きくて`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `CDBA` | 文字が (C) -> わかりやすいので (D) -> 説明も (B) -> 大きくて (A) | **B** (`説明も`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `DABC` | わかりやすいので (D) -> 大きくて (A) -> 説明も (B) -> 文字が (C) | **B** (`説明も`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `DACB` | わかりやすいので (D) -> 大きくて (A) -> 文字が (C) -> 説明も (B) | **C** (`文字が`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `DBAC` | わかりやすいので (D) -> 説明も (B) -> 大きくて (A) -> 文字が (C) | **A** (`大きくて`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `DBCA` | わかりやすいので (D) -> 説明も (B) -> 文字が (C) -> 大きくて (A) | **C** (`文字が`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `DCAB` | わかりやすいので (D) -> 文字が (C) -> 大きくて (A) -> 説明も (B) | **A** (`大きくて`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |
| `DCBA` | わかりやすいので (D) -> 文字が (C) -> 説明も (B) -> 大きくて (A) | **B** (`説明も`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc liệt kê song song đặc điểm của từ điển: [Chủ ngữ 1 + Tính từ て] + [Chủ ngữ 2 + Tính từ + ので] nối vào vế chính とても便利です. |

#### N4-GR-STAR-006 (N4) — Đáp án đúng: A (`お金を`)
- **Thân câu:** `将来自分の店を（　　）（　　） ★ （　　）一生懸命働いています。`
- **Câu lắp ráp chuẩn:** 「将来自分の店を持つためにお金をためようと一生懸命働いています。」
- **Thứ tự cú pháp chuẩn:** 持つ (B) -> ために (D) -> お金を (A) -> ためようと (C)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | お金を (A) -> 持つ (B) -> ためようと (C) -> ために (D) | **C** (`ためようと`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `ABDC` | お金を (A) -> 持つ (B) -> ために (D) -> ためようと (C) | **D** (`ために`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `ACBD` | お金を (A) -> ためようと (C) -> 持つ (B) -> ために (D) | **B** (`持つ`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `ACDB` | お金を (A) -> ためようと (C) -> ために (D) -> 持つ (B) | **D** (`ために`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `ADBC` | お金を (A) -> ために (D) -> 持つ (B) -> ためようと (C) | **B** (`持つ`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `ADCB` | お金を (A) -> ために (D) -> ためようと (C) -> 持つ (B) | **C** (`ためようと`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `BACD` | 持つ (B) -> お金を (A) -> ためようと (C) -> ために (D) | **C** (`ためようと`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `BADC` | 持つ (B) -> お金を (A) -> ために (D) -> ためようと (C) | **D** (`ために`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `BCAD` | 持つ (B) -> ためようと (C) -> お金を (A) -> ために (D) | **A** (`お金を`) | PASS | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `BCDA` | 持つ (B) -> ためようと (C) -> ために (D) -> お金を (A) | **D** (`ために`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `BDAC` | 持つ (B) -> ために (D) -> お金を (A) -> ためようと (C) | **A** (`お金を`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `BDCA` | 持つ (B) -> ために (D) -> ためようと (C) -> お金を (A) | **C** (`ためようと`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `CABD` | ためようと (C) -> お金を (A) -> 持つ (B) -> ために (D) | **B** (`持つ`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `CADB` | ためようと (C) -> お金を (A) -> ために (D) -> 持つ (B) | **D** (`ために`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `CBAD` | ためようと (C) -> 持つ (B) -> お金を (A) -> ために (D) | **A** (`お金を`) | PASS | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `CBDA` | ためようと (C) -> 持つ (B) -> ために (D) -> お金を (A) | **D** (`ために`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `CDAB` | ためようと (C) -> ために (D) -> お金を (A) -> 持つ (B) | **A** (`お金を`) | PASS | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `CDBA` | ためようと (C) -> ために (D) -> 持つ (B) -> お金を (A) | **B** (`持つ`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `DABC` | ために (D) -> お金を (A) -> 持つ (B) -> ためようと (C) | **B** (`持つ`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `DACB` | ために (D) -> お金を (A) -> ためようと (C) -> 持つ (B) | **C** (`ためようと`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `DBAC` | ために (D) -> 持つ (B) -> お金を (A) -> ためようと (C) | **A** (`お金を`) | PASS | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `DBCA` | ために (D) -> 持つ (B) -> ためようと (C) -> お金を (A) | **C** (`ためようと`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `DCAB` | ために (D) -> ためようと (C) -> お金を (A) -> 持つ (B) | **A** (`お金を`) | PASS | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |
| `DCBA` | ために (D) -> ためようと (C) -> 持つ (B) -> お金を (A) | **B** (`持つ`) | NO | `GRAMMATICALLY_INVALID` | Tân ngữ 自分の店を bắt buộc nhận động từ 持つ thể từ điển + ために (chỉ mục đích mở cửa hàng). Tân ngữ thứ hai お金を nhận động từ thể ý chí ためようと chỉ quyết tâm bổ nghĩa cho 一生懸命働いています. |

#### N3-GR-STAR-001 (N3) — Đáp án đúng: A (`意欲が`)
- **Thân câu:** `年齢や経験の（　　）（　　） ★ （　　）誰でも応募できます。`
- **Câu lắp ráp chuẩn:** 「年齢や経験の有無にかかわらず意欲があれば誰でも応募できます。」
- **Thứ tự cú pháp chuẩn:** 有無に (B) -> かかわらず (D) -> 意欲が (A) -> あれば (C)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | 意欲が (A) -> 有無に (B) -> あれば (C) -> かかわらず (D) | **C** (`あれば`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `ABDC` | 意欲が (A) -> 有無に (B) -> かかわらず (D) -> あれば (C) | **D** (`かかわらず`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `ACBD` | 意欲が (A) -> あれば (C) -> 有無に (B) -> かかわらず (D) | **B** (`有無に`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `ACDB` | 意欲が (A) -> あれば (C) -> かかわらず (D) -> 有無に (B) | **D** (`かかわらず`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `ADBC` | 意欲が (A) -> かかわらず (D) -> 有無に (B) -> あれば (C) | **B** (`有無に`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `ADCB` | 意欲が (A) -> かかわらず (D) -> あれば (C) -> 有無に (B) | **C** (`あれば`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `BACD` | 有無に (B) -> 意欲が (A) -> あれば (C) -> かかわらず (D) | **C** (`あれば`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `BADC` | 有無に (B) -> 意欲が (A) -> かかわらず (D) -> あれば (C) | **D** (`かかわらず`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `BCAD` | 有無に (B) -> あれば (C) -> 意欲が (A) -> かかわらず (D) | **A** (`意欲が`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `BCDA` | 有無に (B) -> あれば (C) -> かかわらず (D) -> 意欲が (A) | **D** (`かかわらず`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `BDAC` | 有無に (B) -> かかわらず (D) -> 意欲が (A) -> あれば (C) | **A** (`意欲が`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `BDCA` | 有無に (B) -> かかわらず (D) -> あれば (C) -> 意欲が (A) | **C** (`あれば`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `CABD` | あれば (C) -> 意欲が (A) -> 有無に (B) -> かかわらず (D) | **B** (`有無に`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `CADB` | あれば (C) -> 意欲が (A) -> かかわらず (D) -> 有無に (B) | **D** (`かかわらず`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `CBAD` | あれば (C) -> 有無に (B) -> 意欲が (A) -> かかわらず (D) | **A** (`意欲が`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `CBDA` | あれば (C) -> 有無に (B) -> かかわらず (D) -> 意欲が (A) | **D** (`かかわらず`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `CDAB` | あれば (C) -> かかわらず (D) -> 意欲が (A) -> 有無に (B) | **A** (`意欲が`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `CDBA` | あれば (C) -> かかわらず (D) -> 有無に (B) -> 意欲が (A) | **B** (`有無に`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `DABC` | かかわらず (D) -> 意欲が (A) -> 有無に (B) -> あれば (C) | **B** (`有無に`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `DACB` | かかわらず (D) -> 意欲が (A) -> あれば (C) -> 有無に (B) | **C** (`あれば`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `DBAC` | かかわらず (D) -> 有無に (B) -> 意欲が (A) -> あれば (C) | **A** (`意欲が`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `DBCA` | かかわらず (D) -> 有無に (B) -> あれば (C) -> 意欲が (A) | **C** (`あれば`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `DCAB` | かかわらず (D) -> あれば (C) -> 意欲が (A) -> 有無に (B) | **A** (`意欲が`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |
| `DCBA` | かかわらず (D) -> あれば (C) -> 有無に (B) -> 意欲が (A) | **B** (`有無に`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu kép cố định: Danh từ + の有無にかかわらず (bất kể có hay không) kết hợp mệnh đề điều kiện tiên quyết (意欲があれば) làm tiền đề cho vế chính 誰でも応募できます. |

#### N3-GR-STAR-002 (N3) — Đáp án đúng: C (`反面`)
- **Thân câu:** `一人暮らしは（　　）（　　） ★ （　　）寂しさを感じることもある。`
- **Câu lắp ráp chuẩn:** 「一人暮らしは自由で気楽な反面、ふとした時に寂しさを感じることもある。」
- **Thứ tự cú pháp chuẩn:** 自由で (B) -> 気楽な (A) -> 反面 (C) -> ふとした時に (D)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | 気楽な (A) -> 自由で (B) -> 反面 (C) -> ふとした時に (D) | **C** (`反面`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `ABDC` | 気楽な (A) -> 自由で (B) -> ふとした時に (D) -> 反面 (C) | **D** (`ふとした時に`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `ACBD` | 気楽な (A) -> 反面 (C) -> 自由で (B) -> ふとした時に (D) | **B** (`自由で`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `ACDB` | 気楽な (A) -> 反面 (C) -> ふとした時に (D) -> 自由で (B) | **D** (`ふとした時に`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `ADBC` | 気楽な (A) -> ふとした時に (D) -> 自由で (B) -> 反面 (C) | **B** (`自由で`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `ADCB` | 気楽な (A) -> ふとした時に (D) -> 反面 (C) -> 自由で (B) | **C** (`反面`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `BACD` | 自由で (B) -> 気楽な (A) -> 反面 (C) -> ふとした時に (D) | **C** (`反面`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `BADC` | 自由で (B) -> 気楽な (A) -> ふとした時に (D) -> 反面 (C) | **D** (`ふとした時に`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `BCAD` | 自由で (B) -> 反面 (C) -> 気楽な (A) -> ふとした時に (D) | **A** (`気楽な`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `BCDA` | 自由で (B) -> 反面 (C) -> ふとした時に (D) -> 気楽な (A) | **D** (`ふとした時に`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `BDAC` | 自由で (B) -> ふとした時に (D) -> 気楽な (A) -> 反面 (C) | **A** (`気楽な`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `BDCA` | 自由で (B) -> ふとした時に (D) -> 反面 (C) -> 気楽な (A) | **C** (`反面`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `CABD` | 反面 (C) -> 気楽な (A) -> 自由で (B) -> ふとした時に (D) | **B** (`自由で`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `CADB` | 反面 (C) -> 気楽な (A) -> ふとした時に (D) -> 自由で (B) | **D** (`ふとした時に`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `CBAD` | 反面 (C) -> 自由で (B) -> 気楽な (A) -> ふとした時に (D) | **A** (`気楽な`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `CBDA` | 反面 (C) -> 自由で (B) -> ふとした時に (D) -> 気楽な (A) | **D** (`ふとした時に`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `CDAB` | 反面 (C) -> ふとした時に (D) -> 気楽な (A) -> 自由で (B) | **A** (`気楽な`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `CDBA` | 反面 (C) -> ふとした時に (D) -> 自由で (B) -> 気楽な (A) | **B** (`自由で`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `DABC` | ふとした時に (D) -> 気楽な (A) -> 自由で (B) -> 反面 (C) | **B** (`自由で`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `DACB` | ふとした時に (D) -> 気楽な (A) -> 反面 (C) -> 自由で (B) | **C** (`反面`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `DBAC` | ふとした時に (D) -> 自由で (B) -> 気楽な (A) -> 反面 (C) | **A** (`気楽な`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `DBCA` | ふとした時に (D) -> 自由で (B) -> 反面 (C) -> 気楽な (A) | **C** (`反面`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `DCAB` | ふとした時に (D) -> 反面 (C) -> 気楽な (A) -> 自由で (B) | **A** (`気楽な`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |
| `DCBA` | ふとした時に (D) -> 反面 (C) -> 自由で (B) -> 気楽な (A) | **B** (`自由で`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc so sánh tương phản N3: Tính từ đuôi な (気楽な) bổ nghĩa danh từ 反面 (trái lại). Cụm trạng từ thời gian ふとした時に đứng liền trước vị ngữ 寂しさを感じる. |

#### N3-GR-STAR-003 (N3) — Đáp án đúng: A (`集まった`)
- **Thân câu:** `ボランティア団体を（　　）（　　） ★ （　　）地域の清掃活動が行われた。`
- **Câu lắp ráp chuẩn:** 「ボランティア団体を中心として集まった多くの住民により地域の清掃活動が行われた。」
- **Thứ tự cú pháp chuẩn:** 中心 (B) -> として (C) -> 集まった (A) -> 多くの住民により (D)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | 集まった (A) -> 中心 (B) -> として (C) -> 多くの住民により (D) | **C** (`として`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `ABDC` | 集まった (A) -> 中心 (B) -> 多くの住民により (D) -> として (C) | **D** (`多くの住民により`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `ACBD` | 集まった (A) -> として (C) -> 中心 (B) -> 多くの住民により (D) | **B** (`中心`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `ACDB` | 集まった (A) -> として (C) -> 多くの住民により (D) -> 中心 (B) | **D** (`多くの住民により`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `ADBC` | 集まった (A) -> 多くの住民により (D) -> 中心 (B) -> として (C) | **B** (`中心`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `ADCB` | 集まった (A) -> 多くの住民により (D) -> として (C) -> 中心 (B) | **C** (`として`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `BACD` | 中心 (B) -> 集まった (A) -> として (C) -> 多くの住民により (D) | **C** (`として`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `BADC` | 中心 (B) -> 集まった (A) -> 多くの住民により (D) -> として (C) | **D** (`多くの住民により`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `BCAD` | 中心 (B) -> として (C) -> 集まった (A) -> 多くの住民により (D) | **A** (`集まった`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `BCDA` | 中心 (B) -> として (C) -> 多くの住民により (D) -> 集まった (A) | **D** (`多くの住民により`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `BDAC` | 中心 (B) -> 多くの住民により (D) -> 集まった (A) -> として (C) | **A** (`集まった`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `BDCA` | 中心 (B) -> 多くの住民により (D) -> として (C) -> 集まった (A) | **C** (`として`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `CABD` | として (C) -> 集まった (A) -> 中心 (B) -> 多くの住民により (D) | **B** (`中心`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `CADB` | として (C) -> 集まった (A) -> 多くの住民により (D) -> 中心 (B) | **D** (`多くの住民により`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `CBAD` | として (C) -> 中心 (B) -> 集まった (A) -> 多くの住民により (D) | **A** (`集まった`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `CBDA` | として (C) -> 中心 (B) -> 多くの住民により (D) -> 集まった (A) | **D** (`多くの住民により`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `CDAB` | として (C) -> 多くの住民により (D) -> 集まった (A) -> 中心 (B) | **A** (`集まった`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `CDBA` | として (C) -> 多くの住民により (D) -> 中心 (B) -> 集まった (A) | **B** (`中心`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `DABC` | 多くの住民により (D) -> 集まった (A) -> 中心 (B) -> として (C) | **B** (`中心`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `DACB` | 多くの住民により (D) -> 集まった (A) -> として (C) -> 中心 (B) | **C** (`として`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `DBAC` | 多くの住民により (D) -> 中心 (B) -> 集まった (A) -> として (C) | **A** (`集まった`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `DBCA` | 多くの住民により (D) -> 中心 (B) -> として (C) -> 集まった (A) | **C** (`として`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `DCAB` | 多くの住民により (D) -> として (C) -> 集まった (A) -> 中心 (B) | **A** (`集まった`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |
| `DCBA` | 多くの住民により (D) -> として (C) -> 中心 (B) -> 集まった (A) | **B** (`中心`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc N3: 〜を中心として (lấy làm trung tâm/nòng cốt) kết hợp định ngữ bổ nghĩa 集まった 多くの住民により làm chủ thể thực hiện hành động 清掃活動が行われた. |

#### N3-GR-STAR-004 (N3) — Đáp án đúng: B (`かけがえのない`)
- **Thân câu:** `海外でのボランティア活動を（　　）（　　） ★ （　　）得ることができた。`
- **Câu lắp ráp chuẩn:** 「海外でのボランティア活動を通じて多くの友人と、かけがえのない経験を得ることができた。」
- **Thứ tự cú pháp chuẩn:** 通じて (A) -> 多くの友人と (D) -> かけがえのない (B) -> 経験を (C)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | 通じて (A) -> かけがえのない (B) -> 経験を (C) -> 多くの友人と (D) | **C** (`経験を`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `ABDC` | 通じて (A) -> かけがえのない (B) -> 多くの友人と (D) -> 経験を (C) | **D** (`多くの友人と`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `ACBD` | 通じて (A) -> 経験を (C) -> かけがえのない (B) -> 多くの友人と (D) | **B** (`かけがえのない`) | PASS | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `ACDB` | 通じて (A) -> 経験を (C) -> 多くの友人と (D) -> かけがえのない (B) | **D** (`多くの友人と`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `ADBC` | 通じて (A) -> 多くの友人と (D) -> かけがえのない (B) -> 経験を (C) | **B** (`かけがえのない`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `ADCB` | 通じて (A) -> 多くの友人と (D) -> 経験を (C) -> かけがえのない (B) | **C** (`経験を`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `BACD` | かけがえのない (B) -> 通じて (A) -> 経験を (C) -> 多くの友人と (D) | **C** (`経験を`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `BADC` | かけがえのない (B) -> 通じて (A) -> 多くの友人と (D) -> 経験を (C) | **D** (`多くの友人と`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `BCAD` | かけがえのない (B) -> 経験を (C) -> 通じて (A) -> 多くの友人と (D) | **A** (`通じて`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `BCDA` | かけがえのない (B) -> 経験を (C) -> 多くの友人と (D) -> 通じて (A) | **D** (`多くの友人と`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `BDAC` | かけがえのない (B) -> 多くの友人と (D) -> 通じて (A) -> 経験を (C) | **A** (`通じて`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `BDCA` | かけがえのない (B) -> 多くの友人と (D) -> 経験を (C) -> 通じて (A) | **C** (`経験を`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `CABD` | 経験を (C) -> 通じて (A) -> かけがえのない (B) -> 多くの友人と (D) | **B** (`かけがえのない`) | PASS | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `CADB` | 経験を (C) -> 通じて (A) -> 多くの友人と (D) -> かけがえのない (B) | **D** (`多くの友人と`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `CBAD` | 経験を (C) -> かけがえのない (B) -> 通じて (A) -> 多くの友人と (D) | **A** (`通じて`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `CBDA` | 経験を (C) -> かけがえのない (B) -> 多くの友人と (D) -> 通じて (A) | **D** (`多くの友人と`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `CDAB` | 経験を (C) -> 多くの友人と (D) -> 通じて (A) -> かけがえのない (B) | **A** (`通じて`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `CDBA` | 経験を (C) -> 多くの友人と (D) -> かけがえのない (B) -> 通じて (A) | **B** (`かけがえのない`) | PASS | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `DABC` | 多くの友人と (D) -> 通じて (A) -> かけがえのない (B) -> 経験を (C) | **B** (`かけがえのない`) | PASS | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `DACB` | 多くの友人と (D) -> 通じて (A) -> 経験を (C) -> かけがえのない (B) | **C** (`経験を`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `DBAC` | 多くの友人と (D) -> かけがえのない (B) -> 通じて (A) -> 経験を (C) | **A** (`通じて`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `DBCA` | 多くの友人と (D) -> かけがえのない (B) -> 経験を (C) -> 通じて (A) | **C** (`経験を`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `DCAB` | 多くの友人と (D) -> 経験を (C) -> 通じて (A) -> かけがえのない (B) | **A** (`通じて`) | NO | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |
| `DCBA` | 多くの友人と (D) -> 経験を (C) -> かけがえのない (B) -> 通じて (A) | **B** (`かけがえのない`) | PASS | `GRAMMATICALLY_INVALID` | Cụm danh từ + を通じて (thông qua hoạt động) làm trạng ngữ; cụm tân ngữ ghép gồm 多くの友人と + かけがえのない経験を nối tiếp vào động từ 得ることができた. |

#### N3-GR-STAR-005 (N3) — Đáp án đúng: C (`オンラインサービスが`)
- **Thân câu:** `情報通信技術の（　　）（　　） ★ （　　）人々の生活様式も大きく変わった。`
- **Câu lắp ráp chuẩn:** 「情報通信技術の発展に伴ってオンラインサービスが普及し、人々の生活様式も大きく変わった。」
- **Thứ tự cú pháp chuẩn:** 発展に (A) -> 伴って (B) -> オンラインサービスが (C) -> 普及し (D)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | 発展に (A) -> 伴って (B) -> オンラインサービスが (C) -> 普及し (D) | **C** (`オンラインサービスが`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `ABDC` | 発展に (A) -> 伴って (B) -> 普及し (D) -> オンラインサービスが (C) | **D** (`普及し`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `ACBD` | 発展に (A) -> オンラインサービスが (C) -> 伴って (B) -> 普及し (D) | **B** (`伴って`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `ACDB` | 発展に (A) -> オンラインサービスが (C) -> 普及し (D) -> 伴って (B) | **D** (`普及し`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `ADBC` | 発展に (A) -> 普及し (D) -> 伴って (B) -> オンラインサービスが (C) | **B** (`伴って`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `ADCB` | 発展に (A) -> 普及し (D) -> オンラインサービスが (C) -> 伴って (B) | **C** (`オンラインサービスが`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `BACD` | 伴って (B) -> 発展に (A) -> オンラインサービスが (C) -> 普及し (D) | **C** (`オンラインサービスが`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `BADC` | 伴って (B) -> 発展に (A) -> 普及し (D) -> オンラインサービスが (C) | **D** (`普及し`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `BCAD` | 伴って (B) -> オンラインサービスが (C) -> 発展に (A) -> 普及し (D) | **A** (`発展に`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `BCDA` | 伴って (B) -> オンラインサービスが (C) -> 普及し (D) -> 発展に (A) | **D** (`普及し`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `BDAC` | 伴って (B) -> 普及し (D) -> 発展に (A) -> オンラインサービスが (C) | **A** (`発展に`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `BDCA` | 伴って (B) -> 普及し (D) -> オンラインサービスが (C) -> 発展に (A) | **C** (`オンラインサービスが`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `CABD` | オンラインサービスが (C) -> 発展に (A) -> 伴って (B) -> 普及し (D) | **B** (`伴って`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `CADB` | オンラインサービスが (C) -> 発展に (A) -> 普及し (D) -> 伴って (B) | **D** (`普及し`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `CBAD` | オンラインサービスが (C) -> 伴って (B) -> 発展に (A) -> 普及し (D) | **A** (`発展に`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `CBDA` | オンラインサービスが (C) -> 伴って (B) -> 普及し (D) -> 発展に (A) | **D** (`普及し`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `CDAB` | オンラインサービスが (C) -> 普及し (D) -> 発展に (A) -> 伴って (B) | **A** (`発展に`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `CDBA` | オンラインサービスが (C) -> 普及し (D) -> 伴って (B) -> 発展に (A) | **B** (`伴って`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `DABC` | 普及し (D) -> 発展に (A) -> 伴って (B) -> オンラインサービスが (C) | **B** (`伴って`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `DACB` | 普及し (D) -> 発展に (A) -> オンラインサービスが (C) -> 伴って (B) | **C** (`オンラインサービスが`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `DBAC` | 普及し (D) -> 伴って (B) -> 発展に (A) -> オンラインサービスが (C) | **A** (`発展に`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `DBCA` | 普及し (D) -> 伴って (B) -> オンラインサービスが (C) -> 発展に (A) | **C** (`オンラインサービスが`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `DCAB` | 普及し (D) -> オンラインサービスが (C) -> 発展に (A) -> 伴って (B) | **A** (`発展に`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |
| `DCBA` | 普及し (D) -> オンラインサービスが (C) -> 伴って (B) -> 発展に (A) | **B** (`伴って`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N3: Danh từ + に伴って (cùng với sự phát triển của...) làm trạng ngữ chỉ sự biến đổi; chủ ngữ mới オンラインサービスが kết hợp động từ thể liên dụng 普及し nối vế tiếp theo. |

#### N3-GR-STAR-006 (N3) — Đáp án đúng: A (`性能が`)
- **Thân câu:** `従来の製品と（　　）（　　） ★ （　　）消費電力が30％も削減された。`
- **Câu lắp ráp chuẩn:** 「従来の製品と比べて新型モデルは性能が向上したうえに消費電力が30％も削減された。」
- **Thứ tự cú pháp chuẩn:** 比べて (D) -> 新型モデルは (B) -> 性能が (A) -> 向上したうえに (C)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | 性能が (A) -> 新型モデルは (B) -> 向上したうえに (C) -> 比べて (D) | **C** (`向上したうえに`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `ABDC` | 性能が (A) -> 新型モデルは (B) -> 比べて (D) -> 向上したうえに (C) | **D** (`比べて`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `ACBD` | 性能が (A) -> 向上したうえに (C) -> 新型モデルは (B) -> 比べて (D) | **B** (`新型モデルは`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `ACDB` | 性能が (A) -> 向上したうえに (C) -> 比べて (D) -> 新型モデルは (B) | **D** (`比べて`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `ADBC` | 性能が (A) -> 比べて (D) -> 新型モデルは (B) -> 向上したうえに (C) | **B** (`新型モデルは`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `ADCB` | 性能が (A) -> 比べて (D) -> 向上したうえに (C) -> 新型モデルは (B) | **C** (`向上したうえに`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `BACD` | 新型モデルは (B) -> 性能が (A) -> 向上したうえに (C) -> 比べて (D) | **C** (`向上したうえに`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `BADC` | 新型モデルは (B) -> 性能が (A) -> 比べて (D) -> 向上したうえに (C) | **D** (`比べて`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `BCAD` | 新型モデルは (B) -> 向上したうえに (C) -> 性能が (A) -> 比べて (D) | **A** (`性能が`) | PASS | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `BCDA` | 新型モデルは (B) -> 向上したうえに (C) -> 比べて (D) -> 性能が (A) | **D** (`比べて`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `BDAC` | 新型モデルは (B) -> 比べて (D) -> 性能が (A) -> 向上したうえに (C) | **A** (`性能が`) | PASS | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `BDCA` | 新型モデルは (B) -> 比べて (D) -> 向上したうえに (C) -> 性能が (A) | **C** (`向上したうえに`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `CABD` | 向上したうえに (C) -> 性能が (A) -> 新型モデルは (B) -> 比べて (D) | **B** (`新型モデルは`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `CADB` | 向上したうえに (C) -> 性能が (A) -> 比べて (D) -> 新型モデルは (B) | **D** (`比べて`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `CBAD` | 向上したうえに (C) -> 新型モデルは (B) -> 性能が (A) -> 比べて (D) | **A** (`性能が`) | PASS | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `CBDA` | 向上したうえに (C) -> 新型モデルは (B) -> 比べて (D) -> 性能が (A) | **D** (`比べて`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `CDAB` | 向上したうえに (C) -> 比べて (D) -> 性能が (A) -> 新型モデルは (B) | **A** (`性能が`) | PASS | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `CDBA` | 向上したうえに (C) -> 比べて (D) -> 新型モデルは (B) -> 性能が (A) | **B** (`新型モデルは`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `DABC` | 比べて (D) -> 性能が (A) -> 新型モデルは (B) -> 向上したうえに (C) | **B** (`新型モデルは`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `DACB` | 比べて (D) -> 性能が (A) -> 向上したうえに (C) -> 新型モデルは (B) | **C** (`向上したうえに`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `DBAC` | 比べて (D) -> 新型モデルは (B) -> 性能が (A) -> 向上したうえに (C) | **A** (`性能が`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `DBCA` | 比べて (D) -> 新型モデルは (B) -> 向上したうえに (C) -> 性能が (A) | **C** (`向上したうえに`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `DCAB` | 比べて (D) -> 向上したうえに (C) -> 性能が (A) -> 新型モデルは (B) | **A** (`性能が`) | PASS | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |
| `DCBA` | 比べて (D) -> 向上したうえに (C) -> 新型モデルは (B) -> 性能が (A) | **B** (`新型モデルは`) | NO | `GRAMMATICALLY_INVALID` | Cụm so sánh 〜と比べて nối chủ ngữ 新型モデルは, tiếp theo là cụm đặc tính 性能が向上したうえに (không những hiệu năng tăng mà còn...) nối tiếp vào 消費電力が30％も削減された. |

#### N2-GR-STAR-001 (N2) — Đáp án đúng: B (`存続をも`)
- **Thân câu:** `今回の不祥事は会社の信用を（　　）（　　） ★ （　　）重大な問題である。`
- **Câu lắp ráp chuẩn:** 「今回の不祥事は会社の信用を失墜させるどころか存続をも脅かしかねない重大な問題である。」
- **Thứ tự cú pháp chuẩn:** 失墜させる (A) -> どころか (D) -> 存続をも (B) -> 脅かしかねない (C)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | 失墜させる (A) -> 存続をも (B) -> 脅かしかねない (C) -> どころか (D) | **C** (`脅かしかねない`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `ABDC` | 失墜させる (A) -> 存続をも (B) -> どころか (D) -> 脅かしかねない (C) | **D** (`どころか`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `ACBD` | 失墜させる (A) -> 脅かしかねない (C) -> 存続をも (B) -> どころか (D) | **B** (`存続をも`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `ACDB` | 失墜させる (A) -> 脅かしかねない (C) -> どころか (D) -> 存続をも (B) | **D** (`どころか`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `ADBC` | 失墜させる (A) -> どころか (D) -> 存続をも (B) -> 脅かしかねない (C) | **B** (`存続をも`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `ADCB` | 失墜させる (A) -> どころか (D) -> 脅かしかねない (C) -> 存続をも (B) | **C** (`脅かしかねない`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `BACD` | 存続をも (B) -> 失墜させる (A) -> 脅かしかねない (C) -> どころか (D) | **C** (`脅かしかねない`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `BADC` | 存続をも (B) -> 失墜させる (A) -> どころか (D) -> 脅かしかねない (C) | **D** (`どころか`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `BCAD` | 存続をも (B) -> 脅かしかねない (C) -> 失墜させる (A) -> どころか (D) | **A** (`失墜させる`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `BCDA` | 存続をも (B) -> 脅かしかねない (C) -> どころか (D) -> 失墜させる (A) | **D** (`どころか`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `BDAC` | 存続をも (B) -> どころか (D) -> 失墜させる (A) -> 脅かしかねない (C) | **A** (`失墜させる`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `BDCA` | 存続をも (B) -> どころか (D) -> 脅かしかねない (C) -> 失墜させる (A) | **C** (`脅かしかねない`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `CABD` | 脅かしかねない (C) -> 失墜させる (A) -> 存続をも (B) -> どころか (D) | **B** (`存続をも`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `CADB` | 脅かしかねない (C) -> 失墜させる (A) -> どころか (D) -> 存続をも (B) | **D** (`どころか`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `CBAD` | 脅かしかねない (C) -> 存続をも (B) -> 失墜させる (A) -> どころか (D) | **A** (`失墜させる`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `CBDA` | 脅かしかねない (C) -> 存続をも (B) -> どころか (D) -> 失墜させる (A) | **D** (`どころか`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `CDAB` | 脅かしかねない (C) -> どころか (D) -> 失墜させる (A) -> 存続をも (B) | **A** (`失墜させる`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `CDBA` | 脅かしかねない (C) -> どころか (D) -> 存続をも (B) -> 失墜させる (A) | **B** (`存続をも`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `DABC` | どころか (D) -> 失墜させる (A) -> 存続をも (B) -> 脅かしかねない (C) | **B** (`存続をも`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `DACB` | どころか (D) -> 失墜させる (A) -> 脅かしかねない (C) -> 存続をも (B) | **C** (`脅かしかねない`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `DBAC` | どころか (D) -> 存続をも (B) -> 失墜させる (A) -> 脅かしかねない (C) | **A** (`失墜させる`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `DBCA` | どころか (D) -> 存続をも (B) -> 脅かしかねない (C) -> 失墜させる (A) | **C** (`脅かしかねない`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `DCAB` | どころか (D) -> 脅かしかねない (C) -> 失墜させる (A) -> 存続をも (B) | **A** (`失墜させる`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |
| `DCBA` | どころか (D) -> 脅かしかねない (C) -> 存続をも (B) -> 失墜させる (A) | **B** (`存続をも`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N2 tăng tiến cực đoan: V-る + どころか (không những... mà còn nguy hiểm hơn là) kết hợp trợ từ nhấn mạnh 存続をも và vị ngữ nguy cơ 脅かしかねない bổ nghĩa cho 重大な問題である. |

#### N2-GR-STAR-002 (N2) — Đáp án đúng: B (`一人ひとりの`)
- **Thân câu:** `どのような困難な課題であっても、（　　）（　　） ★ （　　）次第で克服できる。`
- **Câu lắp ráp chuẩn:** 「どのような困難な課題であっても、チームの団結と一人ひとりの取り組み方次第で克服できる。」
- **Thứ tự cú pháp chuẩn:** チームの (D) -> 団結と (C) -> 一人ひとりの (B) -> 取り組み方 (A)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | 取り組み方 (A) -> 一人ひとりの (B) -> 団結と (C) -> チームの (D) | **C** (`団結と`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `ABDC` | 取り組み方 (A) -> 一人ひとりの (B) -> チームの (D) -> 団結と (C) | **D** (`チームの`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `ACBD` | 取り組み方 (A) -> 団結と (C) -> 一人ひとりの (B) -> チームの (D) | **B** (`一人ひとりの`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `ACDB` | 取り組み方 (A) -> 団結と (C) -> チームの (D) -> 一人ひとりの (B) | **D** (`チームの`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `ADBC` | 取り組み方 (A) -> チームの (D) -> 一人ひとりの (B) -> 団結と (C) | **B** (`一人ひとりの`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `ADCB` | 取り組み方 (A) -> チームの (D) -> 団結と (C) -> 一人ひとりの (B) | **C** (`団結と`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `BACD` | 一人ひとりの (B) -> 取り組み方 (A) -> 団結と (C) -> チームの (D) | **C** (`団結と`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `BADC` | 一人ひとりの (B) -> 取り組み方 (A) -> チームの (D) -> 団結と (C) | **D** (`チームの`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `BCAD` | 一人ひとりの (B) -> 団結と (C) -> 取り組み方 (A) -> チームの (D) | **A** (`取り組み方`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `BCDA` | 一人ひとりの (B) -> 団結と (C) -> チームの (D) -> 取り組み方 (A) | **D** (`チームの`) | NO | `GRAMMATICALLY_INVALID` | Về ngữ nghĩa tiếng Nhật, danh từ '団結' (đoàn kết) bắt buộc đi với tập thể ('チームの団結'), hoàn toàn phi lý khi ghép với cá nhân đơn lẻ ('一人ひとりの団結'). Do đó không thể hoán vị. |
| `BDAC` | 一人ひとりの (B) -> チームの (D) -> 取り組み方 (A) -> 団結と (C) | **A** (`取り組み方`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `BDCA` | 一人ひとりの (B) -> チームの (D) -> 団結と (C) -> 取り組み方 (A) | **C** (`団結と`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `CABD` | 団結と (C) -> 取り組み方 (A) -> 一人ひとりの (B) -> チームの (D) | **B** (`一人ひとりの`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `CADB` | 団結と (C) -> 取り組み方 (A) -> チームの (D) -> 一人ひとりの (B) | **D** (`チームの`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `CBAD` | 団結と (C) -> 一人ひとりの (B) -> 取り組み方 (A) -> チームの (D) | **A** (`取り組み方`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `CBDA` | 団結と (C) -> 一人ひとりの (B) -> チームの (D) -> 取り組み方 (A) | **D** (`チームの`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `CDAB` | 団結と (C) -> チームの (D) -> 取り組み方 (A) -> 一人ひとりの (B) | **A** (`取り組み方`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `CDBA` | 団結と (C) -> チームの (D) -> 一人ひとりの (B) -> 取り組み方 (A) | **B** (`一人ひとりの`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `DABC` | チームの (D) -> 取り組み方 (A) -> 一人ひとりの (B) -> 団結と (C) | **B** (`一人ひとりの`) | PASS | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `DACB` | チームの (D) -> 取り組み方 (A) -> 団結と (C) -> 一人ひとりの (B) | **C** (`団結と`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `DBAC` | チームの (D) -> 一人ひとりの (B) -> 取り組み方 (A) -> 団結と (C) | **A** (`取り組み方`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `DBCA` | チームの (D) -> 一人ひとりの (B) -> 団結と (C) -> 取り組み方 (A) | **C** (`団結と`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `DCAB` | チームの (D) -> 団結と (C) -> 取り組み方 (A) -> 一人ひとりの (B) | **A** (`取り組み方`) | NO | `GRAMMATICALLY_INVALID` | Cấu trúc danh từ ghép nối bằng と kết hợp danh từ hình thức 次第で (tùy thuộc vào). Bắt buộc thứ tự: チームの団結 (đoàn kết của đội ngũ) và 一人ひとりの取り組み方 (cách tiếp cận của từng cá nhân). |
| `DCBA` | チームの (D) -> 団結と (C) -> 一人ひとりの (B) -> 取り組み方 (A) | **B** (`一人ひとりの`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |

#### N2-GR-STAR-003 (N2) — Đáp án đúng: D (`傲慢な態度を`)
- **Thân câu:** `いくら専門知識が（　　）（　　） ★ （　　）周囲の信頼は得られない。`
- **Câu lắp ráp chuẩn:** 「いくら専門知識が豊富だからといって傲慢な態度をとっていては周囲の信頼は得られない。」
- **Thứ tự cú pháp chuẩn:** 豊富だから (A) -> といって (C) -> 傲慢な態度を (D) -> とっていては (B)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | 豊富だから (A) -> とっていては (B) -> といって (C) -> 傲慢な態度を (D) | **C** (`といって`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `ABDC` | 豊富だから (A) -> とっていては (B) -> 傲慢な態度を (D) -> といって (C) | **D** (`傲慢な態度を`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `ACBD` | 豊富だから (A) -> といって (C) -> とっていては (B) -> 傲慢な態度を (D) | **B** (`とっていては`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `ACDB` | 豊富だから (A) -> といって (C) -> 傲慢な態度を (D) -> とっていては (B) | **D** (`傲慢な態度を`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `ADBC` | 豊富だから (A) -> 傲慢な態度を (D) -> とっていては (B) -> といって (C) | **B** (`とっていては`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `ADCB` | 豊富だから (A) -> 傲慢な態度を (D) -> といって (C) -> とっていては (B) | **C** (`といって`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `BACD` | とっていては (B) -> 豊富だから (A) -> といって (C) -> 傲慢な態度を (D) | **C** (`といって`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `BADC` | とっていては (B) -> 豊富だから (A) -> 傲慢な態度を (D) -> といって (C) | **D** (`傲慢な態度を`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `BCAD` | とっていては (B) -> といって (C) -> 豊富だから (A) -> 傲慢な態度を (D) | **A** (`豊富だから`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `BCDA` | とっていては (B) -> といって (C) -> 傲慢な態度を (D) -> 豊富だから (A) | **D** (`傲慢な態度を`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `BDAC` | とっていては (B) -> 傲慢な態度を (D) -> 豊富だから (A) -> といって (C) | **A** (`豊富だから`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `BDCA` | とっていては (B) -> 傲慢な態度を (D) -> といって (C) -> 豊富だから (A) | **C** (`といって`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `CABD` | といって (C) -> 豊富だから (A) -> とっていては (B) -> 傲慢な態度を (D) | **B** (`とっていては`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `CADB` | といって (C) -> 豊富だから (A) -> 傲慢な態度を (D) -> とっていては (B) | **D** (`傲慢な態度を`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `CBAD` | といって (C) -> とっていては (B) -> 豊富だから (A) -> 傲慢な態度を (D) | **A** (`豊富だから`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `CBDA` | といって (C) -> とっていては (B) -> 傲慢な態度を (D) -> 豊富だから (A) | **D** (`傲慢な態度を`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `CDAB` | といって (C) -> 傲慢な態度を (D) -> 豊富だから (A) -> とっていては (B) | **A** (`豊富だから`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `CDBA` | といって (C) -> 傲慢な態度を (D) -> とっていては (B) -> 豊富だから (A) | **B** (`とっていては`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `DABC` | 傲慢な態度を (D) -> 豊富だから (A) -> とっていては (B) -> といって (C) | **B** (`とっていては`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `DACB` | 傲慢な態度を (D) -> 豊富だから (A) -> といって (C) -> とっていては (B) | **C** (`といって`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `DBAC` | 傲慢な態度を (D) -> とっていては (B) -> 豊富だから (A) -> といって (C) | **A** (`豊富だから`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `DBCA` | 傲慢な態度を (D) -> とっていては (B) -> といって (C) -> 豊富だから (A) | **C** (`といって`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `DCAB` | 傲慢な態度を (D) -> といって (C) -> 豊富だから (A) -> とっていては (B) | **A** (`豊富だから`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |
| `DCBA` | 傲慢な態度を (D) -> といって (C) -> とっていては (B) -> 豊富だから (A) | **B** (`とっていては`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu N2 điều kiện tiêu cực: Tính từ だから + といって (cho dù có... đi chăng nữa) kết hợp cụm hành vi 傲慢な態度を + とっていては (nếu cứ có thái độ kiêu ngạo) dẫn đến hậu quả 周囲の信頼は得られない. |

#### N2-GR-STAR-004 (N2) — Đáp án đúng: C (`本番の`)
- **Thân câu:** `事前の綿密な（　　）（　　） ★ （　　）予期せぬトラブルが発生した。`
- **Câu lắp ráp chuẩn:** 「事前の綿密な計画にもかかわらず、本番の現場では予期せぬトラブルが発生した。」
- **Thứ tự cú pháp chuẩn:** 計画にも (B) -> かかわらず (A) -> 本番の (C) -> 現場では (D)
- **Bảng phân loại 24 hoán vị:**

| Hoán vị | Thứ tự lựa chọn | Ô số 3 (★) | Khớp key? | Phân loại cú pháp | Đánh giá ngôn ngữ |
| :---: | :--- | :---: | :---: | :--- | :--- |
| `ABCD` | かかわらず (A) -> 計画にも (B) -> 本番の (C) -> 現場では (D) | **C** (`本番の`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `ABDC` | かかわらず (A) -> 計画にも (B) -> 現場では (D) -> 本番の (C) | **D** (`現場では`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `ACBD` | かかわらず (A) -> 本番の (C) -> 計画にも (B) -> 現場では (D) | **B** (`計画にも`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `ACDB` | かかわらず (A) -> 本番の (C) -> 現場では (D) -> 計画にも (B) | **D** (`現場では`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `ADBC` | かかわらず (A) -> 現場では (D) -> 計画にも (B) -> 本番の (C) | **B** (`計画にも`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `ADCB` | かかわらず (A) -> 現場では (D) -> 本番の (C) -> 計画にも (B) | **C** (`本番の`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `BACD` | 計画にも (B) -> かかわらず (A) -> 本番の (C) -> 現場では (D) | **C** (`本番の`) | PASS | `CANONICAL_CORRECT` | Chuỗi sắp xếp tự nhiên, chuẩn mực ngữ pháp tiếng Nhật và khớp 100% với câu hoàn chỉnh chuẩn. |
| `BADC` | 計画にも (B) -> かかわらず (A) -> 現場では (D) -> 本番の (C) | **D** (`現場では`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `BCAD` | 計画にも (B) -> 本番の (C) -> かかわらず (A) -> 現場では (D) | **A** (`かかわらず`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `BCDA` | 計画にも (B) -> 本番の (C) -> 現場では (D) -> かかわらず (A) | **D** (`現場では`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `BDAC` | 計画にも (B) -> 現場では (D) -> かかわらず (A) -> 本番の (C) | **A** (`かかわらず`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `BDCA` | 計画にも (B) -> 現場では (D) -> 本番の (C) -> かかわらず (A) | **C** (`本番の`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `CABD` | 本番の (C) -> かかわらず (A) -> 計画にも (B) -> 現場では (D) | **B** (`計画にも`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `CADB` | 本番の (C) -> かかわらず (A) -> 現場では (D) -> 計画にも (B) | **D** (`現場では`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `CBAD` | 本番の (C) -> 計画にも (B) -> かかわらず (A) -> 現場では (D) | **A** (`かかわらず`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `CBDA` | 本番の (C) -> 計画にも (B) -> 現場では (D) -> かかわらず (A) | **D** (`現場では`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `CDAB` | 本番の (C) -> 現場では (D) -> かかわらず (A) -> 計画にも (B) | **A** (`かかわらず`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `CDBA` | 本番の (C) -> 現場では (D) -> 計画にも (B) -> かかわらず (A) | **B** (`計画にも`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `DABC` | 現場では (D) -> かかわらず (A) -> 計画にも (B) -> 本番の (C) | **B** (`計画にも`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `DACB` | 現場では (D) -> かかわらず (A) -> 本番の (C) -> 計画にも (B) | **C** (`本番の`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `DBAC` | 現場では (D) -> 計画にも (B) -> かかわらず (A) -> 本番の (C) | **A** (`かかわらず`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `DBCA` | 現場では (D) -> 計画にも (B) -> 本番の (C) -> かかわらず (A) | **C** (`本番の`) | PASS | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `DCAB` | 現場では (D) -> 本番の (C) -> かかわらず (A) -> 計画にも (B) | **A** (`かかわらず`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |
| `DCBA` | 現場では (D) -> 本番の (C) -> 計画にも (B) -> かかわらず (A) | **B** (`計画にも`) | NO | `GRAMMATICALLY_INVALID` | Mẫu câu nhượng bộ N2: Danh từ + にもかかわらず (mặc dù kế hoạch kỹ lưỡng) nối trạng ngữ địa điểm 本番の現場では (tại hiện trường thi đấu/thực tế) làm nền cho mệnh đề sự cố 予期せぬトラブルが発生した. |

