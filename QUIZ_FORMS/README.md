# 10 mini-quiz N4 — bộ tạo, chưa có Forms live đã nghiệm thu

[quiz_plan.json](quiz_plan.json) xác định 10 bộ 5–9 câu, khoảng 5–15 phút thử. [answer_mapping.csv](answer_mapping.csv) giữ mã bộ/vị trí/ID câu/nhãn đúng/nội dung đúng/1 điểm/stimulus/khái niệm. Khóa canonical từ [validated_keys.json](../deliverables/phase3/ANSWER_KEY_AND_EXPLANATIONS/validated_keys.json) là nguồn quyết định.

Không sinh câu mới: 68 câu gốc được dùng một lần trong 10 bộ, 12 câu chưa giao. Tám câu nghe chưa chuyển thành quiz nghe khi chưa có âm phù hợp; không cho đọc script rồi gọi là nghe độc lập. Bốn vai nói giữ riêng. Không có ngân hàng N3/N2.

P0: W01-B01, B02, B03. Tập lệnh [một tệp](../DRIVE_SETUP/JP_STUDY_SETUP.gs) tạo quiz chưa publish, khóa 1 điểm/câu, feedback sau nộp, một câu mỗi section và mapping item-ID→question-ID. Không đổi thứ tự/nhãn lựa chọn từ nguồn. Nội dung đúng và giải thích không nằm trong mô tả/HelpText trước nộp. Người quản lý cần xác minh “Xem điểm” và quyền responder trước khi mở link.

Forms có thể không trả ItemResponse cho câu MCQ bỏ trống; mapper đi qua danh sách ID dự kiến, không zip các câu trả lời theo vị trí. Mới/ôn/hỗ trợ giữ riêng; câu cùng ID/stimulus đã có phản hồi không được biến thành mới bởi việc chọn lại “Tự làm”. Lịch sử ngoài hệ thống chưa biết. Câu chưa nộp chưa thể theo dõi.

Đã tạo thật đúng ba Form P0 với 18 câu và chạy `auditForms`; nộp QA giả lập thực tế với đúng/sai/trống đạt điểm chính xác; gỡ responder công khai, chỉ owner. Đã kích hoạt qua `activateP0Verified`: dashboard liên kết `MỞ BÀI NGẮN` trực tiếp; trigger cách ly QA an toàn (0 learner rows). Bảy Form P1 giữ cấu hình sẵn sàng tạo khi có nhu cầu. Xem [DRIVE_FIRST_QA](../DRIVE_FIRST_QA.md) và [bằng chứng triển khai](../qa/drive_first_deployment.json).
