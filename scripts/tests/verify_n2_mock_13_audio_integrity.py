# -*- coding: utf-8 -*-
"""Check M13 MP3 bytes, decoding, duration, and current spoken-content binding."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.question_fingerprint import compute_spoken_content_fingerprint
from scripts.curriculum.bank_data.n2_mock_13_listening import get_n2_mock_13_listening_items

MANIFEST = ROOT / "data/mock_exams/n2_mock_13_audio_manifest.json"


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    items = get_n2_mock_13_listening_items()
    expected_ids = {item["id"] for item in items}
    errors: list[str] = []
    if len(manifest) != 30 or set(manifest) != expected_ids:
        errors.append("Manifest must cover the exact 30 current listening IDs")

    decoded = 0
    hashed = 0
    durations = 0
    for item in items:
        qid = item["id"]
        meta = manifest.get(qid, {})
        path = ROOT / "docs" / str(meta.get("audioUrl", ""))
        if not path.is_file():
            errors.append(f"{qid}: MP3 is missing")
            continue
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash == meta.get("audioSha256"):
            hashed += 1
        else:
            errors.append(f"{qid}: SHA-256 differs from the manifest")
        if meta.get("spokenContentSha256") != compute_spoken_content_fingerprint(item):
            errors.append(f"{qid}: spoken transcript, prompt, or option order differs from the current item")

        probe = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
             "default=noprint_wrappers=1:nokey=1", str(path)],
            capture_output=True, text=True, check=False,
        )
        try:
            duration = float(probe.stdout.strip())
        except ValueError:
            errors.append(f"{qid}: ffprobe could not read duration: {probe.stderr.strip()}")
            continue
        if probe.returncode == 0 and duration > 0:
            decoded += 1
        if abs(duration - float(meta.get("audioDurationSec", 0))) <= 0.05:
            durations += 1
        else:
            errors.append(f"{qid}: probed duration differs from manifest")
        decode = subprocess.run(
            ["ffmpeg", "-v", "error", "-i", str(path), "-f", "null", "-"],
            capture_output=True, text=True, check=False,
        )
        if decode.returncode != 0:
            errors.append(f"{qid}: ffmpeg decode failed: {decode.stderr.strip()}")

    print(f"tracks={len(manifest)} sha256={hashed}/30 ffprobe={decoded}/30 duration={durations}/30")
    if errors:
        print("FAIL M13 audio integrity:\n- " + "\n- ".join(errors))
        return 1
    print("PASS M13 audio integrity: all 30 current tracks match the manifest and spoken-content fingerprints, decode, and have matching durations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
