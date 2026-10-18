const fs = require('fs');
const path = require('path');

const devToolsPort = '9222';
const devToolsActivePortFile = path.join(process.env.LOCALAPPDATA, 'Google/Chrome/User Data/DevToolsActivePort');
const portData = fs.readFileSync(devToolsActivePortFile, 'utf8').split('\n');
const browserWsPath = portData[1].trim();

function sendCommand(ws, method, params = {}, sessionId = null) {
  return new Promise((resolve, reject) => {
    const id = Math.floor(Math.random() * 1000000);
    const timer = setTimeout(() => {
      ws.removeEventListener('message', handler);
      reject(new Error(`Timeout waiting for response to ${method}`));
    }, 15000);
    function handler(event) {
      const msg = JSON.parse(event.data);
      if (msg.id === id) {
        clearTimeout(timer);
        ws.removeEventListener('message', handler);
        if (msg.error) reject(msg.error);
        else resolve(msg.result);
      }
    }
    ws.addEventListener('message', handler);
    const payload = { id, method, params };
    if (sessionId) payload.sessionId = sessionId;
    ws.send(JSON.stringify(payload));
  });
}

async function run() {
  const browserWs = new WebSocket('ws://127.0.0.1:' + devToolsPort + browserWsPath);
  await new Promise(r => browserWs.onopen = r);

  const targets = await sendCommand(browserWs, 'Target.getTargets');
  let target = targets.targetInfos.find(t => t.type === 'page' && t.url && t.url.includes('practice_engine'));
  if (!target) {
    target = targets.targetInfos.find(t => t.type === 'page');
  }
  console.log('Attaching to target:', target.targetId, target.title);

  const attachRes = await sendCommand(browserWs, 'Target.attachToTarget', { targetId: target.targetId, flatten: true });
  const sessionId = attachRes.sessionId;

  const liveUrl = 'https://phuchello.github.io/JP-STUDY/widgets/practice_engine.html';
  console.log('Navigating to LIVE Learner URL:', liveUrl);
  await sendCommand(browserWs, 'Page.navigate', { url: liveUrl }, sessionId);
  await new Promise(r => setTimeout(r, 4000));

  // 1. Clear previous local storage on live URL to verify fresh state
  await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      localStorage.removeItem('JP_STUDY_SEEN_QIDS_V2');
      localStorage.removeItem('JP_STUDY_MISTAKE_LOG_V2');
      localStorage.removeItem('JP_STUDY_SESSIONS_V2');
    `
  }, sessionId);

  // 2. Verify Bank Loading & Metadata on Live URL
  const bankEval = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        const b = window.JP_PRACTICE_BANK;
        const badge = document.getElementById('stat-badge');
        const listeningLink = document.querySelector('#modal-listening a') ? document.querySelector('#modal-listening a').href : null;
        return {
          hasBank: !!b,
          version: b ? b.engineVersion : null,
          totalQuestions: b ? b.totalQuestions : null,
          activeCount: b ? b.activeQuestionsCount : null,
          quarantinedCount: b ? b.quarantinedQuestionsCount : null,
          statusBreakdown: b ? b.statusBreakdown : null,
          metrics: b ? b.metrics : null,
          badgeText: badge ? badge.innerText : null,
          listeningLink: listeningLink
        };
      })()
    `,
    returnByValue: true
  }, sessionId);

  console.log('Live Bank Metrics & Links:', JSON.stringify(bankEval.result.value, null, 2));

  if (!bankEval.result.value.hasBank || bankEval.result.value.activeCount !== 720) {
    throw new Error('FAIL: Bank not loaded properly on live URL!');
  }
  if (bankEval.result.value.metrics.allQAPassed !== false) {
    throw new Error('FAIL: allQAPassed is not False!');
  }

  // 3. TASK 1 VERIFICATION: Viewing a question MUST NOT count it as seen; unfinished questions remain unseen
  console.log('--- Testing markIdSeen: Merely viewing must NOT mark seen ---');
  const viewOnlyTest = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        document.getElementById('a-level').value = 'N2';
        document.getElementById('a-skill').value = 'ALL';
        document.getElementById('a-count').value = '10';
        document.getElementById('a-filter').value = 'UNSEEN';
        startGrindSession();
        // Session started, Question 1 is rendered on screen, but NO answer selected
        const seenWhileViewing = getSeenIds();
        // User quits without answering
        quitSession();
        const seenAfterQuit = getSeenIds();
        return {
          seenWhileViewingCount: seenWhileViewing.length,
          seenAfterQuitCount: seenAfterQuit.length
        };
      })()
    `,
    returnByValue: true
  }, sessionId);

  console.log('View-only Test Result:', viewOnlyTest.result.value);
  if (viewOnlyTest.result.value.seenWhileViewingCount !== 0 || viewOnlyTest.result.value.seenAfterQuitCount !== 0) {
    throw new Error('FAIL: Viewing a question incorrectly marked it as seen!');
  }
  console.log('PASS: Viewing a question does NOT mark it as seen! Unfinished questions preserved as unseen.');

  // 4. Run 3 Consecutive Sessions of 30 N2 Questions Each
  console.log('--- Running 3 Consecutive Learner Sessions of 30 N2 Questions ---');
  const sessionResults = [];
  for (let s = 1; s <= 3; s++) {
    const res = await sendCommand(browserWs, 'Runtime.evaluate', {
      expression: `
        (() => {
          document.getElementById('a-level').value = 'N2';
          document.getElementById('a-skill').value = 'ALL';
          document.getElementById('a-count').value = '30';
          document.getElementById('a-filter').value = 'UNSEEN';
          startGrindSession();
          
          const qids = currentSession.questions.map(q => q.id);
          // Simulate learner answering questions (mixture of correct and incorrect)
          let correct = 0;
          currentSession.questions.forEach((q, idx) => {
            // Answer correct on even index, wrong on odd index
            const chosenId = (idx % 2 === 0) ? q.correctAnswer : q.options.find(o => o.id !== q.correctAnswer).id;
            if (chosenId === q.correctAnswer) correct++;
            selectAnswer(chosenId);
            if (idx < currentSession.questions.length - 1) {
              nextQuestion();
            }
          });
          finishSession();
          return {
            sessionNum: ${s},
            qids: qids,
            qCount: qids.length,
            correctCount: currentSession.scoreCorrect,
            seenTotal: getSeenIds().length
          };
        })()
      `,
      returnByValue: true
    }, sessionId);

    sessionResults.push(res.result.value);
    console.log(`Session ${s} Completed: ${res.result.value.qCount} questions, correct: ${res.result.value.correctCount}, cumulative seen: ${res.result.value.seenTotal}`);
    await sendCommand(browserWs, 'Runtime.evaluate', { expression: `resetToConfig();` }, sessionId);
    await new Promise(r => setTimeout(r, 500));
  }

  // 5. Assert 0% overlap across all 3 sessions
  const s1 = new Set(sessionResults[0].qids);
  const s2 = new Set(sessionResults[1].qids);
  const s3 = new Set(sessionResults[2].qids);

  const overlap12 = [...s1].filter(x => s2.has(x));
  const overlap23 = [...s2].filter(x => s3.has(x));
  const overlap13 = [...s1].filter(x => s3.has(x));

  console.log('Overlap S1 & S2:', overlap12.length);
  console.log('Overlap S2 & S3:', overlap23.length);
  console.log('Overlap S1 & S3:', overlap13.length);

  if (overlap12.length > 0 || overlap23.length > 0 || overlap13.length > 0) {
    throw new Error('FAIL: Overlap detected between consecutive sessions!');
  }
  console.log('SUCCESS: All 90 questions across 3 sessions are 100% unique (0 repeats)!');

  // 6. Verify Persistence before reload
  const preReload = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        return {
          storedCount: getStoredSessions().length,
          seenCount: getSeenIds().length,
          mistakesCount: Object.keys(getMistakeRecords()).length
        };
      })()
    `,
    returnByValue: true
  }, sessionId);
  console.log('Pre-reload Persistence State:', preReload.result.value);

  // 7. Reload page to test full reload survival (Persistence integrity)
  console.log('Reloading live page to test persistence survival...');
  await sendCommand(browserWs, 'Page.reload', { ignoreCache: true }, sessionId);
  await new Promise(r => setTimeout(r, 4000));

  // 8. Verify Persistence after reload
  const postReload = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        switchMode('mode-f');
        const rows = document.querySelectorAll('#session-history-tbody tr');
        return {
          storedCount: getStoredSessions().length,
          tableRowsCount: rows.length,
          seenCount: getSeenIds().length,
          mistakesCount: Object.keys(getMistakeRecords()).length,
          firstRowText: rows[0] ? rows[0].innerText : null
        };
      })()
    `,
    returnByValue: true
  }, sessionId);
  console.log('Post-reload Persistence State:', postReload.result.value);

  if (postReload.result.value.storedCount !== 3 || postReload.result.value.tableRowsCount !== 3) {
    throw new Error('FAIL: Sessions did not survive reload!');
  }
  if (postReload.result.value.seenCount !== 90) {
    throw new Error('FAIL: Seen questions count mismatch after reload!');
  }
  console.log('SUCCESS: Full persistence survival verified after reload! 3 sessions, 90 seen questions intact.');

  // 9. Capture screenshot of Mode F Ledger Table
  const brainDir = path.resolve(process.env.USERPROFILE || process.env.HOME, '.gemini/antigravity/brain/07f27e52-1325-4adc-9ec0-5c8e7670a48d/screenshots');
  if (!fs.existsSync(brainDir)) fs.mkdirSync(brainDir, { recursive: true });

  const shot = await sendCommand(browserWs, 'Page.captureScreenshot', { format: 'png' }, sessionId);
  const shotPath = path.join(brainDir, 'live_learner_mode_f_verified.png');
  fs.writeFileSync(shotPath, Buffer.from(shot.data, 'base64'));
  console.log('Saved Mode F screenshot to:', shotPath);

  // 10. Test Mobile Viewport Emulation
  console.log('Emulating mobile viewport (iPhone 14 / Pixel: 390x844, scale 1.0)...');
  await sendCommand(browserWs, 'Emulation.setDeviceMetricsOverride', {
    width: 390,
    height: 844,
    deviceScaleFactor: 2,
    mobile: true
  }, sessionId);
  await sendCommand(browserWs, 'Runtime.evaluate', { expression: `switchMode('mode-a');` }, sessionId);
  await new Promise(r => setTimeout(r, 1500));

  const shotMobile = await sendCommand(browserWs, 'Page.captureScreenshot', { format: 'png' }, sessionId);
  const shotPathMobile = path.join(brainDir, 'live_learner_mobile_verified.png');
  fs.writeFileSync(shotPathMobile, Buffer.from(shotMobile.data, 'base64'));
  console.log('Saved mobile screenshot to:', shotPathMobile);

  // Clear device override
  await sendCommand(browserWs, 'Emulation.clearDeviceMetricsOverride', {}, sessionId);

  browserWs.close();
  console.log('ALL ACCEPTANCE TESTS PASSED SUCCESSFULLY!');
  process.exit(0);
}

run().catch(e => {
  console.error(e);
  process.exit(1);
});
