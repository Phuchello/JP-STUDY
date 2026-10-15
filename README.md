# JP-STUDY

Hệ thống học tiếng Nhật dành cho người lớn vừa học vừa làm, ít thời gian và sức lực thay đổi. Ưu tiên nghe, nói và phục hồi nền N4; N3/N2 chỉ tăng theo dữ liệu mới. Hồ sơ công khai là **ví dụ tổng hợp**, không phải hồ sơ hay điểm của một người thật.

**Hiện tại: thí điểm Phase 3 đã kiểm trong phạm vi 80 câu N4 và 4 vai nói.** Mốc hoàn thành liền mạch: Checkpoint 3. Checkpoint 4 mới xong tích hợp Excel; phần mở rộng 300–500 câu và ngân hàng N3/N2 chưa làm. Không cam kết đỗ JLPT.

## Bắt đầu trong vài phút

1. Chọn **Code → Download ZIP** trên GitHub, giải nén. Mở `deliverables/phase3/JLPT_PRACTICE/index.html` bằng Chrome/Edge trên laptop. Đây là một tệp HTML tự chứa; xem trang mã trên GitHub chưa chạy ứng dụng. Không cần cài đặt hay API key.
2. Chọn mức mệt. Có thể nghỉ; nếu học, chọn QUICK ngắn hoặc STANDARD khi đủ sức. Làm trước, chữa một lỗi sau, rồi dừng. [Kế hoạch một trang](study-plans/START_TODAY.md) và [hướng dẫn PDF](deliverables/phase3/START_HERE.pdf).
3. Muốn dùng Gemini: mở [prompt chữa lỗi](deliverables/phase3/GEMINI_ERROR_TUTOR.md), sao chép và tự dán vào Gemini. Không có kết nối tự động với tài khoản, Excel hay lịch sử chat.
4. Tiến độ chỉ lưu trong trình duyệt đang dùng. Xuất JSON trước khi đổi thiết bị/xóa dữ liệu. **Giữ JSON/CSV cá nhân ở máy, không đưa lên kho này.** Excel là tùy chọn; [hướng dẫn nhập CSV](tracking/README.md).

Văn bản cốt lõi chạy offline. Nghe tổng hợp chỉ dùng khi có giọng Nhật; không có thì bỏ phần nghe tự chọn. Nguồn MP3 chính thức được liên kết riêng. iPad mới được mô phỏng bố cục, chưa thử thiết bị thật; nếu Files chỉ hiện xem trước, dùng laptop.

## Tìm đúng tài liệu

| Nội dung | Nơi mở | Trạng thái |
|---|---|---|
| Kế hoạch hiện hành, mốc 7/14 ngày | [START_TODAY](study-plans/START_TODAY.md) | VERIFIED |
| 80 câu N4 và schema | [Ngân hàng N4](question-bank/n4/README.md) | VERIFIED trong pilot AI QA |
| Khóa, giải thích và kiểm nội dung độc lập | [Khóa và QA](question-bank/answer-keys/README.md) | VERIFIED trong phạm vi ghi rõ |
| 4 vai nói | [Speaking](speaking/README.md) | VERIFIED trong pilot AI QA |
| 31 thẻ mẫu, 37 ví dụ học | [Thư viện mẫu](grammar-patterns/README.md) | VERIFIED; không tính là 37 câu đo mới |
| Nguồn, 14 kỹ thuật, giới hạn nghiên cứu | [Research](research/README.md) | VERIFIED theo mức đọc từng nguồn |
| Gemini, checkpoint mang theo | [Prompts](gemini-prompts/README.md) | VERIFIED về quy trình; tính năng tài khoản tự kiểm |
| Tracker hiện hành và các bản cũ | [Tracking](tracking/README.md) | VERIFIED; bản trống, không có nhật ký thật |
| PDF và bộ dùng hiện hành | [Deliverables](deliverables/phase3/README.md) | VERIFIED trong phạm vi pilot |
| Phase 1 / 2 / 2.1 | [Archive](archive/README.md) | Checkpoint lịch sử; có bản công khai đã lược hồ sơ |
| Kiểm định bản công khai và QA cũ | [QA](qa/README.md) | Xem phạm vi từng lượt |

**VERIFIED** nghĩa là đã kiểm theo phạm vi và giới hạn được ghi; không có nghĩa được JLPT công nhận, hiệu chuẩn người học hoặc duyệt bởi giáo viên bản ngữ. **QA_PENDING** chưa đủ kiểm; **DRAFT** là bản nháp/lịch sử không được coi là bản phát hành.

Chi tiết hiện trạng: [PROJECT_STATUS](PROJECT_STATUS.md). Danh sách mọi tệp: [FILE_INDEX](FILE_INDEX.md). Hash/kích thước: [MANIFEST](MANIFEST.json). [Kiểm kê nguồn và phần giữ local](qa/source_inventory.json), [chính sách công khai](PUBLICATION_POLICY.md).

## Kiểm tra cho người bảo trì

Chạy `python scripts/validate_release.py`. Node không cần thêm thư viện để chạy `node scripts/tests/test_engine.cjs`. Kiểm giao diện cần Playwright; xem [scripts](scripts/README.md). Tệp kết quả mới nằm trong `tmp/`, bị Git bỏ qua. Đọc [AGENTS.md](AGENTS.md) trước khi tạo checkpoint tiếp theo.

Không tải lại sách, PDF hoặc âm thanh đề JLPT vào repo. Các đường dẫn ngoài là nguồn gốc, có thể thay đổi sau ngày kiểm 15/10/2026. Nội dung do dự án soạn không được gọi là đề thi thật; xem [nguồn và quyền sử dụng](PUBLICATION_POLICY.md).
