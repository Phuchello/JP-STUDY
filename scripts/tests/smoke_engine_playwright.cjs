// scripts/tests/smoke_engine_playwright.cjs
// Phase A: Automated Browser Smoke Test for Practice Engine
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const assert = require('assert/strict');

const HTML_PATH = 'file:///' + path.resolve(__dirname, '../../docs/widgets/practice_engine.html').replaceAll('\\', '/');
const userHome = process.env.USERPROFILE || process.env.HOME || '';
const SCREENSHOT_DIR = path.join(userHome, '.gemini', 'antigravity', 'brain', '07f27e52-1325-4adc-9ec0-5c8e7670a48d', 'screenshots');

if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

async function runSmokeTests() {
  console.log('=== PHASE A: BROWSER AUTOMATION SMOKE TESTS ===');
  console.log('Target URL:', HTML_PATH);

  const browser = await chromium.launch({ headless: true });
  const results = [];
  const errors = [];

  function record(name, passed, details = '') {
    results.push({ name, passed, details });
    const mark = passed ? '✅ PASS' : '❌ FAIL';
    console.log(`${mark} | ${name} ${details ? '(' + details + ')' : ''}`);
    if (!passed) errors.push({ name, details });
  }

  try {
    // -------------------------------------------------------------
    // Test 1: N2-MOCK-01 directly opens 75 questions
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();
      await page.goto(`${HTML_PATH}?mockId=N2-MOCK-01`);
      await page.waitForTimeout(500);

      const state = await page.evaluate(() => ({
        arenaDisplay: document.getElementById('d-arena').style.display,
        configDisplay: document.getElementById('d-config').style.display,
        progress: document.getElementById('d-progress-txt').innerText,
        timer: document.getElementById('d-timer-box').innerText,
        qCount: timedState ? timedState.questions.length : 0,
        isMock: timedState && timedState.mockMeta ? timedState.mockMeta.isMock : false,
        mockId: timedState && timedState.mockMeta ? timedState.mockMeta.mockId : null,
        totalSec: timedState ? timedState.totalSec : 0,
        allN2: timedState ? timedState.questions.every(q => q.level === 'N2') : false
      }));

      await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'phase_a_n2_mock_01_launch.png') });

      record(
        'N2-MOCK-01 Direct Launch (75 questions / 105 mins)',
        state.arenaDisplay === 'block' && state.qCount === 75 && state.allN2 && state.totalSec === 6300,
        `qCount=${state.qCount}, totalSec=${state.totalSec}, allN2=${state.allN2}`
      );
      await context.close();
    }

    // -------------------------------------------------------------
    // Test 2: N3-MOCK-01 directly opens 73 questions
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();
      await page.goto(`${HTML_PATH}?mockId=N3-MOCK-01`);
      await page.waitForTimeout(500);

      const state = await page.evaluate(() => ({
        arenaDisplay: document.getElementById('d-arena').style.display,
        configDisplay: document.getElementById('d-config').style.display,
        progress: document.getElementById('d-progress-txt').innerText,
        timer: document.getElementById('d-timer-box').innerText,
        qCount: timedState ? timedState.questions.length : 0,
        isMock: timedState && timedState.mockMeta ? timedState.mockMeta.isMock : false,
        mockId: timedState && timedState.mockMeta ? timedState.mockMeta.mockId : null,
        totalSec: timedState ? timedState.totalSec : 0,
        allN3: timedState ? timedState.questions.every(q => q.level === 'N3') : false
      }));

      await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'phase_a_n3_mock_01_launch.png') });

      record(
        'N3-MOCK-01 Direct Launch (73 questions / 100 mins)',
        state.arenaDisplay === 'block' && state.qCount === 73 && state.allN3 && state.totalSec === 6000,
        `qCount=${state.qCount}, totalSec=${state.totalSec}, allN3=${state.allN3}`
      );
      await context.close();
    }

    // -------------------------------------------------------------
    // Test 3: N2/N3/Marathon presets have correct question counts, levels and durations
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();

      // N2 preset: 30q / 35m
      await page.goto(`${HTML_PATH}?mode=mode-d&level=N2&count=30&duration=35`);
      await page.evaluate(() => startTimedSession());
      const n2State = await page.evaluate(() => ({
        qCount: timedState.questions.length,
        totalSec: timedState.totalSec,
        allLevel: timedState.questions.every(q => q.level === 'N2')
      }));
      await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'phase_a_n2_preset_30q_35m.png') });
      record('N2 Preset (30q / 35m)', n2State.qCount === 30 && n2State.totalSec === 2100 && n2State.allLevel);

      // N3 preset: 30q / 30m
      await page.goto(`${HTML_PATH}?mode=mode-d&level=N3&count=30&duration=30`);
      await page.evaluate(() => startTimedSession());
      const n3State = await page.evaluate(() => ({
        qCount: timedState.questions.length,
        totalSec: timedState.totalSec,
        allLevel: timedState.questions.every(q => q.level === 'N3')
      }));
      await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'phase_a_n3_preset_30q_30m.png') });
      record('N3 Preset (30q / 30m)', n3State.qCount === 30 && n3State.totalSec === 1800 && n3State.allLevel);

      // Marathon preset: 50q / 60m MIXED
      await page.goto(`${HTML_PATH}?mode=mode-d&level=MIXED&count=50&duration=60`);
      await page.evaluate(() => startTimedSession());
      const maraState = await page.evaluate(() => ({
        qCount: timedState.questions.length,
        totalSec: timedState.totalSec,
        allLevel: timedState.questions.every(q => ['N2', 'N3'].includes(q.level))
      }));
      await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'phase_a_marathon_preset.png') });
      record('Marathon Preset (50q / 60m MIXED)', maraState.qCount === 50 && maraState.totalSec === 3600 && maraState.allLevel);

      // Incompatible custom combo normalized
      await page.goto(`${HTML_PATH}?mode=mode-d&level=N2&count=50&duration=15`);
      await page.evaluate(() => startTimedSession());
      const incompState = await page.evaluate(() => ({
        qCount: timedState.questions.length,
        totalSec: timedState.totalSec,
        badge: document.getElementById('param-config-badge').innerText
      }));
      record(
        'Incompatible Configuration Normalization (count 50 vs duration 15)',
        incompState.qCount === 15 && incompState.totalSec === 900 && incompState.badge.includes('không tương thích'),
        `Normalized to ${incompState.qCount} questions / ${incompState.totalSec / 60} mins`
      );

      await context.close();
    }

    // -------------------------------------------------------------
    // Test 4: Timer, answer navigation, submission, scoring, and history
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();
      await page.goto(`${HTML_PATH}?mode=mode-d&level=N2&count=15&duration=15`);
      await page.evaluate(() => startTimedSession());

      // Answer Question 1
      const q1Id = await page.evaluate(() => timedState.questions[0].id);
      await page.locator('#d-q-options .opt-btn').first().click();

      const answeredPill1 = await page.evaluate(() => {
        const p1 = document.querySelector('#d-palette .pill-num');
        return p1 ? p1.classList.contains('answered') : false;
      });
      record('Answer selection marks palette pill answered', answeredPill1);

      // Next question navigation
      await page.evaluate(() => nextTimedQuestion());
      const curNumAfterNext = await page.evaluate(() => timedState.currentIndex);
      record('Question navigation forward', curNumAfterNext === 1);

      // Prev question navigation
      await page.evaluate(() => prevTimedQuestion());
      const curNumAfterPrev = await page.evaluate(() => timedState.currentIndex);
      record('Question navigation backward', curNumAfterPrev === 0);

      // Submission and scoring
      await page.evaluate(() => submitTimedSession(false));
      const summaryVisible = await page.evaluate(() => document.getElementById('d-summary').style.display === 'block');
      const scoreTxt = await page.evaluate(() => document.getElementById('d-summary-score').innerText);
      await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'phase_a_submission_summary.png') });
      record('Submission reveals summary', summaryVisible && scoreTxt.includes('/ 15'), `score=${scoreTxt}`);

      // History persistence
      await page.evaluate(() => switchMode('mode-history'));
      await page.waitForTimeout(300);
      await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'phase_a_session_history.png') });

      const historyCheck = await page.evaluate(() => {
        const sessions = getStoredSessions();
        const s0 = sessions[0];
        return {
          hasHistory: sessions.length > 0,
          mode: s0 ? s0.mode : null,
          level: s0 ? s0.level : null,
          total: s0 ? s0.totalQuestions : null,
          hasCompletionTime: s0 && !!s0.completionTime
        };
      });
      record(
        'Session recorded into localStorage history',
        historyCheck.hasHistory && historyCheck.total === 15 && historyCheck.hasCompletionTime,
        `mode=${historyCheck.mode}, level=${historyCheck.level}`
      );

      await context.close();
    }

    // -------------------------------------------------------------
    // Test 5: Malicious URL parameters do not execute HTML or JavaScript (DOM XSS Immunity)
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();

      const xssUrl = `${HTML_PATH}?mode=mode-d&level=%3Cimg%20src=x%20onerror=window.XSS_TRIGGERED=1%3E&skill=%3Csvg/onload=window.XSS_TRIGGERED=2%3E&count=%3Cscript%3Ewindow.XSS_TRIGGERED=3%3C/script%3E&duration=999%3Cimg%20src=x%20onerror=window.XSS_TRIGGERED=4%3E`;
      await page.goto(xssUrl);
      await page.waitForTimeout(500);

      const xssState = await page.evaluate(() => ({
        xssExecuted: window.XSS_TRIGGERED || null,
        badgeImgCount: document.getElementById('param-config-badge').querySelectorAll('img').length,
        badgeScriptCount: document.getElementById('param-config-badge').querySelectorAll('script').length,
        badgeSvgCount: document.getElementById('param-config-badge').querySelectorAll('svg').length,
        badgeText: document.getElementById('param-config-badge').innerText
      }));

      await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'phase_a_xss_immunity.png') });

      record(
        'XSS Injection Immunity',
        xssState.xssExecuted === null && xssState.badgeImgCount === 0 && xssState.badgeScriptCount === 0 && xssState.badgeSvgCount === 0,
        `xssExecuted=${xssState.xssExecuted}, imgCount=${xssState.badgeImgCount}`
      );

      await context.close();
    }

    // -------------------------------------------------------------
    // Test 6: Mobile layout remains functional (390x844)
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
      const page = await context.newPage();
      await page.goto(`${HTML_PATH}?mockId=N2-MOCK-01`);
      await page.waitForTimeout(500);

      const mobileState = await page.evaluate(() => {
        const noHorizOverflow = document.documentElement.scrollWidth <= innerWidth + 2;
        const arenaVisible = document.getElementById('d-arena').style.display === 'block';
        const timerBox = document.getElementById('d-timer-box').innerText;
        const progressBox = document.getElementById('d-progress-txt').innerText;
        const firstOpt = document.querySelector('#d-q-options .opt-btn');
        const optHeight = firstOpt ? firstOpt.getBoundingClientRect().height : 0;

        return {
          noHorizOverflow,
          arenaVisible,
          timerBox,
          progressBox,
          optHeight,
          touchTargetOk: optHeight >= 40
        };
      });

      await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'phase_a_mobile_390px.png') });

      record(
        'Mobile Layout Responsiveness (390px Viewport)',
        mobileState.noHorizOverflow && mobileState.arenaVisible && mobileState.touchTargetOk,
        `noOverflow=${mobileState.noHorizOverflow}, optHeight=${mobileState.optHeight}px`
      );

      await context.close();
    }

  } catch (err) {
    console.error('Smoke test error:', err);
    errors.push({ name: 'Exception during smoke test', details: err.message });
  } finally {
    await browser.close();
  }

  console.log('\n=== SMOKE TEST SUMMARY ===');
  console.log(`Total Scenarios: ${results.length}`);
  console.log(`Passed: ${results.filter(r => r.passed).length}`);
  console.log(`Failed: ${results.filter(r => !r.passed).length}`);

  if (errors.length > 0) {
    console.error('Failures encountered:', errors);
    process.exit(1);
  } else {
    console.log('All automated browser acceptance smoke tests PASSED.');
  }
}

runSmokeTests();
