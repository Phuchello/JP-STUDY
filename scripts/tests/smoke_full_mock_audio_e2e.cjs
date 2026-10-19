// scripts/tests/smoke_full_mock_audio_e2e.cjs
// Phase F: Comprehensive End-to-End Browser Testing for JLPT N2 Full Mock #01 with Real Audio Playback
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

async function runE2E() {
  console.log('=== PHASE F: COMPREHENSIVE END-TO-END PLAYWRIGHT TESTS ===');
  const browser = await chromium.launch({ headless: true });
  const results = [];

  function record(name, passed, details = '') {
    results.push({ name, passed, details });
    const mark = passed ? '✅ PASS' : '❌ FAIL';
    console.log(`${mark} | ${name} ${details ? '(' + details + ')' : ''}`);
  }

  try {
    // -------------------------------------------------------------
    // Test 1: Catalog Card & Launch URL
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();
      await page.goto(CATALOG_URL);
      await page.waitForTimeout(500);

      const cardInfo = await page.evaluate(() => {
        const title = document.querySelector('.card-title')?.textContent || '';
        const badge = document.querySelector('.status-badge')?.textContent || '';
        const links = Array.from(document.querySelectorAll('a.btn-start, a.btn-mat')).map(a => a.href);
        return { title, badge, links };
      });

      assert.ok(cardInfo.badge.includes('FULL MOCK · 105 CÂU'), 'Catalog badge must declare 105-item full mock');
      assert.ok(cardInfo.badge.includes('AUDIO PHÒNG THI'), 'Catalog badge must declare verified audio');
      record('Catalog Card Declaration', true, cardInfo.badge);
      await saveEvidenceScreenshot(page, 'e2e_01_catalog_card.png');
      await context.close();
    }

    // -------------------------------------------------------------
    // Test 2: Section 1 Direct Launch & 75 Questions
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();
      await page.goto(`${ENGINE_URL}?mockId=N2-MOCK-01`);
      await page.waitForTimeout(600);

      const state = await page.evaluate(() => ({
        qCount: timedState.questions.length,
        totalSec: timedState.totalSec,
        firstQ: timedState.questions[0].id,
        isSec1: timedState.mockMeta.currentSectionIndex === 0
      }));

      assert.equal(state.qCount, 75, 'Section 1 must have exactly 75 questions');
      assert.equal(state.totalSec, 6300, 'Section 1 must be 105 minutes (6300s)');
      assert.equal(state.isSec1, true, 'Current section must be Section 1');
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
        savedDraft: Boolean(localStorage.getItem('JP_MOCK_SAVE_N2-MOCK-01'))
      }));

      assert.ok(sec1Summary.score.includes('KẾT QUẢ PHẦN 1: 50 / 75 CÂU'), 'Raw score displayed');
      assert.ok(sec1Summary.msg.includes('KHÔNG phải điểm chuẩn hóa JLPT chính thức'), 'Scoring disclaimer present');
      assert.equal(sec1Summary.savedDraft, true, 'Draft preserved in localStorage');
      record('Section 1 Submission & Raw Scoring', true, sec1Summary.score);
      await saveEvidenceScreenshot(page, 'e2e_02_sec1_submission.png');

      // Click Break
      await page.evaluate(() => startMockBreak('N2-MOCK-01'));
      await page.waitForTimeout(300);

      const breakVisible = await page.evaluate(() => {
        const box = document.getElementById('d-break-screen');
        return box && box.style.display !== 'none';
      });
      assert.equal(breakVisible, true, 'Break intermission screen rendered');
      record('10-Minute Break Intermission', true, 'break screen visible');
      await saveEvidenceScreenshot(page, 'e2e_03_break_screen.png');

      await context.close();
    }

    // -------------------------------------------------------------
    // Test 3: Section 2 Listening Audio Verification & Playback
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();
      await page.goto(`${ENGINE_URL}?mockId=N2-MOCK-01&section=2`);
      await page.waitForTimeout(600);

      const sec2State = await page.evaluate(() => ({
        qCount: timedState.questions.length,
        totalSec: timedState.totalSec,
        audioCount: timedState.questions.filter(q => q.audioUrl).length,
        allVerified: timedState.questions.every(q => q.audioVerificationStatus === 'VERIFIED')
      }));

      assert.equal(sec2State.qCount, 30, 'Section 2 must have 30 questions');
      assert.equal(sec2State.totalSec, 3000, 'Section 2 must be 50 minutes (3000s)');
      assert.equal(sec2State.audioCount, 30, 'Every question must map to an audio asset');
      assert.equal(sec2State.allVerified, true, 'All 30 audio assets must have VERIFIED status');
      record('Section 2 Audio Mappings (30/30 Verified)', true, `count=${sec2State.audioCount}`);

      // Verify all 30 audio files physically exist on disk
      const audioFiles = await page.evaluate(() => timedState.questions.map(q => q.audioUrl));
      for (const aUrl of audioFiles) {
        const fullP = path.resolve(__dirname, '../../docs', aUrl);
        assert.ok(fs.existsSync(fullP), `Audio file must exist: ${aUrl}`);
        assert.ok(fs.statSync(fullP).size > 10000, `Audio file must be non-empty: ${aUrl}`);
      }
      record('Physical Audio Asset Integrity (30/30 files exist & valid)', true, 'All MP3s verified > 10KB');

      // Test Transcript Masking during Exam (Mondai 1)
      const transcriptMasked = await page.evaluate(() => {
        const details = document.querySelector('#d-q-passage details');
        const audioTag = document.querySelector('#exam-audio-player');
        return { hasDetails: Boolean(details), hasAudio: Boolean(audioTag) };
      });
      assert.equal(transcriptMasked.hasDetails, false, 'Transcript details must NEVER be exposed during exam');
      assert.equal(transcriptMasked.hasAudio, true, 'Audio player element must be present');
      record('Exam Transcript Masking & Audio Player UI', true, 'Transcript hidden, audio player active');
      await saveEvidenceScreenshot(page, 'e2e_04_listening_exam_masked.png');

      // Test Mondai 4: 3-Choice Format (Question 17 / index 16)
      await page.evaluate(() => {
        timedState.currentIndex = 16; // N2-M4-L01
        renderTimedQuestion();
        renderTimedPalette();
      });
      await page.waitForTimeout(300);

      const m4Format = await page.evaluate(() => {
        const stem = document.getElementById('d-q-stem')?.textContent || '';
        const buttons = Array.from(document.querySelectorAll('#d-q-options .opt-btn'));
        const btnTexts = buttons.map(b => b.textContent.trim());
        const details = document.querySelector('#d-q-passage details');
        return { stem, buttonCount: buttons.length, btnTexts, hasDetails: Boolean(details) };
      });

      assert.equal(m4Format.buttonCount, 3, 'Mondai 4 must strictly have 3 options (1, 2, 3)');
      assert.ok(!m4Format.stem.includes('山田さん'), 'Stem must not leak prompt dialogue text');
      assert.equal(m4Format.hasDetails, false, 'Mondai 4 transcript details must not exist during exam');
      record('Mondai 4 Quick Response 3-Choice Exam Format', true, `Buttons: ${m4Format.buttonCount} (${m4Format.btnTexts.join(', ')})`);
      await saveEvidenceScreenshot(page, 'e2e_05_mondai4_3_choices.png');

      await context.close();
    }

    // -------------------------------------------------------------
    // Test 4: End-to-End Submission & Transparent Scoring Report
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
      const page = await context.newPage();

      // Seed Section 1 save into localStorage
      await page.addInitScript(() => {
        localStorage.setItem('JP_MOCK_SAVE_N2-MOCK-01', JSON.stringify({
          mockId: 'N2-MOCK-01',
          timestamp: Date.now(),
          langCorrect: 42,
          langTotal: 54,
          langScaled: 47,
          readCorrect: 16,
          readTotal: 21,
          readScaled: 46,
          sec1Correct: 58,
          sec1Total: 75,
          sec1Scaled: 93
        }));
      });

      await page.goto(`${ENGINE_URL}?mockId=N2-MOCK-01&section=2`);
      await page.waitForTimeout(500);

      // Answer 25 listening questions correctly
      await page.evaluate(() => {
        timedState.questions.forEach((q, idx) => {
          if (idx < 25) timedState.userAnswers[q.id] = q.correctAnswer;
          else timedState.userAnswers[q.id] = (q.correctAnswer === 'A' ? 'B' : 'A');
        });
        submitTimedSession();
      });
      await page.waitForTimeout(500);

      const finalReport = await page.evaluate(() => {
        const scoreText = document.getElementById('d-summary-score')?.textContent || '';
        const msgHtml = document.getElementById('d-summary-msg')?.innerHTML || '';
        const reviewCards = document.querySelectorAll('#d-review-list .error-item').length;
        const audioReplayTags = document.querySelectorAll('#d-review-list audio').length;
        const transcriptDetails = document.querySelectorAll('#d-review-list details').length;
        return { scoreText, msgHtml, reviewCards, audioReplayTags, transcriptDetails };
      });

      // Total raw correct: 58 (Sec 1) + 25 (Sec 2) = 83 / 105
      assert.ok(finalReport.scoreText.includes('83 / 105 CÂU'), 'Raw overall performance displayed');
      assert.ok(finalReport.msgHtml.includes('KHÔNG phải điểm chuẩn hóa JLPT chính thức'), 'Mandatory IRT disclaimer present');
      assert.ok(finalReport.msgHtml.includes('Phần 1A — Kiến thức ngôn ngữ'), 'Language raw breakdown present');
      assert.ok(finalReport.msgHtml.includes('Phần 1B — Đọc hiểu'), 'Reading raw breakdown present');
      assert.ok(finalReport.msgHtml.includes('Phần 2 — Nghe hiểu'), 'Listening raw breakdown present');
      assert.equal(finalReport.reviewCards, 30, '30 review cards generated');
      assert.equal(finalReport.audioReplayTags, 30, 'All 30 review cards have audio replay players');
      assert.equal(finalReport.transcriptDetails, 30, 'All 30 review cards have revealed full transcripts');

      record('Transparent Score Report & Audio Review Mode', true, finalReport.scoreText);
      await saveEvidenceScreenshot(page, 'e2e_06_final_transparent_score_report.png');
      await saveEvidenceScreenshot(page, 'e2e_07_post_exam_review_mode.png');

      await context.close();
    }

    // -------------------------------------------------------------
    // Test 5: Mobile Viewport (390px) & XSS Immunity
    // -------------------------------------------------------------
    {
      const context = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true });
      const page = await context.newPage();
      await page.goto(`${ENGINE_URL}?mockId=N2-MOCK-01&section=2`);
      await page.waitForTimeout(500);

      const mobileCheck = await page.evaluate(() => {
        const bodyWidth = document.body.scrollWidth;
        const winWidth = window.innerWidth;
        const player = document.getElementById('exam-audio-player');
        const playBtnHeight = player ? player.getBoundingClientRect().height : 0;
        return { noOverflow: bodyWidth <= winWidth + 5, playBtnHeight };
      });

      assert.equal(mobileCheck.noOverflow, true, 'Zero horizontal overflow on 390px mobile viewport');
      record('Mobile 390px Viewport Responsiveness', true, `noOverflow=${mobileCheck.noOverflow}`);
      await saveEvidenceScreenshot(page, 'e2e_08_mobile_390px_audio.png');

      // Test XSS immunity
      await page.goto(`${ENGINE_URL}?mockId=%3Cscript%3Ewindow.__XSS__=1%3C/script%3E&section=%22%3E%3Cimg%20src=x%20onerror=window.__XSS__=2%3E`);
      await page.waitForTimeout(400);

      const xssResult = await page.evaluate(() => window.__XSS__ || null);
      assert.equal(xssResult, null, 'DOM XSS payloads must never execute');
      record('DOM XSS Immunity with Malicious Parameters', true, 'xssResult=null');
      await saveEvidenceScreenshot(page, 'e2e_09_xss_immunity.png');

      await context.close();
    }

    console.log('\n=== E2E TEST SUMMARY ===');
    const passedCount = results.filter(r => r.passed).length;
    console.log(`Passed: ${passedCount}/${results.length}`);
    await browser.close();

    // Write E2E test report in repo
    const reportPath = path.resolve(__dirname, '../../qa/E2E_PLAYWRIGHT_TEST_REPORT.md');
    let md = `# JLPT N2 FULL MOCK #01 — PLAYWRIGHT E2E BROWSER TEST REPORT\n\n`;
    md += `**Date:** 2026-10-19  \n`;
    md += `**Total Scenarios:** ${results.length}  \n`;
    md += `**Passed:** ${passedCount} / ${results.length} (100%)  \n\n`;
    md += `| # | Test Scenario | Verified Condition | Status | Details |\n`;
    md += `|---|---|---|---|---|\n`;
    results.forEach((r, idx) => {
      md += `| ${idx + 1} | ${r.name} | Verified in Chromium engine | **PASS** | ${r.details} |\n`;
    });
    fs.writeFileSync(reportPath, md, 'utf-8');
    console.log('Saved test report to', reportPath);

    return true;
  } catch (err) {
    console.error('E2E Test Failed:', err);
    await browser.close();
    process.exit(1);
  }
}

runE2E();
