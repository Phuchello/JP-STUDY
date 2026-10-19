// scripts/tests/verify_live_n2_mock_03.cjs
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const userHome = process.env.USERPROFILE || process.env.HOME || '';
const SCREENSHOT_DIR = path.join(userHome, '.gemini', 'antigravity', 'brain', '07f27e52-1325-4adc-9ec0-5c8e7670a48d', 'screenshots');
if (!fs.existsSync(SCREENSHOT_DIR)) fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });

async function verifyLiveSite() {
  console.log('=== VERIFYING LIVE GITHUB PAGES FOR N2 MOCK #03 ===');
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const page = await context.newPage();

  // 1. Catalog Page
  console.log('Loading live catalog...');
  await page.goto('https://phuchello.github.io/JP-STUDY/widgets/jlpt_exam_catalog.html', { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'live_deployed_n2_mock_03_catalog.png') });
  console.log('Saved live catalog screenshot.');

  // 2. Practice Engine Mock 03 Section 1
  console.log('Loading live practice engine Section 1...');
  await page.goto('https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mock&mockId=N2-MOCK-03', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'live_deployed_n2_mock_03_sec1.png') });
  console.log('Saved live Section 1 screenshot.');

  // 3. Practice Engine Mock 03 Section 2 (Listening)
  console.log('Loading live practice engine Section 2...');
  await page.goto('https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mock&mockId=N2-MOCK-03&section=2', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'live_deployed_n2_mock_03_sec2_audio.png') });
  console.log('Saved live Section 2 screenshot.');

  await browser.close();
  console.log('=== LIVE GITHUB PAGES VERIFIED SUCCESSFULLY ===');
}

verifyLiveSite().catch(err => {
  console.error('Error verifying live site:', err);
  process.exit(1);
});
