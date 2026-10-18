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

  // Double click at (350, 880)
  console.log('Double clicking on embed at (350, 880)...');
  await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mousePressed', x: 350, y: 880, button: 'left', clickCount: 1 }, sessionId);
  await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mouseReleased', x: 350, y: 880, button: 'left', clickCount: 1 }, sessionId);
  await new Promise(r => setTimeout(r, 100));
  await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mousePressed', x: 350, y: 880, button: 'left', clickCount: 2 }, sessionId);
  await sendCommand(browserWs, 'Input.dispatchMouseEvent', { type: 'mouseReleased', x: 350, y: 880, button: 'left', clickCount: 2 }, sessionId);

  await new Promise(r => setTimeout(r, 2000));

  // Check if a modal / textarea or dialog opened
  const dialogInfo = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        const dialogs = Array.from(document.querySelectorAll('[role="dialog"], [role="alertdialog"]'));
        const textareas = Array.from(document.querySelectorAll('textarea'));
        return {
          dialogCount: dialogs.length,
          dialogTitles: dialogs.map(d => (d.innerText || '').slice(0, 100)),
          textareaCount: textareas.length,
          textareas: textareas.map(t => ({
            id: t.id,
            className: t.className,
            valLength: t.value.length,
            valSnippet: t.value.slice(0, 100)
          }))
        };
      })()
    `,
    returnByValue: true
  }, sessionId);

  console.log('Dialog check:', JSON.stringify(dialogInfo.result.value, null, 2));

  browserWs.close();
}
run().catch(e => {
  console.error(e);
  process.exit(1);
});
