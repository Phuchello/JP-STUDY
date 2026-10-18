const fs = require('fs');
const path = require('path');
const devToolsPort = '9222';
const devToolsActivePortFile = path.join(process.env.LOCALAPPDATA, 'Google/Chrome/User Data/DevToolsActivePort');
const browserWsPath = fs.readFileSync(devToolsActivePortFile, 'utf8').split('\n')[1].trim();

async function run() {
  const browserWs = new WebSocket('ws://127.0.0.1:' + devToolsPort + browserWsPath);
  await new Promise(r => browserWs.onopen = r);

  const attachRes = await new Promise(r => {
    browserWs.onmessage = e => r(JSON.parse(e.data).result);
    browserWs.send(JSON.stringify({ id: 1, method: 'Target.attachToTarget', params: { targetId: '00DDC939ADEB353E2C365B1840587B12', flatten: true } }));
  });
  const sessionId = attachRes.sessionId;

  const shot = await new Promise(r => {
    browserWs.onmessage = e => r(JSON.parse(e.data).result);
    browserWs.send(JSON.stringify({ id: 2, sessionId, method: 'Page.captureScreenshot', params: { format: 'png' } }));
  });

  const brainDir = path.resolve(process.env.USERPROFILE || process.env.HOME, '.gemini/antigravity/brain/07f27e52-1325-4adc-9ec0-5c8e7670a48d/screenshots');
  const shotPath = path.join(brainDir, 'editor_current_screen.png');
  fs.writeFileSync(shotPath, Buffer.from(shot.data, 'base64'));
  console.log('Saved editor screenshot to:', shotPath);

  browserWs.close();
}
run().catch(e => {
  console.error(e);
  process.exit(1);
});
