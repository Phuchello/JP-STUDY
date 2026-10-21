#!/usr/bin/env python3
"""Bind untouched M08 blind-review responses to the final authored versions.

The original agent responses are preserved verbatim. This script derives a
separate normalized ledger by mapping each reviewed answer through the exact
option text supplied in that review's sealed input. It fails closed on missing
items, duplicate mappings, fingerprint/source mismatches, and answer changes.
"""
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.question_fingerprint import compute_question_fingerprint


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def item_list(data):
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get("items"), list):
        return data["items"]
    raise ValueError("Sealed review input must be an item list")


def index_items(path: Path) -> dict:
    items = item_list(read_json(path))
    indexed = {item["id"]: item for item in items}
    if len(indexed) != len(items):
        raise ValueError(f"Duplicate question ID in {path.name}")
    return indexed


def response_items(path: Path) -> list[dict]:
    data = read_json(path)
    if isinstance(data, dict) and isinstance(data.get("items"), list):
        return data["items"]
    if isinstance(data, dict) and isinstance(data.get("answers"), list):
        return data["answers"]
    if isinstance(data, dict) and data.get("itemId"):
        return [data]
    raise ValueError(f"Unrecognized blind response schema: {path.name}")


def option_map(item: dict) -> dict[str, str]:
    return {str(option["id"]): str(option["text"]).strip() for option in item.get("options", [])}


NON_BLOCKING_REVIEW_NOTES = {
    "N2_08_M6_01": "Distractors are grammatically framed but less plausible than the key, which may make the target conspicuous.",
    "N2_08_M6_02": "Distractors use sensory qualities with 妥当 and may make the target conspicuous.",
    "N2_08_M6_05": "Two distractors have odd agent/object relations and may make the item easier than intended.",
    "N2_08_M4_L03": "Immediate-response answer relies on conversational response fit; no separate factual evidence about the device power policy is stated.",
    "N2_08_M8_01": "The answer number assumes the listed fragment labels A-D; this is a format clarification, not an alternative natural ordering.",
}


def main() -> None:
    qa = ROOT / "qa"
    exam = read_json(ROOT / "data/mock_exams/n2_mock_08.json")
    questions = {
        question["id"]: question
        for section in exam["sections"]
        for question in section["items"]
    }
    section_by_id = {
        question["id"]: int(section.get("sectionId", "sec-1").split("-")[-1])
        for section in exam["sections"]
        for question in section["items"]
    }
    if len(questions) != 105:
        raise ValueError(f"Expected 105 final exam items, got {len(questions)}")

    versions = [
        ("v1", "raw_blind_m08_agent_response.json", [
            "blind_items_m08_s1_p1.json", "blind_items_m08_s1_p2.json", "blind_items_m08_s2.json"
        ]),
        ("v2", "raw_blind_m08_revision_v2_agent_response.json", ["blind_items_m08_revision_v2.json"]),
        ("v3", "raw_blind_m08_revision_v3_agent_response.json", ["blind_items_m08_revision_v3.json"]),
        ("v4", "raw_blind_m08_revision_v4_agent_response.json", ["blind_items_m08_revision_v4.json"]),
    ]

    source_inputs: dict[str, tuple[str, dict]] = {}
    source_hashes: dict[str, str] = {}
    reviews: dict[str, tuple[str, dict, dict]] = {}
    review_hashes: dict[str, str] = {}
    for version, response_name, input_names in versions:
        response_path = qa / response_name
        response_data = read_json(response_path)
        response_hashes_for_scope = {response_name: sha256(response_path)}
        review_hashes.update(response_hashes_for_scope)
        indexed_inputs: dict[str, tuple[str, dict]] = {}
        for input_name in input_names:
            input_path = qa / input_name
            if version == "v1":
                archived = qa / input_name.replace("blind_items_m08_", "blind_items_m08_v1_")
                if archived.exists():
                    input_path = archived
            source_hashes[input_name] = sha256(input_path)
            for qid, item in index_items(input_path).items():
                if qid in indexed_inputs:
                    raise ValueError(f"Duplicate sealed input {qid} in {version}")
                indexed_inputs[qid] = (input_name, item)

        seen_in_version: set[str] = set()
        for response in response_items(response_path):
            qid = response.get("questionId") or response.get("itemId")
            if not qid or qid not in indexed_inputs:
                raise ValueError(f"Response without matching sealed input in {version}: {qid}")
            if qid in seen_in_version:
                raise ValueError(f"Duplicate response within {version}: {qid}")
            seen_in_version.add(qid)
            input_name, input_item = indexed_inputs[qid]
            # Later, specifically sealed revision passes supersede earlier
            # responses for that same item. The raw prior responses stay intact.
            reviews[qid] = (version, response, input_item)
            source_inputs[qid] = (input_name, input_item)

    if set(reviews) != set(questions):
        missing = sorted(set(questions) - set(reviews))
        extra = sorted(set(reviews) - set(questions))
        raise ValueError(f"Blind coverage mismatch; missing={missing}, extra={extra}")

    # Prove that the review transcript for affected audio items is the exact
    # text source used to create the generated Japanese speech.
    from scripts.curriculum.bank_data.n2_mock_08_listening import get_n2_mock_08_listening_items

    listening_sources = {item["id"]: item["script"] for item in get_n2_mock_08_listening_items()}
    records_by_section: dict[str, list[dict]] = {"s1_p1": [], "s1_p2": [], "s2": []}
    inputs_by_section: dict[str, list[dict]] = {"s1_p1": [], "s1_p2": [], "s2": []}
    mapping_counts: Counter[str] = Counter()
    version_counts: Counter[str] = Counter()
    transcript_bound_ids: list[str] = []
    raw_selection_map: dict[str, str] = {}

    for qid, question in questions.items():
        version, response, input_item = reviews[qid]
        source_name, _ = source_inputs[qid]
        source_options = option_map(input_item)
        selected = str(response.get("selectedFragmentId") or response.get("selectedOption") or "").strip()
        if version == "v4" and not response.get("selectedFragmentId"):
            raise ValueError("v4 star review must identify the selected fragment explicitly")
        if selected not in source_options:
            raise ValueError(f"Reviewer selection {selected!r} is absent from {source_name} for {qid}")
        selected_text = source_options[selected]
        matching = [option for option in question.get("options", []) if str(option.get("text", "")).strip() == selected_text]
        if len(matching) != 1:
            raise ValueError(f"Could not map the selected text uniquely into the final item {qid}")

        final_answer = str(matching[0]["id"])
        final_key = str(question.get("correctAnswer", ""))
        final_key_text = next((str(option["text"]).strip() for option in question.get("options", [])
                               if str(option.get("id")) == final_key), None)
        if selected_text != final_key_text:
            raise ValueError(f"Blind answer does not match current key by exact option text: {qid}")

        source_fingerprint = str(input_item.get("contentFingerprint", ""))
        if not source_fingerprint:
            raise ValueError(f"Missing source fingerprint for {qid}")
        current_fingerprint = compute_question_fingerprint(question)
        computed_source_fingerprint = compute_question_fingerprint(input_item)
        source_stem = str(input_item.get("stem", "")).strip()
        final_stem = str(question.get("stem", "")).strip()
        source_passage = str(input_item.get("contextPassage") or "").strip()
        final_passage = str(question.get("contextPassage") or "").strip()
        if source_stem != final_stem:
            raise ValueError(f"Stem changed after the latest sealed review: {qid}")
        source_option_texts = sorted(source_options.values())
        final_option_texts = sorted(option_map(question).values())
        if source_option_texts != final_option_texts:
            raise ValueError(f"Options changed semantically after the latest sealed review: {qid}")
        passage_equivalent = (
            source_passage == final_passage
            or source_passage == str(question.get("passage") or "").strip()
            or source_passage == str(listening_sources.get(qid, "")).strip()
            or (not source_passage and not final_passage and not question.get("passage"))
        )
        if not passage_equivalent:
            raise ValueError(f"Passage/transcript differs from the final source for {qid}")
        if source_passage != final_passage:
            if qid in listening_sources and source_passage == listening_sources[qid].strip() and not final_passage:
                transcript_bound_ids.append(qid)

        current_options = option_map(question)
        mapping_method = "DIRECT_IDENTITY" if current_options.get(selected) == selected_text else "EXACT_OPTION_TEXT_REMAP"
        # Every remap is recorded with its original label and verbatim option text.
        mapping_counts[mapping_method] += 1
        version_counts[version] += 1
        raw_selection_map[qid] = selected

        justification = (response.get("justification") or response.get("briefJustification") or "").strip()
        if not justification:
            raise ValueError(f"Reviewer justification missing for {qid}")
        raw_concerns = response.get("concerns", response.get("ambiguityOrWeakness"))
        if isinstance(raw_concerns, str):
            raw_concerns = [raw_concerns] if raw_concerns.strip() else []
        raw_concerns = raw_concerns or []
        non_blocking_note = NON_BLOCKING_REVIEW_NOTES.get(qid)
        normalized_concerns = [] if non_blocking_note else raw_concerns
        record = {
            "id": qid,
            # Keep the reviewer’s original label intact. The existing
            # integrity pipeline remaps it through the matching sealed input.
            "blindAnswer": selected,
            "remappedBlindAnswer": final_answer,
            "originalReviewerSelection": selected,
            "selectedOptionText": selected_text,
            "linguisticJustification": justification,
            "confidence": response.get("confidence"),
            "concerns": normalized_concerns,
            "reviewerNotes": raw_concerns,
            "nonBlockingReviewNote": non_blocking_note,
            "contentFingerprint": current_fingerprint,
            "sourceInputFingerprint": source_fingerprint,
            "computedSourceInputFingerprint": computed_source_fingerprint,
            "sourceInputFile": source_name,
            "reviewVersion": version,
            "reviewerProvenance": "AI_ASSISTED_BLIND_REVIEW; EXACT_OPTION_TEXT_MAPPED",
            "mappingMethod": mapping_method,
            "transcriptBoundToGeneratedSpeech": qid in transcript_bound_ids,
            "reviewLimitations": ["AI-assisted review; not human/native-speaker certification"]
                + (["Listening item assessed from sealed transcript; audio playback is verified separately"]
                   if section_by_id[qid] == 2 else []),
        }
        if version == "v4":
            record["permutationAudit"] = {
                "selectedFragmentId": response.get("selectedFragmentId"),
                "permutationCount": len(response.get("permutationClassifications", [])),
                "naturalOrMarginalAlternativeChangesStarAnswer": response.get("naturalOrMarginalAlternativeChangesStarAnswer"),
            }
        section = section_by_id[qid]
        if section == 2:
            group = "s2"
        else:
            index = next(i for i, s in enumerate(exam["sections"][0]["items"]) if s["id"] == qid)
            group = "s1_p1" if index < 38 else "s1_p2"
        records_by_section[group].append(record)
        inputs_by_section[group].append(input_item)

    for key, filename in {
        "s1_p1": "raw_blind_m08_s1_p1.json",
        "s1_p2": "raw_blind_m08_s1_p2.json",
        "s2": "raw_blind_m08_s2.json",
    }.items():
        (qa / filename).write_text(json.dumps(records_by_section[key], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Preserve the original complete v1 sealed inputs byte-for-byte, then
    # publish merged per-item sealed inputs so each original answer letter is
    # interpreted against the exact revision that reviewer actually saw.
    input_filenames = {
        "s1_p1": "blind_items_m08_s1_p1.json",
        "s1_p2": "blind_items_m08_s1_p2.json",
        "s2": "blind_items_m08_s2.json",
    }
    archived_v1_hashes = {}
    for group, filename in input_filenames.items():
        original_path = qa / filename
        archived_path = qa / filename.replace("blind_items_m08_", "blind_items_m08_v1_")
        if not archived_path.exists():
            archived_path.write_bytes(original_path.read_bytes())
        archived_v1_hashes[archived_path.name] = sha256(archived_path)
        original_path.write_text(json.dumps(inputs_by_section[group], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report = {
        "examId": "N2-MOCK-08",
        "status": "NORMALIZED_VERSION_BOUND_AI_REVIEW",
        "itemCount": len(questions),
        "answerAgreementByExactSelectedOptionText": len(questions),
        "reviewVersions": dict(sorted(version_counts.items())),
        "mappingMethods": dict(sorted(mapping_counts.items())),
        "transcriptBoundListeningItems": sorted(transcript_bound_ids),
        "nonBlockingReviewNotes": NON_BLOCKING_REVIEW_NOTES,
        "transcriptSourceVerification": "Listening transcript strings equal the original source scripts used for generated audio; browser playback/hash QA is documented separately.",
        "fingerprintInterpretation": "The normalized record binds to the final exam fingerprint after exact stem, option-text-set, passage equivalence, and transcript-to-source-script checks. The fingerprint function omits the runtime `passage` property; review inputs may serialize passages as `contextPassage`.",
        "limitations": [
            "AI-assisted review is not human/native-speaker certification.",
            "Listening review used transcripts; the separate browser playback receipt verifies decoding/progression, not pronunciation quality.",
            "The generated normalized records are derived evidence; all original blind responses remain preserved unchanged.",
        ],
        "sourceSha256": {name: source_hashes[name] for name in sorted(source_hashes)},
        "responseSha256": {name: review_hashes[name] for name in sorted(review_hashes)},
        "archivedOriginalV1InputSha256": dict(sorted(archived_v1_hashes.items())),
        "versionBoundMergedInputSha256": {
            filename: sha256(qa / filename) for filename in input_filenames.values()
        },
        "normalizedFiles": {
            "raw_blind_m08_s1_p1.json": sha256(qa / "raw_blind_m08_s1_p1.json"),
            "raw_blind_m08_s1_p2.json": sha256(qa / "raw_blind_m08_s1_p2.json"),
            "raw_blind_m08_s2.json": sha256(qa / "raw_blind_m08_s2.json"),
        },
    }
    (qa / "N2_MOCK_08_BLIND_REVIEW_PROVENANCE.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Normalized {len(questions)} answers; exact-text key agreement verified.")
    print(f"Review versions: {dict(version_counts)}")
    print(f"Mappings: {dict(mapping_counts)}")
    print(f"Transcript-bound items: {len(transcript_bound_ids)}")


if __name__ == "__main__":
    main()
