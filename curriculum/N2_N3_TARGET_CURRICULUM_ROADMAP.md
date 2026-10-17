# KẾ HOẠCH ĐIỀU CHỈNH CHƯƠNG TRÌNH & NỘI DUNG JP-STUDY
## MỤC TIÊU CỐT LÕI: KỲ THI JLPT N2 — THÁNG 12/2026

---

### 1. NGUYÊN TẮC PHÂN BỔ MỚI (CURRICULUM WEIGHTING)

Từ ngày 17/10/2026, dự án JP-STUDY chính thức chuyển đổi trọng tâm từ kiểm định kỹ thuật N4 sang **Luyện thi JLPT N2 Tháng 12/2026**.

Tỉ trọng phân bổ nội dung và thời lượng học tập mặc định:

```
┌──────────────────────────────────────────────────────────┐
│  JLPT N2 (50%) — MỤC TIÊU THI CHÍNH THÁNG 12/2026        │
│  Từ vựng học thuật, ngữ pháp công sở/văn viết,           │
│  đọc hiểu trung-dài, luyện nghe audio thật, mô phỏng thi │
├──────────────────────────────────────────────────────────┤
│  JLPT N3 (40%) — LỚP GIA CỐ NỀN TẢNG TIÊN QUYẾT         │
│  Bù đắp lỗ hổng từ vựng-ngữ pháp trung cấp,              │
│  chẩn đoán điểm yếu, đọc hiểu đoạn văn ngắn-vừa          │
├──────────────────────────────────────────────────────────┤
│  JLPT N4 (10%) — CHỮA LỖI & ÔN TẬP NHANH (REMEDIATION)   │
│  Chỉ kích hoạt khi chẩn đoán phát hiện rỗng trợ từ/thể   │
│  hoặc người học cần bài tập siêu ngắn (3-5 phút) ca đêm  │
└──────────────────────────────────────────────────────────┘
```

> **Nguyên tắc linh hoạt:** Tỉ lệ 50/40/10 là phân bổ ban đầu. Sau khi người học hoàn thành bài kiểm tra chẩn đoán năng lực (Diagnostic Test), hệ thống sẽ tự động điều chỉnh tỉ trọng dựa trên dữ liệu hiệu suất thực tế.

---

### 2. KẾT QUẢ KIỂM TOÁN TÀI NGUYÊN HIỆN CÓ (N3 & N2 AUDIT)

Kho câu hỏi chuẩn hoá `curriculum/QUESTION_BANK_EXPANDED.json` (120 câu) và `curriculum/PRACTICE_SETS.json` (23 bộ đề) hiện đã có sẵn nguồn tài nguyên N2/N3 chất lượng cao, **không cần tạo câu hỏi mới khi chưa tận dụng hết tài nguyên đã thẩm định**:

#### A. Tổng hợp câu hỏi N2 & N3 trong ngân hàng câu hỏi
- **Tổng số câu N2**: 30 câu
  - 26 câu `QA_VERIFIED` (100% độc lập, không có lỗi ngữ nghĩa)
  - 4 câu `STAR_SEMANTIC_REVIEW_PENDING` (`N2-GR-STAR-001` đến `004`)
  - Phân loại: 15 Từ vựng (Cách đọc, Cấu tạo từ phức, Ngữ cảnh), 12 Ngữ pháp, 3 Đọc hiểu ngắn (`N2-RD-SHOR-001` đến `003`).
- **Tổng số câu N3**: 50 câu
  - 44 câu `QA_VERIFIED` (100% độc lập, không có lỗi ngữ nghĩa)
  - 6 câu `STAR_SEMANTIC_REVIEW_PENDING` (`N3-GR-STAR-001` đến `006`)
  - Phân loại: 24 Từ vựng (Cách đọc, Tiền tố/Hậu tố, Ngữ cảnh), 18 Ngữ pháp, 8 Đọc hiểu (5 Đoạn ngắn, 3 Đoạn vừa).
- **Tổng cộng N3 + N2 đã kiểm định**: **70 câu hỏi `QA_VERIFIED`**.

#### B. Các bộ đề N2 & N3 đã sẵn sàng triển khai (`QA_PASSED_NOT_DEPLOYED` - 100% QA_VERIFIED)
1. **`MD-N2-VOC-01`**: N2 Micro-Drill | Kanji & Từ vựng nâng cao (5 câu · 5 phút)
2. **`MD-N2-AFF-01`**: N2 Micro-Drill | Cấu tạo từ phức N2 (5 câu · 5 phút)
3. **`MD-N2-GRA-01`**: N2 Micro-Drill | Mẫu câu văn viết & công sở N2 (5 câu · 6 phút)
4. **`SK-N2-MO-01`**: N2 Skill Practice | Từ vựng học thuật & Đời sống (15 câu · 15 phút)
5. **`MD-N3-VOC-01`**: N3 Micro-Drill | Đọc Kanji trung cấp (5 câu · 5 phút)
6. **`MD-N3-AFF-01`**: N3 Micro-Drill | Tiền tố & Hậu tố ghép từ (5 câu · 5 phút)
7. **`MD-N3-GRA-01`**: N3 Micro-Drill | Mẫu ngữ pháp trung cấp N3 (5 câu · 6 phút)
8. **`SK-N3-MO-01`**: N3 Skill Practice | Chuyên sâu Từ vựng & Cấu tạo từ (16 câu · 15 phút)

👉 **Tổng cộng: 8 bộ đề N2/N3 (62 lượt câu hỏi)** sẵn sàng đóng gói đưa vào bài học cho người học ngay lập tức!

#### C. Các bộ đề đang tạm dừng do 10 câu hỏi dấu sao (★) chờ thẩm định ngữ nghĩa
- N3: `SK-N3-GR-01` (18 câu), `MX-N3-INT-01` (20 câu), `SIM-N3-GENGO` (24 câu).
- N2: `SK-N2-GR-01` (12 câu), `MX-N2-ADV-01` (18 câu).
- Khắc phục: Chỉ cần chạy quy trình thẩm định ngữ nghĩa mù (Blind Semantic Review) cho 10 câu dấu sao (`N3-GR-STAR-001..006` và `N2-GR-STAR-001..004`) là sẽ tự động mở khoá toàn bộ 5 bộ đề chuyên sâu này.

---

### 3. LỘ TRÌNH TRIỂN KHAI NỘI DUNG 7 BƯỚC ƯU TIÊN

```
Bước 1: Chẩn đoán N3 (Grammar & Vocab Diagnostic)
  │     └─ Đo lường nền tảng hiện tại của người học, chỉ ra chính xác lỗ hổng.
  ▼
Bước 2: Đọc hiểu N3 nhắm trúng điểm yếu
  │     └─ 8 bài đọc hiểu N3 (Đoạn văn đời sống, thông báo công việc).
  ▼
Bước 3: Micro-Drills Từ vựng & Ngữ pháp N2
  │     └─ Đưa các bài 5 phút (MD-N2-VOC-01, MD-N2-AFF-01, MD-N2-GRA-01) vào nhịp học hàng ngày.
  ▼
Bước 4: Đọc hiểu N2 tăng dần độ dài đoạn văn
  │     └─ Đoạn văn ngắn (N2-RD-SHOR-001..003) -> Đoạn văn trung và dài (bình luận, xã luận).
  ▼
Bước 5: Luyện nghe N2 với Audio thực tế phát được
  │     └─ Bắt buộc có file âm thanh phát được trực tiếp (NHK, tư liệu bản quyền mở).
  │     └─ Tuyệt đối KHÔNG mô tả bài tập đọc thành bài tập nghe.
  ▼
Bước 6: Luyện thi theo khối thời gian N2 (Timed Sectional Practice)
  │     └─ SIM-N2-GENGO (Kiến thức ngôn ngữ: 30-35 phút), SIM-N2-DOKKAI (Đọc hiểu: 50-60 phút).
  ▼
Bước 7: Thi thử toàn diện N2 (Full JLPT N2 Mock Exam)
        └─ Chỉ công bố khi đạt đủ tối thiểu 85-105 câu hỏi độc lập chưa từng gặp (unseen) và audio chuẩn.
        └─ Tuyệt đối KHÔNG dán nhãn đề tự tạo thành "đề thi thật quá khứ" (JLPT Past Papers).
```

---

### 4. TRẢI NGHIỆM NGƯỜI HỌC (LEARNER EXPERIENCE POLICY)

1. **Giao diện Cổng học tập (Google Sites & Sheets)**:
   - Thay đổi cấu trúc trang chủ: Đưa phần **MỤC TIÊU N2 (Tháng 12/2026)** lên vị trí nổi bật nhất.
   - Hiển thị bài tập N2/N3 kế tiếp cần làm ngay tại đầu trang.
   - **Xoá bỏ hoàn toàn rào cản tuần tự**: Tuyệt đối không bắt người học phải hoàn thành hết các bài N4 mới được mở N3 hay N2. Người học có toàn quyền truy cập trực tiếp bài tập N2/N3 bất cứ lúc nào.
2. **Hỗ trợ người đi làm theo ca (Shift Worker Design)**:
   - Duy trì các phiên siêu ngắn 5–7 phút (Micro-Drills) làm nhanh trên tàu hoặc trước khi ngủ.
   - Thiết lập tùy chọn phiên luyện sâu 20–30 phút cho ngày nghỉ hoặc ngày làm ca ngắn.
   - Không gây áp lực chuỗi ngày học, mệt thì nghỉ; hệ thống chỉ lưu nhận diện lỗi sai để tối ưu thời gian ôn tập.

---

### 5. CHÍNH SÁCH PHÁT TRIỂN & RELEASE QA

- **Dừng mở rộng ngân hàng câu hỏi N4**: Không bổ sung thêm câu hỏi N4 mới trừ khi người học bộc lộ lỗ hổng cụ thể qua bài kiểm tra.
- **Tập trung biên soạn & thẩm định N2**: Toàn bộ chu kỳ bổ sung nội dung tiếp theo sẽ tập trung vào Từ vựng - Ngữ pháp - Đọc hiểu N2.
- **Bảo toàn 100% tài nguyên đã xác thực**: Giữ nguyên 3 Forms P0 nền tảng (`W01-B01` đến `W01-B03`) và biểu mẫu Pilot `MD-N4-VOC-01`.
- **QA tương xứng rủi ro**: Chấm dứt việc mở rộng bài test hồi quy vô hạn; tập trung vào tính khả dụng và hiệu quả thực tế của người học.
