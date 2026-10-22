# -*- coding: utf-8 -*-
"""Create a sanitized current-version reconciliation from immutable local M13 review evidence."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DRAFT = ROOT / "tmp/phase7/n2_mock_13_draft.json"
SEALED_LOCAL = ROOT / "tmp/phase7/blind_items_m13_rev10.json"
SEALED_PUBLIC = ROOT / "qa/blind_items_m13_final.json"
RAW = ROOT / "tmp/phase7/immutable_raw_responses/m13_rev10_105_blind_qa_raw.json"
OUT = ROOT / "qa/N2_MOCK_13_BLIND_RECONCILIATION.json"
PROVENANCE_LIMIT = (
    "AI blind-review artifacts have no portable execution attestation and do not constitute native-speaker certification."
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def confidence_band(value) -> str:
    try:
        score = float(value)
    except (TypeError, ValueError):
        return "low"
    return "high" if score >= 0.85 else "medium" if score >= 0.70 else "low"


def response_rows(raw: dict) -> list[dict]:
    rows = raw.get("responses")
    if not isinstance(rows, list):
        rows = raw.get("items")
    if not isinstance(rows, list):
        raise ValueError("Blind-review raw output has no responses/items array")
    return rows


def selected_option(response: dict) -> tuple[str, str]:
    selected = response.get("selected_option") or response.get("selectedOption") or {}
    if isinstance(selected, dict):
        return str(selected.get("id", "")), str(selected.get("text", ""))
    if isinstance(selected, str):
        return str(response.get("selected_option_id", response.get("selectedOptionId", ""))), selected
    return "", ""


def ambiguity_mentions(response: dict, options: list[dict], selected_text: str) -> list[str]:
    explicit = response.get("alternate_defensible_answers") or response.get("alternateDefensibleAnswers") or []
    if isinstance(explicit, str):
        explicit = [explicit]
    alternatives = [str(value) for value in explicit if str(value)]
    concern = str(response.get("concern") or response.get("concerns") or "")
    if isinstance(response.get("concerns"), list):
        concern = " ".join(str(value) for value in response["concerns"])
    if re.search(r"competing|alternative answer|alternate answer|ambiguous|ambiguity|multiple defensible|another defensible", concern, re.I):
        for option in options:
            text = str(option.get("text", ""))
            if text and text != selected_text and text in concern and text not in alternatives:
                alternatives.append(text)
        if not alternatives:
            alternatives.append("REVIEWER_FLAGGED_UNRESOLVED_AMBIGUITY")
    return alternatives


def main() -> int:
    for path in (DRAFT, SEALED_LOCAL, RAW):
        if not path.is_file():
            raise FileNotFoundError(f"Required local review input is missing: {path.relative_to(ROOT)}")
    raw = json.loads(RAW.read_text(encoding="utf-8"))
    sealed = json.loads(SEALED_LOCAL.read_text(encoding="utf-8"))
    exam = json.loads(DRAFT.read_text(encoding="utf-8"))
    sealed_hash = sha256(SEALED_LOCAL)
    before = raw.get("packet_sha256_before") or raw.get("sealedInputSha256") or raw.get("inputSha256Before")
    after = raw.get("packet_sha256_after") or raw.get("sealedInputSha256After") or raw.get("inputSha256After")
    if before != sealed_hash or after != sealed_hash:
        raise ValueError(f"Review packet hashes do not bind to the current sealed packet: before={before}, after={after}, local={sealed_hash}")

    questions = {q["id"]: q for section in exam["sections"] for q in section["items"]}
    sealed_by_id = {row["id"]: row for row in sealed}
    responses = response_rows(raw)
    response_by_id = {str(row.get("item_id") or row.get("questionId") or row.get("id") or ""): row for row in responses}
    if len(responses) != 105 or len(response_by_id) != 105 or set(response_by_id) != set(questions) or set(sealed_by_id) != set(questions):
        raise ValueError("Review must contain exactly one response for every current M13 question")

    rows = []
    mismatches = 0
    ambiguities = 0
    concern_count = 0
    confidence_counts = {"high": 0, "medium": 0, "low": 0}
    for qid, question in questions.items():
        response = response_by_id[qid]
        sealed_item = sealed_by_id[qid]
        raw_option_id, selected_text = selected_option(response)
        matching = [opt for opt in question.get("options", []) if opt.get("text") == selected_text]
        if len(matching) != 1:
            raise ValueError(f"{qid}: selected exact option text is missing or duplicated in the current item")
        current_option_id = matching[0]["id"]
        correct = next((opt for opt in question["options"] if opt.get("id") == question.get("correctAnswer")), None)
        semantic_agreement = bool(correct and correct.get("text") == selected_text)
        mismatches += not semantic_agreement
        concern_value = response.get("concern")
        concern_list = [str(concern_value)] if concern_value else []
        if isinstance(response.get("concerns"), list):
            concern_list = [str(value) for value in response["concerns"] if value]
        concern_count += bool(concern_list)
        alternatives = ambiguity_mentions(response, sealed_item.get("options", []), selected_text)
        ambiguities += bool(alternatives)
        band = confidence_band(response.get("confidence"))
        confidence_counts[band] += 1
        rows.append({
            "questionId": qid,
            "rawReviewerSelectedOptionId": raw_option_id,
            "rawReviewerExactOptionText": selected_text,
            "currentDisplayedOptionId": current_option_id,
            "authoredCorrectOptionId": question.get("correctAnswer"),
            "contentFingerprint": sealed_item.get("contentFingerprint"),
            "semanticTextAgreement": semantic_agreement,
            "confidence": band,
            "rationaleJa": str(response.get("rationale") or response.get("rationaleJa") or ""),
            "alternateDefensibleAnswers": alternatives,
            "concerns": concern_list,
        })

    playback_scope = str(raw.get("listening_assessment") or raw.get("reviewScopeLimit") or "Text-only review; audio playback was not assessed.")
    report = {
        "schema": "CURRENT_VERSION_TEXT_RECONCILIATION_V1",
        "status": "REVIEW_CONTENT_VERSION_VERIFIED" if mismatches == 0 and ambiguities == 0 else "QA_PENDING",
        "examId": "N2-MOCK-13",
        "reviewProvenanceLimit": PROVENANCE_LIMIT,
        "reviewMethod": "Independent key-isolated AI review of the sealed text version; reviewer had no answer key.",
        "reviewScopeLimit": playback_scope,
        "focusedReviewCoverage": {
            "starItemIds": [q["id"] for q in questions.values() if q.get("typeId") == "N2-GR-STAR"],
            "continuousTextGrammarItemIds": [q["id"] for q in questions.values() if q.get("typeId") == "N2-GR-PARA"],
        },
        "summary": {
            "reviewedItems": len(rows),
            "semanticAgreementCount": len(rows) - mismatches,
            "semanticMismatchCount": mismatches,
            "unresolvedAmbiguityCount": ambiguities,
            "reviewerConcernCount": concern_count,
            "confidenceCounts": confidence_counts,
        },
        "rawEvidence": {
            "sealedInputSha256": sealed_hash,
            "rawOutputSha256": sha256(RAW),
            "inputHashMatchedBeforeAndAfter": before == after == sealed_hash,
            "rawResponsePreservedLocally": True,
            "portableExecutionAttestationAvailable": False,
            "rawOutputFile": RAW.relative_to(ROOT).as_posix(),
            "privacyNote": "Immutable raw reviewer output stays in ignored local tmp; this public file contains a derived, version-bound reconciliation only.",
        },
        "rows": rows,
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    shutil.copyfile(SEALED_LOCAL, SEALED_PUBLIC)
    print(json.dumps({"status": report["status"], "reviewed": len(rows), "agreements": len(rows) - mismatches,
                      "mismatches": mismatches, "ambiguities": ambiguities, "concerns": concern_count,
                      "rawSha256": report["rawEvidence"]["rawOutputSha256"], "report": str(OUT)}, ensure_ascii=False))
    return 0 if report["status"] == "REVIEW_CONTENT_VERSION_VERIFIED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
