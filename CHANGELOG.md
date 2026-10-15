# Changelog

## 2026-10-15 — Phase 3.6 Google Sites learner portal UI/UX overhaul and responsive verification

- Design and deploy polished, Japanese-inspired learner portal on Google Sites (`https://sites.google.com/view/jp-study`) using Aristotle theme with soft lavender/indigo palette, clean typography, and zero-waste title-only header.
- Implement structured 5-page learner architecture: Trang chủ (Today's Card, CTA button, rest reminder), Luyện tập (3 active P0 forms, Week 2 placeholders), Mẹo học (6 core PDF guides summarized), Nghe & Nói (NHK, Irodori, 4 roleplays, Gemini prompt), and Tiến bộ (Gemini Error Tutor workflow, Sheets overview).
- Verify responsive mobile-first layouts and touch targets across 6 viewports: Mobile Small (360x800), Mobile Standard (390x844), Mobile Large (430x932), Tablet (768x1024), Desktop Standard (1280x800), and Desktop Large (1440x900) with zero horizontal scroll.
- Configure Google Sites publication settings with search engine indexing blocked ("Yêu cầu công cụ tìm kiếm công khai không hiển thị trang web của tôi").
- Preserve 100% of underlying backend architecture: Google Sheets source of truth, 3 P0 Google Forms, Apps Script triggers, QA synthetic isolation, and Drive exports remain intact.

## 2026-10-15 — Live P0 acceptance, synthetic QA verification and dashboard activation

- Configure Google Forms grade release settings to immediate post-submission release with missed questions, correct answers, point values, and detailed explanations.
- Execute authentic browser synthetic QA submissions across all three P0 Forms (W01-B01: 3/5, W01-B02: 6/8, W01-B03: 3/5) containing correct, incorrect, and blank items via authenticated browser session.
- Verify installable submit triggers and QA quarantine in Google Apps Script via `verifySyntheticQa()`; confirm zero learner rows in `CHI_TIET` and isolated records in `JP_STUDY_QA_SYNTHETIC` spreadsheet and Drive CSV/JSON reports.
- Execute `activateP0Verified()` to activate all three P0 Forms; verify learner dashboard `HỌC HÔM NAY` status is `Sẵn sàng` with working `MỞ BÀI NGẮN` link and active week checklist.
- Verify automatic export of management report `DAILY_LEARNING_REPORT.csv` and `DAILY_LEARNING_REPORT.json` to Google Drive.
- Verify responsive layout at mobile width (390x844) and laptop viewport (1280x800); confirm owner-only access gating until learner account is assigned.

## 2026-10-15 — Native P0 creation and restricted responder checkpoint

- Execute the existing bound Apps Script. Prior Completed executions were only `onOpen`; they had not deployed quizzes. Create exactly three unpublished P0 Forms, reusing the interrupted first Form, with no changes to source question IDs or keys.
- Repair the native unlinked-Form destination exception without masking unrelated errors or replacing an unexpected destination. Native `setupP0` and `auditForms` then complete.
- Enable Drive Advanced v3 with owner consent and remove default published-view `anyone` responder permissions. Confirm owner-only ACLs on all three Forms via native execution and independent Drive metadata readback.
- Add owner-only deployment inspection and isolated synthetic QA helpers. Pass 394 local logic/Workspace mock checks; helper E2E remains unverified until actual browser submissions and native trigger records exist.
- Synchronize the bound manifest with explicit approved scopes and Asia/Tokyo. Google still gates Sheets access behind OAuth. No publication, activation, learner sharing or live grading/export success is claimed. See [deployment evidence](qa/drive_first_deployment.json).

## 2026-10-15 — Drive-first templates and private Sheets checkpoint

- Create owner-only Drive folders and a native five-tab dashboard; upload seven concise PDFs and tutor/report prompts. No private IDs, records or URLs are published here.
- Reuse 68 of the original 80 N4 questions across ten short quiz specifications. Preserve original bank, keys, patterns and previous checkpoints.
- Add an idempotent Workspace installer, raw response retention, QA quarantine, item-ID scoring mapping, new/review/assisted/unknown separation and daily CSV/JSON export.
- Pass 387 pure-logic/Workspace mock checks. Read back native Sheets and permissions; repair Vietnamese-locale link errors with rich-text links. Verify PDFs and exported-sheet layouts within documented limits.
- Keep Forms deployment, Google grading/triggers and real-device usability QA_PENDING until authenticated live acceptance; this checkpoint does not claim Phase 3.5 completion.


## 2026-10-15 — Initial public synchronization

- Preserve Phase 1, Phase 2, Phase 2.1 and Phase 3 pilot checkpoints in a reviewable repository.
- Publish deidentified Markdown editions of private reports and rebuild the Phase 3 starting PDF with a synthetic profile. Keep all originals local and record source hashes/omissions.
- Preserve the audited 80-question N4 payload, four speaking scenarios, 31 patterns/37 instructional examples and validated keys; retain QA provenance and current tests.
- Include four distinct blank workbook checkpoints, six useful PDFs, Gemini prompts, research synthesis/citation metadata, historical implementation source and scoped QA reports.
- Document incomplete expansion/N3/N2 work, evidence gaps and persistent future commit/push policy. No credentials, personal progress exports, third-party full-text downloads or release ZIP committed.
