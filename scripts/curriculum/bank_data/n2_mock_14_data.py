# -*- coding: utf-8 -*-
"""Original comprehensive-challenge N2 items; authored source for M14 draft."""
from __future__ import annotations

import random
from scripts.curriculum.bank_data.n2_mock_14_explanations_vi import apply_vietnamese_explanations
from scripts.curriculum.phase_71_star_repairs import apply_phase_71_star_repairs

LETTERS = "ABCD"


def _item(qid, type_id, category, stem, choices, key_index, explanation_vi,
          *, topic="comprehensive-challenge", difficulty=2, context=None,
          target=None, distractor_notes=None):
    if len(choices) != 4 or not 0 <= key_index < 4:
        raise ValueError(f"Invalid M14 item: {qid}")
    order = list(range(4))
    _rng.shuffle(order)
    options = [{"id": LETTERS[display], "text": choices[source]}
               for display, source in enumerate(order)]
    key = LETTERS[order.index(key_index)]
    notes = distractor_notes or {}
    distractors = {}
    for option in options:
        if option["id"] == key:
            continue
        distractors[option["id"]] = notes.get(
            choices.index(option["text"]),
            f"Trong ngữ cảnh này, «{option['text']}» không khớp với manh mối cần tìm. {explanation_vi}",
        )
    return {
        "id": qid, "level": "N2", "typeId": type_id, "category": category,
        "stem": stem, "options": options, "correctAnswer": key,
        "explanation": f"正解は「{choices[key_index]}」です。",
        "explanationVi": explanation_vi,
        "distractorExplanations": distractors,
        "topicTag": topic, "difficultyBand": difficulty,
        "distractorStrategy": "意味・文脈・文法形式の対比",
        "skill": "Language Knowledge",
        **({"contextPassage": context, "passage": context} if context else {}),
        **({"targetKanji": target} if target else {}),
    }


def _star(qid, fragments, key_order, explanation_vi, topic="comprehensive-challenge"):
    if len(fragments) != 4 or sorted(key_order) != [0, 1, 2, 3]:
        raise ValueError(f"Invalid M14 STAR item: {qid}")
    sentence = "".join(fragments[i] for i in key_order)
    order = list(range(4))
    _rng.shuffle(order)
    options = [{"id": LETTERS[pos], "text": fragments[index]} for pos, index in enumerate(order)]
    displayed_for_fragment = {fragments[fragment]: LETTERS[pos] for pos, fragment in enumerate(order)}
    key_fragment = fragments[key_order[2]]
    key = displayed_for_fragment[key_fragment]
    return {
        "id": qid, "level": "N2", "typeId": "N2-GR-STAR", "category": "文の組み立て",
        "stem": "次の文を完成させるとき、★に入る部分はどれか。\n（　　）（　　）★（　　）",
        "options": options, "correctAnswer": key,
        "explanation": "四つの部分を自然な係り受けに沿って並べます。",
        "explanationVi": explanation_vi,
        "distractorExplanations": {
            option["id"]: f"Cụm «{option['text']}» không nằm ở vị trí ★ trong câu hoàn chỉnh: {sentence}。 {explanation_vi}"
            for option in options if option["id"] != key
        },
        "topicTag": topic, "difficultyBand": 2,
        "assembledSentence": sentence, "starredOptionText": key_fragment,
        "starPosition": 3,
        "fragmentOrder": "→".join(displayed_for_fragment[fragments[i]] for i in key_order),
        "starValidationSchema": "DISPLAYED_FRAGMENT_ORDER_V1",
        "distractorStrategy": "語順・係り受け", "skill": "Language Knowledge",
    }


def get_n2_mock_14_sec1_items(seed=202614):
    global _rng
    _rng = random.Random(seed)
    q = []

    # Kanji reading: 5
    rows = [
        ("その変更によって、現場の混乱が【緩和】された。", ["かんわ", "かんね", "ゆるわ", "かんわい"], 0, "緩和（かんわ）は、厳しさや緊張をやわらげることです。変更後に混乱が軽くなったという文脈に合います。", "緩和"),
        ("担当者は、利用者の意見を【踏まえて】計画を修正した。", ["ふまえて", "ふんまえて", "ふみえて", "ふまわえて"], 0, "踏まえる（ふまえる）は、事実や意見を考慮に入れることです。利用者の意見をもとに計画を直した場面です。", "踏まえて"),
        ("雨が続いても、試合の開催に大きな【支障】はなかった。", ["ししょう", "しじょう", "ささえ", "しそう"], 0, "支障（ししょう）は、物事を進めるうえでの妨げです。ここでは雨が開催を妨げなかったと述べています。", "支障"),
        ("この制度は、複数の条件を満たす場合に【適用】される。", ["てきよう", "てきおう", "てつよう", "できよう"], 0, "適用（てきよう）は、決まりや制度を特定の事例に当てはめることです。条件を満たす人に制度を使う文脈です。", "適用"),
        ("結論を急がず、別の可能性も【考慮】する必要がある。", ["こうりょ", "こうろ", "けいりょ", "こうじょ"], 0, "考慮（こうりょ）は、事情や可能性を考えに入れることです。複数の可能性を検討する文に合います。", "考慮"),
    ]
    for i, (stem, options, key, vi, target) in enumerate(rows, 1):
        q.append(_item(f"N2_14_M1_{i:02}", "N2-MO-READ", "漢字読み", stem, options, key, vi, difficulty=2, target=target))

    # Orthography: 5
    rows = [
        ("新しい制度の導入には、関係者の【しょうにん】が必要だ。", ["承認", "証人", "招待", "昇任"], 0, "しょうにん ở đây là 承認, tức sự chấp thuận chính thức. Câu nói về việc những người liên quan đồng ý cho áp dụng chế độ mới."),
        ("災害に備えて、避難所の場所を事前に【かくにん】しておこう。", ["確認", "確信", "革新", "各人"], 0, "かくにん là 確認, nghĩa là kiểm tra để chắc chắn. Câu khuyên kiểm tra trước vị trí nơi sơ tán."),
        ("担当者は、変更点を参加者全員に【つたえた】。", ["伝えた", "訪えた", "達えた", "移えた"], 0, "つたえた được viết là 伝えた, dạng quá khứ của 伝える (truyền đạt). Các đáp án còn lại không tạo thành cách viết đúng của động từ này."),
        ("限られた予算の中で、必要な人員を【はいち】した。", ["配置", "配達", "排置", "廃止"], 0, "はいち là 配置, nghĩa là sắp xếp hoặc bố trí người, vật vào vị trí cần thiết. Câu nói về phân công nhân lực."),
        ("発表の前に、資料の数字をもう一度【みなおした】。", ["見直した", "見逃した", "見守った", "見渡した"], 0, "みなおした là 見直した, nghĩa là xem xét lại. Người nói kiểm tra lại số liệu trước khi trình bày."),
    ]
    for i, (stem, options, key, vi) in enumerate(rows, 6):
        q.append(_item(f"N2_14_M1_{i:02}", "N2-MO-ORTH", "表記", stem, options, key, vi, difficulty=2))

    # Word formation: 5
    rows = [
        ("作業を標準化した結果、手続きが以前より【　】化した。", ["簡素", "複雑", "不足", "慎重"], 0, "簡素化する là làm cho đơn giản hơn. Việc chuẩn hóa quy trình khiến thủ tục bớt phức tạp; 複雑化 mang nghĩa ngược lại."),
        ("会場が遠いため、受付を駅前にも【　】した。", ["設置", "設問", "設計", "設定"], 0, "受付を設置する là bố trí quầy tiếp nhận ở một địa điểm. 設問 là câu hỏi; 設計 là thiết kế; 設定 là cài đặt hoặc thiết lập."),
        ("この資料は専門家向けなので、一般向けに内容を【　】する必要がある。", ["要約", "予想", "応援", "延期"], 0, "要約する là tóm tắt các ý chính. Câu yêu cầu chuyển tài liệu chuyên ngành thành nội dung ngắn gọn cho công chúng."),
        ("費用を正確に比べるため、条件をそろえて【　】した。", ["比較", "競争", "交際", "交換"], 0, "比較する là so sánh các phương án theo cùng điều kiện. 競争 là cạnh tranh giữa các bên, không phải thao tác cần nêu ở đây."),
        ("担当者を二人に増やし、問い合わせへの対応を【　】化した。", ["迅速", "平等", "安全", "豊富"], 0, "迅速化する là làm cho nhanh hơn. Tăng nhân sự nhằm rút ngắn thời gian phản hồi, phù hợp với mục tiêu này."),
    ]
    for i, (stem, options, key, vi) in enumerate(rows, 11):
        q.append(_item(f"N2_14_M1_{i:02}", "N2-MO-FORM", "語形成", stem, options, key, vi, difficulty=2))

    # Contextually defined expressions: 7
    rows = [
        ("複数の部署にまたがる問題なので、一つの課だけで判断せず、関係者と【　】を取った。", ["連絡", "記録", "距離", "速度"], 0, "関係者と連絡を取る là liên hệ và trao đổi với những người liên quan. Vấn đề đi qua nhiều bộ phận nên cần phối hợp trước khi quyết định."),
        ("会場が閉まる予定時刻を少し【　】ため、退館が遅れたことを職員に謝った。", ["過ぎた", "逃した", "延ばした", "譲った"], 0, "時刻を過ぎる là thời điểm đã muộn hơn giờ dự kiến. Vì ra về sau giờ đóng cửa nên người nói xin lỗi nhân viên."),
        ("申請書に記入漏れがあったため、窓口でその場で【　】した。", ["補った", "支えた", "抱えた", "備えた"], 0, "記入漏れを補う là điền bổ sung phần còn thiếu. Các động từ khác không diễn tả việc thêm thông tin vào biểu mẫu."),
        ("利用者の希望をすべてかなえるのは難しいが、優先順位をつけて【　】したい。", ["対応", "対立", "対照", "対面"], 0, "対応する là xử lý hoặc đáp ứng một yêu cầu. Câu nói về việc sắp xếp ưu tiên để giải quyết mong muốn của người dùng."),
        ("参加者が少ない場合は、開催方法を変えることも【　】に入れている。", ["視野", "視線", "視点", "視力"], 0, "視野に入れる là tính đến hoặc xem một lựa chọn như khả năng có thể cân nhắc. Câu đang nói về phương án tổ chức thay thế."),
        ("資料の数字だけを見ると増加しているようだが、前年の条件も【　】する必要がある。", ["考慮", "想像", "感謝", "期待"], 0, "考慮する là đưa yếu tố vào quá trình đánh giá. So sánh số liệu cần xét điều kiện của năm trước, không chỉ nhìn con số hiện tại."),
        ("申込者数が定員に達したので、募集を予定より早く【　】ことになった。", ["締め切る", "取り組む", "受け取る", "引き受ける"], 0, "募集を締め切る là dừng nhận đăng ký. Vì số người đã đạt giới hạn nên không thể tiếp tục nhận thêm."),
    ]
    for i, (stem, options, key, vi) in enumerate(rows, 16):
        q.append(_item(f"N2_14_M1_{i:02}", "N2-MO-CONT", "文脈規定", stem, options, key, vi, difficulty=2))

    # Paraphrases: 5
    rows = [
        ("彼の説明は要点を押さえていた。", ["必要な点を正確に捉えていた", "細部をすべて省いていた", "話題を次々に変えていた", "結論を最後まで隠していた"], 0, "要点を押さえる nghĩa là nắm đúng những điểm chính. Đáp án 1 diễn đạt lại ý này; các lựa chọn khác nói về lược bỏ, đổi chủ đề hoặc giấu kết luận."),
        ("この案は現実的とは言いにくい。", ["実行できる可能性が高いとは言えない", "費用をかけずに実現できる", "すでに多くの人が実行した", "以前の案より具体的である"], 0, "現実的とは言いにくい là khó xem là có thể thực hiện trong thực tế. Đáp án 1 giữ đúng sắc thái dè dặt của câu."),
        ("問題の原因を突き止めた。", ["原因が何かを明らかにした", "問題を一時的に隠した", "原因を別の人に伝えた", "起きる前に問題を防いだ"], 0, "突き止める nghĩa là điều tra đến khi xác định được sự thật hoặc nguyên nhân. Đáp án 1 là cách nói tương đương."),
        ("申し込みは先着順で受け付けます。", ["早く申し込んだ人から順に受け付けます", "抽選で当たった人だけ受け付けます", "申し込みの遅い人を優先します", "全員の申し込みを同時に確認します"], 0, "先着順 là theo thứ tự người đến hoặc đăng ký trước được xử lý trước. Đáp án 1 giải thích đúng thứ tự đó."),
        ("雨天の場合は、イベントを延期する。", ["別の日に改めて行う", "予定どおり屋外で実施する", "内容を短くして当日行う", "参加者を半分に減らす"], 0, "延期する là dời sang thời điểm khác. Đáp án 1 nói sự kiện sẽ được tổ chức lại vào ngày khác."),
    ]
    for i, (stem, options, key, vi) in enumerate(rows, 23):
        q.append(_item(f"N2_14_M1_{i:02}", "N2-MO-PARA", "言い換え", stem, options, key, vi, difficulty=2))

    # Usage: 5, choose the sentence where the target word is used naturally.
    rows = [
        ("見込む", ["来月の利用者数は、現在より一割ほど増えると見込まれている。", "人事部は、若手社員の力を見込んで新しい業務を任せた。", "彼女は相手の経験を見込んで、細かな説明を省いた。", "展望台から谷を見込むと、遠くに集落が見えた。"], 0, "Ở đây, 見込む mang nghĩa dự đoán số lượng hoặc kết quả trong tương lai. Câu 1 dự báo lượng người sử dụng tăng; câu 2 và 3 dùng theo nghĩa đánh giá năng lực, còn câu 4 là nhìn xuống thung lũng."),
        ("妥当", ["費用と効果を考えれば、この価格設定は妥当だと思う。", "担当者は、資料の誤りを妥当に直してから再提出した。", "式典の雰囲気に妥当な服装を選んだ。", "説明の妥当を確かめるため、別の資料と比べた。"], 0, "妥当 chỉ nhận định một điều hợp lý khi xét căn cứ và điều kiện. Câu 1 đánh giá giá bán dựa trên chi phí và hiệu quả. Các câu còn lại dùng không tự nhiên: sửa sai thường nói 適切に直す, trang phục thường là ふさわしい, còn danh từ cần dạng 妥当性."),
        ("見合わせる", ["安全が確認できるまで、運行を見合わせます。", "二つの見積書を見合わせて、金額が違う箇所を調べた。", "会議の冒頭、二人は顔を見合わせてから発言した。", "駅で旧友と顔を見合わせ、近況を話した。"], 0, "Câu 1 dùng 見合わせる với nghĩa tạm dừng vận hành cho đến khi xác nhận an toàn. 見積書を見合わせる là đối chiếu tài liệu; 顔を見合わせる nghĩa là nhìn nhau."),
        ("余裕", ["予定より早く着いたので、出発まで時間に余裕がある。", "彼は厳しい質問にも心の余裕を失わずに答えた。", "相手を安心させるため、彼女は余裕のある表情を見せた。", "意見が対立しても、部長は余裕のある態度を崩さなかった。"], 0, "Câu 1 nói còn thời gian rảnh trước giờ khởi hành. Các câu khác dùng 余裕 theo nghĩa bình tĩnh, thoải mái về tinh thần hoặc thái độ, không phải khoảng thời gian còn lại."),
        ("負担", ["手続きが簡単になり、利用者の負担が軽くなった。", "出張に必要な交通費は会社が負担する。", "会場の準備にかかった費用を主催者側が負担した。", "彼は重い荷物の一部を交代で負担した。"], 0, "負担 ở câu 1 là công sức và phiền hà mà người dùng phải chịu khi làm thủ tục. Các câu khác nói đến việc chi trả chi phí hoặc gánh phần tải trọng vật lý."),
    ]
    for i, (word, options, key, vi) in enumerate(rows, 28):
        meaning = {
            "見込む": "将来の数量・結果を予測する",
            "妥当": "根拠や条件に照らして無理がない",
            "見合わせる": "事情が解決するまで一時的に止める",
            "余裕": "予定時刻までに使える時間が残っている",
            "負担": "利用者が行う手間や労力",
        }[word]
        q.append(_item(f"N2_14_M1_{i:02}", "N2-MO-USE", "用法", f"次の文の【{word}】を「{meaning}」という意味で使っているものはどれか。", options, key, vi, difficulty=2))

    # Sentence grammar: 12
    rows = [
        ("十分な説明を受けた【　】、利用者が内容を誤解することもある。", ["にもかかわらず", "とともに", "を通じて", "に応じて"], 0, "にもかかわらず diễn tả sự trái ngược với điều được mong đợi: dù đã được giải thích đầy đủ nhưng vẫn có người hiểu sai."),
        ("関係者の意見を聞いた【　】、最終的な方針を決める。", ["うえで", "ところで", "ばかりで", "どころか"], 0, "Vたうえで là sau khi hoàn thành bước trước rồi mới làm bước sau. Câu đặt việc nghe ý kiến trước quyết định."),
        ("資料を公開する【　】、個人情報が含まれていないか確認してください。", ["にあたって", "に限って", "に比べて", "に反して"], 0, "N/Vるにあたって nghĩa là nhân dịp hoặc trước khi bắt đầu một việc quan trọng. Cần kiểm tra thông tin trước lúc công khai tài liệu."),
        ("この方法は費用が安い【　】、準備に時間がかかる。", ["一方で", "ばかりか", "だけに", "に先立ち"], 0, "一方で nối hai mặt tương phản của cùng một phương pháp: chi phí thấp nhưng chuẩn bị lâu."),
        ("本人の希望を確認せずに決める【　】。", ["わけにはいかない", "にすぎない", "ことになっている", "にほかならない"], 0, "わけにはいかない diễn tả điều không thể làm vì lý do trách nhiệm hoặc lẽ thường. Không thể quyết định thay khi chưa hỏi người đó."),
        ("予定が変わる可能性がある【　】、参加者には前日に連絡する。", ["ことから", "ことには", "ことなく", "ことだから"], 0, "ことから nêu căn cứ dẫn tới hành động. Vì lịch có thể đổi nên ban tổ chức sẽ thông báo trước một ngày."),
        ("説明の順番を工夫した【　】、初めての人にも理解しやすくなった。", ["おかげで", "せいで", "ものの", "ところを"], 0, "おかげで chỉ kết quả tích cực nhờ một nguyên nhân. Cách sắp xếp tốt giúp người mới hiểu dễ hơn."),
        ("担当者が不在の場合は、窓口ではなくメールで問い合わせる【　】。", ["ようにしてください", "ことにしました", "しかありません", "はずでした"], 0, "ようにしてください dùng để hướng dẫn hoặc yêu cầu người nghe thực hiện một cách làm. Câu là hướng dẫn liên hệ khi người phụ trách vắng mặt."),
        ("参加者が増えた【　】、会場を広い部屋に変更した。", ["ため", "ものの", "ところ", "ほど"], 0, "ため nêu nguyên nhân. Số người tăng dẫn đến việc đổi sang phòng lớn hơn."),
        ("この規則は、すべての利用者に例外なく適用される【　】。", ["ことになっている", "ことにしている", "ことがある", "ことはない"], 0, "ことになっている diễn tả quy định hoặc quyết định đã được đặt ra. Đây là quy tắc áp dụng cho tất cả người dùng."),
        ("一度引き受けた仕事だから、最後まで責任を持ってやり【　】。", ["ぬく", "きる", "かける", "なおす"], 0, "やりぬく là kiên trì làm đến cùng. Câu nhấn mạnh trách nhiệm hoàn thành việc đã nhận."),
        ("結論を出すには、もう少し情報を集めてからでないと判断し【　】。", ["かねる", "がたい", "かける", "おえる"], 0, "判断しかねる nghĩa là khó hoặc chưa thể đưa ra phán đoán trong tình trạng thiếu thông tin. Cấu trúc phù hợp với ý cần thu thập thêm dữ liệu."),
    ]
    for i, (stem, options, key, vi) in enumerate(rows, 33):
        q.append(_item(f"N2_14_M1_{i:02}", "N2-GR-FORM", "文法形式", stem, options, key, vi, difficulty=3))

    # STAR arrangement: 5
    stars = [
        (["予算を", "見直した", "うえで", "計画を実行した"], [0, 1, 2, 3], "Câu hoàn chỉnh là 予算を見直したうえで計画を実行した. ★ là うえで, nối việc rà soát ngân sách với hành động triển khai kế hoạch."),
        (["説明を", "聞いた", "から", "質問することにした"], [0, 1, 2, 3], "Câu hoàn chỉnh là 説明を聞いたから質問することにした (nghe giải thích rồi mới quyết định hỏi). ★ nằm ở cụm から, nối nguyên nhân hoặc căn cứ với quyết định."),
        (["条件を", "満たしている", "場合に", "申し込める"], [0, 1, 2, 3], "Câu hoàn chỉnh là 条件を満たしている場合に申し込める. ★ là 場合に, đứng sau mệnh đề điều kiện và trước khả năng đăng ký."),
        (["担当者が", "記録を調べた", "ところ", "申請の誤りに気づいた"], [0, 1, 2, 3], "Câu hoàn chỉnh là 担当者が記録を調べたところ申請の誤りに気づいた. ところ nối hành động kiểm tra với kết quả được phát hiện sau đó; cụm này đứng ở vị trí ★ thứ ba."),
        (["参加者の", "意見を", "参考にしながら", "内容を整えた"], [0, 1, 2, 3], "Câu hoàn chỉnh là 参加者の意見を参考にしながら内容を整えた. ★ là 参考にしながら, nối căn cứ tham khảo với hành động chỉnh sửa."),
    ]
    for i, (fragments, order, vi) in enumerate(stars, 45):
        q.append(_star(f"N2_14_M1_{i:02}", fragments, order, vi))

    # Text grammar: one short coherent passage with five distinct links.
    text = (
        "地域の避難訓練を見直すことになった。これまでは毎年同じ内容を繰り返していたが、参加者の年齢や経験が異なる【　1　】、"
        "同じ説明だけでは十分でないという声が出ていた。そこで、初参加の人には基本的な手順を案内する【　2　】、"
        "経験のある人には実際の避難経路を確認してもらうことにした。訓練の後には感想を集め、次回の内容に反映する【　3　】。"
        "意見がすべて一致するとは限らないが、安全に関わる指摘は小さなもの【　4　】記録に残す。"
        "参加しやすい方法を探り【　5　】、訓練を地域の実情に近づけていく方針だ。"
    )
    text_rows = [
        ("参加者の年齢や経験が異なる【　1　】、同じ説明だけでは十分でないという声が出ていた。", ["ことから", "ものなら", "ことなく", "からには"], 0, "ことから nêu căn cứ cho nhận xét phía sau: vì độ tuổi và kinh nghiệm khác nhau nên cách giải thích giống nhau chưa đủ."),
        ("初参加の人には基本的な手順を案内する【　2　】、経験のある人には実際の避難経路を確認してもらう。", ["一方で", "ばかりに", "どころか", "あげく"], 0, "一方で đặt hai nhóm song song nhưng được hỗ trợ theo cách khác nhau: người mới học quy trình, người có kinh nghiệm kiểm tra đường đi."),
        ("感想を集め、次回の内容に反映する【　3　】。", ["ことにした", "わけではない", "にすぎない", "ものがある"], 0, "ことにした diễn tả quyết định của người tổ chức sau khi xem xét nhu cầu cải tiến."),
        ("安全に関わる指摘は小さなもの【　4　】記録に残す。", ["であっても", "にしては", "としても", "にとって"], 0, "であっても nhấn mạnh rằng dù nhận xét nhỏ đến đâu thì nếu liên quan an toàn vẫn phải ghi lại."),
        ("参加しやすい方法を探り【　5　】、訓練を地域の実情に近づけていく。", ["ながら", "次第", "きり", "つつも"], 0, "Vます bỏ ます + ながら diễn tả hai hoạt động song song: vừa tìm cách dễ tham gia vừa điều chỉnh nội dung theo thực tế."),
    ]
    for i, (stem, options, key, vi) in enumerate(text_rows, 50):
        q.append(_item(f"N2_14_M1_{i:02}", "N2-GR-PARA", "文章文法", stem, options, key, vi, difficulty=3, context=text))

    # Reading: 21, with shared passages only where the question set is designed to do so.
    short = [
        ("市民ホールの会議室は、予約日の一か月前から申し込めます。営利を目的とする利用は料金が異なります。予約後に日時を変更する場合は、利用日の三日前までに窓口へ連絡してください。", "日時を変更したい人は、いつまでに連絡すればよいか。", ["利用日の三日前まで", "予約日の一か月前まで", "利用日の翌日まで", "営利利用の申請と同時に"], 0, "使用者は利用日の三日前までに窓口へ連絡して日時変更を申し出ます。1か月前は予約開始時期であり、変更期限ではありません。"),
        ("新しい相談窓口では、相談内容を詳しく書く必要はありません。予約時には希望日時と連絡方法だけを選んでください。すぐに対応が必要な場合は、予約フォームではなく電話を利用してください。", "予約フォームに入力する内容として正しいものはどれか。", ["希望日時と連絡方法", "相談の経緯をすべて記した文章", "緊急相談の理由と証明書", "担当者の名前と電話番号"], 0, "通常予約では希望日時と連絡方法だけを選ぶとあります。詳しい事情は不要で、緊急の場合は電話を使うと区別されています。"),
        ("展示会の入場は無料だが、体験コーナーは材料費として一人二百円かかる。小学生以下は保護者と一緒に参加すること。会場内では撮影できるが、作品に触れることはできない。", "正しいものはどれか。", ["体験コーナーでは材料費が必要だ", "展示会に入るには必ず予約がいる", "子どもだけで体験に参加できる", "作品は自由に手に取ってよい"], 0, "展示の入場は無料でも、体験コーナーは200円です。小学生以下には保護者が必要で、作品には触れられません。"),
        ("図書の返却期限は、休館日に当たる場合、次の開館日まで延長されます。ただし、予約者がいる本は返却期限を延ばせません。返却ポストは休館日も利用できますが、CDや大型本は入れないでください。", "返却期限を延ばせないのはどの本か。", ["次の利用者が予約している本", "休館日に期限を迎える本", "返却ポストに入る大きさの本", "CDと一緒に借りた本"], 0, "予約者がいる本だけは延長できないと明記されています。休館日に期限が来た場合は通常、次の開館日まで延長されます。"),
        ("講演の録画は、開催後一週間だけ会員ページで視聴できます。資料のダウンロードはできませんが、引用したい箇所を個人の学習ノートに書き写すことは認められています。", "講演後にできることはどれか。", ["録画を一週間視聴する", "講演資料を自由に配布する", "録画を永久に保存する", "ノートへの書き写しを禁止する"], 0, "会員ページの録画は開催後1週間視聴できます。資料のダウンロードは不可ですが、学習ノートへの引用箇所の書き写しは認められています。"),
    ]
    for i, (passage, stem, options, key, vi) in enumerate(short, 55):
        q.append(_item(f"N2_14_M1_{i:02}", "N2-RD-SHORT", "短文読解", stem, options, key, vi, difficulty=2, context=passage))

    medium_passages = [
        "職場では、会議の時間を短くするために、議題を事前に共有する取り組みが広がっている。資料を早く読める人ばかりではないため、送るだけで準備が済んだと考えるのは危険だ。議題ごとに「決めたいこと」と「共有だけのこと」を分け、資料には読む順番や確認箇所を添えると、参加者は必要な準備をしやすい。会議中も、すべての情報を説明するのではなく、意見を決める場面に時間を使える。準備の負担を増やさず、議論の目的をそろえる工夫が必要だ。",
        "駅前の商店街では、空き店舗を一時的に使う「お試し出店」が行われている。店を開きたい人は、短期間営業して客の反応や必要な設備を確かめられる。商店街側にも、長期契約の前に営業の様子を見られる利点がある。一方、短期であることを理由に、出店者が地域との関係づくりを後回しにすると、終了後に活動が続かない。販売の結果だけで判断せず、近隣への説明や地元の行事への参加も含めて、地域に合う形を探ることが期待されている。",
        "自治体の防災情報は、近年、ウェブサイトやアプリから受け取れるようになった。しかし、情報の発信方法を増やすだけでは、必要な人に届くとは限らない。通信環境が弱い地域の人や、通知を多く受け取って見なくなった人もいる。紙の掲示や地域の連絡網を残しつつ、避難所で更新時刻を明示するなど、複数の経路で同じ情報を確かめられるようにすることが大切だ。どの媒体が便利かは、年齢だけでなく生活時間や住む場所によっても違う。",
    ]
    medium_items = [
        [("会議前の資料共有について、筆者が注意していることは何か。", ["資料を送れば参加者の準備が終わったと考えない", "会議中にすべての資料を読み上げる", "議題の決定事項を会議後に初めて知らせる", "資料を作らずに会議の時間を増やす"], 0, "筆者は、資料を送付するだけで全員が準備できるとは限らないと指摘しています。読む順や確認点を示し、議論の目的を共有する必要があります。"),
         ("筆者が会議時間を有効に使うために勧めていることは何か。", ["決める議題と情報共有の議題を分ける", "参加者全員に同じ意見を求める", "事前資料を会議中に配る", "意見の違いを議事録から消す"], 0, "「決めたいこと」と「共有だけのこと」を分けると、会議で決定に必要な意見交換へ時間を使えます。"),
         ("筆者の考えに合うものはどれか。", ["準備の手間を考えたうえで議論の目的をそろえる", "資料の量を増やすほど会議は短くなる", "事前共有は参加者の読解力をそろえる", "会議は説明だけに使うべきだ"], 0, "資料の送り方と参加者の準備負担を工夫し、会議では議論の目的を合わせるという主張です。" )],
        [("お試し出店を行う利点として、本文に合うものはどれか。", ["出店者は客の反応を確かめ、商店街側も営業を見られる", "長期契約を結ばずに必ず売上を増やせる", "近隣への説明や地域活動を省略できる", "空き店舗を恒久的に無料で利用できる"], 0, "短期営業を通じ、出店者は需要や設備を確かめ、商店街側は契約前に営業の様子を見られます。売上保証や無料利用は書かれていません。"),
         ("筆者が、短期出店でも大切だと考えていることは何か。", ["近隣への説明や地域との関係づくり", "短期間で契約を終える準備", "販売結果だけを使った評価", "行事と店の営業を完全に分けること"], 0, "活動を継続するには、販売実績だけでなく、近隣説明や地域行事への参加など関係づくりが重要だと述べています。"),
         ("商店街の取り組みについて、筆者が期待していることは何か。", ["地域に合った営業の形を探ること", "出店者に長期契約を義務づけること", "どの地域でも同じ店を誘致すること", "短期出店を売上だけで終了させること"], 0, "出店者と地域の関係も見ながら、地域に合う形を探ることが期待されています。" )],
        [("筆者が指摘する、防災情報の問題は何か。", ["媒体を増やしても必要な人に届くとは限らない", "紙の情報はデジタル情報より常に遅い", "高齢者はどの情報も受け取れない", "避難所では情報を更新できない"], 0, "情報媒体の追加だけでは、通信環境や通知疲れなどの理由で届かない人がいるという問題です。"),
         ("複数の経路で情報を確かめられるようにするのはなぜか。", ["生活環境によって利用しやすい媒体が異なるから", "すべての住民が同じアプリを使うから", "紙の掲示を法律でなくす必要があるから", "更新時刻を示すと情報が減るから"], 0, "使いやすい媒体は年齢だけでなく生活時間や場所でも違います。複数の経路で同じ情報を確かめられる設計が必要です。"),
         ("筆者の意見に最も近いものはどれか。", ["デジタルと従来の連絡手段を組み合わせる", "新しいアプリを作れば周知は十分だ", "年齢だけで媒体を決めればよい", "避難所に届く情報は更新しなくてよい"], 0, "アプリなどに一本化せず、紙や地域連絡も残し、避難所で更新時刻を示す組み合わせを勧めています。" )],
    ]
    for pidx, questions in enumerate(medium_items):
        for qidx, (stem, options, key, vi) in enumerate(questions):
            n = 60 + pidx * 3 + qidx
            q.append(_item(f"N2_14_M1_{n:02}", "N2-RD-MED", "中文読解", stem, options, key, vi, difficulty=2 + (qidx == 2), context=medium_passages[pidx]))

    # Comparative reading: two short documents, one question each.
    pair_passage = (
        "【A】市立図書館は、来月から平日の開館を午後八時まで延長する。利用者アンケートでは、仕事や授業の後に資料を受け取りたいという声が多かったためだ。人員の都合で、延長時間は貸出と返却を中心とし、相談カウンターは午後六時に閉まる。\n\n"
        "【B】隣町の図書館は、週二回だけ午後九時まで開館している。遅い時間も調べものの相談を受ける一方、夜間は職員が少ないため、予約のない資料は書庫から出せない。利用者には、必要な本を前日までに予約するよう案内している。"
    )
    q.append(_item("N2_14_M1_69", "N2-RD-PAIR", "統合理解", "AとBの図書館について、正しいものはどれか。", ["Aは延長時間の相談カウンターを閉める", "Bは毎日午後九時まで開館する", "Aでは延長時間に書庫の本を自由に探せる", "Bでは夜間に調べものの相談ができない"], 0, "Aは午後8時まで開館しますが、相談カウンターは18時に閉まります。Bの夜間相談は可能ですが、週2回のみで、書庫の資料には事前予約が必要です。", difficulty=3, context=pair_passage))
    q.append(_item("N2_14_M1_70", "N2-RD-PAIR", "統合理解", "夜間に図書館を利用する人が事前にしておくとよいことは何か。", ["Bで必要な書庫資料を前日までに予約する", "Aで相談カウンターを午後八時に訪ねる", "Bで職員に書庫を自由に開けてもらう", "Aで貸出を午後六時までに終える"], 0, "Bは夜間に職員が少なく、予約のない書庫資料を出せません。必要な本を前日までに予約するよう案内されています。", difficulty=3, context=pair_passage))

    long_passage = (
        "自治体が新しい公共施設を計画するとき、利用者数や建設費だけでなく、完成後に誰が運営するかも早い段階で考える必要がある。建物を造る計画は目に見えやすく、予算や日程も決めやすい。しかし、運営費や人員が不足すると、開館日を減らしたり、設備を十分に活用できなかったりする。\n\n"
        "そこで、ある市では、施設の基本設計に入る前に、地域団体、利用者、職員が一緒に「どんな活動を、どの時間帯に行うか」を整理した。最初の会合では要望が多く、意見がまとまらなかった。市はすべてを採用するのではなく、利用目的が重なるものをまとめ、運営に必要な人員や費用も各案に添えて再検討した。その結果、当初の案より部屋数は少なくなったが、複数の活動に使える共有スペースが設けられた。\n\n"
        "この例から、話し合いを早く始めれば、必ず建設費が下がると言えるわけではない。参加者が増えれば、調整に時間がかかることもある。それでも、完成後に使い方をめぐって対立する危険を減らし、現実に運営できる案を選びやすくなる。計画の段階で運営を考えるとは、要望をそのまま積み上げることではなく、目的と制約を共有して優先順位を決めることなのである。"
    )
    long_questions = [
        ("筆者が、施設計画の早い段階で運営方法を考えるべきだとする理由は何か。", ["完成後に使い方が対立する可能性を減らせるから", "建設費が必ず下がるから", "利用者の要望をすべて実現できるから", "設計に必要な人員をなくせるから"], 0, "運営を事前に考えると、完成後の使い方をめぐる対立を減らし、実際に管理できる案を選びやすくなります。建設費が必ず下がるとは述べていません。"),
        ("この市の話し合いで、要望を整理した方法として正しいものはどれか。", ["目的が重なる案をまとめ、必要な人員や費用を添えて見直した", "最初の会合で最も多かった要望をすべて採用した", "職員の意見だけで部屋数を決めた", "運営費を計算せずに設備を増やした"], 0, "市は同じ目的の要望をまとめ、それぞれに必要な人員・費用を加えて再検討しました。要望をそのまま全部実現したわけではありません。"),
        ("筆者の主張に最も近いものはどれか。", ["施設計画では、目的と運営上の制約を共有して優先順位を決める", "話し合いを早く始めれば建設費を必ず削減できる", "施設の部屋数を多くすることが利用者満足につながる", "完成してから利用者の意見を集めれば十分だ"], 0, "最後の段落は、運営を考えることを要望の積み上げではなく、目的と制約を共有し優先順位を定めることと説明しています。"),
    ]
    for i, (stem, options, key, vi) in enumerate(long_questions, 72):
        q.append(_item(f"N2_14_M1_{i:02}", "N2-RD-LONG", "長文読解", stem, options, key, vi, difficulty=3, context=long_passage))

    info = (
        "【地域交流センター・利用案内】\n"
        "予約受付：利用日の2か月前から7日前まで（窓口は平日9:00–17:00、オンラインは毎日）\n"
        "第1会議室：定員20人、1時間800円、飲食可。\n"
        "第2会議室：定員40人、1時間1,400円、飲食不可。\n"
        "音楽室：定員12人、1時間1,000円、防音設備あり。\n"
        "キャンセル：利用日の3日前まで無料。それ以降は料金の半額。\n"
        "備品：プロジェクターは無料、利用希望は予約時に申請。"
    )
    q.append(_item("N2_14_M1_75", "N2-RD-INFO", "情報検索", "25人で会議をし、軽食も取りたい。どの部屋なら条件を満たすか。", ["条件を満たす部屋はない", "第1会議室を利用する", "第2会議室を利用する", "音楽室を利用する"], 0, "第1会議室は飲食できますが定員20人です。第2会議室は25人を収容できますが飲食できず、音楽室も12人までです。したがって、25人で軽食を取る条件を同時に満たす部屋はありません。", difficulty=3, context=info))
    q.append(_item("N2_14_M1_76", "N2-RD-INFO", "情報検索", "プロジェクターを使う場合、予約時に何をすればよいか。", ["利用希望を申請する", "別料金を窓口で支払う", "利用日の3日前に連絡する", "音楽室だけを予約する"], 0, "プロジェクターは無料ですが、利用希望は予約時に申請する必要があります。", difficulty=2, context=info))

    if len(q) != 75:
        raise ValueError(f"M14 Section 1 must contain 75 items, got {len(q)}")
    for index, item in enumerate(q, 1):
        item["id"] = f"N2_14_M1_{index:02}"
    if len(q) != 75:
        raise ValueError(f"M14 Section 1 must contain 75 items, got {len(q)}")
    return apply_phase_71_star_repairs(apply_vietnamese_explanations(q))
