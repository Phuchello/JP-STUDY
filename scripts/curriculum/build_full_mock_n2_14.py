# -*- coding: utf-8 -*-
"""Build a private IN_DEVELOPMENT M14 payload; never promotes or publishes it."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.bank_data.n2_mock_14_data import get_n2_mock_14_sec1_items
from scripts.curriculum.bank_data.n2_mock_14_listening import get_n2_mock_14_listening_items
from scripts.curriculum.content_quality_checks import (
    pattern_defects,
    validate_answer_letter_references,
    validate_vietnamese_explanations,
)
from scripts.curriculum.mock_exam_release_checks import (
    validate_full_mock_blueprint,
    validate_star_fragment_integrity,
)


def build_draft() -> Path:
    sec1 = get_n2_mock_14_sec1_items()
    sec2 = get_n2_mock_14_listening_items()
    exam = {
        "examId": "N2-MOCK-14",
        "title": "JLPT N2 Practice Mock Exam #14 — Comprehensive Challenge (đang phát triển)",
        "level": "N2",
        "status": "IN_DEVELOPMENT",
        "releaseGateStatus": "PENDING_AUDIO_AND_INDEPENDENT_REVIEW",
        "durationMinutes": 155,
        "totalQuestions": 105,
        "sections": [
            {"sectionId": "sec-1", "sectionName": "Phần 1: Kiến thức ngôn ngữ & Đọc hiểu",
             "durationMinutes": 105, "itemCount": 75, "items": sec1},
            {"sectionId": "sec-2", "sectionName": "Phần 2: Nghe hiểu",
             "durationMinutes": 50, "itemCount": 30,
             "audioStatus": "NOT_GENERATED",
             "audioNoticeVi": "Bản đang phát triển: 30 kịch bản chưa có MP3. Đây chưa phải bài thi nghe có thể làm.",
             "items": sec2},
        ],
    }
    errors = []
    errors.extend(validate_full_mock_blueprint(exam))
    errors.extend(validate_vietnamese_explanations(exam))
    errors.extend(validate_answer_letter_references(exam))
    errors.extend(validate_star_fragment_integrity(exam))
    errors.extend(pattern_defects({"N2-MOCK-14": exam}))
    all_items = [item for section in exam["sections"] for item in section["items"]]
    if len({item["id"] for item in all_items}) != 105:
        errors.append("M14 question IDs are not unique")
    for item in all_items:
        if len({option["text"] for option in item.get("options", [])}) != len(item.get("options", [])):
            errors.append(f"{item.get('id')}: duplicate options")
        if item.get("correctAnswer") not in {option.get("id") for option in item.get("options", [])}:
            errors.append(f"{item.get('id')}: answer key is not bound to a displayed option")
    if errors:
        raise ValueError("M14 draft validation failed:\n- " + "\n- ".join(errors))
    out = ROOT / "tmp/phase7/n2_mock_14_draft.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(exam, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Built private IN_DEVELOPMENT M14 draft: {len(sec1)} Section 1 items + {len(sec2)} listening scripts")
    print(f"Output: {out}")
    return out


if __name__ == "__main__":
    build_draft()
