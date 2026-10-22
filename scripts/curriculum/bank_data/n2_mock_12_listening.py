# -*- coding: utf-8 -*-
"""Original society, environment and public-life listening items for N2-MOCK-12."""
from __future__ import annotations

import random

LETTERS = "ABCD"
_rng = random.Random(12012)
VI_EXPLANATIONS = {
    "N2_12_M1_L01": "Trưởng nhóm dặn chưa thông báo mở đường trước khi kiểm tra an toàn. Việc đầu tiên là hỏi công ty thi công thời điểm kiểm tra.",
    "N2_12_M1_L02": "Lịch thu giấy có thể trùng buổi diễn tập. Trước khi đổi sang Chủ nhật, người phụ trách cần gọi hỏi tình trạng đặt hội trường.",
    "N2_12_M1_L03": "Trạm xe buýt phải đổi do công trình. Trước tiên, cô ấy cập nhật hướng dẫn chuyển tuyến rồi mới liên lạc bệnh viện và trường học.",
    "N2_12_M1_L04": "Trước khi xin dùng phòng bên cạnh, nhân viên cần đếm số người đã đăng ký; đồng thời phải giữ lối đi đủ rộng cho xe lăn.",
    "N2_12_M1_L05": "Chưa thể chọn hoãn hay chuyển sang buổi giải thích trong nhà. Trước hết cần kiểm tra dự báo thời tiết và mực nước mới nhất.",
    "N2_12_M2_L01": "Pin bị rò không được bỏ vào thùng thu gom thông thường. Hãy cho pin vào túi riêng và giao trực tiếp cho nhân viên.",
    "N2_12_M2_L02": "Người mang thú cưng được hướng dẫn tới khu vực riêng ở bên ngoài tòa nhà, không vào khu tiếp nhận trong nhà.",
    "N2_12_M2_L03": "Muốn đổi thư viện nhận sách, cần làm thủ tục trên trang web trước khi sách được chuyển tới.",
    "N2_12_M2_L04": "Người đi làm thủ tục thay chủ thẻ phải mang thêm giấy ủy quyền của chủ thẻ, bên cạnh vé và giấy tờ xác minh.",
    "N2_12_M2_L05": "Người dùng nên mang bình cá nhân. Cốc giấy chỉ dành cho người quên bình và số lượng có hạn.",
    "N2_12_M2_L06": "Hạn đăng ký là ngày 25 tháng này và phải gọi điện. Sổ đăng ký nhà đất không bắt buộc, nhưng thông báo thuế hoặc ảnh có thể giúp giải thích tình hình.",
    "N2_12_M3_L01": "Không nên chỉ đặt xe đạp ở nhà ga hoặc chỉ xem giờ đi làm. Cần xét mục đích và khung giờ sử dụng ở từng khu vực để chọn nơi tăng số xe.",
    "N2_12_M3_L02": "Người nói muốn xem giao lưu giữa cư dân là một giá trị của vườn cộng đồng, bên cạnh số rau thu hoạch.",
    "N2_12_M3_L03": "Tăng số tấm pin thôi chưa bảo đảm nguồn điện ổn định. Cần tính cả cách tích trữ và sử dụng điện trong khu vực.",
    "N2_12_M3_L04": "Ngoài cho mượn sách, thư viện còn có thể hướng người dùng tới nguồn thông tin đáng tin cậy về hành chính và học tập.",
    "N2_12_M3_L05": "Hiệp hội du lịch muốn giới thiệu thêm đường đi bộ, điểm triển lãm và khung giờ khác để khách phân tán khỏi một điểm đông.",
    "N2_12_M4_L01": "Người hỏi nhờ mang tài liệu tới tòa thị chính trong ngày; câu trả lời xác nhận sẽ đem đến bằng chuyến buổi chiều.",
    "N2_12_M4_L02": "Người nói báo hồ sơ nộp muộn. Câu đáp phù hợp ghi nhận thông tin, kiểm tra hồ sơ rồi hướng dẫn thủ tục cần thiết.",
    "N2_12_M4_L03": "Câu hỏi là xe buýt có đi qua đoạn đang thi công không. Trả lời rằng xe vẫn chạy luân phiên một chiều là trực tiếp và phù hợp.",
    "N2_12_M4_L04": "Người hỏi đã biết hướng dẫn của thành phố là bỏ pin vào thùng thu gom và muốn xác nhận có thể bỏ vào rác không cháy hay không. Câu trả lời phủ định và nhắc làm theo hướng dẫn.",
    "N2_12_M4_L05": "Câu hỏi về điều kiện cho trẻ em tham gia; câu trả lời nêu rõ trẻ có thể đi cùng người giám hộ.",
    "N2_12_M4_L06": "Người hỏi muốn biết có thể đi ô tô đến buổi họp không. Vì không có bãi đỗ, câu trả lời khuyên dùng phương tiện công cộng.",
    "N2_12_M4_L07": "Có thể đổi điểm nhận sách trên trang web nếu sách chưa tới. Đây là câu trả lời đúng cả điều kiện lẫn cách làm.",
    "N2_12_M4_L08": "Người hỏi muốn biết trước tiên cần khảo sát gì để thu hút thêm người dùng trạm. Phương án phù hợp là tìm hiểu mục đích đi lại và khung giờ sử dụng; thông tin chuyến kế tiếp hoặc tuyến tới tòa thị chính không trả lời yêu cầu này.",
    "N2_12_M4_L09": "Người hỏi muốn biết hạn nộp đơn, nên câu trả lời cần nêu mốc ngày 25 trong tháng.",
    "N2_12_M4_L10": "Người nói không tìm thấy cửa vào nơi sơ tán. Câu trả lời chỉ đúng vị trí phía đông của nhà thi đấu và biển hướng dẫn.",
    "N2_12_M4_L11": "Nếu không có bình cá nhân, vẫn có thể dùng cốc giấy; tuy nhiên số cốc được chuẩn bị có giới hạn.",
    "N2_12_M5_L01": "Để xe buýt vẫn dừng ở phía đông, hai người thống nhất chỉ đặt quầy hàng ở phía tây.",
    "N2_12_M5_L02": "Kế hoạch thử trong một tháng là thêm một chuyến buổi sáng và điều xe nhỏ theo lượng đặt chỗ vào buổi chiều.",
    "N2_12_M5_L03": "Hai người thống nhất mở điểm nước muộn thêm một giờ và phân công luân phiên người bổ sung nước uống.",
}

# Rationale keys use the authored source-choice position, before deterministic display shuffling.
DISTRACTOR_VI = {
    "N2_12_M1_L04": {3: "Đây là việc xem xét sau khi biết số người đăng ký; người nói yêu cầu đếm số trước."},
    "N2_12_M2_L04": {
        1: "Không cần mua thẻ mới; nội dung yêu cầu mang chiếc vé đang xin hoàn tiền.",
        2: "Hóa đơn xe buýt không thay cho vé và giấy tờ xác minh được nêu trong hướng dẫn.",
        3: "Mốc một tháng là điều kiện để được hoàn tiền, không phải giấy tờ cần bổ sung cho người đại diện.",
    },
    "N2_12_M3_L01": {
        1: "Phương án này chỉ ưu tiên nhà ga và giờ đi làm, trong khi bài nói còn ghi nhận nhu cầu ban ngày ở từng khu vực.",
        2: "Bài không đề xuất một khung giờ cho riêng người đi khám; địa điểm cần dựa trên nhiều mục đích và thời điểm sử dụng.",
        3: "Đặt số xe bằng nhau ở mọi nơi bỏ qua khác biệt về nhu cầu mà người nói muốn khảo sát.",
    },
    "N2_12_M3_L02": {
        0: "Đó là cách quảng bá lúc mới mở vườn; người nói muốn ghi nhận thêm giá trị giao lưu.",
        2: "Tăng thời gian làm việc để tăng sản lượng vẫn lấy thu hoạch làm trọng tâm, trái với hướng mở rộng giá trị hoạt động.",
        3: "Người nói muốn người mới dễ tham gia trò chuyện, không chỉ đứng ngoài quan sát.",
    },
    "N2_12_M3_L03": {
        0: "Chỉ tăng số tấm pin không xử lý được chênh lệch giữa lúc phát điện và lúc dùng điện.",
        1: "Bài nêu cần tính cả tích trữ lẫn cách sử dụng điện trong khu vực, không thể bỏ qua vế sau.",
        3: "Ưu tiên nguồn điện khác là một chính sách khác; người nói tập trung phối hợp pin mặt trời, tích trữ và sử dụng tại chỗ.",
    },
    "N2_12_M3_L04": {
        0: "Tăng tiện ích cho mượn sách không bao quát vai trò kết nối người đọc với nguồn thông tin đáng tin cậy.",
        1: "Người nói lưu ý nhân viên không thể tự giải thích mọi thông tin; vai trò được nêu là hướng dẫn tới nguồn phù hợp.",
        2: "Mở buổi tư vấn với chuyên gia không được đề cập; trọng tâm là giúp người dùng tìm đúng nơi hoặc tài liệu để tự chọn thông tin.",
    },
    "N2_12_M3_L05": {
        0: "Đóng đài quan sát không phải kế hoạch được nêu; mục tiêu là phân tán khách trong khu vực.",
        2: "Tăng biển chỉ dẫn đơn thuần từng không giải quyết được ùn tập trung tại một điểm.",
        3: "Hạn chế quảng bá sẽ giảm khách, nhưng không thực hiện mục tiêu để họ khám phá nhiều nơi trong vùng.",
    },
    "N2_12_M4_L01": {
        1: "Câu này hẹn liên lạc lại nhưng không xác nhận sẽ chuyển tài liệu trong hôm nay.",
        2: "Địa chỉ quầy tiếp nhận không trả lời yêu cầu nhờ mang tài liệu tới đó.",
    },
    "N2_12_M4_L02": {
        1: "Vị trí nộp hồ sơ không cho biết cách xử lý việc đã nộp trễ.",
        2: "Cách tải mẫu đơn không trả lời thông tin về hồ sơ hiện đã nộp muộn.",
    },
    "N2_12_M4_L03": {
        1: "Thông tin về đường vòng không xác nhận xe buýt có đi qua đoạn đang thi công hay không.",
        2: "Lệnh đóng đường bắt đầu tuần tới không trả lời tình trạng hiện tại được hỏi.",
    },
    "N2_12_M4_L04": {
        1: "Thông tin về lịch thu gom chung không trả lời có được bỏ pin vào rác không cháy hay không.",
        2: "Phương án này trái với hướng dẫn của thành phố đã được nêu trong câu hỏi.",
    },
    "N2_12_M4_L05": {
        1: "Việc chuẩn bị găng tay hữu ích nhưng không trả lời trẻ em có được tham gia hay không.",
        2: "Hạn đăng ký không nêu điều kiện tham gia của trẻ em.",
    },
    "N2_12_M4_L06": {
        1: "Thời gian đi bộ từ ga không cho biết có thể đỗ xe tại hội trường hay không.",
        2: "Giờ mở quầy tiếp nhận không trả lời phương tiện nên dùng để tới nơi.",
    },
    "N2_12_M4_L07": {
        1: "Gia hạn thời gian nhận sách khác với đổi thư viện nhận sách.",
        2: "Vị trí hộp trả sách không liên quan đến việc đổi điểm nhận cuốn đã đặt.",
    },
    "N2_12_M4_L08": {
        1: "Giờ đến của chuyến kế tiếp không phải dữ liệu cần khảo sát để tìm cách tăng người dùng.",
        2: "Thông tin tuyến tới tòa thị chính không trả lời cần khảo sát gì để thu hút thêm người dùng.",
    },
    "N2_12_M4_L09": {
        1: "Cách nộp đơn trả lời nơi hoặc phương thức nhận hồ sơ, không phải hạn chót.",
        2: "Thời điểm bắt đầu sử dụng vườn không phải ngày cuối để đăng ký.",
    },
    "N2_12_M4_L10": {
        1: "Thông tin cần ghi tại quầy không chỉ vị trí lối vào đang được hỏi.",
        2: "Thời điểm phát chăn chỉ dẫn bước sau khi vào nơi sơ tán, không giúp tìm cửa vào.",
    },
    "N2_12_M4_L11": {
        1: "Quy định về nắp chai không cho biết người không mang bình có thể lấy nước bằng cách nào.",
        2: "Giờ lấy nước không trả lời việc có dụng cụ thay thế bình cá nhân hay không.",
    },
}


def _q(qid, type_id, category, intro, dialogue, stem, choices, key_index, explanation_vi,
       *, topic="public-life", difficulty=2):
    width = 3 if type_id == "N2-LIS-RESP" else 4
    if len(choices) != width or not 0 <= key_index < width:
        raise ValueError(f"Invalid listening item: {qid}")
    indexed = list(enumerate(choices))
    _rng.shuffle(indexed)
    options = [{"id": LETTERS[i], "text": text} for i, (_, text) in enumerate(indexed)]
    key = LETTERS[next(i for i, (source_i, _) in enumerate(indexed) if source_i == key_index)]
    script = "\n".join(part for part in (intro, dialogue) if part) or (stem if type_id == "N2-LIS-RESP" else "")
    explanation_vi = VI_EXPLANATIONS[qid]
    distractor_explanations = {}
    item_rationales = DISTRACTOR_VI.get(qid, {})
    for (source_i, text), option in zip(indexed, options):
        if source_i != key_index:
            distractor_explanations[option["id"]] = item_rationales.get(
                source_i,
                f"Phương án «{text}» không khớp với thông tin hoặc quyết định trong bài nghe. {explanation_vi}",
            )
    row = {
        "id": qid, "level": "N2", "typeId": type_id, "category": category,
        "script": script, "contextPassage": script, "stem": stem,
        "options": options, "correctAnswer": key,
        "explanation": f"正解は「{choices[key_index]}」です。",
        "explanationVi": explanation_vi,
        "distractorExplanations": distractor_explanations,
        "topicTag": topic, "difficultyBand": difficulty, "skill": "Listening",
    }
    return row


def get_n2_mock_12_listening_items(seed=14):
    _rng.seed(seed)
    q = []

    # Mondai 1 — task-based comprehension (5)
    task = [
        ("市役所で、職員と係長が歩道工事について話しています。", "女：南通りの工事ですが、予定より早く舗装が終わりそうです。明日から通れると案内してもいいですか。\n男：検査がまだです。まず施工会社に検査の時刻を確認してください。通行再開は安全を確認してから広報に知らせましょう。\n女：分かりました。先に検査予定を聞きます。", "女性はまず何をしますか。", ["施工会社に検査時刻を確認する", "南通りの通行再開を発表する", "工事を予定より延長する", "歩道を別の場所に移す"], 0, "係長は安全確認の前に案内を出さないよう求め、まず施工会社へ検査時刻を確認するよう指示しています。"),
        ("町内会で、二人が資源回収の日程について話しています。", "男：来週の古紙回収、いつもの土曜でいいですか。\n女：その日は広場で防災訓練があるそうです。回収車が入れないかもしれないので、先に自治会館の予約状況を確認してください。空いていれば日曜にずらしましょう。\n男：分かりました。まず会館に電話します。", "男性はまず何をしますか。", ["回収車を別の会社に頼む", "自治会館の予約状況を確認する", "防災訓練を中止する", "古紙をすぐ広場に運ぶ"], 1, "訓練と回収の時間が重なる可能性があるため、先に会館の予約状況を調べることになっています。"),
        ("バス会社で、運転手と担当者が運行変更について話しています。", "女：山側の停留所が工事で使えなくなります。明日の朝から臨時の停留所に移していいでしょうか。\n男：市の許可は出ていますが、近くの病院にも知らせる必要があります。まず乗り換え案内を更新し、病院と学校に新しい場所を連絡してください。\n女：案内の更新から始めます。", "女性はこの後、最初に何をしますか。", ["運行を一日休止する", "臨時停留所の使用を取り消す", "乗り換え案内を更新する", "病院の職員をバスに乗せる"], 2, "担当者は、関係先へ連絡する前に利用者向けの乗り換え案内を更新するよう指示しています。"),
        ("図書館で、職員二人が子ども向け行事について話しています。", "男：土曜の読み聞かせ、参加者が予定より多くなりそうです。机を増やしますか。\n女：机より、車いすの人が通れる幅を残したいです。まず申込み人数を確認して、定員を超えそうなら隣の部屋を使えるか聞いてください。\n男：はい。人数を数えてから部屋を相談します。", "男性はまず何をしますか。", ["申込み人数を確認する", "机をすべて片づける", "読み聞かせを中止する", "隣の部屋を使えるか先に確認する"], 0, "隣室を使うか決める前に、参加申込みが何人あるか確認するよう言われています。"),
        ("環境課で、職員と上司が川の観察会について話しています。", "女：明日の観察会は雨の予報ですが、予定どおり河原に集まりますか。\n男：川の水位が上がる可能性があります。まず気象情報と水位の最新値を確認してください。その後、延期するか屋内の説明会に変えるか決めます。\n女：では、最新情報を確認してから連絡します。", "女性はまず何をしますか。", ["屋内説明会をすぐ始める", "観察会を必ず中止すると発表する", "参加者に雨具を配る", "気象情報と川の水位を調べる"], 3, "延期か屋内開催かを決める前に、気象と水位の最新情報を調べる手順です。"),
    ]
    for i, row in enumerate(task, 1):
        q.append(_q(f"N2_12_M1_L{i:02}", "N2-LIS-TASK", "課題理解", *row))

    # Mondai 2 — key points (6)
    point = [
        ("市の放送で、ごみの出し方について説明しています。", "女：来月から、使い捨て電池は燃えないごみの日ではなく、月二回の回収箱へ入れてください。回収箱は市役所と各地区センターに置きます。液漏れした電池は袋に分け、職員に直接渡してください。", "液漏れした電池はどうしますか。", ["燃えるごみと一緒に出す", "袋に分けて職員に渡す", "自宅で分解してから出す", "次の燃えないごみの日まで置く"], 1, "液漏れした電池は通常の回収箱ではなく、袋に分けて職員へ直接渡すよう説明されています。"),
        ("町の防災担当者が、避難所の開設について説明しています。", "男：避難所を開ける場合は、正面玄関ではなく体育館の東側入口から入ってください。受付で住所と人数を記入し、ペットを連れている人は建物の外にある専用区画へ案内します。毛布は受付後に配ります。", "ペットを連れている人はどこへ行きますか。", ["体育館の正面玄関", "受付の隣にある会議室", "建物の外の専用区画", "毛布を受け取る倉庫"], 2, "ペット同伴の場合は、建物の外に設けた専用区画へ案内されます。"),
        ("図書館の職員が、予約本の受け取りについて話しています。", "女：予約した本は、到着の連絡を受けてから一週間以内に受け取ってください。期限を過ぎると、次に予約している人へ回します。受け取り場所を変更したい場合は、本が届く前にウェブサイトから手続きしてください。", "受け取り場所を変えたい場合、いつ手続きしますか。", ["予約を入れる前", "本が届く前", "受け取り期限が過ぎてから", "次の人が借りた後"], 1, "受け取り場所は、本が到着する前にウェブサイトから変更する必要があります。"),
        ("バス会社が、定期券の払い戻しについて案内しています。", "男：定期券を払い戻す場合、窓口へ券と本人確認書類をお持ちください。残り期間が一か月未満の場合は払い戻しできません。代理の方が来る場合は、本人の委任状も必要です。", "代理人が払い戻しに行く場合、追加で何が必要ですか。", ["本人の委任状", "新しい定期券", "バスの領収書だけ", "定期券の残り期間が一か月以上あること"], 0, "代理人が手続きする場合、券と本人確認書類に加え、本人の委任状が必要です。"),
        ("市の広報で、熱中症対策の給水所について説明しています。", "女：給水所は市民センターと三つの図書館に設置します。利用できるのは開館時間内で、マイボトルを持参してください。容器を忘れた方には紙コップを用意していますが、数に限りがあります。", "給水所を利用するとき、原則として何を持っていきますか。", ["身分証明書", "紙コップ", "マイボトル", "予約票"], 2, "基本はマイボトルを持参します。忘れた人には数に限りのある紙コップが用意されています。"),
        ("町の担当者が、空き家相談会の申込みについて説明しています。", "男：相談会は予約制で、今月二十五日までに電話で申し込んでください。建物の登記簿がなくても相談できますが、固定資産税の通知書や写真があれば、状況を説明しやすくなります。", "相談会に申し込む方法はどれですか。", ["今月二十五日までに電話する", "登記簿を郵送してから予約する", "当日、写真だけを持って行く", "来月に窓口で申し込む"], 0, "申込みは今月25日までに電話で行います。登記簿は必須ではなく、関連資料があれば相談に役立ちます。"),
    ]
    for i, row in enumerate(point, 1):
        q.append(_q(f"N2_12_M2_L{i:02}", "N2-LIS-POINT", "ポイント理解", *row))

    # Mondai 3 — outline / gist (5)
    gist = [
        ("市の交通政策担当者が、自転車の共同利用について話しています。", "共同利用の自転車は、駅前だけに置けば十分だと思われがちです。しかし、駅から少し離れた診療所や公共施設へ行く人もいます。利用記録を調べると、通勤時間以外にも昼間の利用が多い地区がありました。まずは利用目的と時間帯を見ながら、台数を増やす場所を決めることが大切です。", "話し手が最も伝えたいことは何ですか。", ["利用記録を基に、駅前以外も含めて配置場所を見直す", "通勤時間帯の利用が多い駅前に台数を集中させる", "診療所や公共施設の利用者向けに、昼間の利用を優先する", "利用目的を問わず、すべての地区に同じ台数を置く"], 0, "利用目的や時間帯の記録を基に、駅前だけに限らず地区ごとの需要に応じて配置を決める点が中心です。"),
        ("地域の農園を運営する人が、参加者の募集について話しています。", "農園を始めたころは、収穫した野菜を持ち帰れることを前面に出していました。ところが、参加者の話を聞くと、作業後に近所の人と話せる時間を楽しみにしている人が多いと分かりました。今後は収穫量だけを成果とせず、初めて来た人も自然に会話へ入れる仕組みを考えたいと思います。", "話し手は農園の活動をどうしたいと考えていますか。", ["収穫量を主な成果として、持ち帰れる野菜で参加を促す", "作業後の交流を大切にし、初参加者も会話に入れる仕組みを作る", "交流の時間より作業時間を延ばして、収穫量を増やす", "初めて来た人には作業を任せず、見学を中心にする"], 1, "収穫物だけでなく、初参加者も含めて人とつながれることを活動の価値として育てたいと述べています。"),
        ("大学の研究者が、太陽光発電の導入について説明しています。", "太陽光パネルを増やせば、昼間の発電量は増えます。ただ、天候によって出力が変わり、電気を使う時間と発電する時間が合わないこともあります。設備の数だけを見るのではなく、蓄電や地域内での電力の使い方も合わせて考えなければ、安定した供給にはつながりません。", "話し手が強調していることは何ですか。", ["発電量を増やすには、まずパネルの設置数を優先する", "蓄電設備を整えれば、地域内での使い方は検討しなくてよい", "発電と消費の時間差を踏まえ、蓄電や地域内利用も組み合わせる", "太陽光の変動を補うため、太陽光以外の発電設備を優先して導入する"], 2, "設備の数だけでは電力を安定供給できず、蓄電や地域内での利用方法も一緒に設計する必要があるという説明です。"),
        ("図書館長が、図書館の役割について話しています。", "図書館は本を貸す場所ですが、それだけではありません。行政の案内や学習相談を必要とする人も来ます。すべての情報を職員が説明するのではなく、信頼できる窓口や資料へ案内する役割を整えれば、利用者が自分で必要な情報を選びやすくなります。", "話し手は図書館の役割についてどう考えていますか。", ["行政や学習に関する相談は専門機関に任せ、図書館は本の貸出しを主な役割とする", "行政や学習相談を受けた職員が、その場ですべて回答する", "行政や学習の相談会を定期的に開き、専門家に館内で説明してもらう", "信頼できる窓口や資料を案内し、利用者が情報を選べるようにする"], 3, "本の貸出だけでなく、行政や学習に必要な情報源へ利用者をつなぎ、自分で情報を選べるよう支えることも図書館の役割です。"),
        ("観光協会の職員が、訪問者の集中について説明しています。", "花の見頃には、特定の展望台へ人が集中します。案内板を増やすだけでは混雑が解消しませんでした。そこで、周辺の散策路や小さな展示施設も紹介し、時間をずらして訪れてもらう情報を発信しています。来訪者を一か所に集めず、地域全体を楽しんでもらうことが目標です。", "観光協会が目指していることは何ですか。", ["混雑時には展望台への立入りを一時的に停止する", "周辺施設も紹介し、訪問先や時間帯を地域内に分散させる", "案内板の数を増やし、展望台への移動を効率化する", "見頃の時期は観光情報を控え、来訪を減らす"], 1, "案内板の追加だけに頼らず、周辺の場所や時間帯も紹介して、訪問を地域内に分散させる方針です。"),
    ]
    for i, row in enumerate(gist, 1):
        q.append(_q(f"N2_12_M3_L{i:02}", "N2-LIS-SUMM", "概要理解", *row))

    # Mondai 4 — quick response (11); spoken options are emitted in displayed order.
    response = [
        ("この資料、今日中に市役所へ届けていただけますか。", ["はい、午後の便でお持ちします。", "申し訳ありませんが、担当者が戻り次第こちらからご連絡します。", "市役所の担当窓口は、正面玄関を入って右側です。"], 0, "依頼を受けて、午後に届けると返事しています。"),
        ("申し訳ありません。申請書の提出が一日遅れてしまいました。", ["ご連絡ありがとうございます。まず申請書を確認し、必要な手続きを改めてご案内します。", "提出先は本庁の二階ですので、窓口まで直接お持ちください。", "申請書の書式は、市のウェブサイトからダウンロードできます。"], 0, "遅れの報告を受けたことを受け止め、書類を確認して必要な手続きを案内すると伝える返答が自然です。"),
        ("この先の道路は工事中ですが、バスは通れますか。", ["はい、片側交互通行で運行しています。", "工事区間の迂回路は、停留所に掲示しています。", "通行止めは来週月曜日から始まる予定です。"], 0, "通行可能か尋ねているので、片側交互通行でバスが走ると答える選択肢が合います。"),
        ("この市では、古い電池は回収箱に入れるそうですね。燃えないごみの日に出してもいいでしょうか。", ["いいえ、市の案内どおり回収箱に入れてください。", "この地域では、来月からごみの回収日が変わります。", "はい、燃えないごみの日に透明な袋に入れてください。"], 0, "市の案内を踏まえ、燃えないごみには出さず回収箱を使うよう直接答えています。"),
        ("日曜日の清掃活動ですが、子どもも参加できますか。", ["はい。保護者と一緒なら参加できます。", "軍手はこちらで用意しますので、当日は受付にお越しください。", "参加の申込みは金曜日までにお願いします。"], 0, "参加条件を尋ねているため、保護者同伴なら可能だという返事が適切です。"),
        ("来週の説明会、会場まで車で行っても大丈夫ですか。", ["駐車場がないので、公共交通をご利用ください。", "最寄り駅から会場までは歩いて五分ほどです。", "受付は開始時刻の十五分前からです。"], 0, "車で行けるかという質問には、駐車場がないため公共交通を勧める返答が合います。"),
        ("予約した本を受け取る場所を、別の図書館に変えられますか。", ["本が届く前なら、ウェブサイトから変更できます。", "受取期限の延長は、予約した図書館の窓口でお申し込みください。", "返却ポストの場所は、ウェブサイトでご確認いただけます。"], 0, "受取場所の変更可否を聞いているため、期限と手続き方法を伝える返答が自然です。"),
        ("最近、このバス停を使う人が減っています。利用者を増やすため、まず何を調べればよいでしょうか。", ["利用目的や時間帯を調べてから、対応を検討しましょう。", "次の便は、あと十分ほどで到着する予定です。", "市役所へは、この路線で乗り換えずに行けます。"], 0, "利用者を増やすために最初に調べる情報を尋ねています。利用目的や時間帯を把握してから対応を検討する返答が直接答えています。"),
        ("市民農園の申込みは、いつまでに出せばいいですか。", ["今月二十五日までにお願いします。", "申込みは窓口かウェブサイトで受け付けています。", "今年度の利用は、四月から始まります。"], 0, "期限を尋ねているので、申込締切を答える選択肢が適切です。"),
        ("すみません、避難所の入口が見つからないのですが。", ["体育館の東側にあります。案内表示を見てください。", "受付では、住所と一緒に避難する人数をご記入ください。", "毛布は受付を済ませた後にお渡しします。"], 0, "場所を尋ねているので、東側入口と表示を案内する返答が自然です。"),
        ("この地域の給水所は、マイボトルがなくても使えますか。", ["はい、紙コップを用意していますが、数に限りがあります。", "持参する容器は、ふた付きのものに限ります。", "水の補給は、午後五時までにお願いします。"], 0, "容器がない場合の利用可否に対し、紙コップがあるものの数に限りがあると説明しています。"),
    ]
    for i, (stem, choices, key, vi) in enumerate(response, 1):
        q.append(_q(f"N2_12_M4_L{i:02}", "N2-LIS-RESP", "即時応答", "", "", stem, choices, key, vi, topic="public-life"))

    # Mondai 5 — integrated comprehension (3)
    integ = [
        ("町役場で、二人の職員が夏祭りの交通整理について話しています。", "女：祭りの日は駅前通りを歩行者天国にする案が出ています。屋台を並べられますが、バスは迂回が必要です。\n男：病院へ行く人が困らないよう、東側の停留所は残せませんか。\n女：警察に確認したところ、東側は通行できます。屋台は西側だけにして、バスの案内を一週間前から出しましょう。\n男：では、その案で警察とバス会社に連絡します。", "屋台はどこに並べることになりましたか。", ["東側の停留所の前だけ", "西側の通りだけ", "駅のホーム", "病院の入口"], 1, "東側はバスが通れるように残し、屋台を西側だけに並べる案に決まりました。"),
        ("地域の交通会議で、委員二人が予約制の乗合車について話しています。", "男：利用者アンケートでは、病院へ行く朝の便が足りないという意見が多いですね。\n女：一方で、午後は空席が目立つ便があります。車を増やす前に、朝だけ一便を追加し、午後の便は予約に合わせて小型車に変えるのはどうでしょう。\n男：運転手の勤務時間と車両の都合も確認しておきたいですね。\n女：勤務表を確認したところ、その組み合わせなら調整できそうです。では、まず一か月試して、予約数と乗車できなかった人の数を比べましょう。\n男：それで効果を判断できますね。", "二人は最初にどのような変更を試すことにしましたか。", ["すべての便を廃止する", "朝の便を一つ増やし、午後は予約に応じて小型車にする", "午後の便を増やし、朝の便をなくす", "車両を増やして調査はしない"], 1, "勤務時間を確認して実施できることを確かめたうえで、朝の便を追加し、午後は予約数に合わせて小型車を使う案を一か月試します。"),
        ("市民センターで、二人が猛暑日の給水所の運営について話しています。", "女：来週は気温が高くなる予報です。給水所を予定どおり午後五時で閉めてもいいでしょうか。\n男：仕事帰りの人も利用します。センターの職員だけで延長できるか確認しましょう。\n女：職員は六時までなら対応できますが、飲み水の補充が必要です。\n男：では、閉館を一時間延ばし、補充の担当を町内会と交代で決めましょう。\n女：分かりました。利用者数も記録します。", "二人が合意した変更はどれですか。", ["給水所を一時間長く開け、補充担当を決める", "給水所を午後三時に閉める", "飲み水を各家庭へ配達する", "職員を減らして利用者数を記録しない"], 0, "暑い日の仕事帰りにも使えるよう閉所を一時間遅らせ、飲み水を補充する担当を決めます。"),
    ]
    for i, row in enumerate(integ, 1):
        q.append(_q(f"N2_12_M5_L{i:02}", "N2-LIS-INTEG", "統合理解", *row))

    expected = {"N2-LIS-TASK": 5, "N2-LIS-POINT": 6, "N2-LIS-SUMM": 5, "N2-LIS-RESP": 11, "N2-LIS-INTEG": 3}
    counts = {kind: sum(item["typeId"] == kind for item in q) for kind in expected}
    if len(q) != 30 or counts != expected or len({item["id"] for item in q}) != 30:
        raise ValueError(f"M12 listening blueprint failure: {len(q)} {counts}")
    return q
