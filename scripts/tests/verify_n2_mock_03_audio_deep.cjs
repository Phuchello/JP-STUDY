// scripts/tests/verify_n2_mock_03_audio_deep.cjs
// Deep Audio Playback, Decoding, and Integrity Verification for JLPT N2 Mock #03 (All 30 tracks)
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const crypto = require('crypto');
const assert = require('assert/strict');

const ROOT = path.resolve(__dirname, '../..');
const MANIFEST_PATH = path.join(ROOT, 'data/mock_exams/n2_mock_03_audio_manifest.json');
const AUDIO_DIR = path.join(ROOT, 'docs/audio/n2_mock_03');
const REPORT_OUT = path.join(ROOT, 'qa/N2_MOCK_03_DEEP_AUDIO_PLAYBACK_REPORT.md');
const RECEIPT_OUT = path.join(ROOT, 'qa/N2_MOCK_03_AUDIO_PLAYBACK_RECEIPT.json');

async function runDeepAudioVerification() {
  console.log('=== DEEP REAL AUDIO PLAYBACK & DECODING VERIFICATION FOR MOCK #03 (30 TRACKS) ===');
  assert.ok(fs.existsSync(MANIFEST_PATH), 'Manifest file must exist: ' + MANIFEST_PATH);
  const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf-8'));
  const trackKeys = Object.keys(manifest);
  assert.equal(trackKeys.length, 30, 'Manifest must have exactly 30 tracks');

  const examDataPath = path.join(ROOT, 'data/mock_exams/n2_mock_03.json');
  assert.ok(fs.existsSync(examDataPath), 'Exam JSON must exist');
  const examData = JSON.parse(fs.readFileSync(examDataPath, 'utf-8'));
  const examItems = (examData.sections && examData.sections[1] ? examData.sections[1].items : []);
  const itemMap = new Map(examItems.map(item => [item.id, item]));

  const browser = await chromium.launch({
    headless: true,
    args: ['--autoplay-policy=no-user-gesture-required', '--allow-file-access-from-files']
  });
  const engineFileUrl = 'file:///' + path.join(ROOT, 'docs/widgets/practice_engine.html').replaceAll('\\', '/');
  const desktopPage = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  await desktopPage.goto(engineFileUrl);

  const mobilePage = await browser.newPage({ viewport: { width: 390, height: 844 }, isMobile: true });
  await mobilePage.goto(engineFileUrl);

  const results = [];

  for (let i = 0; i < trackKeys.length; i++) {
    const qid = trackKeys[i];
    const t = manifest[qid];
    const filename = `${qid}.mp3`;
    const expectedSha = t.audioSha256;
    const localPath = path.join(AUDIO_DIR, filename);

    console.log(`\n[${i + 1}/30] Testing ${qid} (${filename})...`);

    // 1. ASSET_EXISTS & Hash Verification
    const exists = fs.existsSync(localPath);
    let shaMatch = false;
    let localSize = 0;
    let computedSha = '';
    if (exists) {
      const fileBytes = fs.readFileSync(localPath);
      localSize = fileBytes.length;
      computedSha = crypto.createHash('sha256').update(fileBytes).digest('hex');
      shaMatch = (computedSha.toLowerCase() === expectedSha.toLowerCase());
    }

    // 2. Real Chromium Decoding & Playback Test (Desktop)
    const relativeSrc = '../audio/n2_mock_03/' + filename;
    const playbackDesktop = await desktopPage.evaluate(async (audioSrc) => {
      return new Promise((resolve) => {
        const audio = new Audio(audioSrc);
        audio.preload = 'auto';

        const timer = setTimeout(() => {
          resolve({
            loaded: false,
            played: false,
            timeAdvanced: false,
            duration: audio.duration || 0,
            currentTime: audio.currentTime || 0,
            error: 'Playback timeout after 5s'
          });
        }, 5000);

        audio.addEventListener('error', (e) => {
          clearTimeout(timer);
          resolve({
            loaded: false,
            played: false,
            timeAdvanced: false,
            duration: 0,
            currentTime: 0,
            error: audio.error ? `Code ${audio.error.code}: ${audio.error.message}` : 'Media error'
          });
        });

        let playTriggered = false;
        audio.addEventListener('canplaythrough', async () => {
          if (playTriggered) return;
          playTriggered = true;
          try {
            await audio.play();
          } catch (err) {
            clearTimeout(timer);
            resolve({
              loaded: true,
              played: false,
              timeAdvanced: false,
              duration: audio.duration || 0,
              currentTime: audio.currentTime || 0,
              error: err.message
            });
            return;
          }

          const startPoll = Date.now();
          const pollInterval = setInterval(() => {
            if (audio.currentTime > 0.05 || Date.now() - startPoll > 1500) {
              clearInterval(pollInterval);
              clearTimeout(timer);
              const timeAdvanced = (audio.currentTime > 0.05);
              const curTime = audio.currentTime;
              audio.pause();
              resolve({
                loaded: true,
                played: true,
                timeAdvanced: timeAdvanced,
                duration: audio.duration,
                currentTime: curTime,
                error: null
              });
            }
          }, 50);
        });
      });
    }, relativeSrc);

    // 3. Real Chromium Decoding & Playback Test (Mobile Viewport 390px)
    const playbackMobile = await mobilePage.evaluate(async (audioSrc) => {
      return new Promise((resolve) => {
        const audio = new Audio(audioSrc);
        audio.preload = 'auto';

        const timer = setTimeout(() => {
          resolve({
            loaded: false,
            played: false,
            timeAdvanced: false,
            duration: audio.duration || 0,
            currentTime: audio.currentTime || 0,
            error: 'Mobile playback timeout'
          });
        }, 5000);

        audio.addEventListener('error', () => {
          clearTimeout(timer);
          resolve({ loaded: false, played: false, timeAdvanced: false, error: 'Mobile media error' });
        });

        let played = false;
        audio.addEventListener('canplaythrough', async () => {
          if (played) return;
          played = true;
          try {
            await audio.play();
          } catch (e) {
            clearTimeout(timer);
            resolve({ loaded: true, played: false, timeAdvanced: false, error: e.message });
            return;
          }
          const startPoll = Date.now();
          const pollInterval = setInterval(() => {
            if (audio.currentTime > 0.05 || Date.now() - startPoll > 1500) {
              clearInterval(pollInterval);
              clearTimeout(timer);
              const adv = (audio.currentTime > 0.05);
              const curTime = audio.currentTime;
              audio.pause();
              resolve({ loaded: true, played: true, timeAdvanced: adv, duration: audio.duration, currentTime: curTime });
            }
          }, 50);
        });
      });
    }, relativeSrc);

    // 4. Determine Acoustic Tier
    let acousticTier = 'AUDIO_FILE_MISSING';
    if (exists) {
      if (shaMatch) {
        if (playbackDesktop.loaded && playbackDesktop.duration > 0) {
          if (playbackDesktop.timeAdvanced && playbackMobile.timeAdvanced) {
            acousticTier = 'BROWSER_PLAYBACK_VERIFIED';
          } else {
            acousticTier = 'AUDIO_DECODES';
          }
        } else {
          acousticTier = 'AUDIO_HASH_VERIFIED';
        }
      } else {
        acousticTier = 'AUDIO_FILE_EXISTS';
      }
    }

    const examItem = itemMap.get(qid);
    const audioUrlInJson = examItem ? examItem.audioUrl : 'MISSING';
    const jsonMatches = audioUrlInJson.includes(filename);

    console.log(`  -> Size: ${localSize} bytes | SHA Match: ${shaMatch} | Desktop Time Adv: ${playbackDesktop.timeAdvanced} | Mobile Time Adv: ${playbackMobile.timeAdvanced}`);
    console.log(`  -> Acoustic Tier: ${acousticTier}`);

    results.push({
      qid,
      filename,
      expectedSha,
      computedSha,
      shaMatch,
      localSize,
      durationReported: t.audioDurationSec,
      durationDecodedDesktop: playbackDesktop.duration,
      desktopPlayed: playbackDesktop.played,
      desktopTimeAdvanced: playbackDesktop.timeAdvanced,
      desktopError: playbackDesktop.error,
      mobilePlayed: playbackMobile.played,
      mobileTimeAdvanced: playbackMobile.timeAdvanced,
      mobileError: playbackMobile.error,
      jsonMappingVerified: jsonMatches,
      audioUrlInJson,
      acousticTier,
      isVerified: (acousticTier === 'BROWSER_PLAYBACK_VERIFIED' && jsonMatches)
    });
  }

  await browser.close();

  // Write Playwright Receipt JSON
  const tracksReceipt = {};
  for (const r of results) {
    tracksReceipt[r.qid] = {
      filename: r.filename,
      audioSha256: r.computedSha,
      audioHashVerified: r.shaMatch,
      audioDecodes: (r.durationDecodedDesktop > 0),
      browserPlaybackVerified: (r.acousticTier === 'BROWSER_PLAYBACK_VERIFIED'),
      acousticTier: r.acousticTier,
      durationSec: r.durationDecodedDesktop,
      fileSizeBytes: r.localSize,
      jsonMappingVerified: r.jsonMappingVerified
    };
  }

  const receiptData = {
    examId: 'N2-MOCK-03',
    generatedAt: new Date().toISOString(),
    totalTracks: results.length,
    verifiedPlaybackCount: results.filter(r => r.isVerified).length,
    overallPlaybackVerified: results.every(r => r.isVerified),
    environment: {
      browser: 'Chromium Headless',
      desktopViewport: '1280x800',
      mobileViewport: '390x844 (Mobile Emulation)',
      audioContextPolicy: 'no-user-gesture-required'
    },
    tracks: tracksReceipt
  };

  fs.writeFileSync(RECEIPT_OUT, JSON.stringify(receiptData, null, 2), 'utf-8');
  console.log(`\nWrote Playwright Audio Receipt to: ${RECEIPT_OUT}`);

  // Write Detailed Markdown Report
  let md = '# JLPT N2 Full Mock #03 — Deep Real Audio Playback & Decoding Verification Report\n\n';
  md += `**Generated:** ${new Date().toISOString()}\n`;
  md += `**Scope:** All 30 Section 2 Listening Audio Assets\n`;
  md += `**Execution Environment:** Chromium Headless (Automated Playback & AudioContext Media Decoding)\n\n`;

  md += '## 1. Executive Summary\n\n';
  const allPassed = results.every(r => r.isVerified);
  md += `| Total Audio Tracks | SHA-256 Verified | Chromium Decoded | Browser Playback Verified | Final Status |\n`;
  md += `| :---: | :---: | :---: | :---: | :---: |\n`;
  md += `| **30 / 30** | **${results.filter(r => r.shaMatch).length} / 30** | **${results.filter(r => r.durationDecodedDesktop > 0).length} / 30** | **${results.filter(r => r.acousticTier === 'BROWSER_PLAYBACK_VERIFIED').length} / 30** | **${allPassed ? '✅ 100% PASS' : '❌ DEFECTS DETECTED'}** |\n\n`;

  md += '## 2. Track-by-Track Acoustic Verification Ledger\n\n';
  md += '| # | Question ID | Filename | Size (Bytes) | SHA-256 Match | Decoded Dur (s) | Desktop Play | Mobile (390px) | JSON Map | Acoustic Tier |\n';
  md += '| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |\n';
  results.forEach((r, idx) => {
    md += `| ${idx + 1} | \`${r.qid}\` | \`${r.filename}\` | ${r.localSize.toLocaleString()} | ${r.shaMatch ? '✅' : '❌'} | ${r.durationDecodedDesktop.toFixed(1)}s | ${r.desktopTimeAdvanced ? '✅' : '❌'} | ${r.mobileTimeAdvanced ? '✅' : '❌'} | ${r.jsonMappingVerified ? '✅' : '❌'} | **\`${r.acousticTier}\`** |\n`;
  });

  fs.writeFileSync(REPORT_OUT, md, 'utf-8');
  console.log(`Wrote Deep Audio Report to: ${REPORT_OUT}`);

  assert.ok(allPassed, 'All 30 tracks must be BROWSER_PLAYBACK_VERIFIED');
  console.log('\n=== ALL 30 AUDIO TRACKS FULLY VERIFIED IN HEADLESS CHROMIUM ===\n');
}

runDeepAudioVerification().catch(err => {
  console.error('\n❌ Audio verification failed:', err);
  process.exit(1);
});
