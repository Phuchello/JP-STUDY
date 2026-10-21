"""Text-preserving option remapping for the Phase 6.1 N2 #07-#09 repair.

The committed QA manifest is the build-time source of displayed option order.
Keys are always reconstructed from exact semantic option text, never copied
from a pre-remap letter.
"""
from __future__ import annotations

import hashlib
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / "qa/PHASE_6_1_OPTION_REMAP_MANIFEST.json"
EXPLANATION_PATH = ROOT / "scripts/curriculum/bank_data/n2_mock_08_09_explanations_vi.py"
AUDIO_COUPLED_TYPES = {"N2-LIS-SUMM", "N2-LIS-OUTL", "N2-LIS-GIST", "N2-LIS-RESP"}


def read_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        raise ValueError(f"Missing Phase 6.1 option remap manifest: {MANIFEST_PATH}")
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def exact_option_map(question: dict) -> dict[str, str]:
    options = question.get("options", [])
    mapping = {str(row.get("id", "")).strip(): str(row.get("text", "")).strip() for row in options}
    if len(mapping) != len(options) or any(not key or not text for key, text in mapping.items()):
        raise ValueError(f"Malformed or duplicate options for {question.get('id')}")
    return mapping


def _star_fragment_order(question: dict) -> list[str]:
    options = exact_option_map(question)
    stored = question.get("fragmentOrder")
    if stored:
        labels = re.findall(r"[A-D]", str(stored).upper())
        if len(labels) == 4 and len(set(labels)) == 4 and all(x in options for x in labels):
            return [options[label] for label in labels]
    sentence = str(question.get("assembledSentence", ""))
    positions = []
    for text in options.values():
        at = sentence.find(text)
        if at < 0 or sentence.find(text, at + 1) >= 0:
            raise ValueError(f"Cannot derive unique STAR fragment order from assembledSentence: {question.get('id')}")
        positions.append((at, text))
    ordered = [text for _, text in sorted(positions)]
    if len(ordered) != 4:
        raise ValueError(f"STAR item must contain four fragments: {question.get('id')}")
    return ordered


def apply_remapping(exam_id: str, items: list[dict], *, apply_explanations: bool = True) -> list[dict]:
    manifest = read_manifest()
    exam_rows = manifest.get("exams", {}).get(exam_id)
    if not isinstance(exam_rows, dict):
        raise ValueError(f"No remapping manifest for {exam_id}")
    explanations = {}
    if apply_explanations and exam_id in {"N2-MOCK-08", "N2-MOCK-09"}:
        # Import lazily so the option helper remains usable by content tools.
        import importlib.util
        spec = importlib.util.spec_from_file_location("phase61_explanations", EXPLANATION_PATH)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        explanations = module.EXPLANATIONS_VI[exam_id]
    seen = set()
    for question in items:
        qid = str(question.get("id", ""))
        row = exam_rows.get(qid)
        if row is None:
            raise ValueError(f"Question is missing from option remap manifest: {exam_id} {qid}")
        seen.add(qid)
        current = exact_option_map(question)
        if sorted(current.values()) != sorted(row["originalOptionTexts"]):
            raise ValueError(f"Source option text set changed since manifest was written: {qid}")
        original_order = [current[label] for label in sorted(current)]
        if original_order != row["originalOptionTexts"]:
            raise ValueError(f"Source option order changed since manifest was written: {qid}")
        old_key = str(question.get("correctAnswer", "")).strip()
        old_key_text = current.get(old_key)
        if old_key_text != row["originalCorrectText"]:
            raise ValueError(f"Source answer text changed since manifest was written: {qid}")
        target_text = row.get("starFragmentAtKey") if question.get("typeId") == "N2-GR-STAR" else old_key_text
        if question.get("typeId") == "N2-GR-STAR" and target_text != old_key_text:
            raise ValueError(f"Authored STAR key does not match its grammatical third fragment: {qid}")

        by_text = {text: next(dict(option) for option in question["options"] if option["text"].strip() == text)
                   for text in row["newOptionOrder"]}
        new_options = []
        new_id_by_text = {}
        for index, text in enumerate(row["newOptionOrder"]):
            option = by_text[text]
            option["id"] = "ABCD"[index]
            new_id_by_text[text] = option["id"]
            new_options.append(option)
        question["options"] = new_options
        question["correctAnswer"] = new_id_by_text[target_text]
        if question.get("typeId") == "N2-GR-STAR":
            fragment_texts = row["fragmentOrderTexts"]
            question["fragmentOrder"] = "→".join(new_id_by_text[text] for text in fragment_texts)

        distractor_explanations = question.get("distractorExplanations")
        if isinstance(distractor_explanations, dict):
            old_by_text = {text: distractor_explanations.get(label)
                           for label, text in current.items()}
            question["distractorExplanations"] = {
                new_id_by_text[text]: old_by_text[text]
                for text in row["newOptionOrder"]
                if text != target_text and old_by_text.get(text) is not None
            }
        if qid in explanations:
            question["explanationVi"] = explanations[qid]
    if seen != set(item for item in exam_rows if item in {q["id"] for q in items}):
        raise ValueError(f"Remapping application mismatch for {exam_id}")
    if apply_explanations and exam_id in {"N2-MOCK-08", "N2-MOCK-09"} and set(explanations) != set(exam_rows):
        raise ValueError(f"Vietnamese explanation coverage does not match 105 items in {exam_id}")
    return items
