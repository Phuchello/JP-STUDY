# -*- coding: utf-8 -*-
"""Original society, environment and public-life items for N2-MOCK-12.

Authoring source only. It must pass key-free review and release validation
before it is copied into the public mock bank.
"""
from __future__ import annotations

import random

LETTERS = "ABCD"
_rng = random.Random(202612)
VI_EXPLANATIONS = {
    "N2_12_M1_01": "実施（じっし）nghĩa là thực hiện một kế hoạch hoặc quy định. Câu nói thành phố đem phương pháp phân loại rác mới áp dụng tại ba khu vực.",
    "N2_12_M1_02": "急激 đọc là きゅうげき, chỉ sự thay đổi nhanh và mạnh. Trong câu, mực nước sông tăng nhanh sau bão.",
    "N2_12_M1_03": "維持 đọc là いじ, nghĩa là giữ cho tình trạng hiện có tiếp tục được duy trì. Ở đây là chi phí bảo dưỡng lối đi bộ.",
    "N2_12_M1_04": "講じる đọc là こうじる, nghĩa là đưa ra hoặc thực hiện biện pháp để xử lý vấn đề. Cụm thường gặp là 対策を講じる.",
    "N2_12_M1_05": "差異 đọc là さい, nghĩa là sự khác biệt giữa các đối tượng. Câu nói về khác biệt trong nhận thức giữa các thế hệ.",
    "N2_12_M2_01": "Cách viết đúng của きょうきゅう là 供給, nghĩa là cung cấp hàng hóa hoặc dịch vụ cho nơi cần. Kế hoạch đưa nước tới các điểm sơ tán dùng từ này.",
    "N2_12_M2_02": "改善 là sửa điểm chưa tốt để tình trạng được tốt hơn. Câu nói về đề xuất cải thiện một chế độ.",
    "N2_12_M2_03": "増設 là xây thêm hoặc lắp thêm cơ sở, thiết bị. Vì lượng khách tăng nên thành phố bổ sung biển chỉ dẫn.",
    "N2_12_M2_04": "更新（こうしん）là thay thông tin cũ bằng nội dung mới. Ở đây thành phố cập nhật thông tin nơi sơ tán trên trang web.",
    "N2_12_M2_05": "重視 nghĩa là xem một điều là quan trọng và lấy nó làm trọng tâm. Thành phố phân tích theo mục đích sử dụng, không theo tuổi.",
    "N2_12_M3_01": "効率化 là quá trình thay đổi để tăng hiệu suất. Động từ 進める cần danh từ chỉ quá trình, vì vậy 化 tạo đúng từ.",
    "N2_12_M3_02": "比較可能性 là khả năng có thể so sánh kết quả giữa các khu vực. Dùng cùng một câu hỏi nhằm bảo đảm khả năng so sánh này.",
    "N2_12_M3_03": "オンライン化 là chuyển thủ tục sang hình thức trực tuyến. Mẫu 「オンライン化する」 tự nhiên khi nói về thay đổi cách làm.",
    "N2_12_M3_04": "自主性 là tính tự chủ, tự quyết định và tiến hành thủ tục. Câu nhấn mạnh khả năng người dùng tự làm.",
    "N2_12_M3_05": "連帯感 là cảm giác gắn bó và cùng hỗ trợ nhau. Hoạt động dọn dẹp chung làm tăng sự gắn kết của cư dân.",
    "N2_12_M4_01": "規制 là áp dụng biện pháp quản lý giao thông trong một phạm vi hoặc thời gian nhất định. Câu nói xe không được đi qua cầu trong lúc kiểm tra; 「通行を規制する」 là cách kết hợp tự nhiên. 許可 trái nghĩa, còn 統制 và 抑制 không hợp với cách diễn đạt giao thông ở đây.",
    "N2_12_M4_02": "開設する nghĩa là mở một cơ sở để bắt đầu tiếp nhận người dùng. Trú ẩn được mở sớm trước dự báo mưa lớn.",
    "N2_12_M4_03": "見直す là xem lại để kiểm tra và điều chỉnh điểm chưa phù hợp. Thiết kế được rà soát trước khi khởi công.",
    "N2_12_M4_04": "比較する là đặt kết quả của hai đối tượng cạnh nhau để xem điểm giống và khác. Vì hai khu vực dùng cùng câu hỏi và cách tổng hợp, kết quả có thể được so sánh trực tiếp; 記録する chỉ là lưu lại, không diễn tả việc đối chiếu giữa hai khu vực.",
    "N2_12_M4_05": "設置する là xây hoặc bố trí một công trình tại địa điểm cụ thể. Bể điều hòa được đặt dưới công viên để giữ nước mưa khi có mưa lớn.",
    "N2_12_M4_06": "説明する là trình bày nội dung để người nghe hiểu. Nhân viên hành chính dùng cách nói dễ hiểu với cư dân.",
    "N2_12_M4_07": "再検討 là suy xét lại một lần nữa. Thành phố xem lại cách vận hành tuyến xe đang giảm người dùng.",
    "N2_12_M5_01": "踏まえて nghĩa là cân nhắc thông tin hoặc ý kiến đã có rồi mới hành động. Thiết bị công viên được sửa dựa trên mong muốn của cư dân.",
    "N2_12_M5_02": "即している nghĩa là phù hợp với tình hình thực tế hoặc tiêu chuẩn. Kế hoạch vận hành khớp với cách người dân đang sử dụng.",
    "N2_12_M5_03": "軽減する nghĩa là làm cho mức độ hoặc gánh nặng nhỏ đi. Giảm mục trong mẫu đơn nhằm giảm công việc phải làm.",
    "N2_12_M5_04": "保留する nghĩa là tạm hoãn kết luận để xem xét sau. Do có ý kiến trái chiều, thành phố chưa đưa ra kết luận ngay; quyết định chưa bị hủy.",
    "N2_12_M5_05": "地区を問わず nghĩa là không phân biệt khu vực. Người ở các khu khác nhau đều có thể sử dụng chế độ.",
    "N2_12_M6_01": "見合わせる ở đây nghĩa là tạm hoãn việc thi công cho đến khi xác nhận an toàn. Các câu còn lại dùng từ này với nghĩa đối chiếu tài liệu hoặc nhìn nhau.",
    "N2_12_M6_02": "負担 trong câu đúng là sức lực và sự bất tiện mà người cao tuổi phải chịu khi đi mua sắm. Các câu còn lại nói về ai trả hoặc chia phần chi phí.",
    "N2_12_M6_03": "見込む ở đây là đánh giá cao năng lực của một người và kỳ vọng họ đảm nhận được vai trò. 「彼の調整力を見込んで委員長を任せた」 nghĩa là tin vào khả năng điều phối của anh ấy nên giao vai trò chủ tịch. Các lựa chọn khác nói về dự đoán số lượng, tính trước chi phí hoặc nhìn thấy cảnh vật.",
    "N2_12_M6_04": "講演依頼に応じる nghĩa là chấp nhận lời mời diễn thuyết. Những lựa chọn khác diễn tả việc thay đổi số lượng theo tình hình hoặc điều kiện.",
    "N2_12_M6_05": "活動を支える là hỗ trợ để hoạt động tiếp tục tồn tại. Các lựa chọn còn lại dùng 支える theo nghĩa đỡ vật hoặc cơ thể bằng lực.",
    "N2_12_M7_01": "ものの nối hai sự thật trái với dự đoán: thống kê xác nhận dân số đang giảm, nhưng số cửa hàng mới ở khu phố trước ga vẫn tăng. Vì mức giảm dân số được nêu rõ là sự thật, どころか (phủ định vế trước để nhấn mạnh điều trái ngược) không phù hợp.",
    "N2_12_M7_02": "かねない chỉ nguy cơ có thể dẫn đến kết quả không mong muốn. Trì hoãn biện pháp có thể khiến thiệt hại lan rộng.",
    "N2_12_M7_03": "ことによって nối hành động với kết quả tạo ra từ hành động đó. Việc đã ghi nhận ý kiến giúp tìm điểm cần cải thiện dễ hơn. うちに thường diễn tả việc xảy ra trong lúc một trạng thái còn tiếp diễn; ở đây hành động ghi nhận đã hoàn tất (記録した).",
    "N2_12_M7_04": "年齢を問わず nghĩa là không phụ thuộc vào tuổi. Bất kỳ ai có nguyện vọng đều được tham gia lớp học.",
    "N2_12_M7_05": "に限らず nghĩa là không chỉ giới hạn ở điều đang nêu. Công viên có cảnh hoa mùa xuân và cả lá đỏ mùa thu.",
    "N2_12_M7_06": "Vたうえで diễn tả việc hoàn tất hành động thứ nhất rồi mới thực hiện hành động sau. Thành phố xác nhận độ an toàn trước khi cho phép lắp thiết bị. うちに cần một trạng thái hoặc hành động còn tiếp diễn; ở đây việc kiểm tra đã hoàn tất. ものの và とはいえ cần quan hệ nhượng bộ, nhưng câu chỉ nêu thứ tự hợp lý.",
    "N2_12_M7_07": "に伴って diễn tả một thay đổi kéo theo thay đổi khác. Việc sửa quy định đi cùng thay đổi trong cách bỏ rác.",
    "N2_12_M7_08": "からといって～とは限らない phủ nhận suy luận rằng chỉ vì vế đầu đúng thì vế sau chắc chắn đúng. Việc sống ở trung tâm không tự chứng minh rằng có thể sinh hoạt không cần xe; ものなら nêu giả định, に応じて cần danh từ làm căn cứ, còn どころか diễn tả quan hệ trái ngược hoặc mức độ vượt xa.",
    "N2_12_M7_09": "だけでなく～にも bổ sung thêm đối tượng. Việc chuẩn bị ứng phó thiên tai cần thiết với cả chính quyền và từng cư dân.",
    "N2_12_M7_10": "にわたって chỉ phạm vi hoặc khoảng thời gian kéo dài. Cuộc khảo sát diễn ra ở nhiều khu vực trong ba năm.",
    "N2_12_M7_11": "にとどまらず nghĩa là không dừng lại ở phạm vi được nêu. Tranh luận về giao thông còn liên quan tới sự công bằng giữa các khu vực.",
    "N2_12_M7_12": "からには diễn tả trách nhiệm hoặc điều cần làm một khi đã quyết định điều gì. Đã đăng ký nhận cảnh báo thiên tai thì cần định kỳ kiểm tra địa chỉ; các lựa chọn còn lại không biểu thị quan hệ cam kết này.",
    "N2_12_M9_01": "Kết quả khảo sát cho thấy nhu cầu buổi sáng cao và buổi tối còn ghế trống. を踏まえて nghĩa là dựa trên/cân nhắc một dữ kiện đã có; kế hoạch tăng chuyến sáng và đổi cách vận hành buổi tối phản ánh trực tiếp dữ liệu đó.",
    "N2_12_M9_02": "ことによって nối biện pháp với kết quả: báo trước nội dung và chọn giờ phù hợp giúp người mới dễ sắp xếp.",
    "N2_12_M9_03": "に応じて nghĩa là tùy theo hoặc căn cứ vào một điều kiện để điều chỉnh việc khác. Câu yêu cầu thay đổi quy mô cơ sở dựa theo quãng đường đi lại và cơ cấu dân số của từng khu vực; các lựa chọn còn lại không nối được quan hệ điều chỉnh đó.",
    "N2_12_M9_04": "からといって～わけではない phủ nhận kết luận tự động. Lắp thiết bị năng lượng tái tạo không có nghĩa là mọi vấn đề điện đều được giải quyết.",
    "N2_12_M9_05": "だけでなく～も nối hai mặt cần được chia sẻ. Buổi họp phải nêu cả lợi ích lẫn khó khăn trong thời gian thi công.",
    "N2_12_M10_02": "Trong lúc cắt tỉa cây, lối phía đông bị đóng nhưng lối phía tây vẫn mở. Nếu mưa, công việc chuyển sang tuần sau và thành phố thông báo trên trang web.",
    "N2_12_M10_03": "Điểm nhận là trung tâm giao lưu cạnh thư viện, không phải cửa chính thư viện. Thực phẩm phải chưa mở và còn hạn ít nhất một tuần; việc nhận chỉ diễn ra ngày thường từ 9 giờ đến 17 giờ. Vì vậy phương án đúng giữ đủ cả địa điểm, tình trạng bao bì và hạn sử dụng; phương án còn lại sai một trong các điều kiện này.",
    "N2_12_M10_04": "Hồ bơi đóng cửa từ ngày 20 đến 22. Lớp bơi được học bù vào ngày 25, còn hạn vé vào cửa được kéo dài trong thời gian đóng cửa.",
    "N2_12_M10_05": "Thứ tự ghé thăm được đổi, nhưng giờ đến và thời lượng dừng ở từng khu vẫn giữ nguyên. Chỉ giờ xe rời thư viện được chuyển sớm hơn 15 phút.",
    "N2_12_M11_01": "Người dùng khó chọn vì không biết mức giảm giá ở từng cửa hàng. Thành phố thống nhất cách ghi thành ba mức để khách dễ so sánh.",
    "N2_12_M11_02": "Sau khi thống nhất cách hiển thị theo ba mức, khách dễ so sánh hơn và nhân viên giảm thời gian giải thích. Thành phố chưa quyết định cùng một tỷ lệ giảm giá cho mọi món; đó vẫn là vấn đề cần xem xét.",
    "N2_12_M11_03": "Khi quyết định tiếp tục dự án, thành phố sẽ xem cả số lượng bán sót, lượng thực phẩm bị thải bỏ và ý kiến người dùng.",
    "N2_12_M11_04": "Xe ghép chuyến được đưa vào vì xe buýt theo giờ cố định vẫn tốn chi phí vào những ngày ít khách.",
    "N2_12_M11_05": "Người dân khó đặt chỗ, vì vậy thị trấn kéo dài giờ nhận cuộc gọi và treo hướng dẫn tại điểm dừng.",
    "N2_12_M11_06": "Thị trấn sẽ cân nhắc liệu những khung giờ cần thiết cho việc đi khám và đi học có được duy trì hay không, chứ không chỉ nhìn chi phí.",
    "N2_12_M11_07": "Thư viện muốn giảm thời gian chờ nhận sách đã đặt, vốn trước đó kéo dài do sách được chuyển tới chi nhánh không thường xuyên.",
    "N2_12_M11_08": "Thời gian chờ đã giảm, nhưng nhu cầu tập trung ở một số chi nhánh khiến thư viện khó quyết định có mua thêm sách hay không.",
    "N2_12_M11_09": "Khi điều chỉnh số lượng sách, thư viện xem cả số lượt mượn, lượt hủy đặt chỗ và mong muốn của bạn đọc.",
    "N2_12_M12_01": "A đề xuất kết nối xe buýt với bãi đỗ ngoại ô để người cần ô tô vẫn di chuyển thuận tiện; B cũng nhấn mạnh người cao tuổi và người mang hàng cần ô tô. Điểm chung là phải tính đến người cần sử dụng xe khi bàn về bãi đỗ.",
    "N2_12_M12_02": "A ủng hộ giảm chỗ đỗ để mở rộng không gian đi bộ. B muốn thử nghiệm trước rồi mới quyết định số lượng chỗ đỗ dựa trên kết quả.",
    "N2_12_M13_01": "Khảo sát cho thấy dòng nước ở hạ lưu chảy nhanh hơn và những vùng nước nông, nơi cá đẻ trứng, đã giảm đi.",
    "N2_12_M13_02": "Người dân lo chi phí cắt cỏ và tầm nhìn; tổ chức môi trường kỳ vọng bảo vệ sinh cảnh. Thử nghiệm nhỏ giúp kiểm tra cả hai điều.",
    "N2_12_M13_03": "Cư dân có thể ghi nhận thay đổi để hỗ trợ thiết kế, nhưng thành phố còn đánh giá an toàn, chi phí duy trì và hệ sinh thái; số người tham gia không phải tiêu chí duy nhất.",
    "N2_12_M14_01": "Cần đăng ký trước ngày 10/6; tối đa 40 người được nhận theo thứ tự đăng ký. Người tham gia phải ở hoặc làm việc trong thành phố, mang theo bút và không thể đỗ xe tại điểm học.",
    "N2_12_M14_02": "Thông báo nêu rõ hai nội dung của buổi học là xác định nơi sơ tán và chọn đồ dùng cần mang theo khi khẩn cấp.",
}

DISTRACTOR_VI = {
    "N2_12_M9_01": {
        "に先立って": "に先立って nghĩa là trước khi một sự việc diễn ra. Khảo sát đã hoàn tất và kết quả đã được biết trước khi thành phố đề xuất điều chỉnh, nên không thể nói kế hoạch có trước kết quả.",
        "を問わず": "を問わず nghĩa là không phụ thuộc vào/không xét đến một điều kiện. Ở đây phương án điều chỉnh thay đổi theo số lượt đặt chỗ buổi sáng và tình trạng ghế trống buổi tối.",
        "を通じて": "を通じて chỉ phương tiện hoặc quá trình 'thông qua/xuyên suốt'. Kết quả khảo sát ở đây là căn cứ để cân nhắc kế hoạch, không phải phương tiện thực hiện kế hoạch.",
    },
    "N2_12_M7_06": {
        "ものの": "ものの nối hai ý có quan hệ nhượng bộ; ở đây việc xác nhận an toàn rồi cấp phép là trình tự hợp lý, không có ý đối lập.",
        "うちに": "うちに thường diễn tả việc xảy ra khi trạng thái hoặc hành động còn tiếp diễn; câu này dùng động từ quá khứ và nêu việc cấp phép sau khi đã xác nhận.",
        "とはいえ": "とはいえ dùng để nhượng bộ hoặc điều chỉnh nhận định trước đó; câu này chỉ nêu thứ tự xác nhận rồi cấp phép.",
    },
    "N2_12_M7_08": {
        "ものなら": "ものなら thường nêu giả định như 'nếu có thể/giá mà'; câu này cần phủ nhận suy luận từ nơi cư trú.",
        "に応じて": "に応じて có nghĩa 'tùy theo/căn cứ vào' và thường đứng sau danh từ; cụm động từ 住んでいる không làm căn cứ phù hợp ở đây.",
        "どころか": "どころか diễn tả ý 'không những không... mà còn...' hoặc mức độ trái xa; câu này chỉ nói vế trước không bảo đảm vế sau.",
    },
    "N2_12_M11_02": {
        "すべての商品を同じ割合で値引きすることにした": "本文 chỉ nêu đây là vấn đề còn tồn tại nếu mọi sản phẩm dùng cùng tỷ lệ giảm; thành phố chưa quyết định làm như vậy.",
    },
    "N2_12_M2_01": {
        "共有": "共有（きょうゆう）は「分け合う・共に持つ」という意味で、読みも供給（きょうきゅう）とは異なります。",
        "教育": "教育（きょういく）は教え育てることを指し、水を避難所へ届ける意味ではありません。",
        "協力": "協力（きょうりょく）は力を合わせることです。必要な物資を届ける場合は供給（きょうきゅう）です。",
    },
    "N2_12_M2_02": {
        "改選": "改選（かいせん）は役員などを選び直すことです。読みは「かいぜん」ではありません。",
        "回線": "回線（かいせん）は通信の経路を指し、制度の問題点を直すことではありません。",
        "開戦": "開戦（かいせん）は戦争を始めることです。制度を改善する意味とは異なります。",
    },
    "N2_12_M2_03": {
        "増刷": "増刷（ぞうさつ）は印刷物を追加で刷ることです。表示設備を追加する場合は増設です。",
        "増築": "増築（ぞうちく）は建物の床面積や部分を増やして建てることです。読みも「ぞうせつ」と異なります。",
        "増員": "増員（ぞういん）は人員を増やすことです。案内表示を追加する意味ではありません。",
    },
    "N2_12_M2_04": {
        "行進": "行進（こうしん）は列を作って進むことです。ウェブ上の情報を書き換える意味ではありません。",
        "後進": "後進（こうしん）は後ろへ進むこと、または後輩を指します。情報の更新とは異なります。",
        "交信": "交信（こうしん）は無線などで連絡を取り合うことです。情報を新しくする場合は更新です。",
    },
}


def _item(qid, type_id, category, stem, choices, key_index, explanation_vi,
          *, topic="public-life", difficulty=2, context=None, extra=None):
    if len(choices) != 4 or not 0 <= key_index < 4:
        raise ValueError(f"Invalid item: {qid}")
    indexed = list(enumerate(choices))
    _rng.shuffle(indexed)
    options = [{"id": LETTERS[i], "text": text} for i, (_, text) in enumerate(indexed)]
    key = LETTERS[next(i for i, (old, _) in enumerate(indexed) if old == key_index)]
    key_text = choices[key_index]
    explanation_vi = VI_EXPLANATIONS.get(qid, explanation_vi)
    row = {
        "id": qid, "level": "N2", "typeId": type_id, "category": category,
        "stem": stem, "options": options, "correctAnswer": key,
        "explanation": f"正解は「{key_text}」です。",
        "explanationVi": explanation_vi,
        "distractorExplanations": {
            option["id"]: DISTRACTOR_VI.get(qid, {}).get(
                option["text"],
                f"Phương án «{option['text']}» không khớp với dữ kiện được hỏi. {explanation_vi}",
            )
            for option in options if option["id"] != key
        },
        "topicTag": topic, "difficultyBand": difficulty,
        "distractorStrategy": "意味・文脈の対比", "skill": "Language Knowledge",
    }
    if context:
        row["contextPassage"] = context
        row["passage"] = context
    if extra:
        row.update(extra)
    return row


def _star(qid, fragments, explanation_vi, sentence, topic="community"):
    if len(fragments) != 4:
        raise ValueError(f"STAR needs four fragments: {qid}")
    if "★" in sentence or sentence != "".join(fragments):
        raise ValueError(f"STAR assembled sentence and fragments disagree: {qid}")
    indexed = list(enumerate(fragments))
    _rng.shuffle(indexed)
    options = [{"id": LETTERS[i], "text": text} for i, (_, text) in enumerate(indexed)]
    ids_by_source_index = {source_i: LETTERS[i] for i, (source_i, _) in enumerate(indexed)}
    star_id = ids_by_source_index[2]
    order = "→".join(ids_by_source_index[i] for i in range(4))
    return {
        "id": qid, "level": "N2", "typeId": "N2-GR-STAR", "category": "文の組み立て",
        "stem": "次の文を完成させるとき、★に入る部分はどれか。\n（　　）（　　）★（　　）",
        "options": options, "correctAnswer": star_id,
        "explanation": "語句の係り受けを確認して文を組み立てます。",
        "explanationVi": explanation_vi,
        "distractorExplanations": {
            option["id"]: f"Cụm «{option['text']}» không chiếm vị trí ★ trong trật tự tự nhiên. {explanation_vi}"
            for option in options if option["id"] != star_id
        },
        "topicTag": topic, "difficultyBand": 2,
        "assembledSentence": sentence, "starredOptionText": fragments[2],
        "starPosition": 3, "fragmentOrder": order,
        "starValidationSchema": "DISPLAYED_FRAGMENT_ORDER_V1",
        "distractorStrategy": "語順・係り受け", "skill": "Language Knowledge",
    }


def get_n2_mock_12_sec1_items(seed=48):
    _rng.seed(seed)
    q = []

    # M1 Kanji readings (5)
    rows = [
        ("市は新しい分別方法を試すため、三つの地区でその方法を【実施】することにした。", ["じっし", "じつし", "じっじ", "じつじ"], 0, "実施（じっし）は計画や方法を実際に行うことです。句中の「その方法」が実施する対象を示しています。"),
        ("台風の後、川の水位が【急激】に上がったため、住民に注意を呼びかけた。", ["きゅうげき", "きゅうけき", "きゅげき", "きゅうげっき"], 0, "急激（きゅうげき）は変化が急で大きいことです。水位が短時間に大きく上がった様子を表します。"),
        ("町内会は、古い遊歩道の【維持】に必要な費用を見直している。", ["いじ", "いし", "ゆいじ", "ゆいし"], 0, "維持（いじ）は、状態を保って続けることです。遊歩道を使える状態に保つ費用を指します。"),
        ("自治体は、空き家の増加を防ぐ対策を【講じた】。", ["こうじた", "こうした", "こういた", "こうじいた"], 0, "講じる（こうじる）は問題に対して手段を取ることです。「対策を講じる」という連語です。"),
        ("この調査は、世代による意識の【差異】を明らかにする目的で行われた。", ["さい", "しゃい", "さえ", "しゃえ"], 0, "差異（さい）は互いの違いを表します。調査対象の世代間にある意識の違いです。"),
    ]
    for i, (stem, choices, key, vi) in enumerate(rows, 1):
        q.append(_item(f"N2_12_M1_{i:02}", "N2-MO-READ", "漢字読み", stem, choices, key, vi, topic="environment", extra={"targetKanji": stem[stem.find("【")+1:stem.find("】")]}))

    # M2 Orthography (5)
    rows = [
        ("市は、災害時に水を各避難所へ【きょうきゅう】する計画を作った。", ["供給", "共有", "教育", "協力"], 0, "供給（きょうきゅう）は必要な物を相手や地域へ届けることです。避難所へ水を届ける計画なので適切です。"),
        ("制度の問題点を直すため、利用者の意見を反映した【かいぜん】案をまとめた。", ["改善", "改選", "回線", "開戦"], 0, "改善（かいぜん）は問題点を直して、よりよい状態にすることです。制度の問題点を直す案に合います。"),
        ("観光客が増えたため、駅前に案内表示を新たに【ぞうせつ】した。", ["増設", "増刷", "増築", "増員"], 0, "増設（ぞうせつ）は設備や施設を追加して設けることです。駅前に案内表示を新たに設ける文脈に合います。"),
        ("市は、災害時の避難所情報をウェブサイトで【こうしん】した。", ["更新", "行進", "後進", "交信"], 0, "更新（こうしん）は古い情報を新しい内容に改めることです。ウェブサイト上の避難所情報を書き換える文脈に合います。"),
        ("調査では、年齢ではなく利用目的を【じゅうし】して分析した。", ["重視", "従事", "充実", "重示"], 0, "重視は大切な点として扱うことです。利用目的を主な分析軸にした場面です。"),
    ]
    for i, (stem, choices, key, vi) in enumerate(rows, 1):
        q.append(_item(f"N2_12_M2_{i:02}", "N2-MO-ORTH", "表記", stem, choices, key, vi, topic="public-service", extra={"readingTarget": stem[stem.find("【")+1:stem.find("】")]}))

    # M3 Word formation (5)
    rows = [
        ("人口の減少に備えて、行政サービスの効率（　）を進める。", ["化", "的", "性", "者"], 0, "「効率化」は効率を高める方向へ変えることです。「効率的」は性質を表す形容動詞になり、ここでは「進める」の目的語になりません。"),
        ("地域間で比較（　）を確保するため、各地で同じ質問を使って調査した。", ["可能性", "化", "的", "者"], 0, "「比較可能性」は地域どうしの結果を比べられる性質です。同じ質問を使って、その比較可能性を確保しています。"),
        ("公共施設の予約をオンライン（　）し、窓口の混雑を減らした。", ["化", "性", "的", "者"], 0, "オンライン化は従来の手続きをオンラインで行える形に変えることです。「オンライン化する」が自然です。"),
        ("この制度は、利用者が自分で手続きを進められる自主（　）を重視する。", ["性", "化", "者", "的"], 0, "自主性は自分の判断で行う性質です。「自主化」では制度の重視点にならず、ここでは性質を表す性が合います。"),
        ("地域の清掃活動を通じて、住民の連帯（　）が高まった。", ["感", "化", "的", "者"], 0, "連帯感は互いに支え合う仲間だという気持ちです。「連帯感が高まる」という形で使います。"),
    ]
    for i, (stem, choices, key, vi) in enumerate(rows, 1):
        q.append(_item(f"N2_12_M3_{i:02}", "N2-MO-FORM", "語形成", stem, choices, key, vi, topic="community"))

    # M4 Contextual vocabulary (7)
    rows = [
        ("橋の点検が終わるまで、車両の通行を（　）することになった。", ["規制", "許可", "統制", "抑止"], 0, "橋の点検中に車両の通行を制限するため、「通行を規制する」が自然です。「許可する」は通行を認める意味です。「統制」は交通全体の運営・管理を指すことが多く、「抑止」は行為や発生を防ぐ語で、通行への一般的な組み合わせは「規制」です。"),
        ("大雨の予報を受け、市は避難所を早めに（　）した。", ["開設", "開発", "公開", "展開"], 0, "避難所を利用できる状態にすることは「開設する」です。開発は新たに作ることを指します。"),
        ("歩道が狭く危険なため、設計を（　）から工事を始める。", ["見直して", "見落として", "見送って", "見合わせて"], 0, "問題点を確認して設計を再検討する意味の「見直す」が合います。"),
        ("二つの地区で同じ質問と集計方法を使い、回答傾向を地域間で（　）できるようにした。", ["比較", "記録", "照合", "検証"], 0, "両地区の回答傾向を比べられるよう、質問と集計方法をそろえています。「記録する」は保存、「照合する」は別の記録と突き合わせる、「検証する」は正しさを確かめる意味で、この文の目的とは異なります。"),
        ("大雨対策として、公園の地下に雨水をためる調整池を（　）した。", ["設置", "設定", "制定", "指定"], 0, "設置する là xây hoặc bố trí một thiết bị/công trình tại chỗ. Bể điều hòa được xây dưới công viên để giữ nước mưa.",),
        ("住民説明会では、専門用語を避け、内容を分かりやすく（　）した。", ["説明", "解釈", "解決", "解消"], 0, "情報の意味を相手に伝える行為は「説明する」です。解釈は意味を受け取って理解する側の行為です。"),
        ("利用者の減少が続いた路線について、市は運行方法を（　）する。", ["再検討", "再現", "再生", "再生産"], 0, "現状を踏まえてもう一度考えることを表す「再検討」が自然です。"),
    ]
    for i, (stem, choices, key, vi) in enumerate(rows, 1):
        q.append(_item(f"N2_12_M4_{i:02}", "N2-MO-CONT", "文脈規定", stem, choices, key, vi, topic="public-service"))

    # M5 Paraphrases (5)
    rows = [
        ("市は、住民の要望を踏まえて公園の設備を改修した。", ["要望を考慮して", "要望を取り消して", "要望を先送りして", "要望を誇張して"], 0, "「踏まえて」は、情報や意見を考慮したうえで、という意味です。"),
        ("この運行計画は、実際の利用状況に即している。", ["利用状況に合っている", "利用状況を隠している", "利用状況を増やしている", "利用状況を無視している"], 0, "「～に即している」は実情や基準に合っていることです。"),
        ("作業の負担を軽減するため、申請書の項目を減らした。", ["負担を小さくする", "負担を均等にする", "負担を予測する", "負担を引き受ける"], 0, "軽減は程度や量を小さくすることです。項目を減らして作業量を下げています。"),
        ("一部の住民から異論が出たため、決定を保留した。", ["結論をすぐに出さず、後で判断することにした", "決定を正式に発表した", "決定を取り消した", "決定を急いだ"], 0, "保留は、すぐに結論を出さず、あとで扱うために判断を止めておくことです。反対意見があっても決定を取り消したわけではありません。"),
        ("新しい制度は、地区を問わず利用できる。", ["地区に関係なく", "地区を限定して", "地区を通過して", "地区と比較して"], 0, "「～を問わず」は条件や区別に関係なく、という意味です。"),
    ]
    for i, (stem, choices, key, vi) in enumerate(rows, 1):
        q.append(_item(f"N2_12_M5_{i:02}", "N2-MO-PARA", "言い換え", stem, choices, key, vi, topic="community"))

    # M6 Usage (5)
    rows = [
        ("「見合わせる」が「実施を一時的に控える」という意味で使われている文はどれか。", ["強風のため、橋の補修工事は安全が確認できるまで見合わせた。", "担当者は二つの資料を見合わせ、違いを確認した。", "会議の後、二人は顔を見合わせて驚いた。", "支出額を昨年度の記録と見合わせ、差を調べた。"], 0, "工事をいったん延期して様子を見る用法です。ほかは資料や数字を比べる、または互いに顔を見る意味です。"),
        ("「負担」が「人にかかる労力や不便」という意味で使われている文はどれか。", ["坂道の多い地区では、徒歩での買い物が高齢者の負担になっている。", "修理費は市が全額負担する。", "保険料の一部を会社が負担する。", "施設の維持費の負担割合を住民と市で決めた。"], 0, "徒歩で買い物に行く体力や不便さが人にかかる意味です。ほかは費用の支払いまたは分担を表します。"),
        ("「見込む」が「能力を評価して役割を任せる」という意味で使われている文はどれか。", ["町長は彼の調整力を見込んで、地域協議会の委員長を任せた。", "市は来年の来場者を二万人と見込んでいる。", "事業費には維持費も見込んでおく。", "窓から向かいの山を見込むことができる。"], 0, "経験を評価して役割を任せる意味です。ほかは数を予測する、費用を含めて計算する、景色を見渡す用法です。"),
        ("「応じる」が「依頼を引き受ける」という意味で使われている文はどれか。", ["専門家は、市民団体からの講演依頼に応じた。", "市は人口の変化に応じて、窓口の数を調整した。", "体調に応じて、運動の量を変えてください。", "利用者数に応じて、バスの本数を増やした。"], 0, "講演依頼を受け入れた意味です。ほかは状況や数に合わせて内容を変える用法です。"),
        ("「支える」が「活動を続けられるよう助ける」という意味で使われている文はどれか。", ["住民の寄付が、閉鎖の危機にあった図書館の活動を支えた。", "橋脚が道路の重さを支えている。", "担当者は重い箱を両手で支えて運んだ。", "手すりを支えにして階段を下りた。"], 0, "寄付によって図書館の運営を続けられた意味です。ほかは物や体を物理的に保持する用法です。"),
    ]
    for i, (stem, choices, key, vi) in enumerate(rows, 1):
        q.append(_item(f"N2_12_M6_{i:02}", "N2-MO-USE", "用法", stem, choices, key, vi, topic="community", difficulty=3))

    # M7 Sentence grammar (12)
    rows = [
        ("市の統計では、人口が減っているのは事実である（　）、駅前の商店街には新しい店が増えている。", ["ものの", "ばかりに", "からには", "どころか"], 0, "市の統計で確認された人口減少を事実として認めたうえで、予想とは異なり新しい店が増えていると述べるため、「ものの」が適切です。"),
        ("対策を先延ばしにすると、被害がさらに広がり（　）。", ["かねない", "がたい", "きれない", "かける"], 0, "「～かねない」は好ましくない結果が起こる可能性を示します。被害拡大の懸念を表します。"),
        ("利用者の声を記録した（　）、必要な改善点をすぐに見つけられた。", ["ことによって", "ものの", "ことなしに", "うちに"], 0, "「ことによって」は行為が結果を生み出す関係を示します。記録した後、改善点を見つけられたという因果関係です。"),
        ("年齢（　）、希望する人は誰でも防災講座に参加できる。", ["を問わず", "に限って", "に沿って", "に対して"], 0, "「～を問わず」は条件に関係なくという意味です。年齢で参加者を限定しない文に合います。"),
        ("この公園は、春の花（　）秋の紅葉も楽しめる。", ["に限らず", "に先立ち", "に応じて", "を通して"], 0, "「～に限らず」はそれだけでなく、という意味です。春に加えて秋の景色も楽しめます。"),
        ("安全性を確かめた（　）、市は新しい遊具の設置を許可した。", ["うえで", "ものの", "うちに", "とはいえ"], 0, "「Vたうえで」は、前の行為を終えてから次の行為をする順序を示します。安全性を確認した後に市が設置を許可しています。"),
        ("条例の改正（　）、ごみの出し方も一部変更される。", ["に伴って", "に先立って", "を問わず", "とともにして"], 0, "「～に伴って」は一つの変化と同時に別の変化が起こることを示します。"),
        ("町の中心部に住んでいる（　）、車を使わずに生活できるとは限らない。", ["からといって", "ものなら", "に応じて", "どころか"], 0, "「～からといって～とは限らない」は前件だけで結論を出せないことを表します。"),
        ("災害への備えは、自治体だけ（　）住民一人ひとりにも必要だ。", ["でなく", "を通じて", "に比べて", "にかけて"], 0, "「～だけでなく～も」は対象を追加します。行政に限らず住民にも備えが必要です。"),
        ("この調査は、複数の地域に（　）三年間続けられた。", ["わたって", "向けて", "限って", "対して"], 0, "「～にわたって」は範囲や期間が広く続くことを表します。"),
        ("公共交通の維持をめぐる議論は、交通手段の選択（　）地域の公平さにも関係する。", ["にとどまらず", "に先立って", "に限って", "を問わず"], 0, "「～にとどまらず」は範囲がその点だけに収まらないことです。交通手段に加えて公平さにも及びます。"),
        ("市の防災情報を受け取ると決めた（　）、登録した住所が正しいか定期的に確認してほしい。", ["からには", "にしても", "からといって", "ことだから"], 0, "「～からには」は、そうすると決めた以上は責任や必要な行動が伴うことを示します。防災情報を受け取る登録をした人には、住所を最新に保つよう求めています。"),
    ]
    for i, (stem, choices, key, vi) in enumerate(rows, 1):
        q.append(_item(f"N2_12_M7_{i:02}", "N2-GR-FORM", "文法形式", stem, choices, key, vi, topic="public-life", difficulty=3))

    # M8 STAR ordering (5)
    stars = [
        (["申請者が提出した", "書類を受付で", "確認し、", "不足があればその場で知らせた"], "申請者が提出した書類を受付で確認し、不足があればその場で知らせた", "Cụm ★ là 「確認し、」. Câu hoàn chỉnh: 申請者が提出した書類を受付で確認し、不足があればその場で知らせた. 「申請者が提出した」 là mệnh đề bổ nghĩa cho 書類を; tân ngữ này phải đứng trước động từ 確認し、. Phần kết nêu hành động tiếp theo nếu giấy tờ thiếu."),
        (["まず回答を集計し、", "個人情報が含まれていないか", "公開前に担当者が確認し、", "必要に応じて該当箇所を修正する"], "まず回答を集計し、個人情報が含まれていないか公開前に担当者が確認し、必要に応じて該当箇所を修正する", "Cụm ★ là 「公開前に担当者が確認し、」. Câu hoàn chỉnh: まず回答を集計し、個人情報が含まれていないか公開前に担当者が確認し、必要に応じて該当箇所を修正する. Mệnh đề nghi vấn với 「ないか」 làm nội dung được kiểm tra nên phải đứng trước 「確認し」; nếu cần thì chỉnh sửa sau đó."),
        (["市が指定した", "避難場所を", "事前に確認し、", "必要な物資を準備しておく"], "市が指定した避難場所を事前に確認し、必要な物資を準備しておく", "Cụm ★ là 「事前に確認し、」. Câu hoàn chỉnh: 市が指定した避難場所を事前に確認し、必要な物資を準備しておく. 「市が指定した」 bổ nghĩa trực tiếp cho danh từ 避難場所; tân ngữ 避難場所を phải đứng trước động từ 確認し、, rồi mới đến hành động chuẩn bị vật dụng cần thiết."),
        (["市は", "買い物が難しい人に", "食料品を届けるための移動販売車を導入し、", "週に二回運行する"], "市は買い物が難しい人に食料品を届けるための移動販売車を導入し、週に二回運行する", "Cụm ★ là 「食料品を届けるための移動販売車を導入し、」. Câu hoàn chỉnh: 市は買い物が難しい人に食料品を届けるための移動販売車を導入し、週に二回運行する. Cụm 「人に」 gắn với hành động giao thực phẩm; 「週に二回運行する」 nêu tần suất vận hành sau khi xe được đưa vào."),
        (["複数の案が出た場合には", "短期的な費用だけでなく", "将来の維持費も", "比較したうえで決める"], "複数の案が出た場合には短期的な費用だけでなく将来の維持費も比較したうえで決める", "Cụm ★ là 「将来の維持費も」. Câu hoàn chỉnh: 複数の案が出た場合には短期的な費用だけでなく将来の維持費も比較したうえで決める. Cấu trúc だけでなく…も ghép hai khoản phí làm đối tượng so sánh trước động từ 決める."),
    ]
    for i, (fragments, sentence, vi) in enumerate(stars, 1):
        q.append(_star(f"N2_12_M8_{i:02}", fragments, vi, sentence, topic="community"))

    # M9 Continuous-text grammar (5)
    cloze = [
        ("市は、高齢者向けの予約制乗合車について、時間帯ごとの利用状況を調査した。朝は予約が多く、夕方は空席が目立つことが分かった。調査結果（　）、朝の便を一つ増やし、夕方の一部を予約制の小型車に変更する案を示した。実施後も、乗車できなかった人の数を確認するという。", ["を踏まえて", "に先立って", "を問わず", "を通じて"], 0, "「を踏まえて」は、すでに分かった事実を考慮して次の判断をすることです。調査で朝の予約が多く夕方に空席があると分かり、その結果に基づく運行案を示しています。"),
        ("地域の清掃活動は、参加者を集めるだけでは続かない。作業の内容を事前に知らせ、無理のない時間に設定する（　）、初めて参加する人も予定を立てやすくなる。", ["ことによって", "どころか", "ものなら", "に限らず"], 0, "「ことによって」nối cách làm với kết quả: thông báo nội dung và đặt thời gian phù hợp giúp người mới dễ sắp xếp."),
        ("公共施設の再編では、全ての地域に同じ基準を当てはめるのではなく、利用者の移動距離や地域ごとの人口構成（　）施設の規模を調整する必要がある。", ["に応じて", "に先立って", "を通じて", "に加えて"], 0, "「に応じて」は条件や状況に合わせて別の事柄を変えることです。施設の規模を移動距離や地域の人口構成に合わせて調整するという関係を表し、ほかの選択肢はこの調整条件を示しません。"),
        ("再生可能エネルギーの設備を増やすと、発電量の変動に対応する工夫も求められる。設備を設置した（　）、地域の電力問題がすべて解決するわけではない。", ["からといって", "にしたがって", "ばかりに", "どころか"], 0, "「設置したからといって～わけではない」phủ định kết luận tự động rằng có thiết bị là giải quyết hết vấn đề."),
        ("住民向けの説明会では、計画の利点を伝える一方、工事中の騒音や通行制限も説明した。利点（　）課題も共有することで、参加者が判断しやすくなる。", ["だけでなく", "に限って", "に先立ち", "どころか"], 0, "「利点だけでなく課題も」nêu hai mặt song song. Vế trước có 一方 cũng báo hiệu cần trình bày cả mặt khó khăn."),
    ]
    for i, (passage, choices, key, vi) in enumerate(cloze, 1):
        q.append(_item(f"N2_12_M9_{i:02}", "N2-GR-PARA", "文章文法", "文中の（　）に入る最も適切なものはどれか。", choices, key, vi, topic="public-policy", context=passage, difficulty=3))

    # M10 Short reading (5)
    short = [
        ("市役所の窓口は、来月から毎週水曜日だけ午後七時まで開く。通常の受付時間に来られない人が対象で、予約は不要。ただし、証明書の一部は別の窓口で申請する必要がある。", "水曜日の延長時間について、本文と合うものはどれか。", ["予約をした人だけが利用できる", "通常時間に来られない人も利用できる", "すべての証明書を同じ窓口で申請できる", "毎日午後七時まで開く"], 1, "Thứ Tư mở muộn để người không thể đến trong giờ thường cũng sử dụng được. Bài đọc nói không cần đặt chỗ và một số giấy tờ cần quầy khác."),
        ("町内の公園では、今週末に樹木の剪定を行う。作業中は東側の通路を通れないが、西側の入口は利用できる。雨の場合は翌週に延期し、変更は市のウェブサイトに掲載する。", "作業中、公園を利用する人はどうすればよいか。", ["東側の通路を使う", "西側の入口から入る", "雨でも予定どおり作業する", "変更を電話でのみ確認する"], 1, "東側通路は使えませんが、西側入口は利用可能です。雨天時は延期し、市のサイトで知らせます。"),
        ("食品回収の箱は、図書館の正面入口ではなく、隣の交流センターに置かれている。未開封で期限まで一週間以上ある食品を、平日の午前九時から午後五時に受け付ける。", "食品を持ち込む場所と条件はどれか。", ["図書館の正面入口に未開封品を持っていく", "交流センターに未開封で期限まで一週間以上ある食品を持っていく", "交流センターに開封済みだが期限内の食品を持っていく", "交流センターに未開封品を平日の午後六時に持っていく"], 1, "回収場所は隣の交流センターで、食品は未開封かつ期限まで一週間以上必要です。受付は平日の9時から17時です。正解はこの三条件を満たし、ほかは場所、開封状態または受付時刻が本文と異なります。"),
        ("市民プールは設備点検のため、二十日から二十二日まで休館する。水泳教室の振替日は二十五日で、通常の入館券は休館中も有効期限が延長される。", "休館に伴う対応として正しいものはどれか。", ["教室は中止され、振替日はない", "入館券の期限は延長される", "休館は二十五日まで続く", "点検中も通常どおり利用できる"], 1, "休館中は券の有効期限が延長され、水泳教室には二十五日の振替日があります。"),
        ("移動図書館は、来月から山側の三地区を回る順番を変更する。各地区での到着時刻と滞在時間は現在のままにし、巡回順の変更に伴い、図書館を出る時刻だけを十五分早める。", "時刻について変更されるのは何か。", ["各地区での滞在時間", "巡回する地区の数", "図書館を出発する時刻", "各地区に着く時刻"], 2, "巡回順は変わりますが、各地区の到着時刻と滞在時間は現状のままです。本文が変更すると明記しているのは、図書館を出る時刻だけで、15分早くなります。"),
    ]
    for i, (passage, stem, choices, key, vi) in enumerate(short, 1):
        q.append(_item(f"N2_12_M10_{i:02}", "N2-RD-SHORT", "短文読解", stem, choices, key, vi, topic="public-service", context=passage))

    # M11 Medium reading (3 passages × 3 questions)
    medium = [
        ("市の環境課は、家庭ごみの量を減らすため、食品ロス対策の実証事業を始めた。協力店では、閉店前に残った食品を割引して販売する。市は当初、値引きの割合を店ごとに任せていたが、利用者から『どの程度安くなるか分からず、選びにくい』という声が出た。そこで、割引率を三段階の表示にそろえたところ、買い手が比較しやすくなり、店員の説明も短くなった。一方、すべての商品を同じ割合で値引きすると、保存可能な日数の違いが反映されないという課題も残った。市は、売れ残りの件数だけでなく、廃棄量と利用者の意見も確認し、事業を続けるか判断する予定である。",
         [
            ("市が割引率の表示をそろえたのはなぜか。", ["店ごとの販売時間を同じにするため", "値引きの程度を利用者が比べやすくするため", "すべての商品を無料にするため", "店員の説明を詳しくするため"], 1, "利用者が値引き幅を比べられず選びにくいと言ったため、三段階表示に統一しました。"),
            ("表示をそろえた後に起きた変化はどれか。", ["廃棄量がゼロになった", "店員が説明する時間が短くなった", "すべての商品を同じ割合で値引きすることにした", "保存日数の差が解消された"], 1, "本文は表示を三段階にそろえた後、買い手が比較しやすくなり、店員の説明も短くなったと述べています。同じ値引き率を全商品に適用することは、なお残る課題として挙げられています。"),
            ("市が今後判断する際に見るものは何か。", ["売れ残り件数だけ", "商品の価格だけ", "廃棄量や利用者の意見も含む複数の情報", "参加店の売上順位"], 2, "継続判断では売れ残り件数に加え、廃棄量と利用者の意見も確認するとあります。"),
         ]),
        ("山間部の移動手段を守るため、町は路線バスの一部を予約制の乗合車に切り替えた。従来のバスは決まった時刻に全ての停留所を回るため、利用者が少ない日も運行費がかかっていた。乗合車は予約のあった地区を通り、病院や買い物施設の近くで乗り降りできる。開始直後は予約方法が分かりにくいという声があり、町は電話の受付時間を延ばし、停留所にも説明を掲示した。利用者は増えたが、予約が重なる朝には希望時刻から遅れる場合がある。町は、費用だけを基準にせず、通院や通学に必要な時間帯が確保できているかを見ながら、運行範囲を調整する考えだ。",
         [
            ("町が乗合車を導入した背景は何か。", ["全ての停留所をなくすため", "利用が少ない日も定時運行の費用がかかっていたため", "病院が町外に移転したため", "運転手を増やすため"], 1, "利用者が少ない日でも定時バスの運行費が必要だったことが背景です。"),
            ("町が受付時間を延ばしたのは何のためか。", ["朝の遅れを隠すため", "予約方法が分かりにくいという声に対応するため", "予約を不要にするため", "運行範囲を縮めるため"], 1, "利用者が予約方法を理解しやすいよう、電話受付時間を延ばし案内も掲示しました。"),
            ("町が運行範囲を調整するとき重視する点はどれか。", ["費用を最小にすることだけ", "すべての利用者を同時に運ぶこと", "通院・通学に必要な時間帯を保てるか", "以前の路線を完全に再現すること"], 2, "費用だけでなく、通院・通学に必要な時間帯が確保できているかを見ます。"),
         ]),
        ("市の図書館では、利用者が本を予約して受け取る仕組みを見直した。以前は中央館に届いた本を分館へ運ぶ回数が限られており、受け取りまで長く待つ場合があった。そこで、予約が多い本は複数館に置き、各館の貸し出し状況を共通システムで確認できるようにした。導入後、平均待ち日数は短くなったが、利用が一部の館に集中する本もあり、追加購入の判断が難しい。図書館は貸し出し件数だけでなく、予約の取り消しや利用者の希望も見ながら、所蔵数を調整する方針である。",
         [
            ("図書館が仕組みを見直した主な目的は何か。", ["本を中央館だけに集めるため", "予約本を受け取るまでの待ち時間を減らすため", "利用者の予約を取り消すため", "分館の貸し出しを停止するため"], 1, "分館への輸送回数が少なく、受取まで待つ問題を改善するのが目的です。"),
            ("導入後にも残っている課題は何か。", ["予約システムが全館で使えない", "人気の偏りがあり、購入冊数を決めにくい", "平均待ち日数が必ず長くなった", "利用者の希望を聞けなくなった"], 1, "待ち日数は短くなりましたが、特定館に利用が集中する本の追加購入は判断しにくいとあります。"),
            ("所蔵数を調整する際に図書館が見る情報は何か。", ["貸し出し件数だけ", "館の建物の広さだけ", "貸出・取消し・利用者希望など", "職員の勤務年数"], 2, "貸出数だけでなく予約取消しや希望も確認すると書かれています。"),
         ]),
    ]
    n = 1
    for passage, questions in medium:
        for stem, choices, key, vi in questions:
            q.append(_item(f"N2_12_M11_{n:02}", "N2-RD-MED", "中文読解", stem, choices, key, vi, topic="public-policy", context=passage))
            n += 1

    # M12 Paired viewpoints (2)
    paired = "【意見A】\n市は、中心部の駐車場を減らし、その場所を歩行者と自転車が安全に通れる空間に変えるべきだ。短い距離の移動がしやすくなれば、商店に立ち寄る人も増える。駐車場をただなくすのではなく、郊外の駐車施設とバスの接続を整えれば、車が必要な人にも配慮できる。\n\n【意見B】\n中心部の駐車場を急に減らすのは賛成できない。高齢者や荷物を運ぶ人には車が欠かせず、郊外の駐車施設へ移る時間も負担になる。まずは時間帯によって道路を歩行者中心にする試験を行い、売上や交通量への影響を測るべきだ。結果を見てから駐車場の数を決めても遅くない。"
    q.append(_item("N2_12_M12_01", "N2-RD-PAIR", "統合理解", "意見Aと意見Bに共通している考えは何か。", ["車をすぐ全面禁止するべきだ", "駐車場のあり方を考える際、車が必要な人への配慮も欠かせない", "駐車場を現在の数より必ず増やすべきだ", "商店の売上は交通政策と関係がない"], 1, "Aは郊外の駐車施設とバスの接続で車が必要な人に配慮し、Bも高齢者や荷物を運ぶ人には車が欠かせないと述べています。方法は異なりますが、駐車場のあり方を考える際に車が必要な人への配慮も欠かせない点が共通しています。", topic="transport", context=paired))
    q.append(_item("N2_12_M12_02", "N2-RD-PAIR", "統合理解", "意見Aと意見Bの相違として最も適切なものはどれか。", ["Aは駐車場削減を進める案を示し、Bは影響を測ってから決める段階的な案を示す", "Aはバスをなくし、Bは全ての車を禁止する", "Aは郊外施設に反対し、Bは商店街の閉鎖を求める", "AもBもすぐに駐車場を倍増するよう求める"], 0, "Aは駐車場を減らして歩行空間を広げる立場です。Bはまず時間帯別の試験を行い、結果を見てから数を決める立場です。", topic="transport", context=paired))

    # M13 Long reading (3)
    long_passage = "市は、十年前から続けてきた河川沿いの護岸工事を一部見直すことにした。これまでは大雨による浸水を防ぐため、川幅を広げ、岸をコンクリートで固める計画を中心に進めていた。しかし、最近の調査で、工事区間の下流では流れが速くなり、魚が産卵する浅瀬が減っていることが分かった。そこで市は、堤防を高くするだけでなく、川の一部に水が広がる場所を設け、植物が育つ岸辺を残す案を検討している。\n\nこの案に対して、近くに住む人の中には、植物を残すと草刈りの費用が増え、見通しも悪くなるのではないかと心配する声がある。一方、環境団体は、川の流れを複数に分ければ生き物のすみかを守りながら水害に備えられると期待している。市は、どちらか一方の意見だけで決めず、草刈りの頻度や水位の変化を小さな区間で確かめることにした。\n\n試験区間では、地元の住民にも月一回の観察会に参加してもらう。観察会は専門知識を持つ人だけの調査ではなく、普段川を利用する人が変化に気づき、記録を共有する機会でもある。市は、観察結果を工事の設計に反映させるが、参加人数の多さだけで案の良し悪しを判断しない。安全性、維持費、生態系の変化を合わせて評価し、二年後に本格工事の範囲を決める予定だ。"
    long_items = [
        ("市が護岸工事を見直すきっかけとなった調査結果は何か。", ["下流の流れが速まり、魚の産卵場所が減っていた", "川幅が広がりすぎて船が通れなくなった", "草刈りの費用が十年前より下がった", "環境団体が工事の中止を決定した"], 0, "調査によって、下流の流れが速くなり魚の産卵場所である浅瀬が減ったことが分かりました。"),
        ("市が小さな区間で試験を行う理由は何か。", ["草刈りや水位への懸念を実際に確かめるため", "本格工事の範囲をすぐに決定するため", "住民の意見を集めずに済ませるため", "環境団体の案をそのまま採用するため"], 0, "住民の心配と環境団体の期待の両方があるため、草刈り頻度や水位変化を試験区間で確かめます。"),
        ("本文から分かる、市の観察会に対する考えはどれか。", ["参加人数が多ければ計画の安全性も証明される", "住民の観察を記録として使うが、評価は複数の基準で行う", "専門家以外は川の変化を記録できない", "観察結果は工事設計に反映しない"], 1, "住民にも変化を記録してもらい設計に生かしますが、人数の多さだけでは判断せず、安全性・維持費・生態系を合わせて評価します。"),
    ]
    for i, (stem, choices, key, vi) in enumerate(long_items, 1):
        q.append(_item(f"N2_12_M13_{i:02}", "N2-RD-LONG", "長文読解", stem, choices, key, vi, topic="environment-policy", context=long_passage, difficulty=3))

    # M14 Information retrieval (2)
    notice = "【地域防災講座】\n日時：6月15日（日）10:00～12:00\n会場：北区民センター 2階講義室\n対象：市内在住・在勤の人（先着40名）\n申込：6月10日までに電話または市ウェブサイト\n内容：避難所の確認、非常持出品の選び方\n※筆記用具を持参。駐車場は利用できません。"
    q.append(_item("N2_12_M14_01", "N2-RD-INFO", "情報検索", "防災講座に参加するための条件として正しいものはどれか。", ["6月10日までに申し込み、先着順で参加する", "市外在住者だけが申し込める", "当日、駐車場を利用して参加する", "筆記用具は会場で配られる"], 0, "申込期限は6月10日で、定員40名の先着順です。市内在住・在勤が対象で、駐車場は使えず筆記用具を持参します。", topic="public-service", context=notice))
    q.append(_item("N2_12_M14_02", "N2-RD-INFO", "情報検索", "講座で扱う内容はどれか。", ["地域の歴史と観光案内", "避難所の確認と非常持出品", "自動車の安全点検", "河川工事の設計方法"], 1, "講座内容として避難所の確認と非常持出品の選び方が記載されています。", topic="public-service", context=notice))

    if len(q) != 75 or len({item["id"] for item in q}) != 75:
        raise ValueError(f"M12 Section 1 must contain 75 unique items; got {len(q)}")
    return q
