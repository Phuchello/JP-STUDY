// scripts/tests/verify_n2_mock_05_audio_deep.cjs
// Deep Audio Playback, Decoding, and Integrity Verification for JLPT N2 Mock #05 (All 30 tracks)
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const crypto = require('crypto');
const assert = require('assert/strict');

const ROOT = path.resolve(__dirname, '../..');
const MANIFEST_PATH = path.join(ROOT, 'data/mock_exams/n2_mock_05_audio_manifest.json');
const AUDIO_DIR = path.join(ROOT, 'docs/audio/n2_mock_05');
const REPORT_OUT = path.join(ROOT, 'qa/N2_MOCK_05_DEEP_AUDIO_PLAYBACK_REPORT.md');
const RECEIPT_OUT = path.join(ROOT, 'qa/N2_MOCK_05_AUDIO_PLAYBACK_RECEIPT.json');

async function runDeepAudioVerification() {
  console.log('=== DEEP REAL AUDIO PLAYBACK & DECODING VERIFICATION FOR MOCK #05 (30 TRACKS) ===');
  assert.ok(fs.existsSync(MANIFEST_PATH), 'Manifest file must exist: ' + MANIFEST_PATH);
  const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf-8'));
  const trackKeys = Object.keys(manifest);
  assert.equal(trackKeys.length, 30, 'Manifest must have exactly 30 tracks');

  const examDataPath = path.join(ROOT, 'data/mock_exams/n2_mock_05.json');
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
    const relativeSrc = '../audio/n2_mock_05/' + filename;
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
              error: 'play() failed: ' + err.message
            });
          }
        });

        audio.addEventListener('timeupdate', () => {
          if (audio.currentTime > 0.05) {
            clearTimeout(timer);
            audio.pause();
            resolve({
              loaded: true,
              played: true,
              timeAdvanced: true,
              duration: audio.duration || 0,
              currentTime: audio.currentTime || 0,
              error: null
            });
          }
        });
      });
    }, relativeSrc);

    // 3. Real Chromium Decoding & Playback Test (Mobile Viewport)
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
            error: 'Mobile playback timeout after 5s'
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
              error: 'Mobile play() failed: ' + err.message
            });
          }
        });

        audio.addEventListener('timeupdate', () => {
          if (audio.currentTime > 0.05) {
            clearTimeout(timer);
            audio.pause();
            resolve({
              loaded: true,
              played: true,
              timeAdvanced: true,
              duration: audio.duration || 0,
              currentTime: audio.currentTime || 0,
              error: null
            });
          }
        });
      });
    }, relativeSrc);

    // 4. Acoustic Tier Assignment
    let acousticTier = 'AUDIO_FILE_MISSING';
    if (exists) {
      if (shaMatch) {
        if (playbackDesktop.loaded && playbackDesktop.duration > 0) {
          if (playbackDesktop.timeAdvanced && playbackMobile.timeAdvanced) {
            acousticTier = 'BROWSER_PLAYBACK_VERIFIED';
          } else {
            acousticTier = 'AUDIO_DECODES_FAILED_PLAYBACK';
          }
        } else {
          acousticTier = 'AUDIO_HASH_VERIFIED_DECODE_FAILED';
        }
      } else {
        acousticTier = 'AUDIO_HASH_MISMATCH';
      }
    }

    const examItem = itemMap.get(qid);
    const audioUrlInJson = examItem ? examItem.audioUrl : 'MISSING';
    const jsonMatchesManifest = (audioUrlInJson === `audio/n2_mock_05/${filename}`);

    const resObj = {
      questionId: qid,
      filename: filename,
      fileSizeBytes: localSize,
      expectedSha256: expectedSha,
      computedSha256: computedSha,
      sha256Match: shaMatch,
      manifestDurationSec: t.audioDurationSec,
      browserDecodedDurationSec: playbackDesktop.duration ? Math.round(playbackDesktop.duration * 10) / 10 : 0,
      desktopPlaybackAdvanced: playbackDesktop.timeAdvanced,
      mobilePlaybackAdvanced: playbackMobile.timeAdvanced,
      desktopError: playbackDesktop.error,
      mobileError: playbackMobile.error,
      acousticTier: acousticTier,
      jsonMatchesManifest: jsonMatchesManifest
    };

    results.push(resObj);
    console.log(`  -> Tier: ${acousticTier} | Desktop Adv: ${playbackDesktop.timeAdvanced} | Mobile Adv: ${playbackMobile.timeAdvanced} | Dur: ${resObj.browserDecodedDurationSec}s`);
  }

  await browser.close();

  // 5. Build Receipt
  const verifiedCount = results.filter(r => r.acousticTier === 'BROWSER_PLAYBACK_VERIFIED').length;
  const tracksDict = {};
  for (const r of results) {
    tracksDict[r.questionId] = {
      filename: r.filename,
      audioSha256: r.computedSha256,
      audioHashVerified: r.sha256Match,
      audioDecodes: (r.browserDecodedDurationSec > 0),
      browserPlaybackVerified: (r.acousticTier === 'BROWSER_PLAYBACK_VERIFIED'),
      acousticTier: r.acousticTier,
      durationSec: r.browserDecodedDurationSec,
      fileSizeBytes: r.fileSizeBytes,
      jsonMappingVerified: r.jsonMatchesManifest
    };
  }

  const receipt = {
    examId: 'N2-MOCK-05',
    verifiedAt: new Date().toISOString(),
    totalTracks: trackKeys.length,
    verifiedPlaybackCount: verifiedCount,
    allPassed: (verifiedCount === trackKeys.length),
    environment: {
      browser: 'Chromium Headless',
      desktopViewport: '1280x800',
      mobileViewport: '390x844 (Mobile Emulation)',
      audioContextPolicy: 'no-user-gesture-required'
    },
    tracks: tracksDict,
    results: results
  };

  fs.writeFileSync(RECEIPT_OUT, JSON.stringify(receipt, null, 2), 'utf-8');
  console.log(`\nWrote Playback Receipt to: ${RECEIPT_OUT}`);

  // 6. Build Markdown Report
  let md = `# JLPT N2 Mock Exam #05 — Deep Audio Playback & Decoding Verification Report\n\n`;
  md += `**Execution Timestamp:** ${receipt.verifiedAt}\n`;
  md += `**Environment:** Chromium Browser Engine (Desktop & Mobile 390px emulation)\n`;
  md += `**Scope:** All 30 Listening Tracks (${trackKeys[0]} to ${trackKeys[trackKeys.length - 1]})\n`;
  md += `**Overall Result:** ${receipt.allPassed ? '✅ 100% PASS (BROWSER_PLAYBACK_VERIFIED)' : '❌ FAIL'}\n\n`;

  md += `## Tier Breakdown\n\n`;
  const tiers = {};
  for (const r of results) {
    tiers[r.acousticTier] = (tiers[r.acousticTier] || 0) + 1;
  }
  for (const [t, cnt] of Object.entries(tiers)) {
    md += `- **${t}**: ${cnt} tracks\n`;
  }

  md += `\n## Detailed Track Verification Ledger\n\n`;
  md += `| Item ID | MP3 File | Size | Manifest Dur | Browser Dur | SHA-256 Match | Desktop Play | Mobile Play | Tier |\n`;
  md += `|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n`;

  for (const r of results) {
    const shaIcon = r.sha256Match ? '✅' : '❌';
    const deskIcon = r.desktopPlaybackAdvanced ? '✅' : '❌';
    const mobIcon = r.mobilePlaybackAdvanced ? '✅' : '❌';
    md += `| \`${r.questionId}\` | \`${r.filename}\` | ${r.fileSizeBytes.toLocaleString()} B | ${r.manifestDurationSec}s | ${r.browserDecodedDurationSec}s | ${shaIcon} | ${deskIcon} | ${mobIcon} | **${r.acousticTier}** |\n`;
  }

  fs.writeFileSync(REPORT_OUT, md, 'utf-8');
  console.log(`Wrote Deep Audio Report to: ${REPORT_OUT}`);

  assert.equal(verifiedCount, 30, `Expected 30 tracks to achieve BROWSER_PLAYBACK_VERIFIED, got ${verifiedCount}`);
  console.log('\n✅ ALL 30 AUDIO TRACKS FOR MOCK #05 FULLY VERIFIED IN REAL BROWSER PLAYBACK & DECODING!');
}

runDeepAudioVerification().catch(err => {
  console.error('\n❌ Audio verification failed:', err);
  process.exit(1);
});
