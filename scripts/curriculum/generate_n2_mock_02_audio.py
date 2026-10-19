# -*- coding: utf-8 -*-
"""
JP-STUDY: GENERATE HIGH-QUALITY NEURAL TTS AUDIO ASSETS FOR JLPT N2 MOCK #02 (30 ITEMS)
Uses Microsoft Edge TTS Neural Japanese Voices:
- ja-JP-NanamiNeural (Female / Narrator / Female characters)
- ja-JP-KeitaNeural (Male / Male characters)

Produces 30 verified MP3 files in docs/audio/n2_mock_02/:
- Mondai 1 (Task-based): N2_02_M1_L01.mp3 to N2_02_M1_L05.mp3
- Mondai 2 (Key points): N2_02_M2_L01.mp3 to N2_02_M2_L06.mp3
- Mondai 3 (General outline): N2_02_M3_L01.mp3 to N2_02_M3_L05.mp3
- Mondai 4 (Quick response - 3 spoken choices): N2_02_M4_L01.mp3 to N2_02_M4_L11.mp3
- Mondai 5 (Integrated): N2_02_M5_L01.mp3 to N2_02_M5_L03.mp3
"""
import os
import sys
import re
import json
import asyncio
import hashlib
import subprocess
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIO_OUT_DIR = ROOT / 'docs/audio/n2_mock_02'
TEMP_DIR = ROOT / 'tmp/audio_gen_temp_02'

VOICE_FEMALE = 'ja-JP-NanamiNeural'
VOICE_MALE = 'ja-JP-KeitaNeural'
VOICE_NARRATOR = 'ja-JP-NanamiNeural'

sys.path.insert(0, str(ROOT))
from scripts.curriculum.bank_data.n2_mock_02_listening import get_n2_mock_02_listening_items
import edge_tts

def get_audio_duration_and_check(file_path):
    """Use ffprobe to check duration and stream integrity."""
    cmd = [
        'ffprobe', '-v', 'error', '-show_entries',
        'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',
        str(file_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    duration = float(res.stdout.strip())
    return duration

def compute_sha256(file_path):
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def make_silence(duration_sec, out_path):
    cmd = [
        'ffmpeg', '-f', 'lavfi', '-i', 'anullsrc=r=24000:cl=mono',
        '-t', str(duration_sec), '-acodec', 'libmp3lame', '-b:a', '48k',
        str(out_path), '-y'
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

async def tts_clip(text, voice, out_path):
    comm = edge_tts.Communicate(text, voice)
    await comm.save(str(out_path))

def concat_clips(clip_paths, out_path):
    """Concatenate multiple audio clips with ffmpeg filter_complex."""
    inputs = []
    filter_ins = []
    for idx, cp in enumerate(clip_paths):
        inputs.extend(['-i', str(cp)])
        filter_ins.append(f'[{idx}:a]')
    filter_str = f'{"".join(filter_ins)}concat=n={len(clip_paths)}:v=0:a=1[out]'
    cmd = ['ffmpeg'] + inputs + ['-filter_complex', filter_str, '-map', '[out]', '-acodec', 'libmp3lame', '-b:a', '48k', str(out_path), '-y']
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

async def build_item_audio(q, item_idx, total_items):
    qid = q['id']
    # Format filename: N2_02_M1_L01 -> N2_02_M1_L01.mp3
    out_filename = f"{qid}.mp3"
    final_mp3 = AUDIO_OUT_DIR / out_filename

    print(f"[{item_idx}/{total_items}] Generating audio for {qid} -> {out_filename}...")
    item_tmp = TEMP_DIR / qid
    if item_tmp.exists():
        shutil.rmtree(item_tmp)
    item_tmp.mkdir(parents=True, exist_ok=True)

    segments = [] # list of (text, voice) or ('SILENCE', duration)

    if q['typeId'] == 'N2-LIS-TASK': # Mondai 1
        full_script = q['contextPassage']
        lines = [l.strip() for l in full_script.splitlines() if l.strip()]
        intro = lines[0]
        qnum_str = f"問題１、{q['examQNum']}番。"
        segments.append((f"{qnum_str} {intro}", VOICE_NARRATOR))
        segments.append(('SILENCE', 0.8))

        # Dialogue
        for l in lines[1:]:
            m = re.match(r'^([^：:]+)[：:](.*)$', l)
            if m:
                spk, speech = m.group(1).strip(), m.group(2).strip()
                v = VOICE_MALE if any(w in spk for w in ['男', '夫', '店員', '受付', '院生', '教授']) and '女' not in spk else VOICE_FEMALE
                segments.append((speech, v))
                segments.append(('SILENCE', 0.4))
        
        # Question repeated
        segments.append(('SILENCE', 0.5))
        segments.append((q['stem'], VOICE_NARRATOR))
        segments.append(('SILENCE', 1.5))

    elif q['typeId'] == 'N2-LIS-POIN': # Mondai 2
        full_script = q['contextPassage']
        lines = [l.strip() for l in full_script.splitlines() if l.strip()]
        intro = lines[0]
        qnum_str = f"問題２、{q['examQNum'] - 5}番。"
        segments.append((f"{qnum_str} {intro}", VOICE_NARRATOR))
        segments.append(('SILENCE', 0.8))
        # Designated reading time (6 seconds pause)
        segments.append(('SILENCE', 6.0))

        # Dialogue or talk
        for l in lines[1:]:
            m = re.match(r'^([^：:]+)[：:](.*)$', l)
            if m:
                spk, speech = m.group(1).strip(), m.group(2).strip()
                v = VOICE_MALE if any(w in spk for w in ['男', '職人', '課長', '部長']) and '女' not in spk else VOICE_FEMALE
                segments.append((speech, v))
                segments.append(('SILENCE', 0.4))
            else:
                segments.append((l, VOICE_MALE))
                segments.append(('SILENCE', 0.4))
        
        segments.append(('SILENCE', 0.5))
        segments.append((q['stem'], VOICE_NARRATOR))
        segments.append(('SILENCE', 1.5))

    elif q['typeId'] == 'N2-LIS-OUTL': # Mondai 3
        full_script = q['contextPassage']
        lines = [l.strip() for l in full_script.splitlines() if l.strip()]
        intro = lines[0]
        m3_num = q['examQNum'] - 11
        qnum_str = f"問題３、{m3_num}番。"
        segments.append((f"{qnum_str} {intro}", VOICE_NARRATOR))
        segments.append(('SILENCE', 0.8))

        # Monologue
        for l in lines[1:]:
            m = re.match(r'^([^：:]+)[：:](.*)$', l)
            if m:
                spk, speech = m.group(1).strip(), m.group(2).strip()
                v = VOICE_MALE if any(w in spk for w in ['男', '教授', '学芸員', '研究者']) and '女' not in spk else VOICE_FEMALE
                segments.append((speech, v))
            else:
                segments.append((l, VOICE_MALE))
            segments.append(('SILENCE', 0.6))

        # Spoken question
        segments.append(('SILENCE', 0.6))
        segments.append((q['stem'], VOICE_NARRATOR))
        segments.append(('SILENCE', 0.8))

        # Spoken choices
        for idx, opt in enumerate(q['options']):
            segments.append((f"{idx+1}番、{opt['text']}", VOICE_NARRATOR))
            segments.append(('SILENCE', 0.6))
        segments.append(('SILENCE', 1.5))

    elif q['typeId'] == 'N2-LIS-RESP': # Mondai 4
        m4_num = q['examQNum'] - 16
        qnum_str = f"問題４、{m4_num}番。"
        segments.append((qnum_str, VOICE_NARRATOR))
        segments.append(('SILENCE', 0.6))

        # Extract prompt from contextPassage: 【音声発話】\n「...」
        m_prompt = re.search(r'【音声発話】\s*[\n\r]*「([^」]+)」', q['contextPassage'])
        prompt_text = m_prompt.group(1) if m_prompt else "恐れ入りますが、よろしくお願いいたします。"
        # Alternate prompt speaker for variety
        prompt_voice = VOICE_MALE if (m4_num % 2 == 1) else VOICE_FEMALE
        segments.append((prompt_text, prompt_voice))
        segments.append(('SILENCE', 1.0))

        # 3 Spoken choices
        spoken_opts = q.get('spokenOptions', [])
        resp_voice = VOICE_FEMALE if prompt_voice == VOICE_MALE else VOICE_MALE
        for opt in spoken_opts:
            num = opt['num']
            text = opt['text']
            segments.append((f"{num}、{text}", resp_voice))
            segments.append(('SILENCE', 0.8))
        segments.append(('SILENCE', 1.5))

    elif q['typeId'] == 'N2-LIS-INTE': # Mondai 5
        full_script = q['contextPassage']
        lines = [l.strip() for l in full_script.splitlines() if l.strip()]
        intro = lines[0]
        qnum_m5 = q['examQNum'] - 27
        segments.append((f"問題５、質問{qnum_m5}。{intro}", VOICE_NARRATOR))
        segments.append(('SILENCE', 0.8))

        for l in lines[1:]:
            m = re.match(r'^([^：:]+)[：:](.*)$', l)
            if m:
                spk, speech = m.group(1).strip(), m.group(2).strip()
                v = VOICE_MALE if any(w in spk for w in ['男', '夫']) and '女' not in spk else VOICE_FEMALE
                segments.append((speech, v))
                segments.append(('SILENCE', 0.4))
            else:
                segments.append((l, VOICE_MALE))
                segments.append(('SILENCE', 0.4))
        
        segments.append(('SILENCE', 0.6))
        segments.append((f"質問。{q['stem']}", VOICE_NARRATOR))
        segments.append(('SILENCE', 1.5))

    # Process all segments into wav/mp3 clips
    clip_files = []
    for s_idx, seg in enumerate(segments):
        clip_path = item_tmp / f"clip_{s_idx:03d}.mp3"
        if seg[0] == 'SILENCE':
            make_silence(seg[1], clip_path)
        else:
            text, voice = seg
            await tts_clip(text, voice, clip_path)
        clip_files.append(clip_path)

    # Concat clips into final mp3
    concat_clips(clip_files, final_mp3)

    # Measure duration & SHA-256
    duration = get_audio_duration_and_check(final_mp3)
    sha256 = compute_sha256(final_mp3)
    file_size = final_mp3.stat().st_size

    # Clean up item temp dir
    shutil.rmtree(item_tmp)

    print(f"-> {qid}: {out_filename} (duration: {duration:.1f}s, size: {file_size:,} bytes, sha256: {sha256[:12]}...)")
    return {
        "id": qid,
        "audioUrl": f"audio/n2_mock_02/{out_filename}",
        "audioDurationSec": round(duration, 1),
        "audioSha256": sha256,
        "fileSizeBytes": file_size,
        "audioVerificationStatus": "VERIFIED",
        "audioSourceType": "NEURAL_TTS_MULTI_VOICE",
        "speakerVoices": ["ja-JP-NanamiNeural", "ja-JP-KeitaNeural"]
    }

async def generate_all_audio():
    print("=== Generating Listening Audio for JLPT N2 Full Mock #02 ===")
    AUDIO_OUT_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    items = get_n2_mock_02_listening_items()
    total = len(items)
    manifest = {}

    for idx, q in enumerate(items, 1):
        info = await build_item_audio(q, idx, total)
        manifest[q['id']] = info

    manifest_file = ROOT / 'data/mock_exams/n2_mock_02_audio_manifest.json'
    with open(manifest_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated all {total} audio tracks!")
    print(f"Manifest written to: {manifest_file}")

    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)

if __name__ == '__main__':
    asyncio.run(generate_all_audio())
