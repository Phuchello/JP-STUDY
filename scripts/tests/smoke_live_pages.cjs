// scripts/tests/smoke_live_pages.cjs
// Live HTTPS smoke verification on GitHub Pages
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const assert = require('assert/strict');

const LIVE_CATALOG = 'https://phuchello.github.io/JP-STUDY/widgets/jlpt_exam_catalog.html';
const LIVE_ENGINE_SEC1 = 'https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mockId=N2-MOCK-01';
const LIVE_ENGINE_SEC2 = 'https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mockId=N2-MOCK-01&section=2';

const userHome = process.env.USERPROFILE || process.env.HOME || '';
const SCREENSHOT_DIR = path.join(userHome, '.gemini', 'antigravity', 'brain', '07f27e52-1325-4adc-9ec0-5c8e7670a48d', 'screenshots');

async function runLiveVerification() {
  console.log('=== VERIFYING LIVE GITHUB PAGES DEPLOYMENT ===');
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const page = await context.newPage();

  try {
    // 1. Catalog Check
    console.log('Testing live catalog:', LIVE_CATALOG);
    await page.goto(LIVE_CATALOG, { waitUntil: 'networkidle' });
    const catalogBadge = await page.evaluate(() => document.querySelector('.status-badge')?.textContent || '');
    console.log('Live Catalog Badge:', catalogBadge);
    assert.ok(catalogBadge.includes('FULL MOCK · 105 CÂU'), 'Catalog badge must include FULL MOCK · 105 CÂU');
    assert.ok(catalogBadge.includes('AUDIO PHÒNG THI'), 'Catalog badge must include AUDIO PHÒNG THI');
    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'live_deployed_n2_mock_catalog_verified.png') });

    // 2. Section 1 Launch Check
    console.log('Testing live Section 1:', LIVE_ENGINE_SEC1);
    await page.goto(LIVE_ENGINE_SEC1, { waitUntil: 'networkidle' });
    const sec1State = await page.evaluate(() => ({
      qCount: timedState.questions.length,
      totalSec: timedState.totalSec,
      timerTxt: document.getElementById('d-timer-box')?.textContent || ''
    }));
    console.log('Live Sec 1 State:', sec1State);
    assert.equal(sec1State.qCount, 75);
    assert.equal(sec1State.totalSec, 6300);
    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'live_deployed_n2_mock_sec1_verified.png') });

    // 3. Section 2 Listening Audio Check
    console.log('Testing live Section 2:', LIVE_ENGINE_SEC2);
    await page.goto(LIVE_ENGINE_SEC2, { waitUntil: 'networkidle' });
    const sec2State = await page.evaluate(() => {
      const q = timedState.questions[0];
      const audioTag = document.querySelector('#exam-audio-player');
      const details = document.querySelector('#d-q-passage details');
      return {
        qCount: timedState.questions.length,
        totalSec: timedState.totalSec,
        audioSrc: audioTag ? audioTag.currentSrc || audioTag.src : null,
        transcriptHidden: !details,
        firstQId: q?.id,
        firstQAudio: q?.audioUrl
      };
    });
    console.log('Live Sec 2 State:', sec2State);
    assert.equal(sec2State.qCount, 30);
    assert.equal(sec2State.totalSec, 3000);
    assert.equal(sec2State.transcriptHidden, true);
    assert.ok(sec2State.audioSrc.includes('N2_M1_L01.mp3'));
    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'live_deployed_n2_mock_sec2_audio_verified.png') });

    // 4. Mondai 4 3-Choice Format on Live Site
    await page.evaluate(() => {
      timedState.currentIndex = 16; // Mondai 4 Question 1
      renderTimedQuestion();
      renderTimedPalette();
    });
    await page.waitForTimeout(300);
    const m4Options = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('#d-q-options .opt-btn'));
      return btns.map(b => b.textContent.trim());
    });
    console.log('Live Mondai 4 Options:', m4Options);
    assert.equal(m4Options.length, 3);
    assert.deepEqual(m4Options, ['A１番', 'B２番', 'C３番']);
    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'live_deployed_n2_mock_m4_verified.png') });

    console.log('🎉 ALL LIVE CHECKS PASSED ON GITHUB PAGES!');
  } catch (err) {
    console.error('Live Verification Failed:', err);
    await browser.close();
    process.exit(1);
  }

  await browser.close();
}

runLiveVerification();
