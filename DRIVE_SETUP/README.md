# Drive-first — cài một lần, học từ một bảng

**Hiện tại:** đã tạo thư mục riêng tư và Google Sheets 5 tab, đã tải 7 PDF và prompt. **Google Forms chưa được tạo/chạy thật** trong phiên này: kết nối có Drive/Sheets nhưng không có API Forms hoặc thực thi Apps Script; trình duyệt cần đăng nhập. Bộ tạo 10 quiz và pipeline đã kiểm bằng dữ liệu giả/API mô phỏng, chưa thay thế nghiệm thu live.

Người học chỉ mở bảng **JP_STUDY_HOC_HOM_NAY**. Link tài khoản riêng được bàn giao trong chat, không lưu ở GitHub. Không tạo website mới; ứng dụng Phase 3 cũ được giữ như checkpoint nguồn.

## Người quản lý làm một lần trên laptop

1. Mở đúng bảng Google Sheets bằng tài khoản sở hữu. Chọn **Tiện ích mở rộng → Apps Script**. Thay nội dung `Code.gs` bằng toàn bộ [JP_STUDY_SETUP.gs](JP_STUDY_SETUP.gs). Đây là một tệp tự chứa; không cần API key, dự án Cloud trả phí hoặc nhập ID riêng.
2. Lưu, chạy **setupP0**. Tập lệnh tự xác định bảng được gắn và hai thư mục cha theo tên, lưu ID trong Script Properties riêng. Nó tạo **3 quiz đầu chưa xuất bản**, một bảng dữ liệu gốc riêng và mỗi Form một trigger nộp. Nếu mất kết nối/chạm giới hạn thời gian, chạy lại; không xóa phản hồi hoặc tạo lại quiz đã hoàn tất.
3. Google yêu cầu người sở hữu xét quyền Sheets, Forms, Drive và tạo trigger. Drive cần để đặt file/báo cáo trong đúng thư mục; script không gửi email, không đọc Gmail, không gọi AI/API ngoài, không chia sẻ công khai, không xóa dữ liệu. Đọc mã trước khi cấp quyền. Không vượt cảnh báo an ninh hoặc gửi mật khẩu trong chat.
4. Mở từng Form vừa tạo trong **02_BÀI_HỌC_VÀ_ĐỀ_LUYỆN/TUẦN_01**. Kiểm **Settings → Release grades → Immediately after each submission**; cho xem câu sai/đáp án sau nộp. Script có khóa/feedback nhưng không cấu hình hoặc xác minh được mọi tùy chọn giao diện về trả điểm. Tắt thu email và tóm tắt phản hồi chung.
5. Trong **Publish/Manage responders**, chọn đúng người học/tài khoản thử, tránh “Anyone with link”. Không cấp quyền chỉnh sửa Form cho người học. Tạo quiz ở trạng thái chưa publish để tránh tự mở rộng người trả lời. Chỉ publish sau khi kiểm đối tượng; quyền responder và quyền editor là hai việc khác nhau.
6. Nộp thử với **Lần làm = QA - Dữ liệu giả**, có đúng/sai/bỏ trống. Xem điểm và lời giải chỉ SAU nộp. Các bản thử được cách ly khỏi lịch sử học, giữ trong dữ liệu gốc và `NHAT_KY_QA`, không bị tự xóa. Có thể xóa thủ công đúng phản hồi thử nếu chủ sở hữu muốn; không dùng xóa hàng loạt.
7. Kiểm **auditForms**. Để kiểm đủ luồng lịch sử/gói lỗi/export, dùng một bản sao thử riêng với một lượt dữ liệu giả chọn “Tự làm”; đối chiếu điểm → lịch sử → ID lỗi → B9 → CSV. Không trộn bản sao thử này vào bảng học thật. Kết quả mô phỏng ở repo không chứng minh trigger Google đã chạy.
8. Khi cả ba Form đạt, chạy **activateReady** và xác nhận đúng nội dung kiểm trực tiếp. Chỉ Form đã publish và audit đúng khóa mới hiện link trong bảng. Chưa xác minh thì giữ “Chờ kích hoạt Forms”. Sau khi P0 live đạt mới chạy **setupRemaining** để tạo 7 quiz còn lại; làm cùng kiểm trước khi giao.

Nếu trình duyệt chưa chạy được Apps Script, dùng các liên kết nghe/nói đã có; quiz và lịch sử tự thu còn chờ kích hoạt. Không bịa link hoặc nhập điểm như thể Forms đã thu. Không cần chờ quiz để nghe một đoạn hoặc tập nói.

## Dữ liệu và sử dụng hằng ngày

- **HỌC HÔM NAY:** tối đa ba lựa chọn, nghỉ là hợp lệ. **TUẦN NÀY:** năm hoạt động từ kho W01/W02, không phải lịch bắt buộc theo ngày. Trạng thái có dropdown; bỏ một ngày không bị báo đỏ hoặc mất chuỗi.
- **LỊCH SỬ:** timestamp nộp, bộ/ID, đúng/tổng/trống, mới tự báo/ôn/hỗ trợ, trạng thái, lỗi, mức mệt tùy chọn. Timestamp không được đổi thành phút học.
- **LỖI CẦN ÔN:** chỉ dữ liệu câu đã nộp; nhấn giữ ô B9 → sao chép toàn bộ ô → dán Gemini. Ô có thể chỉ hiện một phần do dài; thao tác sao chép ô lấy cả gói. Không có dữ liệu thì không có khóa tương lai ở bảng.
- **BÁO CÁO QUẢN LÝ:** thống kê theo kỹ năng và loại lần làm; tỷ lệ đúng chia cho đã trả lời, số trống nằm riêng. Dưới 5 câu mới đã trả lời mỗi nhóm ghi chưa đủ mẫu; đủ 5 cũng chưa chứng minh tiến bộ. Mới là tự báo, không biết lịch sử ngoài hệ thống.
- Menu **JP-STUDY → Xuất báo cáo hôm nay** trên web laptop tạo CSV/JSON riêng trong **05_THEO_DÕI_TIẾN_BỘ/BAO_CAO_XUAT**. Bản xuất cũ được đổi tên giữ lại. Múi giờ mặc định Asia/Tokyo, đổi tại B3 của báo cáo nếu cần; đây không phải lịch ngủ. Không có lần nộp thì ghi “Không có hoạt động học mới.” trong phạm vi dữ liệu đã thu. Nghe/nói hoặc học không nộp chưa được ghi, không suy ra không học.
- Trigger có lỗi/quyền hết hiệu lực: chủ sở hữu chạy **syncResponses**. ID phản hồi + ID câu chống trùng; phản hồi xung đột bị báo lỗi, không ghi đè. Raw Form responses và bảng CHI_TIET giữ nguyên; lịch sử/lỗi/báo cáo là các view được dựng lại từ raw.

## Quyền truy cập và giới hạn điện thoại

Mọi tệp tạo hiện chỉ có chủ sở hữu; chưa biết tài khoản người học nên chưa chia sẻ. Không chia sẻ thư mục gốc hoặc thư mục dữ liệu gốc. Khi giao, cấp đúng tài khoản cho bảng và các PDF cần dùng, và quyền trả lời cho từng Form. Bảng 5 tab phù hợp khi chủ sở hữu và người học được phép xem cùng dữ liệu. Nếu cần thêm người quản lý với mức bí mật khác, dùng một file báo cáo riêng với quyền riêng; ẩn tab không phải kiểm soát truy cập.

HOME được thiết kế rộng 338 px với hai cột; tab tuần/bảng quản lý rộng hơn, nên xem ngang hoặc trên laptop. Menu cài/xuất được thiết kế cho web laptop; chưa xác minh trên ứng dụng Sheets mobile. Chưa thử điện thoại/iPad thật hoặc giao diện Form trực tiếp. Nộp dở chưa bấm Submit không tạo phản hồi, hệ thống không biết đã mở bao nhiêu câu.

## Học liệu, nguồn và tái tạo

[PDF ngắn](../deliverables/phase3.5/) · [Gemini chữa lỗi](../GEMINI_CHUA_LOI.md) · [AI phân tích](../DAILY_AI_ANALYSIS_PROMPT.md) · [Quiz plan](../QUIZ_FORMS/quiz_plan.json) · [QA](../DRIVE_FIRST_QA.md).

80 câu/4 vai/31 thẻ nguồn vẫn nguyên; 10 quiz dùng lại 68 câu không nghe, 12 câu còn dự trữ gồm 8 câu nghe. Không dùng bản chép để giả đo nghe. Nghe đời sống dùng MP3 liên kết chính thức; không tái phân phối âm thanh. Chưa có ngân hàng N3/N2.

Tái tạo bằng runtime có Artifact Tool/Node/Python: chạy `scripts/drive_first/build_bundle.py`, `build_dashboard.mjs` rồi `cache_link_labels.py`; PDF dùng `build_pdfs.py`, kiểm `verify_pdfs.py`. Chạy `node scripts/drive_first/test_drive_first.cjs`. Kết quả và bản xuất chứa link riêng chỉ ở `tmp/`, không commit.

API đã đối chiếu: [Forms và feedback](https://developers.google.com/apps-script/reference/forms/form), [item responses có thể bỏ các câu trống khỏi mảng](https://developers.google.com/apps-script/reference/forms/form-response#getItemResponses()), [trigger cài đặt](https://developers.google.com/apps-script/guides/triggers/installable), [cài trả điểm trong giao diện](https://support.google.com/docs/answer/7032287?hl=en). Vì vậy mapper dùng item ID, không suy vị trí mảng; không hứa có thể cấu hình mọi cài đặt điểm qua script.

Liên kết động trong script dùng [RichTextValueBuilder](https://developers.google.com/apps-script/reference/spreadsheet/rich-text-value-builder), tránh dấu phân cách công thức theo locale; Google Sheet được kiểm lại nhãn và URL sau sửa.
