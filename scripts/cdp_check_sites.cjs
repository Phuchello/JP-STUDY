const fs = require('fs');
const path = require('path');

const devToolsPort = '9222';
const devToolsActivePortFile = path.join(process.env.LOCALAPPDATA, 'Google/Chrome/User Data/DevToolsActivePort');
const portData = fs.readFileSync(devToolsActivePortFile, 'utf8').split('\n');
const browserWsPath = portData[1].trim();

async function run() {
  const browserWsUrl = `ws://127.0.0.1:${devToolsPort}${browserWsPath}`;
  const browserWs = new WebSocket(browserWsUrl);
  await new Promise(r => browserWs.onopen = r);

  const targets = await sendCommand(browserWs, 'Target.getTargets');
  console.log('All targets:');
  targets.targetInfos.forEach(t => {
    if (t.type === 'page') console.log('-', t.targetId, t.title, t.url);
  });

  // Check the published page
  let pubTarget = targets.targetInfos.find(t => t.url && t.url.includes('sites.google.com/view/jp-study'));
  if (pubTarget) {
    const attachRes = await sendCommand(browserWs, 'Target.attachToTarget', { targetId: pubTarget.targetId, flatten: true });
    const sessionId = attachRes.sessionId;

    async function sendSession(method, params = {}) {
      return new Promise((resolve, reject) => {
        const id = Math.floor(Math.random() * 1000000);
        function handler(event) {
          const msg = JSON.parse(event.data);
          if (msg.id === id) {
            browserWs.removeEventListener('message', handler);
            if (msg.error) reject(msg.error);
            else resolve(msg.result);
          }
        }
        browserWs.addEventListener('message', handler);
        browserWs.send(JSON.stringify({ id, sessionId, method, params }));
      });
    }

    console.log('Inspecting published site:', pubTarget.url);
    const iframes = await sendSession('Runtime.evaluate', {
      expression: `
        (() => {
          const frames = Array.from(document.querySelectorAll('iframe')).map(f => f.src);
          return { title: document.title, url: window.location.href, iframes: frames };
        })()
      `,
      returnByValue: true
    });
    console.log('Published site iframes:', iframes.result.value);
  }

  browserWs.close();
}

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

run().catch(e => {
  console.error(e);
  process.exit(1);
});
