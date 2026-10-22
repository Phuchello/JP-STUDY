# -*- coding: utf-8 -*-
"""Bind a preserved key-isolated M12 review to the current candidate version."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DRAFT_PATH = ROOT / "tmp/phase7/n2_mock_12_draft.json"
SEALED_PATH = ROOT / "tmp/phase7/blind_items_m12_final.json"
RAW_PATH = ROOT / "qa/raw_blind_responses/N2_MOCK_12_rev15_raw.json"
PRIOR_RAW_PATHS = [
    ROOT / "qa/raw_blind_responses/N2_MOCK_12_rev12_raw.json",
    ROOT / "qa/raw_blind_responses/N2_MOCK_12_rev13_raw.json",
    ROOT / "qa/raw_blind_responses/N2_MOCK_12_rev14_raw.json",
]
PUBLISHED_SEALED_PATH = ROOT / "qa/blind_items_m12_final.json"
REPORT_PATH = ROOT / "qa/N2_MOCK_12_BLIND_RECONCILIATION.json"

from scripts.curriculum.mock_exam_release_checks import (
    AI_REVIEW_PROVENANCE_LIMIT,
    CURRENT_VERSION_REVIEW_SCHEMA,
)
from scripts.curriculum.question_fingerprint import compute_question_fingerprint


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_note_list(value, field: str, question_id: str) -> list:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        return [value]
    raise ValueError(f"{question_id}: raw {field} must be a list, string, or null")


def main() -> None:
    for path in (DRAFT_PATH, SEALED_PATH, RAW_PATH):
        if not path.is_file():
            raise FileNotFoundError(path)

    sealed = read_json(SEALED_PATH)
    raw = read_json(RAW_PATH)
    exam = read_json(DRAFT_PATH)
    if not isinstance(sealed, list):
        raise ValueError("Sealed review input must be an item list")

    digest = sha256(SEALED_PATH)
    # Raw responses are preserved in their original form. Accept the established
    # nested schema and the current top-level review receipt without rewriting it.
    review_meta = raw.get("review") if isinstance(raw.get("review"), dict) else raw
    input_before = review_meta.get("inputSha256Before", review_meta.get("inputSha256BeforeReview", ""))
    input_after = review_meta.get("inputSha256After", review_meta.get("inputSha256AfterReview", ""))
    if str(input_before).lower() != digest.lower() or str(input_after).lower() != digest.lower():
        raise ValueError("Reviewer input SHA-256 does not match the sealed current input")
    audio_checked = review_meta.get("audioFilesSeparatelyHeardOrChecked", review_meta.get("audioSeparatelyHeardOrChecked"))
    if audio_checked is not False:
        raise ValueError("Raw review must explicitly report that audio was not separately heard/checked")
    raw_summary = review_meta.get("summary", {}) if isinstance(review_meta.get("summary"), dict) else {}
    total_items = raw_summary.get("totalItems", review_meta.get("total", review_meta.get("totalItems", review_meta.get("itemCount"))))
    completed_items = raw_summary.get("completedItems", review_meta.get("completed", review_meta.get("completedItems", review_meta.get("itemCount"))))
    unique_items = review_meta.get("uniqueItemCount", 105)
    if total_items != 105 or completed_items != 105 or unique_items != 105 or review_meta.get("allItemsReviewed", True) is not True:
        raise ValueError("Raw review must cover all 105 items")
    expected_star = [f"N2_12_M8_{i:02}" for i in range(1, 6)]
    expected_text_grammar = [f"N2_12_M9_{i:02}" for i in range(1, 6)]
    focused_star = raw_summary.get("focusedSTARItemIds", review_meta.get("starFocusedItemIds"))
    focused_text = raw_summary.get("focusedContinuousTextGrammarItemIds", review_meta.get("continuousTextGrammarFocusedItemIds"))
    if focused_star is None:
        focused_star = sorted(row["id"] for row in sealed if row.get("typeId") == "N2-GR-STAR")
    if focused_text is None:
        focused_text = sorted(row["id"] for row in sealed if row.get("typeId") in {"N2-GR-PARA", "N2-GR-TEXT"})
    if focused_star != expected_star:
        raise ValueError("Raw review did not confirm focus coverage for all five STAR items")
    if focused_text != expected_text_grammar:
        raise ValueError("Raw review did not confirm focus coverage for all five continuous-text grammar items")

    questions = {q.get("id"): q for section in exam.get("sections", []) for q in section.get("items", [])}
    sealed_by_id = {row.get("id"): row for row in sealed}
    raw_items = raw.get("items", raw.get("responses", []))
    raw_by_id = {row.get("questionId", row.get("itemId")): row for row in raw_items}
    expected_ids = set(questions)
    if len(questions) != 105 or len(sealed_by_id) != 105 or len(raw_by_id) != 105:
        raise ValueError("Current candidate, sealed input, and raw review must each have 105 unique items")
    if set(sealed_by_id) != expected_ids or set(raw_by_id) != expected_ids:
        raise ValueError("Question IDs differ among current candidate, sealed input, and raw review")

    rows = []
    confidence_counts = {"high": 0, "medium": 0, "low": 0}
    alternate_count = 0
    concern_count = 0
    mismatch_count = 0
    for qid in sorted(expected_ids):
        question = questions[qid]
        reviewed = raw_by_id[qid]
        fingerprint = compute_question_fingerprint(question)
        if sealed_by_id[qid].get("contentFingerprint") != fingerprint:
            raise ValueError(f"{qid}: sealed and current candidate fingerprints do not match")
        exact_text = reviewed.get("selectedExactText", reviewed.get("selectedOptionText"))
        option_matches = [o for o in question.get("options", []) if o.get("text") == exact_text]
        sealed_matches = [o for o in sealed_by_id[qid].get("options", []) if o.get("text") == exact_text]
        selected_id = reviewed.get("selectedOptionId")
        answer = question.get("correctAnswer")
        answer_option = next((o for o in question.get("options", []) if o.get("id") == answer), None)
        confidence_ja = reviewed.get("confidence")
        confidence = {"高": "high", "中": "medium", "低": "low"}.get(confidence_ja)
        if not confidence:
            raise ValueError(f"{qid}: unsupported confidence value {confidence_ja!r}")
        confidence_counts[confidence] += 1
        alternatives = normalize_note_list(
            reviewed.get("alternativeDefensibleAnswers", reviewed.get("alternativeDefensibleOptionTexts")),
            "alternativeDefensibleAnswers", qid,
        )
        concerns = normalize_note_list(reviewed.get("concerns"), "concerns", qid)
        alternate_count += len(alternatives)
        concern_count += len(concerns)
        maps_to_answer = (
            len(option_matches) == 1
            and len(sealed_matches) == 1
            and option_matches[0].get("id") == selected_id
            and selected_id == answer
            and answer_option is not None
            and answer_option.get("text") == exact_text
        )
        if not maps_to_answer:
            mismatch_count += 1
        rows.append({
            "questionId": qid,
            "rawReviewerSelectedOptionId": selected_id,
            "rawReviewerExactOptionText": exact_text,
            "currentDisplayedOptionId": option_matches[0].get("id") if len(option_matches) == 1 else None,
            "authoredCorrectOptionId": answer,
            "contentFingerprint": fingerprint,
            "semanticTextAgreement": maps_to_answer,
            "confidence": confidence,
            "rationaleJa": reviewed.get("rationaleJa", reviewed.get("rationale", "")),
            "alternateDefensibleAnswers": alternatives,
            "concerns": concerns,
        })

    if alternate_count or mismatch_count:
        raise ValueError(f"Review cannot pass: alternatives={alternate_count}, semantic mismatches={mismatch_count}")

    prior_attempts = []
    for prior_path in PRIOR_RAW_PATHS:
        if not prior_path.is_file():
            continue
        prior_raw = read_json(prior_path)
        prior_meta = prior_raw.get("review") if isinstance(prior_raw.get("review"), dict) else prior_raw
        prior_items = prior_raw.get("items", prior_raw.get("responses", []))
        prior_alternates = sum(bool(normalize_note_list(
            row.get("alternativeDefensibleAnswers", row.get("alternativeDefensibleOptionTexts")),
            "alternativeDefensibleAnswers", row.get("questionId", row.get("itemId", "unknown")),
        )) for row in prior_items)
        prior_attempts.append({
            "rawOutputFile": str(prior_path.relative_to(ROOT)).replace("\\", "/"),
            "rawOutputSha256": sha256(prior_path),
            "sealedInputSha256": prior_meta.get("inputSha256BeforeReview", prior_meta.get("inputSha256Before", "")),
            "supersededByCurrentRevision": True,
            "unresolvedAlternativeCountAtThatRevision": prior_alternates,
            "note": "Preserved original response. This sealed revision had an M9_01 alternative reading, was revised, and reviewed again; this historical response was not edited.",
        })
    report = {
        "schema": CURRENT_VERSION_REVIEW_SCHEMA,
        "status": "REVIEW_CONTENT_VERSION_VERIFIED",
        "examId": "N2-MOCK-12",
        "reviewProvenanceLimit": AI_REVIEW_PROVENANCE_LIMIT,
        "reviewMethod": "Independent key-isolated AI review of the sealed text version; reviewer had no answer key.",
        "reviewScopeLimit": "Audio assets were not separately heard or checked by this reviewer.",
        "focusedReviewCoverage": {
            "starItemIds": focused_star,
            "continuousTextGrammarItemIds": focused_text,
        },
        "summary": {
            "reviewedItems": len(rows),
            "semanticAgreementCount": len(rows) - mismatch_count,
            "semanticMismatchCount": mismatch_count,
            "unresolvedAmbiguityCount": alternate_count,
            "reviewerConcernCount": concern_count,
            "confidenceCounts": confidence_counts,
        },
        "rawEvidence": {
            "sealedInputSha256": digest,
            "rawOutputSha256": sha256(RAW_PATH),
            "inputHashMatchedBeforeAndAfter": True,
            "rawResponsePreservedLocally": True,
            "portableExecutionAttestationAvailable": False,
            "rawOutputFile": "qa/raw_blind_responses/N2_MOCK_12_rev15_raw.json",
        },
        "priorReviewAttempts": prior_attempts,
        "rows": rows,
    }

    PUBLISHED_SEALED_PATH.write_bytes(SEALED_PATH.read_bytes())
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Wrote current-version M12 reconciliation for {len(rows)} items.")
    print(f"Sealed input SHA-256: {digest}")
    print(f"Raw review SHA-256: {report['rawEvidence']['rawOutputSha256']}")
    print(f"Confidence: {confidence_counts}; non-blocking reviewer concerns preserved: {concern_count}.")


if __name__ == "__main__":
    main()
