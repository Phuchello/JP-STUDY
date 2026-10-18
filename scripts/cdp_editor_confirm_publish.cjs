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

  await new Promise(r => setTimeout(r, 4000));

  // Check the review dialog and find the confirm Publish button
  const confirmBtn = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        const btns = Array.from(document.querySelectorAll('[role="button"], button')).map(b => ({
          text: (b.innerText || '').trim(),
          disabled: b.getAttribute('aria-disabled') === 'true' || b.disabled,
          rect: { top: b.getBoundingClientRect().top, left: b.getBoundingClientRect().left, width: b.getBoundingClientRect().width, height: b.getBoundingClientRect().height }
        })).filter(b => b.text === 'Xuất bản');
        return btns;
      })()
    `,
    returnByValue: true
  }, sessionId);

  console.log('Confirm Publish buttons:', JSON.stringify(confirmBtn.result.value, null, 2));

  // If there's an enabled button, click it
  const targetBtn = confirmBtn.result.value.find(b => !b.disabled && b.rect.width > 0);
  if (targetBtn) {
    const x = targetBtn.rect.left + targetBtn.rect.width / 2;
    const y = targetBtn.rect.top + targetBtn.rect.height / 2;
    console.log(`Clicking confirm Publish at (${x}, ${y})...`);
    await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mousePressed', x, y, button: 'left', clickCount: 1 }, sessionId);
    await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mouseReleased', x, y, button: 'left', clickCount: 1 }, sessionId);
    await new Promise(r => setTimeout(r, 5000));
  } else {
    console.log('No enabled publish button found, checking if already published or nothing changed');
  }

  const shot = await sendCommand(browserWs, 'Page.captureScreenshot', { format: 'png' }, sessionId);
  const brainDir = path.resolve(process.env.USERPROFILE || process.env.HOME, '.gemini/antigravity/brain/07f27e52-1325-4adc-9ec0-5c8e7670a48d/screenshots');
  const shotPath = path.join(brainDir, 'editor_publish_completed.png');
  fs.writeFileSync(shotPath, Buffer.from(shot.data, 'base64'));
  console.log('Saved screenshot to:', shotPath);

  browserWs.close();
}

run().catch(e => {
  console.error(e);
  process.exit(1);
});
