# QA nội dung cuối — bộ thí điểm nền N4

Ngày:15/10/2026. **Kết luận:PASS cho phát hành thí điểm80 câu +4 vai nói.** Không còn phát hiện block,major hoặc minor cụ thể đang mở từ các lượt QA. Đây là chấp thuận trong phạm vi kiểm nội dung, không phải chứng nhận bản ngữ hoặc chuẩn hóa trình độ.

Phụ lục hiện có **31 thẻ:9 grammar,6 listen,4 read,12 templates**, cùng **37 câu chỉ để học**. Phụ lục không cộng vào ngân hàng80.

**Số lượng thực kiểm**

| Phạm vi | Lượt cuối này | Lũy kế qua các lượt |
|---|---|---|
| Câu ngân hàng | Đọc lại đầy đủSHORT007; khóaD đúng |80/80 giải mù trước khóa, rồi rà khóa/ngôn ngữ và240 nhiễu |
| Kiểm sau sửa |80/80 mapping theo từngID;36 thay đổi được đề nghị đã áp dụng | Lượt kiểm trước đọc lại22 câu được chọn và4 vai |
| Thẻ phụ lục | Đọc đủ11 thẻ có sửa hoặc mới |31/31 thẻ |
| Câu học trong phụ lục | Đọc13 câu thuộc các thẻ kiểm lại, gồm3 câuG09 mới |37/37 câu; không gọi là giải mù |
| Đồng bộ cuối | Đọc lại8 trường vừa sửa |6 formula và2 typicalMisunderstanding đều đạt |

Không tuyên bố đã giải mù lần hai toàn80 câu sau xáo. Kết luận dùng lượt đầu đầy đủ80+4 và các lượt kiểm thay đổi nối tiếp; không dùng máy kiểm schema thay suy luận ngôn ngữ.

**Kết quả kiểm các thay đổi**

- SHORT007: đáp án, explanationVi, lời giải nhiễuC và commonMistakes đều nói **có thể** để ví ở ga; không còn khẳng định chắc đã quên.
- Mapping:80/80 khớp quyết định từngID. Các mục phép/cấm/nghĩa vụ/miễn nghĩa vụ dẫn tớiG09; mốc前に dẫnG05; kinh nghiệm dẫnG08; xin nhắc lại dẫnT01; báo trễ dẫnT05. Các chỗ chưa có thẻ phù hợp dùngnull.
- G04: lời giải hạn gọi không buộc kết thúc cuộc nói chuyện lúc5giờ.
- G06: cặpあく/あける được ghi rõ; commonMistake và typicalMisunderstanding đều giới hạn cặp đang học.
- G07: có ngoại lệN/ナAなら, bỏだ phi quá khứ khẳng định; ví dụ学生なら/静かなら đúng.
- R03: dịch“thông thường”, tách ngoại lệ thứHai, không nhầm với平日.
- T03/T04/T05/T08/T10/T11: khung loại từ đã rõ; sáuformula đã đồng bộtemplate. T11 cũng giới hạn cặpなぜなら…からです trong khung bài tập ở cả hai trường nhắc lỗi.
- CácF01–F16 của lượt đầu vàRA01–RA08 của lượt kiểm trước:đã xử lý. Không phát sinh lỗi mới trong phạm vi kiểm cuối.

**G09 và ba khóa mới**

Bốn nghĩa được phép,cấm,phải,không cần được tách đúng. Cách tạoなければなりません vàなくてもいい từ thểない đúng. Không đồng nhất“không cần” với“cấm”. Nguồn[TUFS cho phép](https://www.coelang.tufs.ac.jp/mt/ja/gmod/contents/explanation/058.html) và[TUFS cấm](https://www.coelang.tufs.ac.jp/mt/ja/gmod/contents/explanation/059.html) đã được đọc ở lượt trước.

Đã mở trực tiếp[JF文-53](https://www.jpf.go.jp/j/urawa/j_rsorcs/textbook/setsumei_pdf/setsumei14_2.pdf) và[JF Bangkok Akiko5,trang1–3](https://ba.jpf.go.jp/wp-content/uploads/2022/03/Akiko5_bunpoo382002.pdf). Hai nguồn hỗ trợ nghĩa cần/phải làm và sự khác nhau giữa nghĩa vụ,miễn nghĩa vụ,cho phép,cấm.

| CâuG09 | Chọn lại / khóa(index0) | Đánh giá |
|---|---|---|
|1|0/0 — この紙を出す必要はありません。| Duy nhất;không cần nộp khác cấm nộp |
|2|1/1 — 写真を撮ってはいけません。| Duy nhất;禁止 tương ứng lệnh cấm |
|3|0/0 — 名前を書かなければなりません。| Duy nhất;必ず giữ ý bắt buộc |

**Giới hạn áp dụng**

- QA do mô hình thực hiện, không phải thẩm định của giáo viên bản ngữ.
- Chưa thử trên người học thật; nhãn nềnN4,mức khó,thời gian và độ phân biệt chỉ là ước lượng,chưa hiệu chuẩn.
- Không phải đềJLPT chính thức; điểm không chứng nhận trình độ hoặc khả năng đỗ.
- Chỉ kiểm kịch bản chữ và khóa câu nghe; không nghe hoặc xác nhận phát âm,tốc độ,nhịp,ngữ điệu củaTTS.
- Một số nguồnJ04 vẫn ở cấp khóa; không khẳng định mọi từ/mẫu đã có dẫn đúng trang.
- Chưa kiểm giao diện có che thẻ người đối thoại,cơ chế chấm hoặc lưu dữ liệu người học trong nhiệm vụ nội dung này.

**Dấu vết tệp đã kiểm**

- `deliverables/phase3/JLPT_PRACTICE\question_bank.json` — SHA256:`41643716454835D1A8F78A8F7626EBE74AC2DCA9F68B55EF3194CACBD3C2E3F0`
- `deliverables/phase3/JAPANESE_PATTERN_LIBRARY\patterns.json` — SHA256:`D041F271066E59B3FFC458E0DAE7F1D1BA4B93296A6B6D2FEC4909FE9EA2E9B4`

Metadata QA được tác giả đóng sau kết luận PASS: ngân hàng có trạng thái reviewed-pilot-release; 80 câu và 4 vai đã ghi independentReaudit=true, ngày 2026-10-15; cả 31 thẻ ghi rõ QA độc lập bằng AI và giới hạn chưa thẩm định bản ngữ/hiệu chuẩn người học. Người kiểm đã đọc lại đúng tám trường đồng bộ: formula của T03/T04/T05/T08/T10/T11 và typicalMisunderstanding của G06/T11. Cả tám trường vẫn đúng và nhất quán với template/commonMistake tương ứng.

Hai SHA256 ở trên được tính lại từ các tệp FINAL hiện tại sau khi đóng metadata và thay thế hash snapshot trước stamp. Đây là chốt dấu vết sau PASS, không phải giải lại 80 câu; kết luận PASS nội dung giữ nguyên.

Bản máy đọc đầy đủ: [content_final_reaudit.json](./content_final_reaudit.json). Người kiểm chỉ đọc nguồn và cập nhật báo cáo trong tmp; không sửa nội dung hoặc mở rộng ngân hàng.

