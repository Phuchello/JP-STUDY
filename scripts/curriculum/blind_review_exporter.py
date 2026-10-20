# -*- coding: utf-8 -*-
"""
JP-STUDY: Sealed Blind Review Input Exporter (Component A)
Strict Isolation Boundary:
Extracts candidate assessment items and outputs sealed review inputs.
Strictly strips and forbids:
  - correctAnswer
  - explanationVi
  - distractorExplanations
  - authorNotes / rationale
"""
import hashlib
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.question_fingerprint import compute_question_fingerprint

FORBIDDEN_KEYS = {
    'correctAnswer', 'correct_answer', 'key', 'answer',
    'explanationVi', 'explanation', 'explanation_vi',
    'distractorExplanations', 'distractor_explanations',
    'rationale', 'notes', 'reconciliationClassification', 'finalDisposition'
}

JLPT_INSTRUCTIONS = {
    "N2-VO-READ": "下線部の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
    "N2-VO-ORTH": "下線部の言葉を漢字で書くとき、最もよいものを、1・2・3・4から一つ選びなさい。",
    "N2-VO-FORM": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
    "N2-VO-CTX": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
    "N2-VO-PARA": "下線部の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
    "N2-VO-USE": "つぎの言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
    "N2-GR-FORM": "次の文の（　）に入る最もよいものを、1・2・3・4から一つ選びなさい。",
    "N2-GR-STAR": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
    "N2-GR-TEXT": "文章中の空欄に入る最も適切なものを、1・2・3・4から一つ選びなさい。",
    "N2-RD-SHORT": "次の文章を読んで、後の問いに対する答えとして最もよいものを、1・2・3・4から一つ選びなさい。",
    "N2-RD-MID": "次の文章を読んで、後の問いに対する答えとして最もよいものを、1・2・3・4から一つ選びなさい。",
    "N2-RD-COMP": "次のAとBの文章を読んで、後の問いに対する答えとして最もよいものを、1・2・3・4から一つ選びなさい。",
    "N2-RD-LONG": "次の文章を読んで、後の問いに対する答えとして最もよいものを、1・2・3・4から一つ選びなさい。",
    "N2-RD-INFO": "次の案内を読んで、後の問いに対する答えとして最もよいものを、1・2・3・4から一つ選びなさい。",
    "N2-LIS-TASK": "課題理解：問題用紙を見ながら音声を聞き、質問に対する最もよい答えを、1・2・3・4から一つ選びなさい。",
    "N2-LIS-POINT": "ポイント理解：問題用紙を見ながら音声を聞き、質問に対する最もよい答えを、1・2・3・4から一つ選びなさい。",
    "N2-LIS-GIST": "概要理解：音声を聞き、全体の趣旨・主張に対する最もよい答えを、1・2・3・4から一つ選びなさい。",
    "N2-LIS-QUICK": "即時応答：短い問いかけの音声を聞き、最も適切な返答を、1・2・3から一つ選びなさい。",
    "N2-LIS-INT": "統合理解：長めの会話や議論の音声を聞き、質問に対する最もよい答えを、1・2・3・4から一つ選びなさい。"
}

def validate_sealed_item_purity(item: dict):
    """Enforces zero answer-key leakage into blind input."""
    for k in item.keys():
        if k in FORBIDDEN_KEYS:
            raise ValueError(f"CRITICAL CONTAMINATION: Blind review input contains forbidden key '{k}' for {item.get('id')}")
    # Also verify options do not leak any answer property
    for opt in item.get('options', []):
        for ok in opt.keys():
            if ok in FORBIDDEN_KEYS or ok not in {'id', 'text'}:
                raise ValueError(f"CRITICAL CONTAMINATION: Option contains forbidden key '{ok}' in item {item.get('id')}")

def export_exam_blind_inputs(exam_path: Path, output_dir: Path):
    with open(exam_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    exam_id = data.get('examId')
    sec1 = data['sections'][0]['items']
    sec2 = data['sections'][1]['items']

    def create_blind_item(q, sec_num):
        tid = q.get('typeId', '')
        blind_item = {
            "id": q["id"],
            "examId": exam_id,
            "section": sec_num,
            "skill": q.get("skill", "Language Knowledge" if sec_num == 1 else "Listening"),
            "typeId": tid,
            "category": q.get("category", ""),
            "taskInstructions": JLPT_INSTRUCTIONS.get(tid, "最もよいものを一つ選びなさい。"),
            "stem": q.get("stem", ""),
            "contextPassage": q.get("contextPassage") or q.get("dialogue") or q.get("script", None),
            "options": [{"id": o["id"], "text": o["text"]} for o in q.get("options", [])],
            "contentFingerprint": compute_question_fingerprint(q)
        }
        if sec_num == 2 and q.get("audioUrl"):
            blind_item["audioUrl"] = q["audioUrl"]
        validate_sealed_item_purity(blind_item)
        return blind_item

    sec1_blind = [create_blind_item(q, 1) for q in sec1]
    sec2_blind = [create_blind_item(q, 2) for q in sec2]

    assert len(sec1_blind) == 75, f"Expected 75 Sec 1 items, got {len(sec1_blind)}"
    assert len(sec2_blind) == 30, f"Expected 30 Sec 2 items, got {len(sec2_blind)}"

    p1 = sec1_blind[:38]
    p2 = sec1_blind[38:]

    output_dir.mkdir(parents=True, exist_ok=True)
    raw_num = exam_id.split('-')[-1].lower()
    m_num = f"m{raw_num}" if not raw_num.startswith('m') else raw_num

    p1_path = output_dir / f"blind_items_{m_num}_s1_p1.json"
    p2_path = output_dir / f"blind_items_{m_num}_s1_p2.json"
    s2_path = output_dir / f"blind_items_{m_num}_s2.json"

    p1_path.write_text(json.dumps(p1, ensure_ascii=False, indent=2), encoding='utf-8')
    p2_path.write_text(json.dumps(p2, ensure_ascii=False, indent=2), encoding='utf-8')
    s2_path.write_text(json.dumps(sec2_blind, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"Exported clean sealed blind inputs for {exam_id}:")
    print(f"  - Part 1: {len(p1)} items ({p1_path.name})")
    print(f"  - Part 2: {len(p2)} items ({p2_path.name})")
    print(f"  - Sec 2:  {len(sec2_blind)} items ({s2_path.name})")
    return [p1_path, p2_path, s2_path]

if __name__ == '__main__':
    exam_path = ROOT / "data/mock_exams/n2_mock_06.json"
    export_exam_blind_inputs(exam_path, ROOT / "qa")
