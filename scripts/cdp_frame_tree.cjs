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
    console.log('No published site tab found');
    process.exit(1);
  }

  const attachRes = await sendCommand(browserWs, 'Target.attachToTarget', { targetId: pubTarget.targetId, flatten: true });
  const sessionId = attachRes.sessionId;

  const frameTree = await sendCommand(browserWs, 'Page.getFrameTree', {}, sessionId);
  console.log('Frame Tree Root:', frameTree.frameTree.frame.url);

  function listFrames(node) {
    const frames = [node.frame];
    if (node.childFrames) {
      for (const c of node.childFrames) {
        frames.push(...listFrames(c));
      }
    }
    return frames;
  }

  const allFrames = listFrames(frameTree.frameTree);
  console.log('Total frames:', allFrames.length);
  allFrames.forEach(f => console.log(`- Frame ${f.id} (${f.name || 'unnamed'}): ${f.url.slice(0, 80)}`));

  browserWs.close();
}
run().catch(e => {
  console.error(e);
  process.exit(1);
});
