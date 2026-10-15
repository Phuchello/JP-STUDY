# Phase 3.5 — QA và điểm bàn giao

Ngày kiểm: 15/10/2026. **Checkpoint một phần: Drive/Sheets/tài liệu đã tạo; Forms và luồng Google end-to-end QA_PENDING.** Không có dữ liệu người học thật trong repo hoặc bảng mẫu. Không gọi mock là kiểm Google.

| Hạng mục | Kết quả | Bằng chứng / giới hạn |
|---|---|---|
| Nguồn cũ | VERIFIED toàn vẹn | 80 câu, 4 vai, 31 thẻ/37 ví dụ, khóa và fingerprint QA giữ nguyên; release validator kiểm lại |
| 10 quiz specification | VERIFIED mapping; live QA_PENDING | 68 ID duy nhất dùng lại, 5–9 câu/bài, mỗi câu 1 điểm; từng lựa chọn A–D so với khóa độc lập. Không sinh câu mới |
| Logic và Workspace adapter | VERIFIED trong mock | [387 kiểm](qa/drive_first_tests.json): bỏ trống không lệch vị trí; 2 đúng/2 sai/1 trống; chống trùng/xung đột; ôn/hỗ trợ/không rõ; cách ly QA; giữ raw; sửa lỗi rồi gỡ ứng viên; múi giờ và CSV; tạo 3 rồi 10 Form chưa publish, chạy lại không trùng |
| Tự nhận bảng/thư mục | VERIFIED trong mock | Từ chối bảng sai, thiếu bảng hoặc thư mục cha mơ hồ; không nhúng ID riêng; lưu Script Properties của chính project |
| Drive và Sheet thật | VERIFIED qua API có giới hạn | 10 thư mục; 1 native Sheet + 12 file tải lên. Đọc lại 5 tab, HOME 2 cột, dropdown và 5 việc tuần; lịch sử trống, điểm/mức mệt chưa có. Root và 13 file đều chỉ owner, shared=false |
| Liên kết native | VERIFIED qua readback | Đã sửa 3 ô #ERROR do dấu phân cách locale; HOME không còn lỗi trong A1:B22, 4 link tới lỗi/nghe/vai nói/hướng dẫn có đúng nhãn và URL; link Gemini ở thẻ lỗi hợp lệ. Adapter dùng rich-text link theo API Google |
| Bố cục bảng | VERIFIED bản template/export | Rà 5 tab từ chính XLSX xuất của native Sheets; HOME khoảng 338 px, chữ Arial 12. Không chứng minh UI Google; kiểu Table có khác biệt qua XLSX. Chưa kiểm phone/iPad thật |
| PDF | VERIFIED 7 PDF / 9 trang | Poppler render + rà trực quan + text/link/margin; guide 2 trang, mỗi thẻ 1–2 trang. [Kết quả public](qa/drive_first_pdfs.json). Không phát hành bản trung gian chứa link riêng |
| Quyền, trả điểm, trigger Google | QA_PENDING | Cần đăng nhập và chủ sở hữu chạy script; không có Forms/execution API qua kết nối hiện tại. Chưa có FormURL đã nghiệm thu |
| Thử người học, hiệu chuẩn, mốc 7/14 | QA_PENDING | Chưa có dữ liệu mới; không dự báo đỗ N2, không suy tiến bộ từ điểm ôn |

## Cổng nghiệm thu trực tiếp trước khi giao

- [ ] Người sở hữu đăng nhập đúng Google, mở Apps Script gắn với bảng và xét quyền.
- [ ] `setupP0` tạo đúng 3 quiz chưa publish; `auditForms` đạt mọi item/khóa/điểm.
- [ ] Trước Submit: không có khóa, feedback, bản chép hoặc tóm tắt đáp án; không tự lộ trong description/help.
- [ ] Cấu hình Release grades ngay sau nộp và chỉ đối tượng responder dự kiến; kiểm bằng tài khoản responder thật, không dùng quyền editor để suy ra quyền người học.
- [ ] Mỗi quiz nộp QA có đúng/sai/trống; xem điểm và lời giải sau nộp; điểm khớp ID nguồn, câu trống không dồn vị trí.
- [ ] QA được giữ trong raw/nhật ký QA và không thành lịch sử người học.
- [ ] Trong bản sao thử riêng: lượt tự làm giả đi qua raw → lịch sử → lỗi → gói B9 → CSV/JSON; nộp lại/đồng bộ không trùng; lượt ôn không thành câu mới.
- [ ] Không có lần nộp: báo cáo ghi trung lập “Không có hoạt động học mới.” và nói rõ phạm vi; không tự tạo điểm, phút học hoặc mức mệt.
- [ ] Copy ô B9 đầy đủ sang Gemini; gói khớp đúng câu đã nộp, chọn/khóa/giải thích; Gemini hỏi từng lượt và chờ.
- [ ] Kiểm HOME/Form trên thiết bị người học; không phải đọc folder tree; rồi mới `activateReady` và giao link.
- [ ] Sau P0 live đạt, tạo và kiểm 7 P1; chưa đạt thì không mở link của quiz chưa nghiệm thu.

Không ẩn tab để thay quyền. Không chia sẻ root/raw. Khi cần khác mức bí mật, dùng file báo cáo riêng. Mẫu CSV chỉ có header; bản xuất thật giữ riêng trong Drive, không commit.

## Dữ liệu đo được và giới hạn suy luận

Ngày 7: ưu tiên số lượt đã nộp, số bỏ trống, có mở/chữa được một lỗi, vướng thao tác và mức mệt tự báo nếu có; giảm độ dài khi quá tải. Ngày 14: tách mới/ôn/hỗ trợ và kỹ năng, xem lỗi lặp đang mở; chỉ đề xuất bài mới tương đương chưa xem nếu đủ sức. Mốc tối thiểu 5 câu mỗi nhóm chỉ là heuristic mô tả, không phải ngưỡng thống kê hay bằng chứng tiến bộ. Nghe/nói ngoài quiz chưa có log; không coi không nộp là không học. Theo [prompt phân tích](DAILY_AI_ANALYSIS_PROMPT.md), không tăng lịch hoặc cắt ngủ tự động.

## Tái kiểm

1. `python scripts/drive_first/build_bundle.py`
2. `node scripts/drive_first/test_drive_first.cjs`
3. Khi thay bố cục/PDF, chạy builder và kiểm ảnh theo [setup](DRIVE_SETUP/README.md).
4. `python scripts/update_manifest.py` rồi `python scripts/validate_release.py`.

Raw proof/ảnh native export và deployment state chỉ ở local `tmp/drive-first/`; không đưa ID riêng hoặc URL tải có chữ ký vào báo cáo công khai. [Native link API](https://developers.google.com/apps-script/reference/spreadsheet/rich-text-value-builder) là cơ sở cho sửa liên kết; hành vi chấm/feedback vẫn cần kiểm trên Google.
