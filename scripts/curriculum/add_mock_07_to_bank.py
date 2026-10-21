# -*- coding: utf-8 -*-
"""Integrate N2-MOCK-07 data into the browser bank.

The registry status is managed separately so data integration can happen in
staging. On a release-ready run, the caller updates the registry only after all
content and release gates pass.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BANK_PATH = ROOT / "docs/widgets/mock_exam_bank.js"
EXAM_PATH = ROOT / "data/mock_exams/n2_mock_07.json"
KEY = "N2-MOCK-07"


def remove_data_entry(source: str, key: str) -> str:
    token = f"  '{key}': "
    start = source.find(token)
    if start < 0:
        return source
    value_start = start + len(token)
    if source[value_start] != "{":
        raise ValueError(f"Unexpected JS value for {key}")
    depth = 0
    in_string = False
    escaped = False
    end = None
    for pos in range(value_start, len(source)):
        char = source[pos]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                end = pos + 1
                break
    if end is None:
        raise ValueError(f"Unclosed JS object for {key}")
    if end < len(source) and source[end] == ",":
        end += 1
    if end < len(source) and source[end] == "\n":
        end += 1
    return source[:start] + source[end:]


def main() -> None:
    source = BANK_PATH.read_text(encoding="utf-8")
    exam = json.loads(EXAM_PATH.read_text(encoding="utf-8"))
    source = remove_data_entry(source, KEY)
    marker = "  'N3-MOCK-01': {"
    if marker not in source:
        raise ValueError("Could not locate N3 data entry in mock bank")
    entry = f"  '{KEY}': " + json.dumps(exam, ensure_ascii=False, indent=2) + ",\n"
    source = source.replace(marker, entry + marker, 1)
    BANK_PATH.write_text(source, encoding="utf-8")
    print("Integrated N2-MOCK-07 into JP_MOCK_DATA; registry status unchanged.")


if __name__ == "__main__":
    main()
