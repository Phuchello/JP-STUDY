# Trạng thái dự án — 15/10/2026

## Đã hoàn thành

- Phase 1: nghiên cứu, kế hoạch tạm thời, tracker; bản gốc giữ local, bản Markdown công khai thay hồ sơ thật bằng ví dụ tổng hợp.
- Phase 2: hướng dẫn bắt đầu/chẩn đoán, prompt gia sư, tracker v2, nguồn và QA.
- Phase 2.1: sổ tay tích hợp 12 trang bản gốc, tracker 5 trang tính và prompt cuối; bản công khai sổ tay bằng Markdown đã lược hồ sơ.
- Phase 3 Checkpoint 1–3: ledger, 14 kỹ thuật, schema, pilot, chấm và chọn bài, Gemini; chạy văn bản offline, xuất/nhập tiến độ, phân biệt câu mới/ôn/hỗ trợ.
- Phần Excel của Checkpoint 4 và kiểm giao pilot: tracker 6 trang tính, CSV 12 cột, giây nguyên; năm trang cũ được giữ nguyên.
- Phụ lục: 31 thẻ mẫu, 37 ví dụ chỉ để học; 12 khung viết/nói; mẹo đọc/nghe có nguồn và phân biệt heuristic.
- Đồng bộ công khai: bản gốc không bị ghi đè, kiểm kê nguồn có SHA-256, bản công khai lược hồ sơ và đường dẫn máy, giữ nội dung đã QA.

## Đã kiểm định và còn cần sửa

| Hạng mục | Số lượng | Phạm vi |
|---|---:|---|
| Câu trắc nghiệm N4 | 80 | AI khác giải mù toàn bộ lượt đầu; sửa và tái kiểm có mục tiêu; không tuyên bố giải mù toàn bộ lần hai |
| Vai nói | 4 | Rà độc lập; không có một đáp án duy nhất |
| Thẻ / ví dụ học | 31 / 37 | Rà lũy kế, không cộng vào ngân hàng 80 câu |
| Recipe | 30 | Ghép lại cùng ngân hàng 80, không phải 30 đề độc lập |
| Phát hiện nội dung còn mở sau tái kiểm cuối | 0 | Chỉ trong phạm vi AI QA được ghi; chưa có thẩm định bản ngữ |

QA lịch sử: engine 421 nhóm, browser 36 mục, luồng bổ sung 11, Excel native 64, toàn vẹn 28; kết quả này thuộc bản gốc tại checkpoint. Bản công khai kiểm lại phần bị ảnh hưởng; xem [PUBLICATION_QA](qa/PUBLICATION_QA.md), không coi hash PDF mới là hash PDF cũ.

## Đang làm / chưa làm

- Checkpoint 4 **một phần**: chưa mở rộng 300–500 câu, chưa có ngân hàng N3/N2. Chưa tuyên bố hoàn thành toàn Phase 3.
- Chưa có dữ liệu chẩn đoán hoặc thử nghiệm người học thật mới, nên không có dự báo xác suất đỗ, tốc độ học hay lịch tuần cố định.
- Chưa hiệu chuẩn độ khó/thời gian, chưa thẩm định giáo viên bản ngữ, chưa kiểm iPad thật hoặc nghe TTS bằng âm thực.
- Mã build lịch sử là **DRAFT**, có phụ thuộc tệp trung gian; không phải pipeline tái tạo toàn bộ chỉ bằng một lệnh.
- Nguồn sau paywall chỉ dùng trong giới hạn abstract/metadata được ghi; lỗi Crossref 429/404 không được tính là xác minh.

## Checkpoint tiếp theo

Thu dữ liệu tự nguyện ngày 7/14 và thử người học trên thiết bị thực; kiểm giọng Nhật hoặc chọn MP3 chính thức. Sửa vấn đề được quan sát rồi mới duyệt mở rộng từng lô. Mỗi lô phải giữ ID/khóa/schema đồng bộ, QA độc lập theo phạm vi, cập nhật manifest/docs, commit và push. Không sinh thêm câu chỉ để đủ số lượng.
