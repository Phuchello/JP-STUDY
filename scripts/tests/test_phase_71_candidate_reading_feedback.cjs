const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '../..');
const engine = path.join(root, 'docs/widgets/practice_engine.html');
const fixtureDir = path.join(root, 'tmp/phase7/candidate_e2e');
const targets = {
  'N2-MOCK-11': 'N2_11_M10_01',
  'N2-MOCK-12': 'N2_12_M11_01',
  'N2-MOCK-13': 'N2_13_M11_01',
};
const sha256 = value => crypto.createHash('sha256').update(value, 'utf8').digest('hex');
const sha256Bytes = value => crypto.createHash('sha256').update(value).digest('hex');
const sourceFiles = [
  'scripts/curriculum/phase_71_reading_repairs.py',
  'scripts/curriculum/phase_71_reading_rationales.py',
  'scripts/curriculum/bank_data/n2_mock_11_data.py',
  'scripts/curriculum/bank_data/n2_mock_12_data.py',
  'scripts/curriculum/bank_data/n2_mock_13_data.py',
];
const results = [];

async function main() {
  const browser = await chromium.launch({headless: true, ...(process.env.CHROME_PATH ? {executablePath: process.env.CHROME_PATH} : {}), args: ['--allow-file-access-from-files']});
  try {
    for (const [mockId, questionId] of Object.entries(targets)) {
      const mockNumber = mockId.slice(-2);
      const fixturePath = path.join(fixtureDir, `n2_mock_${mockNumber}_candidate.json`);
      assert.ok(fs.existsSync(fixturePath), `candidate fixture missing: ${fixturePath}`);
      const exam = JSON.parse(fs.readFileSync(fixturePath, 'utf8'));
      const question = exam.sections[0].items.find(item => item.id === questionId);
      assert.ok(question, `${questionId} missing from candidate fixture`);
      assert.ok(question.distractorExplanations && question.explanationVi,
        `${questionId} lacks the reviewed feedback data`);
      const wrongIds = question.options.map(option => option.id).filter(id => id !== question.correctAnswer);
      assert.equal(wrongIds.length, 3);
      assert.deepEqual(Object.keys(question.distractorExplanations).sort(), wrongIds.slice().sort());
      assert.equal(new Set(Object.values(question.distractorExplanations)).size, 3,
        `${questionId} wrong options must have distinct explanations`);
      const selectedWrongId = wrongIds[0];
      const secondWrongId = wrongIds[1];

      const context = await browser.newContext({viewport: {width: 1280, height: 900}});
      const page = await context.newPage();
      const pageErrors = [];
      const consoleErrors = [];
      const screenshots = {};
      page.on('pageerror', error => pageErrors.push(error.message));
      page.on('console', message => { if (message.type() === 'error') consoleErrors.push(message.text()); });
      await page.route('https://**/*', route => {
        const type = route.request().resourceType();
        const contentType = type === 'stylesheet' ? 'text/css' : type === 'script' ? 'application/javascript' : type === 'fetch' ? 'application/json' : 'text/plain';
        return route.fulfill({status: 200, contentType, body: type === 'fetch' ? '{}' : ''});
      });
      const engineUrl = `file:///${engine.replaceAll('\\', '/')}`;
      await page.goto(engineUrl);
      await page.waitForFunction(() => typeof startFullMockExam === 'function' && typeof timedState !== 'undefined');
      await page.evaluate(data => {
        window.JP_MOCK_DATA = window.JP_MOCK_DATA || {};
        window.JP_MOCK_DATA[data.examId] = data;
        localStorage.clear();
        startFullMockExam(data.examId, 0);
      }, exam);
      await page.waitForFunction(() => typeof timedState !== 'undefined' && timedState.questions?.length === 75);
      const itemIndex = await page.evaluate(qid => {
        const index = timedState.questions.findIndex(item => item.id === qid);
        if (index < 0) return -1;
        timedState.currentIndex = index;
        renderTimedQuestion();
        return index;
      }, questionId);
      assert.notEqual(itemIndex, -1, `${questionId} was not loaded by the practice engine`);

      const initial = await page.evaluate(({qid, selectedId}) => {
        const item = timedState.questions.find(candidate => candidate.id === qid);
        return {
          visibleText: document.getElementById('d-arena')?.innerText || '',
          optionCount: document.querySelectorAll('#d-q-options .opt-btn').length,
          markedCorrect: document.querySelectorAll('#d-q-options .opt-btn.correct').length,
          markedIncorrect: document.querySelectorAll('#d-q-options .opt-btn.incorrect').length,
          explanationBoxActive: document.getElementById('d-q-exp')?.classList.contains('active') || false,
          selectedRationaleVisible: (document.getElementById('d-arena')?.innerText || '').includes(item.distractorExplanations[selectedId]),
          generalExplanationVisible: (document.getElementById('d-arena')?.innerText || '').includes(item.explanationVi),
          keyLabelVisible: /答え|正解/.test(document.getElementById('d-arena')?.innerText || ''),
        };
      }, {qid: questionId, selectedId: selectedWrongId});
      assert.equal(initial.optionCount, 4);
      assert.equal(initial.markedCorrect, 0);
      assert.equal(initial.markedIncorrect, 0);
      assert.equal(initial.explanationBoxActive, false);
      assert.equal(initial.selectedRationaleVisible, false);
      assert.equal(initial.generalExplanationVisible, false);
      assert.equal(initial.keyLabelVisible, false);
      screenshots.desktopQuestion = path.join(fixtureDir, 'screenshots', `${mockNumber}_${questionId}_desktop_question.png`);
      fs.mkdirSync(path.dirname(screenshots.desktopQuestion), {recursive: true});
      await page.screenshot({path: screenshots.desktopQuestion, fullPage: true});
      const desktop = await page.evaluate(() => ({width: innerWidth, documentWidth: document.documentElement.scrollWidth}));
      assert.equal(desktop.width, 1280);
      assert.ok(desktop.documentWidth <= desktop.width, JSON.stringify(desktop));

      await page.setViewportSize({width: 390, height: 844});
      const mobileQuestion = await page.evaluate(() => ({width: innerWidth, documentWidth: document.documentElement.scrollWidth, optionCount: document.querySelectorAll('#d-q-options .opt-btn').length}));
      assert.equal(mobileQuestion.width, 390);
      assert.equal(mobileQuestion.optionCount, 4);
      assert.ok(mobileQuestion.documentWidth <= 390, JSON.stringify(mobileQuestion));
      screenshots.mobileQuestion = path.join(fixtureDir, 'screenshots', `${mockNumber}_${questionId}_mobile_question.png`);
      await page.screenshot({path: screenshots.mobileQuestion, fullPage: true});

      const selectedOptionIndex = question.options.findIndex(option => option.id === selectedWrongId);
      await page.locator('#d-q-options .opt-btn').nth(selectedOptionIndex).click();
      assert.equal(await page.evaluate(qid => timedState.userAnswers[qid], questionId), selectedWrongId);
      await page.evaluate(({qid, wrongId}) => {
        const targetIndex = timedState.questions.findIndex(item => item.id === qid);
        const unansweredIndex = targetIndex === 0 ? 1 : 0;
        timedState.questions.forEach((item, index) => {
          if (item.id === qid) timedState.userAnswers[item.id] = wrongId;
          else if (index !== unansweredIndex) timedState.userAnswers[item.id] = item.correctAnswer;
        });
        timedState.currentIndex = targetIndex;
        submitTimedSession();
      }, {qid: questionId, wrongId: selectedWrongId});
      await page.waitForFunction(() => (document.getElementById('d-summary-score')?.textContent || '').includes('73 / 75 CÂU'));

      const card = page.locator('#d-review-list .error-item').filter({hasText: `ID: ${questionId}`});
      assert.equal(await card.count(), 1, `${questionId} review card missing or duplicated`);
      const cardText = await card.innerText();
      const selectedFeedback = question.distractorExplanations[selectedWrongId];
      const otherFeedback = question.distractorExplanations[secondWrongId];
      const listItems = await card.locator('li').allTextContents();
      assert.ok(listItems.includes(`${selectedWrongId}: ${selectedFeedback}`),
        `${questionId} selected choice is not bound to its exact rationale`);
      assert.ok(listItems.includes(`${secondWrongId}: ${otherFeedback}`),
        `${questionId} second wrong choice is not bound to its exact rationale`);
      assert.notEqual(selectedFeedback, otherFeedback);
      assert.ok(cardText.includes(`Bạn chọn: ${selectedWrongId}`));
      assert.ok(cardText.includes(`Đáp án đúng: ${question.correctAnswer}`));
      assert.ok(cardText.includes(`Giải thích chi tiết: ${question.explanationVi}`));
      const score = await page.locator('#d-summary-score').innerText();
      assert.match(score, /73\s*\/\s*75/);
      const reviewHistory = await page.evaluate(() => getStoredSessions()[0]);
      assert.equal(reviewHistory.mockId, mockId);
      assert.equal(reviewHistory.totalQuestions, 75);
      assert.equal(reviewHistory.scoreCorrect, 73);

      screenshots.mobileReview = path.join(fixtureDir, 'screenshots', `${mockNumber}_${questionId}_mobile_review.png`);
      await page.screenshot({path: screenshots.mobileReview, fullPage: true});
      const mobileReview = await page.evaluate(() => ({width: innerWidth, documentWidth: document.documentElement.scrollWidth}));
      assert.equal(mobileReview.width, 390);
      assert.ok(mobileReview.documentWidth <= 390, JSON.stringify(mobileReview));
      assert.equal(pageErrors.length, 0, JSON.stringify(pageErrors));
      assert.equal(consoleErrors.length, 0, JSON.stringify(consoleErrors));

      results.push({
        examId: mockId,
        questionId,
        selectedWrongOptionId: selectedWrongId,
        otherWrongOptionId: secondWrongId,
        correctOptionId: question.correctAnswer,
        selectedExplanationSha256: sha256(selectedFeedback),
        otherExplanationSha256: sha256(otherFeedback),
        generalExplanationSha256: sha256(question.explanationVi),
        beforeSubmit: initial,
        displayedSelectedExplanationExact: true,
        displayedOtherWrongExplanationExact: true,
        correctAnswerAndGeneralExplanationDisplayed: true,
        score,
        desktop,
        mobileQuestion,
        mobileReview,
        pageErrors: pageErrors.length,
        consoleErrors: consoleErrors.length,
        screenshotSha256: Object.fromEntries(Object.entries(screenshots).map(([label, file]) => [label, sha256Bytes(fs.readFileSync(file))])),
      });
      await context.close();
    }
  } finally {
    await browser.close();
  }

  const report = {
    scope: 'Local Chromium; candidate injection with synthetic responses only; no published bank, public-site content, audio, or learner records changed.',
    browser: 'Playwright Chromium headless',
    fixtureSource: 'scripts/curriculum/export_phase_71_candidate_browser_fixtures.py',
    generatedAt: new Date().toISOString(),
    sourceSha256: Object.fromEntries(sourceFiles.map(file => [file, sha256Bytes(fs.readFileSync(path.join(root, file)))])),
    fixtureSha256: Object.fromEntries([11, 12, 13].map(number => {
      const file = path.join(fixtureDir, `n2_mock_${number}_candidate.json`);
      return [`tmp/phase7/candidate_e2e/n2_mock_${number}_candidate.json`, sha256Bytes(fs.readFileSync(file))];
    })),
    runnerSha256: sha256Bytes(fs.readFileSync(__filename)),
    syntheticResponses: true,
    allPassed: true,
    results,
  };
  const output = path.join(fixtureDir, 'phase71_reading_feedback_result.json');
  fs.writeFileSync(output, `${JSON.stringify(report, null, 2)}\n`);
  console.log(JSON.stringify(report, null, 2));
  console.log(`RESULT ${output}`);
}

main().catch(error => {
  console.error(error);
  process.exit(1);
});
