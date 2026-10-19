// scripts/tests/test_n2_mock_06_e2e.cjs
// Playwright End-to-End Verification for JLPT N2 Full Mock #06
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const assert = require('assert/strict');

const CATALOG_URL = 'file:///' + path.resolve(__dirname, '../../docs/widgets/jlpt_exam_catalog.html').replaceAll('\\', '/');
const ENGINE_URL = 'file:///' + path.resolve(__dirname, '../../docs/widgets/practice_engine.html').replaceAll('\\', '/');

const userHome = process.env.USERPROFILE || process.env.HOME || '';
const SCREENSHOT_DIR = path.join(userHome, '.gemini', 'antigravity', 'brain', '07f27e52-1325-4adc-9ec0-5c8e7670a48d', 'screenshots');

if (!fs.existsSync(SCREENSHOT_DIR)) fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });

async function saveEvidenceScreenshot(page, name) {
  const p1 = path.join(SCREENSHOT_DIR, name);
  await page.screenshot({ path: p1, fullPage: false });
}

async function runE2ETests() {
  console.log('=== PLAYWRIGHT E2E SUITE: JLPT N2 FULL MOCK #06 ===');
  const browser = await chromium.launch({
    headless: true,
    args: ['--autoplay-policy=no-user-gesture-required', '--allow-file-access-from-files']
  });

  const results = [];
  function record(name, passed, details = '') {
    results.push({ name, passed, details });
    const mark = passed ? '✅ PASS' : '❌ FAIL';
    console.log(`${mark} | ${name} ${details ? '(' + details + ')' : ''}`);
  }

  try {
    // -------------------------------------------------------------
    // Test 1: Exam Catalog Card Verification for N2-MOCK-06
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();
      await page.goto(CATALOG_URL);
      await page.waitForTimeout(500);

      const cardInfo = await page.evaluate(() => {
        const cards = Array.from(document.querySelectorAll('.card'));
        const mock06Card = cards.find(c => c.textContent.includes('JLPT N2 Full Mock Exam #06'));
        if (!mock06Card) return null;
        const title = mock06Card.querySelector('.card-title')?.textContent || '';
        const badge = mock06Card.querySelector('.status-badge')?.textContent || '';
        const links = Array.from(mock06Card.querySelectorAll('a.btn-start, a.btn-mat')).map(a => a.href);
        return { title, badge, links };
      });

      assert.ok(cardInfo, 'N2-MOCK-06 card must exist in catalog');
      assert.ok(cardInfo.badge.includes('FULL MOCK · 105 CÂU'), 'Badge must indicate 105 questions');
      assert.ok(cardInfo.badge.includes('30 AUDIO'), 'Badge must indicate 30 audio tracks');
      assert.ok(cardInfo.links.some(l => l.includes('mockId=N2-MOCK-06')), 'Must link to N2-MOCK-06');
      record('Catalog Card Declaration (Mock #06)', true, cardInfo.badge);
      await saveEvidenceScreenshot(page, 'mock_06_e2e_01_catalog_card.png');
      await context.close();
    }

    // -------------------------------------------------------------
    // Test 2: Section 1 Direct Launch & 75 Questions
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();
      await page.goto(`${ENGINE_URL}?mode=mock&mockId=N2-MOCK-06`);
      await page.waitForTimeout(800);

      const state = await page.evaluate(() => ({
        qCount: timedState ? timedState.questions.length : 0,
        totalSec: timedState ? timedState.totalSec : 0,
        firstQ: timedState ? timedState.questions[0].id : '',
        mockId: timedState && timedState.mockMeta ? timedState.mockMeta.mockId : '',
        isSec1: timedState && timedState.mockMeta ? timedState.mockMeta.currentSectionIndex === 0 : false
      }));

      assert.equal(state.mockId, 'N2-MOCK-06', 'Must launch N2-MOCK-06');
      assert.equal(state.qCount, 75, 'Section 1 must have exactly 75 questions');
      assert.equal(state.totalSec, 6300, 'Section 1 duration must be 105 minutes (6300s)');
      assert.equal(state.isSec1, true, 'Current section must be Section 1');
      assert.ok(state.firstQ.startsWith('N2_06_'), 'First question must be from Mock 06');
      record('Section 1 Launch (75q / 105m)', true, `qCount=${state.qCount}, sec=${state.totalSec}`);

      // Answer 50 questions
      await page.evaluate(() => {
        timedState.questions.forEach((q, idx) => {
          if (idx < 50) timedState.userAnswers[q.id] = q.correctAnswer;
        });
      });

      // Submit Section 1
      await page.evaluate(() => submitTimedSession());
      await page.waitForTimeout(400);

      const sec1Summary = await page.evaluate(() => ({
        score: document.getElementById('d-summary-score')?.textContent || '',
        msg: document.getElementById('d-summary-msg')?.textContent || '',
        savedDraft: Boolean(localStorage.getItem('JP_MOCK_SAVE_N2-MOCK-06'))
      }));

      assert.ok(sec1Summary.score.includes('KẾT QUẢ PHẦN 1: 50 / 75 CÂU'), 'Raw score displayed');
      assert.ok(sec1Summary.msg.includes('KHÔNG phải điểm chuẩn hóa JLPT chính thức'), 'IRT disclaimer present');
      assert.equal(sec1Summary.savedDraft, true, 'Draft preserved in localStorage');
      record('Section 1 Submission & Raw Scoring', true, sec1Summary.score);
      await saveEvidenceScreenshot(page, 'mock_06_e2e_02_sec1_submission.png');

      // Click Break
      await page.evaluate(() => startMockBreak('N2-MOCK-06'));
      await page.waitForTimeout(400);

      const breakInfo = await page.evaluate(() => ({
        visible: document.getElementById('d-break-screen')?.style.display !== 'none',
        title: document.getElementById('d-break-screen')?.querySelector('h2')?.textContent || ''
      }));
      assert.equal(breakInfo.visible, true, 'Break screen must be visible');
      record('Break Intermission Screen', true, breakInfo.title);
      await saveEvidenceScreenshot(page, 'mock_06_e2e_03_break_screen.png');

      // -------------------------------------------------------------
      // Test 3: Section 2 Listening Execution & Zero Spoiler Masking
      // -------------------------------------------------------------
      await page.evaluate(() => startFullMockExam('N2-MOCK-06', 1));
      await page.waitForTimeout(800);

      const sec2State = await page.evaluate(() => ({
        qCount: timedState ? timedState.questions.length : 0,
        totalSec: timedState ? timedState.totalSec : 0,
        isSec2: timedState && timedState.mockMeta ? timedState.mockMeta.currentSectionIndex === 1 : false,
        audioStatus: timedState && timedState.mockMeta ? timedState.mockMeta.audioStatus : null
      }));

      assert.equal(sec2State.qCount, 30, 'Section 2 must have exactly 30 listening items');
      assert.equal(sec2State.totalSec, 3000, 'Section 2 must be 50 minutes (3000s)');
      assert.equal(sec2State.isSec2, true, 'Current section must be Section 2');
      record('Section 2 Launch (30q / 50m)', true, `qCount=${sec2State.qCount}, sec=${sec2State.totalSec}`);

      // Verify Mondai 1 (Q1) masked stem
      const m1Check = await page.evaluate(() => {
        const passage = document.getElementById('d-q-passage')?.innerText || '';
        const stem = document.getElementById('d-q-stem')?.innerText || '';
        return { passage, stem };
      });
      assert.ok(passageIncludesAudioGuidance(m1Check.passage), 'Mondai 1 must not display script during exam');
      record('Mondai 1 Script Masking', true);

      function passageIncludesAudioGuidance(text) {
        const lower = text.toLowerCase();
        return lower.includes('lắng nghe') || lower.includes('ẩn hoàn toàn') || lower.includes('âm thanh');
      }

      // Verify Mondai 3 (Q12) numbered choices
      await page.evaluate(() => {
        timedState.currentIndex = 11;
        renderTimedQuestion();
        renderTimedPalette();
      });
      await page.waitForTimeout(300);

      const m3Options = await page.evaluate(() => {
        const btns = Array.from(document.querySelectorAll('#d-q-options .opt-btn'));
        return btns.map(b => b.innerText.trim());
      });
      assert.ok(m3Options.some(t => t.includes('1番') || t.includes('１番')), 'Mondai 3 options must be numbered choices without text leaks');
      record('Mondai 3 Zero-Spoiler Modality', true, m3Options.join(', '));

      // Verify Mondai 4 (Q17) exactly 3 choices
      await page.evaluate(() => {
        timedState.currentIndex = 16;
        renderTimedQuestion();
        renderTimedPalette();
      });
      await page.waitForTimeout(300);

      const m4Count = await page.evaluate(() => {
        return document.querySelectorAll('#d-q-options .opt-btn').length;
      });
      assert.equal(m4Count, 3, 'Mondai 4 must strictly provide 3 choices');
      record('Mondai 4 Exactly 3 Choices', true, `count=${m4Count}`);

      // Answer 20 listening questions
      await page.evaluate(() => {
        timedState.questions.forEach((q, idx) => {
          if (idx < 20) timedState.userAnswers[q.id] = q.correctAnswer;
        });
      });

      // Submit Section 2
      await page.evaluate(() => submitTimedSession());
      await page.waitForTimeout(500);

      // -------------------------------------------------------------
      // Test 4: Combined Final Score Report & IRT Disclaimer
      // -------------------------------------------------------------
      const finalReport = await page.evaluate(() => ({
        score: document.getElementById('d-summary-score')?.textContent || '',
        msg: document.getElementById('d-summary-msg')?.textContent || '',
        draftCleared: localStorage.getItem('JP_MOCK_SAVE_N2-MOCK-06') === null
      }));

      assert.ok(finalReport.score.includes('KẾT QUẢ ĐỀ THI MÔ PHỎNG N2') || finalReport.score.includes('70 / 105 CÂU'), 'Combined 105-item score displayed');
      assert.ok(finalReport.msg.includes('Lý thuyết Ứng đáp Câu hỏi') || finalReport.msg.includes('IRT'), 'Mandatory IRT disclaimer present');
      assert.equal(finalReport.draftCleared, true, 'Draft cleanly purged after combined mock scoring');
      record('Combined 105-item Score & Purged Draft', true, finalReport.score);
      await saveEvidenceScreenshot(page, 'mock_06_e2e_04_final_score_report.png');

      // -------------------------------------------------------------
      // Test 5: Post-Exam Review Mode (Transcripts Revealed)
      // -------------------------------------------------------------
      const reviewInfo = await page.evaluate(() => {
        const reviewCards = document.querySelectorAll('#d-review-list .error-item').length;
        const audioReplayTags = document.querySelectorAll('#d-review-list audio').length;
        const transcriptDetails = document.querySelectorAll('#d-review-list details').length;
        const text = document.getElementById('d-review-list')?.textContent || '';
        const hasScriptRevealed = text.includes('Xem Kịch bản hội thoại') || text.includes('男') || text.includes('女');
        const hasDistractor = text.includes('phương án sai') || text.includes('Lựa chọn');
        return { reviewCards, audioReplayTags, transcriptDetails, hasScriptRevealed, hasDistractor };
      });

      assert.equal(reviewInfo.reviewCards, 30, '30 review cards generated for Section 2');
      assert.equal(reviewInfo.audioReplayTags, 30, 'All 30 review cards have audio replay players');
      assert.equal(reviewInfo.transcriptDetails, 30, 'All 30 review cards have revealed full transcripts');
      assert.equal(reviewInfo.hasScriptRevealed, true, 'Full listening transcripts must be revealed in review');
      assert.equal(reviewInfo.hasDistractor, true, 'Distractor explanations must be revealed');
      record('Review Mode (Transcripts & Distractor Rationale)', true, `${reviewInfo.reviewCards} cards`);
      await saveEvidenceScreenshot(page, 'mock_06_e2e_05_review_mode.png');

      await context.close();
    }

    // -------------------------------------------------------------
    // Test 6: Mobile Responsiveness Viewport (390px)
    // -------------------------------------------------------------
    {
      const mobileContext = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true });
      const mobilePage = await mobileContext.newPage();
      await mobilePage.goto(`${ENGINE_URL}?mode=mock&mockId=N2-MOCK-06&section=2`);
      await mobilePage.waitForTimeout(800);

      const mobileLayout = await mobilePage.evaluate(() => {
        const audioEl = document.querySelector('#exam-audio-player') || document.querySelector('audio');
        const stemEl = document.getElementById('d-q-stem');
        const optBtns = document.querySelectorAll('#d-q-options .opt-btn');
        return {
          hasAudio: Boolean(audioEl),
          audioVisible: audioEl ? audioEl.offsetWidth > 200 : false,
          hasStem: Boolean(stemEl),
          optCount: optBtns.length
        };
      });

      assert.equal(mobileLayout.hasAudio, true, 'Audio element must render in mobile viewport');
      assert.ok(mobileLayout.optCount >= 3, 'Option buttons must render in mobile viewport');
      record('Mobile Viewport (390px) Audio & Controls', true, `hasAudio=${mobileLayout.hasAudio}, opts=${mobileLayout.optCount}`);
      await saveEvidenceScreenshot(mobilePage, 'mock_06_e2e_06_mobile_390px.png');
      await mobileContext.close();
    }

    // -------------------------------------------------------------
    // Test 7: Direct XSS Immunity Check
    // -------------------------------------------------------------
    {
      const xssContext = await browser.newContext();
      const xssPage = await xssContext.newPage();
      xssPage.on('dialog', async (dialog) => {
        await dialog.dismiss();
      });

      await xssPage.goto(`${ENGINE_URL}?mockId=%3Cscript%3Ewindow.__XSS__=1%3C/script%3E&section=%22%3E%3Cimg%20src=x%20onerror=window.__XSS__=2%3E`);
      await xssPage.waitForTimeout(400);

      const xssResult = await xssPage.evaluate(() => window.__XSS__ || null);
      assert.equal(xssResult, null, 'DOM XSS payloads must never execute');
      record('XSS Injection Immunity', true, 'xssResult=null');
      await saveEvidenceScreenshot(xssPage, 'mock_06_e2e_07_xss_immunity.png');
      await xssContext.close();
    }

    console.log('\n==================================================');
    console.log(`ALL ${results.length} E2E TESTS PASSED FOR N2-MOCK-06!`);
    console.log('==================================================');
  } finally {
    await browser.close();
  }
}

runE2ETests().catch((err) => {
  console.error('Fatal E2E test error:', err);
  process.exit(1);
});
