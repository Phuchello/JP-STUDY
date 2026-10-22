# -*- coding: utf-8 -*-
"""Build the current key-free, version-bound Phase 7.1 review packet."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.blind_review_exporter import validate_sealed_item_purity
from scripts.curriculum.content_fingerprint import compute_file_sha256
from scripts.curriculum.question_fingerprint import compute_question_fingerprint
from scripts.curriculum.bank_data.n2_mock_11_data import get_n2_mock_11_sec1_items
from scripts.curriculum.bank_data.n2_mock_12_data import get_n2_mock_12_sec1_items
from scripts.curriculum.bank_data.n2_mock_13_data import get_n2_mock_13_sec1_items
from scripts.curriculum.bank_data.n2_mock_14_data import get_n2_mock_14_sec1_items


BASE_COMMIT = "46fbd3bfcbbac6f56f8ce0263ce4d85b437c9316"
SOURCE_PATHS = (
    "scripts/curriculum/phase_71_reading_repairs.py",
    "scripts/curriculum/phase_71_reading_rationales.py",
    "scripts/curriculum/phase_71_star_repairs.py",
    "scripts/curriculum/bank_data/n2_mock_11_data.py",
    "scripts/curriculum/bank_data/n2_mock_11_explanations_vi.py",
    "scripts/curriculum/bank_data/n2_mock_12_data.py",
    "scripts/curriculum/bank_data/n2_mock_13_data.py",
    "scripts/curriculum/bank_data/n2_mock_14_data.py",
    "scripts/curriculum/blind_review_exporter.py",
    "scripts/curriculum/question_fingerprint.py",
    "scripts/curriculum/export_phase_71_candidate_packet.py",
)
READING_TYPES = {"N2-RD-SHORT", "N2-RD-MED", "N2-RD-LONG"}
TASK_INSTRUCTIONS = {
    "N2-GR-STAR": "次の文を完成させるとき、★に入る最もよい部分を一つ選びなさい。",
    "N2-MO-USE": "次の文の【語】の使い方として、最も自然なものを一つ選びなさい。",
    "N2-RD-SHORT": "次の文章を読んで、後の問いに対する答えとして最もよいものを一つ選びなさい。",
    "N2-RD-MED": "次の文章を読んで、後の問いに対する答えとして最もよいものを一つ選びなさい。",
    "N2-RD-LONG": "次の文章を読んで、後の問いに対する答えとして最もよいものを一つ選びなさい。",
}


def _all_sources():
    return {
        11: get_n2_mock_11_sec1_items(),
        12: get_n2_mock_12_sec1_items(),
        13: get_n2_mock_13_sec1_items(),
        14: get_n2_mock_14_sec1_items(),
    }


def build_candidate_packet():
    sources = _all_sources()
    selected = []
    for mock_number in (11, 12, 13):
        for item in sources[mock_number]:
            if item.get("typeId") in READING_TYPES or (
                mock_number == 11 and item.get("typeId") == "N2-GR-STAR"
            ):
                selected.append((mock_number, item))
    for item in sources[14]:
        if item.get("typeId") == "N2-MO-USE":
            selected.append((14, item))

    blind_items = []
    for mock_number, item in selected:
        type_id = item.get("typeId", "")
        blind_item = {
            "id": item["id"],
            "examId": f"N2-MOCK-{mock_number:02}",
            "section": 1,
            "skill": item.get("skill", "Reading" if type_id.startswith("N2-RD-") else "Language Knowledge"),
            "typeId": type_id,
            "category": item.get("category", ""),
            "taskInstructions": TASK_INSTRUCTIONS[type_id],
            "stem": item.get("stem", ""),
            "contextPassage": item.get("contextPassage") or item.get("passage") or None,
            "options": [{"id": option["id"], "text": option["text"]} for option in item.get("options", [])],
            "contentFingerprint": compute_question_fingerprint(item),
        }
        validate_sealed_item_purity(blind_item)
        blind_items.append(blind_item)

    ids = [item["id"] for item in blind_items]
    if len(ids) != 61 or len(ids) != len(set(ids)):
        raise ValueError(f"expected 61 unique target items, found {len(ids)}")
    counts = {
        "reading": sum(item["typeId"] in READING_TYPES for item in blind_items),
        "star": sum(item["typeId"] == "N2-GR-STAR" for item in blind_items),
        "wordUsage": sum(item["typeId"] == "N2-MO-USE" for item in blind_items),
    }
    if counts != {"reading": 51, "star": 5, "wordUsage": 5}:
        raise ValueError(f"unexpected packet target counts: {counts}")

    return {
        "schemaVersion": "JP-STUDY-PHASE-7.1-BLIND-REVIEW-1",
            "packetId": "PHASE-7.1-CANDIDATE-2026-10-22-v6",
        "baseCommit": BASE_COMMIT,
        "candidateSourceSha256": {
            source_path: compute_file_sha256(ROOT / source_path)
            for source_path in SOURCE_PATHS
        },
        "reviewStatus": "PENDING_INDEPENDENT_REVIEW",
        "keyExcluded": True,
        "reviewInstructions": (
            "Review only the learner-visible Japanese text and choices. For each item, choose the best answer by option ID, "
            "briefly explain the linguistic or passage evidence, and flag any unnatural wording, weak distractor, or alternative "
            "that could also be defended. Do not infer or request author keys. A structural pass is not a language certification."
        ),
        "knownEditorialConcern": {
            "id": "N2_14_M1_31",
            "status": "CONTENT_REVIEW_REQUIRED",
            "note": "The current distractors are complete sentences, but rely on contradictions with stated time, budget, or seating facts. They may be eliminated without distinguishing 余裕's lexical use; keep CONTENT_REVIEW_REQUIRED pending a more discriminating design and independent review.",
        },
        "itemCounts": counts,
        "items": blind_items,
    }


def write_candidate_packet(path=None):
    output = Path(path) if path else ROOT / "qa/PHASE_7_1_FRESH_REVIEW_PACKET_20261022_v6.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(build_candidate_packet(), ensure_ascii=False, indent=2) + "\n"
    output.write_text(payload, encoding="utf-8", newline="\n")
    return output, hashlib.sha256(output.read_bytes()).hexdigest()


if __name__ == "__main__":
    packet_path, digest = write_candidate_packet()
    print(json.dumps({"path": str(packet_path), "sha256": digest}, ensure_ascii=False))
