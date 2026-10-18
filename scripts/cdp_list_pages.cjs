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
  const pages = targets.targetInfos.filter(t => t.type === 'page');
  console.log('Open Pages Count:', pages.length);
  pages.forEach(p => console.log(`- [${p.targetId}] "${p.title}" -> ${p.url}`));
  browserWs.close();
}
run();
