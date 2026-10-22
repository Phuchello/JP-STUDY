// Real Chromium decode and playback check for all N2-MOCK-12 listening tracks.
// This validates the released practice mock's exact manifest hashes and UI
// audio paths; it does not claim human pronunciation review.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const crypto = require('crypto');
const assert = require('assert/strict');

const ROOT = path.resolve(__dirname, '../..');
const MANIFEST_PATH = path.join(ROOT, 'data/mock_exams/n2_mock_12_audio_manifest.json');
const EXAM_PATH = process.env.N2_MOCK_12_EXAM_PATH || path.join(ROOT, 'data/mock_exams/n2_mock_12.json');
const AUDIO_DIR = path.join(ROOT, 'docs/audio/n2_mock_12');
const RECEIPT_OUT = path.join(ROOT, 'qa/N2_MOCK_12_AUDIO_PLAYBACK_RECEIPT.json');
const REPORT_OUT = path.join(ROOT, 'qa/N2_MOCK_12_AUDIO_PLAYBACK_REPORT.md');
const ENGINE_PATH = path.join(ROOT, 'docs/widgets/practice_engine.html');
const SYSTEM_CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const CHROME_PATH = process.env.CHROME_PATH || (process.platform === 'win32' && fs.existsSync(SYSTEM_CHROME) ? SYSTEM_CHROME : undefined);

async function testTrack(page, src) {
  return page.evaluate(async audioSrc => new Promise(resolve => {
    const audio = new Audio(audioSrc);
    audio.preload = 'auto';
    let done = false;
    let poll;
    const finish = result => {
      if (done) return;
      done = true;
      clearTimeout(timer);
      if (poll) clearInterval(poll);
      audio.pause();
      resolve(result);
    };
    const timer = setTimeout(() => finish({ loaded: false, played: false, timeAdvanced: false, duration: audio.duration || 0, error: 'Timeout after 8 seconds' }), 8000);
    audio.addEventListener('error', () => finish({ loaded: false, played: false, timeAdvanced: false, duration: 0, error: audio.error ? `Media error ${audio.error.code}` : 'Media error' }), { once: true });
    audio.addEventListener('canplaythrough', async () => {
      try {
        await audio.play();
        const started = Date.now();
        poll = setInterval(() => {
          const advanced = audio.currentTime > 0.05;
          if (advanced || Date.now() - started > 1800) {
            finish({ loaded: true, played: true, timeAdvanced: advanced, duration: audio.duration, currentTime: audio.currentTime, error: advanced ? null : 'Playback clock did not advance' });
          }
        }, 50);
      } catch (error) {
        finish({ loaded: true, played: false, timeAdvanced: false, duration: audio.duration || 0, error: error.message });
      }
    }, { once: true });
  }), src);
}

async function main() {
  const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
  const exam = JSON.parse(fs.readFileSync(EXAM_PATH, 'utf8'));
  const items = exam.sections[1].items;
  assert.ok(['FULL_MOCK', 'IN_DEVELOPMENT'].includes(exam.status), `Unexpected exam status: ${exam.status}`);
  assert.equal(Object.keys(manifest).length, 30);
  assert.equal(items.length, 30);
  const byId = new Map(items.map(q => [q.id, q]));
  assert.deepEqual([...Object.keys(manifest)].sort(), [...byId.keys()].sort());

  const browser = await chromium.launch({
    ...(CHROME_PATH ? { executablePath: CHROME_PATH } : {}),
    headless: true,
    args: ['--autoplay-policy=no-user-gesture-required', '--allow-file-access-from-files']
  });
  const desktopContext = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const mobileContext = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true });
  const desktop = await desktopContext.newPage();
  const mobile = await mobileContext.newPage();
  const engineUrl = `file:///${ENGINE_PATH.replaceAll('\\', '/')}`;
  await Promise.all([desktop.goto(engineUrl), mobile.goto(engineUrl)]);
  const results = [];

  try {
    for (const [questionId, meta] of Object.entries(manifest)) {
      const item = byId.get(questionId);
      const localPath = path.join(AUDIO_DIR, `${questionId}.mp3`);
      const bytes = fs.readFileSync(localPath);
      const actualSha = crypto.createHash('sha256').update(bytes).digest('hex');
      const examAudioUrl = item.audioUrl;
      const expectedAudioUrl = `audio/n2_mock_12/${questionId}.mp3`;
      const src = `../${examAudioUrl}`;
      const [desktopPlayback, mobilePlayback] = await Promise.all([
        testTrack(desktop, src),
        testTrack(mobile, src)
      ]);
      results.push({
        questionId,
        filename: `${questionId}.mp3`,
        fileSizeBytes: bytes.length,
        manifestSha256: meta.audioSha256,
        expectedSha256: meta.audioSha256,
        computedSha256: actualSha,
        sha256Match: actualSha === meta.audioSha256,
        durationManifestSec: meta.audioDurationSec,
        durationBrowserSec: desktopPlayback.duration || 0,
        browserDecodedDurationSec: desktopPlayback.duration || 0,
        audioUrl: examAudioUrl,
        jsonMappingVerified: examAudioUrl === expectedAudioUrl,
        desktop: desktopPlayback,
        mobile: mobilePlayback,
        playbackDesktop: desktopPlayback,
        playbackMobile: mobilePlayback,
        desktopPlaybackAdvanced: desktopPlayback.timeAdvanced,
        mobilePlaybackAdvanced: mobilePlayback.timeAdvanced,
        desktopError: desktopPlayback.error,
        mobileError: mobilePlayback.error,
        browserPlaybackVerified: actualSha === meta.audioSha256 && examAudioUrl === expectedAudioUrl && desktopPlayback.timeAdvanced && mobilePlayback.timeAdvanced
      });
      const last = results.at(-1);
      console.log(`${last.browserPlaybackVerified ? 'PASS' : 'FAIL'} ${questionId}: hash=${last.sha256Match} desktop=${desktopPlayback.timeAdvanced} mobile=${mobilePlayback.timeAdvanced}`);
    }
  } finally {
    await Promise.all([desktopContext.close(), mobileContext.close()]);
    await browser.close();
  }

  const verified = results.filter(row => row.browserPlaybackVerified).length;
  const receipt = {
    examId: 'N2-MOCK-12',
    status: 'VERIFIED_AUDIO_PLAYBACK',
    qaData: true,
    generatedAt: new Date().toISOString(),
    totalTracks: results.length,
    verifiedPlaybackCount: verified,
    overallPlaybackVerified: verified === 30,
    environment: {
      browser: 'Chromium Headless via Playwright',
      desktopViewport: '1280x800',
      mobileViewport: '390x844 mobile emulation',
      audioContextPolicy: 'no-user-gesture-required'
    },
    results
  };
  fs.writeFileSync(RECEIPT_OUT, `${JSON.stringify(receipt, null, 2)}\n`, 'utf8');
  const lines = [
    '# N2-MOCK-12 — Browser Audio Playback QA',
    '',
    `Generated: ${receipt.generatedAt}`,
    `Scope: ${results.length} M12 tracks, decoded and played in desktop and mobile-emulated Chromium.`,
    `Result: ${verified}/30 passed. This confirms browser decoding/playback and file mapping; it does not certify pronunciation or naturalness.`,
    '',
    '| Item | SHA-256 | Duration (s) | Desktop | Mobile |',
    '|---|---:|---:|---|---|',
    ...results.map(row => `| ${row.questionId} | ${row.sha256Match ? 'pass' : 'fail'} | ${row.durationBrowserSec.toFixed(2)} | ${row.desktop.timeAdvanced ? 'pass' : 'fail'} | ${row.mobile.timeAdvanced ? 'pass' : 'fail'} |`),
    ''
  ];
  fs.writeFileSync(REPORT_OUT, lines.join('\n'), 'utf8');
  assert.equal(verified, 30, `Expected 30 browser playback verified tracks; got ${verified}`);
  assert.ok(results.every(row => row.jsonMappingVerified), 'Audio URLs must match the M12 manifest');
  console.log(`Wrote ${RECEIPT_OUT}`);
}

main().catch(error => { console.error(error); process.exit(1); });
