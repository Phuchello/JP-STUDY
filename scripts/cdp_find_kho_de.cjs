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
  const attachRes = await sendCommand(browserWs, 'Target.attachToTarget', { targetId: editorTarget.targetId, flatten: true });
  const sessionId = attachRes.sessionId;

  const res = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        const links = Array.from(document.querySelectorAll('a')).map(a => ({
          text: (a.innerText || '').trim(),
          href: a.href,
          dataHref: a.getAttribute('data-href'),
          target: a.target
        })).filter(x => x.text);
        return links;
      })()
    `,
    returnByValue: true
  }, sessionId);

  console.log('All links in editor:', JSON.stringify(res.result.value, null, 2));
  browserWs.close();
}
run();
