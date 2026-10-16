# BÁO CÁO KIỂM TOÁN NGUỒN GỐC & LIÊN KẾT MẬT MÃ THẨM ĐỊNH (REVIEW PROVENANCE AUDIT)
## PHASE 3.7 — HONEST THREE-TIER REVIEW PROVENANCE AUDIT

### 1. TỔNG QUAN HỆ THỐNG VÀ BA CẤP ĐỘ NGUỒN GỐC (THREE-TIER PROVENANCE)

Nhằm tuân thủ nguyên tắc kiểm toán phản biện độc lập, hệ thống JP-STUDY tách bạch nghiêm ngặt 3 khái niệm nguồn gốc kiểm tra:

1. **`CONTENT_HASH_MATCHED`**: Băm SHA-256 chuẩn hóa Unicode NFC của câu hỏi trong ngân hàng khớp 100% với dữ liệu đầu vào đưa cho người giải mù.
2. **`REVIEW_OUTPUT_RECORDED`**: Tập tin kết quả giải mù thô (`qa/raw_blind_review_*.json`) được lưu trữ nguyên bản và toàn vẹn trong kho mã nguồn.
3. **`REVIEW_EXECUTION_ATTESTED`**: Bằng chứng nhật ký thực thi (Execution Logs / Transcripts) từ môi trường chạy thật. Được phân loại trung thực:
   - **`HOST_LOG_VERIFIED`**: Nhật ký máy trạm cục bộ tồn tại tại `~/.gemini/antigravity/brain/<conv_id>/...` và được đối soát mã băm.
   - **`EXECUTION_PROVENANCE_REPORTED_NOT_ATTESTED`**: Ở góc độ repository độc lập di động (clean checkout), các nhật ký ngoài repo chỉ được coi là khai báo hợp lệ (reported), chưa được chứng thực mật mã từ bên thứ ba.
   - **Đánh giá tổng thể mức độ chứng thực thực thi**: **`PARTIAL`**.

---

### 2. BẢNG PHÂN BỔ BỐN LỚP VÂN TAY NỘI DUNG (FOUR HASH TIERS)

Để đảm bảo không bỏ sót bất kỳ đột biến nào làm thay đổi đáp án hoặc nội dung sư phạm, mỗi câu hỏi được gán 4 mã băm độc lập:
- `BLIND_INPUT_SHA256`: Dành riêng cho người giải mù (chỉ chứa stem, passage, options).
- `SCORING_SHA256`: Chứa khóa đáp án (`correctAnswer`) và liên kết lựa chọn chấm điểm.
- `PEDAGOGICAL_CONTENT_SHA256`: Chứa giải thích tiếng Việt, phân tích đáp án nhiễu, câu ghép hoàn chỉnh và hướng dẫn sửa lỗi.
- `FULL_ITEM_SHA256`: Băm chuẩn tắc toàn bộ các trường phát hành của câu hỏi.

---

### 3. KIỂM TOÁN CÁC ĐỢT GIẢI MÙ (EXECUTION BATCHES AUDIT)

| Batch ID | Phạm vi | Tệp đầu vào (Input) | Tệp kết quả thô (Output) | Hash Tệp Thô | Nhật ký máy trạm | Trạng thái chứng thực |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `batch-20261015-n4` | N4 | `qa/blind_review_n4.json` | `qa/raw_blind_review_n4.json` | `bec76912b721b1a3...` | `HOST_LOG_VERIFIED` | `EXECUTION_PROVENANCE_REPORTED_NOT_ATTESTED` |
| `batch-20261015-n3` | N3 | `qa/blind_review_n3.json` | `qa/raw_blind_review_n3.json` | `1014d71abca05462...` | `HOST_LOG_VERIFIED` | `EXECUTION_PROVENANCE_REPORTED_NOT_ATTESTED` |
| `batch-20261015-n2` | N2 | `qa/blind_review_n2.json` | `qa/raw_blind_review_n2.json` | `98e979716eb04d67...` | `HOST_LOG_VERIFIED` | `EXECUTION_PROVENANCE_REPORTED_NOT_ATTESTED` |
| `batch-20261016-repaired-6` | REPAIRED_6 | `qa/blind_review_repaired_6.json` | `qa/raw_blind_review_repaired_6.json` | `0ca90b7ddec2a903...` | `HOST_LOG_VERIFIED` | `EXECUTION_PROVENANCE_REPORTED_NOT_ATTESTED` |

---

### 4. PHÂN TÁCH TRẠNG THÁI NỘI DUNG VÀ CÂU HỎI DẤU SAO (GATE 2 PENDING)

- **Tổng số câu hỏi được đối soát**: 120
- **Khớp vân tay nội dung (Content Hash Matched)**: 120 / 120 (100.0%)
- **Bản ghi giải mù được lưu trữ (Review Output Recorded)**: 120 / 120 (100.0%)
- **Câu hỏi đã nghiệm thu hoàn chỉnh (`QA_VERIFIED`)**: 104 (Toàn bộ các câu trắc nghiệm từ vựng, ngữ pháp thông thường và đọc hiểu).
- **Câu hỏi dấu sao đang chờ phản biện ngữ nghĩa 24 hoán vị (`STAR_SEMANTIC_REVIEW_PENDING`)**: 16 câu.
- **Chính sách phát hành an toàn (Safe Partial Release)**: Không tự chứng thực 384 hoán vị ngữ nghĩa. Các bộ đề chứa câu hỏi dấu sao được gắn cờ `CONTENT_QA_BLOCKED`. Bộ đề không chứa câu hỏi dấu sao (`MD-N4-VOC-01`) đủ điều kiện phát hành thử nghiệm có kiểm soát.
