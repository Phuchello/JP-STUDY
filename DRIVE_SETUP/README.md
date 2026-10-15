# Drive-first — cài một lần, học từ một bảng

**Hiện tại:** Cả ba Form P0 (18 câu) đã được tạo, audit khóa, nộp QA thật và kích hoạt hoàn tất (`activateP0Verified`). Bảng học **JP_STUDY_HOC_HOM_NAY** hiển thị `Sẵn sàng` với link `MỞ BÀI NGẮN`. Toàn bộ dữ liệu QA được cách ly an toàn (0 learner rows). Báo cáo quản lý xuất tự động đạt. [Bằng chứng triển khai](../qa/drive_first_deployment.json) phân biệt kiểm thật và mock.

Người học chỉ mở bảng **JP_STUDY_HOC_HOM_NAY**. Link tài khoản riêng được bàn giao trong chat, không lưu ở GitHub. Không tạo website mới; ứng dụng Phase 3 cũ được giữ như checkpoint nguồn.

## Quy trình cài mới hoặc tiếp tục bằng công cụ được ủy quyền

Với dự án hiện có, tác tử triển khai tiếp tục chạy các hàm qua trình duyệt đã đăng nhập; không yêu cầu owner chạy từng hàm. Owner chỉ xử lý đăng nhập, cảnh báo an ninh và xét quyền Google. Không tạo lại dự án, không xóa Script Properties hoặc ba Form để né lỗi.

1. Mở đúng bảng Google Sheets bằng tài khoản sở hữu. Chọn **Tiện ích mở rộng → Apps Script**. Dùng toàn bộ [JP_STUDY_SETUP.gs](JP_STUDY_SETUP.gs) trong tệp mã hiện có (có thể là `macro.gs`). Đây là một tệp tự chứa; không cần API key, dự án Cloud trả phí hoặc nhập ID riêng. Hiện manifest trong Project Settings rồi đối chiếu [appsscript.json](appsscript.json): scope đầy đủ cho bảng raw riêng, Drive Advanced v3 và Asia/Tokyo. Không chỉ dán mã rồi bỏ qua manifest.
2. Lưu, chạy **setupP0**. Tập lệnh tự xác định bảng được gắn và hai thư mục cha theo tên, lưu ID trong Script Properties riêng. Nó tạo **3 quiz đầu chưa xuất bản**, một bảng dữ liệu gốc riêng và mỗi Form một trigger nộp. Nếu mất kết nối/chạm giới hạn thời gian, chạy lại; không xóa phản hồi hoặc tạo lại quiz đã hoàn tất.
3. Google yêu cầu người sở hữu xét quyền Sheets, Forms, Drive, tạo trigger và menu của bảng. Bật **Services → Drive API v3** nếu chưa có; việc chấp nhận điều khoản và OAuth do owner quyết định. Drive cần để đặt file/báo cáo và kiểm/gỡ quyền responder công khai; script không gửi email, đọc Gmail hoặc gọi AI/API ngoài. Không xóa dữ liệu. Không vượt cảnh báo an ninh hoặc gửi mật khẩu trong chat. Nếu `openById` báo thiếu `spreadsheets`, kiểm manifest rồi hoàn tất quyền Google; không đổi sang chia sẻ công khai hoặc coi Completed của `onOpen` là triển khai thành công.
4. Mở từng Form vừa tạo trong **02_BÀI_HỌC_VÀ_ĐỀ_LUYỆN/TUẦN_01**. Kiểm **Settings → Release grades → Immediately after each submission**; cho xem câu sai/đáp án sau nộp. Script có khóa/feedback nhưng không cấu hình hoặc xác minh được mọi tùy chọn giao diện về trả điểm. Tắt thu email và tóm tắt phản hồi chung.
5. Chạy `restrictP0Responders` trong chế độ nghiệm thu chỉ owner: chỉ gỡ `anyone / reader / view=published`, không tự thêm người học hoặc gỡ người dùng có tên. Chạy `inspectDeployment` để kiểm native keys/đích raw/mỗi Form đúng một submit trigger, publication state và ACL. `shared=false` không đủ; phải đọc `includePermissionsForView=published`. Tài khoản người học chưa xác nhận thì chỉ owner thử; không cấp quyền editor hoặc chia sẻ root/raw. `publishP0OwnerQa` chỉ publish ba P0 sau khi khóa và ACL chỉ-owner đều đạt, kiểm ACL lần nữa và thu hồi publication nếu ACL bất ngờ thay đổi. Đây là cửa nghiệm thu kỹ thuật, chưa mở link học.
6. Nộp thử với **Lần làm = QA - Dữ liệu giả**, có đúng/sai/bỏ trống. Xem điểm và lời giải chỉ SAU nộp. Các bản thử được cách ly khỏi lịch sử học, giữ trong dữ liệu gốc và `NHAT_KY_QA`, không bị tự xóa. Có thể xóa thủ công đúng phản hồi thử nếu chủ sở hữu muốn; không dùng xóa hàng loạt.
7. Chạy `verifySyntheticQa` sau khi mỗi Form có lượt nộp QA thật. Hàm yêu cầu đúng/sai/trống ở mỗi Form, so điểm Google theo item ID và yêu cầu response ID đã có trong `NHAT_KY_QA` do trigger; không tự gọi trigger để tạo bằng chứng. Hàm chỉ sao chép dashboard khi canonical learner raw còn trống, dựng lịch sử/lỗi/B9 trong một bảng riêng `JP_STUDY_QA_SYNTHETIC` có nhãn QA và xuất `QA_LEARNING_REPORT_*.csv/json` riêng trong `QA_TECHNICAL_ONLY`. Không thêm các lượt thử vào lịch sử thật. Chạy `exportDailyReport` riêng cho bảng học: nếu chưa có lượt học, kết quả phải trung lập. Kết quả mô phỏng không chứng minh trigger Google đã chạy.
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

API đã đối chiếu: [Forms và feedback](https://developers.google.com/apps-script/reference/forms/form), [published-view responder permissions và Drive Advanced v3](https://developers.google.com/workspace/forms/api/guides/publish-form), [item responses có thể bỏ các câu trống khỏi mảng](https://developers.google.com/apps-script/reference/forms/form-response#getItemResponses()), [trigger cài đặt](https://developers.google.com/apps-script/guides/triggers/installable), [cài trả điểm trong giao diện](https://support.google.com/docs/answer/7032287?hl=en). Vì vậy mapper dùng item ID, không suy vị trí mảng; không hứa có thể cấu hình mọi cài đặt điểm qua script. Lỗi Form chưa có đích trả lời được quan sát trực tiếp trên Google; bộ cài bắt đúng lỗi này rồi liên kết raw, không nuốt lỗi quyền hoặc ghi đè đích khác.

Liên kết động trong script dùng [RichTextValueBuilder](https://developers.google.com/apps-script/reference/spreadsheet/rich-text-value-builder), tránh dấu phân cách công thức theo locale; Google Sheet được kiểm lại nhãn và URL sau sửa.
