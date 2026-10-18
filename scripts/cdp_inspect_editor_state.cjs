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
  let editorTarget = targets.targetInfos.find(t => t.url && t.url.includes('sites.google.com/d/'));
  if (!editorTarget) {
    console.log('No editor target');
    process.exit(1);
  }

  const attachRes = await sendCommand(browserWs, 'Target.attachToTarget', { targetId: editorTarget.targetId, flatten: true });
  const sessionId = attachRes.sessionId;

  console.log('Editor URL:', editorTarget.url);

  // Navigate directly to the KHO ĐỀ THI THỬ page in the editor if known, or inspect current editor state
  const state = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        return {
          title: document.title,
          url: window.location.href,
          iframes: Array.from(document.querySelectorAll('iframe')).map(f => ({
            id: f.id,
            src: f.src,
            rect: { top: f.getBoundingClientRect().top, left: f.getBoundingClientRect().left, width: f.getBoundingClientRect().width, height: f.getBoundingClientRect().height }
          }))
        };
      })()
    `,
    returnByValue: true
  }, sessionId);

  console.log('Editor state:', JSON.stringify(state.result.value, null, 2));

  browserWs.close();
}
run().catch(e => {
  console.error(e);
  process.exit(1);
});
