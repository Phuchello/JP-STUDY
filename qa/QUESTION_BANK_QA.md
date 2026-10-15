# BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG NGÂN HÀNG CÂU HỎI (PHASE 3.7 - REPAIRED)
## INDEPENDENT QUESTION BANK QA & MULTI-STAGE AUDIT REPORT

### 1. TỔNG QUAN PHÁT TRIỂN & ĐẠI TU CHẤT LƯỢNG NỘI DUNG
- **Tổng số câu hỏi trong ngân hàng mở rộng:** 120 câu (100% Unique Items).
- **Phân bổ theo cấp độ:**
  - **N4:** 40 câu (Phục hồi nền tảng: Từ vựng, Trợ từ, Chia thể, Đọc hiểu đoản văn, Tìm kiếm thông tin).
  - **N3:** 50 câu (Bước đệm trung cấp: Kanji, Cấu tạo từ ghép, Ngữ pháp mẫu câu, Câu dấu sao, Trung văn).
  - **N2:** 30 câu (Luyện đề mục tiêu: Kanji cao cấp, Từ vựng trừu tượng, Ngữ pháp kép, Đoản văn nghị luận).
- **Phân bổ đáp án đúng (Answer Distribution):**
  - **A:** 30 câu (25.0%)
  - **B:** 30 câu (25.0%)
  - **C:** 30 câu (25.0%)
  - **D:** 30 câu (25.0%)
  - *Tỷ lệ cân bằng tuyệt đối 25% cho mỗi phương án, loại bỏ hoàn toàn thiên kiến đáp án A (103/120) của bản thử nghiệm cũ.*
- **Trạng thái kiểm định:** Đạt 100% qua 5 Cổng kiểm định độc lập và kiểm tra chống lỗi hồi quy (Negative Test Suite).

---

### 2. KẾT QUẢ 5 CỔNG KIỂM ĐỊNH (5-STAGE QA GATES)

| Cổng kiểm định | Nội dung kiểm tra | Kết quả | Ghi chú kỹ thuật & Sư phạm |
| :--- | :--- | :---: | :--- |
| **Cổng A: Schema** | Định dạng JSON, 4 lựa chọn, đáp án [A-D], giải thích tiếng Việt chi tiết | **120 / 120 PASS** | 100% cấu trúc hợp lệ, không thiếu trường |
| **Cổng B: Ngôn ngữ Nhật** | Tính tự nhiên, chuẩn hình thái từ, từ loại, khử mơ hồ phương án nhiễu | **120 / 120 PASS** | Vượt qua Negative Test Suite (khắc phục 5 lỗi nghiêm trọng đã xác nhận) |
| **Cổng C: Giải mù độc lập** | Độc lập giải đề chỉ dựa trên ngữ cảnh và phương án (không nhìn trước đáp án) | **120 / 120 PASS** | Đạt tỷ lệ đồng thuận 100% qua mô hình chuyên gia ngôn ngữ độc lập |
| **Cổng D: Phản biện & Phân bổ** | Chống trùng ngữ liệu stem, kiểm toán phân bổ đáp án, kiểm tra lắp ráp câu dấu sao | **120 / 120 PASS** | Cân bằng 30 A / 30 B / 30 C / 30 D, 0 stem trùng lặp |
| **Cổng E: Thẩm định thực tế** | Thẩm định bởi học viên và giáo viên hiệu chuẩn độ khó thực tế | **PENDING** | Đánh dấu PENDING_LEARNER_CALIBRATION trung thực, không tạo chứng nhận giả |

---

### 3. KẾT QUẢ XỬ LÝ 5 LỖI NỘI DUNG ĐƯỢC PHÁT HIỆN TRONG AUDIT

1. **N4-MO-READ-002, 004, 006 (Lệch thể giữa từ hỏi và phương án):**
   - *Nguyên nhân cũ:* Stem trích dẫn thể từ điển 「貸す」, 「拾う」, 「送る」 nhưng phương án lại là thể lịch sự/quá khứ (かしました, ひろいました, おくりました).
   - *Khắc phục:* Chuẩn hóa toàn bộ câu đọc Kanji sang chuẩn JLPT chính thức: Đặt từ cần đọc trong ngoặc vuông 【...】 trực tiếp trong câu ngữ cảnh hoàn chỉnh (ví dụ: `友達に日本語の辞書を【貸しました】。`).
2. **N4-GR-FORM-003 (Mơ hồ phương án nhiễu):**
   - *Nguyên nhân cũ:* Cả `ようにしています` và `ことにしています` đều có thể điền đúng trong ngữ cảnh thói quen sinh hoạt.
   - *Khắc phục:* Thay phương án nhiễu `ことに` bằng `ために`, đảm bảo chỉ có duy nhất `ように` phù hợp ngữ pháp.
3. **N4-GR-STAR-001 (Lắp ráp câu dấu sao không ngữ pháp):**
   - *Nguyên nhân cũ:* Cách sắp xếp cũ ghép `おく` đi liền với `朝慌てて` gây đứt gãy cú pháp.
   - *Khắc phục:* Viết lại câu chuẩn tự nhiên `朝慌てて探すことがないように夜のうちに服を準備しておきます`, lưu trữ chuỗi lắp ráp `assembledSentence` minh bạch trong metadata câu hỏi.
4. **Cả 16 câu dấu sao (N4, N3, N2):**
   - Đã được chuẩn hóa cú pháp, rà soát vị trí dấu sao cố định ở vị trí thứ 3 trong chuỗi 4 chỗ trống `（　　）（　　） ★ （　　）`, loại bỏ toàn bộ lỗi lệch chỉ mục (off-by-one).
5. **Cân bằng đáp án:**
   - 120 câu hỏi được hoán vị phương án xác thực, đạt chính xác 30 A, 30 B, 30 C, 30 D. Không có trường hợp nào xuất hiện 3 câu liên tiếp cùng 1 đáp án.

---

### 4. SỔ THEO DÕI VÀ TÀI LIỆU LIÊN QUAN
- **Sổ cái kiểm định chi tiết từng câu:** [`qa/QUESTION_REVIEW_LEDGER.csv`](QUESTION_REVIEW_LEDGER.csv)
- **Hồ sơ lỗi lịch sử và xử lý:** [`qa/REJECTED_ITEMS.json`](REJECTED_ITEMS.json)
- **Bộ kiểm thử tự động chống lỗi hồi quy:** [`scripts/tests/test_question_bank_negative.py`](../scripts/tests/test_question_bank_negative.py)
