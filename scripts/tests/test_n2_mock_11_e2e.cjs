// Browser E2E for the integrated M11 practice mock and direct launch route.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const assert = require('node:assert/strict');

const ROOT = path.resolve(__dirname, '../..');
const EXAM_PATH = path.join(ROOT, 'data/mock_exams/n2_mock_11.json');
const CATALOG_PATH = path.join(ROOT, 'docs/widgets/jlpt_exam_catalog.html');
const ENGINE_PATH = path.join(ROOT, 'docs/widgets/practice_engine.html');
const REPORT_PATH = path.join(ROOT, 'qa/N2_MOCK_11_E2E_REPORT.json');
const SYSTEM_CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const CHROME_PATH = process.env.CHROME_PATH || (process.platform === 'win32' && fs.existsSync(SYSTEM_CHROME) ? SYSTEM_CHROME : undefined);

async function main() {
  const exam = JSON.parse(fs.readFileSync(EXAM_PATH, 'utf8'));
  assert.equal(exam.examId, 'N2-MOCK-11');
  assert.equal(exam.status, 'FULL_MOCK');
  assert.equal(exam.sections[0].items.length, 75);
  assert.equal(exam.sections[1].items.length, 30);

  const browser = await chromium.launch({
    ...(CHROME_PATH ? { executablePath: CHROME_PATH } : {}),
    headless: true,
    args: ['--autoplay-policy=no-user-gesture-required', '--allow-file-access-from-files']
  });
  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const page = await context.newPage();
  const pageErrors = [];
  const checks = [];
  page.on('pageerror', error => pageErrors.push(error.message));
  const pass = (name, details) => { checks.push({ name, passed: true, details }); console.log(`PASS ${name}: ${details}`); };

  try {
    const catalogUrl = `file:///${CATALOG_PATH.replaceAll('\\', '/')}`;
    await page.goto(catalogUrl);
    const catalogLinks = await page.evaluate(() => {
      const card = Array.from(document.querySelectorAll('.card')).find(node => node.innerText.includes('Practice Mock Exam #11'));
      const links = card ? Array.from(card.querySelectorAll('a')).map(link => link.getAttribute('href')) : [];
      return { cardFound: Boolean(card), links };
    });
    assert.equal(catalogLinks.cardFound, true);
    assert.deepEqual(catalogLinks.links, [
      'https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mock&mockId=N2-MOCK-11',
      'https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html?mode=mock&mockId=N2-MOCK-11&section=2'
    ]);
    pass('catalog_responder_links', JSON.stringify(catalogLinks.links));

    const engineUrl = `file:///${ENGINE_PATH.replaceAll('\\', '/')}`;
    await page.goto(engineUrl + '?mode=mock&mockId=N2-MOCK-11');
    await page.waitForFunction(() => typeof launchMockExamSafely === 'function' && typeof startFullMockExam === 'function');
    await page.waitForFunction(() => typeof timedState !== 'undefined' && timedState.questions?.length === 75);
    const firstSection = await page.evaluate(() => ({
      mockId: timedState.mockMeta.mockId,
      count: timedState.questions.length,
      durationSec: timedState.totalSec,
      firstId: timedState.questions[0].id,
      optionsRendered: document.querySelectorAll('#d-q-options .opt-btn').length,
      transcriptVisible: (document.getElementById('d-q-passage')?.innerText || '').includes(timedState.questions[0].script || '___NEVER___')
    }));
    assert.equal(firstSection.mockId, 'N2-MOCK-11');
    assert.equal(firstSection.count, 75);
    assert.equal(firstSection.durationSec, 6300);
    assert.ok(firstSection.firstId.startsWith('N2_11_'));
    assert.equal(firstSection.optionsRendered, 4);
    pass('section_1_launch', JSON.stringify(firstSection));

    await page.evaluate(() => {
      timedState.questions.forEach((question, index) => {
        if (index < 60) timedState.userAnswers[question.id] = question.correctAnswer;
        else if (index < 70) timedState.userAnswers[question.id] = question.options.find(option => option.id !== question.correctAnswer).id;
      });
      submitTimedSession();
    });
    await page.waitForFunction(() => (document.getElementById('d-summary-score')?.textContent || '').includes('60 / 75 CÂU'));
    const sectionOne = await page.evaluate(() => ({
      score: document.getElementById('d-summary-score')?.textContent || '',
      savedDraft: Boolean(localStorage.getItem('JP_MOCK_SAVE_N2-MOCK-11')),
      reviewCards: document.querySelectorAll('#d-review-list .error-item').length,
      unansweredCards: Array.from(document.querySelectorAll('#d-review-list .error-item')).filter(card => card.innerText.includes('⚪ CHƯA LÀM')).length
    }));
    assert.equal(sectionOne.savedDraft, true);
    assert.equal(sectionOne.reviewCards, 75);
    assert.equal(sectionOne.unansweredCards, 5);
    pass('section_1_scoring_review_unanswered', JSON.stringify(sectionOne));

    await page.evaluate(() => startFullMockExam('N2-MOCK-11', 1));
    await page.waitForFunction(() => typeof timedState !== 'undefined' && timedState.questions?.length === 30 && timedState.mockMeta.currentSectionIndex === 1);
    const firstListening = await page.evaluate(() => ({
      count: timedState.questions.length,
      durationSec: timedState.totalSec,
      firstId: timedState.questions[0].id,
      audioUrl: timedState.questions[0].audioUrl,
      audioSource: document.querySelector('#exam-audio-player')?.getAttribute('src'),
      optionsRendered: document.querySelectorAll('#d-q-options .opt-btn').length,
      transcriptVisible: (document.getElementById('d-q-passage')?.innerText || '').includes(timedState.questions[0].contextPassage)
    }));
    assert.equal(firstListening.count, 30);
    assert.equal(firstListening.durationSec, 3000);
    assert.ok(firstListening.audioUrl.startsWith('audio/n2_mock_11/'));
    assert.equal(firstListening.audioSource, `../${firstListening.audioUrl}`);
    assert.ok(firstListening.optionsRendered >= 3);
    assert.equal(firstListening.transcriptVisible, false);
    pass('listening_launch_audio_and_transcript_hidden', JSON.stringify(firstListening));

    const mondai4 = await page.evaluate(() => timedState.questions
      .map((q, index) => ({ index, id: q.id, typeId: q.typeId, choiceCount: q.options.length }))
      .filter(q => q.typeId === 'N2-LIS-RESP'));
    assert.equal(mondai4.length, 11);
    assert.ok(mondai4.every(q => q.choiceCount === 3), JSON.stringify(mondai4));
    const mondai4Index = mondai4[0].index;
    const mondai4Options = await page.evaluate(index => {
      timedState.currentIndex = index;
      renderTimedQuestion();
      return document.querySelectorAll('#d-q-options .opt-btn').length;
    }, mondai4Index);
    assert.equal(mondai4Options, 3);
    pass('mondai_4_three_choice_render', `${mondai4.length} items each have 3 choices; UI renders ${mondai4Options}`);

    await page.evaluate(() => {
      timedState.questions.forEach((question, index) => {
        timedState.userAnswers[question.id] = index < 20
          ? question.correctAnswer
          : question.options.find(option => option.id !== question.correctAnswer).id;
      });
      submitTimedSession();
    });
    await page.waitForFunction(() => (document.getElementById('d-summary-score')?.textContent || '').includes('80 / 105 CÂU'));
    const fullResult = await page.evaluate(() => {
      const sessions = getStoredSessions();
      const latest = sessions[0];
      const wrongItems = Array.from(document.querySelectorAll('#d-review-list .error-item')).filter(card => card.innerText.includes('❌ SAI')).length;
      const vietnameseExplanation = (document.getElementById('d-review-list')?.innerText || '').includes('Giải thích chi tiết:');
      return {
        score: document.getElementById('d-summary-score')?.textContent || '',
        historyTotal: latest?.totalQuestions,
        historyCorrect: latest?.scoreCorrect,
        historyMockId: latest?.mockId,
        historyMode: latest?.mode,
        wrongItems,
        reviewCards: document.querySelectorAll('#d-review-list .error-item').length,
        vietnameseExplanation,
        sec1DraftCleared: localStorage.getItem('JP_MOCK_SAVE_N2-MOCK-11') === null
      };
    });
    assert.equal(fullResult.historyTotal, 105);
    assert.equal(fullResult.historyCorrect, 80);
    assert.equal(fullResult.historyMockId, 'N2-MOCK-11');
    assert.equal(fullResult.historyMode, 'FULL_MOCK');
    assert.equal(fullResult.wrongItems, 10);
    assert.equal(fullResult.reviewCards, 30);
    assert.equal(fullResult.vietnameseExplanation, true);
    assert.equal(fullResult.sec1DraftCleared, true);
    pass('full_mock_scoring_history_mistake_review', JSON.stringify(fullResult));

    assert.deepEqual(pageErrors, []);
    pass('browser_page_errors', '0');
    await page.setViewportSize({ width: 390, height: 844 });
    await page.evaluate(() => {
      localStorage.clear();
      launchMockExamSafely('N2-MOCK-11', 0);
    });
    await page.waitForFunction(() => typeof timedState !== 'undefined' && timedState.questions?.length === 75);
    const mobile = await page.evaluate(() => ({
      viewportWidth: window.innerWidth,
      documentWidth: document.documentElement.scrollWidth,
      horizontalOverflow: document.documentElement.scrollWidth > window.innerWidth,
      renderedOptions: document.querySelectorAll('#d-q-options .opt-btn').length,
      questionVisible: Boolean(document.getElementById('d-q-passage')?.innerText.trim())
    }));
    assert.equal(mobile.viewportWidth, 390);
    assert.equal(mobile.horizontalOverflow, false, JSON.stringify(mobile));
    assert.equal(mobile.renderedOptions, 4);
    assert.equal(mobile.questionVisible, true);
    pass('mobile_390px_mock_usability', JSON.stringify(mobile));
    const report = {
      examId: 'N2-MOCK-11',
      status: 'PASS_LOCAL_E2E',
      scope: 'local catalog + exam interaction only; not live-site verification',
      qaData: true,
      generatedAt: new Date().toISOString(),
      browser: 'Local Chromium Headless via Playwright',
      viewport: '1280x800 and 390x844',
      catalogIntegration: 'integrated JP_MOCK_DATA plus direct mode=mock&mockId=N2-MOCK-11 URL route',
      checks,
      allPassed: true
    };
    fs.writeFileSync(REPORT_PATH, `${JSON.stringify(report, null, 2)}\n`, 'utf8');
    console.log(`Wrote ${REPORT_PATH}`);
  } finally {
    await context.close();
    await browser.close();
  }
}

main().catch(error => { console.error(error); process.exit(1); });


