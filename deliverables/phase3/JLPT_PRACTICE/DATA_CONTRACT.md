# Hợp đồng dữ liệu và cách mở rộng

Ứng dụng không có máy chủ bắt buộc. `index.html` chứa CSS, ngân hàng, thư viện và JS nạp sẵn; các bản `.js/.json` bên cạnh là tài nguyên để kiểm tra/tái sử dụng. Không dùng fetch/module trong luồng local. Không gửi dữ liệu mạng trong luồng học văn bản; liên kết ngoài chỉ mở khi người học chọn.

## Ngân hàng và khóa

`question_bank.json`: bankVersion, answerKeyDigest (SHA-256 của cặp ID/khóa theo thứ tự), nguồn khái niệm, 22 nhóm mục tiêu, 80 câu, 4 vai, 30 recipe. Câu gồm ID/cấp ước lượng/kỹ năng/mục tiêu/độ khó, stem/options/khóa, giải thích Việt và từng nhiễu, prerequisite, nguồn, thời gian ước lượng, việc ôn, stimulusId, validation và patternId/relatedTemplate khi có thẻ đúng.

`validation.status=reviewed` chỉ là đã qua quy trình rà được mô tả ở QA_REPORT, không là tham số IRT hay xác nhận giáo viên bản ngữ. Ngân hàng gốc AI, không nhập đề thương mại/đề chính thức hàng loạt. Khi chưa có thẻ dạy đúng mục tiêu thì patternId=null, không gán thẻ gần giống để đủ trường.

Không thay khóa ngầm: phát hành bankVersion/digest mới nếu sửa khóa, giữ lịch sử phiên bản cũ; bộ nhập hiện từ chối khác phiên bản/digest. Digest phát hiện khác khóa theo phiên bản, không phải chữ ký chống gian lận; khóa được cung cấp công khai để tự học. Bản đầu xáo lựa chọn riêng từng ID và đối chiếu 80 mapping nội dung trước phát hành; không dùng chu kỳ đáp án cố định.

Thêm câu chỉ sau schema + giải độc lập + rà từng nhiễu/bằng chứng + kiểm chấm. Giữ bản holdout theo mục tiêu, thử người học để hiệu chuẩn trước khi tuyên bố mức khó. Mục tiêu 100+ mini-test là thiết kế tương lai: thêm recipe bằng ID câu đã kiểm, không tạo mới hàng trăm câu tự động chưa rà. 30 recipe hiện nằm trong bank, giao diện tùy chọn theo mục tiêu; engine vẫn lọc theo lịch sử/sức/giọng và có thể trả ít câu hoặc báo không còn câu phù hợp.

## Tiến độ JSON schemaVersion=1

- attempts: ID bất biến session:question, câu đã chọn và lịch đổi lựa chọn, correctAnswer/digest, đúng/sai/chưa đáp, trợ giúp, đoán, mới theo câu VÀ stimulus, giây hoạt động, thời điểm/ngày địa phương, gián đoạn/quá giờ, lịch ôn và cờ kiểm chuyển hiểu chậm.
- exposures: ghi khi câu thực sự hiện hoặc mở khóa; câu đã lên kế hoạch nhưng chưa xem chưa bị đánh dấu hay chấm sai.
- sessions: danh sách đã nộp, số dự kiến/đã xem/đã đáp/trống, thời gian. active giữ buổi dở, từng lựa chọn và thời gian; tải lại/nhập từ nơi khác đánh dấu gián đoạn.
- diagnostics: chỉ kết quả N4 thật được người học nhập tự nguyện, có ngày/số câu/điều kiện. Không có dữ liệu điền sẵn từ tự đánh giá 0–5.
- reflections: ba lựa chọn ngắn theo session. speaking: bốn ý 0/1/? tự ghi, phát âm chưa đánh giá; không cộng trắc nghiệm.

Phân loại evidenceType: independent-new (STANDARD/DEEP, câu+stimulus chưa thấy, không trợ giúp/đoán/gián đoạn/quá giờ); review; assisted; training-new; new-guessed; new-conditions. Phần trăm luôn kèm mẫu/điều kiện, không quy đổi điểm JLPT. Chưa trả lời khác sai; invalid bị từ chối.

Nghe có audioPlays và firstListen: giữ câu trả lời trước lần hỗ trợ chữ/nghe lại, rồi điểm trợ giúp riêng. Không nghe hết hoặc thiếu âm: no-audio; nghe lại: replayed-audio; script: transcript. TTS không phải âm JLPT. firstListen là dữ liệu luyện có ghi điều kiện, không tự chứng nhận nghe tốt.

Bộ nhập giới hạn tệp 10 MB trên UI, mảng 20.000, kiểm phiên bản/khóa, ID/thời gian/đáp án/điểm/cờ và buổi dở. Gộp theo ID, từ chối lịch sử cùng ID nhưng khác nội dung; không tự ghi đè. Sắp theo thời gian để mốc đầu thật không đổi sai sau gộp. Nếu có hai buổi dở xung đột, giữ bản hiện tại và yêu cầu nộp phần đó trước. Dữ liệu JSON do người dùng giữ; không phải hồ sơ thi chống sửa.

## CSV UTF-8 BOM, 12 cột

Session ID | Ngày | Cấp | Kỹ năng | Mã bài | Loại dữ liệu | Đúng | Đã trả lời | Tổng đã xem | Giây làm | Trợ giúp | Ghi chú

Gộp theo session+kỹ năng+loại. `Mới` chỉ independent-new; `Ôn lại` là review; `Hỗ trợ` là assisted; các điều kiện còn lại là `Luyện`. CSV không chứa chi tiết câu/buổi dở/vai nói; dùng JSON để chuyển thiết bị. Dùng giây nguyên để Excel có dấu thập phân phẩy không đọc sai phút thành chữ. Chuỗi có ký tự mở công thức được vô hiệu hóa khi xuất CSV.

## Quy tắc thích nghi thử nghiệm

N4 trước, ưu tiên nền nơi hành động/tồn tại và chia thể; thêm trọng số từ chẩn đoán N4 ≥5 câu, lỗi lặp, trợ giúp, đoán, trung vị thời gian khi có ≥3 lượt, câu đến ngày ôn và độ đúng câu mới đủ mẫu. Mệt≥4: không giao câu mới; buồn ngủ: nghỉ; DEEP chỉ khi mệt1–2. Thời gian không được dùng để tự kết luận nguyên nhân hay năng lực.

Ôn 1/3/7/14 ngày, độ trễ ≥3 ngày và n≥5 là heuristic, không phải liều tối ưu cá nhân hay chuẩn JLPT. Câu mới cùng mục tiêu sau chậm = chuyển hiểu, khác giữ lại câu cũ. Hết câu mới: nói rõ và không tăng điểm mới bằng câu cũ. Chưa đủ dữ liệu: không đưa kỹ năng mạnh/yếu chắc chắn. Gợi ý sau ≥2 lỗi chỉ là chọn việc học, không chẩn đoán nhận thức.

Lưu localStorage chỉ tại trình duyệt/địa chỉ này; file:// tùy nền tảng, riêng tư hoặc bộ nhớ đầy có thể thất bại. Thất bại hiện thông báo và chuyển bộ nhớ; xuất JSON để giữ. HTTP localhost và file local không tự dùng chung dữ liệu. Không có đồng bộ, API hoặc thao tác tự động trong tài khoản Gemini.
