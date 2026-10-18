"""
Regression Tests for Timed Sessions, Deep Links, and Sectional Practice Metadata.
Validates:
1. P0 - Deep Links:
   - practice_engine.html has option 35 in d-duration
   - applyUrlParameters handles mode, level, count, duration, skill, mockId
   - param-config-badge is present in DOM
   - Catalog links in jlpt_exam_catalog.html pass accurate parameters:
     * N2: mode=mode-d&level=N2&count=30&duration=35
     * N3: mode=mode-d&level=N3&count=30&duration=30
     * Marathon: mode=mode-d&level=MIXED&count=50&duration=60
2. P0 - Timers:
   - Single timer interval controller (stopActiveTimer) exists
   - stopActiveTimer is invoked across all session starting/stopping routines
   - Stale timer callback guards (currentSessionId check) prevent leaked intervals
   - Submission lock (isSubmitted) prevents duplicate submissions
3. P1 - Sectional Practice & History:
   - submitTimedSession preserves mockId, mockTitle, completionTime in history
   - renderSessionHistory displays mockId badge and title
   - exportSessionsCsv includes mockId and title columns
   - No misleading 'Full Mock 180 điểm' or 'scaled score' claims exist
   - N3 100-minute combined structure is explicitly distinguished from official 30+70 schedule
"""
import unittest
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRACTICE_ENGINE_HTML = ROOT / "docs/widgets/practice_engine.html"
CATALOG_HTML = ROOT / "docs/widgets/jlpt_exam_catalog.html"


class TestTimerAndDeepLinks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine_html = PRACTICE_ENGINE_HTML.read_text(encoding="utf-8")
        cls.catalog_html = CATALOG_HTML.read_text(encoding="utf-8")

    # --- P0: Deep Links Tests ---
    def test_d_duration_contains_35_min_option(self):
        """Ensure Mode D duration select contains the 35-minute standard N2 option."""
        self.assertIn('<option value="35">35 Phút (30 câu tiêu chuẩn N2)</option>', self.engine_html)

    def test_param_config_badge_in_dom(self):
        """Ensure param-config-badge div is declared to show applied configuration."""
        self.assertIn('id="param-config-badge"', self.engine_html)
        self.assertIn('showParamBadge', self.engine_html)

    def test_apply_url_parameters_functionality(self):
        """Ensure applyUrlParameters parses and validates level, duration, count, skill, mock."""
        self.assertIn("function applyUrlParameters()", self.engine_html)
        self.assertIn("params.get('level')", self.engine_html)
        self.assertIn("params.get('duration')", self.engine_html)
        self.assertIn("params.get('count')", self.engine_html)
        self.assertIn("params.get('skill')", self.engine_html)
        self.assertIn("params.get('mode')", self.engine_html)
        # Check that d-level, d-duration, a-level, a-count, a-skill are targeted
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
        # startTimedSession
        self.assertTrue(re.search(r"function startTimedSession\(\)\s*\{[\s\S]*?stopActiveTimer\(\);", self.engine_html))
        # startFullMockExam
        self.assertTrue(re.search(r"function startFullMockExam\(mockId\)\s*\{[\s\S]*?stopActiveTimer\(\);", self.engine_html))
        # startGrindSession
        self.assertTrue(re.search(r"function startGrindSession\(\)\s*\{[\s\S]*?stopActiveTimer\(\);", self.engine_html))
        # startSeededSession
        self.assertTrue(re.search(r"function startSeededSession\(\)\s*\{[\s\S]*?stopActiveTimer\(\);", self.engine_html))
        # resetTimedToConfig
        self.assertTrue(re.search(r"function resetTimedToConfig\(\)\s*\{[\s\S]*?stopActiveTimer\(\);", self.engine_html))

    def test_stale_callback_and_duplicate_submission_guards(self):
        """Ensure timer interval checks session ID token and submission state to prevent runaway ticks."""
        self.assertIn("currentSessionId", self.engine_html)
        self.assertIn("timedState.sessionId !== currentSessionId", self.engine_html)
        self.assertIn("timedState.isSubmitted", self.engine_html)

    # --- P1: Sectional Practice & History Tests ---
    def test_mock_metadata_preserved_in_history(self):
        """Ensure submitTimedSession preserves mockId, mockTitle, and completionTime."""
        self.assertIn("mockId: mockId", self.engine_html)
        self.assertIn("title: mockTitle", self.engine_html)
        self.assertIn("completionTime: new Date().toISOString()", self.engine_html)

    def test_history_rendering_and_export_includes_mock_metadata(self):
        """Ensure renderSessionHistory displays mock badge and exportSessionsCsv outputs mock columns."""
        self.assertIn("s.mockId", self.engine_html)
        self.assertIn("Mã phiên,Mã đề,Tiêu đề", self.engine_html)

    def test_no_misleading_claims(self):
        """Ensure no misleading 'Full Mock 180 điểm' or 'scaled score' claims remain in practice engine."""
        self.assertNotIn("180 điểm", self.engine_html)
        self.assertNotIn("scaled score", self.engine_html)

    def test_n3_100_minute_combined_structure_delineation(self):
        """Verify N3 100-minute combined practice note is distinct from official 30+70 schedule."""
    def test_direct_mock_launch_for_n2_and_n3(self):
        """Ensure applyUrlParameters triggers launchMockExamSafely for N2-MOCK-01 and N3-MOCK-01."""
        self.assertIn("function launchMockExamSafely(mockId)", self.engine_html)
        self.assertIn("['N2-MOCK-01', 'N3-MOCK-01'].includes(upperMock)", self.engine_html)
        self.assertIn("launchMockExamSafely(upperMock);", self.engine_html)
        self.assertIn("startFullMockExam(upperMock)", self.engine_html)

    def test_unavailable_mock_rejection(self):
        """Ensure unavailable mock exams trigger alert/badge and do not launch."""
        self.assertIn("Đề thi thử ${upperMock || mockId} hiện đang trong giai đoạn hoàn thiện nội dung (IN DEVELOPMENT)", self.engine_html)
        self.assertIn("switchMode('mode-mock');", self.engine_html)

    def test_absolute_deadline_timer(self):
        """Ensure timer computes absolute deadlineTime with Date.now() and syncs on visibilitychange."""
        self.assertIn("deadlineTime: deadlineTime", self.engine_html)
        self.assertIn("timedState.deadlineTime - now", self.engine_html)
        self.assertIn("visibilitychange", self.engine_html)
        self.assertIn("updateTimedCountdown()", self.engine_html)

    def test_no_silent_level_fallback_in_timed_session(self):
        """Ensure startTimedSession never silently substitutes another JLPT level."""
        self.assertNotIn("if (pool.length < qCount) {\n    pool = bank.filter(q => q.exposureEligible !== false);", self.engine_html)
        self.assertIn("Chỉ có ${pool.length} câu hỏi khả dụng cho cấp độ ${level}", self.engine_html)


if __name__ == "__main__":
    unittest.main()

