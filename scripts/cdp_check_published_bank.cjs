const fs = require('fs');
const path = require('path');
const devToolsPort = '9222';
const devToolsActivePortFile = path.join(process.env.LOCALAPPDATA, 'Google/Chrome/User Data/DevToolsActivePort');
const browserWsPath = fs.readFileSync(devToolsActivePortFile, 'utf8').split('\n')[1].trim();

function sendCommand(ws, method, params = {}, sessionId = null) {
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
    const payload = { id, method, params };
    if (sessionId) payload.sessionId = sessionId;
    ws.send(JSON.stringify(payload));
  });
}

async function run() {
  const browserWs = new WebSocket('ws://127.0.0.1:' + devToolsPort + browserWsPath);
  await new Promise(r => browserWs.onopen = r);

  const targets = await sendCommand(browserWs, 'Target.getTargets');
  let pubTarget = targets.targetInfos.find(t => t.url && t.url.includes('sites.google.com/view/jp-study/kho-'));
  if (!pubTarget) {
    pubTarget = targets.targetInfos.find(t => t.url && t.url.includes('sites.google.com/view/jp-study'));
  }
  console.log('Target:', pubTarget.url);

  const attachRes = await sendCommand(browserWs, 'Target.attachToTarget', { targetId: pubTarget.targetId, flatten: true });
  const sessionId = attachRes.sessionId;

  const contexts = [];
  browserWs.addEventListener('message', e => {
    const msg = JSON.parse(e.data);
    if (msg.method === 'Runtime.executionContextCreated') {
      contexts.push({ sessionId: msg.sessionId || sessionId, context: msg.params.context });
    }
  });

  await sendCommand(browserWs, 'Target.setAutoAttach', { autoAttach: true, waitForDebuggerOnStart: false, flatten: true }, sessionId);
  await sendCommand(browserWs, 'Runtime.enable', {}, sessionId);
  await new Promise(r => setTimeout(r, 3000));

  console.log('Discovered Execution Contexts across all frames:', contexts.length);
  for (const item of contexts) {
    try {
      const evalRes = await sendCommand(browserWs, 'Runtime.evaluate', {
        expression: `
          (() => {
            const b = window.JP_PRACTICE_BANK;
            return {
              origin: window.location.origin,
              hasBank: !!b,
              totalQ: b ? b.totalQuestions : null,
              activeQ: b ? b.activeQuestionsCount : null,
              quarantinedQ: b ? b.quarantinedQuestionsCount : null,
              title: document.title,
              header: document.querySelector('.engine-header-title') ? document.querySelector('.engine-header-title').innerText : null
            };
          })()
        `,
        contextId: item.context.id,
        returnByValue: true
      }, item.sessionId);

      if (evalRes.result.value && (evalRes.result.value.hasBank || evalRes.result.value.header)) {
        console.log(`Context [${item.context.id}] in session [${item.sessionId.slice(0, 8)}]:`, evalRes.result.value);
      }
    } catch(err) {}
  }

  browserWs.close();
}

run().catch(e => {
  console.error(e);
  process.exit(1);
});
