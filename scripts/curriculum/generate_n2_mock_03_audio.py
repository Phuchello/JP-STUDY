# -*- coding: utf-8 -*-
"""
JP-STUDY: GENERATE HIGH-QUALITY NEURAL TTS AUDIO ASSETS FOR JLPT N2 MOCK #03 (30 ITEMS)
Uses Microsoft Edge TTS Neural Japanese Voices:
- ja-JP-NanamiNeural (Female / Narrator / Female characters)
- ja-JP-KeitaNeural (Male / Male characters)

Produces 30 verified MP3 files in docs/audio/n2_mock_03/:
- Mondai 1 (Task-based): N2_03_M1_L01.mp3 to N2_03_M1_L05.mp3
- Mondai 2 (Key points): N2_03_M2_L01.mp3 to N2_03_M2_L06.mp3
- Mondai 3 (General outline): N2_03_M3_L01.mp3 to N2_03_M3_L05.mp3
- Mondai 4 (Quick response - 3 spoken choices): N2_03_M4_L01.mp3 to N2_03_M4_L11.mp3
- Mondai 5 (Integrated): N2_03_M5_L01.mp3 to N2_03_M5_L03.mp3
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
AUDIO_OUT_DIR = ROOT / 'docs/audio/n2_mock_03'
TEMP_DIR = ROOT / 'tmp/audio_gen_temp_03'

VOICE_FEMALE = 'ja-JP-NanamiNeural'
VOICE_MALE = 'ja-JP-KeitaNeural'
VOICE_NARRATOR = 'ja-JP-NanamiNeural'

sys.path.insert(0, str(ROOT))
from scripts.curriculum.bank_data.n2_mock_03_listening import get_n2_mock_03_listening_items
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
    out_filename = f"{qid}.mp3"
    final_mp3 = AUDIO_OUT_DIR / out_filename

    print(f"[{item_idx}/{total_items}] Generating audio for {qid} -> {out_filename}...")
    item_tmp = TEMP_DIR / qid
    if item_tmp.exists():
        shutil.rmtree(item_tmp)
    item_tmp.mkdir(parents=True, exist_ok=True)

    segments = [] # list of (text, voice) or ('SILENCE', duration)

    if q['typeId'] == 'N2-LIS-TASK': # Mondai 1
        full_script = q.get('script') or q.get('contextPassage', '')
        lines = [l.strip() for l in full_script.splitlines() if l.strip()]
        intro = lines[0]
        qnum_str = f"問題１、{item_idx}番。"
        segments.append((f"{qnum_str} {intro}", VOICE_NARRATOR))
        segments.append(('SILENCE', 0.8))

        # Dialogue
        for l in lines[1:]:
            m = re.match(r'^([^：:]+)[：:](.*)$', l)
            if m:
                spk, speech = m.group(1).strip(), m.group(2).strip()
                v = VOICE_MALE if any(w in spk for w in ['男', '夫', '店長', '教授']) and '女' not in spk else VOICE_FEMALE
                segments.append((speech, v))
                segments.append(('SILENCE', 0.4))
        
        # Question repeated
        segments.append(('SILENCE', 0.5))
        segments.append((q['stem'], VOICE_NARRATOR))
        segments.append(('SILENCE', 1.5))

    elif q['typeId'] == 'N2-LIS-POINT': # Mondai 2
        full_script = q.get('script') or q.get('contextPassage', '')
        lines = [l.strip() for l in full_script.splitlines() if l.strip()]
        intro = lines[0]
        m2_num = item_idx - 5
        qnum_str = f"問題２、{m2_num}番。"
        segments.append((f"{qnum_str} {intro}", VOICE_NARRATOR))
        segments.append(('SILENCE', 0.8))
        # Designated reading time (6 seconds pause)
        segments.append(('SILENCE', 6.0))

        # Dialogue or talk
        for l in lines[1:]:
            m = re.match(r'^([^：:]+)[：:](.*)$', l)
            if m:
                spk, speech = m.group(1).strip(), m.group(2).strip()
                v = VOICE_MALE if any(w in spk for w in ['男', '建築家', '監督', '開発者']) and '女' not in spk else VOICE_FEMALE
                segments.append((speech, v))
                segments.append(('SILENCE', 0.4))
            else:
                segments.append((l, VOICE_MALE))
                segments.append(('SILENCE', 0.4))
        
        segments.append(('SILENCE', 0.5))
        segments.append((q['stem'], VOICE_NARRATOR))
        segments.append(('SILENCE', 1.5))

    elif q['typeId'] == 'N2-LIS-SUMM': # Mondai 3
        full_script = q.get('script') or q.get('contextPassage', '')
        lines = [l.strip() for l in full_script.splitlines() if l.strip()]
        intro = lines[0]
        m3_num = item_idx - 11
        qnum_str = f"問題３、{m3_num}番。"
        segments.append((f"{qnum_str} {intro}", VOICE_NARRATOR))
        segments.append(('SILENCE', 0.8))

        # Monologue
        for l in lines[1:]:
            m = re.match(r'^([^：:]+)[：:](.*)$', l)
            if m:
                spk, speech = m.group(1).strip(), m.group(2).strip()
                v = VOICE_MALE if any(w in spk for w in ['男', '専門家', 'デザイナー']) and '女' not in spk else VOICE_FEMALE
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
        m4_num = item_idx - 16
        qnum_str = f"問題４、{m4_num}番。"
        segments.append((qnum_str, VOICE_NARRATOR))
        segments.append(('SILENCE', 0.6))

        full_script = q.get('script') or q.get('contextPassage', '')
        lines = [l.strip() for l in full_script.splitlines() if l.strip()]
        # First line is prompt: e.g. 男：「今日のプレゼン、...」
        prompt_line = lines[0]
        m_prompt = re.search(r'^[男女][：:](.*)$', prompt_line)
        if m_prompt:
            prompt_text = m_prompt.group(1).strip()
        else:
            prompt_text = prompt_line

        prompt_voice = VOICE_MALE if prompt_line.startswith('男') else VOICE_FEMALE
        segments.append((prompt_text, prompt_voice))
        segments.append(('SILENCE', 1.0))

        # 3 Spoken choices from lines[1:]
        resp_voice = VOICE_FEMALE if prompt_voice == VOICE_MALE else VOICE_MALE
        for opt_line in lines[1:]:
            segments.append((opt_line, resp_voice))
            segments.append(('SILENCE', 0.8))
        segments.append(('SILENCE', 1.5))

    elif q['typeId'] == 'N2-LIS-INTEG': # Mondai 5
        full_script = q.get('script') or q.get('contextPassage', '')
        lines = [l.strip() for l in full_script.splitlines() if l.strip()]
        intro = lines[0]
        qnum_m5 = item_idx - 27
        segments.append((f"問題５、質問{qnum_m5}。{intro}", VOICE_NARRATOR))
        segments.append(('SILENCE', 0.8))

        for l in lines[1:]:
            m = re.match(r'^([^：:]+)[：:](.*)$', l)
            if m:
                spk, speech = m.group(1).strip(), m.group(2).strip()
                v = VOICE_MALE if any(w in spk for w in ['男', '夫', '店員']) and '女' not in spk else VOICE_FEMALE
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
        "qid": qid,
        "audioUrl": f"audio/n2_mock_03/{out_filename}",
        "audioDurationSec": round(duration, 1),
        "audioSha256": sha256,
        "sha256": sha256,
        "audioVerificationStatus": "AUDIO_VERIFIED",
        "audioSourceType": "NEURAL_TTS_MULTI_VOICE",
        "speakerVoices": ["ja-JP-NanamiNeural", "ja-JP-KeitaNeural"],
        "fileSizeBytes": file_size
    }

async def main():
    AUDIO_OUT_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    items = get_n2_mock_03_listening_items()
    print(f"Starting audio generation for {len(items)} items in N2 Full Mock #03...")

    manifest = {}
    for idx, q in enumerate(items, 1):
        res = await build_item_audio(q, idx, len(items))
        manifest[q['id']] = res

    manifest_path = ROOT / 'data/mock_exams/n2_mock_03_audio_manifest.json'
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR, ignore_errors=True)

    print(f"\n=======================================================")
    print(f"SUCCESS: Generated all {len(manifest)} audio assets for N2-MOCK-03!")
    print(f"Manifest saved to: {manifest_path}")
    print(f"=======================================================\n")

if __name__ == '__main__':
    asyncio.run(main())
