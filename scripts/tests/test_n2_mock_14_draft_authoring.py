# -*- coding: utf-8 -*-
"""Structural and localization checks for the private M14 authoring draft."""
from collections import Counter

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

