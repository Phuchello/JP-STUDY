// scripts/tests/smoke_mock_section2.cjs
// Phase B: Automated Browser Validation for N2 Full Mock Section 2 (Listening) & 180-pt Scoring
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

async function runSection2Tests() {
  console.log('=== PHASE B: SECTION 2 LISTENING & 180-PT VERIFICATION ===');
  const browser = await chromium.launch({ headless: true });
  const results = [];

  function record(name, passed, details = '') {
    results.push({ name, passed, details });
    const mark = passed ? '✅ PASS' : '❌ FAIL';
    console.log(`${mark} | ${name} ${details ? '(' + details + ')' : ''}`);
  }

  try {
    // -------------------------------------------------------------
    // Test 1: Direct launch of Section 2 Listening (30q / 50m)
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();
      await page.goto(`${HTML_PATH}?mockId=N2-MOCK-01&section=2`);
      await page.waitForTimeout(600);

      const state = await page.evaluate(() => {
        const title = document.getElementById('timed-header-title')?.textContent || '';
        const count = timedState?.questions?.length || 0;
        const totalSec = timedState?.totalSec || 0;
        const isListening = timedState?.questions?.every(q => (q.skill || '').toLowerCase() === 'listening') || false;
        const firstMondai = timedState?.questions?.[0]?.mondai || '';
        return { title, count, totalSec, isListening, firstMondai };
      });

      assert.equal(state.count, 30, 'Section 2 must have exactly 30 questions');
      assert.equal(state.totalSec, 3000, 'Section 2 must have 50 minutes (3000 seconds)');
      assert.equal(state.isListening, true, 'All questions in Section 2 must be LISTENING category');
      record('Section 2 Direct Launch (30q / 50m Listening)', true, `count=${state.count}, totalSec=${state.totalSec}`);

      await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'phase_b_section2_launch.png'), fullPage: false });
      await context.close();
    }

    // -------------------------------------------------------------
    // Test 2: Auditory Simulation, Transcript and Options rendering
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();
      await page.goto(`${HTML_PATH}?mockId=N2-MOCK-01&section=2`);
      await page.waitForTimeout(600);

      // Check audio banner and transcript toggle
      const hasAudioBanner = await page.evaluate(() => {
        const passage = document.getElementById('d-q-passage');
        const text = passage?.textContent || '';
        const details = passage?.querySelector('details');
        return text.includes('PHẦN THI NGHE HIỂU') && Boolean(details);
      });
      assert.ok(hasAudioBanner, 'Audio banner and transcript details must be rendered');
      record('Listening Audio Simulation & Transcript UI', true, 'audio banner & transcript rendered');

      await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'phase_b_listening_transcript_view.png'), fullPage: false });
      await context.close();
    }

    // -------------------------------------------------------------
    // Test 3: Combined 180-Point Scoring & JLPT Diagnosis
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();

      // Seed Section 1 save in localStorage before launching Section 2
      await page.addInitScript(() => {
        const sec1Save = {
          mockId: 'N2-MOCK-01',
          savedAt: Date.now(),
          langCorrect: 35,
          langTotal: 54,
          langScaled: 39,
          readCorrect: 16,
          readTotal: 21,
          readScaled: 46,
          sec1Correct: 51,
          sec1Total: 75,
          sec1Scaled: 85
        };
        localStorage.setItem('JP_MOCK_SAVE_N2-MOCK-01', JSON.stringify(sec1Save));
      });

      await page.goto(`${HTML_PATH}?mockId=N2-MOCK-01&section=2`);
      await page.waitForTimeout(600);

      // Answer 24 questions correctly
      await page.evaluate(() => {
        timedState.questions.forEach((q, idx) => {
          if (idx < 24) {
            timedState.userAnswers[q.id] = q.correctAnswer;
          } else {
            timedState.userAnswers[q.id] = (q.correctAnswer === 'A' ? 'B' : 'A');
          }
        });
      });

      // Submit section 2
      await page.evaluate(() => {
        submitTimedSession();
      });
      await page.waitForTimeout(500);

      const summary = await page.evaluate(() => {
        const scoreText = document.getElementById('d-summary-score')?.textContent || '';
        const msgHtml = document.getElementById('d-summary-msg')?.innerHTML || '';
        const history = JSON.parse(localStorage.getItem('JP_STUDY_SESSIONS') || '[]');
        return { scoreText, msgHtml, historyLen: history.length, latestHistory: history[0] };
      });

      // 85 (Sec 1) + Math.round((24/30)*60 = 48) = 133 / 180
      assert.ok(summary.scoreText.includes('180 ĐIỂM'), 'Summary must show 180-point JLPT scale');
      assert.ok(summary.msgHtml.includes('BẠN ĐẠT CHUẨN ĐỖ JLPT N2'), '133/180 with all sections >= 19 must PASS');
      assert.ok(summary.msgHtml.includes('Phần 1A — Kiến thức ngôn ngữ:</strong> 39 / 60 điểm'), 'Language knowledge breakdown present');
      assert.ok(summary.msgHtml.includes('Phần 1B — Đọc hiểu:</strong> 46 / 60 điểm'), 'Reading breakdown present');
      assert.ok(summary.msgHtml.includes('Phần 2 — Nghe hiểu:</strong> 48 / 60 điểm'), 'Listening breakdown present');

      record('Combined 180-point Scoring & Pass/Fail Evaluation', true, summary.scoreText);

      await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'phase_b_full_mock_180pt_summary.png'), fullPage: false });
      await context.close();
    }

    console.log('\n=== SECTION 2 TEST SUMMARY ===');
    console.log(`Passed: ${results.filter(r => r.passed).length}/${results.length}`);
    await browser.close();
    return true;
  } catch (err) {
    console.error('Section 2 Test failed:', err);
    await browser.close();
    process.exit(1);
  }
}

runSection2Tests();
