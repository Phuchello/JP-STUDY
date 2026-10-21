"""Production validators shared by Phase 6.1 release checks and tests."""
from __future__ import annotations

import re
from collections import Counter

JAPANESE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]")
VIETNAMESE = re.compile(r"[ăâđêôơưĂÂĐÊÔƠƯáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]", re.I)
AUDIO_COUPLED_TYPES = {"N2-LIS-SUMM", "N2-LIS-OUTL", "N2-LIS-GIST", "N2-LIS-RESP"}
ANSWER_LETTER_REFERENCE_PATTERNS = (
    re.compile(r"\b(?:đáp án|câu trả lời)\s+([ABCD])\s+(?:đúng|chính xác)\b", re.I),
    re.compile(r"\b(?:đáp án|câu trả lời)(?: đúng)?\s*(?:là|:)?\s*\(?([ABCD])\)?(?=\s|[.,;:!?]|$)"),
    re.compile(r"\b(?:the correct answer|answer)\s*(?:is|:)?\s*\(?([ABCD])\)?(?=\s|[.,;:!?]|$)", re.I),
    re.compile(r"\b(?:option|phương án|lựa chọn)\s+([ABCD])\b.{0,35}\b(?:đúng|correct)\b"),
    re.compile(r"(?:正解|答え)\s*(?:は|が|：|:)?\s*([ABCD])(?:が正しい|が適切|です)"),
)


def explanation_language_stats(text: str) -> dict:
    text = str(text or "").strip()
    letters = [c for c in text if c.isalpha()]
    ja_count = sum(bool(JAPANESE.fullmatch(c)) for c in letters)
    return {
        "chars": len(text),
        "words": len(re.findall(r"\b[\wÀ-ỹ]+\b", text, re.UNICODE)),
        "japaneseLetterRatio": ja_count / len(letters) if letters else 0.0,
        "vietnameseDiacritics": len(VIETNAMESE.findall(text)),
    }


def validate_vietnamese_explanations(exam: dict, *, require_all: bool = True) -> list[str]:
    errors = []
    all_items = [q for section in exam.get("sections", []) for q in section.get("items", [])]
    explanations = [str(q.get("explanationVi", "")).strip() for q in all_items]
    for q, explanation in zip(all_items, explanations):
        stats = explanation_language_stats(explanation)
        if not explanation:
            errors.append(f"{q.get('id')}: empty explanationVi")
        elif stats["words"] < 10 or stats["vietnameseDiacritics"] < 3 or stats["japaneseLetterRatio"] > 0.62:
            errors.append(f"{q.get('id')}: explanationVi is too short or predominantly non-Vietnamese")
    if require_all and exam.get("examId") in {"N2-MOCK-08", "N2-MOCK-09"} and len(all_items) != 105:
        errors.append(f"{exam.get('examId')}: expected 105 items, got {len(all_items)}")
    normalized = [re.sub(r"\s+", " ", value).casefold() for value in explanations]
    duplicates = Counter(x for x in normalized if x)
    for duplicate, count in duplicates.items():
        if count >= 3:
            errors.append(f"generic/duplicate explanation occurs {count} times: {duplicate[:80]}")
    generic_patterns = (
        r"đáp án [a-d] đúng vì phù hợp với ngữ cảnh",
        r"chọn [a-d] vì đây là đáp án đúng",
        r"phương án [a-d] là đáp án chính xác",
        r"đây là đáp án đúng",
    )
    generic_count = sum(bool(any(re.search(p, value, re.I) for p in generic_patterns)) for value in normalized)
    if generic_count >= 3:
        errors.append(f"{generic_count} generic answer-only explanations")
    return errors


def validate_answer_letter_references(exam: dict) -> list[str]:
    """Flag explicit answer-letter claims that disagree with the current key."""
    errors = []
    for section in exam.get("sections", []):
        for question in section.get("items", []):
            key = str(question.get("correctAnswer", "")).strip().upper()
            text_fields = [question.get("explanation", ""), question.get("explanationVi", "")]
            text_fields.extend((question.get("distractorExplanations") or {}).values())
            for text in text_fields:
                for pattern in ANSWER_LETTER_REFERENCE_PATTERNS:
                    for match in pattern.finditer(str(text or "")):
                        label = match.group(1).upper()
                        if label != key:
                            errors.append(f"{question.get('id')}: explicit answer-letter reference {label} disagrees with current key {key}")
            distractors = question.get("distractorExplanations")
            if isinstance(distractors, dict):
                valid_wrong_ids = {str(option.get("id", "")) for option in question.get("options", [])
                                   if str(option.get("id", "")) != key}
                stale_keys = set(map(str, distractors)) - valid_wrong_ids
                if stale_keys:
                    errors.append(f"{question.get('id')}: distractor explanation keys are not current wrong-option IDs: {sorted(stale_keys)}")
    return errors


def longest_pattern_run(sequence: str, max_period: int = 4) -> dict:
    best = {"length": 0, "period": 0, "start": 0, "pattern": ""}
    n = len(sequence)
    for period in range(1, min(max_period, n) + 1):
        for start in range(n):
            length = min(period, n - start)
            while start + length < n and sequence[start + length] == sequence[start + length - period]:
                length += 1
            if length > best["length"]:
                best = {"length": length, "period": period, "start": start,
                        "pattern": sequence[start:start + min(period, n - start)]}
    return best


def longest_constant_run(sequence: str) -> dict:
    best = {"length": 0, "answer": "", "start": 0}
    start = 0
    while start < len(sequence):
        end = start + 1
        while end < len(sequence) and sequence[end] == sequence[start]:
            end += 1
        if end - start > best["length"]:
            best = {"length": end - start, "answer": sequence[start], "start": start}
        start = end
    return best


def answer_pattern_metrics(exam: dict) -> dict:
    sections = exam.get("sections", [])
    s1 = sections[0].get("items", []) if sections else []
    all_items = [q for section in sections for q in section.get("items", [])]
    seq = "".join(str(q.get("correctAnswer", "")) for q in all_items)
    s1_seq = "".join(str(q.get("correctAnswer", "")) for q in s1)
    stars = [q for q in s1 if q.get("typeId") == "N2-GR-STAR"]
    return {
        "answerCounts": dict(sorted(Counter(seq).items())),
        "section1Counts": dict(sorted(Counter(s1_seq).items())),
        "longestCycleOrShortPattern": longest_pattern_run(seq),
        "section1LongestCycleOrShortPattern": longest_pattern_run(s1_seq),
        "longestSameAnswerRun": longest_constant_run(seq),
        "starAnswers": "".join(str(q.get("correctAnswer", "")) for q in stars),
        "starCounts": dict(sorted(Counter(str(q.get("correctAnswer", "")) for q in stars).items())),
    }


def pattern_defects(exams: dict[str, dict]) -> list[str]:
    defects = []
    metrics = {key: answer_pattern_metrics(value) for key, value in exams.items()}
    for exam_id, row in metrics.items():
        cycle = row["longestCycleOrShortPattern"]
        run = row["longestSameAnswerRun"]
        all_items = [q for section in exams[exam_id].get("sections", []) for q in section.get("items", [])]
        section1_items = exams[exam_id].get("sections", [])[0].get("items", [])
        if cycle["length"] >= 9:
            defects.append(f"{exam_id}: repeated period-{cycle['period']} pattern spans {cycle['length']} answers")
        if run["length"] >= 5:
            defects.append(f"{exam_id}: same-answer run spans {run['length']} answers")
        if len(row["starAnswers"]) == 5 and len(set(row["starAnswers"])) == 1:
            defects.append(f"{exam_id}: all five STAR answers use {row['starAnswers'][0]}")
        for label in "ABCD":
            opportunities = sum(any(str(option.get("id")) == label for option in q.get("options", []))
                                for q in all_items)
            observed = row["answerCounts"].get(label, 0)
            if opportunities and observed / opportunities > 0.38:
                defects.append(f"{exam_id}: answer position {label} is over-concentrated ({observed}/{opportunities})")
            s1_opportunities = sum(any(str(option.get("id")) == label for option in q.get("options", []))
                                   for q in section1_items)
            s1_observed = row["section1Counts"].get(label, 0)
            if s1_opportunities and s1_observed / s1_opportunities > 0.38:
                defects.append(f"{exam_id}: section-1 answer position {label} is over-concentrated ({s1_observed}/{s1_opportunities})")
    pairs = list(exams)
    for i, exam_a in enumerate(pairs):
        for exam_b in pairs[i + 1:]:
            a = exams[exam_a].get("sections", [])[0].get("items", [])
            b = exams[exam_b].get("sections", [])[0].get("items", [])
            if len(a) == len(b) == 75:
                matches = sum(x.get("correctAnswer") == y.get("correctAnswer") for x, y in zip(a, b))
                if matches > 50:
                    defects.append(f"{exam_a}/{exam_b}: {matches}/75 section-1 positions align")
    return defects


def validate_semantic_remap(original: dict, revised: dict, record: dict) -> list[str]:
    errors = []
    old_options = {str(x["id"]): str(x["text"]).strip() for x in original.get("options", [])}
    new_options = {str(x["id"]): str(x["text"]).strip() for x in revised.get("options", [])}
    if sorted(old_options.values()) != sorted(new_options.values()):
        errors.append(f"{original.get('id')}: option text set changed")
        return errors
    old_key_text = old_options.get(str(original.get("correctAnswer", "")))
    new_key_text = new_options.get(str(revised.get("correctAnswer", "")))
    if old_key_text != record.get("originalCorrectText") or new_key_text != record.get("originalCorrectText"):
        errors.append(f"{original.get('id')}: correct semantic option changed")
    if revised.get("typeId") == "N2-GR-STAR":
        labels = re.findall(r"[A-D]", str(revised.get("fragmentOrder", "")).upper())
        if len(labels) != 4 or len(set(labels)) != 4 or len(labels) < 3:
            errors.append(f"{original.get('id')}: STAR fragment order is invalid")
        elif new_options.get(str(revised.get("correctAnswer"))) != new_options[labels[2]]:
            errors.append(f"{original.get('id')}: STAR key is not the fragment at ★")
    return errors


def remap_review_selection(original: dict, revised: dict, selected_id: str) -> dict:
    old_options = {str(x["id"]): str(x["text"]).strip() for x in original.get("options", [])}
    text = old_options.get(str(selected_id))
    if text is None:
        raise ValueError("Reviewer selection is absent from its immutable sealed input")
    matches = [str(x["id"]) for x in revised.get("options", []) if str(x["text"]).strip() == text]
    if len(matches) != 1:
        raise ValueError("Reviewer selection does not map uniquely by exact option text")
    return {"oldId": str(selected_id), "optionText": text, "newId": matches[0],
            "mappingMethod": "EXACT_OPTION_TEXT_DERIVATION"}


def validate_spoken_audio(question: dict, evidence: dict | None) -> list[str]:
    if question.get("typeId") not in AUDIO_COUPLED_TYPES:
        return []
    if not isinstance(evidence, dict) or evidence.get("status") != "VERIFIED":
        return [f"{question.get('id')}: spoken option reorder lacks verified audio evidence"]
    texts = [str(row.get("text", "")).strip() for row in question.get("options", [])]
    if evidence.get("orderedOptionTexts") != texts:
        return [f"{question.get('id')}: spoken option order differs from verified display order"]
    digest = str(evidence.get("audioSha256", "")).lower()
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        return [f"{question.get('id')}: missing valid regenerated audio SHA-256"]
    if evidence.get("audioWasRegenerated") is not True:
        return [f"{question.get('id')}: reordered spoken options did not regenerate the MP3"]
    return []
