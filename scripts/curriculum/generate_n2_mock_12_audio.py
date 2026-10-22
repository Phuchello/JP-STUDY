# -*- coding: utf-8 -*-
"""
JP-STUDY: GENERATE HIGH-QUALITY NEURAL TTS AUDIO ASSETS FOR JLPT N2 MOCK #12 (30 ITEMS)
Uses Microsoft Edge TTS Neural Japanese Voices:
- ja-JP-NanamiNeural (Female / Narrator / Female characters)
- ja-JP-KeitaNeural (Male / Male characters)

Produces 30 verified MP3 files in docs/audio/n2_mock_12/:
- Mondai 1 (Task-based): N2_12_M1_L01.mp3 to N2_12_M1_L05.mp3
- Mondai 2 (Key points): N2_12_M2_L01.mp3 to N2_12_M2_L06.mp3 (with 6.0s pause)
- Mondai 3 (General outline): N2_12_M3_L01.mp3 to N2_12_M3_L05.mp3 (4 spoken choices)
- Mondai 4 (Quick response - 3 spoken choices): N2_12_M4_L01.mp3 to N2_12_M4_L11.mp3
- Mondai 5 (Integrated): N2_12_M5_L01.mp3 to N2_12_M5_L03.mp3
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
AUDIO_OUT_DIR = ROOT / 'docs/audio/n2_mock_12'
TEMP_DIR = ROOT / 'tmp/audio_gen_temp_12'

VOICE_FEMALE = 'ja-JP-NanamiNeural'
VOICE_MALE = 'ja-JP-KeitaNeural'
VOICE_NARRATOR = 'ja-JP-NanamiNeural'

sys.path.insert(0, str(ROOT))
from scripts.curriculum.bank_data.n2_mock_12_listening import get_n2_mock_12_listening_items
from scripts.curriculum.question_fingerprint import compute_spoken_content_fingerprint
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
    dialogue_text = q.get('dialogue') or q.get('script') or q.get('contextPassage', '')
    lines = [l.strip() for l in dialogue_text.splitlines() if l.strip()]

    if q['typeId'] == 'N2-LIS-TASK': # Mondai 1
        intro = lines[0]
        qnum_str = f"問題１、{item_idx}番。"
        segments.append((f"{qnum_str} {intro}", VOICE_NARRATOR))
        segments.append(('SILENCE', 0.8))

        # Dialogue
        for l in lines[1:]:
            m = re.match(r'^([^：:]+)[：:](.*)$', l)
            if m:
                spk, speech = m.group(1).strip(), m.group(2).strip()
                v = VOICE_MALE if any(w in spk for w in ['男', '夫', '課長', '本部長', '役員', '高橋']) and '女' not in spk else VOICE_FEMALE
                segments.append((speech, v))
                segments.append(('SILENCE', 0.4))

        # Question repeated
        segments.append(('SILENCE', 0.5))
        segments.append((q['stem'], VOICE_NARRATOR))
        segments.append(('SILENCE', 1.5))

    elif q['typeId'] == 'N2-LIS-POINT': # Mondai 2
        intro = lines[0]
        m2_num = item_idx - 5
        qnum_str = f"問題２、{m2_num}番。"
        segments.append((f"{qnum_str} {intro}", VOICE_NARRATOR))
        segments.append(('SILENCE', 0.8))
        # Designated reading time (6 seconds pause)
        segments.append(('SILENCE', 6.0))

        for l in lines[1:]:
            m = re.match(r'^([^：:]+)[：:](.*)$', l)
            if m:
                spk, speech = m.group(1).strip(), m.group(2).strip()
                v = VOICE_MALE if any(w in spk for w in ['男', '課長', 'アナウンサー', '役員']) and '女' not in spk else VOICE_FEMALE
                segments.append((speech, v))
                segments.append(('SILENCE', 0.4))
            else:
                v = VOICE_FEMALE if '女' in intro else VOICE_MALE
                segments.append((l, v))
                segments.append(('SILENCE', 0.4))

        segments.append(('SILENCE', 0.5))
        segments.append((q['stem'], VOICE_NARRATOR))
        segments.append(('SILENCE', 1.5))

    elif q['typeId'] in ('N2-LIS-SUMM', 'N2-LIS-OUTL', 'N2-LIS-GIST'): # Mondai 3
        intro = lines[0]
        m3_num = item_idx - 11
        qnum_str = f"問題３、{m3_num}番。"
        segments.append((f"{qnum_str} {intro}", VOICE_NARRATOR))
        segments.append(('SILENCE', 0.8))

        # Monologue
        for l in lines[1:]:
            if re.match(r'^[1-4]番[：:]', l) or '何について話して' in l or '最も伝えたいこと' in l or '何を改善するよう' in l or '何が最も大切だ' in l:
                continue
            m = re.match(r'^([^：:]+)[：:](.*)$', l)
            if m:
                spk, speech = m.group(1).strip(), m.group(2).strip()
                v = VOICE_MALE if any(w in spk for w in ['男', '社長', '館長']) and '女' not in spk else VOICE_FEMALE
                segments.append((speech, v))
            else:
                v = VOICE_FEMALE if ('女' in intro or '専門家' in intro or '議員' in intro) else VOICE_MALE
                segments.append((l, v))
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

    elif q['typeId'] == 'N2-LIS-RESP': # Mondai 4 (Quick Response)
        m4_num = item_idx - 16
        qnum_str = f"問題４、{m4_num}番。"
        segments.append((qnum_str, VOICE_NARRATOR))
        segments.append(('SILENCE', 0.6))

        # Alternating male / female prompts
        prompt_voice = VOICE_MALE if (m4_num % 2 == 1) else VOICE_FEMALE
        resp_voice = VOICE_FEMALE if prompt_voice == VOICE_MALE else VOICE_MALE

        prompt_text = q['stem']
        segments.append((prompt_text, prompt_voice))
        segments.append(('SILENCE', 1.0))

        # Strictly 3 Spoken choices
        for idx, opt in enumerate(q['options']):
            segments.append((f"{idx+1}番、{opt['text']}", resp_voice))
            segments.append(('SILENCE', 0.8))
        segments.append(('SILENCE', 1.5))

    elif q['typeId'] in ('N2-LIS-INTEG', 'N2-LIS-INT'): # Mondai 5
        qnum_m5 = item_idx - 27
        if qnum_m5 == 1:
            segments.append(("問題５、質問１、質問２。", VOICE_NARRATOR))
            segments.append(('SILENCE', 0.8))
        elif qnum_m5 == 2:
            segments.append(("質問２。", VOICE_NARRATOR))
            segments.append(('SILENCE', 0.8))
        elif qnum_m5 == 3:
            segments.append(("質問３。", VOICE_NARRATOR))
            segments.append(('SILENCE', 0.8))

        intro = lines[0]
        segments.append((intro, VOICE_NARRATOR))
        segments.append(('SILENCE', 0.8))

        for l in lines[1:]:
            if '質問：' in l:
                continue
            m = re.match(r'^([^：:]+)[：:](.*)$', l)
            if m:
                spk, speech = m.group(1).strip(), m.group(2).strip()
                v = VOICE_MALE if any(w in spk for w in ['男', '役員', '職員']) and '女' not in spk else VOICE_FEMALE
                segments.append((speech, v))
                segments.append(('SILENCE', 0.4))
            else:
                segments.append((l, VOICE_MALE))
                segments.append(('SILENCE', 0.4))

        segments.append(('SILENCE', 0.6))
        segments.append((f"質問。{q['stem']}", VOICE_NARRATOR))
        segments.append(('SILENCE', 1.5))

    # Process all segments into mp3 clips
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

    print(f"  -> Generated {out_filename}: {duration:.2f}s, {file_size:,} bytes, sha256={sha256[:12]}...")

    return {
        "questionId": qid,
        "audioUrl": f"audio/n2_mock_12/{out_filename}",
        "audioDurationSec": duration,
        "audioSha256": sha256,
        "audioSizeBytes": file_size,
        "audioVerificationStatus": "PLAYBACK_QA_PENDING",
        "audioSourceType": "NEURAL_TTS_MULTI_VOICE",
        "speakerVoices": [VOICE_FEMALE, VOICE_MALE],
        "spokenContentSha256": compute_spoken_content_fingerprint(q),
    }

async def main():
    print("=== JP-STUDY N2 MOCK #12: Studio Neural Audio Generation ===")
    AUDIO_OUT_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    all_items = get_n2_mock_12_listening_items()
    args = sys.argv[1:]
    single_item_id = args[1] if len(args) == 2 and args[0] == "--item-id" else None
    rebuild_spoken_choices = args == ["--rebuild-spoken-choice-tracks"]
    rebuild_mondai4_only = args == ["--rebuild-mondai4-only"]
    if args and not (single_item_id or rebuild_spoken_choices or rebuild_mondai4_only):
        raise SystemExit("Usage: generate_n2_mock_12_audio.py [--item-id QUESTION_ID | --rebuild-spoken-choice-tracks | --rebuild-mondai4-only]")

    if rebuild_spoken_choices or rebuild_mondai4_only:
        spoken_choice_types = {"N2-LIS-SUMM", "N2-LIS-OUTL", "N2-LIS-GIST", "N2-LIS-RESP"}
        if rebuild_mondai4_only:
            spoken_choice_types = {"N2-LIS-RESP"}
        indexed_items = [
            (idx, q) for idx, q in enumerate(all_items, 1)
            if q.get("typeId") in spoken_choice_types
        ]
        label = "Mondai 4" if rebuild_mondai4_only else "spoken-choice"
        print(f"Rebuilding {len(indexed_items)} {label} tracks whose spoken choices changed.")
    elif single_item_id:
        indexed_items = [(idx, q) for idx, q in enumerate(all_items, 1) if q.get("id") == single_item_id]
        if not indexed_items:
            raise SystemExit(f"Unknown N2-MOCK-12 listening item: {single_item_id}")
        print(f"Rebuilding only the revised track {single_item_id}.")
    else:
        indexed_items = list(enumerate(all_items, 1))
        print(f"Loaded {len(indexed_items)} listening items for N2 Mock #12.")

    manifest_file = ROOT / 'data/mock_exams/n2_mock_12_audio_manifest.json'
    if (rebuild_spoken_choices or rebuild_mondai4_only or single_item_id) and manifest_file.exists():
        manifest = json.loads(manifest_file.read_text(encoding='utf-8'))
    else:
        manifest = {}
    for idx, q in indexed_items:
        meta = await build_item_audio(q, idx, len(all_items))
        manifest[q['id']] = meta

    # Write manifest
    with open(manifest_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"\nSuccessfully generated {len(manifest)} audio assets.")
    print(f"Manifest written to: {manifest_file}")

    # Clean up general temp dir
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)

if __name__ == '__main__':
    asyncio.run(main())
