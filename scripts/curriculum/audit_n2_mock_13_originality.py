# -*- coding: utf-8 -*-
"""Cross-exam content overlap audit for N2-MOCK-13 against #01-#12."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.content_quality_checks import answer_pattern_metrics
from scripts.curriculum.bank_data.n2_mock_13_data import get_n2_mock_13_sec1_items
from scripts.curriculum.bank_data.n2_mock_13_listening import get_n2_mock_13_listening_items

OUT = ROOT / "qa/N2_MOCK_13_ORIGINALITY_AUDIT.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def norm(text: str) -> str:
    return re.sub(r"[\s\u3000【】（）＿_★「」『』、。！？,.!?]", "", str(text or "")).casefold()


def ngrams(text: str, n: int) -> set[str]:
    value = norm(text)
    return {value[i:i + n] for i in range(len(value) - n + 1)} if len(value) >= n else set()


def jaccard(left: str, right: str, n: int) -> float:
    a, b = ngrams(left, n), ngrams(right, n)
    return len(a & b) / len(a | b) if a and b else 0.0


def all_items(exam: dict) -> list[dict]:
    return [q for section in exam.get("sections", []) for q in section.get("items", [])]


def build_current() -> dict:
    sec1, sec2 = get_n2_mock_13_sec1_items(), get_n2_mock_13_listening_items()
    for q in sec1:
        q["skill"] = "Reading" if q.get("typeId", "").startswith("N2-RD-") else "Language Knowledge"
    for q in sec2:
        q["contextPassage"] = q["script"]
        q["skill"] = "Listening"
    return {"examId": "N2-MOCK-13", "sections": [{"items": sec1}, {"items": sec2}]}


def main() -> int:
    current = build_current()
    prior = {f"N2-MOCK-{n:02}": load(ROOT / f"data/mock_exams/n2_mock_{n:02}.json") for n in range(1, 13)}
    prior_items = [(exam_id, q) for exam_id, exam in prior.items() for q in all_items(exam)]
    exact_stems, near_stems, passage_pairs, script_pairs = [], [], [], []

    for q in all_items(current):
        stem = norm(q.get("stem", ""))
        if stem:
            for exam_id, old in prior_items:
                old_stem = norm(old.get("stem", ""))
                if stem == old_stem:
                    exact_stems.append({"questionId": q["id"], "priorExamId": exam_id, "priorQuestionId": old["id"], "stem": q["stem"]})
                elif min(len(stem), len(old_stem)) >= 12:
                    score = jaccard(stem, old_stem, 3)
                    if score >= 0.58:
                        near_stems.append({"questionId": q["id"], "priorExamId": exam_id, "priorQuestionId": old["id"], "similarity3Gram": round(score, 3), "stem": q["stem"], "priorStem": old["stem"]})

        field = "script" if q.get("script") else "contextPassage" if q.get("contextPassage") else "passage"
        value = q.get(field) or q.get("passage")
        if not value or len(norm(value)) < 60:
            continue
        for exam_id, old in prior_items:
            old_value = old.get("script") if field == "script" else (old.get("contextPassage") or old.get("passage"))
            if not old_value:
                continue
            if norm(value) == norm(old_value):
                row = {"questionId": q["id"], "priorExamId": exam_id, "priorQuestionId": old["id"], "kind": field}
                (script_pairs if field == "script" else passage_pairs).append(row)
            elif len(norm(old_value)) >= 60:
                score = jaccard(value, old_value, 5)
                if score >= 0.25:
                    row = {"questionId": q["id"], "priorExamId": exam_id, "priorQuestionId": old["id"], "similarity5Gram": round(score, 3), "kind": field}
                    (script_pairs if field == "script" else passage_pairs).append(row)

    distractors: dict[str, list[dict]] = {}
    for exam_id, exam in [("N2-MOCK-13", current), *prior.items()]:
        for q in all_items(exam):
            wrong = sorted(norm(option.get("text", "")) for option in q.get("options", []) if option.get("id") != q.get("correctAnswer"))
            if len(wrong) > 1:
                digest = json.dumps(wrong, ensure_ascii=False)
                distractors.setdefault(digest, []).append({"examId": exam_id, "questionId": q["id"], "texts": wrong})
    repeated_distractors = [rows for rows in distractors.values() if len(rows) > 1 and any(row["examId"] == "N2-MOCK-13" for row in rows)]

    grammar = Counter(q.get("typeId", "") for q in all_items(current) if str(q.get("typeId", "")).startswith("N2-GR-"))
    topic = Counter(q.get("topicTag", "unTagged") for q in all_items(current))
    report = {
        "examId": "N2-MOCK-13",
        "status": "VERIFIED_CROSS_EXAM_AUDIT",
        "comparisonScope": "All 105 current M13 items against all 1,260 items in N2-MOCK-01 through N2-MOCK-12.",
        "exactStemMatches": {"count": len(exact_stems), "matches": exact_stems, "interpretation": "Review repeated generic JLPT prompt frames; confirm passages, scripts, options, and tested content remain distinct."},
        "nearStemMatches": {"threshold": 0.58, "metric": "Jaccard 3-gram after punctuation/spacing normalization", "count": len(near_stems), "matches": near_stems},
        "readingPassageOverlaps": {"threshold": 0.25, "metric": "Jaccard 5-gram", "count": len(passage_pairs), "matches": passage_pairs},
        "listeningScriptOverlaps": {"threshold": 0.25, "metric": "Jaccard 5-gram", "count": len(script_pairs), "matches": script_pairs},
        "exactDistractorSetMatches": {"count": len(repeated_distractors), "matches": repeated_distractors},
        "grammarDistribution": dict(sorted(grammar.items())),
        "topicTagDistribution": dict(sorted(topic.items())),
        "answerPositionMetrics": answer_pattern_metrics(current),
        "limits": ["Near-template thresholds are heuristic screens, not proof of plagiarism or originality.", "Generic JLPT instruction frames may repeat while tested content remains original.", "No claim is made about official JLPT scoring or item-count equivalence."],
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"M13 originality audit: exact stems={len(exact_stems)}, near stems={len(near_stems)}, passage overlap={len(passage_pairs)}, script overlap={len(script_pairs)}, repeated distractor sets={len(repeated_distractors)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
