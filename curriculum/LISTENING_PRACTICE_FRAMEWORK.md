# JP-STUDY — KHUNG PHƯƠNG PHÁP & QUY CHUẨN LUYỆN NGHE (LISTENING FRAMEWORK)

> **Nguyên tắc cốt lõi**:
> 1. *Nghe phải thực sự là nghe*: Tuyệt đối không hiển thị transcript (kịch bản chữ) trước khi người học hoàn thành lượt nghe và nộp bài đầu tiên.
> 2. *Minh bạch nguồn gốc tư liệu*: Phân biệt rạch ròi giữa tư liệu bản quyền giáo dục chính thức (Japan Foundation Irodori, NHK World, JEES Sample), thu âm độc quyền, và giọng đọc máy (TTS). Tuyệt đối không dán nhãn giọng đọc trình duyệt/TTS là "băng thi thật JLPT".
> 3. *Đúng định dạng bản quyền*: Không sao chép hoặc phân phối trái phép CD/audio thương mại từ sách ôn luyện trên thị trường.

---

## 1. PHÂN LOẠI NGUỒN TƯ LIỆU NGHE (PROVENANCE CODES)

| Mã Phân loại | Tên danh mục | Nguồn gốc | Ứng dụng trong JP-STUDY |
|---|---|---|---|
| `OFFICIAL_EXTERNAL` | Tư liệu giáo dục chính thức | Japan Foundation (Irodori), NHK World-Japan, JEES Sample | Luyện nghe đời sống thực tế, làm quen giọng bản xứ, nghe tin tức thời sự hàng ngày. |
| `ORIGINAL_RECORDED` | Thu âm bản ngữ nội bộ | Người Nhật bản xứ thu âm theo kịch bản tình huống độc quyền | Luyện phản xạ công sở và giao tiếp thực tế Nhật Bản. |
| `SYNTHETIC_PEDAGOGICAL_TTS` | Âm thanh tổng hợp hỗ trợ | Giọng đọc AI/TTS chất lượng cao | Chỉ dùng cho bài tập phát âm từ đơn, tra cứu cách đọc; **KHÔNG** dùng làm đề thi nghe mô phỏng. |
| `EXAM_SIMULATION_AUDIO` | Băng thi thử chuẩn hóa | Studio đa diễn viên, mô phỏng đúng thời lượng và tiếng chuông thi JLPT | Dùng cho kỳ thi thử hoàn chỉnh. Trạng thái hiện tại: `UNRELEASED_PENDING_AUDIO_CLEARANCE`. |

---

## 2. QUY TRÌNH HỌC TẬP 3 BƯỚC CHO PHẦN NGHE (LEARN → LISTEN → REVIEW)

### Bước 1: Nghe nắm bắt (First Blind Attempt)
- Người học chỉ được tiếp cận: Câu hỏi gợi ý mục tiêu (VD: *"Người phụ nữ sẽ làm gì trước tiên?"*) và các lựa chọn đáp án.
- Không hiển thị bất kỳ đoạn văn bản hội thoại nào.
- Ghi nhận: Người học nghe bao nhiêu lần (1 lần duy nhất chuẩn thi, hay nghe lại 2-3 lần).

### Bước 2: Nộp đáp án & Nhận phản hồi
- Hệ thống chấm điểm tự động, ghi nhận câu trả lời đúng/sai vào bảng tổng hợp.
- Hiển thị đáp án đúng kèm lý do giải thích ngắn gọn bằng tiếng Việt.

### Bước 3: Xem Transcript & Kỹ thuật Shadowing
- Lúc này mới mở khóa toàn bộ kịch bản tiếng Nhật kèm bản dịch tiếng Việt.
- Bôi đậm các từ khóa then chốt (signals) và liên từ chuyển ý (VD: *実は, でも, やっぱり, それより*).
- Hướng dẫn người học kỹ thuật Shadowing (nói đuổi theo giọng đọc) để cải thiện đồng thời cả phát âm và tốc độ phản xạ.

---

## 3. LỘ TRÌNH TRIỂN KHAI VÀ TRẠNG THÁI KHẢ DỤNG

1. **Hiện tại (Phase 3.7 - Checkpoint 3.7-B & 3.7-C)**:
   - Tích hợp cổng tư liệu nghe chất lượng cao từ `Irodori (A2 & B1)` và `NHK World` trên trang **NGHE & NÓI** của Google Sites.
   - Thử thách luyện phát âm đời sống tích hợp trợ lý gia sư Gemini.
2. **Kỳ thi thử đầy đủ (Mock Exam Listening)**:
   - Được đánh dấu rõ ràng: `NOT_READY — INSUFFICIENT UNIQUE ITEMS / UNRELEASED_PENDING_AUDIO_CLEARANCE`.
   - Cam kết bảo đảm tính trung thực học thuật, không tạo đề thi giả mạo bằng cách trích đoạn đọc hiểu để làm bài nghe.
