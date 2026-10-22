# -*- coding: utf-8 -*-
"""Generate the 30 M14 tracks after explicit M14-scoped provider authorization."""
from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum import generate_n2_mock_12_audio as audio
from scripts.curriculum.bank_data.n2_mock_14_listening import get_n2_mock_14_listening_items

audio.AUDIO_OUT_DIR = ROOT / "docs/audio/n2_mock_14"
audio.TEMP_DIR = ROOT / "tmp/audio_gen_temp_14"
MANIFEST_PATH = ROOT / "data/mock_exams/n2_mock_14_audio_manifest.json"


async def main() -> None:
    items = get_n2_mock_14_listening_items()
    audio.AUDIO_OUT_DIR.mkdir(parents=True, exist_ok=True)
    audio.TEMP_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for index, item in enumerate(items, 1):
        meta = await audio.build_item_audio(item, index, len(items))
        meta["audioUrl"] = f"audio/n2_mock_14/{item['id']}.mp3"
        manifest[item["id"]] = meta
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8", newline="\n")
    print(f"Generated {len(manifest)} M14 MP3s and manifest: {MANIFEST_PATH}")


if __name__ == "__main__":
    asyncio.run(main())
