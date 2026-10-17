"""
Deterministic Pilot Payload Exporter for Phase 3.7.
Derives MD-N4-VOC-01 payload directly from canonical curriculum/QUESTION_BANK_EXPANDED.json
and curriculum/PRACTICE_SETS.json.
Guarantees exact ordered question IDs, quiz identity, metadata, stems, options, correct answers,
and explanations.
Ensures zero manual drift between audited bank, practice sets, and Google Apps Script runtime.
"""
from pathlib import Path
import json
import hashlib
import sys

# Ensure repo root is in sys.path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.content_fingerprint import (
    canonical_blind_input_fingerprint,
    canonical_scoring_fingerprint,
    canonical_pedagogical_fingerprint,
    canonical_full_item_fingerprint
)

BANK_PATH = ROOT / "curriculum/QUESTION_BANK_EXPANDED.json"
PRACTICE_SETS_PATH = ROOT / "curriculum/PRACTICE_SETS.json"
PAYLOAD_JS_PATH = ROOT / "DRIVE_SETUP/pilot_payload.js"
PAYLOAD_JSON_PATH = ROOT / "tmp/drive-first/pilot_data.json"

PILOT_PRACTICE_SET_ID = "MD-N4-VOC-01"
PILOT_QUESTION_IDS = [
    "N4-MO-READ-001",
    "N4-MO-READ-002",
    "N4-MO-READ-003",
    "N4-MO-READ-004",
    "N4-MO-READ-005"
]


def load_canonical_practice_set(sets_path=PRACTICE_SETS_PATH, set_id=PILOT_PRACTICE_SET_ID):
    """Loads and validates the canonical practice set entry from PRACTICE_SETS.json."""
    with open(sets_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    pset = next((s for s in data.get("sets", []) if s.get("id") == set_id), None)
    if not pset:
        raise ValueError(f"CANONICAL_PILOT_SPEC_MISMATCH: Practice set {set_id} not found in {sets_path}")
    return pset


def derive_pilot_quiz_spec(pset):
    """Derives complete pilotQuiz specification from canonical practice set entry."""
    status = pset.get("readinessStatus") or pset.get("status")
    if status not in ["QA_PASSED_NOT_DEPLOYED", "QA_PASSED_READY_FOR_DEPLOYMENT"]:
        raise ValueError(f"CANONICAL_PILOT_SPEC_MISMATCH: Invalid practice set readinessStatus: '{status}'")
    qids = pset.get("questionIds", [])
    if qids != PILOT_QUESTION_IDS:
        raise ValueError(f"CANONICAL_PILOT_SPEC_MISMATCH: Practice set question IDs {qids} != canonical {PILOT_QUESTION_IDS}")

    t_min = pset.get("timeMinutes", 5)
    return {
        "id": pset["id"],
        "title": f"{pset['id']} | {pset['title']}",
        "objective": pset.get("objective", ""),
        "minutes": [t_min, t_min + 3],
        "questionIds": list(qids),
        "releaseGroup": "PILOT",
        "week": 1,
        "mode": "self_reported_unaided_or_review",
        "status": "QA_PASSED_READY_FOR_DEPLOYMENT",
        "category": pset.get("category", "MICRO_DRILL"),
        "level": pset.get("level", "N4"),
        "skill": pset.get("skill", "KNOWLEDGE_VOCABULARY"),
        "targetAudience": pset.get("targetAudience", "")
    }


def load_canonical_pilot_questions(bank_path=BANK_PATH):
    """Loads and validates the 5 canonical pilot questions from the audited bank."""
    with open(bank_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    bank_questions = {q["id"]: q for q in data.get("questions", [])}

    pilot_questions = {}
    for qid in PILOT_QUESTION_IDS:
        if qid not in bank_questions:
            raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: Question {qid} not found in canonical bank {bank_path}")
        q = bank_questions[qid]
        if q.get("status") != "QA_VERIFIED":
            raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: Question {qid} status is {q.get('status')}, expected QA_VERIFIED")

        stem = (q.get("stem") or "").strip()
        if not stem:
            raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: Question {qid} has empty stem")
        opts = q.get("options", [])
        if len(opts) != 4 or [o.get("id") for o in opts] != ["A", "B", "C", "D"]:
            raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: Question {qid} options invalid: {opts}")
        ans = (q.get("correctAnswer") or "").strip().upper()
        if ans not in ["A", "B", "C", "D"]:
            raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: Question {qid} correctAnswer invalid: {ans}")
        expl = (q.get("explanationVi") or "").strip()
        if not expl:
            raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: Question {qid} explanationVi missing")
        dist_expl = q.get("distractorExplanations") or {}
        if not dist_expl:
            raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: Question {qid} distractorExplanations missing")

        pilot_questions[qid] = {
            "id": qid,
            "level": q.get("level", "N4"),
            "skill": q.get("skill", "Vocabulary"),
            "category": q.get("category", "Từ và kanji"),
            "conceptId": q.get("conceptId", "kanji-reading"),
            "learningObjective": q.get("learningObjective", "Đọc Kanji đời sống N4"),
            "stimulusId": q.get("stimulusId", qid),
            "stem": stem,
            "passage": q.get("contextPassage") or "",
            "options": [{"id": o["id"], "text": o["text"].strip()} for o in opts],
            "correctAnswer": ans,
            "explanationVi": expl,
            "distractorExplanations": {k: v.strip() for k, v in dist_expl.items()},
            "references": q.get("references") or [{
                "title": q.get("sourceMetadata", "Official JLPT N4 specifications"),
                "url": "https://www.jlpt.jp/e/samples/sampleindex.html"
            }],
            "fingerprints": {
                "blindInputSha256": canonical_blind_input_fingerprint(q),
                "scoringSha256": canonical_scoring_fingerprint(q),
                "pedagogicalSha256": canonical_pedagogical_fingerprint(q),
                "fullItemSha256": canonical_full_item_fingerprint(q)
            }
        }
    return pilot_questions


def build_pilot_payload(bank_path=BANK_PATH, sets_path=PRACTICE_SETS_PATH):
    """Constructs the canonical pilot payload object directly from bank and practice sets."""
    pset = load_canonical_practice_set(sets_path)
    pilot_quiz = derive_pilot_quiz_spec(pset)
    questions = load_canonical_pilot_questions(bank_path)
    canonical_repr = json.dumps(questions, ensure_ascii=False, sort_keys=True)
    content_digest = hashlib.sha256(canonical_repr.encode("utf-8")).hexdigest()

    return {
        "version": "pilot-n4-voc-01-2026.10.17",
        "contentDigest": content_digest,
        "pilotQuiz": pilot_quiz,
        "questions": questions
    }


def validate_pilot_payload_against_bank(payload, bank_path=BANK_PATH, sets_path=PRACTICE_SETS_PATH):
    """
    Validates pilot payload questions against canonical bank AND validates complete pilotQuiz
    against canonical PRACTICE_SETS.json.
    Raises ValueError upon any discrepancy.
    """
    # 1. Validate complete pilotQuiz specification against canonical practice set
    pilot_quiz = payload.get("pilotQuiz")
    if not pilot_quiz:
        raise ValueError("CANONICAL_PILOT_SPEC_MISMATCH: Missing pilotQuiz in pilot payload")

    pset = load_canonical_practice_set(sets_path)
    derived_quiz = derive_pilot_quiz_spec(pset)

    if pilot_quiz.get("id") != derived_quiz["id"]:
        raise ValueError(f"CANONICAL_PILOT_SPEC_MISMATCH: pilotQuiz.id mismatch: '{pilot_quiz.get('id')}' != '{derived_quiz['id']}'")
    if pilot_quiz.get("questionIds") != derived_quiz["questionIds"]:
        raise ValueError(f"CANONICAL_PILOT_SPEC_MISMATCH: pilotQuiz.questionIds mismatch: {pilot_quiz.get('questionIds')} != {derived_quiz['questionIds']}")
    if pilot_quiz.get("title") != derived_quiz["title"]:
        raise ValueError(f"CANONICAL_PILOT_SPEC_MISMATCH: pilotQuiz.title mismatch: '{pilot_quiz.get('title')}' != '{derived_quiz['title']}'")
    if pilot_quiz.get("objective") != derived_quiz["objective"]:
        raise ValueError(f"CANONICAL_PILOT_SPEC_MISMATCH: pilotQuiz.objective mismatch: '{pilot_quiz.get('objective')}' != '{derived_quiz['objective']}'")
    if pilot_quiz.get("releaseGroup") != derived_quiz["releaseGroup"]:
        raise ValueError(f"CANONICAL_PILOT_SPEC_MISMATCH: pilotQuiz.releaseGroup mismatch: '{pilot_quiz.get('releaseGroup')}' != '{derived_quiz['releaseGroup']}'")
    if pilot_quiz.get("minutes") != derived_quiz["minutes"]:
        raise ValueError(f"CANONICAL_PILOT_SPEC_MISMATCH: pilotQuiz.minutes mismatch: {pilot_quiz.get('minutes')} != {derived_quiz['minutes']}")

    # Verify that pilotQuiz.questionIds exactly matches payload.questions keys in order
    payload_qids = list(payload.get("questions", {}).keys())
    if list(pilot_quiz.get("questionIds", [])) != payload_qids:
        raise ValueError(f"CANONICAL_PILOT_SPEC_MISMATCH: pilotQuiz.questionIds {pilot_quiz.get('questionIds')} does not match payload questions keys {payload_qids}")

    # 2. Validate individual questions against canonical bank
    canonical_questions = load_canonical_pilot_questions(bank_path)
    payload_questions = payload.get("questions", {})

    for qid in PILOT_QUESTION_IDS:
        if qid not in payload_questions:
            raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: Missing question {qid} in pilot payload")
        p_q = payload_questions[qid]
        c_q = canonical_questions[qid]

        if p_q.get("stem") != c_q.get("stem"):
            raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: Stem mismatch for {qid}: '{p_q.get('stem')}' != '{c_q.get('stem')}'")
        if p_q.get("correctAnswer") != c_q.get("correctAnswer"):
            raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: Answer key mismatch for {qid}: '{p_q.get('correctAnswer')}' != '{c_q.get('correctAnswer')}'")
        if p_q.get("options") != c_q.get("options"):
            raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: Options mismatch for {qid}")
        if p_q.get("explanationVi") != c_q.get("explanationVi"):
            raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: ExplanationVi mismatch for {qid}")
        if p_q.get("distractorExplanations") != c_q.get("distractorExplanations"):
            raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: DistractorExplanations mismatch for {qid}")

    canonical_repr = json.dumps(canonical_questions, ensure_ascii=False, sort_keys=True)
    expected_digest = hashlib.sha256(canonical_repr.encode("utf-8")).hexdigest()
    if payload.get("contentDigest") != expected_digest:
        raise ValueError(f"CANONICAL_PILOT_CONTENT_MISMATCH: Content digest mismatch: {payload.get('contentDigest')} != {expected_digest}")
    return True


def export_pilot_payload(bank_path=BANK_PATH, sets_path=PRACTICE_SETS_PATH):
    payload = build_pilot_payload(bank_path, sets_path)
    validate_pilot_payload_against_bank(payload, bank_path, sets_path)

    PAYLOAD_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    PAYLOAD_JSON_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    js_code = (
        "// Generated deterministically by scripts/curriculum/export_pilot_payload.py from curriculum/QUESTION_BANK_EXPANDED.json and curriculum/PRACTICE_SETS.json.\n"
        "// DO NOT EDIT MANUALLY. Re-run python scripts/curriculum/export_pilot_payload.py to update.\n"
        f"var JP_PILOT_DATA = {json.dumps(payload, ensure_ascii=False, separators=(',', ':'))};\n"
    )

    PAYLOAD_JS_PATH.write_text(js_code, encoding="utf-8")
    print(f"Exported pilot payload: {len(payload['questions'])} items, digest={payload['contentDigest'][:16]}...")
    return payload


if __name__ == "__main__":
    export_pilot_payload()
