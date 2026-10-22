# -*- coding: utf-8 -*-
"""Small reusable release checks for full-length practice mock exams."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

from scripts.curriculum.question_fingerprint import compute_question_fingerprint


def validate_full_mock_blueprint(exam: dict, required_counts: tuple[int, int] = (75, 30)) -> list[str]:
    errors = []
    sections = exam.get("sections", [])
    counts = [len(section.get("items", [])) for section in sections]
    if len(sections) != 2 or tuple(counts) != required_counts:
        errors.append(f"expected exactly two sections with counts {required_counts}, got {counts}")
    items = [q for section in sections for q in section.get("items", [])]
    ids = [q.get("id") for q in items]
    if len(items) != sum(required_counts) or len(set(ids)) != len(ids):
        errors.append("question count or stable unique IDs do not match the full-mock blueprint")
    if exam.get("totalQuestions") != sum(required_counts):
        errors.append("exam totalQuestions does not match its full-mock blueprint")
    return errors


def validate_star_fragment_integrity(exam: dict) -> list[str]:
    errors = []
    for section in exam.get("sections", []):
        for q in section.get("items", []):
            if q.get("typeId") != "N2-GR-STAR":
                continue
            qid = q.get("id")
            options = {str(row.get("id")): str(row.get("text", "")) for row in q.get("options", [])}
            labels = re.findall(r"[A-D]", str(q.get("fragmentOrder", "")).upper())
            if len(labels) != 4 or len(set(labels)) != 4 or set(labels) != set(options):
                errors.append(f"{qid}: fragmentOrder must arrange all four displayed fragments once")
                continue
            fragments = [options[label] for label in labels]
            joined = "".join(fragments)
            # Newer candidates preserve the full reconstructed sentence,
            # including fixed stem context and terminal punctuation. Older
            # items stored only the four selectable fragments.
            stem = str(q.get("stem", ""))
            slot_pattern = re.compile(r"（[\s　]*★[\s　]*）|（[\s　]*）|★")
            slots = list(slot_pattern.finditer(stem))
            reconstructed = None
            if len(slots) == 4:
                reconstructed = stem
                for match, fragment in reversed(list(zip(slots, fragments, strict=True))):
                    reconstructed = reconstructed[:match.start()] + fragment + reconstructed[match.end():]
            if q.get("assembledSentence") not in {joined, reconstructed}:
                errors.append(f"{qid}: fragment order does not reconstruct assembledSentence")
            if options.get(str(q.get("correctAnswer"))) != fragments[2]:
                errors.append(f"{qid}: authored key is not the third fragment at ★")
    return errors


def validate_version_bound_reconciliation(report: dict, exam: dict, sealed_input: list[dict],
                                          raw_sha256: dict[str, str] | None = None) -> list[str]:
    """Validate a derived answer-text reconciliation without claiming reviewer attestation."""
    errors = []
    if report.get("status") != "REVIEW_CONTENT_VERSION_VERIFIED":
        errors.append("review report is not marked REVIEW_CONTENT_VERSION_VERIFIED")
    if report.get("semanticAgreementCount") != 105 or report.get("semanticMismatchCount") != 0:
        errors.append("review report does not record 105 agreements and zero mismatches")
    if report.get("reviewProvenanceLimit") != "AI blind-review artifacts have no portable execution attestation and do not constitute native-speaker certification.":
        errors.append("review limitations are missing or overstate independent attestation")

    sealed_by_id = {row.get("id"): row for row in sealed_input}
    questions = {q.get("id"): q for section in exam.get("sections", []) for q in section.get("items", [])}
    rows = report.get("rows", [])
    review_by_id = {row.get("questionId"): row for row in rows}
    if len(sealed_by_id) != 105 or len(questions) != 105 or len(review_by_id) != 105:
        errors.append("sealed input, exam, and reconciliation must each contain 105 unique questions")
        return errors
    if set(sealed_by_id) != set(questions) or set(review_by_id) != set(questions):
        errors.append("sealed input/review question IDs do not match the current exam")

    for qid, q in questions.items():
        row = review_by_id.get(qid)
        sealed = sealed_by_id.get(qid)
        if not row or not sealed:
            continue
        fp = compute_question_fingerprint(q)
        if row.get("contentFingerprint") != fp or sealed.get("contentFingerprint") != fp:
            errors.append(f"{qid}: current fingerprint is stale")
        exact_text = row.get("rawReviewerExactOptionText")
        current_matches = [opt for opt in q.get("options", []) if opt.get("text") == exact_text]
        sealed_matches = [opt for opt in sealed.get("options", []) if opt.get("text") == exact_text]
        if len(current_matches) != 1 or len(sealed_matches) != 1:
            errors.append(f"{qid}: selected raw option text does not map uniquely in current and sealed choices")
            continue
        key = next((opt.get("text") for opt in q.get("options", []) if opt.get("id") == q.get("correctAnswer")), None)
        if (current_matches[0].get("id") != row.get("currentDisplayedOptionId")
                or row.get("authoredCorrectOptionId") != q.get("correctAnswer")
                or key != exact_text or row.get("semanticTextAgreement") is not True):
            errors.append(f"{qid}: semantic reviewer selection, displayed key, and authored answer do not agree")

    evidence = report.get("rawEvidence", {})
    for name in ("revision5CapturedRawSha256", "revision6CapturedRawSha256"):
        if not re.fullmatch(r"[0-9a-fA-F]{64}", str(evidence.get(name, ""))):
            errors.append(f"raw review evidence is missing a valid {name}")
    if evidence.get("capturedRawResponsesMutated") is not False or evidence.get("publicRecordsAreSanitizedProjections") is not True:
        errors.append("raw immutability and path-redacted projection provenance must be explicit")
    coverage = report.get("reviewCoverage", {})
    if coverage.get("currentVersionItems") != 105:
        errors.append("review coverage must identify all 105 current-version items")
    revision7 = evidence.get("revision7Delta")
    revision8 = evidence.get("revision8Delta")
    if not isinstance(revision7, dict) or not isinstance(revision8, dict):
        errors.append("supplemental delta review provenance is incomplete")
    else:
        for label, delta in (("revision7", revision7), ("revision8", revision8)):
            for field in ("inputSha256", "sanitizedProjectionSha256", "capturedRawSha256"):
                if not re.fullmatch(r"[0-9a-fA-F]{64}", str(delta.get(field, ""))):
                    errors.append(f"{label} is missing a valid {field}")
            if delta.get("inputHashMatchedBeforeAndAfter") is not True:
                errors.append(f"{label} input hash stability was not recorded")
            if not delta.get("inputPath") or not delta.get("sanitizedProjectionPath"):
                errors.append(f"{label} source path provenance is incomplete")
        if evidence.get("revision7SupersededRows") != coverage.get("supersededReviewRows"):
            errors.append("superseded delta review rows are not reconciled in coverage")
        current_layers = sum(coverage.get(key, 0) for key in (
            "revision5UnchangedItems", "revision6ChangedItems",
            "revision7ChangedItemsStillCurrent", "revision8ChangedItemsCurrent"))
        if current_layers != 105:
            errors.append("version-specific review layers do not cover all current questions exactly once")
    if raw_sha256:
        for name, path in raw_sha256.items():
            actual = hashlib.sha256(Path(path).read_bytes()).hexdigest()
            expected = evidence.get(name)
            if str(expected).lower() != actual:
                errors.append(f"captured raw response digest does not match local immutable evidence: {name}")
    return errors


CURRENT_VERSION_REVIEW_SCHEMA = "CURRENT_VERSION_TEXT_RECONCILIATION_V1"
AI_REVIEW_PROVENANCE_LIMIT = (
    "AI blind-review artifacts have no portable execution attestation and do not constitute native-speaker certification."
)


def validate_current_version_reconciliation(report: dict, exam: dict, sealed_input: list[dict],
                                            raw_sha256: dict[str, str] | None = None) -> list[str]:
    """Validate a key-free, exact-option-text review of one current exam version.

    The report proves content-version binding and semantic answer agreement. It
    does not certify the reviewer as a human linguist or native speaker.
    """
    errors = []
    if report.get("schema") != CURRENT_VERSION_REVIEW_SCHEMA:
        errors.append(f"review schema must be {CURRENT_VERSION_REVIEW_SCHEMA}")
    if report.get("status") != "REVIEW_CONTENT_VERSION_VERIFIED":
        errors.append("review report is not marked REVIEW_CONTENT_VERSION_VERIFIED")
    if report.get("examId") != exam.get("examId"):
        errors.append("review report examId does not match the current exam")
    if report.get("reviewProvenanceLimit") != AI_REVIEW_PROVENANCE_LIMIT:
        errors.append("review limitations are missing or overstate independent attestation")

    questions = {q.get("id"): q for section in exam.get("sections", []) for q in section.get("items", [])}
    sealed_by_id = {row.get("id"): row for row in sealed_input}
    review_by_id = {row.get("questionId"): row for row in report.get("rows", [])}
    count = len(questions)
    if count == 0 or len(sealed_by_id) != count or len(review_by_id) != count:
        errors.append("current exam, key-free sealed input, and review rows must have equal unique question counts")
        return errors
    if set(questions) != set(sealed_by_id) or set(questions) != set(review_by_id):
        errors.append("current exam, key-free sealed input, and review question IDs do not match")

    summary = report.get("summary", {})
    if summary.get("reviewedItems") != count:
        errors.append("summary does not account for every current question")
    if summary.get("semanticAgreementCount") != count or summary.get("semanticMismatchCount") != 0:
        errors.append("release requires exact semantic agreement for every item and zero mismatches")
    if summary.get("unresolvedAmbiguityCount") != 0:
        errors.append("release requires zero unresolved answer ambiguities")

    evidence = report.get("rawEvidence", {})
    for field in ("sealedInputSha256", "rawOutputSha256"):
        if not re.fullmatch(r"[0-9a-fA-F]{64}", str(evidence.get(field, ""))):
            errors.append(f"raw review evidence is missing a valid {field}")
    if evidence.get("inputHashMatchedBeforeAndAfter") is not True:
        errors.append("sealed input hash stability is not recorded")
    if evidence.get("rawResponsePreservedLocally") is not True:
        errors.append("raw reviewer response preservation is not recorded")
    if evidence.get("portableExecutionAttestationAvailable") is not False:
        errors.append("portable execution-attestation limitation is not explicit")

    for qid, q in questions.items():
        row = review_by_id.get(qid)
        sealed = sealed_by_id.get(qid)
        if not row or not sealed:
            continue
        fingerprint = compute_question_fingerprint(q)
        if row.get("contentFingerprint") != fingerprint or sealed.get("contentFingerprint") != fingerprint:
            errors.append(f"{qid}: current fingerprint is stale")
        exact_text = row.get("rawReviewerExactOptionText")
        current_matches = [opt for opt in q.get("options", []) if opt.get("text") == exact_text]
        sealed_matches = [opt for opt in sealed.get("options", []) if opt.get("text") == exact_text]
        if len(current_matches) != 1 or len(sealed_matches) != 1:
            errors.append(f"{qid}: selected exact option text does not map uniquely in current and sealed choices")
            continue
        correct = next((opt for opt in q.get("options", []) if opt.get("id") == q.get("correctAnswer")), None)
        if (current_matches[0].get("id") != row.get("currentDisplayedOptionId")
                or row.get("authoredCorrectOptionId") != q.get("correctAnswer")
                or not correct or correct.get("text") != exact_text
                or row.get("semanticTextAgreement") is not True):
            errors.append(f"{qid}: reviewer text, displayed key, and authored answer do not agree")
        if row.get("alternateDefensibleAnswers"):
            errors.append(f"{qid}: unresolved alternative defensible answer is recorded")

    if raw_sha256:
        for name, path in raw_sha256.items():
            actual = hashlib.sha256(Path(path).read_bytes()).hexdigest()
            expected = evidence.get(name)
            if str(expected).lower() != actual:
                errors.append(f"captured raw response digest does not match local evidence: {name}")
    return errors
