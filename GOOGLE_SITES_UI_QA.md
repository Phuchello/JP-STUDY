# JP-STUDY — Phase 3.6 Google Sites Learner Portal QA & Verification Audit

## 1. Executive Summary

Phase 3.6 delivers a modern, Japanese-inspired, mobile-first Google Sites learner portal (`JP-STUDY — 日本語を少しずつ`) as the single primary entry point for the learner. 

This UI/UX overhaul transforms the learner experience from technical spreadsheets and bare forms into an inviting, calming, and focused educational space—**without modifying or breaking any underlying backend infrastructure** (Google Sheets, Forms, Apps Script triggers, or Drive storage).

- **Portal Live URL**: `https://sites.google.com/view/jp-study`
- **Publish Status**: Verified live, public view via direct link, search engine indexing blocked.
- **Backend Source of Truth**: Preserved 100% (`JP_STUDY_HOC_HOM_NAY` spreadsheet, 3 P0 Google Forms, `DRIVE_SETUP/JP_STUDY_SETUP.gs`).
- **Target Audience Alignment**: Japanese N4 foundation, low cognitive fatigue, gentle pacing ("5–10 phút cũng được. Mệt thì nghỉ, không cần học bù").

---

## 2. Information Architecture & Page Hierarchy

The portal strictly adheres to the 5-section architecture designed for low-friction daily access:

```
JP-STUDY (Portal Root)
├── 1. TRANG CHỦ (Home)
│   ├── Greeting & Subtitle ("Hôm nay mình học một chút thôi nhé.")
│   ├── Today's Learning Card (N4 Trợ từ trong câu, 5–8 phút)
│   ├── Primary Action Button ("BẮT ĐẦU HỌC" -> W01-B01)
│   ├── Section B: Other Activities overview (Luyện tập, Luyện nghe, Ôn lỗi sai, Mẹo học)
│   ├── Section C: Week 01 Available Practice (W01-B01, W01-B02, W01-B03)
│   └── Section D: Reassuring Rest Message ("Không khỏe thì nghỉ. Ngày mai học tiếp cũng được.")
├── 2. LUYỆN TẬP (Practice)
│   ├── Weekly Schedule: Tuần 01 Khởi động nền tảng
│   ├── W01-B01 — Trợ từ trong câu (5 câu · 5–8 phút)
│   ├── W01-B02 — Từ vựng & Kanji đời sống (8 câu · 8–12 phút)
│   ├── W01-B03 — Chia thể động từ cơ bản (5 câu · 6–10 phút)
│   └── Tuần 02 Placeholders ("Chờ kích hoạt", unlinked)
├── 3. MẸO HỌC (Study Tips & Reference)
│   ├── 01_NGU_PHAP_N4: 31 core grammar patterns
│   ├── 02_MEO_NGHE: Listening heuristics & conversational trap avoidance
│   ├── 03_MEO_DOC: Skimming & scanning techniques for short reading passages
│   ├── 04_NGU_PHAP_DE_NHAM: High-frequency confusing grammar pairs
│   ├── 05_GIAO_TIEP_DOI_SONG: Real-life conversational patterns (Konbini, station, office)
│   └── 06_KHUNG_VIET_NOI: 12 quick sentence frames for speaking and writing
├── 4. NGHE & NÓI (Listening & Speaking)
│   ├── Official Curated Source 1: NHK World — Easy Japanese
│   ├── Official Curated Source 2: Japan Foundation — Irodori Japanese for Life
│   ├── 4 Real-World Roleplay Scenarios: Konbini/supermarket, transit, workplace, medical
│   └── Gemini AI Tutor Practice Prompt (interactive 1-on-1 roleplay)
└── 5. TIẾN BỘ (Progress & Mistake Review)
    ├── 4-Step Gemini Error Tutor Workflow ("Chữa MỘT lỗi sau mỗi lần nộp rồi dừng lại")
    ├── Overview of 5 Tabs in Central Spreadsheet (HỌC HÔM NAY, TUẦN NÀY, LỊCH SỬ, LỖI CẦN ÔN, BÁO CÁO QUẢN LÝ)
    └── Direct link to Google Sheets tracker (authorized learner account only)
```

---

## 3. Visual Design Direction & Typography

| Element | Specification | Rationale |
| :--- | :--- | :--- |
| **Theme** | Aristotle (Khói tím / Soft Lavender-Indigo) | Restrained, professional, Japanese aesthetic without harsh high-contrast colors |
| **Typography** | Modern / Sans-serif (`Hiện đại`) | Clean, high legibility for Vietnamese tone marks and Japanese Kana/Kanji |
| **Header Type** | Chỉ tiêu đề (Title only) | Strips large wasteful banner imagery, maximizing visible content above the fold on mobile |
| **Palette** | Background: warm white/tinted grey; Primary: muted indigo/lavender; Accent: coral/soft red | Calming atmosphere, reducing cognitive fatigue |
| **Layout** | Single-column responsive card flow | Zero horizontal scroll on narrow viewports, 48px+ touch targets |

---

## 4. Responsive Viewport Test Matrix

All viewports were tested using Chrome DevTools device metrics emulation with touch event support:

| Viewport | Device Profile | Layout Outcome | Horizontal Scroll | Touch Targets | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **360 x 800** | Android Small / Budget | 1-column card stack; header collapses into hamburger menu; button text legible | None (0px overflow) | >= 48px, comfortable tap | **PASS** |
| **390 x 844** | iPhone 12/13/14 Standard | Optimal reading line length; crisp typography; cards clearly delineated | None (0px overflow) | >= 48px, comfortable tap | **PASS** |
| **430 x 932** | iPhone 14/15 Pro Max | Generous margins; primary CTA prominently visible above the fold | None (0px overflow) | >= 48px, comfortable tap | **PASS** |
| **768 x 1024** | iPad / Tablet Portrait | Centered reading container; top navigation visible or cleanly accessible | None (0px overflow) | Tablet friendly | **PASS** |
| **1280 x 800** | Laptop / Desktop Standard | Full horizontal navbar; centered aesthetic reading width; no excessive stretch | None (0px overflow) | Desktop click | **PASS** |
| **1440 x 900** | Desktop Large / MacBook | High aesthetic balance; comfortable whitespace; zero visual artifacts | None (0px overflow) | Desktop click | **PASS** |

---

## 5. End-to-End Link & Form Harmonization Audit

### 5.1 Quiz Responder Links
- **W01-B01 (Trợ từ trong câu)**: Verified live P0 responder form (5 questions, 1 pt each, validated N4 key, linked directly from primary portal button).
- **W01-B02 (Từ vựng & Kanji)**: Verified live P0 responder form (8 questions, 1 pt each, validated N4 key, linked from Luyện tập page).
- **W01-B03 (Chia thể động từ)**: Verified live P0 responder form (5 questions, 1 pt each, validated N4 key, linked from Luyện tập page).
*(Note: Full live responder URLs and Drive IDs are handed over privately per repository publication policy and not tracked on public GitHub).*

### 5.2 Forms Visual Harmonization
- **Theme Color**: Violet/lavender palette (`#673ab7`) harmonizes with the Aristotle portal theme.
- **Form Headers**: Clearly labeled with Week, Item ID, Skill, and Question count (`W01-B01 | N4 Trợ từ trong câu | 5 câu`).
- **No Pre-Submission Leakage**: Explanations and answer evaluations appear only after submission via "Xem điểm" (View score).
- **Fatigue & Attempt Tracking**: Includes optional `Mệt hôm nay` and required `Lần làm` fields on page 1 of each form.

---

## 6. Security, Privacy & Search Gating

1. **Search Engine Gating**: "Yêu cầu công cụ tìm kiếm công khai không hiển thị trang web của tôi" (Request search engines not to index) is permanently enabled in Google Sites publication settings.
2. **Access Control**:
   - Google Sites: Viewable by anyone with the link (no sign-in barrier for the portal landing page).
   - Google Sheets Backend: Strictly restricted to the owner and authenticated learner.
   - Google Forms Responses: Stored in restricted sheets via authorized Apps Script installable triggers.
3. **Repository Cleanliness**: Zero private Google Drive IDs, private sheet keys, API secrets, or local Windows file paths are exposed in public markdown files or tracked Git assets.

---

## 7. QA Verdict

**DECISION: PASS — READY FOR LEARNER HANDOFF**

The Google Sites portal provides an inviting, low-stress, mobile-optimized experience that solves the visual and usability challenges of bare Google Sheets/Forms, while keeping 100% of the underlying P0 technical architecture intact.
