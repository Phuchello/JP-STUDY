# -*- coding: utf-8 -*-
"""Build local-only synthetic exam fixtures with current Phase 7.1 candidates."""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.bank_data.n2_mock_11_data import get_n2_mock_11_sec1_items
from scripts.curriculum.bank_data.n2_mock_12_data import get_n2_mock_12_sec1_items
from scripts.curriculum.bank_data.n2_mock_13_data import get_n2_mock_13_sec1_items


BUILDERS = {
    11: get_n2_mock_11_sec1_items,
    12: get_n2_mock_12_sec1_items,
    13: get_n2_mock_13_sec1_items,
}
OUTPUT_DIR = ROOT / "tmp/phase7/candidate_e2e"


def export_fixtures(output_dir: Path = OUTPUT_DIR):
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = []
    for number, builder in BUILDERS.items():
        source = ROOT / f"data/mock_exams/n2_mock_{number:02}.json"
        exam = copy.deepcopy(json.loads(source.read_text(encoding="utf-8")))
        if len(exam.get("sections", [])) != 2:
            raise ValueError(f"N2-MOCK-{number:02} must retain its two-section blueprint")
        candidate_items = builder()
        if len(candidate_items) != 75:
            raise ValueError(f"N2-MOCK-{number:02} candidate Section 1 has {len(candidate_items)} items")
        ids = [item.get("id") for item in candidate_items]
        if len(ids) != len(set(ids)):
            raise ValueError(f"N2-MOCK-{number:02} candidate question IDs are not unique")
        exam["sections"][0]["items"] = candidate_items
        exam["sections"][0]["itemCount"] = len(candidate_items)
        exam["status"] = "SYNTHETIC_CANDIDATE_E2E_FIXTURE"
        output = output_dir / f"n2_mock_{number:02}_candidate.json"
        output.write_text(json.dumps(exam, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        outputs.append(output)
    return outputs


if __name__ == "__main__":
    print("\n".join(path.relative_to(ROOT).as_posix() for path in export_fixtures()))
