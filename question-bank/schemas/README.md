# Hợp đồng dữ liệu — VERIFIED trong pilot

[question.schema.json](../../deliverables/phase3/JLPT_PRACTICE/question.schema.json) và [DATA_CONTRACT](../../deliverables/phase3/JLPT_PRACTICE/DATA_CONTRACT.md) mô tả ID, kỹ năng, đáp án, nguồn, bằng chứng, trợ giúp và định dạng xuất. Schema là hướng dẫn cấu trúc pilot; validator kiểm các trường và quan hệ thực dùng, không tuyên bố chứng nhận từ thư viện JSON Schema bên ngoài.

Giữ `question_bank.json`, `bank.js`, HTML tự chứa và khóa cùng phiên bản. Sau thay đổi chạy kiểm mapping/engine và kiểm nội dung theo phạm vi; không sửa một bản sao riêng lẻ.
