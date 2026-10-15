# Các lệnh kiểm hỗ trợ

Phase 3.5 dùng [Drive-first](../DRIVE_SETUP/README.md). Chạy `python scripts/drive_first/build_bundle.py` và `node scripts/drive_first/test_drive_first.cjs` để tái tạo payload và kiểm logic/API mô phỏng; xem [DRIVE_FIRST_QA](../DRIVE_FIRST_QA.md) cho nghiệm thu Google còn chờ. Không cần chạy máy chủ web cho hệ thống Drive.

Các lệnh dưới đây giữ cho checkpoint ứng dụng Phase 3 trước đó.

Từ thư mục gốc repo:

```sh
python scripts/validate_release.py
node scripts/tests/test_engine.cjs
```

Engine chỉ cần Node. Kiểm browser cần Playwright và Chromium đã cài ngoài repo; dùng `BROWSER_EXECUTABLE` nếu muốn chỉ định Chrome/Edge có sẵn:

```sh
node scripts/tests/test_browser.cjs
node scripts/tests/test_edge_flows.cjs
```

Test chỉ tạo dữ liệu giả trong context trình duyệt riêng, không đọc lịch sử cá nhân; kết quả/ảnh/exports nằm trong `tmp/test-output/` đã bị Git bỏ qua. `test_preview.cjs` nhận `PREVIEW_URL`; mặc định `http://127.0.0.1:8766/JLPT_PRACTICE/index.html`. Để kiểm HTTP, chạy `python -m http.server 8766 --bind 127.0.0.1 --directory deliverables/phase3` trước.

Sau một checkpoint đã kiểm: `python scripts/update_manifest.py` → validator và test liên quan → cập nhật QA/trạng thái → chạy lại manifest/validator nếu tài liệu đổi → commit/push/fetch theo AGENTS.md. Manifest không chứa hash của chính nó; FILE_INDEX có liệt kê manifest.

`build_start_here.py` dựng lại PDF công khai bằng ReportLab, font Arial/MS Gothic trong Windows, không phải pipeline toàn bộ. [Mã build lịch sử](../archive/source-scripts/README.md) là DRAFT, không chạy lên bản phát hành. Bản final đã có sẵn, người học không cần công cụ tác giả.
