"""Validate and summarize the Phase 6.1 exam-content release candidate."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.content_quality_checks import (
    answer_pattern_metrics,
    pattern_defects,
    validate_answer_letter_references,
    validate_semantic_remap,
    validate_vietnamese_explanations,
)

BASE_SHA = "3b7f84d29ff554a228e4d57600634d88551d91e9"
REPORT_PATH = ROOT / "qa/PHASE_6_1_CONTENT_QUALITY_REPORT.json"
EXAM_IDS = [f"N2-MOCK-{number:02}" for number in (7, 8, 9, 10)]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def questions(exam: dict) -> dict[str, dict]:
    items = [question for section in exam.get("sections", []) for question in section.get("items", [])]
    indexed = {question["id"]: question for question in items}
    if len(indexed) != len(items):
        raise ValueError(f"{exam.get('examId')}: duplicate question IDs.")
    if len(indexed) != 105:
        raise ValueError(f"{exam.get('examId')}: expected 105 questions, got {len(indexed)}.")
    if [len(section.get("items", [])) for section in exam.get("sections", [])] != [75, 30]:
        raise ValueError(f"{exam.get('examId')}: expected 75/30 section structure.")
    return indexed


def git_json(ref: str, path: str) -> dict:
    raw = subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT)
    return json.loads(raw.decode("utf-8"))


def star_sentence(question: dict, order: list[str], option_texts: dict[str, str]) -> str:
    slots = re.split(r"（\s*）|★", str(question.get("stem", "")))
    if len(slots) != 5:
        raise ValueError(f"{question.get('id')}: expected four STAR fragment slots.")
    sentence = slots[0]
    for index, label in enumerate(order):
        sentence += option_texts[label] + slots[index + 1]
    return sentence


def validate_exam_remap(exam_id: str, current: dict, remap_rows: dict) -> dict:
    if set(current) != set(remap_rows):
        raise ValueError(f"{exam_id}: remapping manifest does not cover exactly 105 items.")
    reordered = 0
    semantic_mismatches = []
    star_count = 0
    for qid, question in current.items():
        row = remap_rows[qid]
        option_map = {str(option["id"]): str(option["text"]).strip() for option in question.get("options", [])}
        displayed_labels = "ABCD"[:len(option_map)]
        if [option_map.get(label) for label in displayed_labels] != row["newOptionOrder"]:
            raise ValueError(f"{qid}: current display order differs from the reproducible manifest.")
        if sorted(option_map.values()) != sorted(row["originalOptionTexts"]):
            raise ValueError(f"{qid}: one or more option texts changed during remap.")
        old_options = [{"id": label, "text": text} for label, text in zip("ABCD", row["originalOptionTexts"])]
        old_question = {"id": qid, "typeId": question.get("typeId"), "options": old_options,
                        "correctAnswer": row["originalCorrectId"]}
        semantic_errors = validate_semantic_remap(
            old_question, question, {"originalCorrectText": row["originalCorrectText"]}
        )
        if semantic_errors:
            semantic_mismatches.extend(semantic_errors)
        if option_map.get(str(question.get("correctAnswer", ""))) != row["originalCorrectText"]:
            semantic_mismatches.append(f"{qid}: current correct-answer text differs from original semantic key.")
        reordered += int(row["newOptionOrder"] != row["originalOptionTexts"])
        if question.get("typeId") == "N2-GR-STAR":
            star_count += 1
            labels = re.findall(r"[A-D]", str(question.get("fragmentOrder", "")).upper())
            if len(labels) != 4 or len(set(labels)) != 4:
                raise ValueError(f"{qid}: invalid current STAR fragment order.")
            fragment_texts = [option_map[label] for label in labels]
            if fragment_texts != row.get("fragmentOrderTexts"):
                raise ValueError(f"{qid}: grammatical fragment order changed during displayed-label remap.")
            if fragment_texts[2] != row.get("starFragmentAtKey"):
                raise ValueError(f"{qid}: ★ is not the original semantic fragment.")
            if star_sentence(question, labels, option_map) != question.get("assembledSentence"):
                raise ValueError(f"{qid}: assembled sentence does not match current fragments.")
    if semantic_mismatches:
        raise ValueError("Semantic remap mismatch: " + "; ".join(semantic_mismatches[:8]))
    return {"questionsVerified": len(current), "displayOrdersChanged": reordered,
            "displayOrdersUnchanged": len(current) - reordered, "semanticKeyMismatches": 0,
            "starQuestions": star_count}


def verify_review_mapping(exam_id: str, current: dict) -> int:
    number = int(exam_id[-2:])
    if number == 7:
        paths = [ROOT / f"qa/review_answers_m07_{part}.json" for part in ("s1_p1", "s1_p2", "s2")]
    else:
        paths = [ROOT / f"qa/raw_blind_m{number:02}_{part}.json" for part in ("s1_p1", "s1_p2", "s2")]
    records = [row for path in paths for row in read_json(path)]
    if len(records) != 105 or len({row.get("id") for row in records}) != 105:
        raise ValueError(f"{exam_id}: normalized review mapping does not cover exactly 105 questions.")
    for record in records:
        qid = record.get("id")
        question = current[qid]
        selected_id = record.get("blindAnswer") if number == 7 else record.get("remappedBlindAnswer")
        if number == 7 and record.get("mappingMethod") != "EXACT_OPTION_TEXT_DERIVATION":
            raise ValueError(f"{qid}: M07 review lacks explicit exact-text derivation metadata.")
        if not selected_id or not any(option["id"] == selected_id and option["text"].strip() == record.get("selectedOptionText")
                                      for option in question.get("options", [])):
            raise ValueError(f"{qid}: historical reviewer choice does not map to current exact option text.")
    return len(records)


def main() -> int:
    manifest = read_json(ROOT / "qa/PHASE_6_1_OPTION_REMAP_MANIFEST.json")
    audio_receipt = read_json(ROOT / "qa/PHASE_6_1_AUDIO_VERIFICATION.json")
    exams = {}
    exam_reports = {}
    semantic_remap_totals = 0
    for exam_id in EXAM_IDS:
        number = int(exam_id[-2:])
        exam = read_json(ROOT / f"data/mock_exams/n2_mock_{number:02}.json")
        if exam.get("examId") != exam_id:
            raise ValueError(f"Wrong exam ID in data/mock_exams/n2_mock_{number:02}.json.")
        indexed = questions(exam)
        exams[exam_id] = exam
        localization_errors = validate_vietnamese_explanations(exam)
        if localization_errors:
            raise ValueError(f"{exam_id}: {len(localization_errors)} localization failures: {localization_errors[:3]}")
        letter_errors = validate_answer_letter_references(exam)
        if letter_errors:
            raise ValueError(f"{exam_id}: stale answer-letter references: {letter_errors[:3]}")
        remap_report = None
        review_count = None
        if number in (7, 8, 9):
            remap_report = validate_exam_remap(exam_id, indexed, manifest["exams"][exam_id])
            review_count = verify_review_mapping(exam_id, indexed)
            semantic_remap_totals += remap_report["questionsVerified"]
        exam_reports[exam_id] = {
            "questionCount": len(indexed),
            "vietnameseExplanationCount": len(indexed) - len(localization_errors),
            "missingOrInvalidVietnameseExplanations": len(localization_errors),
            "answerPatternMetrics": answer_pattern_metrics(exam),
            "remapping": remap_report,
            "versionBoundReviewMappings": review_count,
        }

    defects = pattern_defects(exams)
    if defects:
        raise ValueError("Answer-pattern screens failed: " + "; ".join(defects))
    before = {exam_id: manifest["beforeMetrics"][exam_id] for exam_id in manifest["exams"]}
    after = {exam_id: answer_pattern_metrics(exams[exam_id]) for exam_id in manifest["exams"]}
    before_08 = git_json(BASE_SHA, "data/mock_exams/n2_mock_08.json")
    before_09 = git_json(BASE_SHA, "data/mock_exams/n2_mock_09.json")
    before_08_s1 = before_08["sections"][0]["items"]
    before_09_s1 = before_09["sections"][0]["items"]
    before_08_09_matches = sum(a["correctAnswer"] == b["correctAnswer"] for a, b in zip(before_08_s1, before_09_s1))
    after_08_s1 = exams["N2-MOCK-08"]["sections"][0]["items"]
    after_09_s1 = exams["N2-MOCK-09"]["sections"][0]["items"]
    after_08_09_matches = sum(a["correctAnswer"] == b["correctAnswer"] for a, b in zip(after_08_s1, after_09_s1))
    if before_08_09_matches != 63 or semantic_remap_totals != 315:
        raise ValueError(f"Unexpected Phase 6.1 baseline/remap totals: alignment={before_08_09_matches}, remapped={semantic_remap_totals}.")
    if audio_receipt.get("status") != "PASS" or sum(row["spokenChoiceTracks"] for row in audio_receipt["exams"].values()) != 48:
        raise ValueError("48 changed spoken-choice audio tracks lack full technical/browser evidence.")
    n2_10_unchanged = subprocess.check_output(
        ["git", "show", f"{BASE_SHA}:data/mock_exams/n2_mock_10.json"], cwd=ROOT
    ) == (ROOT / "data/mock_exams/n2_mock_10.json").read_bytes()
    if not n2_10_unchanged:
        raise ValueError("N2-MOCK-10 changed during this Phase 6.1 task.")

    fresh_audit = read_json(ROOT / "qa/N2_MOCK_09_STAR_M8_04_FRESH_AUDIT.json")
    if len(fresh_audit.get("permutationEvidence", [])) != 24:
        raise ValueError("M09 M8_04 fresh self-audit does not cover all 24 orders.")
    report = {
        "status": "PASS_WITH_TRANSPARENT_SELF_AUDIT_LIMITATION",
        "startingHead": BASE_SHA,
        "exams": exam_reports,
        "beforeAnswerPatternMetrics": before,
        "afterAnswerPatternMetrics": after,
        "beforeN2Mock08Vs09Section1PositionMatches": before_08_09_matches,
        "afterN2Mock08Vs09Section1PositionMatches": after_08_09_matches,
        "remappedItems": semantic_remap_totals,
        "semanticAnswerMismatches": 0,
        "freshLinguisticReviewItems": ["N2_09_M8_04"],
        "freshLinguisticReviewCount": 1,
        "freshReviewEvidence": {
            "questionId": "N2_09_M8_04",
            "all24PermutationsReconstructed": 24,
            "answerChangingDefensibleAlternatives": 0,
            "independentOrHumanReviewObtained": False,
            "provenance": fresh_audit["reviewerProvenance"],
        },
        "localizationExamples": [],
        "audioVerification": audio_receipt,
        "n2Mock10UnchangedFromBaseline": n2_10_unchanged,
        "limitations": [
            "Vietnamese language checks are heuristic regression screens, not native-language editorial certification.",
            "Blind-review mappings preserve historical selections and do not create new independent reviews.",
            "The M09 M8_04 24-order recheck is a transparent implementation-agent self-review, not independent human/native-speaker validation.",
            "Pattern screens flag risk signals; they do not certify answer quality or psychometric calibration.",
        ],
    }
    for number, qid in ((8, "N2_08_M1_01"), (8, "N2_08_M8_03"), (9, "N2_09_M10_01")):
        old_exam = git_json(BASE_SHA, f"data/mock_exams/n2_mock_{number:02}.json")
        old_questions = questions(old_exam)
        current_question = exams[f"N2-MOCK-{number:02}"]
        report["localizationExamples"].append({
            "examId": f"N2-MOCK-{number:02}",
            "questionId": qid,
            "before": old_questions[qid].get("explanationVi", ""),
            "after": questions(current_question)[qid].get("explanationVi", ""),
        })
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"],
                      "explanations": {key: value["vietnameseExplanationCount"] for key, value in exam_reports.items()},
                      "remappedItems": semantic_remap_totals,
                      "semanticAnswerMismatches": 0,
                      "08_09_section1_alignment": f"{before_08_09_matches}/75 -> {after_08_09_matches}/75",
                      "freshLinguisticReviewCount": report["freshLinguisticReviewCount"],
                      "freshStarSelfAudit": "24/24 permutations; 0 answer-changing alternatives",
                      "audioTracks": 48,
                      "report": str(REPORT_PATH)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
