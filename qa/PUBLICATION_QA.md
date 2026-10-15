# QA bản công khai — 15/10/2026

**VERIFIED trong phạm vi đồng bộ pilot công khai.** Bản này không có dữ liệu tiến bộ thật. Giữ nguyên các bản gốc tại máy; thay hồ sơ bằng ví dụ tổng hợp trong các bản công khai. Không thay câu hỏi, khóa, thẻ mẫu hoặc hành vi ứng dụng.

| Kiểm tra | Kết quả / phạm vi |
|---|---|
| Source inventory | 299 tệp thường, SHA-256 và số byte; 134 nguồn được xuất bản hoặc có đối tác công khai, 165 giữ local; không theo junction runtime |
| Byte payload cuối | Ngân hàng, patterns, khóa và ứng dụng giữ nguyên byte từ checkpoint được QA; hai fingerprint nội dung khớp báo cáo độc lập |
| Chạy lại engine | 421/421 nhóm đạt trên payload trong repo |
| Chạy lại browser | 36/36 mục đạt, không lỗi JS; Chrome Windows, tệp local, bố cục iPad mô phỏng |
| Chạy lại luồng bổ sung | 11/11 đạt: offline, chặn storage→xuất JSON, kiểm trợ giúp/nghe bằng callback giả; không phải kiểm âm thực |
| PDF công khai thay hồ sơ | START_HERE 3 trang; dựng lại bằng ReportLab, render Poppler cả 3 và xem ảnh từng trang; không thấy chồng/cắt chữ hoặc mất glyph |
| Các PDF còn lại | 5 PDF giữ nguyên byte, rà văn bản và nguồn; không có hồ sơ định danh/giờ làm cụ thể. Không chạy lại QA bố cục cho tệp không đổi |
| Workbook | 4 checkpoint khác nhau, không trùng binary; giữ nguyên byte, kiểm toàn bộ gói XML/metadata và vùng nhập hiện hành trống. Tái sử dụng QA native Excel 64/64 và author 12/12 của pilot; không tuyên bố chạy Excel native lần nữa cho bản đồng bộ không sửa workbook |
| Nội dung bên thứ ba | Không phân phối PDF/MP3 JLPT tải về, HTML nguồn, raw search/fetch/full text; có tổng hợp gốc, DOI và liên kết nguồn |
| Kích thước / bí mật / hồ sơ | Kiểm tự động mọi payload văn bản và XML workbook, cộng rà thủ công các bản báo cáo/prompt/PDF; không có credential, đường dẫn user, hồ sơ hoặc nhật ký thật được duyệt đưa lên. Regex là lớp hỗ trợ, không chứng minh phát hiện mọi PII |
| Markdown / manifest | Kiểm mọi đích liên kết Markdown tương đối tồn tại, SHA-256/số byte khớp mọi tệp (trừ chính MANIFEST.json), không binary trùng hoặc tệp ≥50 MiB |

[Kết quả chạy hiện hành](current/) khác với [kết quả lịch sử](historical/). Validator ghi kết quả mới vào `tmp/publication_validation.json` bị Git bỏ qua; có thể chạy lại bằng `python scripts/validate_release.py`. `qa/file_status.json` giữ phạm vi nhãn đã duyệt; tệp mới mặc định QA_PENDING.

## Giới hạn và phần còn thiếu

AI QA độc lập chưa phải thẩm định bản ngữ. Chưa hiệu chuẩn người học, chưa thử iPad thực, chưa kiểm âm TTS; máy kiểm không có giọng Nhật. Chưa có ngân hàng 300–500 câu hoặc N3/N2. Mã build lịch sử là DRAFT, không phải pipeline tái tạo toàn bộ. Không suy tỉ lệ đúng thành điểm chuẩn hoặc xác suất đỗ.

## Xác minh GitHub

Kho trước đồng bộ rỗng; không có lịch sử bị ghi đè. Sau push phải fetch và so local HEAD với origin/main, đối chiếu tree/blob và đọc metadata commit trên GitHub. Kết quả SHA/URL thực được báo sau push; phần này không tự xác nhận một push chưa diễn ra.
