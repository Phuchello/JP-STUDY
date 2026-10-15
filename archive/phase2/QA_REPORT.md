> Bản công khai: hồ sơ người học đã được thay bằng ví dụ tổng hợp; không chứa kết quả hay lịch cá nhân. Đây là checkpoint lịch sử, không phải hướng dẫn mới nhất.

# Kết quả kiểm tra hệ thống JLPT phiên bản 2

Ngày kiểm tra 15/10/2026. Hoàn thành sáu đầu ra; các tệp dựng, ảnh kiểm tra và dữ liệu thử nằm ngoài FINAL.

## Kết quả xác nhận

| Hạng mục | Kết quả và phạm vi |
|---|---|
| Bảo toàn bản gốc | Cả 3 mã SHA256 không đổi. Dữ liệu và 68 công thức cũ được giữ trong workbook mới; chỉ thay hướng dẫn được phép và thêm phần cần thiết. |
| PDF | START HERE 2 trang, chẩn đoán 4 trang, khổ A4. Đã render và xem cả 6 trang: dấu tiếng Việt, chữ Nhật, bảng và chân trang hiển thị đúng, không thấy chồng chữ hoặc tràn lề. Trang 2 START HERE là bảng dùng hằng ngày một trang. |
| Công thức và luồng nhập | 60/60 kiểm thử đạt; mở lại tệp đã lưu và tính lại không phát hiện lỗi công thức. Kiểm ô trống/0, mẫu số 0, số đúng vượt tổng, số lẻ/chữ ở ô đếm, thời gian/ngày thiếu, mã không hợp lệ, trùng câu mới, ranh giới tuần và đổi tuần. |
| Chẩn đoán | 66 mã câu được đối chiếu với đề/khóa 2018, chia 11 khối. Kiểm câu 0 vẫn nằm trong mẫu số, không thể gắn Đúng cho 0, câu nghe 3 lựa chọn không nhận 4, trộn mới/cũ trở thành Ôn lại. Chưa đủ khối thì không sinh điểm tổng hợp giả. |
| Đo lường | N4/N3/N2 và từng kỹ năng riêng; chỉ câu Mới hợp lệ được tổng hợp theo tuần. Nghe/nói, giấc ngủ và mệt có cỡ mẫu riêng. Không tính xác suất đỗ hoặc quy đổi độ đúng thô thành điểm JLPT. Toàn bộ dữ liệu thử đã được xóa khỏi tệp giao. |
| Danh sách chọn và ràng buộc | 20 quy tắc nhập, có thông báo dừng lỗi và cho để trống khi chưa biết. Đã kiểm cấu trúc Excel, phạm vi 0–4/0–3, giờ ngủ 0–24, mệt 1–5 và lựa chọn loại câu. Chưa thao tác xác nhận hộp thoại trên Excel bản máy/iPad. |
| Liên kết trong Excel | 79 liên kết gốc Excel, gồm 13 điều hướng nội bộ; đã kiểm tên trang, ô đích và đích PDF. Nhãn hiển thị rõ; không còn thông báo công thức HYPERLINK không hỗ trợ. |
| Nguồn và prompt | Giữ S01–S20, thêm đúng một nghiên cứu nghe S21; tách bằng chứng nghiên cứu với mẹo sư phạm. Một prompt gia sư, có nhật ký chuyển tiếp, luôn tự làm trước, có phương án không Live/không phát âm thanh. |

## Kiểm tra liên kết trực tuyến

Đối chiếu 48 URL duy nhất của đầu ra, gồm liên kết trong cả hai PDF. **47/48 URL phản hồi HTTP 2xx** bằng HEAD hoặc GET giới hạn khi HEAD không phù hợp. Hai phản hồi 206 là phần PDF được yêu cầu kiểm tra, hai phản hồi 203 là trang PubMed. Không coi HEAD 404 ban đầu của Google là link hỏng trước khi thử GET.

Cả **10 liên kết MP3** trả về thành công, gồm 9 MP3 JLPT và 1 MP3 Irodori; các PDF/khóa/bản chép cần cho quy trình bắt đầu đã truy cập được và tên tệp khớp nguồn. Không phát âm thanh trên thiết bị của người học và không tái phân phối tệp đề/MP3.

Đã thay đường dẫn tham khảo S10 sang PDF của tác giả tại Purdue và S11 sang PubMed vì máy chủ gốc chặn truy cập/chuỗi chứng chỉ không xác minh được; giữ nguyên nghiên cứu và DOI. S21 trỏ đến hồ sơ ERIC của cùng bài, nội dung đã đọc được qua Exa nhưng **kiểm tra HTTP trực tiếp vẫn timeout**. Không báo rằng mọi liên kết đều đã vượt kiểm tra trực tiếp; lỗi này không chặn bài học, chẩn đoán hay nhập tiến bộ.

## Phần còn chưa biết

- Chưa có điểm chẩn đoán cá nhân, giờ ngủ, số ca khuya/tuần hoặc quỹ phút bền vững. Các mức thời gian và ngưỡng phần trăm là quy tắc thử nghiệm; vài câu không chứng minh trình độ hay khả năng đỗ.
- Chưa thử bấm liên kết, hộp thoại nhập và hiển thị trực tiếp trong Excel/Numbers trên iPad của người học. Đã kiểm file, công thức, điều hướng và ảnh bằng công cụ dựng; START HERE có cách ghi giấy/ghi chú rồi nhập trên laptop nếu iPad chưa mở được.
- Chưa chạy prompt trong tài khoản Gemini của người học hoặc xác nhận quyền Live. Phương án chat chữ + MP3 + nói thành tiếng vẫn dùng được theo hướng dẫn; không giả định trí nhớ tự động.
- Quy định tuyển sinh cá nhân nằm ngoài phạm vi bản công khai; chưa xác minh điều kiện trường cụ thể.

## Thao tác đầu tiên của người học

Ngày bình thường: mở START HERE trang 1 → trang Chẩn đoán trong workbook → khối N4-G1, câu 1–6, 6 phút → nhập F8:F13 → tự chấm G8:G13 bằng khóa chính thức → bấm Ghi ngày/phút và điền H78/I78/J78. Lưu lỗi rồi mở Master Tutor. Ngày kiệt sức: nghỉ hoặc ôn cũ tối đa 10 phút; không ép hoàn thành khối này.
