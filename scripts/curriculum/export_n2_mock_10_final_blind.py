# -*- coding: utf-8 -*-
"""Export key-free, content-bound blind-review inputs for all M10 items."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.blind_review_exporter import validate_sealed_item_purity
from scripts.curriculum.question_fingerprint import compute_question_fingerprint
from scripts.curriculum.bank_data.n2_mock_10_data import get_n2_mock_10_sec1_items
from scripts.curriculum.bank_data.n2_mock_10_listening import get_n2_mock_10_listening_items

OUT = ROOT / "qa/blind_items_m10_final.json"
INSTRUCTIONS = {
    "N2-MO-READ": "下線部の言葉の読み方として最もよいものを一つ選びなさい。",
    "N2-MO-ORTH": "下線部の言葉を漢字で書くとき、最もよいものを一つ選びなさい。",
    "N2-MO-FORM": "文脈に合う語を一つ選びなさい。",
    "N2-MO-CONT": "文脈に合う語を一つ選びなさい。",
    "N2-MO-PARA": "下線部の意味に最も近いものを一つ選びなさい。",
    "N2-MO-USE": "語の使い方として最もよいものを一つ選びなさい。",
    "N2-GR-FORM": "文の（　）に入る最もよいものを一つ選びなさい。",
    "N2-GR-STAR": "文の★に入る語句を一つ選びなさい。",
    "N2-GR-PARA": "文章中の空欄に入る最もよいものを一つ選びなさい。",
    "N2-RD-SHORT": "文章を読んで、問いの答えとして最もよいものを一つ選びなさい。",
    "N2-RD-MED": "文章を読んで、問いの答えとして最もよいものを一つ選びなさい。",
    "N2-RD-PAIR": "二つの資料を読んで、問いの答えとして最もよいものを一つ選びなさい。",
    "N2-RD-LONG": "文章を読んで、問いの答えとして最もよいものを一つ選びなさい。",
    "N2-RD-INFO": "案内を読んで、問いの答えとして最もよいものを一つ選びなさい。",
    "N2-LIS-TASK": "課題理解：音声を聞き、必要な行動を一つ選びなさい。",
    "N2-LIS-POINT": "ポイント理解：音声を聞き、指定された点について一つ選びなさい。",
    "N2-LIS-SUMM": "概要理解：音声を聞き、話し手の主張や要点を一つ選びなさい。",
    "N2-LIS-RESP": "即時応答：短い問いかけを聞き、最も自然な返答を一つ選びなさい。",
    "N2-LIS-INTEG": "統合理解：会話を聞き、複数の情報を合わせて答えを一つ選びなさい。",
}


def sealed_item(q, section, audio_meta=None):
    source = dict(q)
    stimulus = q.get("contextPassage") or q.get("passage")
    if section == 2:
        stimulus = q.get("script", "")
        # Bind the transcript in the assessment fingerprint without putting
        # transcript text into the learner-facing question UI. The physical
        # audio identity is also part of the reviewed assessment version.
        source["contextPassage"] = stimulus
        if not audio_meta:
            raise ValueError(f"Missing audio manifest entry for {q['id']}")
        source["audioUrl"] = audio_meta["audioUrl"]
        source["audioSha256"] = audio_meta["audioSha256"]
    row = {
        "id": q["id"],
        "examId": "N2-MOCK-10",
        "section": section,
        "typeId": q["typeId"],
        "category": q.get("category", ""),
        "taskInstructions": INSTRUCTIONS[q["typeId"]],
        "stem": q.get("stem", ""),
        "contextPassage": stimulus,
        "options": [{"id": o["id"], "text": o["text"]} for o in q["options"]],
        "contentFingerprint": compute_question_fingerprint(source),
    }
    validate_sealed_item_purity(row)
    return row


def main():
    listening = get_n2_mock_10_listening_items()
    manifest_path = ROOT / "data/mock_exams/n2_mock_10_audio_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if set(manifest) != {q["id"] for q in listening}:
        raise ValueError("M10 blind export and audio manifest IDs do not match")
    items = [sealed_item(q, 1) for q in get_n2_mock_10_sec1_items()]
    items.extend(sealed_item(q, 2, manifest[q["id"]]) for q in listening)
    if len(items) != 105 or len({q["id"] for q in items}) != 105:
        raise ValueError("M10 final blind input must contain exactly 105 unique items")
    OUT.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(items)} key-free items)")
    print(f"SHA-256 {hashlib.sha256(OUT.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
