from pathlib import Path
R=Path(__file__).resolve().parents[2];O=R/'FINAL_V3';O.mkdir(exist_ok=True)
s=(R/'FINAL/GEMINI_MASTER_TUTOR.md').read_text(encoding='utf-8')
prompt=s.split('```text\n',1)[1].split('\n```',1)[0]
prompt=prompt.replace('1. Luôn hỏi ngắn:', '1. Nếu tôi đã nêu phút rảnh, mức mệt và tình trạng buồn ngủ thì dùng ngay; chỉ hỏi phần còn thiếu. Khi chưa có dữ liệu, hỏi ngắn:')
prompt=prompt.replace('NHẬT KÝ CHUYỂN TIẾP','CHECKPOINT')
start=prompt.index('13. Xuất khối CHECKPOINT')
end=prompt.index('\nNhắc tôi ghi dòng nhật ký',start)
prompt=prompt[:start]+'''13. Xuất CHECKPOINT tối đa 8 dòng ngắn, mỗi dòng một nhãn. Chỉ ghi dữ liệu tôi xác nhận; thiếu ghi “chưa biết/chưa đo”. Gộp, không kéo dài thành báo cáo:
NGÀY / MỆT / NGỦ 24H: ...
PHÚT THỰC TẾ HỌC / NGHE / NÓI: ...
MỤC TIÊU / NGUỒN / MÃ BÀI: ...
ÔN CŨ: [đúng/tổng; có/không trợ giúp hoặc chưa đo]
CÂU MỚI LẦN ĐẦU: [đúng/tổng; trợ giúp; chưa đo thì ghi rõ]
LỖI V/G/R/A/M/T/F / MỘT CÂU SỬA: ...
TIẾP THEO / NGÀY ÔN GỢI Ý: ...
CHƯA BIẾT / CẦN KIỂM NGUỒN: ...
''' + prompt[end:]
prompt=prompt.replace('không giả vờ nhớ.', 'không giả vờ nhớ. Tôi tự mang checkpoint sang buổi sau; bạn không tự đọc chat khác.')
header='''# Gia sư tiếng Nhật - một mục tiêu mỗi buổi

**Lần đầu:** mở [Gemini](https://gemini.google.com/), dán khối câu lệnh bên dưới một lần vào chat dùng học. Không cần tạo Gem hay cấu hình.

**Mỗi buổi:** viết “Có 20 phút; mệt 3/5; không phải cắt ngủ” bằng dữ liệu thật → học một mục tiêu → nhận sửa lỗi → sao chép CHECKPOINT tối đa 8 dòng vào ghi chú → buổi sau dán lại checkpoint và phút/mệt mới. Chat mới thì dán lại prompt một lần. Không giả định Gemini nhớ chat khác hay ghi Excel.

Không có Live: mở MP3 chính thức, tự nói thành tiếng rồi nhập câu vừa nói. Không có âm thanh: ghi chưa luyện nghe. Quyền Pro do người học cung cấp; tính năng thực tế chưa kiểm trên tài khoản. Không cần mua thêm. Sổ tay chính có toàn bộ prompt và hướng dẫn, nên không bắt buộc mở tệp này hằng ngày.

## Sao chép từ đây

```text
'''
(O/'GEMINI_MASTER_TUTOR_FINAL.md').write_text(header+prompt+'\n```\n',encoding='utf-8')
(R/'tmp/jlpt-v3/tutor_prompt.txt').write_text(prompt,encoding='utf-8')
print('Tutor retained, checkpoint shortened to eight lines')
