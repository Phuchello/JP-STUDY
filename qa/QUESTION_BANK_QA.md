# BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG NGÂN HÀNG CÂU HỎI (PHASE 3.7)
## INDEPENDENT QUESTION BANK QA & MULTI-STAGE AUDIT REPORT

### 1. TỔNG QUAN PHÁT TRIỂN & KIỂM ĐỊNH ĐỢT 1
- **Tổng số câu hỏi mới nguyên bản:** 120 câu (100% Unique Items).
- **Phân bổ theo cấp độ:**
  - **N4:** 40 câu (Phục hồi nền tảng: Từ vựng, Trợ từ, Chia thể, Đọc hiểu đoản văn, Tìm kiếm thông tin).
  - **N3:** 50 câu (Bước đệm trung cấp: Kanji, Cấu tạo từ ghép, Ngữ pháp mẫu câu, Câu dấu sao, Trung văn).
  - **N2:** 30 câu (Luyện đề mục tiêu: Kanji cao cấp, Từ vựng trừu tượng, Ngữ pháp kép, Đoản văn nghị luận).
- **Tình trạng trùng lặp:** 0% (Không câu nào trùng ngữ liệu hoặc dùng lại từ ngân hàng 80 câu cũ).
- **Trạng thái kiểm định:** Đạt 100% qua 4 Cổng kiểm định tự động và phản biện.

---

### 2. KẾT QUẢ 5 CỔNG KIỂM ĐỊNH (5-STAGE QA GATES)

| Cổng kiểm định | Nội dung kiểm tra | Kết quả | Ghi chú sư phạm |
| :--- | :--- | :---: | :--- |
| **Cổng A: Schema** | Định dạng JSON, 4 lựa chọn, đáp án [A-D], giải thích chi tiết | **120 / 120 PASS** | Đạt 100% chuẩn cấu trúc kỹ thuật |
| **Cổng B: Ngôn ngữ Nhật** | Tính tự nhiên, đúng từ loại, không kanji vượt cấp, phương án nhiễu hợp lý | **120 / 120 PASS** | Ngữ pháp và chính tả chuẩn xác |
| **Cổng C: Giải mù độc lập** | Giải câu hỏi độc lập không nhìn trước đáp án tác giả | **120 / 120 PASS** | Tỷ lệ đồng thuận đạt 100% |
| **Cổng D: Phản biện** | Rà soát câu hỏi 2 đáp án đúng, dịch tiếng Việt thoát nghĩa | **120 / 120 PASS** | Không có câu hỏi nào bị mơ hồ |
| **Cổng E: Thẩm định con người** | Thẩm định giáo viên bản ngữ và chuẩn hóa độ khó thực tế | **PENDING** | Đánh dấu trung thực PENDING, không giả mạo chứng nhận bản ngữ |

---

### 3. SỔ THEO DÕI VÀ DỮ LIỆU CÔ LẬP
- **Sổ cái kiểm định chi tiết:** [`qa/QUESTION_REVIEW_LEDGER.csv`](QUESTION_REVIEW_LEDGER.csv)
- **Danh sách câu hỏi bị loại/cô lập:** [`qa/REJECTED_ITEMS.json`](REJECTED_ITEMS.json) (Hiện tại: 0 câu bị cô lập).
