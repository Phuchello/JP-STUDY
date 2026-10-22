# -*- coding: utf-8 -*-
"""Export a sealed, key-free review packet for the private M13 draft."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.blind_review_exporter import validate_sealed_item_purity
from scripts.curriculum.question_fingerprint import compute_question_fingerprint
from scripts.curriculum.bank_data.n2_mock_13_data import get_n2_mock_13_sec1_items
from scripts.curriculum.bank_data.n2_mock_13_listening import get_n2_mock_13_listening_items

OUT = ROOT / "tmp/phase7/blind_items_m13_rev10.json"


def sealed_item(q: dict, section: int, audio_meta: dict | None = None) -> dict:
    source = dict(q)
    stimulus = q.get("contextPassage") or q.get("passage")
    if section == 2:
        stimulus = q["script"]
        source["contextPassage"] = stimulus
        if not audio_meta:
            raise ValueError(f"Missing exact-asset audio metadata for {q['id']}")
        source["audioUrl"] = audio_meta["audioUrl"]
        source["audioSha256"] = audio_meta["audioSha256"]
    row = {
        "id": q["id"], "examId": "N2-MOCK-13", "section": section,
        "typeId": q["typeId"], "category": q.get("category", ""),
        "stem": q.get("stem", ""), "contextPassage": stimulus,
        "options": [{"id": o["id"], "text": o["text"]} for o in q["options"]],
        "contentFingerprint": compute_question_fingerprint(source),
    }
    validate_sealed_item_purity(row)
    return row


def main() -> Path:
    manifest = json.loads((ROOT / "data/mock_exams/n2_mock_13_audio_manifest.json").read_text(encoding="utf-8"))
    listening = get_n2_mock_13_listening_items()
    if set(manifest) != {q["id"] for q in listening}:
        raise ValueError("M13 review exporter and audio manifest IDs do not match")
    items = [sealed_item(q, 1) for q in get_n2_mock_13_sec1_items()]
    items.extend(sealed_item(q, 2, manifest[q["id"]]) for q in listening)
    if len(items) != 105 or len({q["id"] for q in items}) != 105:
        raise ValueError("M13 review input must contain 105 unique question IDs")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Wrote private sealed key-free M13 input: {OUT}")
    print(f"SHA-256 {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    return OUT


if __name__ == "__main__":
    main()
