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
  let pubTarget = targets.targetInfos.find(t => t.url && t.url.includes('sites.google.com/view/jp-study'));
  if (!pubTarget) {
    console.log('No published site target found');
    process.exit(1);
  }

  const attachRes = await sendCommand(browserWs, 'Target.attachToTarget', { targetId: pubTarget.targetId, flatten: true });
  const sessionId = attachRes.sessionId;

  console.log('Waiting 5s and scrolling to practice engine...');
  await new Promise(r => setTimeout(r, 5000));
  await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `window.scrollBy(0, 600);`
  }, sessionId);
  await new Promise(r => setTimeout(r, 2000));

  const shot = await sendCommand(browserWs, 'Page.captureScreenshot', { format: 'png' }, sessionId);
  const brainDir = path.resolve(process.env.USERPROFILE || process.env.HOME, '.gemini/antigravity/brain/07f27e52-1325-4adc-9ec0-5c8e7670a48d/screenshots');
  const shotPath = path.join(brainDir, 'published_kho_de_scrolled_rendered.png');
  fs.writeFileSync(shotPath, Buffer.from(shot.data, 'base64'));
  console.log('Saved rendered screenshot to:', shotPath);

  browserWs.close();
}
run().catch(e => {
  console.error(e);
  process.exit(1);
});
