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

  // Find the exact bounding box of KHO ĐỀ THI THỬ in the right pane
  const rect = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        // Look in the right-side pages tree
        const allItems = Array.from(document.querySelectorAll('*'));
        const rightPaneItems = allItems.filter(el => {
          const r = el.getBoundingClientRect();
          return r.left > 800 && (el.innerText || '').trim() === 'KHO ĐỀ THI THỬ' && el.children.length === 0;
        });
        if (rightPaneItems.length > 0) {
          const el = rightPaneItems[0];
          const r = el.getBoundingClientRect();
          return { x: r.left + r.width / 2, y: r.top + r.height / 2, text: el.innerText };
        }
        return null;
      })()
    `,
    returnByValue: true
  }, sessionId);

  console.log('Target rect:', rect.result.value);

  if (rect.result.value) {
    const { x, y } = rect.result.value;
    console.log(`Dispatching mouse click at (${x}, ${y})`);
    await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mousePressed', x, y, button: 'left', clickCount: 1 }, sessionId);
    await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mouseReleased', x, y, button: 'left', clickCount: 1 }, sessionId);
  }

  await new Promise(r => setTimeout(r, 2000));

  // Screenshot after click
  const shot = await sendCommand(browserWs, 'Page.captureScreenshot', { format: 'png' }, sessionId);
  const brainDir = path.resolve(process.env.USERPROFILE || process.env.HOME, '.gemini/antigravity/brain/07f27e52-1325-4adc-9ec0-5c8e7670a48d/screenshots');
  const shotPath = path.join(brainDir, 'editor_kho_de_clicked.png');
  fs.writeFileSync(shotPath, Buffer.from(shot.data, 'base64'));
  console.log('Saved screenshot to:', shotPath);

  browserWs.close();
}

run().catch(e => {
  console.error(e);
  process.exit(1);
});
