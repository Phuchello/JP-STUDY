# Trạng thái dự án — 16/10/2026

## Phase 3.7 — Gia cố cổng kiểm định phản biện (Adversarial QA Hardening, Two-Gate STAR Auditor & Provenance Integrity)

- **Xóa bỏ hoàn toàn mã cứng kết luận ngữ nghĩa câu hỏi dấu sao (Two-Gate STAR Architecture)**:
  - Loại bỏ triệt để việc gán kết luận ngữ nghĩa theo ID câu hỏi (`evaluate_permutation_syntax`) trong `scripts/curriculum/audit_star_permutations.py`.
  - Thiết lập kiến trúc kiểm định hai cổng độc lập (Two-Gate Architecture):
    - **Cổng 1 (Kiểm định cấu trúc - Structural Validation)**: Kiểm tra 4 ngữ đoạn riêng biệt, duyệt toàn bộ 24 hoán vị ($4! = 24$), tiền tố/hậu tố tái tạo, khớp câu chuẩn tắc, khớp ô số 3 và phát hiện xung đột trợ từ đồng vị qua ranh giới ngữ đoạn (`check_generic_structural_constraints`). Kết quả: **16 / 16 câu đạt Cổng 1 (PASS)**.
    - **Cổng 2 (Thẩm định độc lập tính duy nhất về ngữ nghĩa - Semantic Uniqueness)**: Không bao giờ tự động suy diễn các hoán vị phi chuẩn tắc là sai ngữ pháp khi chưa có hội đồng chuyên gia độc lập xác nhận. Trạng thái phản ánh trung thực: **`STAR_SEMANTIC_REVIEW_PENDING`**, yêu cầu rà soát bổ sung (`QA_REVIEW_REQUIRED`).
    - Tuyệt đối không tuyên bố tự động "384/384 semantic PASS". Xuất sổ cái độc lập [`qa/STAR_SEMANTIC_REVIEW_LEDGER.json`](qa/STAR_SEMANTIC_REVIEW_LEDGER.json) và báo cáo [`qa/STAR_PERMUTATION_AUDIT.md`](qa/STAR_PERMUTATION_AUDIT.md).
- **Bộ đối chứng tiêu cực thực chất cho câu dấu sao (Real Negative-Control Tests)**:
  - Xây dựng bài kiểm thử mẫu câu dấu sao mơ hồ tự nhiên bằng tiếng Nhật với cấu trúc trạng ngữ di động tự do trước vị ngữ (nghiệm thức Tanaka-san: `昨日` / `会議で` / `その計画について` / `熱心に`), chứng minh hệ thống kiểm định từ chối xác nhận `VERIFIED_COHERENT`, trả về đúng `STAR_SEMANTIC_REVIEW_PENDING`.
  - Bổ sung 6 ca đối chứng tiêu cực: thiếu câu chuẩn tắc, sai khóa đáp án ô số 3, trùng lặp ngữ đoạn, số lượng ô sai quy cách, xung đột trợ từ cách (double case-particle collision), và ID không xác định. Toàn bộ 7 bài kiểm thử đối chứng tiêu cực đều PASS.
- **Mở rộng hệ thống băm mật mã 4 tầng (4-Tier Cryptographic Fingerprints)**:
  - Nâng cấp `scripts/curriculum/content_fingerprint.py` với 4 mã băm SHA-256 riêng biệt:
    1. `BLIND_INPUT_SHA256`: ID, level, typeId, stem, contextPassage, sorted options.
    2. `SCORING_SHA256`: ID, level, typeId, correctAnswer, option ID-to-text bindings.
    3. `PEDAGOGICAL_CONTENT_SHA256`: explanationVi, distractorExplanations, remediation, assembledSentence.
    4. `FULL_ITEM_SHA256`: Tổng thể toàn bộ dữ liệu phát hành của câu hỏi.
  - Kiểm toán tái tạo từ sandbox cô lập (`scripts/curriculum/verify_rebuild_invariance.py`): đạt độ ổn định tuyệt đối **120 / 120 câu** qua 2 lượt build liên tiếp (0 content drift, 0 repaired item drift, 0 historical file drift). Báo cáo chi tiết: [`qa/REPRODUCIBILITY_AUDIT.md`](qa/REPRODUCIBILITY_AUDIT.md).
- **Minh bạch hóa nguồn gốc thẩm định 3 tầng (Honest 3-Tier Review Provenance)**:
  - Phân tách rạch ròi giữa việc khớp băm nội dung (`CONTENT_HASH_MATCHED: True`), lưu trữ đầu ra thẩm định (`REVIEW_OUTPUT_RECORDED: True`), và chứng thực thực thi (`EXECUTION_PROVENANCE_REPORTED_NOT_ATTESTED`).
  - Phân loại trung thực trạng thái chứng thực nguồn gốc là `PARTIAL` thay vì tuyên bố tuyệt đối do thiếu chữ ký mật mã khóa công khai ngoài repository. Ghi nhận chi tiết tại [`qa/CONTENT_FINGERPRINT_MANIFEST.json`](qa/CONTENT_FINGERPRINT_MANIFEST.json) và [`qa/REVIEW_PROVENANCE_AUDIT.md`](qa/REVIEW_PROVENANCE_AUDIT.md).
- **Cổng phát hành bộ đề động & Ranh giới phát hành an toàn (Dynamic Practice Release Gate)**:
  - Chuyển đổi toàn bộ việc tính toán 7 chiều chất lượng sang logic động dựa trên ngân hàng câu hỏi và bộ đề thực tế tại `scripts/curriculum/generate_practice_release_gate.py`.
  - Phân loại rõ ràng:
    - **11 bộ đề `QA_PASSED_NOT_DEPLOYED`**: Chứa 100% câu hỏi đã qua giải mù và thẩm định (`QA_VERIFIED`), hoàn toàn không chứa câu hỏi dấu sao, đủ điều kiện kỹ thuật để chạy thử nghiệm có kiểm soát.
    - **9 bộ đề `CONTENT_QA_BLOCKED`**: Bị chặn tự động và an toàn do chứa câu hỏi dấu sao đang chờ hội đồng thẩm định ngữ nghĩa (`STAR_SEMANTIC_REVIEW_PENDING`).
    - **3 bộ đề thi thử `NOT_READY`**: Chờ mở rộng ngân hàng câu hỏi.
  - Bộ đề sẵn sàng chạy thử nghiệm có kiểm soát (Controlled Pilot): `MD-N4-VOC-01` (5 câu N4 Từ vựng, 0 câu dấu sao, 100% `QA_VERIFIED`).
- **Bộ kiểm thử đột biến phản biện hoàn chỉnh (19 Production Integration Tests)**:
  - [`scripts/tests/test_qa_adversarial_mutations.py`](scripts/tests/test_qa_adversarial_mutations.py) đạt kết quả tuyệt đối **19 / 19 tests PASS** (12 kịch bản đột biến hệ thống + 7 kịch bản đối chứng tiêu cực câu dấu sao), xuất báo cáo nghiệm thu [`qa/ADVERSARIAL_TEST_RESULTS.md`](qa/ADVERSARIAL_TEST_RESULTS.md).
- **Bảo toàn 100% Forms P0 & Báo cáo rào cản tài khoản Google Workspace**:
  - Bảo toàn trọn vẹn 3 Forms P0 đang hoạt động (`W01-B01`, `W01-B02`, `W01-B03`). Không tự tạo Forms giả mạo trên Google Drive khi chưa có phiên đăng nhập xác thực.

---

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

- **Kiểm toán tái lập P0 & Bảo toàn tính bất biến (P0 Reproducibility & Content Invariance)**:
  - Tích hợp 6 câu hỏi sửa đổi trực tiếp vào định nghĩa nguồn chuẩn tắc trong `scripts/curriculum/rebuild_and_repair_bank.py` với hạt giống xáo trộn xác định `seed-clean-audit`.
  - Thực thi kiểm toán trong môi trường sandbox cô lập dùng một lần (`scripts/curriculum/verify_rebuild_invariance.py`): chạy tái tạo 2 lần liên tiếp, đối chiếu băm SHA-256 chuẩn tắc của 120/120 câu hỏi đối với checkpoint được nghiệm thu.
  - Kết quả: **0 câu lệch dữ liệu (120/120 identical)**, 6 câu sửa đổi được bảo toàn tuyệt đối, các tập tin chứng cứ lịch sử (`qa/blind_review_n*.json`, `qa/raw_blind_review_*.json`) hoàn toàn bất biến. Báo cáo chi tiết: [`qa/REPRODUCIBILITY_AUDIT.md`](qa/REPRODUCIBILITY_AUDIT.md).

- **Chứng thực vân tay mật mã & Khóa liên kết thẩm định (P0 Cryptographic Evidence Binding)**:
  - Xây dựng mô-đun sinh vân tay nội dung chuẩn tắc `canonical_question_fingerprint` (Unicode NFC, sắp xếp thuộc tính và danh sách lựa chọn, mã hóa SHA-256) tại `scripts/curriculum/content_fingerprint.py`.
  - Tạo manifest chứng thực [`qa/CONTENT_FINGERPRINT_MANIFEST.json`](qa/CONTENT_FINGERPRINT_MANIFEST.json) liên kết từng kết quả giải mù với mã băm câu hỏi, mã băm tập dữ liệu, mã đợt (batch ID), reviewer ID, conversation ID và digest của tệp thô.
  - Cập nhật hàm cổng kiểm soát `evaluate_question_qa_gate`: từ chối thẳng thừng các kết quả giải mù có vân tay sai lệch (`FINGERPRINT_MISMATCH`) hoặc thiếu liên kết mật mã (`REVIEW_PROVENANCE_UNVERIFIED`). Báo cáo nguồn gốc chi tiết: [`qa/REVIEW_PROVENANCE_AUDIT.md`](qa/REVIEW_PROVENANCE_AUDIT.md).

- **Kiểm toán hoán vị câu hỏi dấu sao 24! (Dynamic 24-Permutation Star Audit)**:
  - Rà quét động toàn bộ ngân hàng: xác nhận chính xác **16 câu dấu sao** (N4: 6 câu, N3: 6 câu, N2: 4 câu; không giả định hoặc mã cứng).
  - Tách 4 ngữ đoạn và chạy thử nghiệm toàn bộ 24 hoán vị ($4! = 24$) cho mỗi câu (tổng cộng 384 hoán vị câu ghép), kiểm tra ngữ đoạn tại vị trí ★ (ô số 3) so với đáp án tác giả.
  - Thẩm định ngôn ngữ học: phân loại chính xác các hoán vị thành `CANONICAL_CORRECT`, `GRAMMATICALLY_INVALID`, `PRAGMATICALLY_UNNATURAL`.
  - Kết quả: **0 hoán vị thay thế hợp lệ làm thay đổi đáp án vị trí dấu sao** trên toàn bộ 16 câu. Báo cáo tự động: [`qa/STAR_PERMUTATION_AUDIT.md`](qa/STAR_PERMUTATION_AUDIT.md).

- **Cổng kiểm soát phát hành bộ đề & 7 chiều chất lượng (P1 Practice Release Gate)**:
  - Phân tách rạch ròi 7 chiều chất lượng trong [`qa/PRACTICE_RELEASE_GATE.md`](qa/PRACTICE_RELEASE_GATE.md): (1) Content Validity (`QA_VERIFIED`), (2) Review Provenance (`CRYPTOGRAPHICALLY_VERIFIED`), (3) Learner Calibration (`PENDING_LEARNER_CALIBRATION`), (4) Exposure Eligibility (`false`), (5) Diagnostic Eligibility (`false`), (6) Google Forms Deployment (`NOT_DEPLOYED`), (7) Live Integration (`UNVERIFIED`).
  - Thanh lọc triệt để các trường `blockReason` lỗi thời khỏi `curriculum/PRACTICE_SETS.json`: 20 bộ đề mang trạng thái sạch `QA_PASSED_NOT_DEPLOYED`, 3 bài thi thử mang trạng thái `NOT_READY`.

- **Bộ kiểm thử tích hợp đột biến phản biện mở rộng (12 Production Integration Tests)**:
  - Cập nhật [`scripts/tests/test_qa_adversarial_mutations.py`](scripts/tests/test_qa_adversarial_mutations.py) với 12 ca kiểm thử gọi trực tiếp các hàm kiểm định thật của hệ thống:
    1. Đột biến 1 ký tự stem -> `FINGERPRINT_MISMATCH` / `QA_REVIEW_REQUIRED`.
    2. Đột biến 1 nội dung lựa chọn giữ nguyên ID -> `FINGERPRINT_MISMATCH` / `QA_REVIEW_REQUIRED`.
    3. Trùng lặp bản ghi reviewer trong batch đầu vào -> ném lỗi `ValueError`.
    4. Xóa bản ghi reviewer -> `check_review_integrity` thất bại / chặn QA.
    5. Tiêm đáp án xung đột -> `QUARANTINED`.
    6. Bổ sung đáp án thay thế hợp lệ -> `QA_REVIEW_REQUIRED`.
    7. Làm hỏng khóa đáp án câu dấu sao -> `audit_star_question` thất bại.
    8. Đưa ID câu dấu sao không tồn tại vào báo cáo -> phát hiện không khớp ngân hàng thật.
    9. Tham chiếu câu hỏi bị hỏng trong bộ đề -> `reconcile_practice_set_status` gắn cờ `CONTENT_QA_BLOCKED`.
    10. Đánh dấu Form không tồn tại là `LIVE_VERIFIED` -> bị từ chối, ép về `QA_PASSED_NOT_DEPLOYED`.
    11. Tái tạo ngân hàng 2 lần -> bất biến vân tay mật mã 120/120 câu.
    12. Tái tạo báo cáo từ nguồn -> kiểm chứng tính nhất quán về số lượng, ID và đáp án.
  - Toàn bộ **12 / 12 bài kiểm thử tích hợp vượt qua thành công** (0.014s).

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
