# -*- coding: utf-8 -*-
"""Integrate the validated N2-MOCK-10 exam JSON into the browser data bank."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BANK_PATH = ROOT / "docs/widgets/mock_exam_bank.js"
EXAM_PATH = ROOT / "data/mock_exams/n2_mock_10.json"
KEY = "N2-MOCK-10"


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
    exam = json.loads(EXAM_PATH.read_text(encoding="utf-8"))
    if exam.get("examId") != KEY or exam.get("status") != "FULL_MOCK":
        raise ValueError("Only a promoted FULL_MOCK exam may be added to the playable bank.")
    if [len(section.get("items", [])) for section in exam.get("sections", [])] != [75, 30]:
        raise ValueError("M10 bank integration requires exactly 75 + 30 questions.")
    source = remove_data_entry(BANK_PATH.read_text(encoding="utf-8"), KEY)
    marker = "  'N3-MOCK-01': {"
    if marker not in source:
        raise ValueError("Could not locate N3 data entry in the mock bank")
    entry = f"  '{KEY}': " + json.dumps(exam, ensure_ascii=False, indent=2) + ",\n"
    source = source.replace(marker, entry + marker, 1)
    BANK_PATH.write_text(source, encoding="utf-8")
    print("Integrated validated N2-MOCK-10 into JP_MOCK_DATA.")


if __name__ == "__main__":
    main()
