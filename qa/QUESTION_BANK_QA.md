# BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG NGÂN HÀNG CÂU HỎI (PHASE 3.7 - INDEPENDENT QA VERIFIED)
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
  - *Chuỗi lặp 4-tuple ABCD giảm xuống 1 (mức ngẫu nhiên kỳ vọng len/256), chuỗi đáp án liên tiếp tối đa là 3. Hoàn toàn loại bỏ chuỗi chu kỳ xác định.*
- **Trạng thái kiểm định ngân hàng:** `QA_VERIFIED`. Toàn bộ 120 câu đã được giải mù độc lập bởi 3 phiên subagent (`subagent:jlpt-blind-reviewer`) không có đáp án tác giả hay giải thích, đạt tỷ lệ đồng thuận tuyệt đối 120/120 (100.0%).
- **Trạng thái bộ đề luyện thi (20 bộ đề):** `QA_PASSED_NOT_DEPLOYED` (`SPEC_ONLY`). Không triển khai Form mới nào ra môi trường chạy thực tế; bảo toàn nguyên vẹn 3 Form P0 hiện hữu (W01-B01, W01-B02, W01-B03).

---

### 2. KẾT QUẢ CÁC CỔNG KIỂM ĐỊNH

| Cổng kiểm định | Nội dung kiểm tra | Kết quả | Ghi chú kỹ thuật |
| :--- | :--- | :---: | :--- |
| **Cổng A: Schema** | Định dạng JSON, 4 lựa chọn, đáp án [A-D], giải thích tiếng Việt chi tiết | **120 / 120 PASS** | Cấu trúc dữ liệu chuẩn JLPT |
| **Cổng B: Ngôn ngữ Nhật** | Tính tự nhiên, chuẩn hình thái từ, từ loại, khử mơ hồ phương án nhiễu | **120 / 120 PASS** | Thẩm định ngữ nghĩa, hình thái từ và ngữ cảnh |
| **Cổng C: Giải mù độc lập** | Độc lập giải đề từ mô hình/subagent riêng biệt không có đáp án tác giả | **120 / 120 PASS** | 3 subagent độc lập (`qa/raw_blind_review_*.json`), 100% khớp đáp án tác giả |
| **Cổng D: Phản biện & Đột biến** | Chống trùng ngữ liệu stem, kiểm toán phân bổ phi chu kỳ, kiểm tra lắp ráp câu dấu sao, test đột biến 8 lớp lỗi | **120 / 120 PASS** | Vượt qua 8/8 bài kiểm tra đột biến phản biện tại `scripts/tests/test_qa_adversarial_mutations.py` |
| **Cổng E: Thẩm định thực tế** | Thẩm định bởi học viên và giáo viên hiệu chuẩn độ khó thực tế | **PENDING_LEARNER_CALIBRATION** | Đánh dấu trung thực đang chờ phiên thử nghiệm thực tế với người học |

---

### 3. TÀI LIỆU VÀ CHỨNG CỨ KIỂM TOÁN
- **Báo cáo đối soát giải mù độc lập:** [`qa/BLIND_REVIEW_RECONCILIATION_REPORT.md`](BLIND_REVIEW_RECONCILIATION_REPORT.md)
- **Tập dữ liệu giải mù đầu vào (không có đáp án/giải thích):**
  - Toàn bộ: [`qa/blind_review_dataset.json`](blind_review_dataset.json)
  - N4 (40 câu): [`qa/blind_review_n4.json`](blind_review_n4.json)
  - N3 (50 câu): [`qa/blind_review_n3.json`](blind_review_n3.json)
  - N2 (30 câu): [`qa/blind_review_n2.json`](blind_review_n2.json)
- **Dữ liệu giải mù thô từ Subagent độc lập (Raw Outputs):**
  - N4: [`qa/raw_blind_review_n4.json`](raw_blind_review_n4.json)
  - N3: [`qa/raw_blind_review_n3.json`](raw_blind_review_n3.json)
  - N2: [`qa/raw_blind_review_n2.json`](raw_blind_review_n2.json)
- **Sổ cái kiểm định chi tiết:** [`qa/QUESTION_REVIEW_LEDGER.csv`](QUESTION_REVIEW_LEDGER.csv)
- **Hồ sơ lỗi lịch sử và xử lý:** [`qa/REJECTED_ITEMS.json`](REJECTED_ITEMS.json)
- **Bộ kiểm thử tự động đột biến (8 classes of defects):** [`scripts/tests/test_qa_adversarial_mutations.py`](../scripts/tests/test_qa_adversarial_mutations.py)
