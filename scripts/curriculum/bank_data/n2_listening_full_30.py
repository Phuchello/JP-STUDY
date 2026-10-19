# -*- coding: utf-8 -*-
"""
JLPT N2 Mock Exam #01 - Section 2: Listening Comprehension (聴解)
Full 30-item exam structure:
- Mondai 1: 課題理解 (5 items)
- Mondai 2: ポイント理解 (6 items)
- Mondai 3: 概要理解 (5 items)
- Mondai 4: 即時応答 (11 items)
- Mondai 5: 統合理解 (3 items)
Total: 30 items
"""

def get_n2_listening_30_items():
    items = []

    # =========================================================================
    # MONDAI 1: 課題理解 (Task-based Comprehension - 5 items)
    # =========================================================================
    m1_data = [
        (
            "N2-M1-L01",
            "Mondai 1: 課題理解 (Task) — 企画書の修正",
            """男の人と女の人が会社で話しています。男の人はこの後、まず何をしなければなりませんか。

男：「課長、来期の新商品キャンペーンの企画書を作成したのですが、ご確認いただけますでしょうか。」
女：「ええ、見せて。……全体のコンセプトは斬新でとてもいいわね。ただ、予算の試算表が少し大雑把すぎる気がするわ。原材料費の高騰も考慮して、詳細な内訳を出し直してほしいの。それから、宣伝部の田中さんにも意見を聞いておいてね。」
男：「分かりました。田中さんへの相談は、予算表を作り直した後の方がよろしいでしょうか。」
女：「そうね。数字が固まっていないと具体的な話ができないから、まずは予算の再計算を最優先でお願いね。プレゼン資料の作成はその後でいいから。」
男：「承知いたしました。すぐに取りかかります。」""",
            "男の人はこの後、まず何をしなければなりませんか。",
            [
                ("A", "新商品のプレゼン資料を作成する。"),
                ("B", "宣伝部の田中さんに相談に行く。"),
                ("C", "企画全体のコンセプトを考え直す。"),
                ("D", "予算の詳細な内訳を再計算する。")
            ],
            "D",
            "Trưởng phòng chỉ thị rõ ràng: '数字が固まっていないと具体的な話ができないから、まずは予算の再計算を最優先でお願いね' (Trước tiên hãy ưu tiên tính toán lại bảng phân bổ ngân sách chi tiết). Việc gặp Tanaka hay làm slide thuyết trình là bước tiếp sau.",
            {
                "A": "Nữ trưởng phòng nói rõ: 'プレゼン資料の作成はその後でいい' (việc làm slide thuyết trình để sau).",
                "B": "Trưởng phòng đồng ý là phải xong bảng dự toán số liệu trước mới đi hỏi ý kiến Tanaka.",
                "C": "Trưởng phòng khen ngợi: 'コンセプトは斬新でとてもいい' (ý tưởng rất mới mẻ), không yêu cầu sửa concept."
            },
            1
        ),
        (
            "N2-M1-L02",
            "Mondai 1: 課題理解 (Task) — 引越しの手配",
            """夫婦が引越しの準備について話しています。夫はこの後、何をしますか。

女：「来週の引越し、不用品の処分はどうなった？」
男：「粗大ゴミの収集はもう予約したよ。ダンボールも届いたから、本や服は週末に詰めるよ。」
女：「助かるわ。あ、電気とガスの使用停止の手続きはネットでしたんだけど、水道局だけは電話で連絡しなきゃいけないの。今日の午後5時までだから、お願いできる？」
男：「分かった、今すぐ電話しておくよ。インターネット回線の移転手続きは？」
女：「それは私が昨日プロバイダに連絡したから大丈夫。」""",
            "夫はこの後、何をしますか。",
            [
                ("A", "水道局に電話をかける。"),
                ("B", "粗大ゴミの収集を予約する。"),
                ("C", "ダンボールに本や服を詰める。"),
                ("D", "インターネットプロバイダに連絡する。")
            ],
            "A",
            "Người vợ nhờ: '水道局だけは電話で連絡しなきゃいけないの... 今日の午後5時までだから、お願いできる？' Người chồng đáp: '分かった、今すぐ電話しておくよ' (Anh hiểu rồi, anh sẽ gọi điện cho cục cấp nước ngay bây giờ).",
            {
                "B": "Người chồng đã đặt lịch thu gom rác cồng kềnh xong từ trước ('もう予約したよ').",
                "C": "Việc đóng thùng sách vở/quần áo dự định cuối tuần mới làm ('週末に詰めるよ').",
                "D": "Người vợ đã liên hệ nhà mạng internet từ hôm qua ('私が昨日プロバイダに連絡した')."
            },
            2
        ),
        (
            "N2-M1-L03",
            "Mondai 1: 課題理解 (Task) — 出張の手配",
            """会社の出張手配で、男性社員と女性社員が話しています。女性社員はこの後、まず何をしますか。

男：「来月の大阪出張だけど、ホテルの予約は取れた？」
女：「駅前のビジネスホテルを予約しました。ただ、新幹線のチケットがまだ手配できていません。」
男：「あ、そうか。来週から連休に入るから、新幹線は混雑するかもしれないね。先に指定席を確保してくれたまえ。経費の精算書は出張から戻ってからで構わないから。」
女：「承知しました。すぐにネットで指定席を予約します。」""",
            "女性社員はこの後、まず何をしますか。",
            [
                ("A", "出張の経費精算書を作成する。"),
                ("B", "大阪のホテルの予約を取り直す。"),
                ("C", "新幹線の指定席を予約する。"),
                ("D", "取引先に出張日程のメールを送る。")
            ],
            "C",
            "Người nam yêu cầu: '先に指定席を確保してくれたまえ' (Hãy ưu tiên giữ chỗ vé tàu Shinkansen trước). Nữ nhân viên xác nhận: 'すぐにネットで指定席を予約します'.",
            {
                "A": "Thanh toán chi phí đợi đi công tác về mới làm ('出張から戻ってからで構わない').",
                "B": "Khách sạn trước nhà ga đã đặt xong, không cần đặt lại.",
                "D": "Bài đối thoại không hề đề cập đến việc gửi mail cho đối tác vào lúc này."
            },
            3
        ),
        (
            "N2-M1-L04",
            "Mondai 1: 課題理解 (Task) — 研究発表の準備",
            """大学の研究室で、教授と大学院生が話しています。学生はこの後、スライドの何を修正しますか。

男（教授）：「君の発表スライド、よくまとまっているよ。ただ、第3章の実験結果のグラフだが、縦軸の単位が抜けているね。それと、先行研究の文献リストで出版年が古いものがあるから、最新の論文に差し替えた方が説得力が増すだろう。」
女（学生）：「はい！ すぐにグラフの単位を追記して、参考文献を更新します。発表原稿の修正はいかがでしょうか。」
男：「原稿の言葉遣いは問題ないから、今の2点だけ手直ししておいてくれ。」""",
            "学生が修正しなければならないものはどれか。",
            [
                ("A", "発表原稿の敬語と言葉遣い。"),
                ("B", "スライド全体のデザインと配色。"),
                ("C", "グラフの単位と参考文献のリスト。"),
                ("D", "実験のやり直しとデータの再測定。")
            ],
            "C",
            "Giáo sư chỉ đạo sửa 2 điểm: điền thêm đơn vị vào trục tung của đồ thị (縦軸の単位) và thay thế danh mục tài liệu tham khảo bằng bài báo mới nhất (最新の論文に差し替え). Lời văn diễn thuyết (原稿) không có vấn đề gì.",
            {
                "A": "Lời thoại diễn thuyết giáo sư khen ngợi không cần sửa ('言葉遣いは問題ない').",
                "B": "Giáo sư không yêu cầu đổi thiết kế hay màu sắc slide.",
                "D": "Dữ liệu thí nghiệm được đánh giá tốt, không phải làm lại thí nghiệm."
            },
            4
        ),
        (
            "N2-M1-L05",
            "Mondai 1: 課題理解 (Task) — 店舗の開店準備",
            """カフェの開店前、店長とアルバイトの店員が話しています。アルバイトの女性はこの後、まず何をしますか。

男（店長）：「今日のランチタイムは予約で満席になりそうだ。テーブルのセッティングは終わったかい？」
女：「はい、お水とグラスの用意も完了しています。」
男：「よし。じゃあ、今日の特別メニューの看板を入り口に出してきてくれるかい？ その後で、レジのお釣りの確認をしておいてほしいんだ。」
女：「分かりました。看板を書いてすぐに出してきます！」""",
            "アルバイトの女性はこの後、まず何をしますか。",
            [
                ("A", "レジのお釣りの金額を確認する。"),
                ("B", "入り口に特別メニューの看板を出す。"),
                ("C", "テーブルのセッティングとお水の用意をする。"),
                ("D", "厨房でランチの仕込みを手伝う。")
            ],
            "B",
            "Quản lý dặn: '今日の特別メニューの看板を入り口に出してきてくれるかい？ その後で、レジのお釣りの確認をしておいてほしいんだ' -> Việc đầu tiên cần làm là đưa biển bảng thực đơn đặc biệt ra cửa.",
            {
                "A": "Việc kiểm tra tiền thối ở quầy thu ngân là bước làm sau đó ('その後で').",
                "C": "Bàn và nước đã chuẩn bị xong từ trước ('用意も完了しています').",
                "D": "Quán không yêu cầu nhân viên chạy bàn phụ bếp nấu ăn."
            },
            5
        )
    ]

    for qid, title, script, stem, opts, ans, exp, dist, qnum in m1_data:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Listening",
            "typeId": "N2-LIS-TASK",
            "stem": stem,
            "stimulusId": qid,
            "contextPassage": script,
            "options": [{"id": oid, "text": otxt} for oid, otxt in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 2,
            "conceptId": "listening-task",
            "remediation": "Lắng nghe kỹ các liên từ chỉ thứ tự ưu tiên (まず, 先に, その後で, 最優先) và hành động nhân vật xác nhận sẽ làm ngay.",
            "status": "QA_VERIFIED",
            "exposureEligible": True,
            "diagnosticEligible": True,
            "sourceMetadata": "Original JLPT N2 Listening Corpus",
            "examQNum": qnum,
            "mondaiTitle": "Mondai 1: 課題理解 (Hiểu yêu cầu - Nhiệm vụ tiếp theo)"
        })

    # =========================================================================
    # MONDAI 2: ポイント理解 (Key Points Comprehension - 6 items)
    # =========================================================================
    m2_data = [
        (
            "N2-M2-L01",
            "Mondai 2: ポイント理解 (Key Points) — 転職の理由",
            """男の人と女の人が話しています。男の人が転職を決意した決定的な理由は何ですか。

女：「佐藤さん、来月で退職されるそうですね。大企業で待遇も恵まれていたのに、なぜ転職されるんですか？」
男：「ええ、給与や福利厚生には全く不満はありませんでした。同僚や上司との人間関係も非常に良好でしたしね。ただ、大きな組織であるがゆえに、自分の提案した新しい事業アイデアが意思決定に時間がかかってなかなか実現できなかったんです。自分の力で責任を持ってスピーディーに挑戦できる環境に身を置きたいと強く思うようになったんです。」
女：「なるほど、ステップアップのための前向きな挑戦なんですね。」""",
            "男の人が転職を決意した一番の理由は何ですか。",
            [
                ("A", "現在の会社の給与や福利厚生に強い不満があったから。"),
                ("B", "上司や同僚との人間関係で深刻なトラブルがあったから。"),
                ("C", "自分のアイデアを迅速に実行できる環境で挑戦したかったから。"),
                ("D", "残業が多すぎて健康を害してしまったから。")
            ],
            "C",
            "Người đàn ông khẳng định lương tốt, quan hệ tốt, nhưng vì muốn ở nơi có thể nhanh chóng hiện thực hóa ý tưởng của bản thân mà không bị bộ máy cồng kềnh cản trở.",
            {
                "A": "Người nam nói rõ: '給与や福利厚生には全く不満はありませんでした' (hoàn toàn không có bất mãn về lương bổng hay đãi ngộ).",
                "B": "Người nam khẳng định: '人間関係も非常に良好でした' (mối quan hệ với sếp và đồng nghiệp rất tốt đẹp).",
                "D": "Không hề đề cập đến chuyện làm thêm giờ quá sức hay ảnh hưởng sức khỏe."
            },
            6
        ),
        (
            "N2-M2-L02",
            "Mondai 2: ポイント理解 (Key Points) — ランニングシューズの選び方",
            """スポーツ用品店で、店員がランニング初心者に向けて靴の選び方を説明しています。初心者が靴を選ぶ際に最も重視すべき点として、店員は何を挙げていますか。

店員：「初心者の方が靴を選ぶ際、どうしても軽さやデザインに目が行きがちです。しかし、実は最も重要なのは『クッション性の高さ』です。走る筋力がまだ十分に備わっていない初心者は、着地時に体重の3倍もの衝撃が膝や足首にかかります。厚みのあるソールがその衝撃を吸収してくれるため、怪我を防ぎ長く走り続けることができるのです。」""",
            "店員によると、初心者が最も重視すべきポイントは何ですか。",
            [
                ("A", "膝や足首への衝撃を吸収するクッション性の高さ。"),
                ("B", "シューズ自体の軽さとスピードの出しやすさ。"),
                ("C", "有名選手が着用している最新の流行デザイン。"),
                ("D", "長期間履いても破れない靴底の耐久性の強さ。")
            ],
            "A",
            "Nhân viên bán hàng chỉ ra với người mới tập chạy, điểm quan trọng nhất là 'クッション性の高さ' (độ êm ái giảm xóc) để bảo vệ khớp gối và cổ chân khỏi chấn thương.",
            {
                "B": "Trọng lượng nhẹ giúp chạy nhanh nhưng người mới chưa có cơ bắp vững chắc nếu mang giày quá mỏng sẽ rất dễ chấn thương.",
                "C": "Kiểu dáng thời trang là điều người mua hay bị thu hút nhưng không phải yếu tố an toàn cốt lõi.",
                "D": "Độ bền chống mòn đế giày chỉ là yếu tố phụ, không phải điểm mấu chốt để phòng ngừa chấn thương."
            },
            7
        ),
        (
            "N2-M2-L03",
            "Mondai 2: ポイント理解 (Key Points) — 読書が長続きしない理由",
            """ラジオで専門家が、大人の読書習慣について話しています。専門家によると、多くの人が読書を挫折してしまう一番の理由は何ですか。

専門家：「本を買っても途中で挫折してしまう人の多くは、『最初から最後まで一言一句漏らさず読まなければならない』という思い込みに縛られています。難解な部分や退屈な章に出くわしたとき、そこで止まってしまい本を開かなくなるのです。目次を見て自分が一番興味のある章から拾い読みしたり、面白くないと感じたら途中で読むのをやめても構わないのです。読書をもっと自由で気楽なものと捉え直すことが大切です。」""",
            "専門家が挙げる、読書が続かない主な原因は何ですか。",
            [
                ("A", "仕事が忙しくて本を読む時間を1分も確保できないこと。"),
                ("B", "最初から最後まで飛ばさずに全部読まなければならないと思い込んでいること。"),
                ("C", "購入する本の難易度が高すぎて理解不能なこと。"),
                ("D", "電子書籍の画面の光で目が疲れてしまうこと。")
            ],
            "B",
            "Chuyên gia chỉ ra nguyên nhân số 1 khiến mọi người bỏ dở cuốn sách là định kiến 'phải đọc từng câu từng chữ từ đầu đến cuối không được bỏ sót'. Gặp đoạn khó hoặc chán là dừng lại rồi bỏ luôn.",
            {
                "A": "Chuyên gia không đổ lỗi cho việc bận rộn thiếu thời gian.",
                "C": "Độ khó của sách không phải là nguyên nhân chính, mà là cách tiếp cận cố chấp không dám đọc lướt.",
                "D": "Không hề đề cập đến thiết bị đọc sách điện tử hay mỏi mắt."
            },
            8
        ),
        (
            "N2-M2-L04",
            "Mondai 2: ポイント理解 (Key Points) — テレワークツールの選定",
            """会社のIT部門で、部長と担当社員が新しい業務ソフトウェアの導入について話しています。会社がこのツールを採用することにした決定的な理由は何ですか。

男（部長）：「A社とB社のソフトウェア、比較検討の結果はどうなった？」
女：「はい。機能の豊富さやデザインの洗練度ではA社が優れていました。しかし、弊社の最重要課題であるセキュリティ面を精査したところ、B社は部署ごとの閲覧権限やファイル暗号化が極めて厳格に設計されており、情報漏洩リスクを最小限に抑えられることが分かりました。」
男：「なるほど。顧客の機密データを扱う我々としては、機能の多さよりも安全性が最優先だな。じゃあB社で進めよう。」""",
            "会社が新しいソフトウェアを選定した一番の決め手は何ですか。",
            [
                ("A", "画面のデザインが美しく、操作が直感的であること。"),
                ("B", "他社製品に比べて利用料金が格段に安いこと。"),
                ("C", "顧客データの漏洩を防ぐ高度なセキュリティ機能があること。"),
                ("D", "あらゆる業務に対応できる機能の数が最も多いこと。")
            ],
            "C",
            "Trưởng phòng và nhân viên thống nhất: Vì công ty xử lý dữ liệu bảo mật của khách hàng nên tính năng bảo mật phân quyền nghiêm ngặt của phần mềm B là yếu tố quyết định số 1 ('安全性が最優先').",
            {
                "A": "Thiết kế đẹp mắt là ưu điểm của phần mềm A nhưng bị loại.",
                "B": "Bài nghe không bàn về việc giá thành rẻ nhất.",
                "D": "Nhiều chức năng nhất cũng là đặc điểm của phần mềm A, bị từ chối vì bảo mật kém hơn."
            },
            9
        ),
        (
            "N2-M2-L05",
            "Mondai 2: ポイント理解 (Key Points) — 和菓子店のパッケージ刷新",
            """老舗和菓子店の店主が、商品の箱のデザインを変更した理由について話しています。店主がパッケージを一新した一番の目的は何ですか。

店主：「創業80年を迎えるにあたり、定番の羊羹の包装をリニューアルしました。伝統の小豆の製法や味は昔のまま一切変えていません。ただ、従来の木箱の包装は高級感はあるものの、どうしても堅苦しく、若い方々が日常の手土産として手に取りにくいという声がありました。そこで、環境に配慮した明るい和紙の小箱に変更したところ、若い世代やビジネス街の女性客にも気軽に買っていただけるようになりました。」""",
            "店主が商品のパッケージを一新した目的は何ですか。",
            [
                ("A", "原材料費が高騰したため、製造コストを抑えるため。"),
                ("B", "若い世代や日常のギフト需要に親しみを持ってもらうため。"),
                ("C", "海外への輸出を増やすために英語表記を導入するため。"),
                ("D", "伝統的な製法をやめて、現代風の新しい味に変更したことを伝えるため。")
            ],
            "B",
            "Chủ tiệm giải thích: Hương vị truyền thống giữ nguyên 100%, việc thay đổi hộp bao bì giấy nhẹ nhàng tươi sáng là để giới trẻ và dân văn phòng dễ dàng mua làm quà tặng hàng ngày mà không bị cảm giác nặng nề.",
            {
                "A": "Không hề đề cập đến việc cắt giảm chi phí do nguyên liệu đắt đỏ.",
                "C": "Không bàn về xuất khẩu nước ngoài hay tiếng Anh.",
                "D": "Chủ tiệm khẳng định hương vị bí truyền từ đậu đỏ không hề thay đổi ('製法や味は昔のまま一切変えていません')."
            },
            10
        ),
        (
            "N2-M2-L06",
            "Mondai 2: ポイント理解 (Key Points) — 健康診断後の医師のアドバイス",
            """病院で、医師が健康診断を終えた男性にアドバイスをしています。医師が男性に最も推奨している生活改善策は何ですか。

医師：「検査結果ですが、血糖値と中性脂肪がやや高めですね。ただ、今すぐ薬を飲む段階ではありません。」
男：「そうですか。炭水化物を完全に抜いた方がいいでしょうか。」
医師：「極端な食事制限は長続きしませんし、リバウンドの危険があります。それよりも、一口ごとに30回よく噛んで時間をかけて食べること、そして食後すぐに座り込まず、15分程度の軽いウォーキングをすることを習慣にしてください。食後の血糖値の急上昇を抑えるには、これが最も効果的なんですよ。」""",
            "医師が推奨している最も効果的な改善策は何ですか。",
            [
                ("A", "炭水化物を一切食べずに厳しい食事制限をすること。"),
                ("B", "一口ごとによく噛んで食べ、食後に軽い散歩をすること。"),
                ("C", "毎朝激しい筋力トレーニングを1時間以上行うこと。"),
                ("D", "数値が下がるまで毎日血糖降下薬を服用し続けること。")
            ],
            "B",
            "Bác sĩ khuyên không nên nhịn ăn tiêu cực; phương pháp hữu hiệu nhất là nhai kỹ từng miếng và đi bộ nhẹ nhàng 15 phút ngay sau bữa ăn để chặn đường huyết tăng vọt.",
            {
                "A": "Bác sĩ phản đối việc kiêng khem cực đoan vì dễ phản tác dụng ('極端な食事制限はリバウンドの危険').",
                "C": "Không khuyên tập thể hình nặng quá sức.",
                "D": "Bác sĩ nói rõ chưa cần thiết phải uống thuốc ('今すぐ薬を飲む段階ではありません')."
            },
            11
        )
    ]

    for qid, title, script, stem, opts, ans, exp, dist, qnum in m2_data:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Listening",
            "typeId": "N2-LIS-POIN",
            "stem": stem,
            "stimulusId": qid,
            "contextPassage": script,
            "options": [{"id": oid, "text": otxt} for oid, otxt in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 3,
            "conceptId": "listening-points",
            "remediation": "Lắng nghe lý do cốt lõi sau các từ nối chuyển ý (ただ, それよりも, 決定的な理由, 実は最も重要なのは).",
            "status": "QA_VERIFIED",
            "exposureEligible": True,
            "diagnosticEligible": True,
            "sourceMetadata": "Original JLPT N2 Listening Corpus",
            "examQNum": qnum,
            "mondaiTitle": "Mondai 2: ポイント理解 (Hiểu điểm mấu chốt - Trích xuất lý do)"
        })

    # =========================================================================
    # MONDAI 3: 概要理解 (General Comprehension - Monologue - 5 items)
    # =========================================================================
    m3_data = [
        (
            "N2-M3-L01",
            "Mondai 3: 概要理解 (General) — 屋上緑化の環境効果",
            """大学の講義で、環境学の教授が話しています。

教授：「都市部におけるヒートアイランド現象の緩和策として、建物の屋上緑化が注目を集めています。屋上に植物を植えることで、直射日光によるコンクリートの温度上昇を防ぎ、最上階の冷房負荷を20％以上削減できるという実験データがあります。さらに、集中豪雨の際には雨水を一時的に土壌に保水することで、下水道への急激な排水を遅らせ、都市型水害を防ぐ役割も果たします。単なる見た目の美しさだけでなく、エネルギー削減と防災の両面において、屋上緑化は都市の持続可能性を支える重要なインフラなのです。」""",
            "教授は何について話していますか。",
            [
                ("A", "都市の屋上緑化がもたらすエネルギー削減と防災の複合的効果。"),
                ("B", "高層ビルの屋上で家庭菜園を行うための最新の栽培技術。"),
                ("C", "集中豪雨による都市の水害を完全に防ぐ最新の堤防建築。"),
                ("D", "都市のコンクリート建築における耐震補強の重要性。")
            ],
            "A",
            "Giáo sư trình bày tổng quan các lợi ích tổng hợp của việc phủ xanh mái nhà đô thị: hạ nhiệt giảm điện điều hòa và trữ nước mưa chống ngập lụt đô thị.",
            {
                "B": "Bài giảng không bàn về kỹ thuật trồng rau làm vườn gia đình.",
                "C": "Không nói về xây đê kè bê tông kiên cố.",
                "D": "Không đề cập đến gia cố chống động đất cho nhà cao tầng."
            },
            12
        ),
        (
            "N2-M3-L02",
            "Mondai 3: 概要理解 (General) — 睡眠の質と就寝前のルーティン",
            """ラジオの健康番組で、専門家が現代人の睡眠について語っています。

専門家：「スマートウォッチなどで自分の睡眠ステージを毎晩細かく計測し、点数に一喜一憂する人が増えています。しかし、数値を気にしすぎるあまり、かえって緊張して眠れなくなる『睡眠恐怖症』に陥るケースも少なくありません。良質な睡眠を得るために本当に必要なのは、機器による監視ではなく、就寝前の『心の移行期間』です。寝る1時間前にはスマホやパソコンを消し、ぬるめのお風呂に入ったり、静かな音楽を聴いたりして副交感神経を優位にすること。このリラックスしたルーティンこそが、自然な熟睡へと導く最良の鍵なのです。」""",
            "専門家が最も主張したいことは何ですか。",
            [
                ("A", "最新のスマートウォッチを使って睡眠データを毎晩詳細に分析すること。"),
                ("B", "睡眠不足を解消するために、休日にまとめて15時間以上眠ること。"),
                ("C", "就寝前にデジタル機器から離れ、心をリラックスさせる移行時間を持つこと。"),
                ("D", "睡眠障害を治療するためには、すぐに強い睡眠薬を服用すること。")
            ],
            "C",
            "Chuyên gia nhấn mạnh: Thay vì ám ảnh đo đạc số liệu bằng đồng hồ thông minh, điều cốt lõi là tạo ra khoảng đệm thư giãn trước khi ngủ (tắt màn hình, nghe nhạc êm để hệ thần kinh thả lỏng).",
            {
                "A": "Đây là hành vi chuyên gia cảnh báo dễ gây lo âu căng thẳng ngược lại.",
                "B": "Không khuyên ngủ bù li bì vào ngày cuối tuần.",
                "D": "Không khuyên lạm dụng thuốc ngủ."
            },
            13
        ),
        (
            "N2-M3-L03",
            "Mondai 3: 概要理解 (General) — 陶芸における「わびさび」の美意識",
            """美術館のギャラリートークで、学芸員が日本の伝統陶芸について解説しています。

学芸員：「西洋の古典的な陶磁器では、左右対称の均整の取れた形や、傷一つない滑らかな表面が理想とされてきました。しかし、日本の茶の湯とともに発展した陶芸では、まったく異なる美意識が重んじられます。それは『わびさび』の精神です。轆轤（ろくろ）の歪み、炎の当たり具合によって偶然生じた釉薬のムラ、長年使い込むことで生まれた細かなひび割れ。不完全さや経年変化の中にこそ、二度と再現できない自然の妙と深い情緒が宿ると考えるのです。欠点を受け入れ、そこに独自の美を見出す姿勢が、日本のものづくりの根底に流れています。」""",
            "学芸員は日本の陶芸についてどのような点を取り上げていますか。",
            [
                ("A", "西洋の陶磁器を模倣して完成させた精密な幾何学的対称性の美。"),
                ("B", "金や宝石を散りばめた豪華絢爛な装飾の歴史的変遷。"),
                ("C", "不完全さや使い込む中での経年変化に美を見出す「わびさび」の美意識。"),
                ("D", "最新の工業用機械を用いて陶器を大量生産する現代の手法。")
            ],
            "C",
            "Chuyên viên nghệ thuật phân tích triết lý Wabi-sabi trong gốm sứ Nhật Bản: Không tìm kiếm sự đối xứng không tì vết, mà trân trọng sự bất đối xứng tự nhiên, vết nứt men và dấu vết thời gian sử dụng.",
            {
                "A": "Đối xứng hình học hoàn hảo là tiêu chuẩn phương Tây cổ điển, đối lập với triết lý wabi-sabi.",
                "B": "Không nói về trang trí vàng bạc lộng lẫy.",
                "D": "Không bàn về sản xuất đồ gốm công nghiệp hàng loạt."
            },
            14
        ),
        (
            "N2-M3-L04",
            "Mondai 3: 概要理解 (General) — 多国籍チームにおけるフィードバック",
            """ビジネスセミナーで、人材育成コンサルタントが指導法について講演しています。

コンサルタント：「多様な文化的背景を持つメンバーで構成されるチームでは、部下へのフィードバックの仕方に細心の注意が必要です。過去のミスを事細かに指摘して反省を促す昔ながらのやり方は、相手に強い防衛本能を生じさせ、モチベーションを著しく低下させます。いまグローバル企業で推奨されているのは『フィードフォワード』と呼ばれる手法です。過去の失敗を責めるのではなく、本人が発揮した具体的な貢献をまず認めた上で、『次のプロジェクトを成功させるために、具体的にどう行動を改善できるか』という未来の選択肢を対話の中で引き出していく。この未来志向のアプローチこそが、自主的な成長を促すのです。」""",
            "コンサルタントは何を提唱していますか。",
            [
                ("A", "部下の自尊心を傷つけないために、ミスがあっても一切指導しないこと。"),
                ("B", "過去のミスを公の場で厳しく叱責して、チーム内の緊張感を高めること。"),
                ("C", "過去の失敗を責めず、具体的な貢献の承認と未来志向の改善策を対話すること。"),
                ("D", "すべての評価を数値化し、上司の主観を完全に排除した機械的査定を行うこと。")
            ],
            "C",
            "Diễn giả đề xuất phương pháp 'Feedforward': công nhận nỗ lực cụ thể đã làm tốt và cùng trao đổi phương án hành động cải tiến cho dự án tương lai thay vì chăm chăm bới móc lỗi lầm quá khứ.",
            {
                "A": "Bỏ mặc lỗi lầm không hướng dẫn là sai lầm trong quản lý.",
                "B": "Quát mắng trước mặt tập thể phá nát tinh thần hợp tác và sự gắn kết.",
                "D": "Không đề xuất đánh giá máy móc vô cảm."
            },
            15
        ),
        (
            "N2-M3-L05",
            "Mondai 3: 概要理解 (General) — プラスチックごみ問題と発生源抑制",
            """環境問題のシンポジウムで、専門家がプラスチック対策について報告しています。

専門家：「プラスチックごみによる海洋汚染が深刻化する中、世界中でリサイクルの推進が叫ばれています。しかし、回収したプラスチックを再資源化するプロセス自体にも膨大なエネルギーとコストが必要であり、リサイクルだけで増え続けるごみを処理し切ることは不可能です。真に持続可能な循環型社会を実現するためには、リサイクルよりも上位の概念である『リデュース』、すなわち使い捨て容器や過剰包装などの発生そのものを元から断つことが不可欠です。企業にはリユース可能な設計への転換が、そして消費者にはライフスタイルの見直しが強く求められています。」""",
            "専門家が最も強調している対策はどれか。",
            [
                ("A", "リサイクルだけに頼るのではなく、使い捨て包装の発生そのものを元から削減すること。"),
                ("B", "プラスチックの生産量をさらに増やして、より安価な使い捨て容器を流通させること。"),
                ("C", "海洋に流出したプラスチックごみをすべて民間のボランティアで回収すること。"),
                ("D", "プラスチック製品の使用を法律で即座に全面禁止し、木材のみで代替すること。")
            ],
            "A",
            "Chuyên gia nhấn mạnh tái chế không thể theo kịp lượng rác phát thải; biện pháp cốt lõi phải là cắt giảm ngay tại nguồn (Reduce) và chuyển đổi sang thiết kế bao bì tái sử dụng.",
            {
                "B": "Tăng sản xuất đồ nhựa dùng 1 lần đi ngược lại bảo vệ môi trường.",
                "C": "Thu gom tình nguyện không thể giải quyết được tận gốc khối lượng rác khổng lồ.",
                "D": "Lệnh cấm toàn bộ đồ nhựa ngay lập tức là cực đoan và phi thực tế."
            },
            16
        )
    ]

    for qid, title, script, stem, opts, ans, exp, dist, qnum in m3_data:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Listening",
            "typeId": "N2-LIS-OUTL",
            "stem": stem,
            "stimulusId": qid,
            "contextPassage": script,
            "options": [{"id": oid, "text": otxt} for oid, otxt in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 3,
            "conceptId": "listening-outline",
            "remediation": "Nắm bắt luận điểm tổng quát (主張, 結論) của toàn bộ bài nói, không bị phân tâm bởi các chi tiết ví dụ minh họa.",
            "status": "QA_VERIFIED",
            "exposureEligible": True,
            "diagnosticEligible": True,
            "sourceMetadata": "Original JLPT N2 Listening Corpus",
            "examQNum": qnum,
            "mondaiTitle": "Mondai 3: 概要理解 (Hiểu khái quát - Luận điểm bài nói)"
        })

    # =========================================================================
    # MONDAI 4: 即時応答 (Quick Response - 11 items, 3 options each)
    # =========================================================================
    m4_data = [
        (
            "N2-M4-L01",
            "山田さん、明日のプレゼン資料、目を通していただけないでしょうか。",
            [
                ("A", "ええ、喜んで拝見します。"),
                ("B", "はい、目を通してください。"),
                ("C", "いえ、何も見えませんでした。")
            ],
            "A",
            "Đối phương nhờ: '目を通していただけないでしょうか' (Có thể xem qua giúp tôi được không?). Cách đáp lễ phép khiêm nhường là: 'ええ、喜んで拝見します' (Vâng, tôi rất sẵn lòng xem qua ạ).",
            {
                "B": "Bảo đối phương xem đi ('目を通してください') là đảo lộn vai vế.",
                "C": "Hiểu sai nghĩa cụm từ 目を通す thành nhìn bằng mắt vật lý ('tôi chả thấy gì')."
            },
            17
        ),
        (
            "N2-M4-L02",
            "この間のプロジェクト、君のおかげで大成功だったよ。",
            [
                ("A", "はい、私が一人で頑張りましたから。"),
                ("B", "とんでもないです。チームの皆さんのおかげです。"),
                ("C", "どうぞお構いなく。")
            ],
            "B",
            "Khi được cấp trên hoặc đối tác khen ngợi thành tích, cách ứng đáp khiêm tốn chuẩn mực trong văn hóa công sở Nhật là: 'とんでもないです。チームの皆さんのおかげです' (Dạ đâu có ạ, đều nhờ công sức của toàn thể mọi người trong đội cả ạ).",
            {
                "A": "Tự mãn vỗ ngực 'do một mình tôi cố gắng' là điều tối kỵ trong văn hóa Nhật.",
                "C": "'どうぞお構いなく' (Xin đừng bận tâm tiếp đãi) dùng khi đến thăm nhà, sai ngữ cảnh."
            },
            18
        ),
        (
            "N2-M4-L03",
            "部長、ご相談したい件があるのですが、今お時間よろしいでしょうか。",
            [
                ("A", "ええ、今なら大丈夫だよ。何かな。"),
                ("B", "はい、お時間を差し上げます。"),
                ("C", "いえ、もう相談は終わりましたよ。")
            ],
            "A",
            "Cấp dưới hỏi xin ý kiến: 'bây giờ sếp có thời gian không ạ?'. Sếp đáp tự nhiên: 'ええ、今なら大丈夫だよ。何かな' (Ừ, lúc này thì được. Chuyện gì thế?).",
            {
                "B": "差し上げる là khiêm nhường ngữ (cho/tặng), cấp trên không nói với cấp dưới như vậy.",
                "C": "Người ta chưa bắt đầu nói mà lại bảo 'cuộc tư vấn đã kết thúc rồi' là vô lý."
            },
            19
        ),
        (
            "N2-M4-L04",
            "あいにく本日のチケットは完売となっておりまして…",
            [
                ("A", "では、全部買わせていただきます。"),
                ("B", "そうですか、残念ですがまた出直します。"),
                ("C", "チケットをお売りいただき感謝します。")
            ],
            "B",
            "Nhân viên thông báo: 'Vé hôm nay rất tiếc đã bán hết sạch rồi ạ...'. Khách đáp phù hợp: 'そうですか、残念ですがまた出直します' (Vậy à, tiếc thật, tôi sẽ quay lại dịp khác).",
            {
                "A": "Đã hết sạch vé mà bảo 'vậy tôi mua hết' là vô nghĩa.",
                "C": "Chưa mua được vé mà lại cảm ơn vì đã bán vé."
            },
            20
        ),
        (
            "N2-M4-L05",
            "この仕事、明日までに終わらせろなんて、無理に決まってるよ。",
            [
                ("A", "そう言わずに、手分けしてやってみようよ。"),
                ("B", "うん、絶対に明日までに終わったね。"),
                ("C", "じゃあ、今日中に全部やってしまおう。")
            ],
            "A",
            "Đồng nghiệp than vãn: 'Bảo xong việc này trước ngày mai thì vô lý quá'. Câu động viên chia việc hợp lý: 'そう言わずに、手分けしてやってみようよ' (Đừng nói thế, chúng mình chia nhau ra cùng làm xem sao).",
            {
                "B": "Dùng thì quá khứ 終わったね trong khi việc chưa hoàn thành là sai.",
                "C": "Mai còn không kịp mà bảo 'làm hết ngay trong hôm nay' là thiếu thực tế."
            },
            21
        ),
        (
            "N2-M4-L06",
            "課長、先ほど田中様がお見えになりました。",
            [
                ("A", "ええ、田中様を見に行きました。"),
                ("B", "そうか、第2応接室にご案内してくれたまえ。"),
                ("C", "はい、田中様はお帰りになりましたか。")
            ],
            "B",
            "Thư ký báo: 'Thưa trưởng phòng, vừa nãy anh Tanaka đã đến ạ' (お見えになる là tôn kính ngữ của 来る). Trưởng phòng chỉ thị: 'そうか、第2応接室にご案内してくれたまえ' (Thế à, hướng dẫn anh ấy vào phòng tiếp khách số 2 giúp tôi).",
            {
                "A": "Hiểu sai お見えになる thành 'nhìn thấy' (見に行く).",
                "C": "Khách vừa mới đến lại hỏi 'đã về rồi à' là phi logic."
            },
            22
        ),
        (
            "N2-M4-L07",
            "昨日のパーティー、行けなくて本当に悪かったね。",
            [
                ("A", "ううん、気にしないで。また今度集まろう。"),
                ("B", "ええ、絶対に来るべきだったのに。"),
                ("C", "はい、私も行けなくて残念でした。")
            ],
            "A",
            "Bạn xin lỗi vì bận không đến được bữa tiệc. Đáp lại thông cảm: 'ううん、気にしないで。また今度集まろう' (Không sao đâu, đừng bận tâm, lần khác tụi mình lại tụ tập nhé).",
            {
                "B": "Trách móc 'lẽ ra cậu nhất định phải đến chứ' là thiếu lịch sự thân thiện.",
                "C": "Người kia không đến được, còn mình là người chủ trì/đã đi tiệc mà lại nói 'tôi cũng không đi được'."
            },
            23
        ),
        (
            "N2-M4-L08",
            "この新製品、使ってみたけど、期待外れもいいところだったよ。",
            [
                ("A", "え、そんなにいまいちだったの？"),
                ("B", "期待通りで本当によかったね。"),
                ("C", "外に出て使ってみればいいよ。")
            ],
            "A",
            "Thành ngữ: 期待外れもいいところだ (thất vọng tràn trề, quá sức kỳ vọng). Phản xạ đáp lại: 'え、そんなにいまいちだったの？' (Hả, tệ/kém đến mức thế cơ à?).",
            {
                "B": "Ngược nghĩa hoàn toàn với thất vọng (期待通り là đúng như mong đợi).",
                "C": "Hiểu nhầm 外れ (hụt, trật) thành 外 (bên ngoài)."
            },
            24
        ),
        (
            "N2-M4-L09",
            "恐れ入りますが、こちらの書類にお名前をご記入いただけますか。",
            [
                ("A", "はい、分かりました。どこに書けばいいですか。"),
                ("B", "どういたしまして、ご記入ください。"),
                ("C", "いえ、お名前は存じ上げております。")
            ],
            "A",
            "Nhân viên lịch sự: 'Xin thứ lỗi, anh/chị có thể vui lòng điền họ tên vào giấy tờ này giúp em được không ạ?'. Khách đồng ý: 'はい、分かりました。どこに書けばいいですか' (Vâng, tôi hiểu rồi. Viết vào chỗ nào thế em?).",
            {
                "B": "Khách lại bảo nhân viên 'xin mời điền vào' là sai.",
                "C": "Hiểu nhầm câu hỏi, đáp 'tôi biết tên rồi'."
            },
            25
        ),
        (
            "N2-M4-L10",
            "駅前の新しいカフェ、もう行ってみた？ コーヒーがすごく美味しかったよ。",
            [
                ("A", "へえ、知らなかった。今度行ってみるね。"),
                ("B", "うん、そのカフェでコーヒーを作ったよ。"),
                ("C", "そうなんだ、コーヒーは飲まなかったんだね。")
            ],
            "A",
            "Bạn gợi ý quán cà phê ngon trước ga: 'Cậu đã ghé thử quán cà phê mới trước ga chưa? Cà phê ở đó ngon lắm đấy!'. Đáp lại tự nhiên: 'へえ、知らなかった。今度行ってみるね' (Thế à, tớ không biết đấy. Bữa nào tớ sẽ ghé thử).",
            {
                "B": "Tự nhiên nhận 'tớ đã pha cà phê ở quán đó' là lạc quẻ.",
                "C": "Người ta vừa khen cà phê ngon mà lại nói 'cậu không uống cà phê à'."
            },
            26
        ),
        (
            "N2-M4-L11",
            "雨が降りそうだから、傘を持って行ったほうがいいんじゃない？",
            [
                ("A", "そうだね、折りたたみ傘を鞄に入れておくよ。"),
                ("B", "うん、傘を持って行かなくてよかった。"),
                ("C", "いえ、雨が降ったら傘を買わないよ。")
            ],
            "A",
            "Lời khuyên: 'Trời trông sắp mưa đấy, chẳng phải nên mang ô đi hay sao?'. Đáp lại hợp lý: 'そうだね、折りたたみ傘を鞄に入れておくよ' (Ừ đúng rồi, tớ sẽ bỏ cây dù gấp vào cặp).",
            {
                "B": "Chưa đi mà đã nói thì quá khứ 'may mà không mang ô đi' là vô lý.",
                "C": "Nói 'nếu trời mưa tôi sẽ không mua ô' là kỳ quặc."
            },
            27
        )
    ]

    for qid, prompt_text, opts, ans, exp, dist, qnum in m4_data:
        # Official JLPT Mondai 4 has exactly 3 spoken choices (1, 2, 3), not 4!
        # During exam, test paper has NO printed text; options are merely 1, 2, 3.
        # Spoken text is preserved in spokenOptions and contextPassage for post-submission review.
        exam_opts = [
            {"id": "A", "text": "１番"},
            {"id": "B", "text": "２番"},
            {"id": "C", "text": "３番"}
        ]
        spoken_opts = [
            {"id": oid, "num": idx + 1, "text": otxt}
            for idx, (oid, otxt) in enumerate(opts[:3])
        ]

        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Listening",
            "typeId": "N2-LIS-RESP",
            "stem": "発話と返事を聞いて、１から３の中から、最もよいものを一つ選んでください。",
            "stimulusId": qid,
            "contextPassage": f"【音声発話】\n「{prompt_text}」\n\n【返事の選択肢】\n1. {opts[0][1]}\n2. {opts[1][1]}\n3. {opts[2][1]}",
            "options": exam_opts,
            "spokenOptions": spoken_opts,
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": {k: v for k, v in dist.items() if k in ['A', 'B', 'C']},
            "difficultyEstimate": 2,
            "conceptId": "listening-response",
            "remediation": "Ôn tập kính ngữ (tôn kính ngữ, khiêm nhường ngữ), thành ngữ giao tiếp thường nhật và quán dụng ngữ phản hồi công sở.",
            "status": "QA_VERIFIED",
            "exposureEligible": True,
            "diagnosticEligible": True,
            "sourceMetadata": "Original JLPT N2 Listening Corpus",
            "examQNum": qnum,
            "mondaiTitle": "Mondai 4: 即時応答 (Phản xạ tức thì - 3 lựa chọn nghe)"
        })

    # =========================================================================
    # MONDAI 5: 統合理解 (Integrated Comprehension - 3 items)
    # =========================================================================
    # Dialogue 1: Year-end party venue (忘年会の会場選び) -> 2 items (Q28, Q29)
    # Dialogue 2: Home air purifier (空気清浄機の選定) -> 1 item (Q30)
    
    script_m5_case1 = """会社の総務部で、男性社員と女性社員が今年の忘年会の会場について相談しています。

男：「課長から忘年会の幹事を頼まれたんだけど、候補のお店を4つピックアップしてみたんだ。相談に乗ってくれる？」
女：「ええ、いいわよ。課長からの条件は何だったかしら。」
男：「参加者は25名で、予算は飲み放題込みで一人6,000円以内。それから、役員も参加するから落ち着いて話せる『完全個室』が必須条件だと言われたよ。あとは駅から近い方がいいな。」
女：「なるほど。候補のお店はどんな感じ？」
男：「まず【1番の和食懐石・松月】。料理は本格的で完全個室だけど、飲み放題付きで一人8,000円と予算オーバーなんだ。駅からも徒歩15分かかる。」
女：「それは予算的に厳しいわね。2番は？」
男：「【2番のイタリアン・バル】。駅から徒歩3分でアクセス抜群。貸切の個室があって、飲み放題付きで一人5,000円と予算内に収まるよ。」
女：「いいじゃない！ 3番と4番は？」
男：「【3番のホテルビュッフェ】は夜景が綺麗で一人7,000円だけど、個室がなくてオープンスペースなんだ。【4番の焼肉店】は一人4,500円で一番安いんだけど、店内全席喫煙可能で、個室ではなく仕切りがあるだけなんだよね。」
女：「うーん、役員はおタバコを吸わないし、煙やにおいがつくのは避けたいわね。やっぱり、予算内で完全個室があって駅から近いあのお店にするのが一番良さそうね。」
男：「そうだね、じゃあそっちで課長に提案してみるよ。」"""

    # Q28
    items.append({
        "id": "N2-M5-L01",
        "level": "N2",
        "skill": "Listening",
        "typeId": "N2-LIS-INTE",
        "stem": "条件を満たし、2人が最終的に課長へ提案することにしたお店はどれですか。",
        "stimulusId": "N2-M5-CASE1",
        "contextPassage": script_m5_case1,
        "options": [
            {"id": "A", "text": "1番の和食懐石・松月"},
            {"id": "B", "text": "2番のイタリアン・バル"},
            {"id": "C", "text": "3番のホテルビュッフェ"},
            {"id": "D", "text": "4番の焼肉店"}
        ],
        "correctAnswer": "B",
        "explanationVi": "Quán số 2 (イタリアン・バル) đáp ứng trọn vẹn tất cả tiêu chí: cách ga 3 phút, có phòng riêng biệt lập (完全個室), giá 5,000 yên kèm đồ uống (dưới mức ngân sách trần 6,000 yên).",
        "distractorExplanations": {
            "A": "Quán 1 giá 8,000 yên bị vượt ngân sách trần (6,000 yên) và cách xa ga 15 phút.",
            "C": "Quán 3 giá 7,000 yên vượt ngân sách và không có phòng riêng (個室がない).",
            "D": "Quán 4 cho phép hút thuốc toàn quán và không có phòng riêng biệt lập."
        },
        "difficultyEstimate": 3,
        "conceptId": "listening-integrated",
        "remediation": "Đối chiếu bảng tiêu chí: ngân sách (<= 6,000 yên), phòng riêng (完全個室), khoảng cách ga, và không gian không thuốc lá.",
        "status": "QA_VERIFIED",
        "exposureEligible": True,
        "diagnosticEligible": True,
        "sourceMetadata": "Original JLPT N2 Listening Corpus",
        "examQNum": 28,
        "mondaiTitle": "Mondai 5: 統合理解 (Hiểu tổng hợp — Hội thoại dài nhiều điều kiện)"
    })

    # Q29
    items.append({
        "id": "N2-M5-L02",
        "level": "N2",
        "skill": "Listening",
        "typeId": "N2-LIS-INTE",
        "stem": "女性社員が4番の焼肉店を避けた主な理由は何ですか。",
        "stimulusId": "N2-M5-CASE1",
        "contextPassage": script_m5_case1,
        "options": [
            {"id": "A", "text": "一人あたりの料金が4,500円で予算よりも安すぎるため。"},
            {"id": "B", "text": "駅から徒歩30分以上離れていて移動が不可能なため。"},
            {"id": "C", "text": "店内で喫煙が可能で、煙やにおいが服につき個室もないため。"},
            {"id": "D", "text": "お酒の飲み放題メニューが一切用意されていないため。"}
        ],
        "correctAnswer": "C",
        "explanationVi": "Nữ nhân viên giải thích: '役員はおタバコを吸わないし、煙やにおいがつくのは避けたいわね' (Các giám đốc không hút thuốc và không muốn bị bám mùi khói, quán lại không có phòng riêng).",
        "distractorExplanations": {
            "A": "Giá rẻ hơn ngân sách là điểm cộng, không phải lý do từ chối.",
            "B": "Quán không hề nói cách ga 30 phút.",
            "D": "Quán có gói đồ uống, lý do bị loại là khói thuốc và thiếu phòng riêng."
        },
        "difficultyEstimate": 3,
        "conceptId": "listening-integrated",
        "remediation": "Lắng nghe lý do từ chối của người nữ đối với các phương án bị loại.",
        "status": "QA_VERIFIED",
        "exposureEligible": True,
        "diagnosticEligible": True,
        "sourceMetadata": "Original JLPT N2 Listening Corpus",
        "examQNum": 29,
        "mondaiTitle": "Mondai 5: 統合理解 (Hiểu tổng hợp — Hội thoại dài nhiều điều kiện)"
    })

    # Dialogue 2: Air Purifier Selection (家電量販店) -> 1 item (Q30)
    script_m5_case2 = """家電量販店で、夫婦が店員の説明を聞きながら空気清浄機を選んでいます。

店員：「いらっしゃいませ。空気清浄機をお探しですか。」
男：「ええ。実はもうすぐ赤ちゃんが生まれるので、寝室に置く静かで高性能なものを探しているんです。」
女：「それと、室内で猫を1匹飼っているので、ペットの毛やにおいをしっかり除去できるフィルターがいいですね。」
店員：「かしこまりました。現在おすすめのモデルが4機種ございます。
まず【タイプA】は、基本性能を抑えたコンパクト型で、価格は2万円とお手頃ですが、消臭フィルターがついていません。
次に【タイプB】は、強力なペット用脱臭機能を備えていますが、ファンの運転音がやや大きく、赤ちゃんの就寝時には気になるかもしれません。
そして【タイプC】ですが、こちらは高性能HEPAフィルター搭載で花粉やペットの毛を99.9%捕集し、さらに特許技術の静音モードで夜間もささやき声以下の静かさで運転できます。加湿機能もついています。価格は4万5千円です。
最後の【タイプD】は、最高峰モデルでAIが空気の汚れを自動検知しますが、サイズが非常に大きく、リビング向けで価格も8万円します。」
男：「寝室に置くならサイズも大きすぎず、夜静かに動いてくれるのが一番だね。」
女：「ええ。猫の毛もにおいもしっかり取れて、赤ちゃんの眠りを妨げないのが理想ね。加湿もできるなら乾燥する冬も安心だし、これに決めましょう！」"""

    items.append({
        "id": "N2-M5-L03",
        "level": "N2",
        "skill": "Listening",
        "typeId": "N2-LIS-INTE",
        "stem": "夫婦が購入することに決めた空気清浄機はどれですか。",
        "stimulusId": "N2-M5-CASE2",
        "contextPassage": script_m5_case2,
        "options": [
            {"id": "A", "text": "タイプA（価格2万円のコンパクト型）"},
            {"id": "B", "text": "タイプB（ペット脱臭重視だが運転音がやや大きい型）"},
            {"id": "C", "text": "タイプC（ペット毛・消臭対応で超静音モードと加湿機能つき）"},
            {"id": "D", "text": "タイプD（AI自動検知機能つきの大型リビング型）"}
        ],
        "correctAnswer": "C",
        "explanationVi": "Hai vợ chồng quyết định chọn Type C: bộ lọc HEPA khử mùi lông mèo 99.9%, chế độ siêu êm ái cho phòng ngủ em bé, và kèm tính năng bù ẩm mùa đông khô ráo.",
        "distractorExplanations": {
            "A": "Type A không có bộ lọc khử mùi (消臭フィルターがついていない).",
            "B": "Type B tiếng quạt kêu khá to (運転音がやや大きい), dễ làm em bé thức giấc.",
            "D": "Type D quá to dành cho phòng khách và giá 8 vạn yên vượt nhu cầu phòng ngủ."
        },
        "difficultyEstimate": 3,
        "conceptId": "listening-integrated",
        "remediation": "Đối chiếu 3 tiêu chí: khử mùi lông thú cưng, êm ái cho trẻ sơ sinh, kích thước vừa vặn cho phòng ngủ.",
        "status": "QA_VERIFIED",
        "exposureEligible": True,
        "diagnosticEligible": True,
        "sourceMetadata": "Original JLPT N2 Listening Corpus",
        "examQNum": 30,
        "mondaiTitle": "Mondai 5: 統合理解 (Hiểu tổng hợp — So sánh lựa chọn thiết bị)"
    })

    return items
