# Trạng thái dự án — 16/10/2026

## Phase 3.7 — Đối soát kiểm định cuối cùng, xử lý dứt điểm mơ hồ ngữ nghĩa & Thử nghiệm kiểm soát (Final QA Reconciliation & Ambiguity Repair)

- **Xử lý triệt để 6 câu hỏi bị cảnh báo/mơ hồ ngữ nghĩa (Checkpoint Remediation)**:
  - Tái cấu trúc và khóa cứng cú pháp/ngữ nghĩa cho toàn bộ 6 câu hỏi được ghi nhận trong đợt kiểm toán:
    1. `N4-GR-FORM-010`: Loại bỏ phương án gây mơ hồ `よかったら`; bổ sung đáp án sai quy tắc hình thái `いいば` và nhượng bộ `よくても`. Đáp án chuẩn duy nhất: `よければ` (A).
    2. `N4-GR-STAR-002`: Tái thiết kế thành chuỗi mệnh đề định ngữ chặt chẽ (`北海道に住んでいる友達に会いに行く`), loại bỏ triệt để khả năng đảo vị trí giới từ ngữ (PP scrambling). Vị trí ★: `友達に` (D).
    3. `N4-GR-STAR-006`: Thay thế trạng từ thời gian di động `今` bằng cụm danh từ tân ngữ `お金を`, khóa cứng thứ tự ngữ pháp (`店を持つために お金を ためようと`). Vị trí ★: `お金を` (A).
    4. `N2-GR-FORM-003`: Thay thế phương án gần nghĩa `する一方だ` bằng các đáp án nhiễu rõ ràng `しっこない` và `しがたい`. Mẫu câu tiếp diễn xu hướng khách quan: `しつつある` (A).
    5. `N3-GR-FORM-006`: Thay thế phương án trùng lặp nguyên nhân `わけ` bằng sắc thái chủ quan `つもり`, làm nổi bật suy luận logic dựa trên tiền đề thực tế: `はずだ` (B).
    6. `N3-GR-STAR-001`: Thay thế cụm trạng từ di động (`誰でも`/`自由に`) bằng mệnh đề điều kiện tiên quyết `意欲があれば`, khóa cứng chuỗi liên kết cú pháp (`有無にかかわらず 意欲があれば 誰でも`). Vị trí ★: `意欲が` (A).
  - Xuất bảng so sánh chi tiết trước và sau sửa đổi tại [`qa/flagged_questions_diff.json`](qa/flagged_questions_diff.json).

- **Phiên giải mù độc lập bổ sung & Chứng cứ nguyên bản**:
  - Xuất tập dữ liệu giải mù thuần túy cho 6 câu đã sửa (không có đáp án/giải thích): [`qa/blind_review_repaired_6.json`](qa/blind_review_repaired_6.json).
  - Khởi tạo phiên Subagent độc lập (`subagent:jlpt-blind-reviewer`) thẩm định trực tiếp từ tiếng Nhật:
    - Độ đồng thuận đạt tuyệt đối **6 / 6 (100.0%)** so với đáp án tác giả.
    - Phương án thay thế hợp lệ (Alternative Defensible Answers): **0 phương án** (`[]`).
    - Quan ngại ngữ nghĩa/ngữ cảnh (Concerns): **0 quan ngại** (`null`).
    - Độ tin cậy (Confidence): 100% `HIGH`.
  - Lưu chứng cứ phản biện gốc tại [`qa/raw_blind_review_repaired_6.json`](qa/raw_blind_review_repaired_6.json).

- **Kiểm toán động câu hỏi dấu sao (Dynamic Star Question Audit)**:
  - Loại bỏ hoàn toàn số liệu giả định 18 câu; bộ tạo báo cáo tự động rà quét trực tiếp từ ngân hàng câu hỏi nguồn và xác nhận có đúng **16 câu dấu sao** (N4: 6 câu, N3: 6 câu, N2: 4 câu; không tự sáng tác thêm 2 câu N2 ngoài ngân hàng).
  - Kiểm toán động 100% câu hỏi dấu sao: cấu trúc đúng 4 ô, vị trí ★ cố định ở ô số 3, câu ghép hoàn chỉnh tự nhiên, và tồn tại duy nhất 1 hoán vị cú pháp hợp lệ. Báo cáo tự động cập nhật tại [`qa/BLIND_REVIEW_RECONCILIATION_REPORT.md`](qa/BLIND_REVIEW_RECONCILIATION_REPORT.md).

- **Chuẩn hóa trạng thái phát hành bộ đề & Thử nghiệm kiểm soát (Controlled Pilot Protocol)**:
  - Thống nhất một trạng thái phát hành chuẩn `readinessStatus` và đồng bộ trường `status` trong [`curriculum/PRACTICE_SETS.json`](curriculum/PRACTICE_SETS.json):
    - 20 bộ đề luyện tập (Micro-drills, Skill practice, Mixed practice, Section simulations): `QA_PASSED_NOT_DEPLOYED` (`SPEC_ONLY`).
    - 3 bài thi thử hoàn chỉnh (Full Mock Exams): `NOT_READY` (`INSUFFICIENT_UNIQUE_ITEMS`).
  - Thử nghiệm kiểm soát (Controlled Pilot): Đã kiểm tra phiên làm việc trong môi trường trình duyệt. Do chưa có phiên ủy quyền Google Workspace / Apps Script sẵn sàng để triển khai Form tự động, hệ thống dừng lại an toàn tại điểm kiểm soát mã nguồn và dữ liệu đã được nghiệm thu.
  - **Báo cáo trung thực**: 0 Form mới được tạo hoặc xuất bản; tuyệt đối không tạo URL Forms giả lập. Bảo toàn nguyên vẹn 3 Form P0 hiện hữu (`W01-B01`, `W01-B02`, `W01-B03`) và toàn bộ bảng dữ liệu phản hồi của học viên.

- **Bộ kiểm thử tích hợp đột biến phản biện mở rộng (12 Integration Tests)**:
  - Cập nhật [`scripts/tests/test_qa_adversarial_mutations.py`](scripts/tests/test_qa_adversarial_mutations.py) với 12 ca kiểm thử tích hợp thực thi trực tiếp các hàm kiểm định trong quy trình sản xuất:
    1. Phát hiện lỗi schema (thiếu trường, sai định dạng).
    2. Phát hiện chuỗi đáp án lặp chu kỳ 4-tuple ABCD.
    3. Phát hiện phân bổ đáp án bị thiên lệch vượt ngưỡng.
    4. Phát hiện câu ghép dấu sao sai ngữ pháp.
    5. Phát hiện phương án đúng thứ hai gây mơ hồ ngữ nghĩa.
    6. Phát hiện độ tin cậy của reviewer dưới mức HIGH.
    7. Phát hiện trùng lặp thân câu hỏi (stem).
    8. Phát hiện thiếu giải thích chi tiết tiếng Việt.
    9. Phát hiện văn bản các lựa chọn trùng nhau.
    10. Phát hiện ký tự đáp án ngoài khoảng A-D.
    11. Phát hiện câu dấu sao thiếu trường assembledSentence.
    12. Phát hiện câu dấu sao tồn tại nhiều hơn 1 hoán vị ngữ pháp hợp lệ.
  - Toàn bộ **12 / 12 bài kiểm thử tích hợp vượt qua thành công** (0.004s).

- **Phân bổ đáp án & Trạng thái toàn ngân hàng**:
  - Tổng số: 120 câu hỏi độc lập (N4: 40, N3: 50, N2: 30).
  - Phân bổ vị trí đáp án: **A: 33 (27.5%), B: 30 (25.0%), C: 29 (24.2%), D: 28 (23.3%)**.
  - Chuỗi lặp 4-tuple ABCD: 1 (mức xác suất ngẫu nhiên kỳ vọng). Chuỗi trùng liên tiếp tối đa: 3.
  - Trạng thái kiểm định ngân hàng: **120 / 120 câu đạt `QA_VERIFIED`**.
  - Sổ cái kiểm định [`qa/QUESTION_REVIEW_LEDGER.csv`](qa/QUESTION_REVIEW_LEDGER.csv) cập nhật đầy đủ dấu vết kiểm toán, phiên bản dữ liệu và nhật ký sửa đổi.

---

## Phase 3.7 — Phục hồi kiểm định chất lượng độc lập (Independent QA Recovery Baseline)

- **Loại bỏ triệt để bộ giải lookup mã cứng & Thiết lập quy trình thẩm định mù thực chất**:
  - Đã xóa bỏ hoàn toàn hàm lookup từ điển gán đáp án và danh tính giả mạo; thay thế bằng quy trình giải mù độc lập 100% từ mô hình ngôn ngữ tách biệt qua Subagent (`subagent:jlpt-blind-reviewer`).
  - Xuất 4 tập dữ liệu giải mù thuần túy, tước bỏ hoàn toàn đáp án tác giả và phần giải thích: `qa/blind_review_dataset.json` (120 câu), `qa/blind_review_n4.json` (40 câu), `qa/blind_review_n3.json` (50 câu), `qa/blind_review_n2.json` (30 câu).
  - Khởi tạo 3 phiên Subagent độc lập giải đề trực tiếp từ văn bản tiếng Nhật theo quy tắc ngữ pháp, ngữ nghĩa, ngữ dụng và tiêu chuẩn JLPT.
  - Lưu trữ chứng cứ nguyên bản không can thiệp tại:
    - [`qa/raw_blind_review_n4.json`](qa/raw_blind_review_n4.json) (40 câu N4)
    - [`qa/raw_blind_review_n3.json`](qa/raw_blind_review_n3.json) (50 câu N3)
    - [`qa/raw_blind_review_n2.json`](qa/raw_blind_review_n2.json) (30 câu N2)

---

## Phase 3.6 — Cổng học tập Google Sites hoàn tất, tối ưu UI/UX Mobile-First

- Xây dựng cổng học tập trực quan trên nền Google Sites (`JP-STUDY — 日本語を少しずつ`) làm điểm chạm duy nhất hàng ngày cho người học, thay thế giao diện kỹ thuật thô của Sheets/Forms.
- Giao diện thiết kế theo phong cách tối giản Nhật Bản, theme Aristotle (khói tím / lavender), phông chữ Hiện đại, tiêu đề gọn không chiếm diện tích màn hình điện thoại.
- Hoàn thiện 5 phân hệ người học: Trang chủ, Luyện tập, Mẹo học, Nghe & Nói, Tiến bộ.
- Kiểm thử responsive hoàn tất trên 6 khung nhìn: 360x800, 390x844, 430x932, 768x1024, 1280x800, 1440x900; 100% không vỡ khung, không cuộn ngang, touch target >= 48px.
- Cài đặt xuất bản bảo mật: Bật tùy chọn chặn công cụ tìm kiếm lập chỉ mục ("Yêu cầu công cụ tìm kiếm công khai không hiển thị trang web của tôi").
- Giữ nguyên 100% kiến trúc backend gốc (Google Sheets, Forms, Apps Script trigger, Drive). Nghiệm thu UI/UX: [GOOGLE_SITES_UI_QA](GOOGLE_SITES_UI_QA.md).

---

## Phase 3.5 — nghiệm thu P0 hoàn tất, kích hoạt Forms thành công

- Đã tạo Drive riêng tư đúng cấu trúc, một Google Sheet native 5 tab, 7 PDF ngắn (9 trang), vai nói và hai prompt. Link thật bàn giao riêng, không đưa lên GitHub.
- 394/394 kiểm logic/Workspace mock đạt. Đã thực thi Apps Script gắn với bảng qua trình duyệt: `setupP0` và `auditForms` hoàn tất; đúng 3 Form P0 (18 câu), 1 bảng raw với ba tab phản hồi.
- Sửa lỗi Google thực tế: `getDestinationId()` ném lỗi khi Form chưa có đích; bộ cài bắt đúng lỗi này và liên kết bảng raw.
- Bật Drive Advanced Service v3 với sự đồng ý của owner. Đã gỡ quyền `anyone` của responder từ cả ba Form; đọc lại `includePermissionsForView=published` xác nhận mỗi Form chỉ có owner.
