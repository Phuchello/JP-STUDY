const fs = require('fs');
const path = require('path');
const devToolsPort = '9222';
const devToolsActivePortFile = path.join(process.env.LOCALAPPDATA, 'Google/Chrome/User Data/DevToolsActivePort');
const browserWsPath = fs.readFileSync(devToolsActivePortFile, 'utf8').split('\n')[1].trim();

async function run() {
  const browserWs = new WebSocket('ws://127.0.0.1:' + devToolsPort + browserWsPath);
  await new Promise(r => browserWs.onopen = r);
  const targets = await new Promise(r => {
    browserWs.onmessage = e => r(JSON.parse(e.data).result);
    browserWs.send(JSON.stringify({ id: 1, method: 'Target.getTargets' }));
  });
  let pubTarget = targets.targetInfos.find(t => t.url && t.url.includes('sites.google.com/view/jp-study'));
  const attachRes = await new Promise(r => {
    browserWs.onmessage = e => r(JSON.parse(e.data).result);
    browserWs.send(JSON.stringify({ id: 2, method: 'Target.attachToTarget', params: { targetId: pubTarget.targetId, flatten: true } }));
  });
  const res = await new Promise(r => {
    browserWs.onmessage = e => r(JSON.parse(e.data).result);
    browserWs.send(JSON.stringify({
      id: 3,
      sessionId: attachRes.sessionId,
      method: 'Runtime.evaluate',
      params: {
        expression: `Array.from(document.querySelectorAll('a')).map(a => ({ text: (a.innerText || '').trim(), href: a.href })).filter(x => x.text && x.href.includes('sites.google.com'))`,
        returnByValue: true
      }
    }));
  });
  console.log(JSON.stringify(res.value, null, 2));
  browserWs.close();
}
run();
