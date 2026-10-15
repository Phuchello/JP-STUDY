# Trạng thái dự án — 15/10/2026

## Phase 3.7 — Phục hồi kiểm định chất lượng độc lập (Independent QA Recovery Completed)

- **Loại bỏ triệt để bộ giải lookup mã cứng & Thiết lập quy trình thẩm định mù thực chất**:
  - Đã xóa bỏ hoàn toàn hàm lookup từ điển gán đáp án và danh tính giả mạo; thay thế bằng quy trình giải mù độc lập 100% từ mô hình ngôn ngữ tách biệt qua Subagent (`subagent:jlpt-blind-reviewer`).
  - Xuất 4 tập dữ liệu giải mù thuần túy, tước bỏ hoàn toàn đáp án tác giả và phần giải thích: `qa/blind_review_dataset.json` (120 câu), `qa/blind_review_n4.json` (40 câu), `qa/blind_review_n3.json` (50 câu), `qa/blind_review_n2.json` (30 câu).
  - Khởi tạo 3 phiên Subagent độc lập giải đề trực tiếp từ văn bản tiếng Nhật theo quy tắc ngữ pháp, ngữ nghĩa, ngữ dụng và tiêu chuẩn JLPT.
  - Lưu trữ chứng cứ nguyên bản không can thiệp tại:
    - [`qa/raw_blind_review_n4.json`](qa/raw_blind_review_n4.json) (40 câu N4)
    - [`qa/raw_blind_review_n3.json`](qa/raw_blind_review_n3.json) (50 câu N3)
    - [`qa/raw_blind_review_n2.json`](qa/raw_blind_review_n2.json) (30 câu N2)
- **Tái phân bổ đáp án ngẫu nhiên có kiểm soát (Seeded Reshuffle - Non-cyclic)**:
  - Áp dụng thuật toán xáo trộn theo hạt giống câu hỏi `seed-clean-audit`, bảo toàn nguyên vẹn nội dung lựa chọn đúng và các giải thích phân tích phương án nhiễu.
  - Loại bỏ hoàn toàn chuỗi lặp chu kỳ 4-tuple ABCD: số lần xuất hiện chuỗi `ABCD` giảm từ 30 xuống còn 1 (mức xác suất ngẫu nhiên thông thường $120/256$).
  - Chuỗi đáp án trùng lặp liên tiếp tối đa là 3 câu.
  - Phân bổ vị trí đáp án trên toàn bộ 120 câu:
    - **A:** 33 câu (27.5%)
    - **B:** 30 câu (25.0%)
    - **C:** 29 câu (24.2%)
    - **D:** 28 câu (23.3%)
- **Quy trình đối soát độc lập & Báo cáo kiểm định minh bạch**:
  - Triển khai `scripts/curriculum/reconcile_blind_review.py` tự động nạp kết quả giải mù từ 3 subagent và đối soát với đáp án tác giả:
    - Tỷ lệ đồng thuận đạt **120 / 120 (100.0%)**.
    - Số câu bất đồng (Disagreements): **0 câu**.
    - Phát hiện và ghi nhận 4 câu có phương án nhiễu gần nghĩa hoặc trạng từ có thể hoán đổi vị trí (N4-GR-FORM-010, N4-GR-STAR-002, N4-GR-STAR-006, N2-GR-FORM-003) tại [`qa/BLIND_REVIEW_RECONCILIATION_REPORT.md`](qa/BLIND_REVIEW_RECONCILIATION_REPORT.md).
  - Kiểm toán cấu trúc 18 câu dấu sao (N4: 6 câu, N3: 6 câu, N2: 6 câu): 100% bảo đảm thứ tự ngữ pháp tự nhiên và vị trí dấu sao cố định tại ô thứ 3.
  - Cập nhật sổ cái kiểm định [QUESTION_REVIEW_LEDGER](qa/QUESTION_REVIEW_LEDGER.csv) với định danh trung thực `subagent:jlpt-blind-reviewer`, mức độ tin cậy `HIGH` và dấu thời gian thực.
  - Cổng E duy trì trạng thái trung thực `PENDING_LEARNER_CALIBRATION`.
- **Bộ kiểm thử đột biến phản biện (Adversarial Mutation Test Suite)**:
  - Ban hành `scripts/tests/test_qa_adversarial_mutations.py` kiểm định khả năng phát hiện tự động của hệ thống đối với 8 lớp lỗi đột biến nguy hiểm:
    1. Đáp án tác giả sai so với kết quả giải mù độc lập (`test_mutation_1_wrong_answer_key`).
    2. Xuất hiện phương án đúng thứ hai gây mơ hồ ngữ nghĩa (`test_mutation_2_second_grammatically_valid_choice`).
    3. Sai lệch thể chia giữa từ đích và lựa chọn đọc (`test_mutation_3_missing_correct_reading`).
    4. Thứ tự ghép câu dấu sao đứt gãy phi ngữ pháp (`test_mutation_4_invalid_star_permutation`).
    5. Lời giải thích mâu thuẫn trực tiếp với ký tự đáp án (`test_mutation_5_explanation_contradicts_answer`).
    6. Đoạn văn đọc hiểu bị thao túng không hỗ trợ đáp án (`test_mutation_6_manipulated_passage`).
    7. Mẫu đáp án lặp chu kỳ ABCD mang tính dự đoán (`test_mutation_7_repeating_abcd_pattern`).
    8. Bộ giải gian lận dùng mã cứng/bảng tra cứu (`test_mutation_8_hardcoded_reviewer_lookup`).
  - Toàn bộ 8/8 bài kiểm tra đột biến vượt qua thành công (100% phát hiện lỗi).
- **Cổng phát hành có kiểm soát & Bảo vệ môi trường thực tế**:
  - Giữ nguyên 100% trạng thái an toàn: **0 Form mới được kích hoạt** (20 bộ đề luyện tập duy trì trạng thái `QA_PASSED_NOT_DEPLOYED`, dạng `SPEC_ONLY`).
  - Bảo toàn tuyệt đối 3 Google Forms P0 đang hoạt động (`W01-B01`, `W01-B02`, `W01-B03`) và toàn bộ dữ liệu học tập của học viên.

---

## Phase 3.7 — Ngân hàng luyện đề JLPT, Chuyên đề kỹ năng & Cổng luyện tập mở rộng (Baseline ban đầu)

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

---

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

---

## Phase 3.5 — nghiệm thu P0 hoàn tất, kích hoạt Forms thành công

- Đã tạo Drive riêng tư đúng cấu trúc, một Google Sheet native 5 tab, 7 PDF ngắn (9 trang), vai nói và hai prompt. Link thật bàn giao riêng, không đưa lên GitHub.
- Đã đọc lại ô/validation/quyền bằng API: HOME 2 cột, trạng thái sẵn sàng, lịch sử sạch (0 learner rows), chỉ chủ sở hữu truy cập. Liên kết động trong bộ cài dùng rich text theo chuẩn Google.
- Đã xuất từ chính native Sheets để rà 5 tab; responsive testing đạt trên kích thước mobile (390 px) và laptop (1280 px).
- Bộ cài tự nhận bảng được gắn, tạo quiz, giữ raw responses, cách ly QA, chống trùng và xuất CSV/JSON. 10 quiz dùng lại 68 câu đã QA; 12 câu nguồn còn dự trữ, không tăng ngân hàng.
- **394/394 kiểm logic/Workspace mock đạt.** Đã thực thi Apps Script gắn với bảng qua trình duyệt: `setupP0` và `auditForms` hoàn tất; đúng 3 Form P0 (18 câu), 1 bảng raw với ba tab phản hồi. Không tạo 7 P1 khi chưa có nhu cầu.
- Sửa lỗi Google thực tế: `getDestinationId()` ném lỗi khi Form chưa có đích; bộ cài bắt đúng lỗi này và liên kết bảng raw.
- Bật Drive Advanced Service v3 với sự đồng ý của owner. Đã gỡ quyền `anyone` của responder từ cả ba Form; đọc lại `includePermissionsForView=published` xác nhận mỗi Form chỉ có owner.
