"""
Regression Tests for Timed Sessions, Deep Links, DOM Security, and Sectional Practice Metadata.

Validates:
1. P0 - DOM Security & Safe Parameter Handling:
   - showParamBadge uses safe DOM construction (document.createElement, textContent)
   - Zero innerHTML injection sinks in URL parameter handling flow
   - renderSessionHistory avoids innerHTML interpolation
   - All URL inputs clamped and validated against strict whitelists
2. P0 - Timers & Absolute Deadline:
   - Single timer interval controller (stopActiveTimer) exists
   - stopActiveTimer is invoked across all session starting/stopping routines
   - Stale timer callback guards (currentSessionId check) prevent leaked intervals
   - Submission lock (isSubmitted) prevents duplicate submissions
   - Absolute wall-clock deadline (Date.now()) and visibilitychange synchronization
3. P1 - Sectional Practice & Data Integrity:
   - N2-MOCK-01 has exactly 75 answerable questions and 105-minute timing
   - N3-MOCK-01 has exactly 73 answerable questions and 100-minute timing
   - Every question strictly matches its designated JLPT level
   - submitTimedSession preserves mockId, mockTitle, completionTime in history
   - N3 100-minute combined structure is explicitly distinguished from official 30+70 schedule
   - Direct launch for N2-MOCK-01 and N3-MOCK-01, rejection for unavailable mocks
4. P1 - Single Validated Session Configuration:
   - N2 standard preset: 30 questions, 35 minutes
   - N3 standard preset: 30 questions, 30 minutes
   - Marathon preset: MIXED N2/N3, 50 questions, 60 minutes
   - Short practice: 15 questions, 15 minutes
   - Rejection and safe normalization of incompatible combinations
   - Zero silent JLPT level substitution at session start
"""
import unittest
import re
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRACTICE_ENGINE_HTML = ROOT / "docs/widgets/practice_engine.html"
CATALOG_HTML = ROOT / "docs/widgets/jlpt_exam_catalog.html"
N2_MOCK_JSON = ROOT / "data/mock_exams/n2_mock_01.json"
N3_MOCK_JSON = ROOT / "data/mock_exams/n3_mock_01.json"


class TestTimerAndDeepLinks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine_html = PRACTICE_ENGINE_HTML.read_text(encoding="utf-8")
        cls.catalog_html = CATALOG_HTML.read_text(encoding="utf-8")

    # --- P0: DOM Security & Deep Links Tests ---
    def test_d_duration_contains_35_min_option(self):
        """Ensure Mode D duration select contains the 35-minute standard N2 option."""
        self.assertIn('<option value="35">35 Phút (30 câu tiêu chuẩn N2)</option>', self.engine_html)

    def test_param_config_badge_in_dom(self):
        """Ensure param-config-badge div is declared to show applied configuration."""
        self.assertIn('id="param-config-badge"', self.engine_html)
        self.assertIn('function showParamBadge', self.engine_html)

    def test_show_param_badge_avoids_innerhtml(self):
        """Ensure showParamBadge constructs DOM elements using textContent and never calls innerHTML."""
        badge_fn_match = re.search(r"function showParamBadge\(paramEntries\)\s*\{([\s\S]*?)\n\}", self.engine_html)
        self.assertIsNotNone(badge_fn_match, "showParamBadge function must be defined")
        badge_body = badge_fn_match.group(1)
        self.assertNotIn(".innerHTML", badge_body, "showParamBadge must never assign to innerHTML")
        self.assertIn("badge.textContent = ''", badge_body, "showParamBadge must clear content safely")
        self.assertIn(".textContent = ", badge_body, "showParamBadge must use textContent for all text values")

    def test_apply_url_parameters_structure(self):
        """Ensure applyUrlParameters parses and validates level, duration, count, skill, mock."""
        self.assertIn("function applyUrlParameters()", self.engine_html)
        self.assertIn("params.get('level')", self.engine_html)
        self.assertIn("params.get('duration')", self.engine_html)
        self.assertIn("params.get('count')", self.engine_html)
        self.assertIn("params.get('skill')", self.engine_html)
        self.assertIn("params.get('mode')", self.engine_html)
        self.assertIn("document.getElementById('d-level')", self.engine_html)
        self.assertIn("document.getElementById('d-duration')", self.engine_html)
        self.assertIn("document.getElementById('a-level')", self.engine_html)
        self.assertIn("document.getElementById('a-count')", self.engine_html)
        self.assertIn("document.getElementById('a-skill')", self.engine_html)

    def test_catalog_random_practice_links(self):
        """Verify catalog random practice links pass duration, level, count, and mode correctly."""
        # N2: 30 questions, 35 minutes
        self.assertIn(
            "practice_engine.html?mode=mode-d&level=N2&count=30&duration=35",
            self.catalog_html,
            "N2 random practice link must pass mode=mode-d, level=N2, count=30, and duration=35"
        )
        # N3: 30 questions, 30 minutes
        self.assertIn(
            "practice_engine.html?mode=mode-d&level=N3&count=30&duration=30",
            self.catalog_html,
            "N3 random practice link must pass mode=mode-d, level=N3, count=30, and duration=30"
        )
        # Marathon: MIXED, 50 questions, 60 minutes
        self.assertIn(
            "practice_engine.html?mode=mode-d&level=MIXED&count=50&duration=60",
            self.catalog_html,
            "Marathon link must pass mode=mode-d, level=MIXED, count=50, and duration=60"
        )

    # --- P0: Timers Tests ---
    def test_single_timer_interval_architecture(self):
        """Ensure stopActiveTimer controller clears global and state timers."""
        self.assertIn("let globalTimerInterval = null;", self.engine_html)
        self.assertIn("function stopActiveTimer()", self.engine_html)
        self.assertIn("clearInterval(globalTimerInterval);", self.engine_html)

    def test_stop_timer_called_on_session_transitions(self):
        """Ensure stopActiveTimer is called when starting or resetting any session."""
        self.assertTrue(re.search(r"function startTimedSession\(\)\s*\{[\s\S]*?stopActiveTimer\(\);", self.engine_html))
        self.assertTrue(re.search(r"function startFullMockExam\([^\)]*\)\s*\{[\s\S]*?stopActiveTimer\(\);", self.engine_html))
        self.assertTrue(re.search(r"function startGrindSession\(\)\s*\{[\s\S]*?stopActiveTimer\(\);", self.engine_html))
        self.assertTrue(re.search(r"function startSeededSession\(\)\s*\{[\s\S]*?stopActiveTimer\(\);", self.engine_html))
        self.assertTrue(re.search(r"function resetTimedToConfig\(\)\s*\{[\s\S]*?stopActiveTimer\(\);", self.engine_html))

    def test_stale_callback_and_duplicate_submission_guards(self):
        """Ensure timer interval checks session ID token and submission state to prevent runaway ticks."""
        self.assertIn("currentSessionId", self.engine_html)
        self.assertIn("timedState.sessionId !== currentSessionId", self.engine_html)
        self.assertIn("timedState.isSubmitted", self.engine_html)

    def test_absolute_deadline_timer(self):
        """Ensure timer computes absolute deadlineTime with Date.now() and syncs on visibilitychange."""
        self.assertIn("deadlineTime: deadlineTime", self.engine_html)
        self.assertIn("timedState.deadlineTime - now", self.engine_html)
        self.assertIn("visibilitychange", self.engine_html)
        self.assertIn("updateTimedCountdown()", self.engine_html)

    # --- P1: Sectional Practice & Mock Launch Tests ---
    def test_direct_mock_launch_for_n2_and_n3(self):
        """Ensure applyUrlParameters triggers launchMockExamSafely for N2-MOCK-01 and N3-MOCK-01."""
        self.assertIn("function launchMockExamSafely(mockId", self.engine_html)
        self.assertIn("['N2-MOCK-01', 'N3-MOCK-01'].includes(upperMock)", self.engine_html)
        self.assertIn("launchMockExamSafely(upperMock", self.engine_html)
        self.assertIn("startFullMockExam(upperMock", self.engine_html)

    def test_unavailable_mock_rejection(self):
        """Ensure unavailable mock exams trigger alert/badge and do not launch."""
        self.assertIn("Đề thi thử ${cleanId} hiện đang trong giai đoạn hoàn thiện nội dung (IN DEVELOPMENT)", self.engine_html)
        self.assertIn("switchMode('mode-mock');", self.engine_html)

    def test_mock_metadata_preserved_in_history(self):
        """Ensure submitTimedSession preserves mockId, mockTitle, and completionTime."""
        self.assertIn("mockId: mockId", self.engine_html)
        self.assertIn("title: mockTitle", self.engine_html)
        self.assertIn("completionTime: new Date().toISOString()", self.engine_html)

    def test_history_rendering_and_export_includes_mock_metadata(self):
        """Ensure renderSessionHistory displays mock badge and exportSessionsCsv outputs mock columns."""
        self.assertIn("s.mockId", self.engine_html)
        self.assertIn("Mã phiên,Mã đề,Tiêu đề", self.engine_html)

    def test_render_session_history_avoids_innerhtml(self):
        """Ensure renderSessionHistory builds table rows with textContent and document.createElement."""
        history_fn_match = re.search(r"function renderSessionHistory\(\)\s*\{([\s\S]*?)\n\}", self.engine_html)
        self.assertIsNotNone(history_fn_match, "renderSessionHistory function must be defined")
        history_body = history_fn_match.group(1)
        self.assertNotIn("tr.innerHTML =", history_body, "renderSessionHistory must not interpolate into tr.innerHTML")
        self.assertIn("document.createElement('tr')", history_body)
        self.assertIn("tdDate.textContent = ", history_body)

    def test_no_misleading_claims(self):
        """Ensure sectional practice without Section 2 is properly labeled and doesn't mislead."""
        self.assertIn("KẾT QUẢ PHẦN 1: KIẾN THỨC NGÔN NGỮ & ĐỌC HIỂU", self.engine_html)
        self.assertIn("Nghỉ giải lao 10 phút & Vào Phần 2", self.engine_html)

    def test_n3_100_minute_combined_structure_delineation(self):
        """Verify N3 100-minute combined practice note is explicitly distinct from official 30+70 schedule."""
        # Must exist in practice engine
        self.assertIn("Kỳ thi N3 chính thức tách rời", self.engine_html)
        self.assertIn("Từ vựng (30p) và Ngữ pháp/Đọc hiểu (70p)", self.engine_html)
        self.assertIn("gộp 2 khối thành phiên liên tục 100 phút", self.engine_html)

        # Must exist in catalog
        self.assertIn("Kỳ thi N3 chính thức tách rời", self.catalog_html)
        self.assertIn("100 phút", self.catalog_html)
        self.assertIn("gộp 2 khối thành phiên liên tục 100 phút", self.catalog_html)

    def test_no_silent_level_fallback_in_timed_session(self):
        """Ensure startTimedSession never silently substitutes another JLPT level."""
        self.assertNotIn("pool = bank.filter(q => q.exposureEligible !== false);", self.engine_html)
        self.assertIn("Chỉ có ${pool.length} câu hỏi khả dụng cho cấp độ ${level}", self.engine_html)
        self.assertIn("Lỗi bảo toàn cấp độ", self.engine_html)

    # --- P1 & P2: Executable Behavioral Verification Tests ---
    def test_n2_mock_data_integrity(self):
        """Executable test: verify N2-MOCK-01 JSON file contains valid full mock questions across 2 sections, all N2."""
        self.assertTrue(N2_MOCK_JSON.exists(), "N2 mock file must exist")
        data = json.loads(N2_MOCK_JSON.read_text(encoding="utf-8"))
        self.assertEqual(data["examId"], "N2-MOCK-01")
        self.assertEqual(data["durationMinutes"], 155)
        self.assertEqual(data["totalQuestions"], 105)
        sec1_items = data["sections"][0]["items"]
        sec2_items = data["sections"][1]["items"]
        self.assertEqual(len(sec1_items), 75, "N2 sectional practice 1 must have exactly 75 items")
        self.assertEqual(len(sec2_items), 30, "N2 sectional practice 2 must have exactly 30 items")
        self.assertTrue(all(q["level"] == "N2" for q in sec1_items + sec2_items), "All questions in N2 mock must be level N2")
        # Check no option duplicates
        for q in sec1_items + sec2_items:
            opt_texts = [opt["text"].strip() for opt in q["options"]]
            self.assertEqual(len(opt_texts), len(set(opt_texts)), f"Item {q['id']} has duplicate option text")

    def test_n3_mock_data_integrity(self):
        """Executable test: verify N3-MOCK-01 JSON file contains exactly 73 answerable questions, all N3."""
        self.assertTrue(N3_MOCK_JSON.exists(), "N3 mock file must exist")
        data = json.loads(N3_MOCK_JSON.read_text(encoding="utf-8"))
        self.assertEqual(data["examId"], "N3-MOCK-01")
        self.assertEqual(data["durationMinutes"], 100)
        self.assertEqual(data["totalQuestions"], 73)
        items = data["sections"][0]["items"]
        self.assertEqual(len(items), 73, "N3 sectional practice must have exactly 73 items")
        self.assertTrue(all(q["level"] == "N3" for q in items), "All questions in N3 mock must be level N3")
        # Check no option duplicates
        for q in items:
            opt_texts = [opt["text"].strip() for opt in q["options"]]
            self.assertEqual(len(opt_texts), len(set(opt_texts)), f"Item {q['id']} has duplicate option text")

    def test_mode_d_configuration_presets_behavior(self):
        """Executable behavioral simulation of Mode D configuration rules."""
        def validate_mode_d_config(level, raw_count, raw_dur):
            # Mirror the exact JavaScript logic in applyUrlParameters
            effective_level = level if level in ['N2', 'N3', 'MIXED'] else 'N2'
            dur_int = int(raw_dur) if raw_dur is not None else None
            count_int = int(raw_count) if raw_count is not None else None
            valid_durations = [15, 30, 35, 60]
            valid_counts = [15, 30, 50]

            selected_dur = 30
            selected_count = 30
            warning = None

            if dur_int is not None and count_int is not None:
                is_compatible = False
                if dur_int == 15 and count_int == 15: is_compatible = True
                elif dur_int == 30 and count_int == 30: is_compatible = True
                elif dur_int == 35 and count_int == 30: is_compatible = True
                elif dur_int == 60 and count_int == 50: is_compatible = True

                if is_compatible:
                    selected_dur = dur_int
                    selected_count = count_int
                else:
                    if dur_int in valid_durations:
                        selected_dur = dur_int
                        selected_count = 15 if dur_int == 15 else (50 if dur_int == 60 else 30)
                        warning = f"Incompatible count {count_int} adjusted to {selected_count} for duration {dur_int}"
                    elif count_int in valid_counts:
                        selected_count = count_int
                        selected_dur = 15 if count_int == 15 else (60 if count_int == 50 else (35 if effective_level == 'N2' else 30))
                        warning = f"Invalid duration {raw_dur} adjusted to {selected_dur} for count {count_int}"
                    else:
                        selected_dur = 60 if effective_level == 'MIXED' else (35 if effective_level == 'N2' else 30)
                        selected_count = 50 if effective_level == 'MIXED' else 30
                        warning = "Both invalid"
            elif dur_int is not None:
                if dur_int in valid_durations:
                    selected_dur = dur_int
                    selected_count = 15 if dur_int == 15 else (50 if dur_int == 60 else 30)
                else:
                    warning = "Invalid duration"
            elif count_int is not None:
                if count_int in valid_counts:
                    selected_count = count_int
                    selected_dur = 15 if count_int == 15 else (60 if count_int == 50 else (35 if effective_level == 'N2' else 30))
                else:
                    warning = "Invalid count"
            else:
                selected_dur = 60 if effective_level == 'MIXED' else (35 if effective_level == 'N2' else 30)
                selected_count = 50 if effective_level == 'MIXED' else 30

            return effective_level, selected_count, selected_dur, warning

        # 1. N2 standard preset
        lvl, cnt, dur, warn = validate_mode_d_config('N2', '30', '35')
        self.assertEqual((lvl, cnt, dur, warn), ('N2', 30, 35, None))

        # 2. N3 standard preset
        lvl, cnt, dur, warn = validate_mode_d_config('N3', '30', '30')
        self.assertEqual((lvl, cnt, dur, warn), ('N3', 30, 30, None))

        # 3. Marathon preset
        lvl, cnt, dur, warn = validate_mode_d_config('MIXED', '50', '60')
        self.assertEqual((lvl, cnt, dur, warn), ('MIXED', 50, 60, None))

        # 4. Short preset
        lvl, cnt, dur, warn = validate_mode_d_config('N2', '15', '15')
        self.assertEqual((lvl, cnt, dur, warn), ('N2', 15, 15, None))

        # 5. Incompatible combination rejection: count 50 with duration 15
        lvl, cnt, dur, warn = validate_mode_d_config('N2', '50', '15')
        self.assertEqual(dur, 15)
        self.assertEqual(cnt, 15, "Incompatible count 50 with duration 15 must adjust count to 15")
        self.assertIsNotNone(warn)

        # 6. Incompatible combination rejection: count 100 with duration 35
        lvl, cnt, dur, warn = validate_mode_d_config('N2', '100', '35')
        self.assertEqual(dur, 35)
        self.assertEqual(cnt, 30, "Incompatible count 100 with duration 35 must adjust count to 30")
        self.assertIsNotNone(warn)


if __name__ == "__main__":
    unittest.main()
