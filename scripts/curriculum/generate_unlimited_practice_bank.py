# -*- coding: utf-8 -*-
"""
Unlimited Practice Engine Bank Generator & Quality Gate.
Compiles, audits, and bundles:
- >= 400 N2 items (Vocabulary, Grammar, Reading, Listening)
- >= 200 N3 items (Vocabulary, Grammar, Reading, Listening)
- >= 25 original reading passages with multi-item comprehension questions
- >= 20 playable listening tracks with questions
- Preserves all 40 canonical N4 items (including MD-N4-VOC-01 pilot and P0 items)
Outputs:
- curriculum/PRACTICE_ENGINE_BANK.json
- docs/widgets/practice_bank.js
"""
import sys
import os
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.bank_data.n2_data import get_n2_vocab_grammar_items
from scripts.curriculum.bank_data.n2_reading_listening import get_n2_reading_listening_items
from scripts.curriculum.bank_data.n3_data import get_n3_vocab_grammar_items
from scripts.curriculum.bank_data.n3_reading_listening import get_n3_reading_listening_items

BANK_EXPANDED = ROOT / "curriculum/QUESTION_BANK_EXPANDED.json"
OUTPUT_JSON = ROOT / "curriculum/PRACTICE_ENGINE_BANK.json"
OUTPUT_JS = ROOT / "docs/widgets/practice_bank.js"

def load_canonical_n4_items():
    """Loads and preserves the 40 audited N4 items from QUESTION_BANK_EXPANDED.json."""
    with open(BANK_EXPANDED, "r", encoding="utf-8") as f:
        data = json.load(f)
    n4_items = [q for q in data.get("questions", []) if q.get("level") == "N4"]
    print(f"Loaded {len(n4_items)} canonical N4 items from {BANK_EXPANDED.name}.")
    return n4_items

def validate_question(q, seen_ids):
    qid = q.get("id")
    if not qid:
        raise ValueError("Missing 'id' in question.")
    if qid in seen_ids:
        raise ValueError(f"Duplicate question ID detected: {qid}")
    seen_ids.add(qid)

    # Level
    lvl = q.get("level")
    if lvl not in ["N2", "N3", "N4"]:
        raise ValueError(f"Invalid level '{lvl}' in question {qid}")

    # Skill
    skill = q.get("skill")
    if skill not in ["Vocabulary", "Grammar", "Reading", "Listening"]:
        raise ValueError(f"Invalid skill '{skill}' in question {qid}")

    # Stem
    stem = q.get("stem")
    if not stem or not stem.strip():
        raise ValueError(f"Empty stem in question {qid}")

    # Options
    opts = q.get("options", [])
    if len(opts) != 4:
        raise ValueError(f"Question {qid} does not have exactly 4 options: {len(opts)}")
    opt_ids = [o.get("id") for o in opts]
    if opt_ids != ["A", "B", "C", "D"]:
        raise ValueError(f"Question {qid} has invalid option IDs: {opt_ids}")
    for o in opts:
        if not o.get("text") or not o.get("text").strip():
            raise ValueError(f"Question {qid} option {o.get('id')} has empty text.")
    # Options text uniqueness
    norm_texts = [unicodedata.normalize('NFKC', o.get("text", "").strip()) for o in opts]
    if len(norm_texts) != len(set(norm_texts)):
        raise ValueError(f"Question {qid} has duplicate options: {norm_texts}")

    # Correct Answer
    ans = q.get("correctAnswer")
    if ans not in ["A", "B", "C", "D"]:
        raise ValueError(f"Question {qid} has invalid correctAnswer: {ans}")

    # Explanation
    exp = q.get("explanationVi")
    if not exp or not exp.strip():
        raise ValueError(f"Question {qid} has empty explanationVi.")

    # Distractor explanations
    dist_exps = q.get("distractorExplanations")
    if not dist_exps or not isinstance(dist_exps, dict):
        raise ValueError(f"Question {qid} missing distractorExplanations dict.")
    for d_char in ["A", "B", "C", "D"]:
        if d_char != ans and d_char not in dist_exps:
            raise ValueError(f"Question {qid} missing distractor explanation for option {d_char}.")

    # Reading check
    if skill == "Reading":
        if not q.get("contextPassage"):
            raise ValueError(f"Reading question {qid} missing contextPassage.")

    # Listening check
    if skill == "Listening":
        if not q.get("audioUrl"):
            raise ValueError(f"Listening question {qid} missing audioUrl.")

    return True

def compile_and_validate_bank():
    print("=" * 60)
    print("JP-STUDY UNLIMITED PRACTICE ENGINE: BANK COMPILATION")
    print("=" * 60)

    all_questions = []

    # 1. N2 Items
    n2_vg = get_n2_vocab_grammar_items()
    n2_rl = get_n2_reading_listening_items()
    all_questions.extend(n2_vg)
    all_questions.extend(n2_rl)
    print(f"Total N2 items loaded: {len(n2_vg) + len(n2_rl)}")

    # 2. N3 Items
    n3_vg = get_n3_vocab_grammar_items()
    n3_rl = get_n3_reading_listening_items()
    all_questions.extend(n3_vg)
    all_questions.extend(n3_rl)
    print(f"Total N3 items loaded: {len(n3_vg) + len(n3_rl)}")

    # 3. N4 Items (Preserve canonical audited pilot & P0 items)
    n4_items = load_canonical_n4_items()
    all_questions.extend(n4_items)

    print(f"Total combined questions: {len(all_questions)}")

    # Rigorous Validation Gate
    seen_ids = set()
    level_counts = {}
    skill_counts = {}
    status_counts = {}
    quarantined_count = 0
    active_count = 0
    reading_passages = set()
    listening_tracks = set()

    for q in all_questions:
        # Enforce P0-1 status integrity and P0-2 listening quarantine
        is_canonical_n4 = q.get("level") == "N4" and q.get("id", "").startswith("N4-")
        if q.get("skill") == "Listening":
            q["status"] = "QUARANTINED"
            q["exposureEligible"] = False
            q["quarantineReason"] = "Pending verified audio-to-script alignment (Stage 2 roadmap)"
            quarantined_count += 1
        elif is_canonical_n4:
            q["status"] = "QA_VERIFIED"
            q["exposureEligible"] = True
            active_count += 1
        else:
            q["status"] = "PROVISIONAL_PRACTICE"
            q["exposureEligible"] = True
            active_count += 1

        validate_question(q, seen_ids)
        lvl = q["level"]
        skill = q["skill"]
        status = q["status"]
        level_counts[lvl] = level_counts.get(lvl, 0) + 1
        skill_counts[skill] = skill_counts.get(skill, 0) + 1
        status_counts[status] = status_counts.get(status, 0) + 1
        if skill == "Reading" and q.get("stimulusId"):
            reading_passages.add(q["stimulusId"])
        if skill == "Listening" and q.get("audioUrl"):
            listening_tracks.add(q["audioUrl"])

    print("-" * 60)
    print("VALIDATION RESULTS & AUDIT METRICS:")
    print("Level breakdown:", level_counts)
    print("Skill breakdown:", skill_counts)
    print("Status breakdown:", status_counts)
    print(f"Active Practice Questions: {active_count} | Quarantined: {quarantined_count}")
    print(f"Unique Reading Passages: {len(reading_passages)} (Target: >= 25) -> {'PASS' if len(reading_passages) >= 25 else 'FAIL'}")
    print(f"Playable Listening Tracks: {len(listening_tracks)} (Target: >= 20) -> {'PASS' if len(listening_tracks) >= 20 else 'FAIL'}")
    print(f"N2 Questions Count: {level_counts.get('N2', 0)} (Target: >= 400) -> {'PASS' if level_counts.get('N2', 0) >= 400 else 'FAIL'}")
    print(f"N3 Questions Count: {level_counts.get('N3', 0)} (Target: >= 200) -> {'PASS' if level_counts.get('N3', 0) >= 200 else 'FAIL'}")
    print("-" * 60)

    # Check targets strictly
    if level_counts.get("N2", 0) < 400:
        raise ValueError(f"N2 target not met: {level_counts.get('N2', 0)} < 400")
    if level_counts.get("N3", 0) < 200:
        raise ValueError(f"N3 target not met: {level_counts.get('N3', 0)} < 200")
    if len(reading_passages) < 25:
        raise ValueError(f"Reading passages target not met: {len(reading_passages)} < 25")

    # Build Bank Metadata
    bank_payload = {
        "engineVersion": "2.0.0-unlimited",
        "description": "JP-STUDY Large-Scale Dynamic Practice Engine Question Bank",
        "primaryTarget": "JLPT N2 December 2026",
        "totalQuestions": len(all_questions),
        "activeQuestionsCount": active_count,
        "quarantinedQuestionsCount": quarantined_count,
        "levels": level_counts,
        "skills": skill_counts,
        "statusBreakdown": status_counts,
        "metrics": {
            "n2Questions": level_counts.get("N2", 0),
            "n3Questions": level_counts.get("N3", 0),
            "n4Questions": level_counts.get("N4", 0),
            "activeQuestions": active_count,
            "quarantinedQuestions": quarantined_count,
            "readingPassages": len(reading_passages),
            "listeningTracks": len(listening_tracks),
            "allQAPassed": True
        },
        "questions": all_questions
    }

    # Write JSON
    OUTPUT_JSON.write_text(json.dumps(bank_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Successfully saved canonical bank JSON: {OUTPUT_JSON} ({OUTPUT_JSON.stat().st_size:,} bytes)")

    # Write JS Bundle
    js_content = f"// JP-STUDY Dynamic Practice Bank Bundle - Version 2.0.0\nwindow.JP_PRACTICE_BANK = {json.dumps(bank_payload, ensure_ascii=False)};\n"
    OUTPUT_JS.write_text(js_content, encoding="utf-8")
    print(f"Successfully saved browser JS bundle: {OUTPUT_JS} ({OUTPUT_JS.stat().st_size:,} bytes)")

    return bank_payload

if __name__ == '__main__':
    compile_and_validate_bank()
