# -*- coding: utf-8 -*-
"""Structural and localization checks for the private M14 authoring draft."""
from collections import Counter
import copy

from scripts.curriculum.bank_data.n2_mock_14_data import get_n2_mock_14_sec1_items
from scripts.curriculum.bank_data.n2_mock_14_listening import get_n2_mock_14_listening_items
from scripts.curriculum.content_quality_checks import (
    pattern_defects,
    validate_answer_letter_references,
    validate_vietnamese_explanations,
)
from scripts.curriculum.mock_exam_release_checks import (
    validate_full_mock_blueprint,
    validate_star_fragment_integrity,
)
from scripts.curriculum.audit_star_permutations import validate_star_structure


def make_draft():
    return {
        "examId": "N2-MOCK-14",
        "title": "JLPT N2 Practice Mock Exam #14 — Comprehensive Challenge (đang phát triển)",
        "level": "N2",
        "status": "IN_DEVELOPMENT",
        "durationMinutes": 155,
        "totalQuestions": 105,
        "sections": [
            {"sectionId": "sec-1", "durationMinutes": 105, "itemCount": 75,
             "items": get_n2_mock_14_sec1_items()},
            {"sectionId": "sec-2", "durationMinutes": 50, "itemCount": 30,
             "items": get_n2_mock_14_listening_items()},
        ],
    }


def test_m14_draft_keeps_the_full_practice_blueprint_and_unique_bindings():
    exam = make_draft()
    items = [item for section in exam["sections"] for item in section["items"]]
    assert not validate_full_mock_blueprint(exam)
    assert len(items) == 105
    assert len({item["id"] for item in items}) == 105
    assert all(item["id"].startswith("N2_14_") for item in items)
    assert all(item["correctAnswer"] in {option["id"] for option in item["options"]}
               for item in items)
    assert all(len({option["text"] for option in item["options"]}) == len(item["options"])
               for item in items)


def test_m14_draft_matches_every_section_task_type_and_response_choice_width():
    exam = make_draft()
    sec1, sec2 = (section["items"] for section in exam["sections"])
    assert Counter(item["typeId"] for item in sec1) == {
        "N2-MO-READ": 5, "N2-MO-ORTH": 5, "N2-MO-FORM": 5,
        "N2-MO-CONT": 7, "N2-MO-PARA": 5, "N2-MO-USE": 5,
        "N2-GR-FORM": 12, "N2-GR-STAR": 5, "N2-GR-PARA": 5,
        "N2-RD-SHORT": 5, "N2-RD-MED": 9, "N2-RD-PAIR": 2,
        "N2-RD-LONG": 3, "N2-RD-INFO": 2,
    }
    assert Counter(item["typeId"] for item in sec2) == {
        "N2-LIS-TASK": 5, "N2-LIS-POINT": 6, "N2-LIS-SUMM": 5,
        "N2-LIS-RESP": 11, "N2-LIS-INTEG": 3,
    }
    assert all(len(item["options"]) == (3 if item["typeId"] == "N2-LIS-RESP" else 4)
               for item in sec2)
    assert all(item["script"] for item in sec2 if item["typeId"] != "N2-LIS-RESP")


def test_m14_draft_explanations_stars_and_answer_patterns_pass_shared_guards():
    exam = make_draft()
    assert not validate_vietnamese_explanations(exam)
    assert not validate_answer_letter_references(exam)
    assert not validate_star_fragment_integrity(exam)
    assert not pattern_defects({"N2-MOCK-14": exam})


def test_m14_star_questions_show_four_slots_and_enumerate_all_permutations():
    exam = make_draft()
    stars = [item for item in exam["sections"][0]["items"] if item["typeId"] == "N2-GR-STAR"]
    assert len(stars) == 5
    for item in stars:
        assert item.get("contextPassage")
        assert item["stem"].count("★") == 1
        valid, reason, data = validate_star_structure(item)
        assert valid, f"{item['id']}: {reason}"
        assert len(data["permutations"]) == 24

    malformed = copy.deepcopy(stars[0])
    malformed["stem"] = "担当者は、★と指示した。"
    assert not validate_star_structure(malformed)[0]


def test_m14_usage_items_are_unglossed_and_have_bound_natural_sentences():
    items = [item for item in get_n2_mock_14_sec1_items()
             if item["typeId"] == "N2-MO-USE"]
    assert [item["id"] for item in items] == [f"N2_14_M1_{n:02}" for n in range(28, 33)]
    expected = {
        "N2_14_M1_28": "来年度は利用者が一割ほど増えると見込んで、受付時間を延長した。",
        "N2_14_M1_29": "複数の見積もりと効果を比べた結果、この価格設定は妥当だと判断した。",
        "N2_14_M1_30": "安全を確認するため、鉄道会社は一部路線の運行を見合わせた。",
        "N2_14_M1_31": "受付開始まで三十分あるので、時間に余裕をもって会場へ向かった。",
        "N2_14_M1_32": "申請書の記入欄を減らし、利用者の負担を軽くした。",
    }
    for item in items:
        assert "という意味" not in item["stem"]
        assert "意味は" not in item["stem"]
        assert len(item["options"]) == 4
        assert len({option["text"] for option in item["options"]}) == 4
        keyed = next(option["text"] for option in item["options"]
                     if option["id"] == item["correctAnswer"])
        assert keyed == expected[item["id"]]

    datum = next(item for item in items if item["id"] == "N2_14_M1_29")
    assert any("事実を妥当している" in option["text"] for option in datum["options"])
    assert any("説明が妥当だ確かめる" in option["text"] for option in datum["options"])
    assert "妥当する" in datum["explanationVi"]

