# -*- coding: utf-8 -*-
"""Build and validate immutable Phase 7.1 M11–M13 candidate receipts.

The receipts keep the original current-release validators untouched. They
extend version binding for the candidate by verifying every changed row against
the exact key-free packet and reviewer response that cover that fingerprint.
Unchanged rows reuse the already validated release reconciliation only when
the full question fingerprint and exact keyed option text are unchanged.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.mock_exam_release_checks import (
    AI_REVIEW_PROVENANCE_LIMIT,
    CURRENT_VERSION_REVIEW_SCHEMA,
    validate_current_version_reconciliation,
)
from scripts.curriculum.question_fingerprint import compute_question_fingerprint

EXAMS = (11, 12, 13)
V6_PACKET = "qa/PHASE_7_1_FRESH_REVIEW_PACKET_20261022_v6.json"
V6_RAW = "qa/PHASE_7_1_INDEPENDENT_REVIEW_RESPONSE_20261022_v6.md"
V8_PACKET = "qa/PHASE_7_1_FRESH_REVIEW_PACKET_20261023_v8.json"
V8_RAW = "qa/PHASE_7_1_FINAL_REVIEW_V8_RAW_20261023_v1.json"
STAR_PACKET = "qa/PHASE_7_1_M12_M13_STAR_DELTA_PACKET_20261023_v1.json"
STAR_RAW = "qa/PHASE_7_1_M12_M13_STAR_DELTA_RAW_20261023_v1.json"
DELTA_PACKET = "qa/PHASE_7_1_FINAL_INTEGRATION_DELTA_PACKET_20261023_v1.json"
DELTA_RAW = "qa/PHASE_7_1_FINAL_INTEGRATION_DELTA_RAW_20261023_v1.json"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest_file(path: Path) -> str:
    return digest_bytes(path.read_bytes())


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def question_map(exam: dict) -> dict[str, tuple[dict, int]]:
    result = {}
    for section_number, section in enumerate(exam.get("sections", []), 1):
        for question in section.get("items", []):
            qid = question.get("id")
            if not qid or qid in result:
                raise ValueError(f"Missing or duplicate question ID in {exam.get('examId')}: {qid}")
            result[qid] = (question, section_number)
    return result


def keyed_text(question: dict) -> tuple[str, str]:
    matches = [option for option in question.get("options", []) if option.get("id") == question.get("correctAnswer")]
    if len(matches) != 1:
        raise ValueError(f"{question.get('id')}: current answer key does not map to exactly one displayed option")
    return str(question["correctAnswer"]), str(matches[0].get("text", ""))


def feedback_fingerprint(question: dict) -> str:
    payload = {
        key: question.get(key)
        for key in ("explanation", "explanationVi", "distractorExplanations")
    }
    return digest_bytes(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def packet_rows(path: Path) -> dict[str, dict]:
    payload = read_json(path)
    rows = payload.get("items", []) if isinstance(payload, dict) else payload
    result = {}
    for row in rows:
        qid = row.get("id") or row.get("questionId")
        if not qid or qid in result:
            raise ValueError(f"Missing or duplicate item ID in packet {rel(path)}: {qid}")
        result[qid] = row
    return result


def fingerprint_from_packet(packet_item: dict, current_question: dict) -> str:
    """Recompute a packet fingerprint, filling only omitted non-visible type metadata.

    Some older key-free review packets declared the canonical fingerprint but
    omitted `typeId` from the exported row. In that case use the candidate's
    typeId solely to reproduce the existing fingerprint schema; the packet's
    learner-visible stem, passage, and option IDs/text still remain byte-exact.
    """
    projection = dict(packet_item)
    if not projection.get("typeId"):
        projection["typeId"] = current_question.get("typeId")
    return compute_question_fingerprint(projection)


def v6_letters(raw_path: Path) -> dict[str, str]:
    raw = raw_path.read_text(encoding="utf-8")
    match = re.search(r"Packet SHA-256:\s*([0-9a-f]{64})", raw, re.IGNORECASE)
    if not match:
        raise ValueError("v6 raw response does not record its packet SHA-256")
    rows = re.findall(r"^\|\s*(N2_[A-Z0-9_]+)\s*\|\s*([A-D])\s*\|", raw, re.MULTILINE)
    result = dict(rows)
    if len(result) != len(rows):
        raise ValueError("v6 raw response repeats an item ID")
    return result


def response_registry() -> dict[str, dict]:
    registry: dict[str, dict] = {}
    v6_packet_path, v6_raw_path = ROOT / V6_PACKET, ROOT / V6_RAW
    v6_hash = digest_file(v6_packet_path)
    v6_raw_text = v6_raw_path.read_text(encoding="utf-8")
    v6_recorded = re.search(r"Packet SHA-256:\s*([0-9a-f]{64})", v6_raw_text, re.IGNORECASE)
    if not v6_recorded or v6_recorded.group(1).lower() != v6_hash:
        raise ValueError("v6 raw response packet fingerprint does not match the preserved packet")
    for qid, option_id in v6_letters(v6_raw_path).items():
        registry[qid] = {
            "kind": "v6_markdown",
            "packetPath": V6_PACKET,
            "rawPath": V6_RAW,
            "packetSha256": v6_hash,
            "rawSha256": digest_file(v6_raw_path),
            "selectedOptionId": option_id,
            "reviewer": "Independent AI editorial reviewer (packet v6)",
            "binding": "Raw response records the packet SHA; preserved packet SHA and item fingerprint match.",
            "concerns": [],
        }

    v8_packet_path, v8_raw_path = ROOT / V8_PACKET, ROOT / V8_RAW
    v8_hash = digest_file(v8_packet_path)
    v8_raw = read_json(v8_raw_path)
    packet_claim = v8_raw.get("packet", {})
    if not (packet_claim.get("sha256BeforeReview") == v8_hash == packet_claim.get("sha256AfterReview")
            and packet_claim.get("matchesExpected") is True):
        raise ValueError("v8 raw response does not prove stable binding to the preserved packet")
    for item in v8_raw.get("items", []):
        qid = item.get("id")
        registry[qid] = {
            "kind": "json_answer",
            "packetPath": V8_PACKET,
            "rawPath": V8_RAW,
            "packetSha256": v8_hash,
            "rawSha256": digest_file(v8_raw_path),
            "selectedOptionId": item.get("selectedOptionId"),
            "selectedExactText": item.get("exactDisplayedOptionText"),
            "reviewer": v8_raw.get("reviewer", "Separate Codex AI editorial reviewer"),
            "binding": "Raw response records matching packet SHA-256 before and after review.",
            "concerns": [item.get("concerns")] if item.get("concerns") else [],
            "alternatives": [],
        }

    star_packet_path, star_raw_path = ROOT / STAR_PACKET, ROOT / STAR_RAW
    star_hash = digest_file(star_packet_path)
    star_raw = read_json(star_raw_path)
    if not (star_raw.get("reviewedPacketSha256") == star_hash
            and star_raw.get("inputHashBefore") == star_hash == star_raw.get("inputHashAfter")):
        raise ValueError("STAR raw response does not prove stable binding to its preserved packet")
    for item in star_raw.get("results", []):
        qid = item.get("id")
        if qid in registry:
            raise ValueError(f"Multiple review sources need explicit precedence for {qid}")
        third = item.get("thirdSlot", {})
        alternatives = []
        same_key_alternatives = []
        for alternative in item.get("alternateDefensibleOrders", []):
            third_alt = alternative.get("thirdSlot", {})
            record = {
                "thirdSlotOptionId": third_alt.get("optionId"),
                "thirdSlotExactText": third_alt.get("text"),
                "fullSentence": alternative.get("fullSentence"),
                "status": alternative.get("status"),
            }
            if third_alt.get("text") == third.get("text"):
                same_key_alternatives.append(record)
            else:
                alternatives.append(record)
        registry[qid] = {
            "kind": "star_third_slot",
            "packetPath": STAR_PACKET,
            "rawPath": STAR_RAW,
            "packetSha256": star_hash,
            "rawSha256": digest_file(star_raw_path),
            "selectedOptionId": third.get("optionId"),
            "selectedExactText": third.get("text"),
            "reviewer": star_raw.get("reviewer", {}).get("identity", "Codex independent blind reviewer"),
            "binding": "Raw response records matching packet SHA-256 before and after review.",
            "concerns": list(item.get("concerns", [])),
            "alternatives": alternatives,
            "sameKeyAlternativeOrders": same_key_alternatives,
            "selectedOrder": item.get("selectedOrder", []),
            "fullSentence": item.get("fullSentence"),
        }

    delta_packet_path, delta_raw_path = ROOT / DELTA_PACKET, ROOT / DELTA_RAW
    delta_hash = digest_file(delta_packet_path)
    delta_raw = read_json(delta_raw_path)
    if delta_raw.get("input", {}).get("sha256") != delta_hash or delta_raw.get("input", {}).get("keyExcluded") is not True:
        raise ValueError("Final delta raw response does not bind to its preserved key-free packet")
    for item in delta_raw.get("items", []):
        qid = item.get("id")
        superseded_sources = {
            "N2_12_M8_05": "star_third_slot",
            "N2_13_M8_02": "star_third_slot",
            "N2_13_M8_05": "star_third_slot",
            "N2_13_M11_03": "v6_markdown",
        }
        if qid in registry and registry[qid].get("kind") != superseded_sources.get(qid):
            raise ValueError(f"Multiple review sources need explicit precedence for {qid}")
        selected = item.get("selectedAnswer", {})
        registry[qid] = {
            "kind": "integration_delta",
            "packetPath": DELTA_PACKET,
            "rawPath": DELTA_RAW,
            "packetSha256": delta_hash,
            "rawSha256": digest_file(delta_raw_path),
            "selectedOptionId": selected.get("optionId"),
            "selectedExactText": selected.get("exactDisplayedOptionText"),
            "reviewer": delta_raw.get("reviewer", {}).get("identity", "Separate Codex AI editorial reviewer"),
            "binding": "Raw response records matching key-free packet SHA-256; row fingerprint is verified against current candidate.",
            "concerns": [item.get("concerns")] if item.get("concerns") and item.get("concerns") != "No material concern." else [],
            "alternatives": item.get("defensibleAlternativeOrders", []),
            "sameKeyAlternativeOrders": [],
            "selectedOrder": selected.get("fullFragmentOrder", []),
            "fullSentence": selected.get("reconstructedSentence"),
            "reviewItem": item,
        }
    return registry


def evidence_files_for_exam(exam_number: int, used_review_sources: set[str]) -> list[dict]:
    files: dict[str, dict] = {}
    for path_str in sorted(used_review_sources):
        path = ROOT / path_str
        files[path_str] = {"path": path_str, "sha256": digest_file(path), "role": "candidate packet or raw response"}
        sidecar = path.with_name(path.stem + ".redaction_provenance.json")
        if sidecar.is_file():
            sidecar_rel = rel(sidecar)
            files[sidecar_rel] = {
                "path": sidecar_rel,
                "sha256": digest_file(sidecar),
                "role": "raw response envelope path-redaction provenance",
            }
    old_report_path = ROOT / f"qa/N2_MOCK_{exam_number:02d}_BLIND_RECONCILIATION.json"
    old_sealed_path = ROOT / f"qa/blind_items_m{exam_number:02d}_final.json"
    for path in (old_report_path, old_sealed_path):
        files[rel(path)] = {"path": rel(path), "sha256": digest_file(path), "role": "unchanged released-version provenance"}
    old_report = read_json(old_report_path)
    raw_path = old_report.get("rawEvidence", {}).get("rawOutputFile")
    if raw_path and not raw_path.startswith("tmp/") and (ROOT / raw_path).is_file():
        files[raw_path] = {"path": raw_path, "sha256": digest_file(ROOT / raw_path), "role": "local historical raw review response"}
    return list(files.values())


def make_key_free_snapshot(exam: dict, qmap: dict[str, tuple[dict, int]]) -> list[dict]:
    rows = []
    for qid, (question, section_number) in qmap.items():
        rows.append({
            "id": qid,
            "examId": exam.get("examId"),
            "section": section_number,
            "typeId": question.get("typeId"),
            "category": question.get("category"),
            "stem": question.get("stem"),
            "contextPassage": question.get("contextPassage") or "",
            "options": question.get("options", []),
            "contentFingerprint": compute_question_fingerprint(question),
        })
    return rows


def changed_source_for(qid: str, exam_number: int, question: dict, registry: dict[str, dict]) -> dict:
    if qid not in registry:
        raise ValueError(f"Changed candidate item has no current-version reviewer response: {qid}")
    source = registry[qid]
    packet_path = ROOT / source["packetPath"]
    packet_map = packet_rows(packet_path)
    packet_item = packet_map.get(qid)
    if not packet_item:
        raise ValueError(f"{qid}: source packet does not contain this row")
    current_fp = compute_question_fingerprint(question)
    packet_fp = packet_item.get("contentFingerprint") or compute_question_fingerprint(packet_item)
    computed_packet_fp = fingerprint_from_packet(packet_item, question)
    if packet_fp != current_fp or computed_packet_fp != current_fp:
        raise ValueError(f"{qid}: review packet fingerprint does not match current candidate")
    if source["packetSha256"] != digest_file(packet_path):
        raise ValueError(f"{qid}: current packet SHA differs from raw reviewer response")

    option_id = source.get("selectedOptionId")
    choices = question.get("options", [])
    by_id = [option for option in choices if option.get("id") == option_id]
    packet_by_id = [option for option in packet_item.get("options", []) if option.get("id") == option_id]
    if len(by_id) != 1 or len(packet_by_id) != 1:
        raise ValueError(f"{qid}: reviewer selection does not map to one displayed option")
    selected_text = source.get("selectedExactText") or by_id[0].get("text")
    if by_id[0].get("text") != selected_text or packet_by_id[0].get("text") != selected_text:
        raise ValueError(f"{qid}: raw response exact option text differs from the current and packet option")
    if source["kind"] == "star_third_slot":
        selected_order = source.get("selectedOrder", [])
        if len(selected_order) != 4 or selected_order[2].get("text") != selected_text or selected_order[2].get("optionId") != option_id:
            raise ValueError(f"{qid}: STAR response does not place the selected fragment in slot three")
        assembled = "".join(str(item.get("text", "")) for item in selected_order)
        if source.get("fullSentence") not in {assembled, assembled + "。"}:
            raise ValueError(f"{qid}: STAR full sentence does not match the reported four-fragment order")
    elif source["kind"] == "integration_delta" and "reviewItem" in source:
        reviewer_item = source["reviewItem"]
        selected = reviewer_item.get("selectedAnswer", {})
        if selected.get("optionId") != option_id or selected.get("exactDisplayedOptionText") != selected_text:
            raise ValueError(f"{qid}: final delta raw response does not bind its exact selected option")
        if question.get("typeId") == "N2-GR-STAR":
            order = selected.get("fullFragmentOrder", [])
            if len(order) != 4 or order[2] != selected_text or "".join(order) != selected.get("reconstructedSentence"):
                raise ValueError(f"{qid}: final delta STAR raw response does not bind its four fragments")
    current_id, current_text = keyed_text(question)
    if selected_text != current_text:
        raise ValueError(f"{qid}: reviewer answer disagrees with the current key by exact option text")
    if source.get("alternatives"):
        raise ValueError(f"{qid}: reviewer recorded a defensible alternative that changes the answer")
    return source | {
        "selectedOptionId": option_id,
        "selectedExactText": selected_text,
        "currentDisplayedOptionId": by_id[0].get("id"),
        "currentAnswerId": current_id,
        "currentAnswerText": current_text,
        "contentFingerprint": current_fp,
        "packetItem": packet_item,
    }


def build_receipt(exam_number: int, registry: dict[str, dict], write: bool = True) -> dict:
    exam_id = f"N2-MOCK-{exam_number:02d}"
    candidate_path = ROOT / f"tmp/phase7/n2_mock_{exam_number:02d}_draft.json"
    published_path = ROOT / f"data/mock_exams/n2_mock_{exam_number:02d}.json"
    if not candidate_path.is_file():
        raise FileNotFoundError(f"Candidate not built: {rel(candidate_path)}")
    candidate = read_json(candidate_path)
    baseline_path = ROOT / f"qa/n2_mock_{exam_number:02d}_phase71_pre_release_baseline.json"
    published = read_json(baseline_path if baseline_path.is_file() else published_path)
    if candidate.get("examId") != exam_id or published.get("examId") != exam_id:
        raise ValueError(f"Exam identity mismatch for {exam_id}")
    candidate_map, published_map = question_map(candidate), question_map(published)
    if set(candidate_map) != set(published_map) or len(candidate_map) != 105:
        raise ValueError(f"{exam_id}: candidate and released item IDs must match at exactly 105")

    snapshot = make_key_free_snapshot(candidate, candidate_map)
    sealed_path = ROOT / f"qa/blind_items_m{exam_number:02d}_phase71_candidate.json"
    receipt_path = ROOT / f"qa/N2_MOCK_{exam_number:02d}_PHASE71_CANDIDATE_RECONCILIATION.json"
    old_report_path = ROOT / f"qa/N2_MOCK_{exam_number:02d}_BLIND_RECONCILIATION.json"
    old_sealed_path = ROOT / f"qa/blind_items_m{exam_number:02d}_final.json"
    old_report = read_json(old_report_path)
    old_sealed = read_json(old_sealed_path)
    old_rows = {row.get("questionId"): row for row in old_report.get("rows", [])}
    old_sealed_rows = {row.get("id"): row for row in old_sealed}
    if set(old_rows) != set(published_map) or set(old_sealed_rows) != set(published_map):
        raise ValueError(f"{exam_id}: historical report or sealed input does not cover the released exam")

    rows = []
    used_paths: set[str] = set()
    counts = {"UNCHANGED_FROM_RELEASED_VERSION": 0, "CHANGED_AND_REVIEWED_CURRENT_VERSION": 0}
    changed_ids = []
    for qid, (question, section_number) in candidate_map.items():
        old_question = published_map[qid][0]
        fp = compute_question_fingerprint(question)
        old_fp = compute_question_fingerprint(old_question)
        current_answer_id, current_answer_text = keyed_text(question)
        feedback_changed = feedback_fingerprint(question) != feedback_fingerprint(old_question)
        if fp == old_fp:
            old_row = old_rows[qid]
            sealed_old = old_sealed_rows[qid]
            if old_row.get("contentFingerprint") != fp or sealed_old.get("contentFingerprint") != fp:
                raise ValueError(f"{qid}: exact released-version provenance fingerprint does not match")
            selected = old_row.get("rawReviewerExactOptionText")
            selected_matches = [o for o in question.get("options", []) if o.get("text") == selected]
            if (len(selected_matches) != 1 or selected_matches[0].get("id") != current_answer_id
                    or selected != current_answer_text or old_row.get("semanticTextAgreement") is not True
                    or old_row.get("alternateDefensibleAnswers")):
                raise ValueError(f"{qid}: historical evidence is not semantically reusable on the exact current version")
            status = "UNCHANGED_FROM_RELEASED_VERSION"
            counts[status] += 1
            source = {
                "kind": "unchanged_release_row",
                "reconciliationPath": rel(old_report_path),
                "reconciliationSha256": digest_file(old_report_path),
                "sealedInputPath": rel(old_sealed_path),
                "sealedInputSha256": digest_file(old_sealed_path),
                "sourceQuestionId": qid,
                "sourceFingerprint": old_row.get("contentFingerprint"),
                "rawEvidenceSummary": old_report.get("rawEvidence", {}),
                "rawReviewerRevision": old_row.get("rawReviewerRevision"),
                "rawReviewerExactOptionText": selected,
            }
            reviewer_id = "Existing version-bound released-version review"
            concerns = list(old_row.get("concerns", []))
            selected_id = old_row.get("rawReviewerSelectedOptionId")
            selected_text = selected
            alternatives = []
            packet_sha = None
            packet_path = None
            raw_path = old_report.get("rawEvidence", {}).get("rawOutputFile")
            raw_sha = old_report.get("rawEvidence", {}).get("rawOutputSha256")
        else:
            source = changed_source_for(qid, exam_number, question, registry)
            status = "CHANGED_AND_REVIEWED_CURRENT_VERSION"
            counts[status] += 1
            changed_ids.append(qid)
            used_paths.update((source["packetPath"], source["rawPath"]))
            reviewer_id = source["reviewer"]
            concerns = list(source.get("concerns", []))
            selected_id = source["selectedOptionId"]
            selected_text = source["selectedExactText"]
            alternatives = list(source.get("alternatives", []))
            packet_sha = source["packetSha256"]
            packet_path = source["packetPath"]
            raw_path = source["rawPath"]
            raw_sha = source["rawSha256"]

        rows.append({
            "questionId": qid,
            "section": section_number,
            "contentFingerprint": fp,
            "releasedContentFingerprint": old_fp,
            "classification": status,
            "reviewEvidenceSource": source,
            "reviewPacketPath": packet_path,
            "reviewPacketSha256": packet_sha,
            "rawReviewerResponseReference": raw_path or rel(old_report_path),
            "rawReviewerResponseSha256": raw_sha,
            "reviewerIdentity": reviewer_id,
            "reviewerSelectedOptionId": selected_id,
            "rawReviewerExactOptionText": selected_text,
            "currentDisplayedOptionId": current_answer_id,
            "authoredCorrectOptionId": current_answer_id,
            "currentKeyedOptionExactText": current_answer_text,
            "semanticTextAgreement": selected_text == current_answer_text,
            "alternateDefensibleAnswers": alternatives,
            "sameKeyAlternativeOrders": source.get("sameKeyAlternativeOrders", []),
            "editorialConcerns": concerns,
            "feedbackChangedWithoutChangingAnswerReviewFingerprint": feedback_changed,
            "feedbackFingerprint": feedback_fingerprint(question),
            "provenanceStatus": "EXACT_VERSION_EVIDENCE_VERIFIED",
            "releaseEligible": selected_text == current_answer_text and not alternatives,
            "releaseEligibilityReason": "Exact key text agrees; no answer-changing alternative is recorded.",
        })

    snapshot_bytes = (json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    v6_raw_path = ROOT / V6_RAW
    # The primary raw-output field names one preserved response; every other
    # response used by this receipt is enumerated and checked separately.
    raw_evidence = {
        "sealedInputSha256": digest_bytes(snapshot_bytes),
        "rawOutputSha256": digest_file(v6_raw_path),
        "rawOutputFile": V6_RAW,
        "rawResponsePreservedLocally": True,
        "inputHashMatchedBeforeAndAfter": True,
        "inputHashMatchMethod": "Reviewer-recorded packet SHA-256 matches the preserved packet; explicit before/after captures are checked where the raw response includes them.",
        "portableExecutionAttestationAvailable": False,
        "perItemPacketHashBinding": "Verified by the dedicated Phase 7.1 candidate receipt validator.",
        "sourceFiles": evidence_files_for_exam(exam_number, used_paths),
    }
    receipt = {
        "schema": CURRENT_VERSION_REVIEW_SCHEMA,
        "candidateReceiptSchema": "PHASE_7_1_CANDIDATE_TEXT_RECONCILIATION_V1",
        "status": "REVIEW_CONTENT_VERSION_VERIFIED",
        "examId": exam_id,
        "reviewProvenanceLimit": AI_REVIEW_PROVENANCE_LIMIT,
        "reviewMethod": "Exact 105-row candidate reconciliation. Unchanged rows reuse matching released-version review; changed rows bind to current key-free packets and preserved raw AI editorial responses.",
        "reviewScopeLimit": "Content version and answer semantics only; not native-speaker certification, JLPT calibration, or portable execution attestation.",
        "candidatePathAtBuild": rel(candidate_path),
        "candidateExamSha256AtBuild": digest_file(candidate_path),
        "releasedBaselinePath": rel(baseline_path) if baseline_path.is_file() else rel(published_path),
        "releasedBaselineSha256": digest_file(baseline_path if baseline_path.is_file() else published_path),
        "summary": {
            "reviewedItems": len(rows),
            "semanticAgreementCount": sum(row["semanticTextAgreement"] for row in rows),
            "semanticMismatchCount": sum(not row["semanticTextAgreement"] for row in rows),
            "unresolvedAmbiguityCount": sum(bool(row["alternateDefensibleAnswers"]) for row in rows),
            "reviewerConcernCount": sum(bool(row["editorialConcerns"]) for row in rows),
            "unchangedFromReleasedVersion": counts["UNCHANGED_FROM_RELEASED_VERSION"],
            "changedAndReviewedCurrentVersion": counts["CHANGED_AND_REVIEWED_CURRENT_VERSION"],
            "changedPending": 0,
            "evidenceInvalidOrIncomplete": 0,
            "currentVersionChangedQuestionIds": changed_ids,
        },
        "rawEvidence": raw_evidence,
        "rows": rows,
    }
    if write:
        sealed_path.write_bytes(snapshot_bytes)
        receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return receipt


def validate_receipt(exam_number: int, registry: dict[str, dict], source: str = "candidate") -> list[str]:
    errors: list[str] = []
    exam_id = f"N2-MOCK-{exam_number:02d}"
    exam_path = (ROOT / f"tmp/phase7/n2_mock_{exam_number:02d}_draft.json") if source == "candidate" else (ROOT / f"data/mock_exams/n2_mock_{exam_number:02d}.json")
    receipt_path = ROOT / f"qa/N2_MOCK_{exam_number:02d}_PHASE71_CANDIDATE_RECONCILIATION.json"
    sealed_path = ROOT / f"qa/blind_items_m{exam_number:02d}_phase71_candidate.json"
    try:
        exam, report, sealed = read_json(exam_path), read_json(receipt_path), read_json(sealed_path)
    except Exception as exc:
        return [f"{exam_id}: cannot read candidate reconciliation inputs: {exc}"]
    if exam.get("examId") != exam_id:
        errors.append(f"{exam_id}: source exam identity mismatch")
    questions = question_map(exam)
    historical_report_path = ROOT / f"qa/N2_MOCK_{exam_number:02d}_BLIND_RECONCILIATION.json"
    historical_sealed_path = ROOT / f"qa/blind_items_m{exam_number:02d}_final.json"
    historical_report = read_json(historical_report_path)
    historical_sealed = read_json(historical_sealed_path)
    historical_rows = {row.get("questionId"): row for row in historical_report.get("rows", [])}
    historical_sealed_rows = {row.get("id"): row for row in historical_sealed}
    rows = {row.get("questionId"): row for row in report.get("rows", [])}
    sealed_rows = {row.get("id"): row for row in sealed}
    if len(questions) != 105 or set(rows) != set(questions) or set(sealed_rows) != set(questions) or len(rows) != 105:
        errors.append(f"{exam_id}: receipt, candidate, and key-free snapshot must contain the same 105 unique IDs")
        return errors
    if report.get("schema") != CURRENT_VERSION_REVIEW_SCHEMA or report.get("status") != "REVIEW_CONTENT_VERSION_VERIFIED":
        errors.append(f"{exam_id}: receipt schema/status mismatch")
    if report.get("reviewProvenanceLimit") != AI_REVIEW_PROVENANCE_LIMIT:
        errors.append(f"{exam_id}: reviewer limitations missing or overstated")
    baseline_path = ROOT / report.get("releasedBaselinePath", "")
    if (not baseline_path.is_file()
            or digest_file(baseline_path) != report.get("releasedBaselineSha256")):
        errors.append(f"{exam_id}: exact pre-Phase-7.1 public baseline snapshot is missing or changed")
    if digest_file(exam_path) != report.get("candidateExamSha256AtBuild"):
        errors.append(f"{exam_id}: receipt does not bind the exact current candidate/published exam bytes")
    expected_summary = report.get("summary", {})
    if expected_summary.get("reviewedItems") != 105 or expected_summary.get("semanticAgreementCount") != 105 or expected_summary.get("semanticMismatchCount") != 0:
        errors.append(f"{exam_id}: answer agreement summary does not reconcile to 105/105")
    if expected_summary.get("unresolvedAmbiguityCount") != 0 or expected_summary.get("changedPending") != 0 or expected_summary.get("evidenceInvalidOrIncomplete") != 0:
        errors.append(f"{exam_id}: ambiguity or pending evidence remains")

    # Validate every referenced immutable source file before using the shared
    # current-version checks. The shared validator remains fail-closed and
    # unchanged; this wrapper supplies the additional multi-packet checks.
    for source_file in report.get("rawEvidence", {}).get("sourceFiles", []):
        path = ROOT / source_file.get("path", "")
        if not path.is_file() or digest_file(path) != source_file.get("sha256"):
            errors.append(f"{exam_id}: source evidence digest does not match: {source_file.get('path')}")
    for qid, (question, section_number) in questions.items():
        row, sealed_row = rows[qid], sealed_rows[qid]
        fp = compute_question_fingerprint(question)
        if row.get("contentFingerprint") != fp or sealed_row.get("contentFingerprint") != fp:
            errors.append(f"{qid}: candidate receipt or sealed snapshot fingerprint is stale")
        if row.get("section") != section_number or sealed_row.get("options") != question.get("options"):
            errors.append(f"{qid}: section or key-free exact displayed options mismatch")
        key_id, key_text = keyed_text(question)
        if row.get("authoredCorrectOptionId") != key_id or row.get("currentDisplayedOptionId") != key_id or row.get("currentKeyedOptionExactText") != key_text:
            errors.append(f"{qid}: answer key binding in receipt does not match current candidate")
        if row.get("rawReviewerExactOptionText") != key_text or row.get("semanticTextAgreement") is not True or row.get("releaseEligible") is not True:
            errors.append(f"{qid}: reviewer exact text does not agree with current key")
        historical_row = historical_rows.get(qid, {})
        historical_sealed_row = historical_sealed_rows.get(qid, {})
        released_fp = historical_row.get("contentFingerprint")
        if (row.get("releasedContentFingerprint") != released_fp
                or historical_sealed_row.get("contentFingerprint") != released_fp):
            errors.append(f"{qid}: released-version comparison fingerprint is stale")
        expected_class = "UNCHANGED_FROM_RELEASED_VERSION" if fp == released_fp else "CHANGED_AND_REVIEWED_CURRENT_VERSION"
        if row.get("classification") != expected_class:
            errors.append(f"{qid}: reuse/current-review classification is incorrect")
        if expected_class == "UNCHANGED_FROM_RELEASED_VERSION":
            src = row.get("reviewEvidenceSource", {})
            if (src.get("kind") != "unchanged_release_row" or src.get("reconciliationSha256") != digest_file(historical_report_path)
                    or historical_row.get("contentFingerprint") != fp
                    or historical_row.get("rawReviewerExactOptionText") != key_text
                    or historical_row.get("semanticTextAgreement") is not True
                    or historical_row.get("alternateDefensibleAnswers")):
                errors.append(f"{qid}: historical answer evidence cannot be reused")
        else:
            spec = registry.get(qid)
            if not spec:
                errors.append(f"{qid}: no independent current-version response is available")
                continue
            packet_path = ROOT / spec["packetPath"]
            raw_path = ROOT / spec["rawPath"]
            if not packet_path.is_file() or not raw_path.is_file():
                errors.append(f"{qid}: current-version packet or raw response is missing")
                continue
            packet_hash = digest_file(packet_path)
            if (packet_hash != spec.get("packetSha256") or row.get("reviewPacketSha256") != packet_hash
                    or row.get("reviewPacketPath") != spec.get("packetPath")
                    or row.get("rawReviewerResponseReference") != spec.get("rawPath")
                    or digest_file(raw_path) != row.get("rawReviewerResponseSha256")):
                errors.append(f"{qid}: packet/raw response binding differs from the preserved evidence")
            packet_item = packet_rows(packet_path).get(qid)
            if not packet_item or fingerprint_from_packet(packet_item, question) != fp or packet_item.get("contentFingerprint") != fp:
                errors.append(f"{qid}: packet does not contain the exact candidate fingerprint")
            if spec.get("selectedExactText") and spec.get("selectedExactText") != key_text:
                errors.append(f"{qid}: raw current reviewer response selects a different exact option text")
            if spec.get("selectedOptionId") != key_id:
                errors.append(f"{qid}: raw current reviewer response selects a different option ID")
            if spec.get("alternatives"):
                errors.append(f"{qid}: current reviewer reported a defensible answer-changing alternative")
    if not errors:
        # The existing shared checker is applied unchanged to the candidate
        # snapshot and reconciliation. It confirms unique IDs, exact content
        # fingerprints, selected option text, key semantics, and zero ambiguity.
        errors.extend(validate_current_version_reconciliation(report, exam, sealed))
    return errors


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "--validate":
        source = sys.argv[2] if len(sys.argv) > 2 else "candidate"
        registry = response_registry()
        failures = []
        for number in EXAMS:
            failures.extend(validate_receipt(number, registry, source=source))
        if failures:
            print("FAIL Phase 7.1 candidate reconciliation:\n- " + "\n- ".join(failures))
            return 1
        print("PASS Phase 7.1 candidate reconciliation: 315/315 rows; exact fingerprints, packet/raw provenance, answer semantics, and zero unresolved answer ambiguity.")
        return 0

    registry = response_registry()
    # Snapshot the complete reviewer-source packet set before writing receipts.
    packet_hashes_before = {spec["packetPath"]: digest_file(ROOT / spec["packetPath"]) for spec in registry.values()}
    for number in EXAMS:
        receipt = build_receipt(number, registry)
        summary = receipt["summary"]
        print(f"{receipt['examId']}: {summary['unchangedFromReleasedVersion']} unchanged + {summary['changedAndReviewedCurrentVersion']} changed/reviewed = {summary['reviewedItems']} rows")
    packet_hashes_after = {spec["packetPath"]: digest_file(ROOT / spec["packetPath"]) for spec in registry.values()}
    if packet_hashes_before != packet_hashes_after:
        print("FAIL: one or more review packets changed while receipts were built")
        return 1
    return main_validate()


def main_validate() -> int:
    registry = response_registry()
    failures = []
    for number in EXAMS:
        failures.extend(validate_receipt(number, registry))
    if failures:
        print("FAIL Phase 7.1 candidate reconciliation:\n- " + "\n- ".join(failures))
        return 1
    print("PASS Phase 7.1 candidate reconciliation: 315/315 rows; exact fingerprints, packet/raw provenance, answer semantics, and zero unresolved answer ambiguity.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
