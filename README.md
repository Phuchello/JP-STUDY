# JP-STUDY

Học tiếng Nhật qua **một Google Sheet**: chọn một việc ngắn, làm bài, chữa một lỗi rồi dừng. Mệt thì nghỉ. Ưu tiên nghe/nói đời sống và phục hồi nền N4; không áp lịch cố định hoặc cam kết đỗ JLPT.

**Phase 3.5 đang triển khai:** đã tạo Drive riêng tư, bảng 5 tab, 7 PDF ngắn và prompt. **Forms còn QA_PENDING**: đã chuẩn bị 10 quiz và kiểm logic bằng API mô phỏng; chưa chạy trực tiếp trên Google. Không coi bộ cài là 10 Form đã hoạt động.

## Bắt đầu

- **Người học:** mở link `JP_STUDY_HOC_HOM_NAY` được chủ sở hữu bàn giao riêng. HOME chỉ có bài ngắn, nghe một đoạn và một vai nói. Quiz ghi rõ chờ kích hoạt; có thể nghe/nói ngay khi tài khoản được cấp quyền tài liệu.
- **Người quản lý:** làm theo [cài một lần](DRIVE_SETUP/README.md), tạo và nghiệm thu 3 quiz P0 trước, rồi mới mở 7 quiz còn lại. Không cần API key hoặc thiết bị mới.
- **Bảo trì:** đọc [hiện trạng](PROJECT_STATUS.md), [QA Drive-first](DRIVE_FIRST_QA.md), [AGENTS](AGENTS.md). Giữ dữ liệu cá nhân và link tài khoản ngoài repo công khai.

## Mở đúng tài liệu

| Cần dùng | Tài liệu | Phạm vi |
|---|---|---|
| Bảng trống để nhập Sheets | [Mẫu 5 tab](DRIVE_SETUP/JP_STUDY_HOC_HOM_NAY.xlsx) | VERIFIED về nội dung/bản nhập; chưa thử thiết bị thật |
| Tạo quiz và tự thu phản hồi | [Bộ cài Workspace](DRIVE_SETUP/README.md) | QA_PENDING chạy thật |
| 10 quiz ngắn, 5–9 câu | [Quiz plan](QUIZ_FORMS/README.md) | Dùng lại 68 câu N4; không sinh mới |
| Hướng dẫn và 6 thẻ tham khảo | [PDF ngắn](deliverables/phase3.5/) | 7 PDF, tổng 9 trang |
| Chữa một lỗi sau nộp | [Gemini](GEMINI_CHUA_LOI.md) | Sao chép/dán thủ công |
| Bốn vai nói | [Vai nói](deliverables/phase3.5/VAI_NOI.md) | Luyện có hướng dẫn, không phải điểm nói JLPT |
| Phân tích dữ liệu thực | [AI analysis prompt](DAILY_AI_ANALYSIS_PROMPT.md) | Phân biệt mới/ôn/hỗ trợ/trống/không rõ |
| CSV xuất hằng ngày | [Mẫu header](DRIVE_SETUP/templates/DAILY_LEARNING_REPORT.csv) | Trống; xuất thật sau cài script |

## Nguồn cũ được giữ nguyên

[80 câu và schema](question-bank/n4/README.md) · [khóa/giải thích/QA](question-bank/answer-keys/README.md) · [31 thẻ, 37 ví dụ học](grammar-patterns/README.md) · [nghiên cứu và giới hạn bằng chứng](research/README.md) · [mốc 7/14 ngày](study-plans/START_TODAY.md) · [Phase 1/2/2.1](archive/README.md).

Ứng dụng HTML và tracker Excel Phase 3 vẫn nằm ở [checkpoint cũ](deliverables/phase3/README.md); không phải lối vào chính của Phase 3.5. 30 recipe cũ ghép lại cùng 80 câu, không phải 30 đề độc lập. Chưa có ngân hàng N3/N2 hoặc mở rộng 300–500 câu. AI QA không thay thế thẩm định bản ngữ/hiệu chuẩn người học.

## Dữ liệu và kiểm định

Drive hiện chỉ chủ sở hữu truy cập. Không chia sẻ thư mục gốc/bảng raw; nếu người quản lý và người học cần mức bí mật khác nhau, dùng file riêng với quyền riêng. Ẩn tab không phải kiểm soát truy cập. Không đưa CSV/JSON thật, ID tài khoản, link riêng, token hoặc bản xuất cá nhân lên GitHub.

`VERIFIED` chỉ đúng phạm vi đã kiểm; `QA_PENDING` chưa đủ nghiệm thu; `DRAFT` là nháp/lịch sử. [FILE_INDEX](FILE_INDEX.md) và [MANIFEST](MANIFEST.json) ghi trạng thái/hash từng tệp; [PUBLICATION_POLICY](PUBLICATION_POLICY.md) quy định bản công khai.

Chạy `python scripts/drive_first/build_bundle.py`, `node scripts/drive_first/test_drive_first.cjs`, rồi `python scripts/update_manifest.py` và `python scripts/validate_release.py`. Build bảng/PDF cần runtime ghi trong [setup](DRIVE_SETUP/README.md). Kết quả thử nằm trong `tmp/`, bị Git bỏ qua. Không tái phân phối sách, đề/audio bên thứ ba; chỉ liên kết nguồn chính thức.
