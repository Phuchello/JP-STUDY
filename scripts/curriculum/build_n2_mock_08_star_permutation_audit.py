#!/usr/bin/env python3
"""Consolidate the two M08 sentence-order permutation reviews verbatim."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QA = ROOT / "qa"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    exam = load(ROOT / "data/mock_exams/n2_mock_08.json")
    questions = {q["id"]: q for section in exam["sections"] for q in section["items"]}
    v2_path = QA / "raw_blind_m08_revision_v2_agent_response.json"
    v4_path = QA / "raw_blind_m08_revision_v4_agent_response.json"
    v2 = load(v2_path)
    v4 = load(v4_path)
    m8_02 = next(item for item in v2["permutationAudits"] if item["questionId"] == "N2_08_M8_02")
    audits = [
        {
            "questionId": "N2_08_M8_01",
            "reviewVersion": "v4",
            "answer": v4["selectedFragmentId"],
            "permutationClassifications": v4["permutationClassifications"],
            "naturalOrder": v4["intendedNaturalOrder"],
            "naturalSentence": v4["intendedNaturalSentence"],
            "naturalOrMarginalAlternativeChangesStarAnswer": v4["naturalOrMarginalAlternativeChangesStarAnswer"],
            "alternativeAssessment": v4["alternativeAssessment"],
        },
        {
            "questionId": "N2_08_M8_02",
            "reviewVersion": "v2",
            "answer": m8_02["bestStarFragment"],
            "permutations": m8_02["permutations"],
            "naturalOrders": [p["order"] for p in m8_02["permutations"] if p["classification"] == "natural"],
            "marginalOrders": [p["order"] for p in m8_02["permutations"] if p["classification"] == "marginal"],
            "alternativesThatChangeStar": m8_02["alternativesThatChangeStar"],
            "classificationNote": m8_02["classificationNote"],
        },
    ]
    for audit in audits:
        q = questions[audit["questionId"]]
        permutations = audit.get("permutationClassifications", audit.get("permutations", []))
        if len(permutations) != 24:
            raise ValueError(f"Expected 24 permutations for {audit['questionId']}")
        orders = [tuple((row.get("order") if isinstance(row.get("order"), list) else str(row["order"]).replace(" → ", "-").split("-"))) for row in permutations]
        if len(set(orders)) != 24:
            raise ValueError(f"Duplicate or missing permutation for {audit['questionId']}")
        if audit["answer"] != q["correctAnswer"]:
            raise ValueError(f"Star review answer/key mismatch for {audit['questionId']}")

    output = {
        "examId": "N2-MOCK-08",
        "status": "AI_ASSISTED_PERMUTATION_QA",
        "scope": "Both authored star-arrangement items; all 24 A-D permutations evaluated per item.",
        "limitations": ["AI-assisted review; not human/native-speaker certification."],
        "sourceSha256": {
            v2_path.name: sha256(v2_path),
            v4_path.name: sha256(v4_path),
        },
        "items": audits,
    }
    target = QA / "N2_MOCK_08_STAR_PERMUTATION_AUDIT.json"
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {target.name}: 2 items, 48 unique permutations, answer keys match.")


if __name__ == "__main__":
    main()
