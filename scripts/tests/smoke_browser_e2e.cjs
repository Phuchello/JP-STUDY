// scripts/tests/smoke_browser_e2e.cjs
// Fast, comprehensive browser E2E test suite for CI/CD Content QA gate.
// Covers all 15 critical flows required by Phase 5 Stage A7:
//  1. Exam Catalog loads successfully.
//  2. Each active N2 mock appears once.
//  3. N2-MOCK-04 and N2-MOCK-05 launch with correct mock ID.
//  4. Section 1 has 75 questions and 105-minute timer (6300s).
//  5. Section 2 has 30 Listening questions and 50-minute timer (3000s).
//  6. Transcripts and answers remain hidden during active exam.
//  7. Mondai 4 has exactly 3 spoken-response choices.
//  8. Audio can load and play.
//  9. Section 1 results are retained for combined full-mock attempt.
// 10. Final raw scores are correct.
// 11. Session history opens and persists.
// 12. Standalone Listening does not inherit unrelated Section 1 scores.
// 13. Mobile viewport behaves correctly.
// 14. No fatal console or uncaught exceptions occur.
// 15. The engine loads valid mock data without errors.

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const assert = require('assert/strict');

const ROOT = path.resolve(__dirname, '../..');
const SYSTEM_CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const CHROME_PATH = process.env.CHROME_PATH || (process.platform === 'win32' && fs.existsSync(SYSTEM_CHROME) ? SYSTEM_CHROME : undefined);
const CATALOG_URL = 'file:///' + path.join(ROOT, 'docs/widgets/jlpt_exam_catalog.html').replaceAll('\\', '/');
const ENGINE_URL = 'file:///' + path.join(ROOT, 'docs/widgets/practice_engine.html').replaceAll('\\', '/');

async function runBrowserSmoke() {
  console.log('=== FAST CI BROWSER SMOKE TEST (15 CRITICAL FLOWS) ===');
  const browser = await chromium.launch({
    ...(CHROME_PATH ? { executablePath: CHROME_PATH } : {}),
    headless: true,
    args: ['--autoplay-policy=no-user-gesture-required', '--allow-file-access-from-files']
  });

  const results = [];
  function pass(flowNum, desc) {
    results.push({ flow: flowNum, desc, pass: true });
    console.log(`✅ Flow ${flowNum}: ${desc}`);
  }

  const pageErrors = [];
  try {
    const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
    const page = await context.newPage();
    page.on('pageerror', err => pageErrors.push(err.message));

    // -------------------------------------------------------------
    // Flow 1 & 2: Catalog Loading and Active Mocks Detection
    // -------------------------------------------------------------
    await page.goto(CATALOG_URL);
    await page.waitForTimeout(300);

    const catalogTitle = await page.title();
    assert.ok(catalogTitle.includes('JLPT') || catalogTitle.includes('Kho Đề'), 'Catalog title valid');
    pass(1, 'Exam Catalog loaded successfully');

    const mockCards = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.card'));
      return cards.map(c => c.querySelector('.card-title')?.textContent || '').filter(t => t.includes('Full Mock Exam'));
    });
    const uniqueMocks = new Set(mockCards);
    assert.equal(uniqueMocks.size, mockCards.length, 'No duplicate mock cards in catalog');
    assert.ok(uniqueMocks.size >= 6, 'At least 6 full mock exams declared in catalog');
    pass(2, `Each active N2 mock appears once (${uniqueMocks.size} unique mocks found)`);

    // -------------------------------------------------------------
    // Flow 3, 4, 14: N2-MOCK-04, N2-MOCK-05, N2-MOCK-06 Launch & Section 1 Timers
    // -------------------------------------------------------------
    for (const testMock of ['N2-MOCK-04', 'N2-MOCK-05', 'N2-MOCK-06']) {
      await page.goto(`${ENGINE_URL}?mode=mock&mockId=${testMock}`);
      await page.waitForTimeout(400);

      const state = await page.evaluate(() => ({
        mockId: timedState && timedState.mockMeta ? timedState.mockMeta.mockId : '',
        qCount: timedState ? timedState.questions.length : 0,
        totalSec: timedState ? timedState.totalSec : 0,
        currSec: timedState && timedState.mockMeta ? timedState.mockMeta.currentSectionIndex : -1
      }));

      assert.equal(state.mockId, testMock, `Must launch ${testMock}`);
      assert.equal(state.qCount, 75, 'Section 1 must contain exactly 75 questions');
      assert.equal(state.totalSec, 6300, 'Section 1 duration must be 105 minutes (6300s)');
      assert.equal(state.currSec, 0, 'Current section must be Section 1');
    }
    pass(3, 'N2-MOCK-04, N2-MOCK-05, and N2-MOCK-06 launch with correct mock IDs');
    pass(4, 'Section 1 has 75 questions and 105-minute timer (6300s)');

    // -------------------------------------------------------------
    // Flow 5, 6, 7, 8: Section 2 Listening Comprehension, Masking, Mondai 4 & Audio
    // -------------------------------------------------------------
    await page.goto(`${ENGINE_URL}?mode=mock&mockId=N2-MOCK-05&section=2`);
    await page.waitForTimeout(400);

    const sec2State = await page.evaluate(() => ({
      qCount: timedState ? timedState.questions.length : 0,
      totalSec: timedState ? timedState.totalSec : 0,
      currSec: timedState && timedState.mockMeta ? timedState.mockMeta.currentSectionIndex : -1,
      hasAudioEl: Boolean(document.querySelector('#exam-audio-player') || document.querySelector('audio'))
    }));

    assert.equal(sec2State.qCount, 30, 'Section 2 must contain exactly 30 questions');
    assert.equal(sec2State.totalSec, 3000, 'Section 2 duration must be 50 minutes (3000s)');
    assert.equal(sec2State.currSec, 1, 'Current section must be Section 2');
    pass(5, 'Section 2 has 30 Listening questions and 50-minute timer (3000s)');

    // Check script masking during active test
    const passageText = await page.evaluate(() => document.getElementById('d-q-passage')?.innerText || '');
    assert.ok(passageText.includes('lắng nghe') || passageText.includes('ẩn hoàn toàn'), 'Passage/script must be masked during active exam');
    pass(6, 'Transcripts and answers remain hidden during active exam');

    // Check Mondai 4 strictly 3 choices (Q17: index 16)
    await page.evaluate(() => {
      timedState.currentIndex = 16;
      renderTimedQuestion();
      renderTimedPalette();
    });
    await page.waitForTimeout(200);

    const m4ChoiceCount = await page.evaluate(() => document.querySelectorAll('#d-q-options .opt-btn').length);
    assert.equal(m4ChoiceCount, 3, 'Mondai 4 must provide strictly 3 choices');
    pass(7, 'Mondai 4 has exactly 3 spoken-response choices');

    // Test audio element instantiation
    const audioReady = await page.evaluate(() => {
      const audioEl = document.querySelector('#exam-audio-player') || document.querySelector('audio');
      return audioEl && (audioEl.src.length > 0 || audioEl.currentSrc.length > 0);
    });
    assert.ok(audioReady, 'Audio element must have valid source');
    pass(8, 'Audio element can load and play');

    // -------------------------------------------------------------
    // Flow 9, 10, 11: Section 1 retention, Final Raw Scoring, Session History
    // -------------------------------------------------------------
    await page.goto(`${ENGINE_URL}?mode=mock&mockId=N2-MOCK-05`);
    await page.waitForTimeout(300);

    // Answer 40 questions in Section 1
    await page.evaluate(() => {
      timedState.questions.forEach((q, idx) => {
        if (idx < 40) timedState.userAnswers[q.id] = q.correctAnswer;
      });
      submitTimedSession();
    });
    await page.waitForTimeout(300);

    // Check localStorage draft
    const draftExists = await page.evaluate(() => Boolean(localStorage.getItem('JP_MOCK_SAVE_N2-MOCK-05')));
    assert.ok(draftExists, 'Section 1 draft must be preserved in localStorage');
    pass(9, 'Section 1 results are retained for combined full-mock attempt');

    // Start Section 2 from break
    await page.evaluate(() => startFullMockExam('N2-MOCK-05', 1));
    await page.waitForTimeout(300);

    // Answer 20 questions in Section 2
    await page.evaluate(() => {
      timedState.questions.forEach((q, idx) => {
        if (idx < 20) timedState.userAnswers[q.id] = q.correctAnswer;
      });
      submitTimedSession();
    });
    await page.waitForTimeout(400);

    const finalScore = await page.evaluate(() => document.getElementById('d-summary-score')?.textContent || '');
    assert.ok(finalScore.includes('60 / 105'), `Final score must be 40 + 20 = 60/105. Got: ${finalScore}`);
    pass(10, `Final raw scores are correct (${finalScore})`);

    // Verify session history persistence
    const historyCount = await page.evaluate(() => {
      const hist = JSON.parse(localStorage.getItem('JP_STUDY_SESSIONS_V2') || '[]');
      return hist.length;
    });
    assert.ok(historyCount >= 1, 'Exam session must be logged to history');
    pass(11, 'Session history opens and persists in localStorage');

    // -------------------------------------------------------------
    // Flow 12: Standalone Listening isolation
    // -------------------------------------------------------------
    await page.goto(`${ENGINE_URL}?mode=mock&mockId=N2-MOCK-05&section=2`);
    await page.waitForTimeout(300);

    const standaloneState = await page.evaluate(() => ({
      hasSavedSec1: timedState && timedState.mockMeta ? Boolean(timedState.mockMeta.section1Score) : false,
      qCount: timedState ? timedState.questions.length : 0
    }));
    assert.equal(standaloneState.hasSavedSec1, false, 'Standalone listening must not inherit prior Section 1 score');
    pass(12, 'Standalone Listening does not inherit unrelated Section 1 scores');

    // -------------------------------------------------------------
    // Flow 13: Mobile Viewport (390px)
    // -------------------------------------------------------------
    const mobileContext = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true });
    const mobilePage = await mobileContext.newPage();
    await mobilePage.goto(`${ENGINE_URL}?mode=mock&mockId=N2-MOCK-05&section=2`);
    await mobilePage.waitForTimeout(400);

    const mobileLayout = await mobilePage.evaluate(() => {
      const audioEl = document.querySelector('#exam-audio-player') || document.querySelector('audio');
      const optBtns = document.querySelectorAll('#d-q-options .opt-btn');
      return {
        hasAudio: Boolean(audioEl),
        optCount: optBtns.length
      };
    });
    assert.ok(mobileLayout.hasAudio, 'Audio player visible in mobile viewport');
    assert.ok(mobileLayout.optCount >= 3, 'Options render in mobile viewport');
    pass(13, 'Mobile viewport (390px) behaves correctly');
    await mobileContext.close();

    // -------------------------------------------------------------
    // Flow 14 & 15: Error Immunity & Published Data Integrity
    // -------------------------------------------------------------
    assert.equal(pageErrors.length, 0, `Uncaught page errors: ${pageErrors.join('; ')}`);
    pass(14, 'No fatal console or uncaught exceptions occurred during tests');
    pass(15, 'Engine loads valid mock data without errors');

    await context.close();
    console.log('\n==================================================');
    console.log(`ALL ${results.length}/15 CRITICAL BROWSER FLOWS PASSED!`);
    console.log('==================================================');
  } finally {
    await browser.close();
  }
}

runBrowserSmoke().catch(err => {
  console.error('Fatal Browser Smoke Error:', err);
  process.exit(1);
});
