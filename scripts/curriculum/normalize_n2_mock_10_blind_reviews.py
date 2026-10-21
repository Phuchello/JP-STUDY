# -*- coding: utf-8 -*-
"""Normalize the isolated M10 blind reviewer output without consulting answer keys."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.curriculum.blind_review_exporter import validate_sealed_item_purity

QA = ROOT / "qa"
SEALED_PATH = QA / "blind_items_m10_final.json"
STAR_IDS = {f"N2_10_M8_{index:02d}" for index in range(1, 6)}
EXPECTED_ORDERS = {"".join(row) for row in itertools.permutations("ABCD")}
GROUP_FILES = {"s1_p1": "raw_blind_m10_s1_p1.json", "s1_p2": "raw_blind_m10_s1_p2.json", "s2": "raw_blind_m10_s2.json"}
INPUT_FILES = {"s1_p1": "blind_items_m10_s1_p1.json", "s1_p2": "blind_items_m10_s1_p2.json", "s2": "blind_items_m10_s2.json"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def order_code(value) -> str:
    if isinstance(value, list) and len(value) == 4:
        return "".join(str(part).strip().upper() for part in value)
    if isinstance(value, str):
        return "".join(part for part in value.strip().upper() if part in "ABCD")
    return ""


def option_map(item: dict) -> dict[str, str]:
    return {str(option["id"]).strip(): str(option["text"]).strip() for option in item.get("options", [])}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--response", required=True, type=Path, help="Path to the unmodified reviewer JSON retained outside the repository.")
    response_path = parser.parse_args().response.resolve()
    if not response_path.is_file():
        raise FileNotFoundError(response_path)

    sealed_hash = sha256(SEALED_PATH)
    response = load_json(response_path)
    input_meta = response.get("input", {}) if isinstance(response.get("input"), dict) else {}
    counts = response.get("counts", {}) if isinstance(response.get("counts"), dict) else {}
    verification = response.get("verification", {}) if isinstance(response.get("verification"), dict) else {}
    response_hash = response.get(
        "sealedInputSha256",
        response.get(
            "sourceSha256After",
            response.get(
                "sourceSha256Expected",
                response.get("inputSha256AfterReview", response.get("inputSha256", response.get("expectedInputSha256", input_meta.get("sha256AfterReview")))),
            ),
        ),
    )
    if input_meta:
        expected_matched = (
            input_meta.get("expectedSha256Match") is True
            and input_meta.get("sha256BeforeReview") == sealed_hash
            and input_meta.get("sha256AfterReview") == sealed_hash
        )
    else:
        expected_matched = response.get("expectedSha256Matched") is True or (
            response.get("sourceSha256Before") == sealed_hash
            and response.get("sourceSha256After", response.get("sourceSha256Expected")) == sealed_hash
        ) or (
            response.get("expectedInputSha256") == sealed_hash
            and response.get("inputSha256BeforeReview") == sealed_hash
            and response.get("inputSha256AfterReview") == sealed_hash
        ) or (
            response.get("inputSha256") == sealed_hash
            and verification.get("inputHashBefore") == sealed_hash
            and verification.get("inputHashAfter") == sealed_hash
        )
    if response_hash != sealed_hash or not expected_matched:
        raise ValueError("Reviewer response does not verify against the current sealed-input SHA-256.")
    item_count = int(response.get("itemCount", counts.get("sealedItemCount", counts.get("items", verification.get("answerCount", 0)))))
    unique_item_count = int(response.get("uniqueItemCount", counts.get("uniqueQuestionIdCount", counts.get("uniqueQuestionIds", verification.get("uniqueQuestionMappings", item_count)))))
    if item_count != 105 or unique_item_count != 105:
        raise ValueError("Reviewer response must cover all 105 sealed items.")
    if response.get("exactIdSetVerified") is False or response.get("selectedOptionTextMappingVerified") is False:
        raise ValueError("Reviewer response self-check reports an ID or exact option-text mapping failure.")
    if response.get("naturalOrMarginalAlternativeChangesStarAnswer") is True:
        raise ValueError("Reviewer response reports a natural or marginal alternate ★ answer.")
    if verification.get("exactOptionTextMatches") is False or verification.get("uniquePermutationsPerStarItem") is False:
        raise ValueError("Reviewer self-check reports an option-text or permutation-integrity failure.")

    sealed_rows = load_json(SEALED_PATH)
    if not isinstance(sealed_rows, list):
        raise ValueError("The sealed input must be a JSON list.")
    sealed_by_id = {}
    group_inputs = {name: [] for name in INPUT_FILES}
    for item in sealed_rows:
        validate_sealed_item_purity(item)
        qid = item.get("id")
        if not qid or qid in sealed_by_id:
            raise ValueError(f"Missing or duplicate sealed question ID: {qid}")
        sealed_by_id[qid] = item
        section = int(item.get("section", 0))
        if section == 1:
            group = "s1_p1" if len(group_inputs["s1_p1"]) < 38 else "s1_p2"
        elif section == 2:
            group = "s2"
        else:
            raise ValueError(f"Unexpected section for {qid}: {section}")
        group_inputs[group].append(item)
    if len(sealed_by_id) != 105 or [len(group_inputs[key]) for key in INPUT_FILES] != [38, 37, 30]:
        raise ValueError("Sealed input must contain 38 + 37 Section 1 items and 30 Section 2 items.")

    rows = response.get("responses", response.get("items", response.get("answers")))
    if not isinstance(rows, list):
        raise ValueError("Reviewer response must contain a responses array.")
    response_by_id = {}
    for row in rows:
        qid = row.get("id", row.get("questionId"))
        if not qid or qid in response_by_id:
            raise ValueError(f"Missing or duplicate response ID: {qid}")
        response_by_id[qid] = row
    if set(response_by_id) != set(sealed_by_id):
        raise ValueError(
            f"Reviewer response ID mismatch: missing={sorted(set(sealed_by_id)-set(response_by_id))}, "
            f"extra={sorted(set(response_by_id)-set(sealed_by_id))}"
        )

    self_check = response.get("selfCheck", {})
    self_counts = self_check.get("counts", {})
    mapping_check = self_check.get("exactOptionTextMapping")
    mapping_passed = self_check.get("selectedOptionIdAndTextMappingPassed") is True
    if isinstance(mapping_check, bool):
        mapping_passed = mapping_passed or mapping_check
    elif isinstance(mapping_check, dict):
        mapping_passed = mapping_passed or (
            int(mapping_check.get("matched", 0)) == 105 and not mapping_check.get("mismatches")
        )
    mapping_passed = mapping_passed or int(self_counts.get("exactOptionTextMappings", 0)) == 105
    mapping_passed = mapping_passed or self_check.get("answerOptionIdsAndTextsVerifiedAgainstSource") is True
    mapping_passed = mapping_passed or response.get("selectedOptionTextMappingVerified") is True
    mapping_passed = mapping_passed or (
        int(counts.get("selectedIdOptionTextMappingCount", 0)) == 105
        and int(counts.get("uniqueIdOptionMappingCount", 0)) == 105
    )
    mapping_passed = mapping_passed or int(counts.get("answerMappings", 0)) == 105
    mapping_passed = mapping_passed or (verification.get("exactOptionTextMatches") is True and int(verification.get("uniqueQuestionMappings", 0)) == 105)
    if not mapping_passed:
        raise ValueError("Reviewer self-check did not confirm exact option ID/text mappings.")
    response_count = self_check.get("responseCount", self_counts.get("responseItems", self_check.get("uniqueAnswerIds", counts.get("answerCount", counts.get("answerMappings", verification.get("answerCount", response.get("itemCount", 0)))))))
    unique_count = self_check.get("uniqueResponseIdCount", self_counts.get("uniqueResponseIds", self_check.get("uniqueAnswerIds", counts.get("uniqueIdOptionMappingCount", counts.get("answerMappings", verification.get("uniqueQuestionMappings", response.get("uniqueItemCount", 0)))))))
    if int(response_count) != 105 or int(unique_count) != 105:
        raise ValueError("Reviewer self-check does not confirm 105 unique answers.")
    missing_ids = self_check.get("missingIds", self_counts.get("missingIds", []))
    extra_ids = self_check.get("extraIds", self_counts.get("extraIds", []))
    duplicate_ids = self_check.get("duplicateIds", self_counts.get("duplicateIds", []))
    if missing_ids not in ([], 0, None) or extra_ids not in ([], 0, None) or duplicate_ids not in ([], 0, None):
        raise ValueError("Reviewer self-check reports missing, duplicate, or extra question IDs.")
    if response.get("exactIdSetVerified") is False:
        raise ValueError("Reviewer response self-check reports an incomplete or incorrect ID set.")

    grouped_reviews = {name: [] for name in GROUP_FILES}
    star_results = []
    unresolved_star_alternatives = []
    for group, input_items in group_inputs.items():
        for item in input_items:
            qid = item["id"]
            response_row = response_by_id[qid]
            selected = str(response_row.get("selectedOptionId", "")).strip().upper()
            selected_text = str(response_row.get("selectedOptionText", response_row.get("selectedText", response_row.get("exactOptionText", "")))).strip()
            options = option_map(item)
            if selected not in options or options[selected] != selected_text:
                raise ValueError(f"{qid}: reviewer answer ID/text does not exactly match the sealed options.")
            reason = str(response_row.get("reasonJa", response_row.get("rationaleJa", ""))).strip()
            if not reason:
                raise ValueError(f"{qid}: Japanese rationale is missing.")

            concerns = response_row.get("concerns", response_row.get("concern", response_row.get("ambiguityOrConcern")))
            if isinstance(concerns, list):
                concern_texts = [str(value).strip() for value in concerns if str(value).strip()]
            elif concerns:
                concern_texts = [str(concerns).strip()]
            else:
                concern_texts = []
            alternatives = []
            if qid in STAR_IDS:
                star = response_row.get("starPermutationReview")
                if not isinstance(star, dict):
                    permutation_audit = response.get("permutationAudit", {})
                    nested_stars = permutation_audit.get("items", []) if isinstance(permutation_audit, dict) else []
                    star_rows = [*response.get("starPermutationAudit", []), *response.get("starPermutationAudits", []), *nested_stars]
                    star = next((entry for entry in star_rows if entry.get("itemId", entry.get("id", entry.get("questionId"))) == qid), None)
                if not isinstance(star, dict) or int(star.get("starPosition", 3)) != 3:
                    if not isinstance(star, dict):
                        raise ValueError(f"{qid}: complete star-arrangement permutation review is required.")
                intended = order_code(star.get("intendedOrder", star.get("intendedPermutation", star.get("intendedOrderOptionIds", star.get("naturalOrder")))))
                intended_star = str(star.get("intendedStarOptionId", star.get("resultingStarOptionIdForNaturalOrder", ""))).strip().upper()
                if intended not in EXPECTED_ORDERS or intended[2] != selected:
                    raise ValueError(f"{qid}: selected answer does not match the independently solved third fragment.")
                if intended_star and intended_star != selected:
                    raise ValueError(f"{qid}: explicit intended star does not match the selected answer.")
                permutations = star.get("permutations")
                codes = [order_code(entry.get("order", entry.get("permutation", entry.get("orderOptionIds")))) for entry in permutations] if isinstance(permutations, list) else []
                if len(codes) != 24 or len(set(codes)) != 24 or set(codes) != EXPECTED_ORDERS:
                    raise ValueError(f"{qid} must have all 24 unique fragment permutations.")
                compact_permutations = []
                for entry, code in zip(permutations, codes):
                    star_id = str(entry.get("starOptionId", entry.get("resultingStarOptionId", ""))).strip().upper()
                    judgment = str(entry.get("classification", entry.get("grammaticalNaturalness", entry.get("naturalness", "")))).strip().lower()
                    if judgment == "intended":
                        judgment = "natural"
                    elif judgment in {"ungrammaticalorunnatural", "ungrammatical", "unnatural_or_incomplete"}:
                        judgment = "ungrammatical_or_incomplete"
                    elif judgment in {"文法的で自然", "文法的・自然", "自然"}:
                        judgment = "natural"
                    elif judgment in {"語順・係り受けが不自然", "不自然", "非文法的", "文法的でない"}:
                        judgment = "ungrammatical_or_incomplete"
                    if star_id != code[2] or judgment not in {"natural", "marginal", "ungrammatical_or_incomplete", "unnatural"}:
                        raise ValueError(f"{qid}: malformed permutation judgment for {code}.")
                    if "changesSelectedStar" in entry and entry.get("changesSelectedStar") is not (star_id != selected):
                        raise ValueError(f"{qid}: inconsistent changed-star flag for {code}.")
                    assembled_sentence = str(entry.get("assembledSentence", entry.get("reconstructedSentence", entry.get("assembledJapaneseSentence", entry.get("reconstructedJapanese", entry.get("sentence", "")))))).strip()
                    compact_permutations.append({
                        "order": code,
                        "starOptionId": star_id,
                        "classification": judgment,
                        "assembledSentence": assembled_sentence,
                    })
                    if judgment in {"natural", "marginal"} and star_id != selected:
                        alternate = {
                            "order": code,
                            "starOptionId": star_id,
                            "judgment": judgment,
                            "sentence": assembled_sentence,
                        }
                        unresolved_star_alternatives.append({"questionId": qid, **alternate})
                        alternatives.append({"optionId": star_id, **alternate})
                if not any(row["classification"] in {"natural", "marginal"} and row["starOptionId"] == selected for row in compact_permutations):
                    raise ValueError(f"{qid}: no natural/marginal permutation supports the selected answer.")
                star_results.append({
                    "questionId": qid,
                    "reviewedPermutationCount": 24,
                    "intendedOrder": intended,
                    "selectedOptionId": selected,
                    "naturalOrMarginalOrders": [row for row in compact_permutations if row["classification"] in {"natural", "marginal"}],
                    "allPermutationJudgments": compact_permutations,
                    "alternateChangesReviewedAnswer": any(row["starOptionId"] != selected and row["classification"] in {"natural", "marginal"} for row in compact_permutations),
                })
            grouped_reviews[group].append({
                "id": qid,
                "blindAnswer": selected,
                "selectedOptionText": selected_text,
            "linguisticJustification": reason,
                "confidence": str(response_row.get("confidence", "NOT_REPORTED")).strip().upper(),
                "alternativeDefensibleAnswers": alternatives,
                "concerns": concern_texts,
                "contentFingerprint": item["contentFingerprint"],
                "reviewerProvenance": "INDEPENDENT_AI_BLIND_REVIEW; EXACT_SEALED_INPUT_SHA_VERIFIED",
            })

    star_counts = self_check.get("starPermutationCounts", self_check.get("permutationCountsByItem", {}))
    if not star_counts and isinstance(self_check.get("permutationCounts"), list):
        star_counts = {
            row.get("id"): row.get("permutations", row.get("total"))
            for row in self_check["permutationCounts"] if isinstance(row, dict)
        }
    permutation_audit = response.get("permutationAudit", {})
    nested_stars = permutation_audit.get("items", []) if isinstance(permutation_audit, dict) else []
    top_star_rows = response.get("starPermutationAudit", response.get("starPermutationAudits", nested_stars))
    if not star_counts and isinstance(top_star_rows, list):
        star_counts = {
            row.get("itemId", row.get("id", row.get("questionId"))): len(row.get("permutations", []))
            for row in top_star_rows if isinstance(row, dict)
        }
    if set(star_counts) != STAR_IDS:
        raise ValueError("Reviewer self-check must confirm all five star-arrangement permutations.")
    if any(int(value) != 24 for value in star_counts.values()):
        raise ValueError("Reviewer self-check reports incomplete star-arrangement permutations.")
    total_permutations = response.get("starPermutationTotal", permutation_audit.get("totalPermutations") if isinstance(permutation_audit, dict) else counts.get("starPermutations", verification.get("permutationCount")))
    if total_permutations is None:
        total_permutations = counts.get("starPermutations", verification.get("permutationCount"))
    audit_count = response.get("starPermutationAuditCount", counts.get("starItemCount", counts.get("starItems", verification.get("starItemCount"))))
    if total_permutations not in (None, 120) or audit_count not in (None, 5):
        raise ValueError("Reviewer self-check reports incomplete aggregate star-arrangement coverage.")
    if self_check.get("allStarThirdsMatchSelectedOption") is False or self_check.get("allStarIntendedOrdersThirdLetterMatchSelectedOption") is False:
        raise ValueError("Reviewer self-check reports an intended ★ mismatch.")

    for group, filename in INPUT_FILES.items():
        (QA / filename).write_text(json.dumps(group_inputs[group], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for group, filename in GROUP_FILES.items():
        (QA / filename).write_text(json.dumps(grouped_reviews[group], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    reviewer_method = str(response.get("reviewMethod", response.get("review", "Independent AI review of sealed text/options"))).strip()
    reviewer_self_check = {key: self_check[key] for key in ("exactOptionTextMapping", "selectedOptionIdAndTextMappingPassed", "allStarThirdsMatchSelectedOption") if key in self_check}
    reviewer_self_check.update({
        key: verification[key]
        for key in ("answerCount", "uniqueQuestionMappings", "exactOptionTextMatches", "starItemCount", "permutationCount", "uniquePermutationsPerStarItem", "inputHashBefore", "inputHashAfter")
        if key in verification
    })
    provenance = {
        "examId": "N2-MOCK-10",
        "status": "REVIEW_RECONCILIATION_PENDING",
        "reviewerType": "Independent AI blind reviewer",
        "itemCount": len(sealed_by_id),
        "selectedAnswerCount": len(response_by_id),
        "exactOptionIdAndTextMappings": len(response_by_id),
        "sealedInputSha256": sealed_hash,
        "reviewerResponseSha256": sha256(response_path),
        "reviewerResponseRetainedOutsideRepository": True,
        "sealedInputPurityValidated": True,
        "reviewMethod": reviewer_method,
        "reviewerResponseSelfCheck": reviewer_self_check,
        "reviewerTaskScope": "Fresh independent reviewer was instructed to use only this exact sealed input and not consult answer keys, authored explanations, source, or previous QA. No external process audit is claimed.",
        "listeningReviewScope": "Transcript-based content review; separate browser receipt checks exact manifest hash, decode and playback progression, not pronunciation.",
        "limitations": [
            "AI-assisted review is not human/native-speaker review, official JLPT approval, or psychometric calibration.",
            "Original unmodified reviewer JSON is retained outside the repository; normalized records preserve the exact selections, text, rationale, concerns, and permutation judgments without the local file path.",
        ],
        "starPermutationAudits": sorted(star_results, key=lambda row: row["questionId"]),
        "unresolvedStarAlternativesChangingAnswer": unresolved_star_alternatives,
        "normalizedArtifactSha256": {filename: sha256(QA / filename) for filename in [*INPUT_FILES.values(), *GROUP_FILES.values()]},
        "normalizedCounts": {name: len(values) for name, values in grouped_reviews.items()},
    }
    (QA / "N2_MOCK_10_BLIND_REVIEW_PROVENANCE.json").write_text(
        json.dumps(provenance, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "status": provenance["status"], "sealedInputSha256": sealed_hash,
        "reviewerResponseSha256": provenance["reviewerResponseSha256"], "items": len(response_by_id),
        "starPermutations": sum(row["reviewedPermutationCount"] for row in star_results),
        "unresolvedStarAlternatives": len(unresolved_star_alternatives),
        "normalizedCounts": provenance["normalizedCounts"],
    }, ensure_ascii=False, indent=2))
    return 1 if unresolved_star_alternatives else 0


if __name__ == "__main__":
    raise SystemExit(main())
