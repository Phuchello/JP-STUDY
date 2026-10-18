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

  // Evaluate elements in editor
  const res = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        // Find tabs in right drawer
        const tabs = Array.from(document.querySelectorAll('[role="tab"]')).map(t => ({
          text: t.innerText,
          selected: t.getAttribute('aria-selected')
        }));
        return { tabs };
      })()
    `,
    returnByValue: true
  }, sessionId);

  console.log('Editor Tabs:', res.result.value);

  // Click on "Trang" tab (Pages tab)
  await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        const pagesTab = Array.from(document.querySelectorAll('[role="tab"]')).find(t => t.innerText && t.innerText.includes('Trang'));
        if (pagesTab) pagesTab.click();
      })()
    `
  }, sessionId);

  await new Promise(r => setTimeout(r, 1000));

  // Get list of pages from the pages panel
  const pagesList = await sendCommand(browserWs, 'Runtime.evaluate', {
    expression: `
      (() => {
        const pageItems = Array.from(document.querySelectorAll('[data-page-id], [role="treeitem"], [data-view-id]')).map(el => (el.innerText || '').trim()).filter(Boolean);
        return { pageItems: Array.from(new Set(pageItems)).slice(0, 30) };
      })()
    `,
    returnByValue: true
  }, sessionId);

  console.log('Pages List:', pagesList.result.value);

  // Take screenshot of pages panel
  const shot = await sendCommand(browserWs, 'Page.captureScreenshot', { format: 'png' }, sessionId);
  const brainDir = path.resolve(process.env.USERPROFILE || process.env.HOME, '.gemini/antigravity/brain/07f27e52-1325-4adc-9ec0-5c8e7670a48d/screenshots');
  const shotPath = path.join(brainDir, 'editor_pages_panel.png');
  fs.writeFileSync(shotPath, Buffer.from(shot.data, 'base64'));
  console.log('Saved screenshot to:', shotPath);

  browserWs.close();
}

run().catch(e => {
  console.error(e);
  process.exit(1);
});
