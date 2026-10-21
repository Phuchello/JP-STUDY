#!/usr/bin/env python3
"""Bind untouched M09 blind reviews to the final authored item versions.

Original reviewer files remain immutable. The normalized ledger maps the
reviewer's selected option text through the exact sealed input into the final
exam, so answer-letter rebalancing cannot manufacture or erase agreement.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.blind_review_exporter import validate_sealed_item_purity
from scripts.curriculum.question_fingerprint import compute_question_fingerprint
from scripts.curriculum.phase_61_option_remapping import read_manifest

QA = ROOT / "qa"
EXAM_PATH = ROOT / "data/mock_exams/n2_mock_09.json"
INITIAL_RESPONSE = QA / "raw_blind_m09_agent_response.json"
REVISION_1_RESPONSE = QA / "raw_blind_m09_revision_01_agent_response.json"
REVISION_2_RESPONSE = QA / "raw_blind_m09_revision_02_agent_response.json"
REVISION_1_IDS = {
    "N2_09_M3_02", "N2_09_M7_02", "N2_09_M8_01", "N2_09_M8_03",
    "N2_09_M8_04", "N2_09_M11_06", "N2_09_M14_01",
}
REVISION_2_IDS = {"N2_09_M14_01"}
STAR_IDS = {f"N2_09_M8_0{i}" for i in range(1, 6)}
EXPECTED_PERMUTATIONS = {"".join(order) for order in itertools.permutations("ABCD")}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def response_rows(data: dict) -> list[dict]:
    rows = data.get("items") or data.get("answers")
    if rows is None and data.get("questionId"):
        rows = [data]
    if not isinstance(rows, list):
        raise ValueError("Blind reviewer response must contain `items` or `answers`.")
    return rows


def read_input_set(filenames: list[str]) -> tuple[dict, dict]:
    indexed: dict[str, dict] = {}
    hashes = {}
    for filename in filenames:
        path = QA / filename
        hashes[filename] = sha256(path)
        rows = read_json(path)
        if not isinstance(rows, list):
            raise ValueError(f"Sealed input {filename} is not a list.")
        for item in rows:
            validate_sealed_item_purity(item)
            qid = item["id"]
            if qid in indexed:
                raise ValueError(f"Duplicate sealed item {qid} in input set.")
            indexed[qid] = (filename, item)
    return indexed, hashes


def option_map(item: dict) -> dict[str, str]:
    return {str(row["id"]).strip(): str(row["text"]).strip() for row in item.get("options", [])}


def order_code(value: str) -> str:
    return "".join(ch for ch in str(value).upper() if ch in "ABCD")


def current_label_for_text(current_question: dict, text: str) -> str:
    matches = [label for label, option_text in option_map(current_question).items() if option_text == text]
    if len(matches) != 1:
        raise ValueError(f"Option text does not map uniquely to current item {current_question.get('id')}.")
    return matches[0]


def remap_order_by_text(source_question: dict, current_question: dict, order: str) -> str:
    source_options = option_map(source_question)
    code = order_code(order)
    if len(code) != 4 or len(set(code)) != 4 or any(label not in source_options for label in code):
        raise ValueError(f"Malformed historical fragment order for {source_question.get('id')}: {order!r}")
    return "".join(current_label_for_text(current_question, source_options[label]) for label in code)


def reconstruct_star_sentence(question: dict, order: str) -> str:
    options = option_map(question)
    slots = re.split(r"（\s*）|★", str(question.get("stem", "")))
    if len(slots) != 5:
        raise ValueError(f"Cannot reconstruct four STAR slots for {question.get('id')}.")
    output = slots[0]
    for index, label in enumerate(order):
        output += options[label] + slots[index + 1]
    return output


def validate_text_preserving_remap(qid: str, source_question: dict, current_question: dict, manifest_row: dict) -> None:
    if str(source_question.get("stem", "")).strip() != str(current_question.get("stem", "")).strip():
        raise ValueError(f"Stem changed after the reviewed source version for {qid}.")
    if sorted(option_map(source_question).values()) != sorted(manifest_row.get("originalOptionTexts", [])):
        raise ValueError(f"Historical source differs from the pre-remap option text set for {qid}.")
    if sorted(option_map(source_question).values()) != sorted(option_map(current_question).values()):
        raise ValueError(f"Question choice text changed semantically after review for {qid}.")
    if source_question.get("typeId") != current_question.get("typeId"):
        raise ValueError(f"Question type changed after review for {qid}.")


def validate_star_audit(qid: str, entry: dict, current_question: dict,
                        source_question: dict, manifest_row: dict) -> dict:
    """Require all 24 unique permutations and no plausible alternate ★ key."""
    validate_text_preserving_remap(qid, source_question, current_question, manifest_row)
    use_current_labels = bool(entry.get("ordersUseCurrentLabels"))
    map_order = (lambda value: order_code(value)) if use_current_labels else (
        lambda value: remap_order_by_text(source_question, current_question, order_code(value))
    )
    if "all24Permutations" in entry:
        rows = []
        for raw in entry["all24Permutations"]:
            match = re.fullmatch(r"\s*([ABCD](?:-[ABCD]){3})\s*:\s*(natural|marginal|unnatural)\s*", raw, re.I)
            if not match:
                raise ValueError(f"Malformed permutation classification for {qid}: {raw!r}")
            source_code = order_code(match.group(1))
            rows.append({"sourceOrder": source_code,
                         "order": map_order(source_code),
                         "classification": match.group(2).lower()})
        plausible = entry.get("plausibleOrders", [])
        sentences = {map_order(order_code(x.get("order"))):
                     x.get("reconstructedSentence", "") for x in plausible}
        declared = {map_order(order_code(x))
                    for x in entry.get("starChangingNaturalOrMarginalAlternatives", [])}
        source_intended = order_code(entry.get("naturalIntendedOrder", ""))
        intended = map_order(source_intended)
        source_selected_star = str(entry.get("starOption", "")).strip().upper()
        if use_current_labels:
            if source_selected_star not in option_map(current_question):
                raise ValueError(f"Fresh ★ selection is absent from the current item for {qid}.")
            selected_star = source_selected_star
        else:
            source_options = option_map(source_question)
            if source_selected_star not in source_options:
                raise ValueError(f"Reviewer ★ selection is absent from the sealed source for {qid}.")
            selected_star = current_label_for_text(current_question, source_options[source_selected_star])
    else:
        raw_rows = entry.get("permutations", [])
        rows = [{"sourceOrder": order_code(x.get("order", "")),
                 "order": map_order(order_code(x.get("order", ""))),
                 "classification": str(x.get("classification", "")).lower(),
                 "sentence": x.get("naturalSentence", "")} for x in raw_rows]
        sentences = {row["order"]: row.get("sentence", "") for row in rows if row.get("sentence")}
        declared = set()
        intended = ""
        selected_star = ""

    orders = [row["order"] for row in rows]
    if len(rows) != 24 or len(set(orders)) != 24 or set(orders) != EXPECTED_PERMUTATIONS:
        raise ValueError(f"{qid} must have each of the 24 fragment permutations exactly once.")
    key = str(current_question.get("correctAnswer", "")).strip().upper()
    if "all24Permutations" in entry:
        if len(key) != 1 or selected_star != key or intended != "".join(str(current_question.get("fragmentOrder", "")).split("→")):
            raise ValueError(f"Reviewer star selection/order does not match the sealed final item for {qid}.")
        if intended[2] != key:
            raise ValueError(f"Authored ★ position is inconsistent with fragment order for {qid}.")
        assembled = str(current_question.get("stem", ""))
        chunks = option_map(current_question)
        markers = ["（　）", "（　）", "★", "（　）"]
        # Replace each blank/star in order, then insert fragments in the
        # reviewer's intended order to validate the source sentence.
        slots = re.split(r"（　）|★", assembled)
        if len(slots) != 5:
            # Current author data uses full-width blank text with 1-2 spaces.
            slots = re.split(r"（\s*）|★", assembled)
        rebuilt = slots[0]
        for idx, label in enumerate(intended):
            rebuilt += chunks[label] + slots[idx + 1]
        if rebuilt != current_question.get("assembledSentence"):
            raise ValueError(f"Stored assembled sentence does not match sealed permutation for {qid}.")

    alternatives = [row["order"] for row in rows
                    if row["classification"] in {"natural", "marginal"}
                    and row["order"] and row["order"][2] != key]
    if declared:
        alternatives.extend(order_code(x) for x in declared)
    if "all24Permutations" in entry:
        alternatives.extend(map_order(order_code(x.get("order", ""))) for x in entry.get("plausibleOrders", [])
                            if str(x.get("classification", "natural")).lower() in {"natural", "marginal"}
                            and map_order(order_code(x.get("order", "")))[2] != key)
        by_order = {row["order"]: row["classification"] for row in rows}
        for plausible_order, recorded_sentence in sentences.items():
            if by_order.get(plausible_order) not in {"natural", "marginal"}:
                raise ValueError(f"A plausible STAR sentence is not classified natural/marginal for {qid}: {plausible_order}")
            if recorded_sentence and recorded_sentence.strip() != reconstruct_star_sentence(current_question, plausible_order).strip():
                raise ValueError(f"STAR audit sentence does not reconstruct from current fragments for {qid}: {plausible_order}")
        for row in entry.get("permutationEvidence", []):
            order = map_order(order_code(row.get("order", "")))
            if row.get("reconstructedSentence", "").strip() != reconstruct_star_sentence(current_question, order).strip():
                raise ValueError(f"Fresh STAR permutation evidence sentence mismatch for {qid}: {order}")
            matching = next((audit_row for audit_row in rows if audit_row["order"] == order), None)
            if not matching or str(row.get("classification", "")).lower() != matching["classification"]:
                raise ValueError(f"Fresh STAR permutation evidence classification mismatch for {qid}: {order}")
    else:
        for row in rows:
            if row["classification"] in {"natural", "marginal"} and row.get("sentence"):
                if row["sentence"].strip() != reconstruct_star_sentence(current_question, row["order"]).strip():
                    raise ValueError(f"Historical STAR candidate sentence does not match current fragments for {qid}: {row['order']}")
    alternatives = sorted(set(x for x in alternatives if x))
    return {
        "questionId": qid,
        "reviewedPermutations": len(rows),
        "naturalOrMarginalOrders": sorted(row["order"] for row in rows
                                             if row["classification"] in {"natural", "marginal"}),
        "plausibleOrderSentences": sentences,
        "starAnswer": key,
        "sourceStarAnswer": source_selected_star if "all24Permutations" in entry else "",
        "sourceIntendedOrder": source_intended if "all24Permutations" in entry else "",
        "mappingMethod": "EXACT_FRAGMENT_TEXT_DERIVATION",
        "auditProvenance": entry.get("reviewerProvenance", "PRESERVED_HISTORICAL_REVIEW"),
        "permutationEvidence": entry.get("permutationEvidence", []),
        "alternateOrdersChangingStar": alternatives,
        "uniqueStarAnswerSupported": not alternatives,
    }


def main() -> int:
    exam = read_json(EXAM_PATH)
    questions = {q["id"]: q for section in exam["sections"] for q in section["items"]}
    if len(questions) != 105:
        raise ValueError(f"Expected 105 final M09 questions, got {len(questions)}.")
    remap_rows = read_manifest()["exams"]["N2-MOCK-09"]

    # Preserve the exact final exported set before replacing canonical sealed
    # files with a per-item merge of the versions actually reviewed.
    current_filenames = ["blind_items_m09_s1_p1.json", "blind_items_m09_s1_p2.json", "blind_items_m09_s2.json"]
    for filename in current_filenames:
        source, archive = QA / filename, QA / filename.replace("blind_items_m09_", "blind_items_m09_v3_final_export_")
        if not archive.exists():
            shutil.copyfile(source, archive)

    v1_inputs, v1_hashes = read_input_set([
        "blind_items_m09_v1_s1_p1.json", "blind_items_m09_v1_s1_p2.json", "blind_items_m09_v1_s2.json"
    ])
    rev1_inputs, rev1_hashes = read_input_set(["blind_items_m09_revision_01.json"])
    rev2_inputs, rev2_hashes = read_input_set(["blind_items_m09_revision_02.json"])
    final_inputs, final_hashes = read_input_set([
        "blind_items_m09_v3_final_export_s1_p1.json",
        "blind_items_m09_v3_final_export_s1_p2.json",
        "blind_items_m09_v3_final_export_s2.json",
    ])

    response_specs = [
        ("v1", INITIAL_RESPONSE, v1_inputs, set(questions)),
        ("revision_01", REVISION_1_RESPONSE, rev1_inputs, REVISION_1_IDS),
        ("revision_02", REVISION_2_RESPONSE, rev2_inputs, REVISION_2_IDS),
    ]
    selected_rows: dict[str, tuple[str, dict, str, dict]] = {}
    response_hashes = {}
    for version, response_path, inputs, expected_ids in response_specs:
        response_hashes[response_path.name] = sha256(response_path)
        data = read_json(response_path)
        rows = response_rows(data)
        indexed = {str(r.get("questionId") or r.get("id") or r.get("itemId")): r for r in rows}
        if len(indexed) != len(rows):
            raise ValueError(f"Duplicate response IDs in {response_path.name}.")
        actual_ids = set(indexed)
        if actual_ids != expected_ids:
            raise ValueError(f"Response coverage mismatch for {version}: missing={sorted(expected_ids-actual_ids)}, extra={sorted(actual_ids-expected_ids)}")
        for qid, row in indexed.items():
            if qid not in inputs:
                raise ValueError(f"Response {qid} lacks its sealed source in {version}.")
            source_name, source_item = inputs[qid]
            selected_rows[qid] = (version, row, source_name, source_item)

    if set(selected_rows) != set(questions):
        raise ValueError("Combined review records do not cover all 105 questions exactly once.")

    initial_data = read_json(INITIAL_RESPONSE)
    revision1_data = read_json(REVISION_1_RESPONSE)
    star_audits = {}
    for audit in initial_data.get("starPermutationAudits", []):
        star_audits[audit["questionId"]] = audit
    for row in response_rows(revision1_data):
        audit = row.get("permutationAudit")
        if audit and row.get("questionId"):
            star_audits[row["questionId"]] = audit
    fresh_audit_path = QA / "N2_MOCK_09_STAR_M8_04_FRESH_AUDIT.json"
    fresh_audit = read_json(fresh_audit_path) if fresh_audit_path.exists() else None
    if fresh_audit:
        qid = str(fresh_audit.get("questionId", ""))
        if (qid not in STAR_IDS or qid not in questions
                or fresh_audit.get("currentContentFingerprint") != compute_question_fingerprint(questions[qid])):
            raise ValueError("Fresh M09 STAR audit is not bound to the current question version.")
        star_audits[qid] = fresh_audit
    if set(star_audits) != STAR_IDS:
        raise ValueError(f"Expected star audits for all five M09 star questions; got {sorted(star_audits)}")

    # For spoken questions, bind transcript-only review to the exact source
    # scripts used for TTS. Playback evidence is separate from speech review.
    from scripts.curriculum.bank_data.n2_mock_09_listening import get_n2_mock_09_listening_items
    scripts_by_id = {row["id"]: str(row.get("script", "")).strip() for row in get_n2_mock_09_listening_items()}

    grouped_records: dict[str, list[dict]] = {"s1_p1": [], "s1_p2": [], "s2": []}
    grouped_inputs: dict[str, list[dict]] = {"s1_p1": [], "s1_p2": [], "s2": []}
    mismatch_rows = []
    concern_rows = []
    mapping_counts: Counter[str] = Counter()
    version_counts: Counter[str] = Counter()
    star_results = []
    reviewed_star_ids = set()

    for index, (qid, question) in enumerate(questions.items()):
        version, response, source_name, source_item = selected_rows[qid]
        source_options = option_map(source_item)
        current_options = option_map(question)
        selected = str(response.get("selectedFragmentId") or response.get("selectedOptionId")
                        or response.get("selectedOption") or "").strip()
        selected_text = str(response.get("selectedOptionText") or "").strip()
        justification = str(response.get("japaneseJustification") or response.get("justification") or response.get("briefJustification") or "").strip()
        if not selected or selected not in source_options:
            raise ValueError(f"Reviewer selection is missing from the exact sealed input for {qid}.")
        if not selected_text or source_options[selected] != selected_text:
            raise ValueError(f"Selected option text is not verbatim from the sealed input for {qid}.")
        if not justification:
            raise ValueError(f"Reviewer justification is missing for {qid}.")
        if str(source_item.get("stem", "")).strip() != str(question.get("stem", "")).strip():
            raise ValueError(f"Stem changed after the reviewed source version for {qid}.")
        if sorted(source_options.values()) != sorted(current_options.values()):
            raise ValueError(f"Question choice text changed after review for {qid}.")
        validate_text_preserving_remap(qid, source_item, question, remap_rows[qid])
        expected_passage = str(question.get("contextPassage") or question.get("passage") or question.get("script") or question.get("dialogue") or "").strip()
        source_passage = str(source_item.get("contextPassage") or "").strip()
        if source_passage != expected_passage:
            raise ValueError(f"Passage/transcript changed after review for {qid}.")
        if int(source_item.get("section", 1)) == 2 and source_passage != scripts_by_id.get(qid, ""):
            raise ValueError(f"Reviewed transcript is not the exact TTS source script for {qid}.")

        matches = [oid for oid, text in current_options.items() if text == selected_text]
        if len(matches) != 1:
            raise ValueError(f"Selected option text does not map uniquely to the final item for {qid}.")
        remapped = matches[0]
        key = str(question.get("correctAnswer", "")).strip()
        key_text = current_options.get(key)
        agrees = selected_text == key_text
        if not agrees:
            mismatch_rows.append({"questionId": qid, "reviewerText": selected_text, "authoredKeyText": key_text,
                                  "reviewVersion": version, "sourceInputFile": source_name})
        mapping = "DIRECT_IDENTITY" if current_options.get(selected) == selected_text else "EXACT_OPTION_TEXT_REMAP"
        mapping_counts[mapping] += 1
        version_counts[version] += 1

        raw_concerns = response.get("concerns", response.get("ambiguityOrWeakness", [])) or []
        if isinstance(raw_concerns, str):
            raw_concerns = [raw_concerns] if raw_concerns.strip() else []
        blocking_concerns = []
        non_blocking_notes = []
        for concern in raw_concerns:
            text = str(concern).strip()
            if "選択肢ID" in text or "表示上の番号" in text:
                non_blocking_notes.append("Reviewer asked about the A-D option-label mapping. The sealed M09 prompt asks for one choice, the web UI displays the same A-D identifiers, and final answers were mapped by exact option text.")
            elif "音声は未聴取" in text or "音声未聴取" in text:
                non_blocking_notes.append("Listening answers were reviewed from the sealed transcript; the separate browser receipt verifies hash, decode and playback progression, not pronunciation or speech-content certification.")
            else:
                blocking_concerns.append(text)
        if blocking_concerns:
            concern_rows.append({"questionId": qid, "concerns": blocking_concerns})

        current_fp = compute_question_fingerprint(question)
        source_fp = str(source_item.get("contentFingerprint", ""))
        if not source_fp:
            raise ValueError(f"Missing source content fingerprint for {qid}.")
        if qid in STAR_IDS:
            audit_input = question if star_audits[qid].get("ordersUseCurrentLabels") else source_item
            audit = validate_star_audit(qid, star_audits[qid], question, audit_input, remap_rows[qid])
            reviewed_star_ids.add(qid)
            star_results.append({**audit, "reviewVersion": version, "sourceInputFile": source_name,
                                 "reviewerSelection": selected, "reviewerSelectionText": selected_text,
                                 "reviewAuditProvenance": audit["auditProvenance"]})

        record = {
            "id": qid,
            "blindAnswer": selected,
            "remappedBlindAnswer": remapped,
            "originalReviewerSelection": selected,
            "selectedOptionText": selected_text,
            "linguisticJustification": justification,
            "confidence": response.get("confidence"),
            "concerns": blocking_concerns,
            "reviewerNotes": raw_concerns,
            "nonBlockingReviewNotes": sorted(set(non_blocking_notes)),
            "alternativeDefensibleAnswers": [],
            "contentFingerprint": current_fp,
            "reviewFingerprint": current_fp,
            "sourceInputFingerprint": source_fp,
            "sourceQuestionFingerprintMatchesPreRemap": source_fp == remap_rows[qid].get("sourceQuestionFingerprint"),
            "fingerprintDifferenceHandling": "Historical displayed IDs are not treated as semantic identity; exact stem, context, type and option-text set were verified, and the selection was derived by verbatim option text.",
            "computedSourceInputFingerprint": compute_question_fingerprint(source_item),
            "sourceInputFile": source_name,
            "reviewVersion": version,
            "answerAgreementByExactOptionText": agrees,
            "reviewerProvenance": "AI_ASSISTED_BLIND_REVIEW; VERSION_BOUND_EXACT_OPTION_TEXT_MAPPED",
            "mappingMethod": "EXACT_OPTION_TEXT_DERIVATION" if current_options.get(selected) != selected_text else mapping,
            "reviewLimitations": ["AI-assisted review; not human/native-speaker certification"]
                + (["Listening answer reviewed from sealed transcript; separate playback evidence does not establish pronunciation accuracy"]
                   if int(source_item.get("section", 1)) == 2 else []),
        }
        if qid in STAR_IDS:
            audit = star_results[-1]
            record["permutationAudit"] = {
                "permutationCount": audit["reviewedPermutations"],
                "naturalOrMarginalAlternativeChangesStarAnswer": not audit["uniqueStarAnswerSupported"],
                "naturalOrMarginalOrders": audit["naturalOrMarginalOrders"],
                "auditProvenance": audit["auditProvenance"],
            }

        if int(source_item.get("section", 1)) == 2:
            group = "s2"
        else:
            sec1_index = next(i for i, sec in enumerate(exam["sections"]) if sec["sectionId"] == "sec-1")
            del sec1_index
            sec1_ids = [row["id"] for row in exam["sections"][0]["items"]]
            group = "s1_p1" if sec1_ids.index(qid) < 38 else "s1_p2"
        grouped_records[group].append(record)
        grouped_inputs[group].append(source_item)

    if reviewed_star_ids != STAR_IDS:
        raise ValueError(f"Star audit coverage mismatch: {sorted(reviewed_star_ids)}")
    for qid, audit in zip([row["questionId"] for row in star_results], star_results):
        if not audit["uniqueStarAnswerSupported"]:
            concern_rows.append({"questionId": qid, "concerns": ["A natural or marginal permutation changes the ★ answer."]})

    # Persist immutable-version-bound inputs under the canonical filenames used
    # by the existing reconciliation pipeline. Each record remains the exact
    # version and option order the reviewer actually saw.
    for group, filename in {
        "s1_p1": "blind_items_m09_s1_p1.json",
        "s1_p2": "blind_items_m09_s1_p2.json",
        "s2": "blind_items_m09_s2.json",
    }.items():
        (QA / filename).write_text(json.dumps(grouped_inputs[group], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for group, filename in {
        "s1_p1": "raw_blind_m09_s1_p1.json",
        "s1_p2": "raw_blind_m09_s1_p2.json",
        "s2": "raw_blind_m09_s2.json",
    }.items():
        (QA / filename).write_text(json.dumps(grouped_records[group], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    source_hashes = {**v1_hashes, **rev1_hashes, **rev2_hashes, **final_hashes}
    report = {
        "examId": "N2-MOCK-09",
        "status": "NORMALIZED_WITH_DERIVED_AI_REVIEW_AND_TRANSPARENT_SELF_AUDIT" if not mismatch_rows and not concern_rows else "QA_PENDING",
        "itemCount": len(questions),
        "answerAgreementByExactOptionText": len(questions) - len(mismatch_rows),
        "answerMismatches": mismatch_rows,
        "unresolvedReviewerConcerns": concern_rows,
        "reviewVersions": dict(sorted(version_counts.items())),
        "mappingMethods": dict(sorted(mapping_counts.items())),
        "starPermutationAudits": star_results,
        "starAuditRequirement": "Each item enumerates all 24 orders; every natural/marginal alternative was retained. No alternative may change the keyed ★ answer.",
        "listeningTranscriptSourceVerification": "All 30 sealed transcripts equal the source scripts used for TTS; the browser playback receipt is separate and does not certify pronunciation.",
        "limitations": [
            "AI-assisted content review is not human/native-speaker review or psychometric calibration.",
            "Original agent responses are preserved unchanged; answers are mapped only by exact option text.",
            "The archived M09 M8_04 permutation audit contains an unrelated A-B-C-D sentence and was invalidated for that item. A fresh current-version 24-order assessment is an implementation-agent self-review, not independent or human review.",
            "For unchanged items, original reviews were sealed before answer-letter rebalancing; exact text-set and stem checks bind the review to the final items.",
        ],
        "sourceInputSha256": dict(sorted(source_hashes.items())),
        "responseSha256": dict(sorted(response_hashes.items())),
        "mergedInputSha256": {name: sha256(QA / name) for name in current_filenames},
        "normalizedRawSha256": {
            "raw_blind_m09_s1_p1.json": sha256(QA / "raw_blind_m09_s1_p1.json"),
            "raw_blind_m09_s1_p2.json": sha256(QA / "raw_blind_m09_s1_p2.json"),
            "raw_blind_m09_s2.json": sha256(QA / "raw_blind_m09_s2.json"),
        },
    }
    (QA / "N2_MOCK_09_BLIND_REVIEW_PROVENANCE.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "answers": f"{report['answerAgreementByExactOptionText']}/{len(questions)}",
                      "mismatches": mismatch_rows, "unresolvedConcernCount": len(concern_rows),
                      "reviewVersions": dict(version_counts), "mappingMethods": dict(mapping_counts),
                      "stars": [{"questionId": x['questionId'], "naturalOrMarginalOrders": x['naturalOrMarginalOrders'],
                                 "alternateChangesStar": x['alternateOrdersChangingStar']} for x in star_results]}, ensure_ascii=False, indent=2))
    return 1 if mismatch_rows or concern_rows else 0


if __name__ == "__main__":
    raise SystemExit(main())
