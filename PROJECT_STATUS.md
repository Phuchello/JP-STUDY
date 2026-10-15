# Trạng thái dự án — 15/10/2026

## Phase 3.7 — Ngân hàng luyện đề JLPT, Chuyên đề kỹ năng & Cổng luyện tập mở rộng (Checkpoints 3.7-A đến 3.7-C hoàn tất)

- **Checkpoint 3.7-A (Sửa lỗi & Khung chương trình)**:
  - Sửa dứt điểm độ lệch mô tả bài tập Tuần 02 (W02-B01 đến W02-B05) trên Google Sites, khớp 100% với đặc tả `QUIZ_FORMS/quiz_plan.json`.
  - Ban hành chuẩn phân loại năng lực quốc tế JEES/Japan Foundation: [JLPT_SKILL_TAXONOMY](curriculum/JLPT_SKILL_TAXONOMY.md), [LEVEL_COMPETENCY_MATRIX](curriculum/LEVEL_COMPETENCY_MATRIX.csv), [QUESTION_TYPE_BLUEPRINT](curriculum/QUESTION_TYPE_BLUEPRINT.json), và [TEST_GENERATION_PLAN](curriculum/TEST_GENERATION_PLAN.md).
- **Checkpoint 3.7-B (120 câu hỏi gốc mới & Kiểm thử 5 tầng độc lập)**:
  - Biên soạn và nghiệm thu đúng **120 câu hỏi mới nguyên bản**: N4 (40 câu), N3 (50 câu), N2 (30 câu) trong [QUESTION_BANK_EXPANDED](curriculum/QUESTION_BANK_EXPANDED.json).
  - Vượt qua 4 cổng QA tự động nghiêm ngặt: Schema chuẩn xác, tự nhiên ngữ cảnh tiếng Nhật, độc lập giải mù đạt 120/120 đáp án khớp, kiểm toán đối kháng 0 trùng lặp/0 lộ đáp án. Báo cáo chi tiết: [QUESTION_BANK_QA](qa/QUESTION_BANK_QA.md), [QUESTION_REVIEW_LEDGER](qa/QUESTION_REVIEW_LEDGER.csv), [REJECTED_ITEMS](qa/REJECTED_ITEMS.json). Cổng E (thẩm định bản ngữ và hiệu chuẩn người học) duy trì trạng thái minh bạch `PENDING_LEARNER_CALIBRATION`.
  - Thiết lập nhà máy đề thi [PRACTICE_SETS](curriculum/PRACTICE_SETS.json): 23 bộ đề hoàn chỉnh gồm 9 Micro-Drills (5 câu), 6 Skill Practice (12–18 câu), 3 Mixed Practice (18–20 câu), 2 Section Simulations (20–24 câu), và 3 Full Mock Exams được đánh dấu minh bạch `NOT_READY — INSUFFICIENT UNIQUE ITEMS`.
  - Khung phương pháp và tư liệu nghe chân thực: [LISTENING_PRACTICE_FRAMEWORK](curriculum/LISTENING_PRACTICE_FRAMEWORK.md) và [LISTENING_RESOURCE_REGISTRY](curriculum/LISTENING_RESOURCE_REGISTRY.json) khai thác nguồn bản quyền mở Japan Foundation (Irodori A2/B1) và NHK World, tuân thủ nguyên tắc giấu kịch bản trước khi nghe lần đầu và không dùng TTS giả danh băng thi thật.
- **Checkpoint 3.7-C (Triển khai & Đồng bộ cổng Google Sites)**:
  - Xuất bản mới trang **ÔN THEO DẠNG** (`https://sites.google.com/view/jp-study/%C3%B4n-theo-d%E1%BA%A1ng`) tổ chức theo mô hình 3 bước (Learn → Practice → Check) phủ 3 cấp độ N4, N3, N2.
  - Tái cấu trúc trang **LUYỆN TẬP (Kho đề)** (`https://sites.google.com/view/jp-study/luy%E1%BB%87n-t%E1%BA%ADp`) tích hợp đầy đủ 5 phân hệ luyện đề, duy trì 100% hoạt động của 3 Form P0 và lộ trình P1.
  - Cập nhật tài liệu nghiệm thu giao diện [GOOGLE_SITES_UI_QA](GOOGLE_SITES_UI_QA.md).

## Phase 3.6 — Cổng học tập Google Sites hoàn tất, tối ưu UI/UX Mobile-First

- Xây dựng cổng học tập trực quan trên nền Google Sites (`JP-STUDY — 日本語を少しずつ`) làm điểm chạm duy nhất hàng ngày cho người học, thay thế giao diện kỹ thuật thô của Sheets/Forms.
- Giao diện thiết kế theo phong cách tối giản Nhật Bản, theme Aristotle (khói tím / lavender), phông chữ Hiện đại, tiêu đề gọn không chiếm diện tích màn hình điện thoại.
- Hoàn thiện 5 phân hệ người học:
  1. **Trang chủ**: Thẻ bài học hôm nay (N4 Trợ từ trong câu, 5–8 phút), nút bấm nổi bật `BẮT ĐẦU HỌC` liên kết trực tiếp Form W01-B01, tổng quan hoạt động và lời nhắc nghỉ ngơi ("Không khỏe thì nghỉ. Ngày mai học tiếp cũng được.").
  2. **Luyện tập**: Danh mục 3 bài tập Tuần 01 đã sẵn sàng (`W01-B01`, `W01-B02`, `W01-B03`), bài Tuần 02 đánh dấu "Chờ kích hoạt", kèm lời khuyên nhẹ nhàng.
  3. **Mẹo học**: Tóm lược 6 tài liệu PDF cốt lõi (31 mẫu ngữ pháp N4, mẹo nghe, mẹo đọc, cặp ngữ pháp dễ nhầm, giao tiếp đời sống, khung viết/nói).
  4. **Nghe & Nói**: Tuyển chọn nguồn chuẩn NHK World Easy Japanese và Japan Foundation Irodori, 4 tình huống hội thoại đời sống, prompt luyện nói phản xạ 1-1 cùng gia sư AI Gemini.
  5. **Tiến bộ**: Hướng dẫn quy trình 4 bước Gemini Error Tutor ("Chữa MỘT lỗi sau mỗi lần nộp rồi dừng lại"), giải thích cấu trúc 5 tab bảng tính trung tâm và link mở bảng an toàn.
- Kiểm thử responsive hoàn tất trên 6 khung nhìn: 360x800, 390x844, 430x932, 768x1024, 1280x800, 1440x900; 100% không vỡ khung, không cuộn ngang, touch target >= 48px.
- Cài đặt xuất bản bảo mật: Bật tùy chọn chặn công cụ tìm kiếm lập chỉ mục ("Yêu cầu công cụ tìm kiếm công khai không hiển thị trang web của tôi").
- Giữ nguyên 100% kiến trúc backend gốc (Google Sheets, Forms, Apps Script trigger, Drive). Nghiệm thu UI/UX: [GOOGLE_SITES_UI_QA](GOOGLE_SITES_UI_QA.md).

## Phase 3.5 — nghiệm thu P0 hoàn tất, kích hoạt Forms thành công

- Đã tạo Drive riêng tư đúng cấu trúc, một Google Sheet native 5 tab, 7 PDF ngắn (9 trang), vai nói và hai prompt. Link thật bàn giao riêng, không đưa lên GitHub.
- Đã đọc lại ô/validation/quyền bằng API: HOME 2 cột, trạng thái sẵn sàng, lịch sử sạch (0 learner rows), chỉ chủ sở hữu truy cập. Liên kết động trong bộ cài dùng rich text theo chuẩn Google.
- Đã xuất từ chính native Sheets để rà 5 tab; responsive testing đạt trên kích thước mobile (390 px) và laptop (1280 px).
- Bộ cài tự nhận bảng được gắn, tạo quiz, giữ raw responses, cách ly QA, chống trùng và xuất CSV/JSON. 10 quiz dùng lại 68 câu đã QA; 12 câu nguồn còn dự trữ, không tăng ngân hàng.
- **394/394 kiểm logic/Workspace mock đạt.** Đã thực thi Apps Script gắn với bảng qua trình duyệt: `setupP0` và `auditForms` hoàn tất; đúng 3 Form P0 (18 câu), 1 bảng raw với ba tab phản hồi. Không tạo 7 P1 khi chưa có nhu cầu.
- Sửa lỗi Google thực tế: `getDestinationId()` ném lỗi khi Form chưa có đích; bộ cài bắt đúng lỗi này và liên kết bảng raw.
- Bật Drive Advanced Service v3 với sự đồng ý của owner. Đã gỡ quyền `anyone` của responder từ cả ba Form; đọc lại `includePermissionsForView=published` xác nhận mỗi Form chỉ có owner.
- **Đã nghiệm thu live P0 trọn vẹn:** Đã cấu hình trả điểm ngay sau khi nộp (Immediate release) cùng phản hồi chi tiết. Thực hiện nộp QA giả lập thực tế trên cả 3 Form qua browser automation; điểm số hiển thị chính xác (W01-B01: 3/5, W01-B02: 6/8, W01-B03: 3/5) với đầy đủ mẫu câu đúng, sai và bỏ trống. Trigger `onQuizSubmit` phân luồng dữ liệu QA vào `NHAT_KY_QA` và tạo bảng riêng `JP_STUDY_QA_SYNTHETIC` mà không ghi đè vào lịch sử người học (`learnerRows: 0`). Đã chạy `activateP0Verified`: cell B6 hiện `Sẵn sàng`, B7 hiện link `MỞ BÀI NGẮN`, tab `TUẦN NÀY` mở link 3 Form P0. Đã chạy thử xuất báo cáo quản lý CSV/JSON thành công vào Drive. [Bằng chứng đã lược thông tin riêng](qa/drive_first_deployment.json).
- Báo cáo chỉ phản ánh lượt quiz đã nộp. Nghe/nói/học ngoài hệ thống chưa ghi; không suy ra không học, không suy phút học từ timestamp, không coi điểm ôn tăng là tiến bộ độc lập.

Nghiệm thu và giới hạn: [DRIVE_FIRST_QA](DRIVE_FIRST_QA.md). Cài/kích hoạt: [DRIVE_SETUP](DRIVE_SETUP/README.md).

## Các checkpoint trước đã hoàn thành

- Phase 1: nghiên cứu, kế hoạch tạm thời, tracker; bản gốc giữ local, bản Markdown công khai thay hồ sơ thật bằng ví dụ tổng hợp.
- Phase 2: hướng dẫn bắt đầu/chẩn đoán, prompt gia sư, tracker v2, nguồn và QA.
- Phase 2.1: sổ tay tích hợp 12 trang bản gốc, tracker 5 trang tính và prompt cuối; bản công khai sổ tay bằng Markdown đã lược hồ sơ.
- Phase 3 Checkpoint 1–3: ledger, 14 kỹ thuật, schema, pilot, chấm và chọn bài, Gemini; chạy văn bản offline, xuất/nhập tiến độ, phân biệt câu mới/ôn/hỗ trợ.
- Phần Excel của Checkpoint 4 và kiểm giao pilot: tracker 6 trang tính, CSV 12 cột, giây nguyên; năm trang cũ được giữ nguyên.
- Phụ lục: 31 thẻ mẫu, 37 ví dụ chỉ để học; 12 khung viết/nói; mẹo đọc/nghe có nguồn và phân biệt heuristic.
- Đồng bộ công khai: bản gốc không bị ghi đè, kiểm kê nguồn có SHA-256, bản công khai lược hồ sơ và đường dẫn máy, giữ nội dung đã QA.

## Đã kiểm định và còn cần sửa

| Hạng mục | Số lượng | Phạm vi |
|---|---:|---|
| Câu trắc nghiệm N4 | 80 | AI khác giải mù toàn bộ lượt đầu; sửa và tái kiểm có mục tiêu; không tuyên bố giải mù toàn bộ lần hai |
| Vai nói | 4 | Rà độc lập; không có một đáp án duy nhất |
| Thẻ / ví dụ học | 31 / 37 | Rà lũy kế, không cộng vào ngân hàng 80 câu |
| Recipe | 30 | Ghép lại cùng ngân hàng 80, không phải 30 đề độc lập |
| Phát hiện nội dung còn mở sau tái kiểm cuối | 0 | Chỉ trong phạm vi AI QA được ghi; chưa có thẩm định bản ngữ |

QA lịch sử: engine 421 nhóm, browser 36 mục, luồng bổ sung 11, Excel native 64, toàn vẹn 28; kết quả này thuộc bản gốc tại checkpoint. Bản công khai kiểm lại phần bị ảnh hưởng; xem [PUBLICATION_QA](qa/PUBLICATION_QA.md), không coi hash PDF mới là hash PDF cũ.

## Đang làm / chưa làm

- Checkpoint 4 **một phần**: chưa mở rộng 300–500 câu, chưa có ngân hàng N3/N2. Chưa tuyên bố hoàn thành toàn Phase 3.
- Chưa có dữ liệu chẩn đoán hoặc thử nghiệm người học thật mới, nên không có dự báo xác suất đỗ, tốc độ học hay lịch tuần cố định.
- Chưa hiệu chuẩn độ khó/thời gian, chưa thẩm định giáo viên bản ngữ, chưa kiểm iPad thật hoặc nghe TTS bằng âm thực.
- Mã build lịch sử là **DRAFT**, có phụ thuộc tệp trung gian; không phải pipeline tái tạo toàn bộ chỉ bằng một lệnh.
- Nguồn sau paywall chỉ dùng trong giới hạn abstract/metadata được ghi; lỗi Crossref 429/404 không được tính là xác minh.

## Checkpoint tiếp theo

Hoàn tất OAuth cho script đã gắn, rồi tiếp tục nghiệm thu trực tiếp 3 Form P0 từ làm → nộp → điểm → lỗi → Gemini → lịch sử → CSV bằng dữ liệu QA trong bảng riêng; sau đó mới mở 7 Form P1. Thu dữ liệu tự nguyện ngày 7/14 và thử người học trên thiết bị thực; kiểm giọng Nhật hoặc chọn MP3 chính thức. Sửa vấn đề được quan sát rồi mới duyệt mở rộng từng lô. Mỗi lô phải giữ ID/khóa/schema đồng bộ, QA độc lập theo phạm vi, cập nhật manifest/docs, commit và push. Không sinh thêm câu chỉ để đủ số lượng.
