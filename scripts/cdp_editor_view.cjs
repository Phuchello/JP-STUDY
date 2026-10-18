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
    console.log('Editor target not found, targets:', targets.targetInfos.map(t => t.url));
    process.exit(1);
  }

  const attachRes = await sendCommand(browserWs, 'Target.attachToTarget', { targetId: editorTarget.targetId, flatten: true });
  const sessionId = attachRes.sessionId;

  console.log('Attached to editor:', editorTarget.title);

  // Take screenshot of editor
  const shot = await sendCommand(browserWs, 'Page.captureScreenshot', { format: 'png' }, sessionId);
  const brainDir = path.resolve(process.env.USERPROFILE || process.env.HOME, '.gemini/antigravity/brain/07f27e52-1325-4adc-9ec0-5c8e7670a48d/screenshots');
  const shotPath = path.join(brainDir, 'google_sites_editor_view.png');
  fs.writeFileSync(shotPath, Buffer.from(shot.data, 'base64'));
  console.log('Editor screenshot saved to:', shotPath);

  browserWs.close();
}

run().catch(e => {
  console.error(e);
  process.exit(1);
});
