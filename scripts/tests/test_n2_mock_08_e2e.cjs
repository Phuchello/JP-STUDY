// Focused browser E2E for N2-MOCK-08. The catalog card intentionally remains
// unpublished while this test exercises the locally integrated exam data.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const assert = require('assert/strict');

const ROOT = path.resolve(__dirname, '../..');
const ENGINE_URL = 'file:///' + path.join(ROOT, 'docs/widgets/practice_engine.html').replaceAll('\\', '/') + '?mode=mock&mockId=N2-MOCK-08';
const CATALOG_URL = 'file:///' + path.join(ROOT, 'docs/widgets/jlpt_exam_catalog.html').replaceAll('\\', '/');
const REPORT_PATH = path.join(ROOT, 'qa/N2_MOCK_08_E2E_REPORT.json');
const SYSTEM_CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const CHROME_PATH = process.env.CHROME_PATH || (process.platform === 'win32' && fs.existsSync(SYSTEM_CHROME) ? SYSTEM_CHROME : undefined);

async function main() {
  const browser = await chromium.launch({
    ...(CHROME_PATH ? { executablePath: CHROME_PATH } : {}),
    headless: true,
    args: ['--autoplay-policy=no-user-gesture-required', '--allow-file-access-from-files']
  });
  const checks = [];
  const pageErrors = [];
  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const page = await context.newPage();
  page.on('pageerror', error => pageErrors.push(error.message));
  function pass(name, details) { checks.push({ name, passed: true, details }); console.log(`PASS ${name}: ${details}`); }

  try {
    await page.goto(CATALOG_URL);
    const m08Card = page.locator('.card').filter({
      has: page.getByText('JLPT N2 | Full Mock Exam #08', { exact: true })
    });
    assert.equal(await m08Card.count(), 1);
    const catalogLinks = await m08Card.locator('a').evaluateAll(links => links.map(a => a.href));
    assert.ok(catalogLinks.some(href => href.includes('mode=mock&mockId=N2-MOCK-08')));
    assert.ok(catalogLinks.some(href => href.includes('mockId=N2-MOCK-08&section=2')));
    assert.match(await m08Card.innerText(), /PRACTICE MOCK|AI REVIEWED/);
    pass('catalog_entry_and_responder_links', JSON.stringify(catalogLinks));

    await page.goto(ENGINE_URL);
    await page.waitForFunction(() => typeof timedState !== 'undefined' && timedState.questions.length === 75, null, { timeout: 10000 });
    const sec1 = await page.evaluate(() => ({
      mockId: timedState.mockMeta?.mockId,
      count: timedState.questions.length,
      duration: timedState.totalSec,
      section: timedState.mockMeta?.currentSectionIndex,
      firstId: timedState.questions[0]?.id
    }));
    assert.equal(sec1.mockId, 'N2-MOCK-08');
    assert.equal(sec1.count, 75);
    assert.equal(sec1.duration, 6300);
    assert.equal(sec1.section, 0);
    assert.ok(sec1.firstId.startsWith('N2_08_'));
    pass('section_1_launch', JSON.stringify(sec1));

    await page.evaluate(() => {
      const language = timedState.questions.filter(q => q.skill !== 'Reading');
      const reading = timedState.questions.filter(q => q.skill === 'Reading');
      [...language.slice(0, 47), ...reading.slice(0, 3)].forEach(q => { timedState.userAnswers[q.id] = q.correctAnswer; });
      submitTimedSession();
    });
    await page.waitForFunction(() => (document.getElementById('d-summary-score')?.textContent || '').includes('50 / 75 CÂU'), null, { timeout: 5000 });
    const sec1Score = await page.evaluate(() => ({
      score: document.getElementById('d-summary-score')?.textContent || '',
      savedDraft: Boolean(localStorage.getItem('JP_MOCK_SAVE_N2-MOCK-08'))
    }));
    assert.equal(sec1Score.savedDraft, true);
    pass('section_1_scoring_and_draft', JSON.stringify(sec1Score));

    await page.evaluate(() => startMockBreak('N2-MOCK-08'));
    const breakVisible = await page.evaluate(() => document.getElementById('d-break-screen')?.style.display !== 'none');
    assert.equal(breakVisible, true);
    pass('break_screen', 'break is visible after Section 1');

    await page.evaluate(() => startFullMockExam('N2-MOCK-08', 1));
    await page.waitForFunction(() => typeof timedState !== 'undefined' && timedState.questions?.length === 30 && timedState.mockMeta?.currentSectionIndex === 1, null, { timeout: 10000 });
    const sec2 = await page.evaluate(() => ({
      count: timedState.questions.length,
      duration: timedState.totalSec,
      section: timedState.mockMeta?.currentSectionIndex,
      audioUrl: timedState.questions[0]?.audioUrl,
      mondai4Index: timedState.questions.findIndex(q => q.id.includes('_M4_'))
    }));
    assert.equal(sec2.count, 30);
    assert.equal(sec2.duration, 3000);
    assert.equal(sec2.section, 1);
    assert.ok(sec2.audioUrl.startsWith('audio/n2_mock_08/'));
    pass('section_2_launch_and_audio_mapping', JSON.stringify(sec2));

    const m4 = await page.evaluate(index => {
      timedState.currentIndex = index;
      renderTimedQuestion();
      renderTimedPalette();
      return Array.from(document.querySelectorAll('#d-q-options .opt-btn')).map(button => button.innerText.trim());
    }, sec2.mondai4Index);
    assert.equal(m4.length, 3);
    pass('mondai_4_three_choices', m4.join(' | '));

    await page.evaluate(() => {
      timedState.questions.forEach((q, i) => { if (i < 20) timedState.userAnswers[q.id] = q.correctAnswer; });
      submitTimedSession();
    });
    await page.waitForFunction(() => (document.getElementById('d-summary-score')?.textContent || '').includes('70 / 105 CÂU'), null, { timeout: 5000 });
    const final = await page.evaluate(() => ({
      score: document.getElementById('d-summary-score')?.textContent || '',
      draftCleared: localStorage.getItem('JP_MOCK_SAVE_N2-MOCK-08') === null,
      reviewCards: document.querySelectorAll('#d-review-list .error-item').length,
      audioTags: document.querySelectorAll('#d-review-list audio').length,
      transcripts: document.querySelectorAll('#d-review-list details').length,
      explanationsVisible: (document.getElementById('d-review-list')?.innerText || '').includes('Giải thích chi tiết:')
    }));
    assert.ok(final.score.includes('70 / 105 CÂU'));
    assert.equal(final.draftCleared, true);
    assert.equal(final.reviewCards, 30);
    assert.equal(final.audioTags, 30);
    assert.equal(final.transcripts, 30);
    assert.equal(final.explanationsVisible, true);
    pass('combined_score_and_review', JSON.stringify(final));

    const mobileContext = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true });
    const mobilePage = await mobileContext.newPage();
    mobilePage.on('pageerror', error => pageErrors.push(error.message));
    await mobilePage.goto(ENGINE_URL + '&section=2');
    await mobilePage.waitForFunction(() => typeof timedState !== 'undefined' && timedState.questions.length === 30, null, { timeout: 10000 });
    const mobile = await mobilePage.evaluate(() => ({
      audio: Boolean(document.querySelector('#exam-audio-player') || document.querySelector('audio')),
      optionCount: document.querySelectorAll('#d-q-options .opt-btn').length,
      viewportWidth: window.innerWidth,
      pageWidth: document.documentElement.scrollWidth
    }));
    assert.equal(mobile.audio, true);
    assert.ok(mobile.optionCount >= 3);
    assert.ok(mobile.pageWidth <= mobile.viewportWidth + 1, `horizontal overflow: ${JSON.stringify(mobile)}`);
    pass('mobile_390px_layout', JSON.stringify(mobile));
    await mobileContext.close();

    assert.deepEqual(pageErrors, []);
    pass('browser_console_page_errors', '0');
    const report = {
      examId: 'N2-MOCK-08',
      generatedAt: new Date().toISOString(),
      browser: 'Google Chrome installed on local test host, headless',
      viewport: '1280x800 desktop; 390x844 mobile emulation',
      catalog: 'Public practice entry and full/listening launch links are present and verified in the local browser',
      checkCount: checks.length,
      allPassed: true,
      checks
    };
    fs.writeFileSync(REPORT_PATH, JSON.stringify(report, null, 2), 'utf8');
    console.log(`Wrote ${REPORT_PATH}`);
  } finally {
    await context.close();
    await browser.close();
  }
}

main().catch(error => { console.error(error); process.exit(1); });
