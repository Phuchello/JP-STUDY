# -*- coding: utf-8 -*-
"""Versioned STAR display and context repairs for N2 mock authoring sources.

These candidates remain unreviewed until fresh, version-bound independent
review is completed. The function preserves each displayed fragment and key,
but normalizes the four visible slots and supplies a brief Japanese context.
"""
from __future__ import annotations

import re

from scripts.curriculum.audit_star_permutations import parse_strict_star_stem


CONTEXTS = {
    "N2_11_M8_01": "経理部では、支払前に請求内容を確かめる手順を見直している。",
    "N2_11_M8_02": "会議では、報告の結論を早く出すべきだという意見が出た。",
    "N2_11_M8_03": "先方に説明する前に、まず事実関係を調べることになった。",
    "N2_11_M8_04": "申請書と添付された原本の数値が一致しない場合がある。",
    "N2_11_M8_05": "職場で意見が分かれたときの話し合い方が課題になっている。",
    "N2_12_M8_01": "窓口では、書類に不足があるときの案内方法を統一することになった。",
    "N2_12_M8_02": "市の広報課は、調査結果を公表する前の確認手順を決めた。",
    "N2_12_M8_03": "地域では災害に備え、各世帯が必要な準備を進めている。",
    "N2_12_M8_04": "市は、食料を買いにくい地域の住民を支援する方法を検討した。",
    "N2_12_M8_05": "複数の公共事業案について、将来の維持費も比べる方針になった。",
    "N2_13_M8_01": "研究成果を読者が検証できるよう、研究室は資料の示し方を改めた。",
    "N2_13_M8_02": "授業では、学生の理解度に合わせて説明を工夫することになった。",
    "N2_13_M8_03": "編集部は、見出しだけで記事を判断しないよう読者に呼びかけている。",
    "N2_13_M8_04": "新機能の導入に当たり、利用者への影響を事前に調べることになった。",
    "N2_13_M8_05": "編集部では、記事を公開する前に複数の資料を確認している。",
    "N2_14_M1_45": "予算案に修正が必要だと分かり、担当者は実行前に内容を再検討した。",
    "N2_14_M1_46": "講師の説明を聞いた学生は、疑問点を整理して質問することにした。",
    "N2_14_M1_47": "この制度には申込条件があり、条件を満たした人だけが手続きできる。",
    "N2_14_M1_48": "申請内容に誤りがないか、担当者が記録と照らし合わせて確認した。",
    "N2_14_M1_49": "参加者から意見を集め、内容に反映させる方法を検討している。",
}

_SLOT = re.compile(r"（[\s　]*★[\s　]*）|（[\s　]*）|★")


def _ordered_fragments(item: dict) -> list[str]:
    options = {str(row.get("id", "")).upper(): str(row.get("text", ""))
               for row in item.get("options", [])}
    labels = [label.strip().upper() for label in str(item.get("fragmentOrder", "")).split("→")]
    if len(options) != 4 or len(labels) != 4 or len(set(labels)) != 4 or set(labels) != set(options):
        raise ValueError(f"{item.get('id')}: STAR order must identify four displayed fragments")
    if options.get(str(item.get("correctAnswer", "")).upper()) != options[labels[2]]:
        raise ValueError(f"{item.get('id')}: authored key does not match the third ordered fragment")
    return [options[label] for label in labels]


def apply_phase_71_star_repairs(items: list[dict]) -> list[dict]:
    by_id = {item.get("id"): item for item in items}
    applicable = {qid: text for qid, text in CONTEXTS.items() if qid in by_id}
    mock_numbers = {item_id.split("_")[1] for item_id in by_id if item_id.startswith("N2_")}
    expected = {qid for qid in CONTEXTS
                if any(qid.startswith(f"N2_{number}_") for number in mock_numbers)}
    missing = sorted(expected - set(by_id))
    if missing:
        raise ValueError("Phase 7.1 STAR items missing from candidate: " + ", ".join(missing))

    for qid, context in applicable.items():
        item = by_id[qid]
        if item.get("typeId") != "N2-GR-STAR":
            raise ValueError(f"{qid}: refusing to apply STAR repair to a non-STAR item")
        fragments = _ordered_fragments(item)
        previous_sentence = str(item.get("assembledSentence", ""))
        item["contextPassage"] = context
        item["passage"] = context

        # M11 already has a meaningful sentence prefix/suffix in its stem.
        # Keep those boundaries and verify the complete reconstructed sentence.
        if qid.startswith("N2_11_"):
            valid, reason, parsed = parse_strict_star_stem(item.get("stem", ""))
            if not valid:
                raise ValueError(f"{qid}: invalid repaired stem: {reason}")
            matches = list(_SLOT.finditer(item["stem"]))
            sentence = item["stem"]
            for match, fragment in reversed(list(zip(matches, fragments, strict=True))):
                sentence = sentence[:match.start()] + fragment + sentence[match.end():]
            if not sentence.startswith(parsed["prefix"]) or not sentence.endswith(parsed["suffix"]):
                raise ValueError(f"{qid}: reconstructed sentence lost its stem context")
            item["assembledSentence"] = sentence
        else:
            # M12–M14's four fragments make one complete sentence. Remove the
            # instruction line and show four explicit positions; keep terminal
            # punctuation outside the selectable fragments when needed.
            joined = "".join(fragments)
            existing = str(item.get("assembledSentence", ""))
            if existing.rstrip("。") != joined.rstrip("。"):
                raise ValueError(f"{qid}: canonical sentence does not match fragment order")
            suffix = "" if joined.endswith("。") else "。"
            item["stem"] = "（　　　）（　　　）（　★　）（　　　）" + suffix
            item["assembledSentence"] = joined + suffix

        item["starPosition"] = 3
        item["starredOptionText"] = fragments[2]
        if previous_sentence and previous_sentence != item["assembledSentence"]:
            item["distractorExplanations"] = {
                option_id: str(reason).replace(previous_sentence, item["assembledSentence"])
                for option_id, reason in (item.get("distractorExplanations") or {}).items()
            }
        valid, reason, _ = parse_strict_star_stem(item["stem"])
        if not valid:
            raise ValueError(f"{qid}: repaired stem is invalid: {reason}")
    return items
