# -*- coding: utf-8 -*-
"""Fail-closed reconciliation of immutable, key-free M11 blind-review evidence."""
from __future__ import annotations

import hashlib
import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.blind_review_exporter import validate_sealed_item_purity
from scripts.curriculum.question_fingerprint import compute_question_fingerprint

QA = ROOT / "qa"
SEALED = QA / "blind_items_m11_final.json"
REV5 = QA / "blind_review_m11_revision5_sanitized.json"
REV6 = QA / "blind_review_m11_revision6_delta_sanitized.json"
REV7 = QA / "blind_review_m11_revision7_delta_sanitized.json"
REV8 = QA / "blind_review_m11_revision8_delta_sanitized.json"
SEALED7 = QA / "blind_items_m11_revision7.json"
SEALED8 = QA / "blind_items_m11_revision8.json"
DELTA7 = QA / "blind_items_m11_revision7_delta.json"
DELTA8 = QA / "blind_items_m11_revision8_delta.json"
PUBLISHED_EXAM = ROOT / "data/mock_exams/n2_mock_11.json"
EXAM = PUBLISHED_EXAM if PUBLISHED_EXAM.exists() else ROOT / "tmp/phase7/n2_mock_11_draft.json"
OUT = QA / "N2_MOCK_11_BLIND_RECONCILIATION.json"
EXPECTED_REVISED = {
    "N2_11_M2_01", "N2_11_M2_02", "N2_11_M2_03", "N2_11_M2_04",
    "N2_11_M2_05", "N2_11_M4_07", "N2_11_M6_01",
}
EXPECTED_REVISION7 = {"N2_11_M9_02", "N2_11_M9_04"}
EXPECTED_REVISION8 = {"N2_11_M9_02"}
STAR_IDS = {f"N2_11_M8_{n:02d}" for n in range(1, 6)}
EXPECTED_PERMUTATIONS = {"".join(p) for p in itertools.permutations("ABCD")}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(reason: str) -> None:
    raise SystemExit(f"FAIL M11 blind review: {reason}")


def main() -> int:
    for path in (SEALED, REV5, REV6, REV7, REV8, SEALED7, SEALED8, DELTA7, DELTA8, EXAM):
        if not path.is_file():
            fail(f"required evidence is missing: {path.relative_to(ROOT)}")

    sealed = load(SEALED)
    rev5_record = load(REV5)
    rev6_record = load(REV6)
    rev7_record = load(REV7)
    rev8_record = load(REV8)
    records = (rev5_record, rev6_record, rev7_record, rev8_record)
    if any(record.get("artifactType") != "SANITIZED_PUBLICATION_PROJECTION" for record in records):
        fail("reviewer records must be explicitly identified as sanitized projections")
    rev5 = rev5_record.get("response", {})
    rev6 = rev6_record.get("response", {})
    rev7 = rev7_record.get("response", {})
    rev8 = rev8_record.get("response", {})
    exam = load(EXAM)
    sealed = load(SEALED)
    sealed7 = load(SEALED7)
    sealed8 = load(SEALED8)
    delta7 = load(DELTA7)
    delta8 = load(DELTA8)
    if digest(SEALED) != digest(SEALED8):
        fail("the current final sealed input must be an exact copy of revision 8")
    if str(rev5.get("sealedInputSha256Before", "")).lower() != str(rev5.get("sealedInputSha256After", "")).lower():
        fail("revision-5 reviewer input changed during review")
    if str(rev6.get("referenceRawResponseSha256", "")).lower() != str(rev5_record.get("sourceRawSha256", "")).lower():
        fail("revision-6 delta does not reference the captured immutable revision-5 response bytes")
    if str(rev6.get("referenceSealedInputSha256", "")).lower() != str(rev5.get("sealedInputSha256Before", "")).lower():
        fail("revision-6 delta references a different revision-5 input")

    exam_questions = {
        q["id"]: q
        for section in exam.get("sections", [])
        for q in section.get("items", [])
    }
    sealed_by_id = {item.get("id"): item for item in sealed}
    rev5_answers = {row.get("questionId"): row for row in rev5.get("answers", [])}
    revised_answers = {row.get("questionId"): row for row in rev6.get("changedItemAnswers", [])}
    if len(sealed_by_id) != 105 or len(exam_questions) != 105 or len(rev5_answers) != 105:
        fail("review, sealed input, and final exam must each cover exactly 105 items")
    if set(sealed_by_id) != set(exam_questions) or set(rev5_answers) != set(exam_questions):
        fail("question IDs do not match across the sealed input, reviewer, and exam")
    if set(revised_answers) != EXPECTED_REVISED:
        fail("revision-6 must contain exactly the seven materially changed questions")
    if rev6.get("fingerprintComparison", {}).get("unchangedFingerprintMatchCount") != 98:
        fail("revision-6 did not verify the 98 unchanged question fingerprints")
    if rev6.get("validation", {}).get("fresh105ItemSolveClaimed") is not False:
        fail("review provenance incorrectly claims a fresh 105-item re-solve")

    for label, record, response, delta_path, delta_rows, expected_ids in (
        ("revision-7", rev7_record, rev7, DELTA7, delta7, EXPECTED_REVISION7),
        ("revision-8", rev8_record, rev8, DELTA8, delta8, EXPECTED_REVISION8),
    ):
        expected_delta_hash = digest(delta_path)
        if response.get("inputSha256") != expected_delta_hash or response.get("inputSha256MatchedBeforeAndAfter") is not True:
            fail(f"{label} response is not bound to the unchanged key-free delta input")
        raw_hash = str(record.get("sourceRawSha256", ""))
        if len(raw_hash) != 64 or any(c not in "0123456789abcdefABCDEF" for c in raw_hash):
            fail(f"{label} response is missing the preserved raw-output digest")
        answer_rows = response.get("answers", [])
        answer_ids = {row.get("questionId") for row in answer_rows}
        if len(answer_rows) != len(expected_ids) or answer_ids != expected_ids:
            fail(f"{label} must contain exactly the authorized delta question IDs")
        if {row.get("id") for row in delta_rows} != expected_ids:
            fail(f"{label} sealed delta does not contain the expected question IDs")

    exam_questions = {
        q["id"]: q
        for section in exam.get("sections", [])
        for q in section.get("items", [])
    }
    sealed_by_id = {item.get("id"): item for item in sealed}
    sealed7_by_id = {item.get("id"): item for item in sealed7}
    sealed8_by_id = {item.get("id"): item for item in sealed8}
    if len(sealed_by_id) != 105 or len(exam_questions) != 105:
        fail("current review, sealed input, and final exam must each cover exactly 105 items")
    if set(sealed_by_id) != set(exam_questions) or set(sealed8_by_id) != set(exam_questions):
        fail("question IDs do not match across the current sealed input and exam")
    if set(sealed7_by_id) != set(exam_questions):
        fail("revision-7 complete sealed input must preserve the complete 105-item set")

    for qid, question in exam_questions.items():
        current_fp = compute_question_fingerprint(question)
        if sealed_by_id[qid].get("contentFingerprint") != current_fp or sealed8_by_id[qid].get("contentFingerprint") != current_fp:
            fail(f"current sealed fingerprint is stale for {qid}")
        if qid not in EXPECTED_REVISION8 and sealed7_by_id[qid].get("contentFingerprint") != current_fp:
            fail(f"revision-7 fingerprint changed without a later review for {qid}")

    rev5_answers = {row.get("questionId"): row for row in rev5.get("answers", [])}
    rev6_answers = {row.get("questionId"): row for row in rev6.get("changedItemAnswers", [])}
    rev7_answers = {row.get("questionId"): row for row in rev7.get("answers", [])}
    rev8_answers = {row.get("questionId"): row for row in rev8.get("answers", [])}
    if len(rev5_answers) != 105 or set(rev6_answers) != EXPECTED_REVISED:
        fail("revision-5 baseline and revision-6 seven-item delta coverage do not match")

    delta7_by_id = {row.get("id"): row for row in delta7}
    delta8_by_id = {row.get("id"): row for row in delta8}
    review_layers = {}
    for qid in exam_questions:
        if qid in EXPECTED_REVISION8:
            review_layers[qid] = (8, rev8_answers[qid], delta8_by_id[qid])
        elif qid in rev7_answers:
            review_layers[qid] = (7, rev7_answers[qid], delta7_by_id[qid])
        elif qid in rev6_answers:
            review_layers[qid] = (6, rev6_answers[qid], sealed7_by_id[qid])
        else:
            review_layers[qid] = (5, rev5_answers[qid], sealed7_by_id[qid])

    reconciled = []
    unchanged = 0
    for qid, question in exam_questions.items():
        review_revision, review, review_input = review_layers[qid]
        validate_sealed_item_purity(sealed_by_id[qid])
        fingerprint = compute_question_fingerprint(question)
        if review_revision in (7, 8):
            review_fp = review_input.get("contentFingerprint")
            exact_text = review.get("exactOptionText")
            selected_id = review.get("selectedOptionId")
            raw_id = selected_id
            rationale = review.get("rationaleJapanese", "")
            confidence = review.get("confidence")
            alternates = review.get("alternateDefensibleAnswers", [])
            concerns = review.get("concerns", [])
        else:
            review_fp = review.get("contentFingerprint")
            exact_text = review.get("exactOptionText")
            raw_id = review.get("selectedOptionId")
            selected_id = next((o.get("id") for o in review_input.get("options", []) if o.get("text") == exact_text), None)
            rationale = review.get("rationaleJapanese", "")
            confidence = review.get("confidence")
            alternates = review.get("alternateDefensibleAnswers", [])
            concerns = review.get("concerns", [])
        if review_fp != fingerprint:
            fail(f"revision-{review_revision} response is not bound to the current fingerprint for {qid}")
        if selected_id is None:
            fail(f"reviewer selection cannot map to one exact displayed option for {qid}")
        selected_texts = [o.get("text") for o in question.get("options", []) if o.get("id") == selected_id]
        if review_revision in (7, 8) and selected_texts != [exact_text]:
            fail(f"{qid}: raw reviewer selection ID and exact option text disagree")
        if not exact_text:
            fail(f"reviewer exact option text is missing for {qid}")
        current_matches = [o for o in question.get("options", []) if o.get("text") == exact_text]
        if len(current_matches) != 1:
            fail(f"reviewer exact option text does not map uniquely to the current displayed choices for {qid}")
        current_id = current_matches[0].get("id")
        key_options = [o for o in question.get("options", []) if o.get("id") == question.get("correctAnswer")]
        if len(key_options) != 1 or key_options[0].get("text") != exact_text:
            fail(f"blind selected option text disagrees with the authored key for {qid}")
        if review_revision == 5:
            unchanged += 1
        reconciled.append({
            "questionId": qid,
            "contentFingerprint": fingerprint,
            "rawReviewerRevision": review_revision,
            "rawReviewerSelectedOptionId": raw_id,
            "rawReviewerExactOptionText": exact_text,
            "currentDisplayedOptionId": current_id,
            "authoredCorrectOptionId": question["correctAnswer"],
            "semanticTextAgreement": True,
            "confidence": confidence,
            "rationaleJapanese": rationale,
            "alternateDefensibleAnswers": alternates,
            "concerns": concerns,
        })

    stars = {row.get("questionId"): row for row in rev5.get("starAudits", [])}
    if set(stars) != STAR_IDS:
        fail("five current unchanged STAR items must retain their original review audit")
    permutation_count = 0
    for qid, star in stars.items():
        findings = star.get("permutationFindings", [])
        orders = [row.get("permutation") for row in findings]
        if len(orders) != 24 or set(orders) != EXPECTED_PERMUTATIONS:
            fail(f"{qid} does not preserve all 24 distinct STAR permutations")
        if not star.get("naturalOrMarginalOrdersShareKeyedThird"):
            fail(f"{qid} has a natural/marginal permutation that changes the ★ answer")
        permutation_count += len(orders)

    report = {
        "examId": "N2-MOCK-11",
        "status": "REVIEW_CONTENT_VERSION_VERIFIED",
        "scope": "Sealed blind answer text reconciled against current displayed options, authored keys, and exact current fingerprints.",
        "generatedBy": "scripts/curriculum/validate_n2_mock_11_blind_review.py",
        "sealedInputSha256": digest(SEALED),
        "rawEvidence": {
            "revision5Path": REV5.relative_to(ROOT).as_posix(),
            "revision5SanitizedProjectionSha256": digest(REV5),
            "revision5CapturedRawSha256": rev5_record.get("sourceRawSha256"),
            "revision6DeltaPath": REV6.relative_to(ROOT).as_posix(),
            "revision6SanitizedProjectionSha256": digest(REV6),
            "revision6CapturedRawSha256": rev6_record.get("sourceRawSha256"),
            "revision6ReferencesRevision5Bytes": True,
            "revision7Delta": {
                "inputPath": DELTA7.relative_to(ROOT).as_posix(),
                "inputSha256": digest(DELTA7),
                "sanitizedProjectionPath": REV7.relative_to(ROOT).as_posix(),
                "sanitizedProjectionSha256": digest(REV7),
                "capturedRawSha256": rev7_record.get("sourceRawSha256"),
                "inputHashMatchedBeforeAndAfter": rev7.get("inputSha256MatchedBeforeAndAfter") is True,
                "captureTimeUtc": rev7.get("captureTimeUtc"),
            },
            "revision8Delta": {
                "inputPath": DELTA8.relative_to(ROOT).as_posix(),
                "inputSha256": digest(DELTA8),
                "sanitizedProjectionPath": REV8.relative_to(ROOT).as_posix(),
                "sanitizedProjectionSha256": digest(REV8),
                "capturedRawSha256": rev8_record.get("sourceRawSha256"),
                "inputHashMatchedBeforeAndAfter": rev8.get("inputSha256MatchedBeforeAndAfter") is True,
                "captureTimeUtc": rev8.get("captureTimeUtc"),
            },
            "revision7SupersededRows": 1,
            "capturedRawResponsesMutated": False,
            "publicRecordsAreSanitizedProjections": True,
        },
        "reviewCoverage": {
            "currentVersionItems": 105,
            "revision5UnchangedItems": unchanged,
            "revision6ChangedItems": len(EXPECTED_REVISED),
            "revision7ChangedItemsStillCurrent": 1,
            "revision8ChangedItemsCurrent": 1,
            "supersededReviewRows": 1,
        },
        "semanticAgreementCount": len(reconciled),
        "semanticMismatchCount": 0,
        "starAudit": {
            "currentStarItems": len(stars),
            "preservedPermutationFindings": permutation_count,
            "retainedAlternativeNaturalSequences": sum(len(row.get("alternateDefensibleSequences", [])) for row in stars.values()),
            "allNaturalOrMarginalOrdersKeepStarAnswer": True,
        },
        "reviewProvenanceLimit": "AI blind-review artifacts have no portable execution attestation and do not constitute native-speaker certification.",
        "rows": reconciled,
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("PASS M11 blind review: 105 current fingerprints, 96 revision-5 + 7 revision-6 + 1 revision-7 + 1 revision-8 answer rows, 105 exact semantic matches, 120 retained STAR permutation judgments.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
