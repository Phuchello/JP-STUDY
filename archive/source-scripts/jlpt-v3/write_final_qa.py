from pathlib import Path
import json
R=Path(__file__).resolve().parents[2];T=R/'tmp/jlpt-v3';O=R/'FINAL_V3';a=json.loads((T/'final_audit.json').read_text(encoding='utf-8'))
q=f'''# QA FINAL - tích hợp và kiểm tra khả năng sử dụng

Ngày kiểm tra: 15/10/2026. Hoàn tất đúng bốn đầu ra trong FINAL_V3. Không mở lại nghiên cứu hay đổi chiến lược N4 → N3 → N2. Các mức phút và ngưỡng sư phạm tiếp tục là mức thử, không phải khả năng đã xác nhận hay dự báo đỗ.

## Kết quả cuối

| Hạng mục | Đã kiểm và kết quả |
|---|---|
| Bảo toàn nguồn | SHA256 của cả 6 tệp Phase 2 và 3 tệp Phase 1 không đổi. Dữ liệu lịch sử/ngày có sẵn không bị đổi. |
| Công thức cũ | {a['v2_formulas_unchanged']} công thức Phase 2 giữ nguyên; {a['v2_formulas_changed_for_scope']} công thức được đổi đúng phạm vi: 40 ô tổng hợp chẩn đoán và 9 ô dashboard để nhận chế độ nhanh. 68 công thức có từ Phase 1 vẫn nằm nguyên vị trí/nội dung. Không thay lịch sử bằng số tĩnh. |
| Kiểm thử bằng Artifact Tool | **{a['artifact_tests']}/{a['artifact_tests']} đạt**. Ô trống/0, bỏ câu, sai/chữ/số lẻ/ngoài phạm vi, khối dở dang, thiếu ngày/phút/loại câu, điểm chưa lộ trước Xong, trộn nhanh/chi tiết, xung đột hai chế độ, mới/ôn lại, ngày bắt đầu sai và D7/D14 động. Đã mở lại bản xuất cuối và tính lại: không có lỗi công thức trong vùng quét. |
| Excel desktop thực tế | **{a['native_excel_tests']}/{a['native_excel_tests']} đạt** bằng Microsoft Excel **{a['native_excel_version']}** chạy ẩn qua COM trên bản sao. Mở đúng Làm nhanh, kiểm validation và địa chỉ link, nhập/sửa sáu đáp án, chấm, ghi ngày/phút, tổng hợp từng khối, loại ôn lại, tính lại toàn bộ, lưu, đóng và mở lại. Quét ô công thức lỗi sau mở lại: 0. Đây là kiểm engine Excel thực, không phải thao tác bấm của người dùng trên giao diện. |
| Khóa chấm tự động | **66/66 đáp án** khớp bảng khóa chính thức N4/N3 năm 2018 bằng bộ trích bảng độc lập với mảng khóa nhúng, đồng thời xem ảnh cả 4 trang khóa. Đã thử toàn bộ 11 khối đúng hết, sai một câu, bỏ toàn bộ; câu 3 lựa chọn không nhận 4. Số 0 nằm trong mẫu số; trống vẫn chưa hoàn tất. |
| Điều hướng và ràng buộc | {a['hyperlinks']} liên kết Excel, trong đó {a['internal_links']} nội bộ; {a['validation_rules']} quy tắc nhập có cảnh báo dừng lỗi và cho để trống. Kiểm cấu trúc/ô đích; Excel COM kiểm đại diện, chưa bấm từng liên kết bằng tay. Không macro, không liên kết tính toán đến workbook bên ngoài. |
| PDF chính | **12 trang A4**, 12 bookmark; {a['pdf_internal_links']} liên kết nội bộ và {a['pdf_external_or_local_links']} liên kết web/tệp. Đã render, xem cả 12 trang và xem lại các trang sửa. Dấu Việt, chữ Nhật kể cả dấu câu Nhật đã sửa font, không thấy cắt/tràn/chồng chữ. Nội dung nằm trong lề; cỡ chính 11 pt, bảng 10,5 pt, prompt 10,4 pt. |
| Màn hình tablet | Xem ảnh trang 2 và 10 ở chiều rộng 768 px để kiểm mật độ/chữ. Đây là mô phỏng ảnh, không phải kiểm trực tiếp iPad hay xác nhận thị lực/cỡ máy của người học. Có thể cần phóng to. |
| Gemini/checkpoint | Một prompt, đủ 13 quy tắc giáo dục; các quy tắc học cốt lõi được so tự động với bản cũ. Checkpoint đúng **8 dòng**, có thiếu dữ liệu, trợ giúp và nguồn. Đã kiểm sao chép/lưu/đọc lại mẫu checkpoint trong tệp văn bản; không giả vờ đã chạy hội thoại trong tài khoản Gemini. |
| Dữ liệu thử | Tất cả fixture nằm ở tmp, không nằm trong tệp giao. Bản cuối chưa có đáp án/điểm/ngày bắt đầu cá nhân giả; chưa đo vẫn trống hoặc Chưa đủ dữ liệu. |

Trong kiểm thử native đã phát hiện và sửa phần tử hyperlinks rỗng do bước đóng gói thêm vào hai trang không có liên kết. Sau sửa, tệp mở được trong Excel, vượt đầy đủ kiểm tra lưu/mở lại; không giao bản lỗi. Các lỗi ở script kiểm thử cũng đã sửa trước khi ghi số kiểm thử đạt trên đây.

## Quyền sử dụng và nguồn khóa

Đã đọc [JLPT Site Policy](https://www.jlpt.jp/e/policy.html), mục 1(1): cho phép sao chép/chỉnh dịch để tự học cá nhân. Bản này dùng cho người học đã mô tả, chỉ nhúng đáp án số cần chấm; không nhúng đề, bản chép hay âm thanh. Không suy ra quyền tái phân phối tác phẩm bên thứ ba hoặc xuất bản thương mại. Nguồn đặt cạnh cột khóa ẩn: “Source: Official Worldwide Japanese-Language Proficiency Test Website (https://www.jlpt.jp/)”.

Khóa được lấy trực tiếp từ [N4answer.pdf](https://www.jlpt.jp/samples/sample2018/pdf/N4answer.pdf) và [N3answer.pdf](https://www.jlpt.jp/samples/sample2018/pdf/N3answer.pdf). Cột khóa ẩn giúp tránh xem trước, không phải biện pháp bảo mật. Không có đáp án tự sáng tác; nếu sau này đổi bộ câu phải kiểm khóa tương ứng, không dùng khóa 2018 cho đề khác.

## Kiểm luồng học từ đầu đến cuối

| Bước yêu cầu | Kiểm thực tế và giới hạn |
|---|---|
| 1. Mở sổ tay | Mở bằng bộ đọc PDF và render đủ 12 trang; tệp không lỗi. Không thao tác trong trình đọc PDF trên iPad. |
| 2. Tới N4 đầu tiên | Link nằm ngay đoạn đầu trang 1; hướng dẫn trang PDF 3, số in 1 đã nhìn trực tiếp ở đề. Fragment #page=3 có thể bị trình đọc bỏ qua; số trang vẫn được ghi rõ. |
| 3. Mở đề chính thức | GET trực tiếp N4G.pdf trả HTTP 200, 1.193.596 byte, 9 trang; đã render trang có câu 1-6 để xác nhận. Trình đọc web từng timeout nhưng tải trực tiếp thành công; không đánh đồng timeout đó với link hỏng. |
| 4. Ghi sáu đáp án | Fixture ở B13:G13 trong Excel desktop; blank/0/chữ/số sai được kiểm. Không nhập đáp án fixture vào bản giao. |
| 5. Chấm | Trước Xong không hiện điểm; sau Xong chấm tự động và liệt kê câu sai/bỏ. Sáu đúng cho 6/6; một câu 0 cho 5/6; blank giữ dở dang. |
| 6. Ngày và phút | Thiếu ngày/phút/loại câu chưa được đưa vào tổng hợp. Nhập ngày thật, 6 phút và Mới trong fixture cho trạng thái Đã chấm. |
| 7. Tính workbook | G1 riêng chưa sinh tổng ngữ pháp; G1+G2 đủ mới có tổng 13 câu. Native Excel xác nhận tử/mẫu, tuần, mới/ôn lại và không lỗi công thức. |
| 8. Mở gia sư | Liên kết Gemini và bản Markdown có trong PDF; toàn bộ prompt cũng có ở trang 9-10. Chưa đăng nhập/chạy prompt trong tài khoản Gemini của người học. |
| 9. Xuất checkpoint | Kiểm cấu trúc 8 dòng và vòng lưu/sao chép/đọc lại văn bản. Phản hồi thực tế của Gemini, việc tuân thủ prompt và tính năng Live chưa thử. |
| 10. Xem tổng hợp tuần | Fixture Excel thay tuần B4, ngày bắt đầu B38, xem độ đúng; lưu và mở lại giữ phân biệt ôn lại, D7/D14 đúng. |

**Mốc thiết lập dưới ba phút:** thiết kế chỉ cần mở trang 1, bấm một link và chuẩn bị giấy/ghi chú; không đòi hỏi thiết lập Excel/Gemini trước khi làm. Chưa bấm giờ với người học thật, nên **chưa xác nhận đạt tiêu chí thời gian này bằng thử nghiệm người dùng**. Thời gian GET khoảng 2 giây ở máy kiểm không đại diện thời gian thiết lập hay mạng của người học.

## Tương thích nền tảng

| Nền tảng | Mức xác minh | Kết luận sử dụng |
|---|---|---|
| Excel desktop 16.0 trên máy kiểm | **Đã thử engine thực** | Mở/chấm/tính lại/lưu/mở lại đạt. Chưa kiểm thao tác cảm ứng, hộp thoại nhập bằng tay, bản Mac hoặc mọi phiên bản Excel. Quyền sử dụng ở máy kiểm không xác nhận quyền trên laptop người học. |
| Excel cho web | **Suy luận có căn cứ, chưa thử file trên tài khoản thật** | Dùng công thức thông dụng và validation chuẩn; [Microsoft](https://support.microsoft.com/en-us/excel/differences-between-using-a-workbook-in-the-browser-and-in-excel) mô tả hỗ trợ validation trừ IME. Chưa xác minh mở/lưu/điều hướng của workbook trong dịch vụ. Không coi kiểm cấu trúc là kiểm cloud. |
| Excel iPad | **Chưa thử** | Chưa biết mẫu máy, phiên bản app/quyền chỉnh sửa. [Microsoft](https://support.microsoft.com/en-us/microsoft-365-activation-licensing/when-do-i-need-a-microsoft-365-subscription) nêu thiết bị >10,1 inch hoặc một số nhu cầu cần thuê bao. Không khẳng định iPad Excel chỉnh sửa miễn phí. |
| Google Sheets / Apple Numbers | **Chưa thử chuyển đổi hoặc round-trip** | Không hứa công thức/validation/links còn nguyên; không khuyến nghị chuyển file chính. Không lược tính năng Excel để chạy ứng dụng chưa kiểm. |
| Giấy/ghi chú bất kỳ | **Mẫu và phép chấm đã kiểm** | Mẫu trang 1 giữ được ngày, mã câu, đáp án, đúng/tổng, phút, loại câu và lỗi. Chấm bằng khóa trực tiếp, nhập sau nếu muốn; không có dashboard tự tính cho ghi giấy. |

[Microsoft xác nhận Excel web có mức miễn phí với tài khoản Microsoft](https://support.microsoft.com/en-gb/accounts-billing/subscriptions/what-s-the-difference-between-a-microsoft-365-subscription-and-free-web-apps?nochrome=true). Cần mạng/đăng nhập; điều này không xác nhận quyền lợi của mọi app, gói trả phí hoặc tương thích workbook đã được thử trên web. Không yêu cầu mua gì để bắt đầu.

## Điều kiện dữ liệu và âm thanh

- D7/D14 từ B38 +7/+14; B38 mới để trống. Mốc tuần B4 và ngày cũ được giữ. Ngày bắt đầu 0, âm, số lẻ, chữ, vượt giới hạn không sinh ngày kiểm tra giả. Cổng dữ liệu D7/D14 là tiêu chí tổ chức, chưa chấm tự động các mục tiêu nhớ/nghe/nói và không suy ra xác suất đỗ.
- Giữ nguyên 9 URL MP3 JLPT và 1 MP3 Irodori đã kiểm ở Phase 2; lần này không tải/phát/tua toàn bộ âm thanh để tạo mốc giây. Mỗi khối ghi đúng tệp, nhóm và câu 1-2, bắt đầu ở 1番, dừng sau câu 2 và khoảng trả lời, trước 3番. **Không có timestamp được đo/kiểm độc lập.** Không bịa nội dung âm thanh hoặc bản chép; phân biệt nghe đầu không hỗ trợ và chữa sau bằng script.
- Giữ nghiên cứu/cảnh báo cỡ mẫu, điểm quy đổi, giới hạn AI, không giảm ngủ và hồ sơ chưa xác nhận. Liên kết ERIC S21 từng timeout trực tiếp như QA cũ; đây là tham khảo, không chặn bài học. Không kiểm lại toàn bộ 48 URL như một vòng nghiên cứu mới.
- Chưa có kết quả chẩn đoán của người học, lịch tuần/ca khuya, giờ ngủ thật hay quỹ phút bền vững. Không gán số liệu fixture cho người học. Chưa kiểm quy định tuyển sinh của trường; không cam kết đỗ N2 hoặc nhập học.

## Thao tác đầu tiên

Mở **JLPT_STUDY_SYSTEM_FINAL.pdf trang 1**, bấm đề N4 → trang PDF 3 (số in 1) → làm câu 1-6 trong 6 phút khi đủ tỉnh. Ghi giấy ngay hoặc mở **Làm nhanh**: B13:G13, Xong tại B17; sau đó ngày B16, phút D16, loại câu F16. Xem câu cần sửa ở B20, chọn một lỗi ở B21 rồi dừng/chữa 5-10 phút. Kiệt sức thì nghỉ hoặc ôn cũ tối đa 10 phút.
'''
(O/'QA_FINAL.md').write_text(q,encoding='utf-8')
expected={'JLPT_STUDY_SYSTEM_FINAL.pdf','JLPT_PROGRESS_TRACKER_FINAL.xlsx','GEMINI_MASTER_TUTOR_FINAL.md','QA_FINAL.md'}
assert {p.name for p in O.iterdir()}==expected
print('QA written; exactly four final deliverables')
