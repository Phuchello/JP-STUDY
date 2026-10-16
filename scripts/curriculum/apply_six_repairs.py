import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BANK_PATH = ROOT / "curriculum/QUESTION_BANK_EXPANDED.json"

with open(BANK_PATH, "r", encoding="utf-8") as f:
    bank = json.load(f)

repairs = {
    "N4-GR-FORM-010": {
        "stem": "天気が（　　）、明日は海へ泳ぎに行きましょう。",
        "options": [
            {"id": "A", "text": "よければ"},
            {"id": "B", "text": "いいば"},
            {"id": "C", "text": "よくて"},
            {"id": "D", "text": "よくても"}
        ],
        "correctAnswer": "A",
        "explanationVi": "Thể điều kiện chuẩn của tính từ đuôi い (いい -> よければ): nếu thời tiết đẹp thì ngày mai chúng ta hãy đi bơi biển. Phương án A là dạng chia duy nhất đúng.",
        "distractorExplanations": {
            "B": "いいば là dạng chia sai quy tắc hình thái học (tính từ đuôi い phải đổi いい thành よ- trước khi gắn ければ).",
            "C": "よくて là thể て nối tiếp trạng thái, không thể dùng để tạo mệnh đề điều kiện giả định trước lời rủ rê.",
            "D": "よくても là thể điều kiện nhượng bộ (cho dù có đẹp thì...), mâu thuẫn hoàn toàn về mặt ngữ nghĩa với lời rủ rê đi bơi biển."
        },
        "remediation": "Ôn tập thể điều kiện 〜ば của tính từ đuôi い đặc biệt (いい -> よければ).",
        "repairNotes": "Replaced ambiguous distractor 'よかったら' with morphological distractor 'いいば' and concessive 'よくても' to eliminate distractor overlap."
    },
    "N4-GR-STAR-002": {
        "stem": "来年の夏休みには、（　　）（　　） ★ （　　）行く予定です。",
        "options": [
            {"id": "A", "text": "会いに"},
            {"id": "B", "text": "北海道に"},
            {"id": "C", "text": "住んでいる"},
            {"id": "D", "text": "友達に"}
        ],
        "correctAnswer": "D",
        "assembledSentence": "来年の夏休みには、北海道に住んでいる友達に会いに行く予定です。",
        "explanationVi": "Thứ tự đúng: 来年の夏休みには、[北海道に] [住んでいる] ★[友達に] [会いに] 行く予定です. Mệnh đề định ngữ bổ nghĩa cho danh từ: 北海道に住んでいる (sống ở Hokkaido) + 友達に (cho bạn) + 会いに行く (đi gặp). Vị trí ★ (thứ 3) duy nhất là '友達に' (D).",
        "distractorExplanations": {
            "A": "Đứng ở vị trí thứ 4 tạo cụm mục đích chuyển động 会いに行く予定です.",
            "B": "Đứng ở vị trí thứ 1 làm trạng ngữ chỉ nơi chốn sau 来年の夏休みには、.",
            "C": "Đứng ở vị trí thứ 2 làm vị ngữ cho mệnh đề định ngữ bổ nghĩa cho 友達."
        },
        "remediation": "Ôn tập cấu trúc mệnh đề định ngữ và cấu trúc chỉ mục đích V-ます (bỏ ます) + に行く.",
        "repairNotes": "Re-engineered star chunks to establish a rigid syntactic dependency chain (Location -> Relative Clause -> Noun -> Purpose Verb), eliminating alternative scrambled order."
    },
    "N4-GR-STAR-006": {
        "stem": "将来自分の店を（　　）（　　） ★ （　　）一生懸命働いています。",
        "options": [
            {"id": "A", "text": "お金を"},
            {"id": "B", "text": "持つ"},
            {"id": "C", "text": "ためようと"},
            {"id": "D", "text": "ために"}
        ],
        "correctAnswer": "A",
        "assembledSentence": "将来自分の店を持つためにお金をためようと一生懸命働いています。",
        "explanationVi": "Thứ tự đúng: 将来自分の店を [持つ] [ために] ★[お金を] [ためようと] 一生懸命働いています. Cấu trúc chỉ mục đích và ý chí: 自分の店を持つ (có cửa hàng) + ために (để) + お金をためようと (với ý định tiết kiệm tiền). Vị trí ★ (thứ 3) duy nhất là 'お金を' (A).",
        "distractorExplanations": {
            "B": "Đứng ở vị trí thứ 1 đi liền sau tân ngữ 自分の店を.",
            "C": "Đứng ở vị trí thứ 4 đi liền trước động từ 一生懸命働いています.",
            "D": "Đứng ở vị trí thứ 2 hoàn thiện cấu trúc mục đích V-る + ために."
        },
        "remediation": "Ôn tập cấu trúc V-る + ために và thể ý chí V-よう + と (chỉ mục đích / dự định).",
        "repairNotes": "Replaced floating temporal adverb '今' with case-locked object noun phrase 'お金を', eliminating word order permutation ambiguity."
    },
    "N2-GR-FORM-003": {
        "stem": "伝統的な工芸技術を受け継ぐ後継者が不足し、存続が危ぶまれる技術が増加（　　）。",
        "options": [
            {"id": "A", "text": "しつつある"},
            {"id": "B", "text": "したきりだ"},
            {"id": "C", "text": "しっこない"},
            {"id": "D", "text": "しがたい"}
        ],
        "correctAnswer": "A",
        "explanationVi": "Mẫu câu chính luận N2 diễn tả tiến trình đang dần biến đổi theo thời gian: 「V-ます bỏ ます + つつある」 (đang dần dần gia tăng). Phương án A là đáp án chính xác và trang trọng nhất.",
        "distractorExplanations": {
            "B": "したきりだ diễn tả sau khi thực hiện hành động thì giữ nguyên trạng thái không biến chuyển, không phù hợp với xu hướng biến thiên 増加.",
            "C": "しっこない mang tính khẩu ngữ tuyệt đối phủ định ('tuyệt đối không thể'), mâu thuẫn hoàn toàn với thực trạng thiếu hụt nhân lực.",
            "D": "しがたい chỉ dùng với các động từ tâm lý cảm xúc (信じがたい, 理解しがたい), không kết hợp với biến đổi tự nhiên như 増加."
        },
        "remediation": "Ôn tập mẫu câu N2 diễn tả xu hướng biến đổi: 〜つつある (đang dần dần).",
        "repairNotes": "Replaced near-synonymous distractor 'する一方だ' with unambiguous grammatical distractors 'しっこない' and 'しがたい'."
    },
    "N3-GR-FORM-006": {
        "stem": "彼は昨日遅くまで残業していたから、今日は疲れている（　　）だ。",
        "options": [
            {"id": "A", "text": "こと"},
            {"id": "B", "text": "はず"},
            {"id": "C", "text": "つもり"},
            {"id": "D", "text": "もの"}
        ],
        "correctAnswer": "B",
        "explanationVi": "Mẫu câu phán đoán logic dựa trên căn cứ khách quan: 「〜はずだ」 (chắc hẳn là đang rất mệt vì hôm qua tăng ca muộn). Phương án B là đáp án duy nhất phù hợp.",
        "distractorExplanations": {
            "A": "ことだ thường dùng cho lời khuyên hoặc mệnh lệnh nhẹ nhàng mang tính đạo đức.",
            "C": "つもりだ diễn tả ý định chủ quan của bản thân hoặc niềm tin sai lệch, phi logic trong ngữ cảnh suy đoán trạng thái của người khác.",
            "D": "ものだ dùng cho chân lý hiển nhiên, quy luật tự nhiên hoặc hoài niệm quá khứ."
        },
        "remediation": "Ôn tập mẫu câu N3 phán đoán logic 〜はずだ so sánh với các danh từ hình thức khác.",
        "repairNotes": "Replaced potential overlap distractor 'わけ' with 'つもり', eliminating nuance ambiguity in causal sentence."
    },
    "N3-GR-STAR-001": {
        "stem": "年齢や経験の（　　）（　　） ★ （　　）誰でも応募できます。",
        "options": [
            {"id": "A", "text": "意欲が"},
            {"id": "B", "text": "有無に"},
            {"id": "C", "text": "あれば"},
            {"id": "D", "text": "かかわらず"}
        ],
        "correctAnswer": "A",
        "assembledSentence": "年齢や経験の有無にかかわらず意欲があれば誰でも応募できます。",
        "explanationVi": "Thứ tự đúng: 年齢や経験の [有無に] [かかわらず] ★[意欲が] [あれば] 誰でも応募できます. Cấu trúc N3: 〜にかかわらず (bất kể có hay không) + 意欲があれば (nếu có ý chí quyết tâm) + 誰でも応募できます. Vị trí ★ (thứ 3) duy nhất là '意欲が' (A).",
        "distractorExplanations": {
            "B": "Đứng ở vị trí thứ 1 ngay sau cụm danh từ 年齢や経験の.",
            "C": "Đứng ở vị trí thứ 4 nối vào mệnh đề chính 誰でも応募できます.",
            "D": "Đứng ở vị trí thứ 2 hoàn thiện mẫu câu ngữ pháp N3 有無にかかわらず."
        },
        "remediation": "Ôn tập cấu trúc N3 〜にかかわらず (bất kể) kết hợp với điều kiện 〜ば.",
        "repairNotes": "Replaced movable quantifier/adverb pair (誰でも/自由に) with locked conditional clause (意欲があれば), locking slot 3 to option A."
    }
}

diff_log = []

for q in bank["questions"]:
    qid = q["id"]
    if qid in repairs:
        before = {
            "id": qid,
            "stem": q["stem"],
            "options": q["options"],
            "correctAnswer": q["correctAnswer"],
            "assembledSentence": q.get("assembledSentence"),
            "explanationVi": q.get("explanationVi"),
            "distractorExplanations": q.get("distractorExplanations")
        }
        rep = repairs[qid]
        q["stem"] = rep["stem"]
        q["options"] = rep["options"]
        q["correctAnswer"] = rep["correctAnswer"]
        if "assembledSentence" in rep:
            q["assembledSentence"] = rep["assembledSentence"]
        q["explanationVi"] = rep["explanationVi"]
        q["distractorExplanations"] = rep["distractorExplanations"]
        q["remediation"] = rep["remediation"]
        q["status"] = "INDEPENDENT_REVIEW_PENDING"  # Needs fresh review because question materially changed!
        if "independentReview" in q:
            q["historicalReview"] = q.pop("independentReview")  # Preserve versioned historical evidence!
        
        after = {
            "id": qid,
            "stem": q["stem"],
            "options": q["options"],
            "correctAnswer": q["correctAnswer"],
            "assembledSentence": q.get("assembledSentence"),
            "explanationVi": q.get("explanationVi"),
            "distractorExplanations": q.get("distractorExplanations"),
            "repairNotes": rep["repairNotes"]
        }
        diff_log.append({"id": qid, "before": before, "after": after})

with open(BANK_PATH, "w", encoding="utf-8") as f:
    json.dump(bank, f, ensure_ascii=False, indent=2)

DIFF_PATH = ROOT / "qa/flagged_questions_diff.json"
with open(DIFF_PATH, "w", encoding="utf-8") as f:
    json.dump(diff_log, f, ensure_ascii=False, indent=2)

print(f"Repaired {len(diff_log)} questions and wrote diff log to {DIFF_PATH}")

# Also generate blind dataset for these 6 repaired questions
BLIND_6_PATH = ROOT / "qa/blind_review_repaired_6.json"
blind_items = []
for q in bank["questions"]:
    if q["id"] in repairs:
        blind_items.append({
            "id": q["id"],
            "level": q["level"],
            "skill": q["skill"],
            "typeId": q["typeId"],
            "stem": q["stem"],
            "contextPassage": q.get("contextPassage"),
            "options": q["options"]
        })

with open(BLIND_6_PATH, "w", encoding="utf-8") as f:
    json.dump(blind_items, f, ensure_ascii=False, indent=2)

print(f"Exported {len(blind_items)} blind items to {BLIND_6_PATH}")
