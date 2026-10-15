# Bắt đầu ở một màn hình

Mở [ứng dụng học](JLPT_PRACTICE/index.html) bằng Chrome/Edge trên laptop. Không cần cài, đăng nhập hay API. Khi mệt, có thể chọn nghỉ. Hướng dẫn ngắn: [START_HERE.pdf](START_HERE.pdf).

Trong ứng dụng: làm 5–15 phút → nộp → xem một lỗi → học mẫu liên quan hoặc sao chép cho Gemini → dừng. Tiến độ tự lưu khi trình duyệt cho phép. Trước khi đổi thiết bị, địa chỉ mở hoặc xóa dữ liệu trình duyệt, xuất JSON trong **Sao lưu**. Không có đồng bộ tự động.

## Các tệp dùng khi cần

| Tệp | Khi mở |
|---|---|
| JLPT_PRACTICE/index.html | Giao diện chính; văn bản và mã đã gói trong một tệp để giảm lỗi mở local |
| START_HERE.pdf | Ba trang hướng dẫn, mốc D7/D14 và sáu câu bổ sung dữ liệu tùy chọn |
| LEARNING_METHODS.pdf | 14 kỹ thuật, năm trang; chỉ chọn một kỹ thuật hôm nay |
| LISTENING_READING_CHEATSHEETS.pdf | Năm trang: dạng thi chính thức và cách tìm ý/bằng chứng |
| JAPANESE_WRITING_SPEAKING_TEMPLATES.pdf | Sáu trang, 12 khung dùng ở trường/nơi làm; không phải phần thi viết JLPT |
| JAPANESE_PATTERN_LIBRARY/patterns.json | 31 thẻ có tìm kiếm trong ứng dụng, 37 câu học có hướng dẫn; dữ liệu cho chủ dự án |
| GEMINI_ERROR_TUTOR.md | Prompt chữa một lỗi, chờ trả lời và checkpoint mang theo |
| JLPT_PROGRESS_TRACKER.xlsx | Năm trang cũ giữ nguyên; trang “Luyện tập” nhận CSV tùy chọn |
| ANSWER_KEY_AND_EXPLANATIONS/index.html | Khóa sau bài; mở chi tiết trong ứng dụng sẽ đánh dấu đã xem |
| RESEARCH_EVIDENCE_LEDGER.md / QA_REPORT.md | Nguồn, cách kiểm và giới hạn cho người phụ trách |

80 câu trắc nghiệm gốc nền N4 và bốn vai nói được giữ riêng. 30 bộ ghép dùng lại cùng 80 câu, không phải 30 đề mới độc lập. 37 câu trong thư viện chỉ để học, không cộng vào 80 câu của ngân hàng. Chưa mở rộng 300–500 câu hoặc ngân hàng N3/N2.

Mở tệp local đã được kiểm trên Chrome Windows; bố cục iPad chỉ được mô phỏng, chưa dùng iPad thật. iPad Files có thể chỉ xem trước HTML; nếu không chạy được, dùng laptop. Giữ cấu trúc thư mục để các liên kết PDF hoạt động. Có thể học văn bản offline; Gemini, nguồn ngoài và một số giọng TTS cần mạng. Máy kiểm thử không có giọng Nhật, ứng dụng tự bỏ câu nghe trong phiên chọn tự động; không phát tiếng Anh thay tiếng Nhật.

## CSV → Excel, nếu muốn tổng hợp

1. Trong ứng dụng chọn **Sao lưu → Xuất CSV**. JSON mới là bản sao đầy đủ của lịch sử và buổi dở.
2. Mở CSV bằng Excel với UTF-8 và dấu phẩy. Sao chép **12 cột dữ liệu A–L**, bỏ dòng tiêu đề, vào trang **Luyện tập** từ A8. Cột J là **giây nguyên**, Excel tự tính tổng phút; cách này tránh lỗi dấu thập phân theo vùng.
3. Khi cập nhật, thay cả vùng nhập A8:L507 bằng bản xuất mới hoặc thêm dưới. Dòng trùng Session ID + kỹ năng + loại dữ liệu bị loại sau dòng đầu. Cột M báo dữ liệu cần kiểm. Vượt 500 dòng thì lưu bản cũ và dùng bản mới hoặc nhờ mở rộng; không dán đè công thức cột M.

Ứng dụng không mở/sửa Excel, không điều khiển Gemini, không đọc lịch sử tài khoản. Nguồn chính thức đã có liên kết trong sổ cũ. Điểm bài gốc, điểm có hỗ trợ và chẩn đoán chính thức được xem riêng.
