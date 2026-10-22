# -*- coding: utf-8 -*-
"""Promote the private M13 candidate only after current-version review passes."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.mock_exam_release_checks import validate_current_version_reconciliation

DRAFT = ROOT / "tmp/phase7/n2_mock_13_draft.json"
SEALED = ROOT / "qa/blind_items_m13_final.json"
REVIEW = ROOT / "qa/N2_MOCK_13_BLIND_RECONCILIATION.json"
OUT = ROOT / "data/mock_exams/n2_mock_13.json"


def main() -> None:
    draft = json.loads(DRAFT.read_text(encoding="utf-8"))
    sealed = json.loads(SEALED.read_text(encoding="utf-8"))
    review = json.loads(REVIEW.read_text(encoding="utf-8"))
    errors = validate_current_version_reconciliation(review, draft, sealed)
    evidence = review.get("rawEvidence", {})
    raw_rel = Path(str(evidence.get("rawOutputFile", "")))
    raw_path = (ROOT / raw_rel).resolve()
    if ROOT.resolve() not in raw_path.parents or not raw_path.is_file():
        errors.append("The immutable local raw reviewer response is not available")
    elif hashlib.sha256(raw_path.read_bytes()).hexdigest() != evidence.get("rawOutputSha256"):
        errors.append("The immutable raw reviewer response hash does not match the reconciliation")
    if errors:
        raise ValueError("M13 promotion blocked:\n- " + "\n- ".join(errors))

    exam = draft
    exam["status"] = "FULL_MOCK"
    exam["releaseGateStatus"] = "REVIEW_CONTENT_VERSION_VERIFIED"
    exam["title"] = exam["title"].replace(" (đang phát triển)", "")
    if not exam["title"].endswith("— Education, Media & Technology"):
        exam["title"] = "JLPT N2 Practice Mock Exam #13 — Education, Media & Technology"
    exam["sections"][1]["audioNoticeVi"] = (
        "Audio tiếng Nhật được tạo bằng giọng TTS tổng hợp. Cả 30 MP3 đã khớp manifest, giải mã được "
        "và phát tiến trên Chromium desktop và mobile emulation; giọng đọc chưa được chứng nhận bởi người bản ngữ."
    )
    OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Promoted current-version M13 candidate after {len(sealed)} reviewed items: {OUT}")


if __name__ == "__main__":
    main()
