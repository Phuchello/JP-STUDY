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

  // Click on the iframe container at (300, 860)
  console.log('Clicking on embed block at (300, 860)...');
  await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mousePressed', x: 300, y: 860, button: 'left', clickCount: 1 }, sessionId);
  await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mouseReleased', x: 300, y: 860, button: 'left', clickCount: 1 }, sessionId);

  await new Promise(r => setTimeout(r, 1500));

  // Inspect any floating toolbars or buttons that appeared
  const toolbars = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        const btns = Array.from(document.querySelectorAll('[role="button"], [aria-label]')).map(b => ({
          ariaLabel: b.getAttribute('aria-label'),
          text: (b.innerText || '').trim(),
          rect: { top: b.getBoundingClientRect().top, left: b.getBoundingClientRect().left, width: b.getBoundingClientRect().width, height: b.getBoundingClientRect().height }
        })).filter(b => b.ariaLabel || b.text);
        return btns.filter(b => b.rect.top > 700 && b.rect.top < 950);
      })()
    `,
    returnByValue: true
  }, sessionId);

  console.log('Nearby buttons:', JSON.stringify(toolbars.result.value, null, 2));

  browserWs.close();
}
run().catch(e => {
  console.error(e);
  process.exit(1);
});
