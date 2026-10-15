# QA — phát hành thí điểm Phase 3 + phụ lục

Ngày kiểm: 15/10/2026. **PASS trong phạm vi bản thí điểm đã triển khai**, với các giới hạn nền tảng/ngôn ngữ bên dưới. Chưa có điểm thực mới của người học; các dữ liệu dùng kiểm thử nằm ngoài gói giao và đã xóa khỏi workbook giao.

## Mốc hoàn thành và phần chưa làm

| Checkpoint | Trạng thái |
|---|---|
| 1 — bằng chứng, schema, thiết kế | Hoàn thành: 14 kỹ thuật, ledger nguồn/độ mạnh và giới hạn |
| 2 — pilot + chấm | Hoàn thành: 80 câu gốc nền N4, 4 vai; QA độc lập đầy đủ lượt đầu và các lượt kiểm thay đổi nối tiếp |
| 3 — chọn bài + Gemini | Hoàn thành trong pilot: ba chế độ, nghỉ, mới/ôn/hỗ trợ, khóa sau nộp, sao chép lỗi/mẫu |
| 4 — mở rộng + Excel | **Một phần:** Excel đã tích hợp; chưa làm 300–500 câu/N3/N2. Có 30 bộ ghép từ 80 câu, không coi là câu độc lập mới |
| 5 — kiểm thử và giao | Đã kiểm bản pilot như bảng dưới; chưa phải nghiệm thu ngân hàng mở rộng |

Mốc liền mạch hoàn thành đầy đủ: **Checkpoint 3**. Các kiểm tra giao diện/dữ liệu của Checkpoint 5 đã làm cho pilot; không gắn nhãn toàn Phase 3 đã hoàn thành quy mô 300–500. Dừng tại giai đoạn thí điểm đã kiểm, ưu tiên thu dữ liệu người học trước khi sinh thêm câu.

## Kiểm nội dung độc lập

- Tác giả soạn; một tác tử AI khác giải mù 80/80 trước khóa, sau đó rà 80 khóa, 240 nhiễu, 22 bằng chứng đọc/nghe và 4 vai. Khóa chữ cái lúc bản nháp khớp 80/80; QA vẫn phát hiện lỗi dữ kiện/lời giải và yêu cầu sửa.
- Lượt đầu có 1 block, 5 major, 10 minor theo **nhóm**. Sửa dữ kiện hàng tới trước ngày nhận, lịch thay đổi đã chốt, lời giải suy đoán, nguồn đích và thẻ người đối thoại. Sau đó kiểm 22 câu có thay đổi/nguồn liên quan, 4 vai; rà lại 80 mapping tới thẻ chữa. Các liên kết sai mục tiêu đã sửa; không có thẻ đúng thì dùng null.
- Thư viện **31 thẻ / 37 câu chỉ để học** được rà lũy kế đầy đủ; ba câu G09 mới cũng được kiểm độc lập. Không gọi 37 câu này là giải mù, không cộng vào 80 câu ngân hàng.
- Lượt cuối PASS; không còn phát hiện cụ thể đang mở. [Báo cáo của người kiểm](ANSWER_KEY_AND_EXPLANATIONS/content_final_reaudit.md), [JSON kiểm định](ANSWER_KEY_AND_EXPLANATIONS/content_final_reaudit.json).
- Không tuyên bố giải mù lại toàn 80 lần hai. Xáo nhãn sau soạn được kiểm bằng 80 mapping đúng nội dung/nhiễu; khóa có digest/phiên bản. Chỉ metadata xác nhận QA được đóng sau phê duyệt; trường dạy học và khóa không đổi, đã đối chiếu hash trước/sau.

## Các kiểm tra thực chạy

| Phần | Kết quả cuối | Phạm vi |
|---|---|---|
| Engine | 421/421 nhóm kiểm đạt | 320 lựa chọn của 80 câu; trống/invalid, buổi dở, đã thấy cùng đoạn/kịch bản, trợ giúp/đoán/gián đoạn, holdout/chậm, 30 recipe, nhập/xuất/xung đột, hồi phục sau lỗi, dùng đúng kỹ năng chẩn đoán |
| Browser | 36 mục ghi nhận, không lỗi JS | 155.0.8059.40; Chrome Windows chạy tự động, tệp local; bàn phím, chấm, lưu/tải lại, clipboard/fallback, gộp JSON, tìm mẫu, khóa, phiếu nói |
| Luồng bổ sung | 11/11 đạt | Offline không gửi HTTP ngoài, chặn mẫu/khóa trong đo, đánh dấu dừng, CSV UTF-8, lưu bị chặn→JSON, mô phỏng callback nghe để kiểm snapshot trước script |
| Excel author | 12/12 đạt | Dòng hợp lệ/trùng/sai số, trợ giúp không vào điểm mới, giây→phút, trống không bịa tỉ lệ |
| Excel thật | 64/64 đạt | Excel 16.0 COM ẩn trên bản sao; chức năng cũ, save/reopen, CSV UTF-8 thực tải từ browser→12 cột→copy vào workbook→phân loại Luyện không thành Mới |
| Toàn vẹn | 28/28 kiểm đạt | 13 tài liệu trước không đổi SHA; 5 worksheet cũ và quan hệ byte giữ nguyên ; 123 liên kết, 142 quy tắc nhập; đối chiếu JSON/JS/HTML/khóa |
| PDF | 19 trang, đúng 3/5/5/6 | Render Poppler từng trang; xem ảnh bố cục và trang chữ lớn; kiểm lề/glyph trích xuất không thấy lỗi |

Kiểm phát hiện CSV phút thập phân bị Excel vùng dấu phẩy đọc thành chữ. Đã đổi riêng cột J của CSV sang **giây nguyên**, workbook tự tính phút; test cuối kiểm đúng dữ liệu thực qua cầu nối. Các worksheet chẩn đoán cũ giữ đơn vị/hành vi cũ.

## Điều kiện đo và tính bền vững

STANDARD/DEEP hiển thị câu mới trước câu ôn, chỉ chữa sau nộp. QUICK và bộ chọn mục tiêu là luyện. Câu có trợ giúp/đã thấy/cùng đoạn/đoán/gián đoạn/quá giờ không vào nhóm câu mới tự làm. Trống khác sai; câu dự kiến chưa mở chưa bị chấm. Mẫu n < 5 không đưa mạnh/yếu chắc chắn. Ôn đúng câu cũ khác chuyển hiểu ở câu mới sau ≥3 ngày. Lịch 1/3/7/14 và ngưỡng mẫu là heuristic.

Chọn bài dùng lỗi gần đây để không giữ người học mãi ở lỗi cũ đã phục hồi; vẫn giữ lịch sử cũ. STANDARD ban đầu lấy mẫu đọc ngắn/từ cùng nền ngữ pháp; chỉ thêm nghe khi có giọng Nhật. Mệt 4–5 không có chẩn đoán mới; buồn ngủ cho nghỉ. Không có cam kết đỗ, điểm chuẩn hay dự báo xác suấtN2.

## Giới hạn đã xác nhận

- **Nội dung:** QA do AI, chưa giáo viên bản ngữ/thử người học; độ khó/thời gian và cấp N4 là ước lượng. Một số nguồn JF vẫn ở cấp khóa, không xác nhận mọi từ đúng trang.
- **Nghe:** chỉ kịch bản/khóa được rà. Probe thực thấy3 giọng tiếng Anh, không có giọng Nhật. Ứng dụng bỏ câu nghe khi thiếu giọng và không lấy giọng tiếng Anh thay thế. Test UI callback bằngstub **không phải nghe âm thực**; chưa kiểm phát âm/nhịp/tốc độ hay chất lượng âm trên iPad. Có liên kết MP3JF chính thức để luyện ngoài, không giả là điểm JLPT.
- **Nền tảng:** viewport1280×900,768×1024,1024×768,390×844 không tràn ngang; nút chính≥44px. Đây là mô phỏng màn hình, không phải kiểm iPad/Safari thật hoặc người chạm màn hình thật. iPadFiles có thể chỉ previewHTML.
- **Dữ liệu:** localStorage có thể khác theo trình duyệt/địa chỉ/chế độ riêng tư. Đã thử tải lại ởChrome và mô phỏng bị chặn lưu. Phải dùng JSON để sao lưu/chuyển thiết bị; không đồng bộ hay tự ghi Excel. JSON chỉnh tay không phải hồ sơ chống gian lận.
- **AI:** chỉ sao chép để người học tự dán Gemini; chưa kiểm trong tài khoản thật, không đọc lịch sử/nhập phản hồi tự động. NotebookLM tùy chọn, không bảo đảm tính năng theo gói cấp tài khoản.
- **Quy mô:** chưa 300–500 câu, chưa ngân hàng N3/N2 hay 100+ mini-test độc lập. 30 recipe có thể thiếu câu mới/âm Nhật tùy lịch sử; giao diện nói rõ ôn/không đủ câu, không tạo câu chưa rà để bù.

13 tài liệu trước vẫn giữ nguyên trong các thư mục cũ. Tất cả tệp giao ở FINAL_PHASE3; dữ liệu kiểm thử/build/render ngoài gói. Không có điểm người học, tài khoản hay API key được thêm vào gói.
