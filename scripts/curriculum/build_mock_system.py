# -*- coding: utf-8 -*-
"""
JP-STUDY: BUILD FULL MOCK EXAMS & EXPANDED EXAM CATALOG
Generates:
1. docs/widgets/mock_exam_bank.js
2. updates docs/widgets/practice_engine.html (adds Mock Exam mode)
3. updates docs/widgets/jlpt_exam_catalog.html (6 tabs with 20 N2 mocks, 10 N3 mocks, 6 official workbooks, 7 external providers)
4. generates corresponding _ncr.html files
"""
import json
import os
import re

def to_ncr(text):
    return ''.join(f'&#{ord(c)};' if ord(c) > 127 else c for c in text)

def main():
    print("=== STEP 1: Building Mock Exam Bank & Registry ===")
    
    with open('data/mock_exams/n2_mock_01.json', 'r', encoding='utf-8') as f:
        mock_01 = json.load(f)

    catalog_mocks = {
        'N2': [],
        'N3': []
    }

    # N2 Mocks: 1 READY, 2-20 IN DEVELOPMENT
    catalog_mocks['N2'].append({
        'mockId': 'N2-MOCK-01',
        'title': 'Đề thi thử JLPT N2 Thực chiến — Số 01',
        'level': 'N2',
        'status': 'READY',
        'badgeText': 'READY · ĐÃ KIỂM ĐỊNH',
        'badgeClass': 'status-ready',
        'durationMinutes': 155,
        'totalQuestions': 105,
        'section1Count': 75,
        'section2Count': 30,
        'releaseDate': '18/10/2026',
        'description': 'Đề thi trọn vẹn theo khung năng lực JLPT N2 chính thức. 75 câu Kiến thức ngôn ngữ & Đọc hiểu (105 phút) kèm 5 bài Nghe hiểu Chokai (50 phút).',
        'playable': True
    })

    for i in range(2, 21):
        catalog_mocks['N2'].append({
            'mockId': f'N2-MOCK-{i:02d}',
            'title': f'Đề thi thử JLPT N2 Thực chiến — Số {i:02d}',
            'level': 'N2',
            'status': 'IN_DEVELOPMENT',
            'badgeText': 'IN DEVELOPMENT · ĐANG BIÊN SOẠN',
            'badgeClass': 'status-dev',
            'durationMinutes': 155,
            'totalQuestions': 105,
            'section1Count': 75,
            'section2Count': 30,
            'releaseDate': f'Kỳ thi 12/2026 (Đợt {(i-1)//4 + 1})',
            'description': f'Bộ đề mô phỏng đợt thi số {i:02d}. Đang trong quy trình biên soạn chuẩn hóa ngữ cảnh và kịch bản nghe hiểu.',
            'playable': False
        })

    # N3 Mocks: 1-10 IN DEVELOPMENT
    for i in range(1, 11):
        catalog_mocks['N3'].append({
            'mockId': f'N3-MOCK-{i:02d}',
            'title': f'Đề thi thử JLPT N3 Cốt lõi — Số {i:02d}',
            'level': 'N3',
            'status': 'IN_DEVELOPMENT',
            'badgeText': 'IN DEVELOPMENT · ĐANG BIÊN SOẠN',
            'badgeClass': 'status-dev',
            'durationMinutes': 140,
            'totalQuestions': 95,
            'section1Count': 67,
            'section2Count': 28,
            'releaseDate': 'Kỳ thi 12/2026',
            'description': f'Bộ đề mô phỏng N3 đợt {i:02d}. 30p Từ vựng + 70p Ngữ pháp & Đọc hiểu + 40p Nghe hiểu.',
            'playable': False
        })

    js_mock_bank = f"""/**
 * JP-STUDY — MOCK EXAM BANK & REGISTRY
 * Generated: 2026-10-18
 */
window.JP_MOCK_REGISTRY = {json.dumps(catalog_mocks, ensure_ascii=False, indent=2)};

window.JP_MOCK_DATA = {{
  'N2-MOCK-01': {json.dumps(mock_01, ensure_ascii=False, indent=2)}
}};
"""
    with open('docs/widgets/mock_exam_bank.js', 'w', encoding='utf-8') as f:
        f.write(js_mock_bank)
    print("Saved docs/widgets/mock_exam_bank.js")

    print("=== STEP 2: Building Comprehensive Exam Catalog (jlpt_exam_catalog.html) ===")
    build_exam_catalog()

    print("=== STEP 3: Updating Practice Engine to support Mock Exams ===")
    update_practice_engine()

    print("=== STEP 4: Generating NCR versions ===")
    for filename in ['jlpt_exam_catalog.html', 'practice_engine.html']:
        path = os.path.join('docs/widgets', filename)
        ncr_path = os.path.join('docs/widgets', filename.replace('.html', '_ncr.html'))
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        ncr_content = to_ncr(content)
        with open(ncr_path, 'w', encoding='utf-8') as f:
            f.write(ncr_content)
        print(f"Generated {ncr_path} (len: {len(ncr_content)})")

def build_exam_catalog():
    html = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kho Đề Thi Thử & Tài Liệu JLPT — JP-STUDY</title>
<style>
  :root {
    --primary: #8b0000;
    --primary-light: #fef2f2;
    --n2-color: #1e40af;
    --n3-color: #065f46;
    --n4-color: #6b21a8;
    --bg-light: #f8fafc;
    --card-bg: #ffffff;
    --text-main: #0f172a;
    --text-muted: #64748b;
    --border: #e2e8f0;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    background-color: var(--bg-light);
    color: var(--text-main);
    padding: 16px;
    line-height: 1.5;
  }
  .header {
    text-align: center;
    margin-bottom: 20px;
    padding-bottom: 16px;
    border-bottom: 2px solid #e2e8f0;
  }
  .header h1 {
    font-size: 1.45rem;
    color: var(--primary);
    margin-bottom: 6px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
  }
  .header p {
    font-size: 0.88rem;
    color: var(--text-muted);
  }
  
  /* Top Navigation Tabs */
  .catalog-nav {
    display: flex;
    gap: 6px;
    overflow-x: auto;
    padding-bottom: 8px;
    margin-bottom: 20px;
    border-bottom: 1px solid var(--border);
  }
  .catalog-nav::-webkit-scrollbar { height: 4px; }
  .catalog-nav::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
  .nav-tab {
    padding: 8px 16px;
    font-size: 0.84rem;
    font-weight: 700;
    color: #475569;
    background: #fff;
    border: 1px solid #cbd5e1;
    border-radius: 20px;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.2s;
  }
  .nav-tab:hover {
    color: var(--primary);
    border-color: var(--primary);
  }
  .nav-tab.active {
    background: var(--primary);
    color: #fff;
    border-color: var(--primary);
  }

  /* Notice & Banner Boxes */
  .info-banner {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    color: #fff;
    padding: 16px 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 14px;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.12);
  }
  .info-banner h2 {
    font-size: 1.15rem;
    font-weight: 800;
    margin-bottom: 4px;
  }
  .info-banner p {
    font-size: 0.82rem;
    color: #cbd5e1;
  }
  .btn-banner {
    background: #e11d48;
    color: #fff;
    text-decoration: none;
    padding: 10px 18px;
    border-radius: 8px;
    font-weight: 700;
    font-size: 0.88rem;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 2px 8px rgba(225, 29, 72, 0.3);
    transition: transform 0.15s;
  }
  .btn-banner:hover {
    transform: translateY(-2px);
  }

  /* Grid Layout */
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 16px;
  }
  .card {
    background: var(--card-bg);
    border-radius: 12px;
    border: 1px solid var(--border);
    padding: 18px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.15s, box-shadow 0.15s;
  }
  .card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(0,0,0,0.06);
  }
  .card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
  }
  .badge {
    font-size: 0.72rem;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 6px;
    color: #fff;
    text-transform: uppercase;
  }
  .badge-n2 { background-color: var(--n2-color); }
  .badge-n3 { background-color: var(--n3-color); }
  .badge-n4 { background-color: var(--n4-color); }
  
  .status-badge {
    font-size: 0.7rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 6px;
    text-transform: uppercase;
  }
  .status-ready { background: #dcfce7; color: #166534; border: 1px solid #bbf7d0; }
  .status-dev { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }
  .status-ext { background: #e0f2fe; color: #075985; border: 1px solid #bae6fd; }
  .status-paid { background: #fee2e2; color: #991b1b; border: 1px solid #fecaca; }
  .status-free { background: #f0fdf4; color: #15803d; border: 1px solid #bbf7d0; }

  .card-title {
    font-size: 1.05rem;
    font-weight: 800;
    color: #1e293b;
    margin-bottom: 6px;
  }
  .card-meta {
    font-size: 0.8rem;
    color: #64748b;
    margin-bottom: 12px;
  }
  .card-desc {
    font-size: 0.82rem;
    color: #334155;
    line-height: 1.45;
    margin-bottom: 14px;
    background: #f8fafc;
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #f1f5f9;
  }
  .section-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 14px;
  }
  .sec-tag {
    font-size: 0.72rem;
    background: #f1f5f9;
    color: #475569;
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 600;
  }

  .btn-start {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    width: 100%;
    padding: 10px;
    border-radius: 8px;
    font-size: 0.88rem;
    font-weight: 700;
    text-decoration: none;
    cursor: pointer;
    border: none;
    transition: all 0.15s;
  }
  .btn-ready {
    background: #15803d;
    color: #fff;
    box-shadow: 0 2px 6px rgba(21, 128, 61, 0.25);
  }
  .btn-ready:hover {
    background: #166534;
  }
  .btn-disabled {
    background: #f1f5f9;
    color: #94a3b8;
    border: 1px dashed #cbd5e1;
    cursor: not-allowed;
  }
  .btn-external {
    background: #0284c7;
    color: #fff;
    box-shadow: 0 2px 6px rgba(2, 132, 199, 0.25);
  }
  .btn-external:hover {
    background: #0369a1;
  }

  /* PDF materials button group */
  .btn-group {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 12px;
  }
  .btn-mat {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    color: #1e293b;
    padding: 5px 9px;
    border-radius: 6px;
    font-size: 0.75rem;
    text-decoration: none;
    font-weight: 500;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    transition: background 0.15s;
  }
  .btn-mat:hover {
    background: #e2e8f0;
  }
  .audio-box {
    margin-top: 10px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    padding: 8px 10px;
    border-radius: 8px;
  }
  .audio-label {
    font-size: 0.75rem;
    font-weight: 600;
    color: #475569;
    margin-bottom: 6px;
    display: flex;
    justify-content: space-between;
  }
  audio { width: 100%; height: 32px; }

  /* Tab View containers */
  .view-tab { display: none; }
  .view-tab.active { display: block; }
</style>
</head>
<body>

<div class="header">
  <h1>📚 KHO ĐỀ THI THỬ & TÀI LIỆU LUYỆN THI JLPT</h1>
  <p>Hệ thống 30 đề thi thử mô phỏng N2/N3, Đề chính thức 2012/2018 và Cổng liên kết nguồn đề bên ngoài đã kiểm định</p>
</div>

<!-- TOP NAV TABS -->
<div class="catalog-nav">
  <button type="button" class="nav-tab active" onclick="switchCatalogTab('tab-n2')">🔥 N2: 20 ĐỀ THI THỬ (FULL MOCKS)</button>
  <button type="button" class="nav-tab" onclick="switchCatalogTab('tab-n3')">📗 N3: 10 ĐỀ THI THỬ (FULL MOCKS)</button>
  <button type="button" class="nav-tab" onclick="switchCatalogTab('tab-rand')">🎲 LUYỆN ĐỀ NGẪU NHIÊN</button>
  <button type="button" class="nav-tab" onclick="switchCatalogTab('tab-skill')">🎯 LUYỆN THEO KỸ NĂNG</button>
  <button type="button" class="nav-tab" onclick="switchCatalogTab('tab-official')">📚 ĐỀ CHÍNH THỨC 2012/2018</button>
  <button type="button" class="nav-tab" onclick="switchCatalogTab('tab-ext')">🌐 NGUỒN THI THỬ BÊN NGOÀI</button>
</div>

<!-- ========================================================================= -->
<!-- TAB 1: N2 — 20 ĐỀ THI THỬ (FULL MOCKS) -->
<!-- ========================================================================= -->
<div id="tab-n2" class="view-tab active">
  <div class="info-banner">
    <div>
      <h2>🎯 KẾ HOẠCH N2: 20 ĐỀ THI THỬ TOÀN DIỆN (FULL MOCKS)</h2>
      <p>Mục tiêu kỳ thi 12/2026: 20 đề thi chuẩn cấu trúc JEES (105 câu · 155 phút/đề). Phát hành lũy tiến theo từng đợt kiểm định chất lượng.</p>
    </div>
    <a href="https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mock&mockId=N2-MOCK-01" target="_blank" class="btn-banner">
      🚀 VÀO THI ĐỀ SỐ 01 (105 PHÚT) ▶
    </a>
  </div>

  <div class="grid">
    <!-- N2-MOCK-01 (READY) -->
    <div class="card" style="border: 2px solid #16a34a; box-shadow: 0 4px 12px rgba(22, 163, 74, 0.1);">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">JLPT N2</span>
          <span class="status-badge status-ready">READY · ĐÃ KIỂM ĐỊNH</span>
        </div>
        <div class="card-title">JLPT N2 | Full Mock Exam #01 (Đề thi thử số 01)</div>
        <div class="card-meta">105 câu hỏi · 155 phút (105p Đọc/Hiểu/Ngôn ngữ + 50p Nghe)</div>
        <div class="card-desc">
          Bộ đề trọn vẹn bám sát 100% đặc tả bài thi JLPT N2:
          <br>• <strong>Phần 1 (105 phút):</strong> 75 câu Kiến thức ngôn ngữ (Từ vựng Mondai 1-6, Ngữ pháp Mondai 7-9) và Đọc hiểu (Mondai 10-14).
          <br>• <strong>Phần 2 (50 phút):</strong> 30 câu Nghe hiểu Chokai (Task-based, Point, General, Quick response, Integrated).
        </div>
        <div class="section-tags">
          <span class="sec-tag">📖 Từ vựng (32c)</span>
          <span class="sec-tag">📜 Ngữ pháp (22c)</span>
          <span class="sec-tag">📑 Đọc hiểu (21c)</span>
          <span class="sec-tag">🎧 Nghe hiểu (30c)</span>
        </div>
      </div>
      <a href="https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mock&mockId=N2-MOCK-01" target="_blank" class="btn-start btn-ready">
        🚀 BẮT ĐẦU LÀM BÀI (BẤM GIỜ 105 PHÚT) ▶
      </a>
    </div>

    <!-- N2 MOCKS 02 - 20 (IN DEVELOPMENT) -->
"""
    # Generate cards 02 to 20
    for i in range(2, 21):
        html += f"""    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">JLPT N2</span>
          <span class="status-badge status-dev">IN DEVELOPMENT · ĐANG BIÊN SOẠN</span>
        </div>
        <div class="card-title">JLPT N2 | Full Mock Exam #{i:02d}</div>
        <div class="card-meta">Mục tiêu: 105 câu hỏi · 155 phút · Chuẩn cấu trúc JEES</div>
        <div class="card-desc">
          Bộ đề mô phỏng đợt thi số {i:02d}. Đang trong quy trình rà soát độc lập ngữ liệu đoạn văn và kịch bản audio nhằm tránh lặp câu hỏi và đảm bảo tính tin cậy sư phạm cao nhất.
        </div>
        <div class="section-tags">
          <span class="sec-tag">Từ vựng (32c)</span>
          <span class="sec-tag">Ngữ pháp (22c)</span>
          <span class="sec-tag">Đọc hiểu (21c)</span>
          <span class="sec-tag">Nghe hiểu (30c)</span>
        </div>
      </div>
      <button type="button" class="btn-start btn-disabled" disabled>
        ⏳ Đang chuẩn hóa (Đợt phát hành {(i-1)//4 + 1})
      </button>
    </div>
"""

    html += """  </div>
</div>

<!-- ========================================================================= -->
<!-- TAB 2: N3 — 10 ĐỀ THI THỬ (FULL MOCKS) -->
<!-- ========================================================================= -->
<div id="tab-n3" class="view-tab">
  <div class="info-banner" style="background: linear-gradient(135deg, #064e3b 0%, #022c22 100%);">
    <div>
      <h2>📗 KẾ HOẠCH N3: 10 ĐỀ THI THỬ CỐT LÕI (FULL MOCKS)</h2>
      <p>Củng cố nền tảng 40% cho người học hướng tới N2. Quy chuẩn 95 câu hỏi · 140 phút (30p Từ vựng + 70p Ngữ pháp/Đọc + 40p Nghe).</p>
    </div>
    <a href="https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?level=N3" target="_blank" class="btn-banner" style="background: #059669;">
      ⚡ CÀY 258 CÂU N3 NGAY ▶
    </a>
  </div>

  <div class="grid">
"""
    for i in range(1, 11):
        html += f"""    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n3">JLPT N3</span>
          <span class="status-badge status-dev">IN DEVELOPMENT · ĐANG BIÊN SOẠN</span>
        </div>
        <div class="card-title">JLPT N3 | Full Mock Exam #{i:02d}</div>
        <div class="card-meta">Mục tiêu: 95 câu hỏi · 140 phút · Chuẩn cấu trúc JEES</div>
        <div class="card-desc">
          Bộ đề thi thử N3 đợt {i:02d}. Phân bổ 35 câu Kiến thức từ vựng, 39 câu Ngữ pháp/Đọc hiểu và 28 câu Nghe hiểu Chokai. Hiện đang chuẩn hóa ngữ cảnh và đối chiếu bản dịch tiếng Việt.
        </div>
        <div class="section-tags">
          <span class="sec-tag">Từ vựng (35c)</span>
          <span class="sec-tag">Ngữ pháp/Đọc (39c)</span>
          <span class="sec-tag">Nghe hiểu (28c)</span>
        </div>
      </div>
      <button type="button" class="btn-start btn-disabled" disabled>
        ⏳ Đang chuẩn hóa (Kỳ thi 12/2026)
      </button>
    </div>
"""

    html += """  </div>
</div>

<!-- ========================================================================= -->
<!-- TAB 3: LUYỆN ĐỀ NGẪU NHIÊN -->
<!-- ========================================================================= -->
<div id="tab-rand" class="view-tab">
  <div class="grid">
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">N2 / N3 / N4</span>
          <span class="status-badge status-ready">720 CÂU HOẠT ĐỘNG</span>
        </div>
        <div class="card-title">🔥 Cỗ Máy Luyện Đề Vô Tận (Chế độ Cày liên tục)</div>
        <div class="card-meta">Phản hồi tức thì · Giải thích chi tiết & Phân tích đáp án sai</div>
        <div class="card-desc">
          Tùy chọn số lượng 10 đến 100 câu hỏi, ưu tiên câu hỏi mới chưa từng làm (tuyệt đối không trùng lặp), làm đến đâu biết điểm và đọc giải thích ngay đến đó.
        </div>
      </div>
      <a href="https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mode-a" target="_blank" class="btn-start btn-ready">
        ⚡ BẮT ĐẦU CÀY CÂU HỎI ▶
      </a>
    </div>

    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">TIMED DRILL</span>
          <span class="status-badge status-ready">15P · 30P · 60P</span>
        </div>
        <div class="card-title">⏱️ Phòng Luyện Tập Tính Giờ (Áp Lực Phòng Thi)</div>
        <div class="card-meta">Đồng hồ đếm ngược · Bảng câu hỏi Palette · Chấm điểm sau khi nộp</div>
        <div class="card-desc">
          Mô phỏng áp lực thời gian của kỳ thi thật. Không hiển thị đáp án trong lúc làm bài, tự động nộp bài khi hết giờ và cung cấp bảng tổng kết phân tích chi tiết.
        </div>
      </div>
      <a href="https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mode-d" target="_blank" class="btn-start btn-ready">
        ⏱️ VÀO PHÒNG TÍNH GIỜ ▶
      </a>
    </div>

    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">SEEDED TEST</span>
          <span class="status-badge status-ready">TÁI TẠO 100%</span>
        </div>
        <div class="card-title">🎲 Đề Thi Ngẫu Nhiên Có Mã Số (Seeded Test)</div>
        <div class="card-meta">Cùng mã số = cùng đề thi · Dễ dàng thi đấu nhóm bạn</div>
        <div class="card-desc">
          Sinh đề thi ngẫu nhiên nhưng cố định câu hỏi theo mã Seed. Cho phép chia sẻ mã đề cho bạn học để cùng làm một đề và so sánh kết quả minh bạch.
        </div>
      </div>
      <a href="https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mode-c" target="_blank" class="btn-start btn-ready">
        🎲 TẠO ĐỀ CÓ MÃ SEED ▶
      </a>
    </div>

    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">SPACED REPETITION</span>
          <span class="status-badge status-ready">SỔ TAY CÂU SAI</span>
        </div>
        <div class="card-title">📝 Sổ Tay Ôn Câu Sai & Spaced Repetition</div>
        <div class="card-meta">Ghi nhớ tự động · Lặp lại ngắt quãng 1 - 3 - 7 ngày</div>
        <div class="card-desc">
          Tự động thu thập mọi câu hỏi bạn từng trả lời sai trong tất cả các phiên làm bài. Luyện tập lại cho đến khi thành thạo (đúng liên tiếp ≥ 2 lần).
        </div>
      </div>
      <a href="https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mode-e" target="_blank" class="btn-start btn-ready">
        📝 MỞ SỔ TAY CÂU SAI ▶
      </a>
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- TAB 4: LUYỆN THEO KỸ NĂNG -->
<!-- ========================================================================= -->
<div id="tab-skill" class="view-tab">
  <div class="grid">
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">VOCABULARY</span>
          <span class="status-badge status-ready">470 CÂU N2/N3</span>
        </div>
        <div class="card-title">📖 Chữ Hán & Từ Vựng (Mondai 1 - 6)</div>
        <div class="card-meta">Kanji đọc, Kanji viết, Tạo từ, Ngữ cảnh, Đồng nghĩa, Cách dùng từ</div>
        <div class="card-desc">
          Bộ câu hỏi trắc nghiệm rèn luyện toàn diện 6 dạng thức thi Từ vựng của N2 và 5 dạng thức của N3. Kèm âm Hán Việt và phân tích từ gây nhiễu.
        </div>
      </div>
      <a href="https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mode-b" target="_blank" class="btn-start btn-ready">
        🎯 LUYỆN TỪ VỰNG & KANJI ▶
      </a>
    </div>

    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">GRAMMAR</span>
          <span class="status-badge status-ready">158 CÂU N2/N3</span>
        </div>
        <div class="card-title">📜 Ngữ Pháp Câu & Ngữ Pháp Đoạn Văn (Mondai 7 - 9)</div>
        <div class="card-meta">Mẫu câu, Ngữ cảnh hội thoại và Điền liên từ trong văn bản</div>
        <div class="card-desc">
          Chuyên đề rèn luyện các mẫu ngữ pháp trung cấp N2/N3, phó từ nối, liên từ chỉ thị và mạch suy luận logic trong đoạn văn.
        </div>
      </div>
      <a href="https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mode-b" target="_blank" class="btn-start btn-ready">
        🎯 LUYỆN NGỮ PHÁP ▶
      </a>
    </div>

    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">STAR ★</span>
          <span class="status-badge status-ready">45 CÂU N2/N3</span>
        </div>
        <div class="card-title">★ Kỹ Thuật Xếp Câu Sao (Mondai 8)</div>
        <div class="card-meta">Khóa cặp ngữ pháp · Ghép cụm trước sau · Bắt vị trí ngôi sao</div>
        <div class="card-desc">
          Dạng bài học viên thường e ngại nhất trong JLPT. Cung cấp phương pháp khóa các khối từ cố định để tìm ra đáp án chính xác trong dưới 60 giây.
        </div>
      </div>
      <a href="https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mode-b" target="_blank" class="btn-start btn-ready">
        🎯 LUYỆN XẾP CÂU SAO ▶
      </a>
    </div>

    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">READING</span>
          <span class="status-badge status-ready">52 BÀI ĐỌC N2/N3</span>
        </div>
        <div class="card-title">📑 Đọc Hiểu Thực Chiến (Mondai 10 - 14)</div>
        <div class="card-meta">Đoản văn, Trung văn, So sánh A/B, Trường văn, Tra cứu thông tin</div>
        <div class="card-desc">
          Hệ thống bài đọc thực thụ kèm câu hỏi tư duy phản biện. Rèn kỹ năng đọc quét từ khóa, xác định luận điểm chính và lọc bảng biểu thông báo.
        </div>
      </div>
      <a href="https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mode-b" target="_blank" class="btn-start btn-ready">
        🎯 LUYỆN ĐỌC HIỂU ▶
      </a>
    </div>

    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">LISTENING</span>
          <span class="status-badge status-ready">AUDIO CHUẨN 100%</span>
        </div>
        <div class="card-title">🎧 Phòng Luyện Nghe Trực Tuyến (5 Mondai)</div>
        <div class="card-meta">Trình phát audio chất lượng cao từ Japan Foundation & JEES</div>
        <div class="card-desc">
          Kho bài nghe chia rõ theo 5 dạng đề thi thật: Task-based, Point comprehension, General outline, Quick response và Integrated comprehension.
        </div>
      </div>
      <a href="https://sites.google.com/view/jp-study/ph%C3%B2ng-luy%E1%BB%87n-nghe" target="_blank" class="btn-start btn-external">
        🎧 VÀO PHÒNG LUYỆN NGHE ▶
      </a>
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- TAB 5: ĐỀ CHÍNH THỨC 2012 / 2018 (OFFICIAL WORKBOOKS) -->
<!-- ========================================================================= -->
<div id="tab-official" class="view-tab">
  <div style="background: #fffbeb; border: 1px solid #fef3c7; border-radius: 8px; padding: 14px; margin-bottom: 20px; font-size: 0.82rem; color: #92400e; line-height: 1.5;">
    📌 <strong>Tài liệu lưu trữ chính thức:</strong> Các bộ tài liệu dưới đây là Official Practice Workbooks do Hiệp hội Hỗ trợ Giáo dục Quốc tế Nhật Bản (JEES) và The Japan Foundation phát hành (Vol. 1 năm 2012, Vol. 2 năm 2018). Mỗi bộ chứa đề thi mẫu tương đương một đề thi thật, kèm đáp án, script nghe và audio MP3 nguyên gốc.
  </div>

  <div class="grid">
    <!-- N2 2018 -->
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">JLPT N2</span>
          <span class="status-badge status-free">OFFICIAL 2018</span>
        </div>
        <div class="card-title">JLPT N2 | Official Practice Workbook Vol. 2 (2018)</div>
        <div class="card-meta">105 câu hỏi · ~155 phút · Nguồn: Japan Foundation & JEES</div>
        
        <div style="font-size:0.75rem; font-weight:700; color:#475569; text-transform:uppercase; margin-bottom:6px;">Tài liệu PDF đề thi:</div>
        <div class="btn-group">
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N2V.pdf" target="_blank">📖 Từ vựng</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N2G.pdf" target="_blank">📜 Ngữ pháp</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N2R.pdf" target="_blank">📑 Đọc hiểu</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N2L.pdf" target="_blank">🎧 Đề nghe</a>
        </div>
        <div style="font-size:0.75rem; font-weight:700; color:#475569; text-transform:uppercase; margin-bottom:6px;">Đáp án & Kịch bản nghe:</div>
        <div class="btn-group">
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N2sheet.pdf" target="_blank">📝 Phiếu trả lời</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N2answer.pdf" target="_blank">✅ Đáp án</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N2script.pdf" target="_blank">💬 Script nghe</a>
        </div>
      </div>
      <div class="audio-box">
        <div class="audio-label">
          <span>🎧 Nghe thử Mondai 1 (Task-based):</span>
          <a href="https://www.jlpt.jp/e/samples/sampleindex.html" target="_blank" style="color:#2980b9; font-size:0.7rem; text-decoration:none;">Xem tại nguồn</a>
        </div>
        <audio controls preload="none">
          <source src="https://www.jlpt.jp/samples/sample2018/mp3/N2Q1.mp3" type="audio/mpeg">
        </audio>
      </div>
    </div>

    <!-- N2 2012 -->
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n2">JLPT N2</span>
          <span class="status-badge status-free">OFFICIAL 2012</span>
        </div>
        <div class="card-title">JLPT N2 | Official Practice Workbook Vol. 1 (2012)</div>
        <div class="card-meta">105 câu hỏi · ~155 phút · Nguồn: Japan Foundation & JEES</div>
        
        <div style="font-size:0.75rem; font-weight:700; color:#475569; text-transform:uppercase; margin-bottom:6px;">Tài liệu PDF đề thi:</div>
        <div class="btn-group">
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N2V.pdf" target="_blank">📖 Từ vựng</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N2G.pdf" target="_blank">📜 Ngữ pháp</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N2R.pdf" target="_blank">📑 Đọc hiểu</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N2L.pdf" target="_blank">🎧 Đề nghe</a>
        </div>
        <div style="font-size:0.75rem; font-weight:700; color:#475569; text-transform:uppercase; margin-bottom:6px;">Đáp án & Kịch bản nghe:</div>
        <div class="btn-group">
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N2sheet.pdf" target="_blank">📝 Phiếu trả lời</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N2answer.pdf" target="_blank">✅ Đáp án</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N2script.pdf" target="_blank">💬 Script nghe</a>
        </div>
      </div>
      <div class="audio-box">
        <div class="audio-label">
          <span>🎧 Nghe thử Mondai 1 (Task-based):</span>
          <a href="https://www.jlpt.jp/e/samples/sampleindex.html" target="_blank" style="color:#2980b9; font-size:0.7rem; text-decoration:none;">Xem tại nguồn</a>
        </div>
        <audio controls preload="none">
          <source src="https://www.jlpt.jp/samples/sample2012/mp3/N2Q1.mp3" type="audio/mpeg">
        </audio>
      </div>
    </div>

    <!-- N3 2018 -->
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n3">JLPT N3</span>
          <span class="status-badge status-free">OFFICIAL 2018</span>
        </div>
        <div class="card-title">JLPT N3 | Official Practice Workbook Vol. 2 (2018)</div>
        <div class="card-meta">95 câu hỏi · ~140 phút · Nguồn: Japan Foundation & JEES</div>
        
        <div style="font-size:0.75rem; font-weight:700; color:#475569; text-transform:uppercase; margin-bottom:6px;">Tài liệu PDF đề thi:</div>
        <div class="btn-group">
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N3V.pdf" target="_blank">📖 Từ vựng</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N3G.pdf" target="_blank">📜 Ngữ pháp</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N3R.pdf" target="_blank">📑 Đọc hiểu</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N3L.pdf" target="_blank">🎧 Đề nghe</a>
        </div>
        <div style="font-size:0.75rem; font-weight:700; color:#475569; text-transform:uppercase; margin-bottom:6px;">Đáp án & Kịch bản nghe:</div>
        <div class="btn-group">
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N3script.pdf" target="_blank">💬 Script nghe</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N3answer.pdf" target="_blank">✅ Đáp án</a>
        </div>
      </div>
      <div class="audio-box">
        <div class="audio-label">
          <span>🎧 Nghe thử Mondai 1 (Task-based):</span>
          <a href="https://www.jlpt.jp/e/samples/sampleindex.html" target="_blank" style="color:#065f46; font-size:0.7rem; text-decoration:none;">Xem tại nguồn</a>
        </div>
        <audio controls preload="none">
          <source src="https://www.jlpt.jp/samples/sample2018/mp3/N3Q1.mp3" type="audio/mpeg">
        </audio>
      </div>
    </div>

    <!-- N3 2012 -->
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n3">JLPT N3</span>
          <span class="status-badge status-free">OFFICIAL 2012</span>
        </div>
        <div class="card-title">JLPT N3 | Official Practice Workbook Vol. 1 (2012)</div>
        <div class="card-meta">95 câu hỏi · ~140 phút · Nguồn: Japan Foundation & JEES</div>
        
        <div style="font-size:0.75rem; font-weight:700; color:#475569; text-transform:uppercase; margin-bottom:6px;">Tài liệu PDF đề thi:</div>
        <div class="btn-group">
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N3V.pdf" target="_blank">📖 Từ vựng</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N3G.pdf" target="_blank">📜 Ngữ pháp</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N3R.pdf" target="_blank">📑 Đọc hiểu</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N3L.pdf" target="_blank">🎧 Đề nghe</a>
        </div>
        <div style="font-size:0.75rem; font-weight:700; color:#475569; text-transform:uppercase; margin-bottom:6px;">Đáp án & Kịch bản nghe:</div>
        <div class="btn-group">
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N3script.pdf" target="_blank">💬 Script nghe</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N3answer.pdf" target="_blank">✅ Đáp án</a>
        </div>
      </div>
      <div class="audio-box">
        <div class="audio-label">
          <span>🎧 Nghe thử Mondai 1 (Task-based):</span>
          <a href="https://www.jlpt.jp/e/samples/sampleindex.html" target="_blank" style="color:#065f46; font-size:0.7rem; text-decoration:none;">Xem tại nguồn</a>
        </div>
        <audio controls preload="none">
          <source src="https://www.jlpt.jp/samples/sample2012/mp3/N3Q1.mp3" type="audio/mpeg">
        </audio>
      </div>
    </div>

    <!-- N4 2018 & 2012 -->
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n4">JLPT N4</span>
          <span class="status-badge status-free">OFFICIAL 2018</span>
        </div>
        <div class="card-title">JLPT N4 | Official Practice Workbook Vol. 2 (2018)</div>
        <div class="card-meta">85 câu hỏi · ~125 phút · Nguồn: Japan Foundation & JEES</div>
        <div class="btn-group">
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N4V.pdf" target="_blank">📖 Từ vựng</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N4G.pdf" target="_blank">📜 Ngữ pháp</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N4R.pdf" target="_blank">📑 Đọc hiểu</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2018/pdf/N4L.pdf" target="_blank">🎧 Đề nghe</a>
        </div>
      </div>
      <div class="audio-box">
        <audio controls preload="none">
          <source src="https://www.jlpt.jp/samples/sample2018/mp3/N4Q1.mp3" type="audio/mpeg">
        </audio>
      </div>
    </div>

    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge badge-n4">JLPT N4</span>
          <span class="status-badge status-free">OFFICIAL 2012</span>
        </div>
        <div class="card-title">JLPT N4 | Official Practice Workbook Vol. 1 (2012)</div>
        <div class="card-meta">85 câu hỏi · ~125 phút · Nguồn: Japan Foundation & JEES</div>
        <div class="btn-group">
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N4V.pdf" target="_blank">📖 Từ vựng</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N4G.pdf" target="_blank">📜 Ngữ pháp</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N4R.pdf" target="_blank">📑 Đọc hiểu</a>
          <a class="btn-mat" href="https://www.jlpt.jp/samples/sample2012/pdf/N4L.pdf" target="_blank">🎧 Đề nghe</a>
        </div>
      </div>
      <div class="audio-box">
        <audio controls preload="none">
          <source src="https://www.jlpt.jp/samples/sample2012/mp3/N4Q1.mp3" type="audio/mpeg">
        </audio>
      </div>
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- TAB 6: NGUỒN THI THỬ BÊN NGOÀI (VERIFIED EXTERNAL PROVIDERS) -->
<!-- ========================================================================= -->
<div id="tab-ext" class="view-tab">
  <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px; margin-bottom: 20px; font-size: 0.82rem; color: #1e40af; line-height: 1.5;">
    🌐 <strong>Cổng liên kết nguồn thi thử độc lập đã kiểm chứng:</strong> Các nền tảng dưới đây được rà soát và xác minh tính pháp lý nhằm giúp học viên mở rộng cơ hội cọ xát đề thi thử. JP-STUDY không sao chép lại nội dung độc quyền, xin vui lòng truy cập trực tiếp website gốc của từng đơn vị.
  </div>

  <div class="grid">
    <!-- Provider 1: Japan Foundation Official -->
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge" style="background:#0f172a;">JLPT OFFICIAL</span>
          <span class="status-badge status-free">100% MIỄN PHÍ</span>
        </div>
        <div class="card-title">The Japan Foundation & JEES (Trang chủ JLPT)</div>
        <div class="card-meta">Cấp độ: N1, N2, N3, N4, N5 · Đơn vị: Cơ quan tổ chức kỳ thi JLPT</div>
        <div class="card-desc">
          • <strong>Quy mô:</strong> 2 bộ đề thi đầy đủ/mỗi cấp độ + Bộ câu hỏi mẫu trực tuyến.<br>
          • <strong>Phân loại:</strong> Full Practice Workbook (Chuẩn hóa 100%).<br>
          • <strong>Âm thanh:</strong> File MP3 gốc + Kịch bản hội thoại chuẩn.<br>
          • <strong>Chi phí:</strong> Miễn phí toàn bộ, không cần đăng ký tài khoản.
        </div>
      </div>
      <a href="https://www.jlpt.jp/e/samples/sampleindex.html" target="_blank" rel="noopener noreferrer" class="btn-start btn-external">
        🌐 Mở Website Chính Thức (jlpt.jp) ↗
      </a>
    </div>

    <!-- Provider 2: Migii JLPT -->
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge" style="background:#2563eb;">MIGII JLPT</span>
          <span class="status-badge status-paid">FREEMIUM (CÓ TRẢ PHÍ)</span>
        </div>
        <div class="card-title">Migii JLPT (Web & Ứng dụng Di động)</div>
        <div class="card-meta">Cấp độ: N5 đến N1 · Đơn vị: Migii Team</div>
        <div class="card-desc">
          • <strong>Quy mô:</strong> ~10–15 đề thi thử mô phỏng/cấp độ + Ngân hàng câu hỏi theo dạng.<br>
          • <strong>Phân loại:</strong> Full Mock Test, Mini-Test & Luyện từng Mondai.<br>
          • <strong>Âm thanh:</strong> Đầy đủ audio nghe hiểu và kịch bản dịch nghĩa.<br>
          • <strong>Chi phí:</strong> Làm thử miễn phí 1–2 đề/mini-test; mở khóa toàn bộ kho đề yêu cầu gói Premium.
        </div>
      </div>
      <a href="https://migii.net/en/jlpt" target="_blank" rel="noopener noreferrer" class="btn-start btn-external">
        🌐 Mở Nền Tảng Migii JLPT ↗
      </a>
    </div>

    <!-- Provider 3: TodayJLPT -->
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge" style="background:#d97706;">TODAYJLPT</span>
          <span class="status-badge status-ext">CẦN ĐĂNG NHẬP</span>
        </div>
        <div class="card-title">TodayJLPT (Thi Thử & Chẩn Đoán Trình Độ)</div>
        <div class="card-meta">Cấp độ: N5 đến N1 · Đơn vị: TodayJLPT Platform</div>
        <div class="card-desc">
          • <strong>Quy mô:</strong> Hệ thống bài thi thử trực tuyến & kiểm tra phân loại nhanh.<br>
          • <strong>Phân loại:</strong> Full Mock & Chẩn đoán điểm yếu.<br>
          • <strong>Âm thanh:</strong> Tích hợp âm thanh nghe hiểu trực tiếp trên web.<br>
          • <strong>Chi phí:</strong> Cần tạo tài khoản; miễn phí các tính năng cốt lõi và có gói tài khoản nâng cao.
        </div>
      </div>
      <a href="https://todayjlpt.com" target="_blank" rel="noopener noreferrer" class="btn-start btn-external">
        🌐 Mở Website TodayJLPT ↗
      </a>
    </div>

    <!-- Provider 4: VNJPCLUB -->
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge" style="background:#dc2626;">VNJPCLUB</span>
          <span class="status-badge status-free">MIỄN PHÍ WEB</span>
        </div>
        <div class="card-title">VNJPCLUB (Cộng Đồng Tiếng Nhật Việt Nam)</div>
        <div class="card-meta">Cấp độ: N5 đến N1 · Đơn vị: VNJPCLUB Community</div>
        <div class="card-desc">
          • <strong>Quy mô:</strong> Kho đề thi phong phú mô phỏng các kỳ thi qua các năm.<br>
          • <strong>Phân loại:</strong> Full Mock (Đủ 3 phần: Kiến thức chữ Hán/Ngữ pháp, Đọc hiểu, Nghe hiểu).<br>
          • <strong>Âm thanh:</strong> Tích hợp sẵn audio nghe trên trình duyệt.<br>
          • <strong>Chi phí:</strong> Miễn phí trực tuyến, có tính giờ và chấm điểm tự động.
        </div>
      </div>
      <a href="https://vnjpclub.com" target="_blank" rel="noopener noreferrer" class="btn-start btn-external">
        🌐 Mở Website VNJPCLUB ↗
      </a>
    </div>

    <!-- Provider 5: Dungmori -->
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge" style="background:#7c3aed;">DUNGMORI</span>
          <span class="status-badge status-ext">THI ĐỊNH KỲ / CÓ PHÍ</span>
        </div>
        <div class="card-title">Dungmori (Phòng Thi Ảo Mô Phỏng Đếm Ngược)</div>
        <div class="card-meta">Cấp độ: N5 đến N1 · Đơn vị: Dũng Mori Nhật Ngữ</div>
        <div class="card-desc">
          • <strong>Quy mô:</strong> Các đợt thi thử trực tuyến định kỳ trước mỗi kỳ thi tháng 7 & 12.<br>
          • <strong>Phân loại:</strong> Full Mock Exam (Mô phỏng áp lực phòng thi, có bảng xếp hạng toàn quốc).<br>
          • <strong>Âm thanh:</strong> Hệ thống phòng thi nghe bấm giờ chuẩn 50 phút.<br>
          • <strong>Chi phí:</strong> Tổ chức miễn phí theo đợt công bố; kho đề chi tiết đi kèm khóa học.
        </div>
      </div>
      <a href="https://dungmori.com" target="_blank" rel="noopener noreferrer" class="btn-start btn-external">
        🌐 Mở Website Dungmori ↗
      </a>
    </div>

    <!-- Provider 6: Mazii / Try JLPT -->
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge" style="background:#ea580c;">MAZII</span>
          <span class="status-badge status-paid">FREEMIUM</span>
        </div>
        <div class="card-title">Mazii Japanese (Công Cụ Luyện Đề & Từ Điển)</div>
        <div class="card-meta">Cấp độ: N5 đến N1 · Đơn vị: Mazii Platform</div>
        <div class="card-desc">
          • <strong>Quy mô:</strong> Ngân hàng câu hỏi trắc nghiệm chia theo từng dạng Mondai.<br>
          • <strong>Phân loại:</strong> Mini-Test & Luyện chuyên sâu từng kỹ năng.<br>
          • <strong>Âm thanh:</strong> Có hỗ trợ phát âm và luyện nghe một số dạng đề.<br>
          • <strong>Chi phí:</strong> Miễn phí tính năng cơ bản, gói tài khoản trả phí mở rộng kho bài tập.
        </div>
      </div>
      <a href="https://mazii.net" target="_blank" rel="noopener noreferrer" class="btn-start btn-external">
        🌐 Mở Nền Tảng Mazii ↗
      </a>
    </div>

    <!-- Provider 7: Minna no Nihongo Hub -->
    <div class="card">
      <div>
        <div class="card-top">
          <span class="badge" style="background:#059669;">MINNA NIHONGO</span>
          <span class="status-badge status-free">MIỄN PHÍ CĂN BẢN</span>
        </div>
        <div class="card-title">Minna no Nihongo Online Hub</div>
        <div class="card-meta">Cấp độ: N5, N4 · Đơn vị: Cộng đồng học tập giáo trình Minna</div>
        <div class="card-desc">
          • <strong>Quy mô:</strong> 50 bài học nền tảng từ vựng và mẫu ngữ pháp sơ cấp.<br>
          • <strong>Phân loại:</strong> Bổ trợ củng cố kiến thức ngữ pháp/từ vựng căn bản (Bài 1–50).<br>
          • <strong>Âm thanh:</strong> File nghe hội thoại và bài tập điền từ theo giáo trình.<br>
          • <strong>Chi phí:</strong> Miễn phí trực tuyến.
        </div>
      </div>
      <a href="https://minnanonihongo.com" target="_blank" rel="noopener noreferrer" class="btn-start btn-external">
        🌐 Mở Minna no Nihongo Hub ↗
      </a>
    </div>
  </div>
</div>

<script>
function switchCatalogTab(tabId) {
  document.querySelectorAll('.nav-tab').forEach(btn => btn.classList.remove('active'));
  document.querySelectorAll('.view-tab').forEach(tab => tab.classList.remove('active'));
  
  const targetTab = document.getElementById(tabId);
  if (targetTab) {
    targetTab.classList.add('active');
  }
  
  const tabButtons = {
    'tab-n2': 0,
    'tab-n3': 1,
    'tab-rand': 2,
    'tab-skill': 3,
    'tab-official': 4,
    'tab-ext': 5
  };
  const btnIdx = tabButtons[tabId];
  if (btnIdx !== undefined) {
    document.querySelectorAll('.nav-tab')[btnIdx].classList.add('active');
  }
}

// Auto select tab from URL parameter if present
(function() {
  try {
    const params = new URLSearchParams(window.location.search);
    const tab = params.get('tab');
    if (tab && document.getElementById(tab)) {
      switchCatalogTab(tab);
    }
  } catch(e) {}
})();
</script>

</body>
</html>
"""
    with open('docs/widgets/jlpt_exam_catalog.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Saved docs/widgets/jlpt_exam_catalog.html")

def update_practice_engine():
    path = 'docs/widgets/practice_engine.html'
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Add mock_exam_bank.js script tag if not present
    if 'mock_exam_bank.js' not in code:
        code = code.replace('<script src="practice_bank.js"></script>', '<script src="practice_bank.js"></script>\n<script src="mock_exam_bank.js"></script>')

    # 2. Add mock tab in engine navigation
    if 'switchMode(\'mode-mock\')' not in code:
        mock_tab = '<div class="nav-tab" onclick="switchMode(\'mode-mock\')">🏛️ Thi thử N2 (Mock 01)</div>'
        code = code.replace('<div class="nav-tab" onclick="switchMode(\'mode-f\')">📊 Nhật ký học tập</div>', '<div class="nav-tab" onclick="switchMode(\'mode-f\')">📊 Nhật ký học tập</div>\n    ' + mock_tab)

    # 3. Add mode-mock view panel before mode-f if not present
    if 'id="mode-mock"' not in code:
        mock_panel = """
  <!-- MODE MOCK: ĐỀ THI THỬ TOÀN DIỆN (FULL MOCK EXAM) -->
  <div id="mode-mock" class="view-panel">
    <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: white; padding: 20px; border-radius: 12px; margin-bottom: 24px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:8px;">
        <span style="font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.5px; background:rgba(255,255,255,0.2); padding:2px 8px; border-radius:4px;">🏛️ KỲ THI THỬ CHUẨN HOÁ</span>
        <span class="status-badge status-ready" style="font-size:0.75rem;">READY · CHÍNH THỨC MỞ</span>
      </div>
      <h2 style="font-size:1.35rem; font-weight:800; margin-bottom:6px;">ĐỀ THI THỬ JLPT N2 THỰC CHIẾN — SỐ 01</h2>
      <p style="font-size:0.88rem; color:#cbd5e1; line-height:1.5;">Đề thi trọn vẹn mô phỏng chuẩn xác cấu trúc và thời lượng kỳ thi N2 (Tháng 12/2026). Gồm 75 câu hỏi Phần 1 (105 phút) và 30 câu hỏi Phần 2 Nghe hiểu (50 phút).</p>
    </div>

    <div class="config-grid" style="margin-bottom:20px;">
      <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:16px;">
        <div style="font-size:0.8rem; font-weight:700; color:#475569; text-transform:uppercase; margin-bottom:4px;">Phần 1: Kiến thức & Đọc hiểu</div>
        <div style="font-size:1.15rem; font-weight:800; color:#1e40af;">75 Câu hỏi · 105 Phút</div>
        <p style="font-size:0.8rem; color:#64748b; margin-top:6px;">Mondai 1-6 (Từ vựng: 32c) · Mondai 7-9 (Ngữ pháp: 22c) · Mondai 10-14 (Đọc hiểu: 21c).</p>
      </div>
      <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:16px;">
        <div style="font-size:0.8rem; font-weight:700; color:#475569; text-transform:uppercase; margin-bottom:4px;">Phần 2: Nghe hiểu (Chokai)</div>
        <div style="font-size:1.15rem; font-weight:800; color:#065f46;">30 Câu hỏi · 50 Phút</div>
        <p style="font-size:0.8rem; color:#64748b; margin-top:6px;">Mondai 1-5 Chokai tích hợp phòng nghe audio chất lượng cao từ Japan Foundation & JEES.</p>
      </div>
    </div>

    <div style="background:#fffbeb; border:1px solid #fef3c7; border-radius:8px; padding:14px; margin-bottom:24px; font-size:0.85rem; color:#92400e; line-height:1.5;">
      ⚠️ <strong>Quy chế thi thử:</strong><br>
      1. Thời gian đếm ngược chính xác <strong>105 phút</strong> cho Phần 1. Không hiển thị đáp án khi làm.<br>
      2. Sử dụng <strong>Bảng câu hỏi Palette (1–75)</strong> để chuyển nhanh giữa các câu hoặc kiểm tra lại câu chưa chọn.<br>
      3. Sau khi nộp bài: Hệ thống chấm điểm thô, phân tích tỷ lệ chính xác theo từng kỹ năng và mở toàn bộ giải thích chi tiết.<br>
      4. Nút chuyển tiếp sẽ hướng dẫn bạn hoàn thành nốt Phần 2 (Nghe hiểu) tại Phòng luyện nghe.
    </div>

    <button type="button" class="btn-primary" style="padding:14px 28px; font-size:1.05rem;" onclick="startFullMockExam('N2-MOCK-01')">
      🚀 BẮT ĐẦU THI THỬ ĐỀ SỐ 01 (105 PHÚT) ▶
    </button>
  </div>
"""
        code = code.replace('<!-- MODE F: NHẬT KÝ & LỊCH SỬ HỌC TẬP (PERSISTENCE) -->', mock_panel + '\n  <!-- MODE F: NHẬT KÝ & LỊCH SỬ HỌC TẬP (PERSISTENCE) -->')

    # 4. Add mock logic into javascript in practice_engine.html
    if 'function startFullMockExam' not in code:
        mock_js = """
// =========================================================================
// FULL MOCK EXAM MODE HANDLER
// =========================================================================
function startFullMockExam(mockId) {
  mockId = mockId || 'N2-MOCK-01';
  const mockData = (window.JP_MOCK_DATA && window.JP_MOCK_DATA[mockId]) ? window.JP_MOCK_DATA[mockId] : null;

  if (!mockData || !mockData.sections || !mockData.sections[0] || !mockData.sections[0].items) {
    alert('Không tìm thấy dữ liệu đề thi thử: ' + mockId);
    return;
  }

  const items = mockData.sections[0].items;
  const durMin = mockData.sections[0].durationMinutes || 105;

  timedState = {
    questions: items,
    currentIndex: 0,
    userAnswers: {},
    totalSec: durMin * 60,
    remainSec: durMin * 60,
    startTime: Date.now(),
    timerInterval: null,
    mockMeta: {
      isMock: true,
      mockId: mockId,
      mockTitle: mockData.title,
      level: mockData.level || 'N2'
    }
  };

  switchMode('mode-d');
  document.getElementById('d-config').style.display = 'none';
  document.getElementById('d-summary').style.display = 'none';
  document.getElementById('d-arena').style.display = 'block';

  renderTimedPalette();
  renderTimedQuestion();
  startTimedTimer();
}
window.startFullMockExam = startFullMockExam;
"""
        code = code.replace('// =========================================================================\n// MODE D: LUYỆN TẬP TÍNH GIỜ (TIMED PRACTICE)', mock_js + '\n// =========================================================================\n// MODE D: LUYỆN TẬP TÍNH GIỜ (TIMED PRACTICE)')

    # 5. Handle mock query params in DOMContentLoaded
    if "const qMock = params.get('mock') || params.get('mockId');" not in code:
        param_handler = """    const qMock = params.get('mock') || params.get('mockId');
    if (qMock) {
      setTimeout(() => startFullMockExam(qMock), 200);
      return;
    }
    if (qMode === 'mock' || qMode === 'mode-mock') {
      switchMode('mode-mock');
      return;
    }"""
        code = code.replace("const qMode = params.get('mode');", param_handler + "\n    const qMode = params.get('mode');")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(code)
    print("Updated docs/widgets/practice_engine.html")

if __name__ == '__main__':
    main()
