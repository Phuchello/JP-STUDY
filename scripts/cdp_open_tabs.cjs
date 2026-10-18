const fs = require('fs');
const path = require('path');
const devToolsPort = '9222';
const devToolsActivePortFile = path.join(process.env.LOCALAPPDATA, 'Google/Chrome/User Data/DevToolsActivePort');
const browserWsPath = fs.readFileSync(devToolsActivePortFile, 'utf8').split('\n')[1].trim();

function sendCommand(ws, method, params = {}) {
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
    ws.send(JSON.stringify({ id, method, params }));
  });
}

async function run() {
  const browserWs = new WebSocket('ws://127.0.0.1:' + devToolsPort + browserWsPath);
  await new Promise(r => browserWs.onopen = r);

  console.log('Creating new tab for published site...');
  const res1 = await sendCommand(browserWs, 'Target.createTarget', { url: 'https://sites.google.com/view/jp-study' });
  console.log('Created published site tab:', res1.targetId);

  console.log('Creating new tab for Sites editor...');
  const res2 = await sendCommand(browserWs, 'Target.createTarget', { url: 'https://sites.google.com/d/1QwlrmMjrjtJ9vKnylnML7DemY3BmRBwQ' });
  console.log('Created Sites editor tab:', res2.targetId);

  browserWs.close();
}
run().catch(e => {
  console.error(e);
  process.exit(1);
});
