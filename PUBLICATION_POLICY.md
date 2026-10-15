# Chính sách bản công khai

Kho GitHub này công khai. Tài liệu học thuật và tài liệu do dự án soạn được giữ để người khác kiểm tra nguồn và cách triển khai. Không cấp thêm quyền đối với nội dung của bên thứ ba. Không có giấy phép mở mới được áp lên toàn bộ kho trong lần đồng bộ này.

- Không có hồ sơ người học thật, bảng điểm cá nhân, lịch làm/ngủ, thông tin đăng ký thi hoặc quyền lợi tài khoản trong bản công khai. Hồ sơ minh họa là ví dụ tổng hợp; các ô tracker nhập tiến độ được để trống. Tên/ngày/giờ trong bài tập là dữ kiện hư cấu của bài học.
- PDF Phase 1, sổ tay PDF Phase 2.1 và PDF bắt đầu Phase 3 bản gốc có hồ sơ riêng: giữ tại máy. Các bản Markdown công khai thay thế hai báo cáo đầu; PDF bắt đầu Phase 3 được dựng lại với hồ sơ tổng hợp. Mọi bản gốc có hash và lý do xử lý trong kiểm kê, không bị ghi đè.
- PDF/MP3 đề mẫu JLPT, HTML nguồn và toàn văn nghiên cứu tải về không được phân phối lại. Dùng liên kết tới nguồn chính thức. Ledger, phương pháp do dự án tổng hợp, danh mục DOI và URL khám phá được công khai; full-text/abstract trích xuất thô giữ local.
- Không có API key, token, `.env`, thư mục dependency, cache, ảnh preview, workbook kiểm thử hoặc file xuất tiến độ trong kho. ZIP phát hành cũ không được thêm; từng tệp quan trọng có đường dẫn riêng.
- QA lịch sử là bằng chứng của checkpoint nguồn; bản công khai có kiểm tra riêng. Chỉ đường dẫn máy/hồ sơ được đổi; payload ngân hàng, mẫu và khóa cuối được giữ byte nguyên để kiểm SHA. Không áp nhãn VERIFIED cho mã build nháp.

[Source inventory](qa/source_inventory.json) dùng đường dẫn tương đối, kích thước và SHA-256 của từng tệp nguồn; không chứa payload bị loại. `LOCAL_ONLY` không có nghĩa tệp mất hoặc bị xóa. Thư mục dependency dạng junction được bỏ qua, không theo liên kết ra runtime.

Tệp lớn nhất của bản công khai được kiểm trong QA; không cần Git LFS ở checkpoint này. Ngưỡng GitHub tham khảo: [tài liệu chính thức](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github). Không dùng ZIP để né giới hạn.
