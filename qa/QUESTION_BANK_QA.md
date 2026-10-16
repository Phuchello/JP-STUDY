# BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG NGÂN HÀNG CÂU HỎI (PHASE 3.7 - FINAL QA RECONCILIATION)
## INDEPENDENT QUESTION BANK QA & MULTI-STAGE AUDIT REPORT

### 1. TỔNG QUAN HIỆN TRẠNG
- **Tổng số câu hỏi trong ngân hàng:** 120 câu (100% Unique Items).
- **Phân bổ theo cấp độ:**
  - **N4:** 40 câu (Phục hồi nền tảng: Từ vựng, Trợ từ, Chia thể, Đọc hiểu đoản văn, Tìm kiếm thông tin).
  - **N3:** 50 câu (Bước đệm trung cấp: Kanji, Cấu tạo từ ghép, Ngữ pháp mẫu câu, Câu dấu sao, Trung văn).
  - **N2:** 30 câu (Luyện đề mục tiêu: Kanji cao cấp, Từ vựng trừu tượng, Ngữ pháp kép, Đoản văn nghị luận).
- **Phân bổ vị trí đáp án đúng (Seeded Shuffle `seed-clean-audit` - Non-cyclic):**
  - **A:** 33 câu (27.5%)
  - **B:** 30 câu (25.0%)
  - **C:** 29 câu (24.2%)
  - **D:** 28 câu (23.3%)
  - *Chuỗi lặp 4-tuple ABCD: 1 (mức xác suất ngẫu nhiên kỳ vọng len/256), chuỗi đáp án trùng liên tiếp tối đa là 3. Hoàn toàn loại bỏ chuỗi chu kỳ xác định.*
- **Trạng thái kiểm định ngân hàng:** `QA_VERIFIED`. Toàn bộ 120 câu đã được thẩm định qua vòng giải mù độc lập bởi subagent độc lập (`subagent:jlpt-blind-reviewer`) không có đáp án tác giả hay giải thích, đạt tỷ lệ đồng thuận tuyệt đối 120/120 (100.0%).
- **Xử lý dứt điểm 6 câu hỏi bị cảnh báo/mơ hồ ngữ nghĩa (Checkpoint remediation):**
  - Đã tái cấu trúc và khử triệt để mơ hồ cho 6 câu: `N4-GR-FORM-010`, `N4-GR-STAR-002`, `N4-GR-STAR-006`, `N3-GR-FORM-006`, `N3-GR-STAR-001`, `N2-GR-FORM-003`.
  - Thực hiện phiên giải mù độc lập bổ sung cho cả 6 câu đã sửa (không cung cấp đáp án tác giả); subagent đạt độ đồng thuận 6/6 (100%), 0 đáp án thay thế hợp lệ, 0 quan ngại ngữ nghĩa. Lưu trữ tại [`qa/raw_blind_review_repaired_6.json`](raw_blind_review_repaired_6.json).
  - Dữ liệu so sánh trước/sau sửa đổi được lưu tại [`qa/flagged_questions_diff.json`](flagged_questions_diff.json).
- **Kiểm toán động câu hỏi dấu sao (Dynamic Star Question Audit):**
  - Toàn bộ ngân hàng có đúng **16 câu dấu sao** (N4: 6 câu, N3: 6 câu, N2: 4 câu; không ngụy tạo thêm câu N2 ngoài ngân hàng).
  - Trình kiểm tra tự động xác nhận 16/16 câu: cấu trúc 4 ô, dấu sao cố định tại vị trí 3, câu hoàn chỉnh chuẩn ngữ pháp, chỉ tồn tại duy nhất 1 hoán vị cú pháp hợp lệ (khóa chặt cấu trúc ngữ đoạn và quan hệ bổ nghĩa).
- **Trạng thái bộ đề luyện thi (20 bộ đề):** `QA_PASSED_NOT_DEPLOYED` (`SPEC_ONLY`). Không triển khai Form mới nào ra môi trường chạy thực tế; bảo toàn nguyên vẹn 3 Form P0 hiện hữu (W01-B01, W01-B02, W01-B03).

---

### 2. KẾT QUẢ CÁC CỔNG KIỂM ĐỊNH

| Cổng kiểm định | Nội dung kiểm tra | Kết quả | Ghi chú kỹ thuật |
| :--- | :--- | :---: | :--- |
| **Cổng A: Schema** | Định dạng JSON, 4 lựa chọn, đáp án [A-D], giải thích tiếng Việt chi tiết | **120 / 120 PASS** | Cấu trúc dữ liệu chuẩn JLPT |
| **Cổng B: Ngôn ngữ Nhật** | Tính tự nhiên, chuẩn hình thái từ, từ loại, khử mơ hồ phương án nhiễu | **120 / 120 PASS** | Thẩm định ngữ nghĩa, hình thái từ, ngữ cảnh; đã sửa dứt điểm 6 câu cảnh báo |
| **Cổng C: Giải mù độc lập** | Độc lập giải đề từ mô hình/subagent riêng biệt không có đáp án tác giả | **120 / 120 PASS** | 4 phiên subagent độc lập (`qa/raw_blind_review_*.json`), 100% khớp đáp án tác giả |
| **Cổng D: Phản biện & Đột biến** | Chống trùng ngữ liệu stem, kiểm toán phân bổ phi chu kỳ, kiểm toán động 16 câu dấu sao, test đột biến 12 lớp lỗi | **120 / 120 PASS** | Vượt qua 12/12 bài kiểm tra đột biến phản biện tại `scripts/tests/test_qa_adversarial_mutations.py` |
| **Cổng E: Thẩm định thực tế** | Thẩm định bởi học viên và giáo viên hiệu chuẩn độ khó thực tế | **PENDING_LEARNER_CALIBRATION** | Đánh dấu trung thực đang chờ phiên thử nghiệm thực tế với người học |

---

### 3. TÀI LIỆU VÀ CHỨNG CỨ KIỂM TOÁN
- **Báo cáo đối soát giải mù độc lập:** [`qa/BLIND_REVIEW_RECONCILIATION_REPORT.md`](BLIND_REVIEW_RECONCILIATION_REPORT.md)
- **Báo cáo kiểm toán tái lập P0 (Reproducibility & Invariance):** [`qa/REPRODUCIBILITY_AUDIT.md`](REPRODUCIBILITY_AUDIT.md)
- **Manifest chứng thực vân tay mật mã (Canonical SHA-256 NFC):** [`qa/CONTENT_FINGERPRINT_MANIFEST.json`](CONTENT_FINGERPRINT_MANIFEST.json)
- **Báo cáo kiểm toán nguồn gốc thẩm định (Provenance Audit):** [`qa/REVIEW_PROVENANCE_AUDIT.md`](REVIEW_PROVENANCE_AUDIT.md)
- **Báo cáo kiểm toán hoán vị câu hỏi dấu sao (Star Permutation 24!):** [`qa/STAR_PERMUTATION_AUDIT.md`](STAR_PERMUTATION_AUDIT.md)
- **Cổng kiểm soát phát hành bộ đề (7 Release Dimensions):** [`qa/PRACTICE_RELEASE_GATE.md`](PRACTICE_RELEASE_GATE.md)
- **Tập dữ liệu giải mù đầu vào (không có đáp án/giải thích):**
  - Toàn bộ 120 câu: [`qa/blind_review_dataset.json`](blind_review_dataset.json)
  - N4 (40 câu): [`qa/blind_review_n4.json`](blind_review_n4.json)
  - N3 (50 câu): [`qa/blind_review_n3.json`](blind_review_n3.json)
  - N2 (30 câu): [`qa/blind_review_n2.json`](blind_review_n2.json)
  - 6 câu sửa đổi sau phúc tra: [`qa/blind_review_repaired_6.json`](blind_review_repaired_6.json)
- **Dữ liệu giải mù thô từ Subagent độc lập (Raw Reviewer Outputs):**
  - N4: [`qa/raw_blind_review_n4.json`](raw_blind_review_n4.json)
  - N3: [`qa/raw_blind_review_n3.json`](raw_blind_review_n3.json)
  - N2: [`qa/raw_blind_review_n2.json`](raw_blind_review_n2.json)
  - 6 câu sửa đổi: [`qa/raw_blind_review_repaired_6.json`](raw_blind_review_repaired_6.json)
- **Bảng so sánh trước và sau sửa đổi 6 câu:** [`qa/flagged_questions_diff.json`](flagged_questions_diff.json)
- **Sổ cái kiểm định chi tiết:** [`qa/QUESTION_REVIEW_LEDGER.csv`](QUESTION_REVIEW_LEDGER.csv)
- **Hồ sơ lỗi lịch sử và xử lý:** [`qa/REJECTED_ITEMS.json`](REJECTED_ITEMS.json)
- **Bộ kiểm thử tự động đột biến (12 classes of defects):** [`scripts/tests/test_qa_adversarial_mutations.py`](../scripts/tests/test_qa_adversarial_mutations.py)
- **Bộ kiểm thử hồi quy phủ định (Negative Test Suite):** [`scripts/tests/test_question_bank_negative.py`](../scripts/tests/test_question_bank_negative.py)
