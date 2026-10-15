# KẾ HOẠCH PHÁT TRIỂN VÀ KIỂM ĐỊNH NGÂN HÀNG CÂU HỎI (PHASE 3.7)
## TEST GENERATION, ASSEMBLY & MULTI-STAGE QA PLAN

---

## 1. MỤC TIÊU VÀ PHÂN BỔ CÂU HỎI THEO CẤP ĐỘ

Mục tiêu dài hạn: Xây dựng 300–500 câu hỏi nguyên bản độc lập, có thể kiểm định độc lập.
**Mục tiêu đợt 1 (Milestone 1): 120 CÂU HỎI MỚI NGUYÊN BẢN (100% UNIQUE ITEMS)**

| Cấp độ | Số lượng câu mới | Trọng tâm sư phạm | Phân bổ dạng bài chi tiết |
| :---: | :---: | :--- | :--- |
| **N4** | **40 câu** | Phục hồi và củng cố nền tảng, chữa lỗi trợ từ và thể động từ | • Đọc Kanji (`N4-MO-READ`): 8 câu<br/>• Từ vựng ngữ cảnh (`N4-MO-CONT`): 8 câu<br/>• Trợ từ & Ngữ pháp (`N4-GR-FORM`): 12 câu<br/>• Sắp xếp câu dấu sao (`N4-GR-STAR`): 6 câu<br/>• Đoản văn đời sống (`N4-RD-SHOR`): 4 câu<br/>• Tìm kiếm thông tin (`N4-RD-INFO`): 2 câu |
| **N3** | **50 câu** | Bước đệm chuyển tiếp trung cấp, mở rộng từ ghép và câu phức | • Đọc Kanji (`N3-MO-READ`): 8 câu<br/>• Tiền tố & Hậu tố (`N3-MO-AFFX`): 8 câu<br/>• Từ vựng ngữ cảnh (`N3-MO-CONT`): 8 câu<br/>• Ngữ pháp trung cấp (`N3-GR-FORM`): 12 câu<br/>• Sắp xếp câu dấu sao (`N3-GR-STAR`): 6 câu<br/>• Đọc hiểu đoản văn (`N3-RD-SHOR`): 5 câu<br/>• Đọc hiểu trung văn (`N3-RD-MEDI`): 3 câu |
| **N2** | **30 câu** | Làm quen với áp lực khảo thí, từ vựng học thuật & cấu trúc chính luận | • Đọc Kanji N2 (`N2-MO-READ`): 5 câu<br/>• Cấu tạo từ ghép (`N2-MO-AFFX`): 5 câu<br/>• Từ vựng trừu tượng (`N2-MO-CONT`): 5 câu<br/>• Ngữ pháp nâng cao (`N2-GR-FORM`): 8 câu<br/>• Sắp xếp câu dấu sao (`N2-GR-STAR`): 4 câu<br/>• Đọc hiểu đoản văn công vụ (`N2-RD-SHOR`): 3 câu |
| **TỔNG** | **120 câu** | **Độ phủ cân đối: Từ vựng (47) · Ngữ pháp (48) · Đọc hiểu (25)** | |

---

## 2. QUY CHUẨN DỮ LIỆU CÂU HỎI (QUESTION DATA SPECIFICATION)

Mỗi câu hỏi mới phải tuân thủ nghiêm ngặt cấu trúc trường dữ liệu sau:

```json
{
  "id": "N3-GR-FORM-001",
  "level": "N3",
  "skill": "Grammar",
  "typeId": "N3-GR-FORM",
  "stem": "Câu hỏi bằng tiếng Nhật tự nhiên...",
  "stimulusId": "STIM-N3-001", // hoặc null nếu câu đơn
  "contextPassage": null, // đoạn văn nếu là bài đọc hiểu
  "options": [
    { "id": "A", "text": "Phương án A" },
    { "id": "B", "text": "Phương án B" },
    { "id": "C", "text": "Phương án C" },
    { "id": "D", "text": "Phương án D" }
  ],
  "correctAnswer": "B",
  "explanationVi": "Giải thích chi tiết tại sao B đúng bằng tiếng Việt...",
  "distractorExplanations": {
    "A": "Lý do A sai...",
    "C": "Lý do C sai...",
    "D": "Lý do D sai..."
  },
  "difficultyEstimate": 3,
  "conceptId": "conditional-tara",
  "remediation": "Gợi ý ôn tập cụ thể cho người học khi làm sai câu này...",
  "sourceMetadata": "Original educational authoring, aligned with TUFS grammar module",
  "exposureEligible": true,
  "diagnosticEligible": true,
  "status": "DRAFT" // chuyển thành VERIFIED sau khi qua 5 cổng kiểm định
}
```

---

## 3. QUY TRÌNH 5 CỔNG KIỂM ĐỊNH CHẤT LƯỢNG (5-STAGE QA GATES)

1. **Cổng A — Kiểm tra Schema & Cú pháp kỹ thuật:**
   - Mã ID duy nhất, không trùng lặp.
   - Đủ 4 lựa chọn A, B, C, D (hoặc 3 lựa chọn cho bài nghe phản xạ nếu có).
   - Đáp án đúng nằm trong tập [A, B, C, D].
   - Có đầy đủ giải thích tiếng Việt cho đáp án đúng và từng phương án sai.
2. **Cổng B — Thẩm định Ngôn ngữ Tiếng Nhật:**
   - Câu văn tự nhiên, ngữ pháp chuẩn xác.
   - Đúng âm đọc kanji, không dùng kanji vượt cấp không có furigana (ở N4).
   - Đúng văn phong và cấp độ lịch sự (Desu/Masu ở hội thoại thường nhật, Thể thường/Chính luận ở bài đọc).
   - Không có 2 đáp án cùng đúng (Loại trừ tính mơ hồ của phương án gây nhiễu).
3. **Cổng C — Giải mù độc lập (Independent Blind Solving):**
   - Chạy giải mù độc lập: Giải câu hỏi mà KHÔNG nhìn đáp án có sẵn.
   - So sánh kết quả giải mù với đáp án gốc:
     - Nếu trùng khớp 100%: PASS Cổng C.
     - Nếu có bất đồng ý kiến: Chuyển sang Cổng D để rà soát ngữ pháp đối chiếu.
4. **Cổng D — Thẩm định phản biện (Adversarial Review):**
   - Tìm kiếm bẫy hai phương án đều có lý.
   - Kiểm tra xem bản dịch tiếng Việt có dịch thoát ý chuẩn xác hay không.
   - Đảm bảo độ khó phù hợp với cấp độ được công bố.
5. **Cổng E — Đánh dấu trạng thái thẩm định con người:**
   - Tất cả câu hỏi qua AI QA được ghi nhận rõ ràng: `QA_METHOD: MULTI_STAGE_INDEPENDENT_AI_AUDIT`.
   - Đánh dấu `HUMAN_NATIVE_REVIEW: PENDING` để đảm bảo tính trung thực sư phạm tuyệt đối.

---

## 4. KẾ HOẠCH GHÉP BỘ ĐỀ LUYỆN TẬP (PRACTICE SET FACTORY)

120 câu hỏi mới sau khi kiểm định sẽ được phân bổ thành:
1. **Micro Drills (5 câu / bài · 5–8 phút):** Dành cho những ngày đi làm về mệt.
2. **Skill Practice Sets (10–15 câu / bài · 10–15 phút):** Luyện sâu theo từng phân môn cụ thể (Trợ từ N4, Từ ghép N3, Câu dấu sao N2).
3. **Mixed Practice Sets (15–20 câu / bài):** Tổng hợp kiến thức Từ vựng - Ngữ pháp trong một cấp độ.
4. **Independent Diagnostic Sets (Bộ đề đánh giá chẩn đoán độc lập):** Giữ cách ly, không dùng chung câu hỏi với các bộ luyện tập hàng ngày.
