// Browser-level verification of Phase 6.1 remapped scoring and review behavior.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const assert = require('assert/strict');

const ROOT = path.resolve(__dirname, '../..');
const CATALOG_URL = 'file:///' + path.join(ROOT, 'docs/widgets/jlpt_exam_catalog.html').replaceAll('\\', '/');
const ENGINE_PATH = 'file:///' + path.join(ROOT, 'docs/widgets/practice_engine.html').replaceAll('\\', '/');
const REPORT_PATH = path.join(ROOT, 'qa/PHASE_6_1_RUNTIME_SEMANTICS_REPORT.json');
const SYSTEM_CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const CHROME_PATH = process.env.CHROME_PATH || (process.platform === 'win32' && fs.existsSync(SYSTEM_CHROME) ? SYSTEM_CHROME : undefined);

async function main() {
  const browser = await chromium.launch({
    ...(CHROME_PATH ? { executablePath: CHROME_PATH } : {}),
    headless: true,
    args: ['--autoplay-policy=no-user-gesture-required', '--allow-file-access-from-files']
  });
  const checks = [];
  const errors = [];
  const catalog = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  catalog.on('pageerror', error => errors.push(error.message));
  try {
    await catalog.goto(CATALOG_URL);
    for (const mockNumber of [7, 8, 9]) {
      const mockId = `N2-MOCK-${String(mockNumber).padStart(2, '0')}`;
      const cardTitle = mockNumber === 7
        ? `JLPT N2 Full Mock Exam #${String(mockNumber).padStart(2, '0')}`
        : `JLPT N2 | Full Mock Exam #${String(mockNumber).padStart(2, '0')}`;
      const card = catalog.locator('.card').filter({
        has: catalog.getByText(cardTitle, { exact: true })
      });
      assert.equal(await card.count(), 1, `${mockId} catalog card`);
      const links = await card.locator('a').evaluateAll(rows => rows.map(row => row.href));
      assert.ok(links.some(url => url.includes(`mode=mock&mockId=${mockId}`)), `${mockId} full link`);
      assert.ok(links.some(url => url.includes(`mockId=${mockId}&section=2`)), `${mockId} listening link`);
      checks.push({ examId: mockId, check: 'catalog_and_responder_links', passed: true, links });
    }

    for (const mockNumber of [7, 8, 9]) {
      const mockId = `N2-MOCK-${String(mockNumber).padStart(2, '0')}`;
      const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
      page.on('pageerror', error => errors.push(`${mockId}: ${error.message}`));
      const url = `${ENGINE_PATH}?mode=mock&mockId=${mockId}`;
      await page.goto(url);
      await page.waitForFunction(() => typeof timedState !== 'undefined' && timedState.questions?.length === 75, null, { timeout: 10000 });
      const active = await page.evaluate(() => ({
        mockId: timedState.mockMeta?.mockId,
        questionCount: timedState.questions.length,
        renderedOptions: Array.from(document.querySelectorAll('#d-q-options .opt-btn')).map(x => x.innerText.trim()),
        explanationVisible: Boolean(document.getElementById('d-review-list')?.innerText.trim()),
        transcriptVisible: Boolean(document.querySelector('#d-review-list details'))
      }));
      assert.equal(active.mockId, mockId);
      assert.equal(active.questionCount, 75);
      assert.equal(active.renderedOptions.length, 4);
      assert.equal(active.explanationVisible, false);
      assert.equal(active.transcriptVisible, false);

      const probe = await page.evaluate(() => {
        const correctQuestion = timedState.questions[0];
        const wrongQuestion = timedState.questions[1];
        const wrongOption = wrongQuestion.options.find(option => option.id !== wrongQuestion.correctAnswer);
        timedState.userAnswers[correctQuestion.id] = correctQuestion.correctAnswer;
        timedState.userAnswers[wrongQuestion.id] = wrongOption.id;
        return {
          correctQuestionId: correctQuestion.id,
          wrongQuestionId: wrongQuestion.id,
          wrongAnswer: wrongOption.id,
          correctAnswer: wrongQuestion.correctAnswer,
          correctText: wrongQuestion.options.find(option => option.id === wrongQuestion.correctAnswer).text,
          explanation: wrongQuestion.explanationVi
        };
      });
      await page.evaluate(() => submitTimedSession());
      await page.waitForFunction(() => Boolean(document.getElementById('d-summary-score')?.textContent), null, { timeout: 5000 });
      const review = await page.evaluate(id => {
        const card = Array.from(document.querySelectorAll('#d-review-list .error-item'))
          .find(row => row.innerText.includes(`ID: ${id}`));
        return card?.innerText || '';
      }, probe.wrongQuestionId);
      assert.ok(review.includes(`Bạn chọn: ${probe.wrongAnswer}`), `${mockId} selected distractor appears`);
      assert.ok(review.includes(`Đáp án đúng: ${probe.correctAnswer}`), `${mockId} current answer label appears`);
      assert.ok(review.includes(probe.correctText), `${mockId} semantic correct option appears`);
      assert.ok(review.includes(probe.explanation), `${mockId} Vietnamese explanation appears after submission`);
      const score = await page.locator('#d-summary-score').innerText();
      assert.match(score, /1 \/ 75 CÂU/);
      checks.push({ examId: mockId, check: 'active_quiz_no_leaks_scoring_and_semantic_review', passed: true,
        active, probe, score, reviewCardContainsCorrectText: true });

      await page.evaluate(id => startMockBreak(id), mockId);
      await page.evaluate(id => startFullMockExam(id, 1), mockId);
      await page.waitForFunction(() => typeof timedState !== 'undefined' && timedState.questions?.length === 30, null, { timeout: 10000 });
      const listening = await page.evaluate(() => {
        const q = timedState.questions[0];
        return {
          count: timedState.questions.length,
          audioUrl: q.audioUrl,
          transcript: q.contextPassage || q.script || '',
          explanation: q.explanationVi || '',
          reviewVisible: document.getElementById('d-summary')?.style.display !== 'none' && Boolean(document.getElementById('d-review-list')?.innerText.trim()),
          transcriptVisible: Boolean(document.body.innerText.includes(q.contextPassage || q.script || '\u0000')),
        };
      });
      assert.equal(listening.count, 30);
      assert.ok(listening.audioUrl.includes(`/n2_mock_${String(mockNumber).padStart(2, '0')}/`));
      assert.ok(listening.transcript.length > 20);
      assert.equal(listening.reviewVisible, false);
      assert.equal(listening.transcriptVisible, false);
      const m4 = await page.evaluate(() => {
        const index = timedState.questions.findIndex(q => q.id.includes('_M4_'));
        timedState.currentIndex = index;
        renderTimedQuestion();
        return { index, optionCount: document.querySelectorAll('#d-q-options .opt-btn').length };
      });
      assert.ok(m4.index >= 0);
      assert.equal(m4.optionCount, 3);
      checks.push({ examId: mockId, check: 'listening_no_transcript_leak_and_mondai4_choices', passed: true, listening, m4 });
      await page.close();
    }

    assert.deepEqual(errors, []);
    const report = { status: 'PASS', browser: 'Chromium headless', viewport: '1280x800', checks, pageErrors: errors };
    fs.writeFileSync(REPORT_PATH, JSON.stringify(report, null, 2), 'utf8');
    console.log(JSON.stringify({ status: report.status, checkCount: checks.length, pageErrors: errors, report: REPORT_PATH }, null, 2));
  } finally {
    await browser.close();
  }
}

main().catch(error => { console.error(error); process.exit(1); });
