# Trạng thái dự án — 15/10/2026

## Phase 3.5 — nghiệm thu P0 hoàn tất, kích hoạt Forms thành công

- Đã tạo Drive riêng tư đúng cấu trúc, một Google Sheet native 5 tab, 7 PDF ngắn (9 trang), vai nói và hai prompt. Link thật bàn giao riêng, không đưa lên GitHub.
- Đã đọc lại ô/validation/quyền bằng API: HOME 2 cột, trạng thái sẵn sàng, lịch sử sạch (0 learner rows), chỉ chủ sở hữu truy cập. Liên kết động trong bộ cài dùng rich text theo chuẩn Google.
- Đã xuất từ chính native Sheets để rà 5 tab; responsive testing đạt trên kích thước mobile (390 px) và laptop (1280 px).
- Bộ cài tự nhận bảng được gắn, tạo quiz, giữ raw responses, cách ly QA, chống trùng và xuất CSV/JSON. 10 quiz dùng lại 68 câu đã QA; 12 câu nguồn còn dự trữ, không tăng ngân hàng.
- **394/394 kiểm logic/Workspace mock đạt.** Đã thực thi Apps Script gắn với bảng qua trình duyệt: `setupP0` và `auditForms` hoàn tất; đúng 3 Form P0 (18 câu), 1 bảng raw với ba tab phản hồi. Không tạo 7 P1 khi chưa có nhu cầu.
- Sửa lỗi Google thực tế: `getDestinationId()` ném lỗi khi Form chưa có đích; bộ cài bắt đúng lỗi này và liên kết bảng raw.
- Bật Drive Advanced Service v3 với sự đồng ý của owner. Đã gỡ quyền `anyone` của responder từ cả ba Form; đọc lại `includePermissionsForView=published` xác nhận mỗi Form chỉ có owner.
- **Đã nghiệm thu live P0 trọn vẹn:** Đã cấu hình trả điểm ngay sau khi nộp (Immediate release) cùng phản hồi chi tiết. Thực hiện nộp QA giả lập thực tế trên cả 3 Form qua browser automation; điểm số hiển thị chính xác (W01-B01: 3/5, W01-B02: 6/8, W01-B03: 3/5) với đầy đủ mẫu câu đúng, sai và bỏ trống. Trigger `onQuizSubmit` phân luồng dữ liệu QA vào `NHAT_KY_QA` và tạo bảng riêng `JP_STUDY_QA_SYNTHETIC` mà không ghi đè vào lịch sử người học (`learnerRows: 0`). Đã chạy `activateP0Verified`: cell B6 hiện `Sẵn sàng`, B7 hiện link `MỞ BÀI NGẮN`, tab `TUẦN NÀY` mở link 3 Form P0. Đã chạy thử xuất báo cáo quản lý CSV/JSON thành công vào Drive. [Bằng chứng đã lược thông tin riêng](qa/drive_first_deployment.json).
- Báo cáo chỉ phản ánh lượt quiz đã nộp. Nghe/nói/học ngoài hệ thống chưa ghi; không suy ra không học, không suy phút học từ timestamp, không coi điểm ôn tăng là tiến bộ độc lập.

Nghiệm thu và giới hạn: [DRIVE_FIRST_QA](DRIVE_FIRST_QA.md). Cài/kích hoạt: [DRIVE_SETUP](DRIVE_SETUP/README.md).

## Các checkpoint trước đã hoàn thành

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

Hoàn tất OAuth cho script đã gắn, rồi tiếp tục nghiệm thu trực tiếp 3 Form P0 từ làm → nộp → điểm → lỗi → Gemini → lịch sử → CSV bằng dữ liệu QA trong bảng riêng; sau đó mới mở 7 Form P1. Thu dữ liệu tự nguyện ngày 7/14 và thử người học trên thiết bị thực; kiểm giọng Nhật hoặc chọn MP3 chính thức. Sửa vấn đề được quan sát rồi mới duyệt mở rộng từng lô. Mỗi lô phải giữ ID/khóa/schema đồng bộ, QA độc lập theo phạm vi, cập nhật manifest/docs, commit và push. Không sinh thêm câu chỉ để đủ số lượng.
