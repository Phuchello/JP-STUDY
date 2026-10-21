# -*- coding: utf-8 -*-
"""Bind preserved blind-solve outputs to the exact final M07 item versions.

This normalizes an already preserved AI sub-agent response; it does not create
answers, explanations, reviewer identities, or execution attestations.
"""
import hashlib
import itertools
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.blind_review_exporter import validate_sealed_item_purity
from scripts.curriculum.question_fingerprint import compute_question_fingerprint

EXAM_PATH = ROOT / "data/mock_exams/n2_mock_07.json"
PRIMARY_RESPONSE = ROOT / "qa/raw_blind_m07_fresh_agent_response.json"
REVISION_RESPONSE = ROOT / "qa/raw_blind_m07_revision_response.json"
REVISION_INPUT = ROOT / "qa/blind_items_m07_revision_3.json"
STAR_REVISION_RESPONSE = ROOT / "qa/raw_blind_m07_star_revision_response.json"
STAR_REVISION_INPUT = ROOT / "qa/blind_items_m07_star_revision_5.json"
FINAL_STAR_RESPONSE = ROOT / "qa/raw_blind_m07_star_revision_12_response.json"
FINAL_STAR_INPUT = ROOT / "qa/blind_items_m07_star_revision_12.json"
STAR_REVISION_7_RESPONSE = ROOT / "qa/raw_blind_m07_star_revision_7_response.json"
STAR_REVISION_7_INPUT = ROOT / "qa/blind_items_m07_star_revision_7.json"
STAR_REVISION_8_RESPONSE = ROOT / "qa/raw_blind_m07_star_revision_8_response.json"
STAR_REVISION_8_INPUT = ROOT / "qa/blind_items_m07_star_revision_8.json"
STAR_REVISION_9_RESPONSE = ROOT / "qa/raw_blind_m07_star_revision_9_response.json"
STAR_REVISION_9_INPUT = ROOT / "qa/blind_items_m07_star_revision_9.json"
STAR_REVISION_10_RESPONSE = ROOT / "qa/raw_blind_m07_star_revision_10_response.json"
STAR_REVISION_10_INPUT = ROOT / "qa/blind_items_m07_star_revision_10.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def order_code(value):
    if isinstance(value, (list, tuple)):
        return "".join(str(part).strip().upper() for part in value)
    return "".join(char for char in str(value).strip().upper() if char in "ABCD")


def reconstructed_star_sentence(q, order):
    slots = ["(__)", "(__)", "(__)", "(__)"]
    # The canonical JLPT star stem has 3 blanks and one ★, hence four insertion slots.
    marker = "§"
    template = q["stem"].replace("（　　）", marker, 3).replace("★", marker, 1)
    if template.count(marker) != 4:
        raise ValueError(f"Expected four star insertion slots for {q['id']}")
    chunks = {str(o["id"]).upper(): str(o["text"]) for o in q["options"]}
    for option_id in order:
        template = template.replace(marker, chunks[option_id], 1)
    return template


def main() -> None:
    exam = read_json(EXAM_PATH)
    current = {q["id"]: q for section in exam["sections"] for q in section["items"]}
    assert len(current) == 105, f"Expected 105 unique items, got {len(current)}"

    primary_answers = read_json(PRIMARY_RESPONSE)["answers"]
    primary_inputs = {}
    for filename in (
        "blind_items_m07_s1_p1.json",
        "blind_items_m07_s1_p2.json",
        "blind_items_m07_s2.json",
    ):
        for item in read_json(ROOT / "qa" / filename):
            validate_sealed_item_purity(item)
            primary_inputs[item["id"]] = item
    assert set(primary_inputs) == set(current), "Primary sealed-input IDs differ from the exam"
    assert set(primary_answers) == set(current), "Primary blind response is not exactly 105 items"

    revision_output = read_json(REVISION_RESPONSE)
    revision_input = {item["id"]: item for item in read_json(REVISION_INPUT)}
    revision_answers = {
        item["id"]: item["answer"]["option"]
        for item in revision_output["items"]
    }
    assert set(revision_answers) == set(revision_input) == {
        "N2_07_M7_01", "N2_07_M7_06", "N2_07_M9_04"
    }, "Revision review must contain only the three repaired items"

    star_revision_output = read_json(STAR_REVISION_RESPONSE)
    star_revision_input = {item["id"]: item for item in read_json(STAR_REVISION_INPUT)}
    star_revision_answers = {}
    for item in star_revision_output["items"]:
        qid = item["id"]
        order = [str(option).strip().upper() for option in item["natural_order"]]
        answer = str(item["star_option"]).strip().upper()
        if len(order) != 4 or len(set(order)) != 4 or answer != order[2]:
            raise ValueError(f"Blind star-order response is internally inconsistent for {qid}")
        if item.get("alternate_changes_star"):
            raise ValueError(f"Blind reviewer found an alternate ★ answer for {qid}")
        star_revision_answers[qid] = answer
    expected_star_ids = {f"N2_07_M8_0{i}" for i in range(1, 6)}
    assert set(star_revision_answers) == set(star_revision_input) == expected_star_ids, (
        "Star revision response must cover exactly the five sealed M8 star items"
    )

    final_star_output = read_json(FINAL_STAR_RESPONSE)
    final_star_input = {item["id"]: item for item in read_json(FINAL_STAR_INPUT)}
    final_star_answers = {}
    final_star_orders = {}
    star_permutation_audit = []
    expected_permutations = {"".join(parts) for parts in itertools.permutations("ABCD")}
    for item in final_star_output["items"]:
        qid = item["id"]
        order_code_value = order_code(item["natural_order"])
        order = list(order_code_value)
        answer = str(item["star_option"]).strip().upper()
        if len(order) != 4 or len(set(order)) != 4 or answer != order[2]:
            raise ValueError(f"Blind final star-order response is internally inconsistent for {qid}")
        candidates = item.get("candidates", [])
        candidate_orders = [order_code(c.get("order", "")) for c in candidates]
        if len(candidates) != 24 or len(set(candidate_orders)) != 24 or set(candidate_orders) != expected_permutations:
            raise ValueError(f"Blind final star review must judge each of the 24 permutations exactly once for {qid}")
        changed_alternates = [
            c for c, candidate_order in zip(candidates, candidate_orders)
            if str(c.get("judgment", "")).strip().lower() in {"natural", "marginal"}
            and candidate_order[2] != answer
        ]
        if item.get("alternate_changes_star") or changed_alternates:
            raise ValueError(f"Blind reviewer found an alternate ★ answer for {qid}: {changed_alternates}")
        if not any(candidate_order == order_code_value and str(c.get("judgment", "")).lower() == "natural"
                   for c, candidate_order in zip(candidates, candidate_orders)):
            raise ValueError(f"Reviewer did not classify the intended order as natural for {qid}")
        final_star_answers[qid] = answer
        final_star_orders[qid] = order_code_value
        star_permutation_audit.append({
            "questionId": qid,
            "contentFingerprint": final_star_input[qid].get("contentFingerprint"),
            "reviewedPermutations": len(candidates),
            "reviewerNaturalOrder": order_code_value,
            "reviewerStarOption": answer,
            "marginalOrNaturalAlternatesChangingStar": [],
            "candidateJudgments": candidates,
        })
    expected_final_star_ids = {"N2_07_M8_04", "N2_07_M8_05"}
    assert set(final_star_answers) == set(final_star_input) == expected_final_star_ids, (
        "Final star revision response must cover exactly the two sealed final M8 items"
    )

    answer_map = dict(primary_answers)
    answer_map.update(revision_answers)
    answer_map.update(star_revision_answers)
    answer_map.update(final_star_answers)
    input_map = dict(primary_inputs)
    input_map.update(revision_input)
    input_map.update(star_revision_input)
    input_map.update(final_star_input)
    assert len(answer_map) == 105

    grouped = defaultdict(list)
    changed_items = []
    for qid, q in current.items():
        sealed = input_map[qid]
        validate_sealed_item_purity(sealed)
        live_fingerprint = compute_question_fingerprint(q)
        if sealed.get("contentFingerprint") != live_fingerprint:
            raise ValueError(f"Final sealed-input fingerprint mismatch: {qid}")
        if qid in final_star_answers:
            reviewer_order = final_star_orders[qid]
            if q.get("correctAnswer") != final_star_answers[qid]:
                raise ValueError(f"Blind star reviewer answer differs from authored key for {qid}")
            reconstructed = reconstructed_star_sentence(q, reviewer_order)
            if reconstructed != q.get("assembledSentence"):
                raise ValueError(f"Blind star review order does not reconstruct the current sentence for {qid}")
        answer = str(answer_map[qid]).strip().upper()
        options = {str(o["id"]).strip().upper(): str(o["text"]).strip() for o in sealed.get("options", [])}
        if answer not in options:
            raise ValueError(f"Reviewer selection {answer!r} is not a sealed option for {qid}")
        record = {
            "id": qid,
            "blindAnswer": answer,
            "contentFingerprint": live_fingerprint,
            "responseSource": (
                FINAL_STAR_RESPONSE.name if qid in final_star_answers else
                STAR_REVISION_RESPONSE.name if qid in star_revision_answers else
                REVISION_RESPONSE.name if qid in revision_answers else
                PRIMARY_RESPONSE.name
            ),
            "selectedOptionText": options[answer],
        }
        grouped["s2" if qid in {it["id"] for it in read_json(ROOT / "qa/blind_items_m07_s2.json")} else
                "s1_p1" if qid in {it["id"] for it in read_json(ROOT / "qa/blind_items_m07_s1_p1.json")} else
                "s1_p2"].append(record)
        if qid in revision_answers or qid in star_revision_answers or qid in final_star_answers:
            changed_items.append(qid)

    outputs = []
    for part in ("s1_p1", "s1_p2", "s2"):
        out = ROOT / f"qa/review_answers_m07_{part}.json"
        out.write_text(json.dumps(grouped[part], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        outputs.append(out)

    report = [
        "# M07 Blind Review Response Provenance",
        "",
        "The preserved primary response is an AI sub-agent's answer map to the sealed 105-item inputs. Three items were rewritten after the first review flags and replaced by a sealed three-item revision review. Five star-order items were subsequently redesigned and solved from a separate sealed five-item input. Two more star items were examined through successive sealed, exhaustive permutation reviews: reviewers found answer-changing alternates for M8_04/M8_05, then M8_05 alone, and that item was rewritten before the final two-item review. Those negative reviews remain preserved as raw evidence. The final star options are checked against the third fragment in the returned order and all 24 candidate permutations are required in the final audit.",
        "",
        "No authored answer key or explanation was included in any review input. The raw response artifacts preserve the reviewer selections as returned. The three `review_answers` files are normalized copies bound to final item fingerprints; they do not add explanations or alter reviewer selections.",
        "",
        "This is independent blind AI linguistic review, not a native-speaker review and not a portable execution attestation. CI should classify these records as content-version checked, not execution-attested.",
        "",
        f"Primary response SHA-256: `{sha256(PRIMARY_RESPONSE)}`",
        f"Revision response SHA-256: `{sha256(REVISION_RESPONSE)}`",
        f"Revision sealed-input SHA-256: `{sha256(REVISION_INPUT)}`",
        f"Star revision response SHA-256: `{sha256(STAR_REVISION_RESPONSE)}`",
        f"Star revision sealed-input SHA-256: `{sha256(STAR_REVISION_INPUT)}`",
        f"Final star response SHA-256: `{sha256(FINAL_STAR_RESPONSE)}`",
        f"Final star sealed-input SHA-256: `{sha256(FINAL_STAR_INPUT)}`",
        f"Rejected star revision 7 response SHA-256: `{sha256(STAR_REVISION_7_RESPONSE)}`",
        f"Rejected star revision 7 sealed-input SHA-256: `{sha256(STAR_REVISION_7_INPUT)}`",
        f"Rejected star revision 8 response SHA-256: `{sha256(STAR_REVISION_8_RESPONSE)}`",
        f"Rejected star revision 8 sealed-input SHA-256: `{sha256(STAR_REVISION_8_INPUT)}`",
        f"Rejected star revision 9 response SHA-256: `{sha256(STAR_REVISION_9_RESPONSE)}`",
        f"Rejected star revision 9 sealed-input SHA-256: `{sha256(STAR_REVISION_9_INPUT)}`",
        f"Rejected star revision 10 response SHA-256: `{sha256(STAR_REVISION_10_RESPONSE)}`",
        f"Rejected star revision 10 sealed-input SHA-256: `{sha256(STAR_REVISION_10_INPUT)}`",
        f"Current exam SHA-256: `{sha256(EXAM_PATH)}`",
        f"Re-reviewed item IDs: {', '.join(f'`{qid}`' for qid in changed_items)}",
        "",
        "| Normalized response | Count | SHA-256 |",
        "|---|---:|---|",
    ]
    for out in outputs:
        report.append(f"| `{out.name}` | {len(read_json(out))} | `{sha256(out)}` |")
    report.extend([
        "",
        "The first blind reviewer noted that `N2_07_M5_L01` and `N2_07_M5_L02` require inference from the stated constraints rather than an explicit final-choice sentence. Their answer remains unique under the dialogue's criteria; this design nuance is retained in the raw response and should be visible in any human content review.",
    ])
    (ROOT / "qa/M07_REVIEW_RESPONSE_PROVENANCE.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    (ROOT / "qa/M07_STAR_PERMUTATION_RELEASE_AUDIT.json").write_text(
        json.dumps({"reviewSource": FINAL_STAR_RESPONSE.name, "items": star_permutation_audit}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    print(f"Normalized 105 preserved answers; 3 came from the grammar revision, 5 from the first sealed star revision, and 2 from the final sealed star revision. Wrote {len(outputs)} version-bound files.")


if __name__ == "__main__":
    main()
