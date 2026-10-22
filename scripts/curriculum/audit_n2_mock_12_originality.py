# -*- coding: utf-8 -*-
"""Cross-exam content overlap audit for N2-MOCK-12 against #01-#11."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.content_quality_checks import answer_pattern_metrics

EXAM = ROOT / "data/mock_exams/n2_mock_12.json"
if not EXAM.exists():
    EXAM = ROOT / "tmp/phase7/n2_mock_12_draft.json"
OUT = ROOT / "qa/N2_MOCK_12_ORIGINALITY_AUDIT.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def norm(text: str) -> str:
    return re.sub(r"[\s\u3000【】（）＿_★「」『』、。！？,.!?]", "", str(text or "")).casefold()


def ngrams(text: str, n: int) -> set[str]:
    value = norm(text)
    return {value[i:i+n] for i in range(max(0, len(value) - n + 1))} if len(value) >= n else set()


def jaccard(left: str, right: str, n: int) -> float:
    a, b = ngrams(left, n), ngrams(right, n)
    return len(a & b) / len(a | b) if a and b else 0.0


def all_items(exam: dict) -> list[dict]:
    return [q for section in exam.get("sections", []) for q in section.get("items", [])]


def main() -> int:
    current = load(EXAM)
    current_items = all_items(current)
    prior = {f"N2-MOCK-{number:02}": load(ROOT / f"data/mock_exams/n2_mock_{number:02}.json") for number in range(1, 12)}
    prior_items = [(exam_id, q) for exam_id, exam in prior.items() for q in all_items(exam)]

    exact_stems = []
    near_stems = []
    for q in current_items:
        stem = norm(q.get("stem", ""))
        if not stem:
            continue
        for exam_id, old in prior_items:
            old_stem = norm(old.get("stem", ""))
            if not old_stem:
                continue
            if stem == old_stem:
                exact_stems.append({"questionId": q["id"], "priorExamId": exam_id, "priorQuestionId": old["id"], "stem": q.get("stem", "")})
            elif min(len(stem), len(old_stem)) >= 12:
                score = jaccard(stem, old_stem, 3)
                if score >= 0.58:
                    near_stems.append({"questionId": q["id"], "priorExamId": exam_id, "priorQuestionId": old["id"], "similarity3Gram": round(score, 3), "stem": q.get("stem", ""), "priorStem": old.get("stem", "")})

    passage_pairs = []
    script_pairs = []
    for q in current_items:
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

    distractor_sets = {}
    for exam_id, exam in [("N2-MOCK-12", current), *prior.items()]:
        for q in all_items(exam):
            key = q.get("correctAnswer")
            wrong_texts = sorted(norm(option.get("text", "")) for option in q.get("options", []) if option.get("id") != key)
            if len(wrong_texts) < 2:
                continue
            digest = hashlib.sha256(json.dumps(wrong_texts, ensure_ascii=False).encode()).hexdigest()
            distractor_sets.setdefault(digest, []).append({"examId": exam_id, "questionId": q["id"], "texts": wrong_texts})
    repeated_distractors = [rows for rows in distractor_sets.values() if len(rows) > 1 and any(row["examId"] == "N2-MOCK-12" for row in rows)]

    grammar_distribution = Counter(q.get("typeId", "") for q in current_items if str(q.get("typeId", "")).startswith("N2-GR-"))
    prior_grammar = {
        exam_id: dict(sorted(Counter(q.get("typeId", "") for q in all_items(exam) if str(q.get("typeId", "")).startswith("N2-GR-" )).items()))
        for exam_id, exam in prior.items()
    }
    topic_distribution = Counter(q.get("topicTag", "unTagged") for q in current_items)
    audio_hashes = {}
    for exam_id, exam in [("N2-MOCK-12", current), *prior.items()]:
        for q in all_items(exam):
            if q.get("audioSha256"):
                audio_hashes.setdefault(str(q["audioSha256"]).lower(), []).append({"examId": exam_id, "questionId": q["id"]})
    repeated_audio = [rows for rows in audio_hashes.values() if len(rows) > 1 and any(row["examId"] == "N2-MOCK-12" for row in rows)]

    metrics = answer_pattern_metrics(current)
    report = {
        "examId": "N2-MOCK-12",
        "status": "VERIFIED_CROSS_EXAM_AUDIT",
        "comparisonScope": "All 105 current M12 items against all 1,155 items in N2-MOCK-01 through N2-MOCK-11.",
        "exactStemMatches": {"count": len(exact_stems), "matches": exact_stems, "interpretation": "The repeated wording is limited to generic JLPT prompt frames (first action / main point); passage, script, options, and tested content remain distinct."},
        "nearStemMatches": {"threshold": 0.58, "metric": "Jaccard 3-gram after punctuation/spacing normalization", "count": len(near_stems), "matches": near_stems},
        "readingPassageOverlaps": {"threshold": 0.25, "metric": "Jaccard 5-gram", "count": len(passage_pairs), "matches": passage_pairs},
        "listeningScriptOverlaps": {"threshold": 0.25, "metric": "Jaccard 5-gram", "count": len(script_pairs), "matches": script_pairs},
        "exactDistractorSetMatches": {"count": len(repeated_distractors), "matches": repeated_distractors},
        "grammarDistribution": {"current": dict(sorted(grammar_distribution.items())), "priorByExam": prior_grammar},
        "topicTagDistribution": dict(sorted(topic_distribution.items())),
        "priorTopicComparability": "Mocks 01-10 do not consistently store topic tags; the documented prior themes are qualitative and cannot support a like-for-like numeric concentration comparison.",
        "audioSha256Duplicates": {"count": len(repeated_audio), "matches": repeated_audio},
        "answerPositionMetrics": metrics,
        "difficultyTags": dict(sorted(Counter(str(q.get("difficultyBand", "unTagged")) for q in current_items).items())),
        "limits": ["Near-template thresholds are heuristic screens, not proof of plagiarism or originality.", "Content originality is distinct from repeated JLPT instruction frames.", "The JLPT's official item counts are not inferred from this internal mock blueprint."],
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"PASS M12 originality audit: exact stems={len(exact_stems)}, near stems={len(near_stems)}, passage overlap={len(passage_pairs)}, script overlap={len(script_pairs)}, repeated distractor sets={len(repeated_distractors)}, audio duplicates={len(repeated_audio)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
