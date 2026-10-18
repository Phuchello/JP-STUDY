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
  let pubTarget = targets.targetInfos.find(t => t.url && t.url.includes('sites.google.com/view/jp-study'));
  if (!pubTarget) {
    console.error('No published site tab found');
    process.exit(1);
  }

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

  const pagesToInspect = [
    { name: 'kho_de_luyen', url: 'https://sites.google.com/view/jp-study/kho-de-luyen' },
    { name: 'jlpt_n2', url: 'https://sites.google.com/view/jp-study/jlpt-n2' }
  ];

  const brainDir = path.resolve(process.env.USERPROFILE || process.env.HOME, '.gemini/antigravity/brain/07f27e52-1325-4adc-9ec0-5c8e7670a48d/screenshots');

  for (const p of pagesToInspect) {
    console.log(`Navigating to ${p.url}...`);
    await sendSession('Page.navigate', { url: p.url });
    await new Promise(r => setTimeout(r, 4000));

    const pageInfo = await sendSession('Runtime.evaluate', {
      expression: `
        (() => {
          return {
            title: document.title,
            iframes: Array.from(document.querySelectorAll('iframe')).map(f => f.src)
          };
        })()
      `,
      returnByValue: true
    });
    console.log(`Page Info (${p.name}):`, pageInfo.result.value);

    const shot = await sendSession('Page.captureScreenshot', { format: 'png' });
    const shotPath = path.join(brainDir, `published_${p.name}_latest.png`);
    fs.writeFileSync(shotPath, Buffer.from(shot.data, 'base64'));
    console.log(`Saved screenshot to ${shotPath}`);
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
