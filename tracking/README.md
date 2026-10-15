# Theo dõi tiến bộ — bản trống

Hiện hành: [JLPT_PROGRESS_TRACKER.xlsx](../deliverables/phase3/JLPT_PROGRESS_TRACKER.xlsx). Bản này giữ nguyên byte từ workbook pilot đã kiểm Excel native. Không điền dữ liệu cá nhân trước; ngày mẫu/mốc kế hoạch không phải nhật ký học thật.

1. Xuất CSV ở ứng dụng → Sao lưu; JSON mới là bản sao đầy đủ.
2. Mở CSV UTF-8, dấu phẩy; sao chép **12 cột dữ liệu A–L, bỏ tiêu đề**, vào trang **Luyện tập** từ A8.
3. Thay vùng A8:L507 bằng bản xuất mới, hoặc thêm dưới. Cột J là **giây nguyên**, Excel tự đổi phút. Cột M có công thức kiểm; không dán đè. Dòng trùng Session ID + kỹ năng + loại dữ liệu chỉ nhận lần đầu.
4. Giữ tệp đã nhập tiến độ trong thư mục riêng ngoài repo. Kho này chỉ lưu template; không commit CSV/JSON cá nhân.

Các checkpoint khác: [Phase 1](../archive/phase1/Theo_doi_tien_bo_JLPT.xlsx), [Phase 2](../archive/phase2/JLPT_PROGRESS_TRACKER_v2.xlsx), [Phase 2.1](../archive/phase2.1/JLPT_PROGRESS_TRACKER_FINAL.xlsx). Bốn workbook khác nhau về cấu trúc/chức năng; dùng bản hiện hành cho app. Ngưỡng nội bộ không phải chuẩn JLPT.
