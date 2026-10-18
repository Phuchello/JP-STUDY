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

  // Find the "Xuất bản" button
  const pubBtn = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        const btns = Array.from(document.querySelectorAll('[role="button"], div, span'));
        const target = btns.find(b => (b.innerText || '').trim() === 'Xuất bản');
        if (target) {
          const r = target.getBoundingClientRect();
          return { x: r.left + r.width / 2, y: r.top + r.height / 2, text: target.innerText };
        }
        return null;
      })()
    `,
    returnByValue: true
  }, sessionId);

  console.log('Publish button rect:', pubBtn.result.value);

  if (pubBtn.result.value) {
    const { x, y } = pubBtn.result.value;
    console.log(`Clicking Publish at (${x}, ${y})...`);
    await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mousePressed', x, y, button: 'left', clickCount: 1 }, sessionId);
    await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mouseReleased', x, y, button: 'left', clickCount: 1 }, sessionId);
  }

  await new Promise(r => setTimeout(r, 3000));

  // Check what appeared
  const status = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        const dialogs = Array.from(document.querySelectorAll('[role="dialog"], [role="alertdialog"]'));
        const buttons = Array.from(document.querySelectorAll('[role="button"]')).map(b => (b.innerText || '').trim()).filter(Boolean);
        return {
          url: window.location.href,
          dialogCount: dialogs.length,
          dialogText: dialogs.map(d => d.innerText.slice(0, 200)),
          buttons: buttons.slice(0, 20)
        };
      })()
    `,
    returnByValue: true
  }, sessionId);

  console.log('Post-publish click status:', JSON.stringify(status.result.value, null, 2));

  // Take screenshot
  const shot = await sendCommand(browserWs, 'Page.captureScreenshot', { format: 'png' }, sessionId);
  const brainDir = path.resolve(process.env.USERPROFILE || process.env.HOME, '.gemini/antigravity/brain/07f27e52-1325-4adc-9ec0-5c8e7670a48d/screenshots');
  const shotPath = path.join(brainDir, 'editor_after_publish_click.png');
  fs.writeFileSync(shotPath, Buffer.from(shot.data, 'base64'));
  console.log('Saved screenshot to:', shotPath);

  browserWs.close();
}

run().catch(e => {
  console.error(e);
  process.exit(1);
});
