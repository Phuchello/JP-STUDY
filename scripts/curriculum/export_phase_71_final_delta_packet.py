# -*- coding: utf-8 -*-
"""Export only the learner-facing text for the final Phase 7.1 delta review."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.question_fingerprint import compute_question_fingerprint
from scripts.curriculum.bank_data.n2_mock_11_data import get_n2_mock_11_sec1_items
from scripts.curriculum.bank_data.n2_mock_12_data import get_n2_mock_12_sec1_items
from scripts.curriculum.bank_data.n2_mock_13_data import get_n2_mock_13_sec1_items
from scripts.curriculum.bank_data.n2_mock_14_data import get_n2_mock_14_sec1_items


OUTPUT = ROOT / "qa/PHASE_7_1_FRESH_REVIEW_PACKET_20261023_v11.json"
# This closure packet combines the final versions of the three repaired M14
# items. The latest Q30 source no longer includes a wait-for-opportunity
# reading as a possible second answer.
TARGET_IDS = {"N2_14_M1_29", "N2_14_M1_30", "N2_14_M1_31"}
TASK_INSTRUCTIONS = {
    "N2-RD-SHORT": "次の文章を読んで、後の問いに対する答えとして最もよいものを一つ選びなさい。",
    "N2-RD-MED": "次の文章を読んで、後の問いに対する答えとして最もよいものを一つ選びなさい。",
    "N2-RD-LONG": "次の文章を読んで、後の問いに対する答えとして最もよいものを一つ選びなさい。",
    "N2-MO-USE": "次の文の【語】の使い方として、最も自然なものを一つ選びなさい。",
}


def _current_items():
    builders = (
        get_n2_mock_12_sec1_items,
        get_n2_mock_13_sec1_items,
        get_n2_mock_14_sec1_items,
    )
    return {
        item["id"]: item
        for builder in builders
        for item in builder()
        if item.get("id") in TARGET_IDS
    }


def build_final_delta_packet():
    items = _current_items()
    if set(items) != TARGET_IDS:
        raise ValueError(f"final delta item set mismatch: {sorted(set(items) ^ TARGET_IDS)}")
    packet = []
    for question_id in sorted(TARGET_IDS):
        item = items[question_id]
        type_id = item.get("typeId")
        if type_id not in TASK_INSTRUCTIONS:
            raise ValueError(f"{question_id}: unexpected task type {type_id!r}")
        clean = {
            "id": question_id,
            "skill": item.get("skill", "Reading" if type_id.startswith("N2-RD-") else "Language Knowledge"),
            "category": item.get("category", ""),
            "taskInstructions": TASK_INSTRUCTIONS[type_id],
            "contextPassage": item.get("contextPassage") or item.get("passage") or None,
            "stem": item.get("stem", ""),
            "options": [{"id": option["id"], "text": option["text"]} for option in item.get("options", [])],
            "contentFingerprint": compute_question_fingerprint(item),
        }
        if len(clean["options"]) != 4 or len({option["id"] for option in clean["options"]}) != 4:
            raise ValueError(f"{question_id}: expected four distinct option IDs")
        packet.append(clean)
    return packet


def write_final_delta_packet(path: Path = OUTPUT):
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(build_final_delta_packet(), ensure_ascii=False, indent=2) + "\n"
    path.write_text(payload, encoding="utf-8", newline="\n")
    return path, hashlib.sha256(path.read_bytes()).hexdigest()


if __name__ == "__main__":
    packet_path, digest = write_final_delta_packet()
    print(json.dumps({"path": packet_path.relative_to(ROOT).as_posix(), "sha256": digest}, ensure_ascii=False))
