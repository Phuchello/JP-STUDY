"""Create the reproducible, exact-text option permutation manifest once."""
from __future__ import annotations

import copy
import hashlib
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.content_quality_checks import answer_pattern_metrics, pattern_defects
from scripts.curriculum.phase_61_option_remapping import _star_fragment_order
from scripts.curriculum.question_fingerprint import compute_question_fingerprint, compute_option_text_fingerprint


def stable_order(exam_id: str, qid: str, original_texts: list[str], salt: int) -> list[str]:
    seed_text = "\0".join(("JP-STUDY Phase 6.1 option remap v1", exam_id, qid, str(salt), *original_texts))
    seed = int.from_bytes(hashlib.sha256(seed_text.encode("utf-8")).digest(), "big")
    order = list(original_texts)
    random.Random(seed).shuffle(order)
    return order


def apply_simulated(exam: dict, rows: dict) -> dict:
    candidate = copy.deepcopy(exam)
    for section in candidate["sections"]:
        for q in section["items"]:
            row = rows[q["id"]]
            new_texts = row["newOptionOrder"]
            by_text = {o["text"]: o for o in q["options"]}
            q["options"] = [{"id": "ABCD"[i], **{k: v for k, v in by_text[text].items() if k != "id"}}
                            for i, text in enumerate(new_texts)]
            q["correctAnswer"] = next("ABCD"[i] for i, text in enumerate(new_texts)
                                      if text == row.get("starFragmentAtKey", row["originalCorrectText"]))
            if q.get("typeId") == "N2-GR-STAR":
                q["fragmentOrder"] = "→".join(
                    next("ABCD"[i] for i, new_text in enumerate(new_texts) if new_text == text)
                    for text in row["fragmentOrderTexts"]
                )
    return candidate


def create_manifest(salt: int) -> dict:
    exams = {}
    before_metrics = {}
    simulated = {}
    baseline_explanation_examples = {}
    for number in (7, 8, 9):
        exam_id = f"N2-MOCK-{number:02}"
        path = ROOT / f"data/mock_exams/n2_mock_{number:02}.json"
        exam = json.loads(path.read_text(encoding="utf-8"))
        before_metrics[exam_id] = answer_pattern_metrics(exam)
        rows = {}
        for section in exam["sections"]:
            for q in section["items"]:
                original_options = sorted(q["options"], key=lambda row: str(row["id"]))
                original_texts = [str(row["text"]).strip() for row in original_options]
                correct_id = str(q["correctAnswer"]).strip()
                original_correct_text = next((str(row["text"]).strip() for row in original_options
                                              if str(row["id"]) == correct_id), None)
                if original_correct_text is None or len(set(original_texts)) != len(original_texts):
                    raise ValueError(f"Invalid authored key/options for {q['id']}")
                row = {
                    "originalOptionTexts": original_texts,
                    "newOptionOrder": stable_order(exam_id, q["id"], original_texts, salt),
                    "originalCorrectId": correct_id,
                    "originalCorrectText": original_correct_text,
                    "optionTextSetSha256": compute_option_text_fingerprint(q["options"]),
                    "sourceQuestionFingerprint": compute_question_fingerprint(q),
                    "audioRemapRequired": q.get("typeId") in {
                        "N2-LIS-SUMM", "N2-LIS-OUTL", "N2-LIS-GIST", "N2-LIS-RESP"
                    },
                    "audioStatus": "PENDING" if q.get("typeId") in {
                        "N2-LIS-SUMM", "N2-LIS-OUTL", "N2-LIS-GIST", "N2-LIS-RESP"
                    } else "NOT_SPOKEN",
                }
                if q["id"] in {"N2_08_M1_01", "N2_08_M8_03", "N2_09_M10_01"}:
                    baseline_explanation_examples[q["id"]] = q.get("explanationVi", "")
                if q.get("typeId") == "N2-GR-STAR":
                    fragment_order = _star_fragment_order(q)
                    if len(fragment_order) != 4 or len(set(fragment_order)) != 4:
                        raise ValueError(f"STAR must have one unambiguous four-fragment order: {q['id']}")
                    if original_correct_text != fragment_order[2]:
                        raise ValueError(f"STAR key does not point to grammatical third fragment: {q['id']}")
                    row["fragmentOrderTexts"] = fragment_order
                    row["starFragmentAtKey"] = fragment_order[2]
                rows[q["id"]] = row
        exams[exam_id] = rows
        simulated[exam_id] = apply_simulated(exam, rows)
    return {
        "schemaVersion": 1,
        "purpose": "Reproducible text-preserving display-label remap; raw reviewer artifacts remain immutable.",
        "method": "Independent SHA-256-derived Python PRNG seed per exam/question; Fisher-Yates shuffle; no target quota.",
        "salt": salt,
        "baselineN2Mock10Sha256": hashlib.sha256(
            (ROOT / "data/mock_exams/n2_mock_10.json").read_bytes()
        ).hexdigest(),
        "baselineExplanationExamples": baseline_explanation_examples,
        "exams": exams,
        "beforeMetrics": before_metrics,
        "afterMetrics": {exam_id: answer_pattern_metrics(exam) for exam_id, exam in simulated.items()},
    }


def main() -> None:
    output = ROOT / "qa/PHASE_6_1_OPTION_REMAP_MANIFEST.json"
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite the Phase 6.1 source baseline: {output}")
    for salt in range(10000):
        manifest = create_manifest(salt)
        exams = {}
        for n in (7, 8, 9):
            exam_id = f"N2-MOCK-{n:02}"
            original = json.loads((ROOT / f"data/mock_exams/n2_mock_{n:02}.json").read_text(encoding="utf-8"))
            exams[exam_id] = apply_simulated(original, manifest["exams"][exam_id])
        defects = pattern_defects(exams)
        if not defects:
            output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"Wrote {output.relative_to(ROOT)} using deterministic salt {salt}.")
            print("All Phase 6.1 answer-pattern screens passed.")
            print(json.dumps(manifest["afterMetrics"], ensure_ascii=False, indent=2))
            return
    raise RuntimeError("No valid independent option permutation found in 10,000 attempts")


if __name__ == "__main__":
    main()
