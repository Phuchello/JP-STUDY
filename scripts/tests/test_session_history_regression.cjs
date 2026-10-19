// scripts/tests/test_session_history_regression.cjs
// Playwright regression test for Session History navigation and persistence
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const assert = require('assert/strict');

const ENGINE_URL = 'file:///' + path.resolve(__dirname, '../../docs/widgets/practice_engine.html').replaceAll('\\', '/');
const userHome = process.env.USERPROFILE || process.env.HOME || '';
const SCREENSHOT_DIR = path.join(userHome, '.gemini', 'antigravity', 'brain', '07f27e52-1325-4adc-9ec0-5c8e7670a48d', 'screenshots');

async function testSessionHistory() {
  console.log('=== TEST: SESSION HISTORY NAVIGATION & PERSISTENCE REGRESSION ===');
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const page = await context.newPage();

  try {
    // 1. Direct Launch Section 1
    await page.goto(`${ENGINE_URL}?mockId=N2-MOCK-01`);
    await page.waitForTimeout(500);

    // Answer 50 questions and submit Section 1
    await page.evaluate(() => {
      timedState.questions.forEach((q, idx) => {
        if (idx < 50) timedState.userAnswers[q.id] = q.correctAnswer;
      });
      submitTimedSession();
    });
    await page.waitForTimeout(400);

    // Click "Xem Lịch Sử Học Tập" from Section 1 summary
    const historyBtnVisible = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('#d-summary-msg button'));
      const hBtn = btns.find(b => b.textContent.includes('Xem Lịch Sử Học Tập'));
      if (hBtn) {
        hBtn.click();
        return true;
      }
      return false;
    });
    assert.equal(historyBtnVisible, true, 'History button must be present in Section 1 summary');
    await page.waitForTimeout(300);

    // Verify mode-f is active and nav-tab 5 is highlighted
    const modeState = await page.evaluate(() => {
      const modeF = document.getElementById('mode-f');
      const isModeFActive = modeF && modeF.classList.contains('active');
      const navTabs = Array.from(document.querySelectorAll('.nav-tab'));
      const activeTab = navTabs.find(t => t.classList.contains('active'));
      const activeTabIdx = navTabs.findIndex(t => t.classList.contains('active'));
      const rows = document.querySelectorAll('#session-history-tbody tr').length;
      const firstRowScore = document.querySelector('#session-history-tbody tr td:nth-child(4)')?.textContent || '';
      return { isModeFActive, activeTabText: activeTab?.textContent, activeTabIdx, rows, firstRowScore };
    });

    console.log('Mode F Active State:', modeState);
    assert.equal(modeState.isModeFActive, true, 'mode-f must be active');
    assert.equal(modeState.activeTabIdx, 5, 'Nav-tab index 5 (Nhật ký học tập) must be highlighted');
    assert.ok(modeState.activeTabText.includes('Nhật ký học tập'), 'Active tab must be Nhật ký học tập');
    assert.equal(modeState.rows, 1, 'Exactly 1 session recorded after Section 1');
    assert.ok(modeState.firstRowScore.includes('50'), 'Recorded score must match 50 correct');

    // 2. Full Mock Combined Submission Check
    // Start Section 2 directly after Section 1 (simulating break transition)
    await page.evaluate(() => {
      startFullMockExam('N2-MOCK-01', 1);
    });
    await page.waitForTimeout(400);

    // Verify Section 2 Listening Modality in exam mode
    const modality = await page.evaluate(() => {
      // Check Mondai 1 stem
      const m1Stem = document.getElementById('d-q-stem')?.textContent || '';
      // Advance to Mondai 3 (index 11)
      timedState.currentIndex = 11;
      renderTimedQuestion();
      const m3Stem = document.getElementById('d-q-stem')?.textContent || '';
      const m3Opts = Array.from(document.querySelectorAll('#d-q-options .opt-btn')).map(b => b.textContent.trim());
      // Advance to Mondai 4 (index 16)
      timedState.currentIndex = 16;
      renderTimedQuestion();
      const m4Stem = document.getElementById('d-q-stem')?.textContent || '';
      const m4Opts = Array.from(document.querySelectorAll('#d-q-options .opt-btn')).map(b => b.textContent.trim());

      return { m1Stem, m3Stem, m3Opts, m4Stem, m4Opts };
    });

    assert.ok(modality.m1Stem.includes('問題１：問題用紙を見ながら音声を聞いて'), 'Mondai 1 stem shows official instruction');
    assert.ok(modality.m3Stem.includes('問題３：問題用紙に何も印刷されていません'), 'Mondai 3 stem shows official instruction');
    assert.deepEqual(modality.m3Opts, ['A１番', 'B２番', 'C３番', 'D４番'], 'Mondai 3 shows clean numbered choices without text spoilers');
    assert.ok(modality.m4Stem.includes('問題４：問題用紙に何も印刷されていません'), 'Mondai 4 stem shows official instruction');
    assert.deepEqual(modality.m4Opts, ['A１番', 'B２番', 'C３番'], 'Mondai 4 shows 3 clean numbered choices');
    console.log('✅ Listening modality verified: Zero text spoilers during active exam!');

    // Answer 25 questions in Section 2 and submit
    await page.evaluate(() => {
      timedState.questions.forEach((q, idx) => {
        if (idx < 25) timedState.userAnswers[q.id] = q.correctAnswer;
        else timedState.userAnswers[q.id] = (q.correctAnswer === 'A' ? 'B' : 'A');
      });
      submitTimedSession();
    });
    await page.waitForTimeout(400);

    // Click "Xem Lịch Sử Học Tập" from Full Mock summary
    const clickHistory2 = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('#d-summary-msg button'));
      const hBtn = btns.find(b => b.textContent.includes('Xem Lịch Sử Học Tập'));
      if (hBtn) {
        hBtn.click();
        return true;
      }
      return false;
    });
    assert.equal(clickHistory2, true, 'History button must be clickable in Full Mock summary');
    await page.waitForTimeout(300);

    // Verify session history now contains both sessions, and the latest is FULL_MOCK 105 questions
    const historyData = await page.evaluate(() => {
      const sessions = JSON.parse(localStorage.getItem('JP_STUDY_SESSIONS_V2') || '[]');
      const firstSess = sessions[0];
      const rows = document.querySelectorAll('#session-history-tbody tr').length;
      return { totalSessions: sessions.length, firstSess, rows };
    });

    console.log('History data after Full Mock:', historyData);
    assert.equal(historyData.totalSessions, 2, 'Two total sessions recorded');
    assert.equal(historyData.firstSess.mode, 'FULL_MOCK');
    assert.equal(historyData.firstSess.totalQuestions, 105, 'Combined full mock records 105 questions');
    assert.equal(historyData.firstSess.scoreCorrect, 75, '50 (Sec 1) + 25 (Sec 2) = 75 correct');
    assert.equal(historyData.firstSess.accuracyPct, 71, '75/105 = 71%');

    // 3. Test Refresh & Persistence
    await page.reload();
    await page.waitForTimeout(400);

    await page.evaluate(() => switchMode('mode-f'));
    await page.waitForTimeout(300);

    const reloadedRows = await page.evaluate(() => document.querySelectorAll('#session-history-tbody tr').length);
    assert.equal(reloadedRows, 2, 'Session history must persist across full page reloads');

    // 4. Test Stale Section 1 draft isolation
    // Verify that the temporary JP_MOCK_SAVE draft was cleared after full mock completion
    const draftAfterFull = await page.evaluate(() => localStorage.getItem('JP_MOCK_SAVE_N2-MOCK-01'));
    assert.equal(draftAfterFull, null, 'Draft must be cleared after combined full mock completion');

    // Now test standalone Section 2 run without Section 1
    await page.evaluate(() => {
      startFullMockExam('N2-MOCK-01', 1);
      timedState.questions.forEach((q, idx) => {
        if (idx < 20) timedState.userAnswers[q.id] = q.correctAnswer;
      });
      submitTimedSession();
    });
    await page.waitForTimeout(300);

    const standaloneCheck = await page.evaluate(() => {
      const scoreTxt = document.getElementById('d-summary-score')?.textContent || '';
      const msgTxt = document.getElementById('d-summary-msg')?.textContent || '';
      return { scoreTxt, msgTxt };
    });

    assert.ok(standaloneCheck.scoreTxt.includes('20 / 30 CÂU'), 'Standalone Section 2 reports 20/30 questions');
    assert.ok(standaloneCheck.msgTxt.includes('độc lập cho Phần 2'), 'Standalone notice displayed');
    console.log('✅ Section isolation verified: Standalone Section 2 never inherits stale data!');

    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'session_history_regression_verified.png') });
    console.log('🎉 SESSION HISTORY & LISTENING MODALITY REGRESSION TESTS PASSED 100%!');
  } catch (err) {
    console.error('Session History Test Failed:', err);
    await browser.close();
    process.exit(1);
  }

  await browser.close();
}

testSessionHistory();
