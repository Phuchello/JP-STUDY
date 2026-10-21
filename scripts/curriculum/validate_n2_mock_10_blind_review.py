# -*- coding: utf-8 -*-
"""Fail-closed validation of M10 blind-review provenance and reconciliation."""
from __future__ import annotations

import hashlib
import itertools
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.curriculum.blind_review_exporter import validate_sealed_item_purity
from scripts.curriculum.question_fingerprint import compute_question_fingerprint

QA = ROOT / "qa"
PROVENANCE = QA / "N2_MOCK_10_BLIND_REVIEW_PROVENANCE.json"
SEALED = QA / "blind_items_m10_final.json"
STAR_IDS = {f"N2_10_M8_{index:02d}" for index in range(1, 6)}
EXPECTED_ORDERS = {"".join(row) for row in itertools.permutations("ABCD")}
INPUT_FILES = ["blind_items_m10_s1_p1.json", "blind_items_m10_s1_p2.json", "blind_items_m10_s2.json"]
REVIEW_FILES = ["raw_blind_m10_s1_p1.json", "raw_blind_m10_s1_p2.json", "raw_blind_m10_s2.json"]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compatible_text_sha256(data: bytes) -> set[str]:
    """Return hashes for the exact bytes under Git's LF/CRLF checkout conversion.

    The reviewer report is bound to the source file as read on Windows, while
    GitHub Actions checks out text files with LF. Accept only the two equivalent
    newline encodings; all JSON content bytes remain covered by the digest.
    """
    lf_bytes = data.replace(b"\r\n", b"\n")
    crlf_bytes = lf_bytes.replace(b"\n", b"\r\n")
    return {hashlib.sha256(candidate).hexdigest() for candidate in (data, lf_bytes, crlf_bytes)}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def fail(message: str) -> None:
    raise SystemExit(f"FAIL M10 blind review evidence: {message}")


def main() -> int:
    if not PROVENANCE.is_file():
        fail("provenance report is missing")
    report = load(PROVENANCE)
    sealed_hashes = compatible_text_sha256(SEALED.read_bytes())
    if report.get("examId") != "N2-MOCK-10" or report.get("sealedInputSha256") not in sealed_hashes:
        fail("review report is not bound to the current sealed-input SHA-256")
    if not re.fullmatch(r"[0-9a-f]{64}", str(report.get("reviewerResponseSha256", ""))):
        fail("raw reviewer response hash is missing or malformed")
    if report.get("reviewerResponseRetainedOutsideRepository") is not True:
        fail("unmodified reviewer response retention is not recorded")
    if report.get("sealedInputPurityValidated") is not True:
        fail("sealed input purity validation is not recorded")
    if not report.get("reviewerTaskScope") or not report.get("reviewMethod"):
        fail("review method and scope limitations must be recorded")
    if int(report.get("itemCount", 0)) != 105 or int(report.get("selectedAnswerCount", 0)) != 105:
        fail("the reviewer did not solve all 105 items")
    if report.get("exactOptionIdAndTextMappings") != 105:
        fail("not all responses map to an exact sealed option ID and text")

    all_inputs = []
    for filename in INPUT_FILES:
        path = QA / filename
        if not path.is_file():
            fail(f"missing split sealed input: {filename}")
        all_inputs.extend(load(path))
    sealed_rows = load(SEALED)
    if {item.get("id") for item in all_inputs} != {item.get("id") for item in sealed_rows}:
        fail("split sealed inputs do not cover the same 105 question IDs")
    for item in all_inputs:
        validate_sealed_item_purity(item)
    current_exam = load(ROOT / "data/mock_exams/n2_mock_10.json")
    current_questions = {
        question["id"]: question
        for section in current_exam.get("sections", [])
        for question in section.get("items", [])
    }
    sealed_by_id = {item["id"]: item for item in all_inputs}
    if set(current_questions) != set(sealed_by_id):
        fail("sealed input and current exam question IDs differ")
    fingerprint_mismatches = [
        qid for qid, item in sealed_by_id.items()
        if item.get("contentFingerprint") != compute_question_fingerprint(current_questions[qid])
    ]
    if fingerprint_mismatches:
        fail(f"sealed input fingerprints do not match the current exam: {fingerprint_mismatches[:5]}")

    review_rows = []
    for filename in REVIEW_FILES:
        path = QA / filename
        if not path.is_file():
            fail(f"missing normalized review file: {filename}")
        review_rows.extend(load(path))
    review_by_id = {row.get("id"): row for row in review_rows}
    if len(review_by_id) != 105 or set(review_by_id) != set(sealed_by_id):
        fail("normalized review rows do not contain 105 unique, matching IDs")
    for qid, row in review_by_id.items():
        input_item = sealed_by_id[qid]
        options = {str(option["id"]): str(option["text"]).strip() for option in input_item.get("options", [])}
        answer = str(row.get("blindAnswer", "")).strip().upper()
        if answer not in options or options[answer] != str(row.get("selectedOptionText", "")).strip():
            fail(f"normalized answer for {qid} is not an exact input option mapping")
        if row.get("contentFingerprint") != input_item.get("contentFingerprint"):
            fail(f"normalized review for {qid} is not bound to the sealed item fingerprint")

    artifact_hashes = report.get("normalizedArtifactSha256", {})
    for filename in [*INPUT_FILES, *REVIEW_FILES]:
        path = QA / filename
        if artifact_hashes.get(filename) not in compatible_text_sha256(path.read_bytes()):
            fail(f"normalized artifact content hash changed beyond newline conversion: {filename}")

    stars = report.get("starPermutationAudits", [])
    star_map = {entry.get("questionId"): entry for entry in stars}
    if len(star_map) != 5 or set(star_map) != STAR_IDS:
        fail("all five STAR items must have review evidence")
    for qid, entry in star_map.items():
        if entry.get("reviewedPermutationCount") != 24:
            fail(f"{qid} does not include all 24 fragment permutations")
        if entry.get("intendedOrder", "")[2:3] != entry.get("selectedOptionId"):
            fail(f"{qid} reviewer selection does not match the intended third fragment")
        permutations = entry.get("allPermutationJudgments", [])
        codes = [str(row.get("order", "")) for row in permutations]
        if len(codes) != 24 or len(set(codes)) != 24 or set(codes) != EXPECTED_ORDERS:
            fail(f"{qid} permutation evidence is not a full unique set")
        for row in permutations:
            order = str(row.get("order", ""))
            star_id = str(row.get("starOptionId", "")).upper()
            judgment = str(row.get("classification", "")).lower()
            if star_id != order[2:3] or judgment not in {"natural", "marginal", "ungrammatical_or_incomplete", "unnatural"}:
                fail(f"{qid} has malformed STAR permutation evidence")
        alternates = entry.get("naturalOrMarginalOrders", [])
        for alternate in alternates:
            order = str(alternate.get("order", ""))
            star_id = str(alternate.get("starOptionId", "")).upper()
            judgment = str(alternate.get("judgment", alternate.get("classification", ""))).lower()
            if order not in EXPECTED_ORDERS or star_id != order[2] or judgment not in {"natural", "marginal", "unnatural", "ungrammatical_or_incomplete"}:
                fail(f"{qid} has malformed STAR permutation evidence")
            if judgment in {"natural", "marginal"} and star_id != entry.get("selectedOptionId"):
                fail(f"{qid} has an unresolved natural/marginal order that changes the starred answer")
    if report.get("unresolvedStarAlternativesChangingAnswer"):
        fail("unresolved STAR alternatives change the starred answer")

    ledger_path = QA / "QUESTION_AUDIT_LEDGER.json"
    if not ledger_path.is_file():
        fail("question reconciliation ledger is missing")
    ledger = [row for row in load(ledger_path) if row.get("examId") == "N2-MOCK-10"]
    if len(ledger) != 105:
        fail(f"expected 105 reconciled M10 ledger rows, found {len(ledger)}")
    unresolved = [
        row for row in ledger
        if row.get("reconciliationClassification") != "AGREEMENT"
        or row.get("finalDisposition") != "AI_SEMANTIC_VERIFIED"
        or row.get("independentProposedAnswer") != row.get("originalStoredAnswer")
    ]
    if unresolved:
        fail(f"M10 has unresolved key/answer concerns: {[row.get('questionId') for row in unresolved[:10]]}")

    text = PROVENANCE.read_text(encoding="utf-8")
    if re.search(r"[A-Za-z]:\\Users\\", text, re.IGNORECASE):
        fail("local Windows user path must not be published in provenance")
    report["status"] = "REVIEW_CONTENT_VERSION_VERIFIED"
    report["reconciledAgreementCount"] = len(ledger)
    report["unresolvedAnswerConcernCount"] = 0
    report["unresolvedStarAlternativeCount"] = 0
    PROVENANCE.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("PASS M10 blind review: 105/105 exact mappings, current fingerprints, five complete 24-order STAR audits, zero unresolved answer concerns.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
