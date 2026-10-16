# BÁO CÁO KIỂM TOÁN NGUỒN GỐC & LIÊN KẾT MẬT MÃ THẨM ĐỊNH (REVIEW PROVENANCE AUDIT)
## PHASE 3.7 — CRYPTOGRAPHIC REVIEW-TO-CONTENT BINDING AUDIT

> [!IMPORTANT]
> - **Tổng số câu hỏi được định danh mật mã**: **120 câu (100% Unique Items)**.
> - **Số câu khớp dấu vân tay nội dung (Content Fingerprint Match)**: **120 / 120 (100.0%)**.
> - **Số câu sai lệch dấu vân tay (Stale / Unverified)**: **0 câu (0.0%)**.
> - **Quy tắc bảo vệ**: Bất kỳ sự thay đổi dù chỉ 1 ký tự trong stem, passage, hoặc phương án lựa chọn đều làm thay đổi Content Fingerprint SHA-256 và lập tức bị hệ thống từ chối (`FINGERPRINT_MISMATCH`), ngăn chặn kế thừa trạng thái QA sai phiên bản.

---

### 1. BẢNG PHÂN BỔ CÁC ĐỢT GIẢI MÙ ĐỘC LẬP (REVIEW BATCHES)

| Batch ID | Cấp độ / Phạm vi | Số câu | Conversation ID (Subagent) | Input Dataset Digest (SHA-256) | Raw Output Digest (SHA-256) | Trạng thái |
| :--- | :---: | :---: | :--- | :--- | :--- | :---: |
| `batch-20261015-n4` | N4 | 40 | `5a240741-f93...` | `45edd284a70f...` | `bec76912b721...` | **CRYPTOGRAPHICALLY_VERIFIED** |
| `batch-20261015-n3` | N3 | 50 | `d0ff9896-0e2...` | `c6920aaf8d23...` | `69dc6a89876f...` | **CRYPTOGRAPHICALLY_VERIFIED** |
| `batch-20261015-n2` | N2 | 30 | `cacea4de-bfe...` | `9797fb4af47b...` | `98e979716eb0...` | **CRYPTOGRAPHICALLY_VERIFIED** |
| `batch-20261016-repaired-6` | REPAIRED_6 | 6 | `cbfb8289-5e9...` | `0df362a54594...` | `0ca90b7ddec2...` | **CRYPTOGRAPHICALLY_VERIFIED** |

---

### 2. SỔ CÁI LIÊN KẾT MẬT MÃ NỘI DUNG VỚI KẾT QUẢ ĐÁNH GIÁ (MẪU ĐẠI DIỆN)

| Question ID | Level | Content Fingerprint (SHA-256) | Author Key | Blind Key | Conf | Batch ID | Provenance | Validity |
| :--- | :---: | :--- | :---: | :---: | :---: | :--- | :---: | :---: |
| **N4-MO-READ-001** | N4 | `cc881c5550597e05...` | **C** | **C** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-READ-002** | N4 | `26a6f1927299da50...` | **D** | **D** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-READ-003** | N4 | `2500a86b47bebec9...` | **B** | **B** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-READ-004** | N4 | `8e3132414d3b2d19...` | **C** | **C** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-READ-005** | N4 | `b7987ff4723b9eb8...` | **C** | **C** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-READ-006** | N4 | `4d1a5e6e60a64b00...` | **B** | **B** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-READ-007** | N4 | `972c714737b34fd3...` | **A** | **A** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-READ-008** | N4 | `9724aef1b96eb8f3...` | **A** | **A** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-CONT-001** | N4 | `c43a76e1f177952c...` | **C** | **C** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-CONT-002** | N4 | `e7e272cc8ce7899a...` | **B** | **B** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-CONT-003** | N4 | `981d0a8c04bf8ad6...` | **D** | **D** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-CONT-004** | N4 | `27130de843379111...` | **D** | **D** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-CONT-005** | N4 | `2cfc38b798dce220...` | **A** | **A** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-CONT-006** | N4 | `02c367b786a12d65...` | **C** | **C** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-CONT-007** | N4 | `4af2a921a55deee8...` | **B** | **B** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-MO-CONT-008** | N4 | `8b3e186d717fb028...` | **A** | **A** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-FORM-001** | N4 | `fa3b0c854f4c5133...` | **B** | **B** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-FORM-002** | N4 | `893f0795ab79cc5d...` | **B** | **B** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-FORM-003** | N4 | `4db34cd431e3cff7...` | **D** | **D** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-FORM-004** | N4 | `9632a3c4a4ec0e3c...` | **B** | **B** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-FORM-005** | N4 | `43236466c9cdb092...` | **D** | **D** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-FORM-006** | N4 | `791e7b4a07bd247f...` | **B** | **B** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-FORM-007** | N4 | `464ee729dfa3da85...` | **A** | **A** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-FORM-008** | N4 | `b651986e92aad3df...` | **C** | **C** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-FORM-009** | N4 | `d16f7869a12348b0...` | **D** | **D** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-FORM-010** | N4 | `7eeec32b9584542d...` | **A** | **A** | HIGH | `batch-20261016-repaired-6` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-FORM-011** | N4 | `b941544dfd183a96...` | **A** | **A** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-FORM-012** | N4 | `9a0809dd80c817ab...` | **C** | **C** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-STAR-001** | N4 | `98aecc2bf11f582c...` | **D** | **D** | HIGH | `batch-20261015-n4` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |
| **N4-GR-STAR-002** | N4 | `a7de6f437d0ba643...` | **D** | **D** | HIGH | `batch-20261016-repaired-6` | `CRYPTOGRAPHICALLY_VERIFIED` | **QA_VERIFIED** |

*(Toàn bộ 120 bản ghi liên kết mật mã chi tiết được lưu trữ có cấu trúc tại [`qa/CONTENT_FINGERPRINT_MANIFEST.json`](CONTENT_FINGERPRINT_MANIFEST.json))*

---

### 3. KIỂM TOÁN ĐẶC BIỆT: 6 CÂU HỎI SỬA ĐỔI SAU PHÚC TRA (REPAIRED ITEMS PROVENANCE)

| Question ID | Trạng thái ban đầu | Lý do sửa đổi | Raw Output Batch Mới | Content Fingerprint Mới | Kết quả thẩm định mù |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **N2-GR-FORM-003** | `FLAGGED_AMBIGUITY` | Sửa dứt điểm phương án nhiễu & khóa cứng cú pháp | `batch-20261016-repaired-6` | `d968908774862c24...` | **A (HIGH)** · 100% PASS |
| **N3-GR-FORM-006** | `FLAGGED_AMBIGUITY` | Sửa dứt điểm phương án nhiễu & khóa cứng cú pháp | `batch-20261016-repaired-6` | `1b1c6582253c5acd...` | **B (HIGH)** · 100% PASS |
| **N3-GR-STAR-001** | `FLAGGED_AMBIGUITY` | Sửa dứt điểm phương án nhiễu & khóa cứng cú pháp | `batch-20261016-repaired-6` | `1a78d433d822942c...` | **A (HIGH)** · 100% PASS |
| **N4-GR-FORM-010** | `FLAGGED_AMBIGUITY` | Sửa dứt điểm phương án nhiễu & khóa cứng cú pháp | `batch-20261016-repaired-6` | `7eeec32b9584542d...` | **A (HIGH)** · 100% PASS |
| **N4-GR-STAR-002** | `FLAGGED_AMBIGUITY` | Sửa dứt điểm phương án nhiễu & khóa cứng cú pháp | `batch-20261016-repaired-6` | `a7de6f437d0ba643...` | **D (HIGH)** · 100% PASS |
| **N4-GR-STAR-006** | `FLAGGED_AMBIGUITY` | Sửa dứt điểm phương án nhiễu & khóa cứng cú pháp | `batch-20261016-repaired-6` | `8effaa221d34a725...` | **A (HIGH)** · 100% PASS |

---

### 4. KẾT LUẬN KIỂM TOÁN NGUỒN GỐC (PROVENANCE VERDICT)

**DECISION: VERIFIED — TOÀN BỘ 120 CÂU HỎI ĐƯỢC RÀNG BUỘC MẬT MÃ TOÀN VẸN**

- 114 câu gốc khớp 100% dấu vân tay với 3 tập dữ liệu giải mù ban đầu (`qa/raw_blind_review_n4.json`, `n3.json`, `n2.json`).
- 6 câu sửa đổi được cập nhật dấu vân tay mới và ràng buộc với tập giải mù bổ sung (`qa/raw_blind_review_repaired_6.json`).
- Hệ thống đã loại bỏ hoàn toàn cơ chế liên kết lỏng lẻo chỉ theo ID; mọi phiên bản câu hỏi đều được đối chiếu chặt chẽ bằng SHA-256.

