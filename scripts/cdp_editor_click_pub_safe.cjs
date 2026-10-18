const fs = require('fs');
const path = require('path');
const devToolsPort = '9222';
const devToolsActivePortFile = path.join(process.env.LOCALAPPDATA, 'Google/Chrome/User Data/DevToolsActivePort');
const browserWsPath = fs.readFileSync(devToolsActivePortFile, 'utf8').split('\n')[1].trim();

function sendCommand(ws, method, params = {}, sessionId = null) {
  return new Promise((resolve, reject) => {
    const id = Math.floor(Math.random() * 1000000);
    const timer = setTimeout(() => {
      ws.removeEventListener('message', handler);
      reject(new Error(`Timeout waiting for response to ${method}`));
    }, 8000);
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
  let editorTarget = targets.targetInfos.find(t => t.url && t.url.includes('sites.google.com/d/'));
  if (!editorTarget) {
    console.log('No editor target');
    process.exit(1);
  }

  const attachRes = await sendCommand(browserWs, 'Target.attachToTarget', { targetId: editorTarget.targetId, flatten: true });
  const sessionId = attachRes.sessionId;
  console.log('Attached to editor target');

  // Query all buttons
  const res = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        return Array.from(document.querySelectorAll('button, [role="button"], div, span'))
          .filter(el => (el.innerText || '').trim() === 'Xuất bản')
          .map(el => {
            const r = el.getBoundingClientRect();
            return {
              tag: el.tagName,
              disabled: el.getAttribute('aria-disabled'),
              rect: { left: r.left, top: r.top, width: r.width, height: r.height }
            };
          });
      })()
    `,
    returnByValue: true
  }, sessionId);

  console.log('Xuất bản elements:', JSON.stringify(res.result.value, null, 2));

  // If there is an active button in the top right (top < 100, left > 1600)
  const activeBtn = res.result.value.find(b => b.rect.top < 100 && b.rect.left > 1600 && b.disabled !== 'true');
  if (activeBtn) {
    const x = activeBtn.rect.left + activeBtn.rect.width / 2;
    const y = activeBtn.rect.top + activeBtn.rect.height / 2;
    console.log(`Clicking active Xuất bản button at (${x}, ${y})...`);
    await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mousePressed', x, y, button: 'left', clickCount: 1 }, sessionId);
    await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mouseReleased', x, y, button: 'left', clickCount: 1 }, sessionId);
    console.log('Clicked! Waiting 4s for publication to finish...');
    await new Promise(r => setTimeout(r, 4000));
  } else {
    console.log('Active button not found or button is currently disabled');
  }

  browserWs.close();
}

run().catch(e => {
  console.error(e);
  process.exit(1);
});
