# -*- coding: utf-8 -*-
"""Generate M13 MP3 tracks from its frozen original Japanese scripts.

Uses the already-reviewed local Edge TTS/ffmpeg synthesis and decoding helpers;
only Japanese spoken segments and voice synthesis settings are sent to TTS.
"""
from __future__ import annotations

import asyncio
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum import generate_n2_mock_12_audio as audio
from scripts.curriculum.bank_data.n2_mock_13_listening import get_n2_mock_13_listening_items

audio.AUDIO_OUT_DIR = ROOT / "docs/audio/n2_mock_13"
audio.TEMP_DIR = ROOT / "tmp/audio_gen_temp_13"
MANIFEST_PATH = ROOT / "data/mock_exams/n2_mock_13_audio_manifest.json"


async def main(selected_ids: set[str] | None = None) -> None:
    items = get_n2_mock_13_listening_items()
    if selected_ids is not None:
        known_ids = {item["id"] for item in items}
        unknown = selected_ids - known_ids
        if unknown:
            raise ValueError(f"Unknown M13 listening IDs: {sorted(unknown)}")
        if MANIFEST_PATH.is_file():
            manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
            if set(manifest) != known_ids:
                raise ValueError("Cannot update selected tracks: existing manifest does not cover all 30 M13 items")
        else:
            raise FileNotFoundError("Cannot update selected tracks without the complete initial M13 audio manifest")
    else:
        manifest = {}
    audio.AUDIO_OUT_DIR.mkdir(parents=True, exist_ok=True)
    audio.TEMP_DIR.mkdir(parents=True, exist_ok=True)
    targets = [item for item in items if selected_ids is None or item["id"] in selected_ids]
    for index, item in enumerate(items, 1):
        if item not in targets:
            continue
        meta = await audio.build_item_audio(item, index, len(items))
        meta["audioUrl"] = f"audio/n2_mock_13/{item['id']}.mp3"
        manifest[item["id"]] = meta
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8", newline="\n")
    print(f"Generated {len(manifest)} M13 tracks and manifest: {MANIFEST_PATH}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ids", nargs="+", help="Regenerate only these listening IDs and merge their current fingerprints")
    args = parser.parse_args()
    asyncio.run(main(set(args.ids) if args.ids else None))
