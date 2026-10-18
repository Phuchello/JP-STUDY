const fs = require('fs');
const path = require('path');

const devToolsPort = '9222';
const devToolsActivePortFile = path.join(process.env.LOCALAPPDATA, 'Google', 'Chrome', 'User Data', 'DevToolsActivePort');
const portData = fs.readFileSync(devToolsActivePortFile, 'utf8').split('\n');
const browserWsPath = portData[1].trim();

async function run() {
  const browserWsUrl = `ws://127.0.0.1:${devToolsPort}${browserWsPath}`;
  console.log('Connecting to browser WS:', browserWsUrl);

  const browserWs = new WebSocket(browserWsUrl);
  await new Promise((resolve, reject) => {
    browserWs.onopen = resolve;
    browserWs.onerror = reject;
  });

  const targets = await sendCommand(browserWs, 'Target.getTargets');
  let target = targets.targetInfos.find(t => t.url && t.url.includes('practice_engine.html'));
  if (!target) {
    target = targets.targetInfos.find(t => t.type === 'page');
  }

  console.log('Attached target:', target.targetId, target.title);
  const attachRes = await sendCommand(browserWs, 'Target.attachToTarget', { targetId: target.targetId, flatten: true });
  const sessionId = attachRes.sessionId;

  async function sendSession(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = Math.floor(Math.random() * 1000000);
      function handler(event) {
        const msg = JSON.parse(event.data);
        if (msg.id === id) {
          browserWs.removeEventListener('message', handler);
          if (msg.error) reject(msg.error);
          else resolve(msg.result);
        }
      }
      browserWs.addEventListener('message', handler);
      browserWs.send(JSON.stringify({ id, sessionId, method, params }));
    });
  }

  // Navigate to local practice_engine.html
  const localHtml = path.resolve(__dirname, '../docs/widgets/practice_engine.html').replace(/\\/g, '/');
  const url = `file:///${localHtml}`;
  console.log('Navigating to:', url);
  await sendSession('Page.navigate', { url });
  await new Promise(r => setTimeout(r, 1500));

  // Clear previous session storage in browser to start clean
  await sendSession('Runtime.evaluate', {
    expression: `
      localStorage.removeItem('JP_STUDY_SEEN_QIDS_V2');
      localStorage.removeItem('JP_STUDY_MISTAKE_LOG_V2');
      localStorage.removeItem('JP_STUDY_SESSIONS_V2');
    `
  });

  // Verify Bank Metrics
  const bankEval = await sendSession('Runtime.evaluate', {
    expression: `
      (() => {
        const b = window.JP_PRACTICE_BANK;
        return {
          totalQuestions: b.totalQuestions,
          activeCount: b.activeQuestionsCount,
          quarantinedCount: b.quarantinedQuestionsCount,
          statusBreakdown: b.statusBreakdown
        };
      })()
    `,
    returnByValue: true
  });
  console.log('Bank Metrics:', bankEval.result.value);

  // Run 3 Consecutive Sessions of 30 N2 Questions Each
  const sessionResults = [];
  for (let s = 1; s <= 3; s++) {
    const res = await sendSession('Runtime.evaluate', {
      expression: `
        (() => {
          document.getElementById('a-level').value = 'N2';
          document.getElementById('a-skill').value = 'ALL';
          document.getElementById('a-count').value = '30';
          document.getElementById('a-filter').value = 'UNSEEN';
          startGrindSession();
          
          const qids = currentSession.questions.map(q => q.id);
          // Mark all 30 as answered to simulate full session completion
          currentSession.questions.forEach((q, idx) => {
            selectAnswer(q.options[0].id);
            if (idx < currentSession.questions.length - 1) {
              nextQuestion();
            }
          });
          finishSession();
          return {
            sessionNum: ${s},
            qids: qids,
            qCount: qids.length,
            seenTotal: getSeenIds().length
          };
        })()
      `,
      returnByValue: true
    });
    sessionResults.push(res.result.value);
    console.log(`Session ${s} Completed:`, res.result.value.qCount, 'questions, cumulative seen:', res.result.value.seenTotal);
    await sendSession('Runtime.evaluate', { expression: `resetToConfig();` });
    await new Promise(r => setTimeout(r, 400));
  }

  // Assert 0% overlap across all 3 sessions
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
  console.log('SUCCESS: 3 consecutive 30-question sessions have 100% unique items (0% overlap)!');

  // Verify Persistence: Check Mode F has 3 sessions
  const historyCheck = await sendSession('Runtime.evaluate', {
    expression: `
      (() => {
        switchMode('mode-f');
        const rows = Array.from(document.querySelectorAll('#session-history-tbody tr'));
        return {
          storedCount: getStoredSessions().length,
          tableRowsCount: rows.length
        };
      })()
    `,
    returnByValue: true
  });
  console.log('Persistence History Check:', historyCheck.result.value);

  // Take final screenshot
  const screenshot = await sendSession('Page.captureScreenshot', { format: 'png' });
  const brainDir = path.resolve(process.env.USERPROFILE || process.env.HOME, '.gemini/antigravity/brain/07f27e52-1325-4adc-9ec0-5c8e7670a48d/screenshots');
  const screenshotPath = path.join(brainDir, 'practice_engine_v2_sessions_verified.png');
  fs.writeFileSync(screenshotPath, Buffer.from(screenshot.data, 'base64'));
  console.log('Saved verification screenshot to:', screenshotPath);

  browserWs.close();
}

function sendCommand(ws, method, params = {}) {
  return new Promise((resolve, reject) => {
    const id = Math.floor(Math.random() * 1000000);
    function handler(event) {
      const msg = JSON.parse(event.data);
      if (msg.id === id) {
        ws.removeEventListener('message', handler);
        if (msg.error) reject(msg.error);
        else resolve(msg.result);
      }
    }
    ws.addEventListener('message', handler);
    ws.send(JSON.stringify({ id, method, params }));
  });
}

run().catch(e => {
  console.error(e);
  process.exit(1);
});
