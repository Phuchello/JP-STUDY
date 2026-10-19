# -*- coding: utf-8 -*-
"""
JLPT N2 Mock Exam #02 - Section 2: Listening Comprehension (聴解)
Full 30-item exam structure:
- Mondai 1: 課題理解 (5 items) [Q1 - Q5]
- Mondai 2: ポイント理解 (6 items) [Q6 - Q11]
- Mondai 3: 概要理解 (5 items) [Q12 - Q16]
- Mondai 4: 即時応答 (11 items) [Q17 - Q27]
- Mondai 5: 統合理解 (3 items) [Q28 - Q30]
Total: 30 items
"""

def get_n2_mock_02_listening_items():
    items = []

    # =========================================================================
    # MONDAI 1: 課題理解 (Task-based Comprehension - 5 items)
    # =========================================================================
    m1_data = [
        (
            "N2_02_M1_L01",
            "Mondai 1: 課題理解 (Task) — 社内パソコンの更新手続き",
            """会社のオフィスで、男性社員と女性社員がパソコンの交換作業について話しています。男性社員はこの後、まず何をしなければなりませんか。

男：「山田さん、来週実施される業務パソコンの全社入れ替えの件だけど、事前準備は何をすればいいんだっけ？」
女：「ええと、まず個人のデスクトップにある業務データやブックマークを、共有サーバーの指定フォルダにバックアップしておく必要があるわ。それから、必要な専門ソフトウェアの再インストール申請書を情報システム部に提出するの。」
男：「バックアップは昨日の夕方に済ませてあるよ。」
女：「さすが手際がいいわね。じゃあ申請書ね。実はその申請書の提出締め切りが今日の午後5時までなのよ。これを過ぎると新しいパソコンのセットアップが来週に間に合わなくなるから、何よりも先に申請フォームをオンラインで送ってちょうだい。」
男：「分かった。古いパソコンの返却用段ボールの受け取りは？」
女：「それは申請書を出した後、明日の朝に総務部へ取りに行けば大丈夫よ。」
男：「了解。じゃあ、急いで申請書を作成して送るよ。」""",
            "男性社員はこの後、まず何をしなければなりませんか。",
            [
                ("A", "業務データを共有サーバーにバックアップする。"),
                ("B", "総務部へ行って返却用段ボールを受け取る。"),
                ("C", "新しいパソコンの初期設定を行う。"),
                ("D", "専門ソフトの再インストール申請書を提出する。")
            ],
            "D",
            "Nữ nhân viên nhấn mạnh thời hạn gấp: '実はその申請書の提出締め切りが今日の午後5時までなのよ... 何よりも先に申請フォームをオンラインで送ってちょうだい' (Thực ra hạn chót nộp đơn đăng ký cài đặt lại phần mềm là 5 giờ chiều hôm nay, hãy ưu tiên gửi form online trước hết). Nam nhân viên đồng ý làm ngay.",
            {
                "A": "Người nam đã hoàn thành sao lưu dữ liệu từ chiều hôm qua ('バックアップは昨日の夕方に済ませてある').",
                "B": "Nhận thùng các tông bàn giao máy cũ để sáng mai sang phòng Tổng vụ lấy cũng kịp ('明日の朝に総務部へ取りに行けば大丈夫').",
                "C": "Cài đặt máy mới là việc của bộ phận hệ thống thông tin tuần sau, không phải việc nam nhân viên làm ngay bây giờ."
            },
            1
        ),
        (
            "N2_02_M1_L02",
            "Mondai 1: 課題理解 (Task) — 地域防災訓練の準備",
            """町内会の事務所で、男性役員と女性役員が来月の防災訓練について話し合っています。女性役員はこの後、まず何をしますか。

男：「来月の合同防災訓練、案内チラシの原稿ができたよ。印刷に回していいかな？」
女：「確認しますね。……あ、訓練場所が『桜小学校の校庭』になっていますが、雨天時の避難所となる体育館の使用許可はもう学校側から取れていますか？」
男：「あ、いけない！ 校庭の使用申請は出したが、体育館の空き状況はまだ確認していなかったよ。」
女：「最近は秋の天候が変わりやすいですし、雨天時に体育館が使えないと訓練計画全体を見直さなければなりません。私が今すぐ小学校の教頭先生に連絡して、体育館の利用可否を確認してきます。」
男：「ありがとう、助かるよ。体育館が確保できたら、その旨をチラシに追記して印刷を発注しよう。参加賞の非常食の手配は僕がやっておくよ。」
女：「分かりました。すぐ電話してまいります。」""",
            "女性役員はこの後、まず何をしますか。",
            [
                ("A", "小学校に連絡して体育館の使用許可を確認する。"),
                ("B", "防災訓練の案内チラシを印刷所に発注する。"),
                ("C", "訓練参加者用の非常食の在庫を確認する。"),
                ("D", "雨天中止の案内文をチラシに追記する。")
            ],
            "A",
            "Nữ cán bộ chỉ ra điểm chưa rõ: phòng thể dục làm nơi trú mưa đã xin phép chưa. Nam cán bộ nhận sơ suất chưa hỏi, nữ cán bộ chốt: '私が今すぐ小学校の教頭先生に連絡して、体育館の利用可否を確認してきます' (Tôi sẽ gọi điện ngay cho thầy hiệu phó trường tiểu học để xác nhận xem có dùng được nhà thể chất không).",
            {
                "B": "In tờ rơi phải đợi sau khi xác nhận nhà thể chất xong mới bổ sung vào rồi gửi in ('体育館が確保できたら、その旨をチラシに追記して印刷を発注しよう').",
                "C": "Chuẩn bị lương khô khẩn cấp làm quà lưu niệm do nam cán bộ đảm nhận ('非常食の手配は僕がやっておくよ').",
                "D": "Không phải thông báo hủy khi mưa mà là xác nhận địa điểm mưa vẫn tập huấn trong nhà thể chất."
            },
            2
        ),
        (
            "N2_02_M1_L03",
            "Mondai 1: 課題理解 (Task) — 学術シンポジウムの緊急対応",
            """大学の研究室で、教授と大学院生が国際シンポジウムの進行について話しています。大学院生はこの後、すぐに何をしなければなりませんか。

男（教授）：「佐藤君、大変だ。基調講演をお願いしているスミス教授の乗った飛行機が、悪天候で到着が2時間遅れると連絡が入った。」
女（院生）：「えっ、そうしますと午後の最初の講演に間に合いませんね。プログラムの順序を変更しますか？」
男：「うむ。後半に予定していたパネルディスカッションを先に行い、スミス教授の基調講演を夕方の最終枠にスライドさせよう。パンフレットの刷り直しは間に合わないから、会場前の掲示板に修正スケジュールを貼り出してくれ。」
女：「承知しました。参加予定の皆様へメールで時間変更の一斉通知を送る必要はありますか？」
男：「いや、すでに受付を済ませて会場入りしている聴衆が多いから、メールよりもまず館内アナウンスと会場入り口への案内板の設置を最優先で頼む。アナウンス原稿は私が書くから、佐藤君は今すぐ案内板を作ってホール前に立ててきてくれ。」
女：「かしこまりました。すぐに作成して設置いたします。」""",
            "大学院生はこの後、すぐに何をしなければなりませんか。",
            [
                ("A", "全参加者に時間変更の案内メールを一斉送信する。"),
                ("B", "会場のホール前に修正スケジュールの案内板を立てる。"),
                ("C", "館内放送のアナウンス原稿を作成する。"),
                ("D", "シンポジウムのパンフレットを大至急印刷し直す。")
            ],
            "B",
            "Giáo sư chỉ đạo rõ: Người tham gia đã vào hội trường đông đủ nên không cần gửi email, mà ưu tiên thông báo trực tiếp. Giáo sư tự thảo bản phát thanh, còn sinh viên được giao: '佐藤君は今すぐ案内板を作ってホール前に立ててきてくれ' (Em hãy lập tức làm bảng thông báo lịch trình sửa đổi và dựng trước cửa hội trường).",
            {
                "A": "Giáo sư bảo không cần gửi email vì cử tọa đã vào hội trường ('メールよりもまず...').",
                "C": "Bản thảo thông báo phát thanh do chính giáo sư viết ('アナウンス原稿は私が書く').",
                "D": "In lại tài liệu không kịp thời gian ('パンフレットの刷り直しは間に合わない')."
            },
            3
        ),
        (
            "N2_02_M1_L04",
            "Mondai 1: 課題理解 (Task) — アパレル店舗の冬物ディスプレイ替え",
            """アパレル店で、店長と女性店員が店内レイアウトの変更について話しています。店員はこの後、まず何をしますか。

女（店長）：「明日から急激に気温が下がる予報だから、エントランス正面の特設コーナーを秋物から冬のダウンコート特集に切り替えたいの。」
男（店員）：「分かりました。倉庫から今年の新作ダウンジャケットを運んできますね。」
女：「待って、荷解きをする前に、まず今メイン通路に並んでいる秋物の薄手トレンチコートを奥のセール棚へ移動させて、スペースを空けてちょうだい。通路が塞がっていると大きな段ボールを運び込めないから。」
男：「そうですね。先に秋物を奥へ下げます。」
女：「お願いね。スペースが空いたら、新作ダウンの検品と値札付けを二人でやりましょう。マネキンの着せ替えはその後でいいわ。」
男：「了解しました。すぐ秋物の移動にとりかかります。」""",
            "店員はこの後、まず何をしますか。",
            [
                ("A", "倉庫から新作ダウンジャケットの箱を運び出す。"),
                ("B", "新作ダウンジャケットに値札を取り付ける。"),
                ("C", "秋物のコートを奥のセール棚へ移動させて場所を空ける。"),
                ("D", "店頭マネキンの服を冬物に着せ替える。")
            ],
            "C",
            "Cửa hàng trưởng dặn: Trước khi bê thùng hàng新作 mới ra, phải dọn lối đi trước: 'まず今メイン通路に並んでいる秋物の薄手トレンチコートを奥のセール棚へ移動させて、スペースを空けてちょうだい' (Trước hết hãy dời các áo khoác thu ở lối đi chính vào kệ xả hàng phía trong để lấy chỗ trống).",
            {
                "A": "Cửa hàng trưởng ngăn lại: '待って、荷解きをする前に...' (Khoan đã, trước khi chuyển hàng dỡ thùng...).",
                "B": "Kiểm tra gắn mác giá để sau khi dọn xong chỗ hai người cùng làm ('スペースが空いたら二人でやりましょう').",
                "D": "Thay trang phục ma-nơ-canh làm sau cùng ('マネキンの着せ替えはその後でいい')."
            },
            4
        ),
        (
            "N2_02_M1_L05",
            "Mondai 1: 課題理解 (Task) — クリニックの発熱患者受付",
            """内科クリニックの受付で、看護師と新人受付スタッフが話しています。受付スタッフはこの後、来院した患者に対してまず何をしますか。

女（看護師）：「田中さん、さっき待合室に入られた男性の患者さん、少し顔が赤くて息が荒そうね。」
男（受付）：「はい、問診票をお渡しして保険証をお預かりしようとしたところです。」
女：「今の時期はインフルエンザなどの感染症が流行しているから、一般の患者さんと接触させない配慮が必要よ。保険証の登録手続きより前に、まずは体温を測っていただいて、37.5度以上あればすぐに奥の隔離ブースにご案内してちょうだい。」
男：「分かりました。体温測定ですね。」
女：「ええ。隔離ブースに入っていただいてから、感染症専用の詳しい問診票を記入してもらいましょう。診察の順番調整は医師に確認して私がやっておくわ。」
男：「承知いたしました。すぐに体温計を持ってご案内します。」""",
            "受付スタッフはこの後、来院した患者に対してまず何をしますか。",
            [
                ("A", "体温を測り、発熱があれば隔離ブースへ案内する。"),
                ("B", "保険証を預かってパソコンに保険者番号を入力する。"),
                ("C", "感染症専用の詳しい問診票を待合室で記入してもらう。"),
                ("D", "医師に相談して診察の順番を繰り上げる。")
            ],
            "A",
            "Y tá hướng dẫn quy trình kiểm soát nhiễm khuẩn: Trước khi làm thủ tục bảo hiểm, phải đo nhiệt độ trước và nếu trên 37.5 độ thì hướng dẫn vào buồng cách ly ngay: '保険証の登録手続きより前に、まずは体温を測っていただいて... 奥の隔離ブースにご案内してちょうだい'.",
            {
                "B": "Nhận thẻ bảo hiểm và nhập máy làm sau ('保険証の登録手続きより前に...').",
                "C": "Phiếu câu hỏi chuyên biệt về bệnh truyền nhiễm chỉ phát sau khi bệnh nhân đã vào buồng cách ly, không phát ngoài phòng chờ chung.",
                "D": "Điều phối thứ tự khám do y tá trực tiếp trao đổi với bác sĩ ('私がやっておくわ')."
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
            "remediation": "Nắm bắt các chỉ thị thứ tự ưu tiên (まず, 最優先で, 何よりも先に, ～の前に).",
            "status": "QA_VERIFIED",
            "exposureEligible": True,
            "diagnosticEligible": True,
            "sourceMetadata": "Original JLPT N2 Listening Corpus #02",
            "examQNum": qnum,
            "mondaiTitle": "Mondai 1: 課題理解 (Hiểu nhiệm vụ - Hành động kế tiếp)"
        })

    # =========================================================================
    # MONDAI 2: ポイント理解 (Key Points Comprehension - 6 items)
    # =========================================================================
    m2_data = [
        (
            "N2_02_M2_L01",
            "Mondai 2: ポイント理解 (Key Points) — ペットボトルキャップの改良",
            """飲料メーカーの開発部で、女性デザイナーと男性課長がお茶のボトルの新キャップについて話しています。会社がキャップの形状を変更した一番の理由は何ですか。

女：「課長、来月リニューアル発売する緑茶ボトルの新キャップ、試作品が届きました。」
男：「おお、これだね。従来のものより少し溝が深くなって、幅もひと回り大きくなっているね。プラスチックの使用量を削減するためだったっけ？」
女：「いえ、原材料のコスト削減や環境対策も検討されましたが、今回は高齢者のお客様から『指の力が弱くてキャップが固くて開けられない』というご意見が多数寄せられたことが直接の契機です。側面の凹凸を増やして握りやすくすることで、握力が弱くても小さな力でスムーズに開けられるユニバーサルデザインを採用したんです。」
男：「なるほど。誰にとっても使いやすいのが一番だね。パッケージのロゴ印刷の変更よりずっと意味のある改良だよ。」""",
            "会社がキャップの形状を変更した一番の理由は何ですか。",
            [
                ("A", "プラスチックの使用量を削減して製造コストを下げるため。"),
                ("B", "新商品のロゴマークをより大きく目立たせるため。"),
                ("C", "握力が弱い高齢者でも少ない力で容易に開けられるようにするため。"),
                ("D", "炭酸飲料の強い内圧に耐えられる密閉性を高めるため。")
            ],
            "C",
            "Lý do trực tiếp: Nhận được nhiều phản ánh của khách hàng cao tuổi ngón tay yếu không mở được nắp chai, nên công ty đổi sang thiết kế universal có rãnh sâu dễ cầm nắm, mở được chỉ với lực nhỏ ('握力が弱くても小さな力でスムーズに開けられるユニバーサルデザインを採用したんです').",
            {
                "A": "Nữ thiết kế đính chính: Cắt giảm chi phí/nhựa cũng có xem xét nhưng không phải lý do trực tiếp ('いえ、原材料のコスト削減や環境対策も検討されましたが、今回は...').",
                "B": "Nam quản lý khen việc này có ý nghĩa hơn nhiều so với đổi logo bao bì bên ngoài.",
                "D": "Đây là chai trà xanh thông thường, không phải nước có ga."
            },
            6
        ),
        (
            "N2_02_M2_L02",
            "Mondai 2: ポイント理解 (Key Points) — 社内健康プログラムの参加率向上",
            """社内ラジオで、人事部の女性担当者が社員の健康増進施策について話しています。以前は低調だった健康プログラムへの参加率が大幅に上がった決め手は何ですか。

女：「昨年まで実施していた『勤務時間外の健康セミナー』は、参加率が10％前後と伸び悩んでいました。業務終了後にわざわざ残って講義を聞くのは、社員にとって負担が大きかったためです。そこで今年度は、業務時間中の毎朝の朝礼直後に、部署全員でわずか5分間だけ行う『デスクストレッチ』に切り替えました。個人で自主的に参加させるのではなく、日々の業務ルーティンの中に最初から自然に組み込んだこと。これが参加率90％超えを達成した最大の要因です。」""",
            "健康プログラムの参加率が大幅に向上した主な理由は何ですか。",
            [
                ("A", "参加した社員にボーナスや金銭的インセンティブを支給したこと。"),
                ("B", "業務時間内の毎朝の朝礼に5分間の軽い体操を組み込んだこと。"),
                ("C", "休日に有名スポーツインストラクターを招いて本格講習を開いたこと。"),
                ("D", "スマートフォンの歩数計アプリで順位を競わせたこと。")
            ],
            "B",
            "Yếu tố quyết định: Thay vì bắt nhân viên ở lại sau giờ làm, công ty chuyển sang bài tập co giãn 5 phút ngay sau giờ họp giao ban buổi sáng trong giờ làm việc, lồng ghép vào thói quen hàng ngày ('日々の業務ルーティンの中に最初から自然に組み込んだこと。これが参加率90％超えを達成した最大の要因').",
            {
                "A": "Bài nói không đề cập đến thưởng tiền hay điểm chuyên cần.",
                "C": "Không hề mở lớp học cuối tuần với huấn luyện viên nổi tiếng.",
                "D": "Không nhắc đến thi đua đếm bước chân trên app."
            },
            7
        ),
        (
            "N2_02_M2_L03",
            "Mondai 2: ポイント理解 (Key Points) — 伝統工芸・漆器の魅力",
            """テレビの美術番組で、漆器（しっき）の職人が伝統工芸品の特長についてインタビューに答えています。職人によると、本物の漆器が持つ最も独特な魅力は何ですか。

男（職人）：「現代のプラスチックやウレタン塗装の器は、買った瞬間が一番美しく、使えば使うほど傷がついて劣化していきます。しかし、天然の漆を何層も塗り重ねた本物の漆器は正反対です。空気中の微量な水分を吸収しながら何十年もかけて硬化を続けるため、日々の生活で使い込み、布で拭き込むほどに、内側から透明感のある深い艶が生まれ、色合いが鮮やかさを増していくのです。時間とともに育ち、持ち主の手の温もりとともに輝きを増すことこそが、漆器にしかない唯一無二の魅力ですね。」""",
            "職人が述べる、本物の漆器の最も独特な魅力は何ですか。",
            [
                ("A", "ガラスのように完全に透明で、料理の色彩をそのまま透かして見せること。"),
                ("B", "化学塗料を用いており、熱いスープを入れても一切変形しないこと。"),
                ("C", "購入直後が最も美しく、長期間保管しても新品の状態を保ち続けること。"),
                ("D", "長年使い込んで手入れするほどに、内側から深い艶と透明感が増すこと。")
            ],
            "D",
            "Nghệ nhân chỉ ra điểm độc nhất vô nhị: Khác với nhựa càng dùng càng cũ, sơn mài tự nhiên càng sử dụng và lau chùi qua năm tháng thì lớp sơn càng cứng cáp, từ bên trong toát lên độ bóng sâu thẳm và trong suốt ('使い込み、布で拭き込むほどに、内側から透明感のある深い艶が生まれ...').",
            {
                "A": "Sơn mài không trong suốt như thủy tinh để nhìn thấu thức ăn.",
                "B": "Sơn mài dùng nhựa cây sơn tự nhiên (天然の漆), không phải sơn hóa học urethane.",
                "C": "Đẹp nhất ngay khi mua rồi cũ dần là đặc điểm của đồ nhựa công nghiệp, hoàn toàn đối lập với sơn mài."
            },
            8
        ),
        (
            "N2_02_M2_L04",
            "Mondai 2: ポイント理解 (Key Points) — 市立図書館の新サービス",
            """地域のラジオニュースで、市立図書館の新しい案内サービスについてリポーターが伝えています。このサービスが市民に好評な理由は何ですか。

女（リポーター）：「先月から中央図書館で始まった『読書コンシェルジュ』が、本好きの間で大きな話題となっています。これまでの検索機による機械的なキーワード検索とは異なり、司書が利用者の現在の悩みや関心事を丁寧にヒアリングし、数十万冊の蔵書の中からその人にぴったりの3冊を厳選して提案してくれます。自分では思いつきもしなかった意外なジャンルの良書に出会える点が高く評価され、週末の予約枠は常に満席となっています。」""",
            "「読書コンシェルジュ」が利用者に高く評価されている理由は何ですか。",
            [
                ("A", "司書が対話を通じて、自分では見つけられない意外な良書を推薦してくれるから。"),
                ("B", "人工知能の端末がわずか1秒でベストセラー本を検索してくれるから。"),
                ("C", "一度に借りられる本の冊数がこれまでの3倍に拡大されたから。"),
                ("D", "自宅までドローンで本を即日配達してくれるサービスがついたから。")
            ],
            "A",
            "Điểm được đánh giá cao: Khác với máy tra cứu, thủ thư trực tiếp trò chuyện lắng nghe tâm tư và gợi ý đúng 3 cuốn sách phù hợp, giúp độc giả tiếp cận được những cuốn sách hay thuộc thể loại bất ngờ mà bản thân chưa từng nghĩ tới ('自分では思いつきもしなかった意外なジャンルの良書に出会える点が高く評価され').",
            {
                "B": "Dịch vụ này thành công nhờ sự tư vấn chu đáo của con người (thủ thư), không phải máy tìm kiếm AI vô cảm.",
                "C": "Bản tin không nói về việc tăng hạn mức số lượng sách được mượn.",
                "D": "Không có dịch vụ giao sách bằng drone."
            },
            9
        ),
        (
            "N2_02_M2_L05",
            "Mondai 2: ポイント理解 (Key Points) — コアタイムなしフレックス制度の導入理由",
            """IT企業で、人事部長が全社に向けた新勤務制度の説明をしています。会社がコアタイムのない完全フレックス制を導入した決定的な理由は何ですか。

男（部長）：「来期より、従来の11時から15時までのコアタイムを撤廃し、完全に勤務時間帯を社員の裁量に委ねる制度へ移行します。通勤ラッシュの回避や育児支援という側面もありますが、経営陣が下した最大の決断理由は『海外拠点とのタイムゾーンの壁の解消』です。欧米やアジアの取引先や開発チームと共同プロジェクトを進める際、従来のコアタイムの制約があると早朝や深夜のミーティングに参加しづらく、業務の遅延が生じていました。世界各国の時差に柔軟に合わせて業務スケジュールを組めるようにすることが、グローバル競争力を高める鍵なのです。」""",
            "会社が完全フレックスタイム制を導入した決定的な理由は何ですか。",
            [
                ("A", "オフィスの電気代や水道代などの固定維持費を削減するため。"),
                ("B", "社員全員に必ず毎朝早朝出勤を義務付けるため。"),
                ("C", "海外拠点との時差に合わせて柔軟にプロジェクトを進めるため。"),
                ("D", "残業手当の支払いを全額カットして人件費を抑えるため。")
            ],
            "C",
            "Trưởng phòng nhân sự tuyên bố lý do lớn nhất của ban lãnh đạo: Giải quyết rào cản múi giờ với các chi nhánh và đối tác nước ngoài để dự án không bị đình trệ ('経営陣が下した最大の決断理由は『海外拠点とのタイムゾーンの壁の解消』です... 時差に柔軟に合わせて業務スケジュールを組めるようにすること').",
            {
                "A": "Không nhằm mục đích tiết kiệm điện nước văn phòng.",
                "B": "Bỏ khung giờ bắt buộc chứ không bắt đi làm sớm.",
                "D": "Không phải để cắt giảm lương hay tiền làm thêm giờ."
            },
            10
        ),
        (
            "N2_02_M2_L06",
            "Mondai 2: ポイント理解 (Key Points) — デジタル眼精疲労の予防法",
            """健康番組のインタビューで、眼科医がパソコン作業に伴う目の疲れの予防法について解説しています。医師が最も効果的だと推奨する対策は何ですか。

女（医師）：「長時間の画面作業で目がかすんだり頭痛が起きたりする原因は、画面を凝視し続けることでピント調節を司る『毛様体筋』が緊張して固まってしまうことにあります。高価なブルーライトカット眼鏡や目薬を使うことも悪くはありませんが、筋肉の疲労を元から取る最も確実な方法は『20-20-20の法則』です。20分間パソコンを見たら、作業を止めて、20フィート、つまり約6メートル以上離れた遠くの景色を20秒間ぼんやり眺めること。遠くを見ることで目の筋肉の緊張が一気に緩み、疲労の蓄積を防ぐことができるのです。」""",
            "医師が推奨している最も確実で効果的な目の疲労予防策は何ですか。",
            [
                ("A", "高価なブルーライトカット眼鏡を常に2重にかけて作業すること。"),
                ("B", "20分ごとに作業を止め、6メートル以上遠くの景色を20秒間眺めること。"),
                ("C", "1時間ごとに市販の強い清涼感のある目薬を大量に点眼すること。"),
                ("D", "パソコンの画面の明るさを限界まで暗くして作業すること。")
            ],
            "B",
            "Bác sĩ chỉ ra giải pháp cốt lõi và chắc chắn nhất là quy tắc 20-20-20: Cứ sau 20 phút nhìn màn hình thì nghỉ 20 giây và nhìn vào vật thể cách xa ít nhất 6 mét (20 feet) để cơ điều tiết của mắt được thả lỏng hoàn toàn ('最も確実な方法は『20-20-20の法則』です。20分間パソコンを見たら... 約6メートル以上離れた遠くの景色を20秒間ぼんやり眺めること').",
            {
                "A": "Bác sĩ nói kính chống ánh sáng xanh cũng được nhưng không phải cách giải tỏa mỏi cơ then chốt, và không ai đeo kính 2 lớp.",
                "C": "Thuốc nhỏ mắt chỉ là giải pháp tạm thời bên ngoài.",
                "D": "Giảm độ sáng quá mức có thể khiến mắt phải căng ra nhìn, không được khuyến nghị."
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
            "remediation": "Lắng nghe lý do cốt lõi xuất hiện sau các từ nối chuyển ý (いえ、～が直接の契機, 最大の決断理由は, 最も確実な方法は).",
            "status": "QA_VERIFIED",
            "exposureEligible": True,
            "diagnosticEligible": True,
            "sourceMetadata": "Original JLPT N2 Listening Corpus #02",
            "examQNum": qnum,
            "mondaiTitle": "Mondai 2: ポイント理解 (Hiểu điểm mấu chốt - Trích xuất nguyên nhân)"
        })

    # =========================================================================
    # MONDAI 3: 概要理解 (General Comprehension - Monologue - 5 items)
    # =========================================================================
    m3_data = [
        (
            "N2_02_M3_L01",
            "Mondai 3: 概要理解 (General) — 都市のグリーンネットワークと生態系保全",
            """大学の環境学の講義で、教授が都市計画と生物多様性について話しています。

男（教授）：「大都市における自然保護というと、広大な森林公園を新しく造成することばかりが議論されがちです。しかし、どれほど広大な公園を作っても、周囲がコンクリートで完全に孤立していれば、鳥や昆虫などの小動物は近親交配が進んで個体数が減少してしまいます。今、生態系保全の現場で最も重視されているのは『エコロジカル・ネットワーク』、すなわち緑の回廊の形成です。街路樹を連続させたり、河川敷の草地を残したり、ビルの屋上やベランダに緑化スポットを飛び石のように配置すること。これにより、生き物が街全体を自由に移動できるようになり、都市全体の生態系の豊かさが維持されるのです。」""",
            "教授は何について話していますか。",
            [
                ("A", "孤立した大規模公園よりも、緑を回廊状につなぐネットワークが生態系維持に不可欠であること。"),
                ("B", "都市のコンクリート建築物をすべて解体して原生林へと戻す環境再生の手法。"),
                ("C", "河川敷の雑草をすべて刈り取って近代的な運動公園を造成する計画。"),
                ("D", "街路樹に集まる害虫を駆除するための最新の化学薬品の散布方法。")
            ],
            "A",
            "Giáo sư trình bày luận điểm: Để duy trì đa dạng sinh học trong đô thị, việc tạo ra các hành lang cây xanh kết nối liên hoàn (Ecological Network) quan trọng hơn nhiều so với việc chỉ xây những công viên biệt lập bị bao vây bởi bê tông.",
            {
                "B": "Không bàn về đập bỏ nhà cao tầng để phục hồi rừng nguyên sinh.",
                "C": "Không nói về việc chặt cỏ làm sân vận động.",
                "D": "Không đề cập đến việc xịt thuốc trừ sâu hóa học trên cây xanh đường phố."
            },
            12
        ),
        (
            "N2_02_M3_L02",
            "Mondai 3: 概要理解 (General) — 行動経済学の「おとり効果」",
            """ラジオの経済解説番組で、専門家が消費者の購買心理について話しています。

女（専門家）：「レストランのランチメニューで、2,000円のAランチと1,200円のBランチの2種類だけだと、多くの人は割安な1,200円のBを選びがちです。ところが、ここに新たに3,500円の超豪華な『特選プレミアムランチ』を加えると、不思議な現象が起きます。最も高額な3,500円のメニューはほとんど売れないにもかかわらず、これまで敬遠されていた2,000円のAランチの売れ行きが急激に跳ね上がるのです。これは行動経済学で『おとり効果』と呼ばれる現象です。人間は絶対的な価値ではなく、提示された選択肢の中での『極端の回避』、つまり高すぎず安すぎない無難な中間を選びたくなる心理を持っています。企業はこの心理を巧みに活用して、売りたい価格帯へ消費者を誘導しているのです。」""",
            "専門家が最も主張したいことは何ですか。",
            [
                ("A", "レストランは最も高価な料理を看板商品として大量に仕入れるべきであること。"),
                ("B", "消費者は常に最も安い商品だけを選び続けるという絶対的な法則があること。"),
                ("C", "豪華な料理の写真を見せるだけで客の食欲を何倍にも増進させられること。"),
                ("D", "人間には極端を避けて中間を選ぶ心理があり、企業はあえて高い選択肢を置いて本命の商品へ誘導していること。")
            ],
            "D",
            "Chuyên gia phân tích tâm lý người tiêu dùng: Con người luôn có xu hướng tránh 2 thái cực (quá đắt và quá rẻ) để chọn phương án ở giữa. Doanh nghiệp đặt ra 'món chim mồi' giá rất cao không phải để bán món đó mà để thúc đẩy khách mua món ở tầm giá mà họ thực sự muốn bán.",
            {
                "A": "Món giá cao nhất thực chất hầu như không bán được ('ほとんど売れない') và không phải mục tiêu chính.",
                "B": "Bài nói khẳng định khi có món thứ 3 thì khách không còn đổ xô chọn món rẻ nhất nữa.",
                "C": "Không bàn về hình ảnh kích thích vị giác."
            },
            13
        ),
        (
            "N2_02_M3_L03",
            "Mondai 3: 概要理解 (General) — 日本建築における「仕切り」の柔軟性",
            """美術館の講演会で、建築史の学芸員が伝統的な日本家屋の特質について話しています。

男（学芸員）：「西洋の伝統的な石造り建築では、壁は建物の重みを支える構造体であり、部屋と部屋は重厚な壁とドアによって厳格に遮断されています。一度作られた空間は固定され、用途を変更することは容易ではありません。一方、柱と梁で支える木造の日本建築では、空間を仕切る『襖（ふすま）』や『障子（しょうじ）』は構造上の壁ではなく、取り外し自在な装置にすぎません。襖を閉めれば独立した私室となり、取り払えば大勢が集まる大広間へと一瞬で変貌します。外部の自然との境界も雨戸を開け放てば庭と一体化する。固定的な境界を持たず、生活の場面に応じて空間を伸縮させる柔軟性こそが、日本建築の最大の知恵なのです。」""",
            "学芸員は日本建築のどのような特質を強調していますか。",
            [
                ("A", "地震や台風に耐えるために西洋の石造り工法を忠実に模倣したこと。"),
                ("B", "襖や障子によって空間の境界を固定せず、用途に応じて柔軟に変化させられること。"),
                ("C", "プライバシーを守るために頑丈な防音壁で部屋を完全に密閉したこと。"),
                ("D", "木材の腐食を防ぐために一年中雨戸を閉め切って生活していたこと。")
            ],
            "B",
            "Chuyên viên kiến trúc làm nổi bật trí tuệ kiến trúc Nhật Bản: Cửa lùa Fusuma và Shoji không phải tường chịu lực mà là vách ngăn di động, cho phép không gian linh hoạt đóng mở theo nhu cầu sử dụng (tách phòng riêng hoặc mở toang thành đại sảnh, hòa làm một với sân vườn).",
            {
                "A": "Kiến trúc gỗ Nhật Bản đi theo nguyên lý hoàn toàn khác với kiến trúc đá phương Tây.",
                "C": "Nhà truyền thống Nhật không dùng tường đá cách âm kiên cố.",
                "D": "Ngược lại, mở cửa liếp đón thiên nhiên sân vườn là nét đặc trưng."
            },
            14
        ),
        (
            "N2_02_M3_L04",
            "Mondai 3: 概要理解 (General) — 組織における「心理的安全性」の役割",
            """経営セミナーで、組織論のコンサルタントがチームの生産性向上について講演しています。

女（コンサルタント）：「優れた能力を持つ人材を集めたにもかかわらず、新規事業で成果を出せないチームが後を絶ちません。その根本原因を突き詰めると、組織内の『心理的安全性』の欠如に行き着きます。心理的安全性とは、無知や失敗を恐れずに自分の意見や疑問を率直に口にできる安心感のことです。これが欠けていると、メンバーはミスを隠蔽し、上司の顔色をうかがって当たり障りのない提案しかしなくなります。小さな違和感や失敗を早期に共有し、互いに建設的に議論できる文化があるチームほど、変化への適応スピードが速く、最終的に革新的な成果を生み出すことができるのです。」""",
            "コンサルタントは何が組織の成功に最も重要だと主張していますか。",
            [
                ("A", "社員同士の私的な会話を一切禁じて、業務効率を極限まで高めること。"),
                ("B", "失敗した社員に対して厳しい懲戒処分を科して、緊張感を維持すること。"),
                ("C", "失敗や疑問を恐れずに率直に発言できる「心理的安全性」を職場に醸成すること。"),
                ("D", "すべての判断をAIのアルゴリズムに任せ、人間の感情を排除すること。")
            ],
            "C",
            "Diễn giả nhấn mạnh điều kiện tiên quyết cho một tập thể thành công: Xây dựng 'An toàn tâm lý' (Psychological Safety) - nơi các thành viên không sợ bị phán xét khi thừa nhận sai sót hay đặt câu hỏi, nhờ đó phát hiện sớm rủi ro và cùng tạo ra giải pháp đổi mới.",
            {
                "A": "Cấm đoán trò chuyện làm thui chột tinh thần hợp tác.",
                "B": "Trừng phạt khắt khe chỉ khiến nhân viên giấu giếm lỗi lầm.",
                "D": "Không đề xuất thay thế toàn bộ quản lý bằng thuật toán AI."
            },
            15
        ),
        (
            "N2_02_M3_L05",
            "Mondai 3: 概要理解 (General) — 発酵技術と食品ロスの有効活用",
            """食品科学のシンポジウムで、研究者が発酵技術の新たな可能性について報告しています。

男（研究者）：「世界的な食糧問題と環境負荷の増大を背景に、食品廃棄物の削減が急務となっています。従来、野菜の芯や皮、酒造りの過程で出る酒粕などは、その多くが産業廃棄物として焼却処分されてきました。しかし近年、日本の伝統的な麹菌や乳酸菌を用いた先端バイオ技術により、これら未利用資源を劇的に価値あるものへと転換する研究が進んでいます。廃棄されていた端材に微生物を作用させることで、濃厚なうま味成分を持つ機能性調味料や、家畜の免疫力を高める高栄養飼料へとアップサイクルできるのです。発酵は単なる食品保存の知恵にとどまらず、持続可能な食の循環を生み出す最先端の環境技術なのです。」""",
            "研究者は発酵技術についてどのような点を強調していますか。",
            [
                ("A", "廃棄されていた食品残渣を発酵によって高価値な調味料や飼料へ再生できること。"),
                ("B", "すべての食品残渣を直ちに埋め立て処分することが最も環境に優しいこと。"),
                ("C", "化学調味料の製造コストを下げるために麹菌を海外から大量輸入すること。"),
                ("D", "伝統的な日本酒の醸造において手作業の工程をすべてロボット化すること。")
            ],
            "A",
            "Nhà nghiên cứu nhấn mạnh tiềm năng to lớn của vi sinh vật lên men (men Koji, vi khuẩn Lactic): Tái chế các phụ phẩm thực phẩm tưởng như bỏ đi thành gia vị đậm đà umami và thức ăn chăn nuôi giàu dinh dưỡng (Upcycling).",
            {
                "B": "Chôn lấp rác thực phẩm gây hại môi trường, hoàn toàn ngược với bài nói.",
                "C": "Không bàn về nhập khẩu men Koji để làm mì chính.",
                "D": "Không nói về việc tự động hóa nhà máy nấu rượu Sake."
            },
            16
        )
    ]

    for qid, title, script, stem, opts, ans, exp, dist, qnum in m3_data:
        # In Mondai 3: options are spoken on audio, question paper has NO printed choices.
        # But for engine display and review, 4 choices are defined.
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
            "remediation": "Lắng nghe cấu trúc tổng quan của bài thuyết trình: nêu vấn đề thực trạng -> giải pháp cốt lõi -> kết luận khái quát.",
            "status": "QA_VERIFIED",
            "exposureEligible": True,
            "diagnosticEligible": True,
            "sourceMetadata": "Original JLPT N2 Listening Corpus #02",
            "examQNum": qnum,
            "mondaiTitle": "Mondai 3: 概要理解 (Hiểu đại ý - Độc thoại chủ đề học thuật/xã hội)"
        })

    # =========================================================================
    # MONDAI 4: 即時応答 (Quick Response - 11 items, 3 options each)
    # =========================================================================
    m4_data = [
        (
            "N2_02_M4_L01",
            "田中部長、先ほどの会議の議事録を作成したのですが、目を通していただけないでしょうか。",
            [
                ("A", "ええ、もう会議は始まっているよ。"),
                ("B", "分かった、机の上に置いておいてくれたまえ。"),
                ("C", "いえ、私の目は通っていませんよ。")
            ],
            "B",
            "Lời nhờ vả lịch thiệp của cấp dưới: 'Trưởng phòng Tanaka, em đã soạn biên bản cuộc họp lúc nãy, trưởng phòng có thể xem qua giúp em được không ạ?'. Đáp lại chuẩn mực: 'Được rồi, cậu cứ để trên bàn cho tôi'.",
            {
                "A": "Biên bản sau cuộc họp chứ cuộc họp không phải đang diễn ra.",
                "C": "Dịch nghĩa đen chữ 目を通す là trò đùa vô nghĩa, sai ngữ dụng giao tiếp."
            },
            17
        ),
        (
            "N2_02_M4_L02",
            "プレゼンのリハーサル、もう少し時間をかけておくべきだったね。",
            [
                ("A", "おっしゃる通りです。準備不足を痛感しました。"),
                ("B", "ええ、時間をかけすぎて飽きてしまいました。"),
                ("C", "いえ、明日リハーサルを始める予定です。")
            ],
            "A",
            "Nhận xét tiếc nuối: 'Đáng lẽ chúng ta nên dành thêm chút thời gian tập dượt thuyết trình nhỉ'. Đáp lại đồng tình nhận lỗi: 'Đúng như anh nói ạ, em cũng cảm thấy thấm thía sự thiếu chuẩn bị'.",
            {
                "B": "Nói 'tốn quá nhiều thời gian nên phát ngấy' đi ngược lại ý 'đáng lẽ nên dành thêm thời gian'.",
                "C": "Buổi thuyết trình đã xong xuôi rồi, không thể nói 'dự định ngày mai mới tập dượt'."
            },
            18
        ),
        (
            "N2_02_M4_L03",
            "恐れ入りますが、こちらの書類にお名前をご記入願えますか。",
            [
                ("A", "はい、どうぞご自由にお書きください。"),
                ("B", "いいえ、名前は知っていますよ。"),
                ("C", "はい、この欄に書けばよろしいでしょうか。")
            ],
            "C",
            "Nhân viên đề nghị lịch sự: 'Xin thứ lỗi, anh/chị vui lòng điền tên vào giấy tờ này giúp em được không ạ?'. Khách hàng đáp lại: 'Vâng, tôi viết vào ô này là được phải không ạ?'.",
            {
                "A": "Người ta nhờ mình viết mà mình lại bảo đối phương 'mời bạn cứ tự do viết' là sai chủ thể.",
                "B": "Trả lời cộc cằn 'tôi biết tên rồi' là lạc đề."
            },
            19
        ),
        (
            "N2_02_M4_L04",
            "明日の課の歓送迎会、山田さんも顔を出せそう？",
            [
                ("A", "ええ、顔を洗ってから行きますね。"),
                ("B", "あいにく先約がありまして、今回は遠慮させてください。"),
                ("C", "はい、顔がとても広いですからね。")
            ],
            "B",
            "Lời rủ rê: 'Buổi liên hoan chia tay chào đón thành viên mới ngày mai của phòng, Yamada có ghé qua tham gia được không?'. Từ chối khéo léo: 'Tiếc quá em lại có hẹn trước mất rồi, xin phép lần này cho em không tham gia ạ'.",
            {
                "A": "Dịch nghĩa đen 'rửa mặt rồi mới đi' cho quán dụng ngữ 顔を出す (ghé mặt/tham dự) là sai ngớ ngẩn.",
                "C": "顔が広い là quen biết rộng, trả lời không ăn nhập câu hỏi."
            },
            20
        ),
        (
            "N2_02_M4_L05",
            "この大規模なプロジェクト、新人の佐藤さん一人に任せるのは荷が重すぎないか。",
            [
                ("A", "おっしゃる通りです。先輩社員をサポートにつけましょう。"),
                ("B", "はい、段ボールの荷物が重すぎて運べません。"),
                ("C", "いえ、佐藤さんは一人で十分満足しているはずです。")
            ],
            "A",
            "Bày tỏ lo ngại: 'Dự án quy mô lớn thế này mà giao cho một mình người mới như Sato thì có quá sức (quá tải) không nhỉ?'. Đáp lại chuẩn: 'Đúng như anh nói, chúng ta nên bố trí nhân viên tiền bối hỗ trợ'.",
            {
                "B": "Nhầm quán dụng ngữ 荷が重い (trách nhiệm quá nặng nề) thành khiêng vác hành lý thực tế.",
                "C": "Nói Sato 'hài lòng một mình' không giải quyết rủi ro dự án thất bại."
            },
            21
        ),
        (
            "N2_02_M4_L06",
            "せっかく遠くまで足を運んでいただいたのに、お役に立てず申し訳ありません。",
            [
                ("A", "ええ、足がとても疲れましたよ。"),
                ("B", "いえ、二度と来ることはありません。"),
                ("C", "とんでもないです。詳しいお話を伺えただけでも有意義でした。")
            ],
            "C",
            "Đối tác xin lỗi vì không giúp được dù mình đã cất công đến tận nơi: 'Rất xin lỗi vì anh/chị đã cất công đến xa xôi thế này mà bên em lại chưa giúp được gì'. Đáp lễ lịch sự: 'Đâu có ạ, chỉ riêng việc được lắng nghe trao đổi chi tiết thế này đã rất bổ ích với em rồi ạ'.",
            {
                "A": "Than phiền 'mỏi chân lắm' là bất lịch sự trong giao tiếp kinh doanh.",
                "B": "Nói 'tôi sẽ không bao giờ đến nữa' là thô lỗ, cắt đứt quan hệ."
            },
            22
        ),
        (
            "N2_02_M4_L07",
            "先輩、昨日お貸しした参考資料、もうご覧になりましたでしょうか。",
            [
                ("A", "うん、君に見せてあげるよ。"),
                ("B", "ああ、急ぎの仕事が入ってまだ読めてないんだ。今日中に目を通すよ。"),
                ("C", "はい、私が資料を貸してあげました。")
            ],
            "B",
            "Hỏi thăm lịch thiệp: 'Tiền bối ơi, tài liệu tham khảo hôm qua em cho mượn tiền bối đã xem qua chưa ạ?'. Trả lời thẳng thắn và hẹn giờ xem: 'À, có việc gấp chèn vào nên anh chưa kịp đọc, trong hôm nay anh sẽ xem nhé'.",
            {
                "A": "Tài liệu của cấp dưới cho mượn, không thể nói 'để anh cho em xem'.",
                "C": "Nhầm chủ thể ai cho ai mượn tài liệu."
            },
            23
        ),
        (
            "N2_02_M4_L08",
            "課長、企画案の提出期限ですが、週明けの月曜まで延ばしていただけないでしょうか。",
            [
                ("A", "うーん、月曜の朝一番に出せるなら構わないよ。"),
                ("B", "ええ、もう月曜日が過ぎてしまいましたよ。"),
                ("C", "はい、期限を早めて提出してください。")
            ],
            "A",
            "Cấp dưới xin lùi hạn nộp: 'Trưởng phòng, hạn nộp bản kế hoạch cho em lùi đến sáng thứ Hai đầu tuần được không ạ?'. Quản lý đồng ý có điều kiện: 'Ừm, nếu nộp được ngay sáng sớm thứ Hai thì được thôi'.",
            {
                "B": "Thứ Hai tuần tới chứ chưa trôi qua.",
                "C": "Xin lùi hạn mà bảo 'hãy nộp sớm hơn hạn' là mâu thuẫn."
            },
            24
        ),
        (
            "N2_02_M4_L09",
            "駅前に新しくできたパン屋さん、夕方にはいつも完売しちゃうんだって。",
            [
                ("A", "そうなんだ。じゃあ夕方遅くに行ってみようか。"),
                ("B", "へえ、そんなに人気ならお昼休みに買いに行ってみようかな。"),
                ("C", "うん、売れ残って困っているらしいね。")
            ],
            "B",
            "Thông tin đời sống: 'Tiệm bánh mì mới mở trước ga nghe bảo cứ đến chiều tối là bán hết sạch queo'. Phản xạ logic: 'Chà, đắt khách thế thì chắc tranh thủ giờ nghỉ trưa tớ phải ra mua mới được'.",
            {
                "A": "Chiều tối hết sạch mà lại bảo 'thế thì chiều muộn hẵng đi' là phi lý.",
                "C": "Bán hết sạch (完売) trái ngược hoàn toàn với ế ẩm thừa hàng (売れ残る)."
            },
            25
        ),
        (
            "N2_02_M4_L10",
            "来期からの海外支社への転勤の打診、引き受けて本当に後悔はないの？",
            [
                ("A", "ええ、後悔ばかりで毎日憂鬱です。"),
                ("B", "はい、国内勤務に留まることにしました。"),
                ("C", "はい。自分自身のキャリアを広げる絶好の挑戦だと思っています。")
            ],
            "C",
            "Hỏi thăm quyết định lớn: 'Chuyện được đề bạt chuyển công tác sang chi nhánh nước ngoài kỳ tới, cậu nhận lời thật sự không hối hận chứ?'. Bày tỏ quyết tâm: 'Vâng ạ, em nghĩ đây là cơ hội tuyệt vời để mở rộng sự nghiệp của bản thân'.",
            {
                "A": "Chưa đi mà bảo 'ngày nào cũng u sầu toàn thấy hối hận' là mâu thuẫn với việc đã dứt khoát nhận lời.",
                "B": "Đã nhận lời đi nước ngoài thì không thể bảo 'tôi đã quyết định ở lại làm trong nước'."
            },
            26
        ),
        (
            "N2_02_M4_L11",
            "部長、本日発熱があり体調が優れないため、大変恐縮ですがお休みをいただきたいのですが。",
            [
                ("A", "それは心配だね。業務のことは気にせず、今日はしっかり療養しなさい。"),
                ("B", "はい、私が代わりに休みを取ってあげましょう。"),
                ("C", "ええ、遠慮なく会社に来て仕事してください。")
            ],
            "A",
            "Xin nghỉ ốm qua điện thoại: 'Trưởng phòng, hôm nay em bị sốt người không khỏe, em rất xin lỗi nhưng cho phép em xin nghỉ hôm nay ạ'. Lãnh đạo hồi đáp chuẩn mực: 'Thế thì lo quá. Công việc đừng bận tâm, hôm nay cứ tĩnh dưỡng cho lại sức đi'.",
            {
                "B": "Trưởng phòng không thể nói 'để tôi nghỉ hộ cậu'.",
                "C": "Người ta đang sốt mà bảo 'cứ tự nhiên đến công ty làm việc' là vô cảm và lây bệnh."
            },
            27
        )
    ]

    for qid, prompt_text, opts, ans, exp, dist, qnum in m4_data:
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
            "remediation": "Luyện tập kính ngữ công sở (khiêm nhường ngữ, tôn kính ngữ), quán dụng ngữ và từ chối khéo léo.",
            "status": "QA_VERIFIED",
            "exposureEligible": True,
            "diagnosticEligible": True,
            "sourceMetadata": "Original JLPT N2 Listening Corpus #02",
            "examQNum": qnum,
            "mondaiTitle": "Mondai 4: 即時応答 (Phản xạ tức thì - 3 lựa chọn nghe)"
        })

    # =========================================================================
    # MONDAI 5: 統合理解 (Integrated Comprehension - 3 items)
    # =========================================================================
    # Case 1: Company training seminar venue selection (社員研修の会場選び) -> 2 items (Q28, Q29)
    # Case 2: Office coffee maker selection (オフィスのコーヒーメーカー選定) -> 1 item (Q30)

    script_m5_case1 = """会社の総務人事部で、男性社員と女性課長が来月の新任リーダー研修の会場選びについて相談しています。

男：「課長、来月実施予定のリーダー研修ですが、社内の会議室が改装工事で使えないため、外部の貸し会議室を探しました。条件に合いそうな候補が4つあります。」
女：「そうね。参加者は30名で、予算は半日で税込み12万円以内だったわね。研修の内容は講義だけじゃなく、5人ずつのグループワークを何度も行うから、机や椅子を自由に動かせるレイアウト変更が可能な部屋であることが必須条件よ。それから、全員が持参したノートPCでオンライン演習をするから、大容量のWi-Fiが安定してつながることも絶対に譲れないわ。」
男：「はい、承知しています。まず【1番のグランドホール】です。格式が高く設備も最新ですが、座席が固定式の階段シアター形式になっていて机が動かせません。料金は半日10万円です。」
女：「固定席だとグループディスカッションができないから、いくら安くても無理ね。」
男：「次に【2番のステーションプラザ】。駅から徒歩3分でアクセス抜群です。キャスター付きの可動式デスクで島型レイアウトに自由に変更できます。専有の高速光Wi-Fi完備で、料金は半日11万円と予算内です。」
女：「いいわね！ 3番と4番はどう？」
男：「【3番のグリーンガーデン】は緑が見える静かな環境で、可動式デスクもあり半日8万円と一番安いです。ただ、駅からバスで20分かかり、Wi-Fiは建物の共用回線で大人数の同時接続には不安があります。最後に【4番のテックベイ】。最新の高速Wi-Fiと可動式デスクを備えていますが、半日で14万円と予算オーバーです。」
女：「なるほどね。ネット回線が不安定だと研修自体がストップしてしまうし、やっぱり条件をすべてクリアしているあの部屋で決定しましょう。すぐに予約手続きを取ってちょうだい。」
男：「分かりました。ではそちらを押さえます。」"""

    # Q28
    items.append({
        "id": "N2_02_M5_L01",
        "level": "N2",
        "skill": "Listening",
        "typeId": "N2-LIS-INTE",
        "stem": "必須条件をすべて満たし、2人が最終的に予約することにした会議室はどれですか。",
        "stimulusId": "N2_02_M5_CASE1",
        "contextPassage": script_m5_case1,
        "options": [
            {"id": "A", "text": "1番のグランドホール"},
            {"id": "B", "text": "2番のステーションプラザ"},
            {"id": "C", "text": "3番のグリーンガーデン"},
            {"id": "D", "text": "4番のテックベイ"}
        ],
        "correctAnswer": "B",
        "explanationVi": "Phòng số 2 (ステーションプラザ) thỏa mãn trọn vẹn mọi điều kiện: giá 11 vạn yên (dưới ngân sách 12 vạn), bàn ghế có bánh xe ghép nhóm thảo luận được, Wi-Fi quang tốc độ cao riêng biệt, cách ga chỉ 3 phút đi bộ.",
        "distractorExplanations": {
            "A": "Phòng 1 giá 10 vạn nhưng ghế bậc thang gắn cố định (固定式), không thể kê bàn thảo luận nhóm.",
            "C": "Phòng 3 giá rẻ nhất (8 vạn) nhưng mạng Wi-Fi dùng chung chập chờn và cách xa ga (phải đi xe buýt 20 phút).",
            "D": "Phòng 4 trang thiết bị tốt nhưng giá 14 vạn, vượt trần ngân sách cho phép (12 vạn)."
        },
        "difficultyEstimate": 3,
        "conceptId": "listening-integrated",
        "remediation": "Lập bảng đối chiếu 4 điều kiện: ngân sách (<= 12 vạn), bàn ghế di động (可動式), Wi-Fi riêng ổn định cho 30 máy, và cự ly đi lại.",
        "status": "QA_VERIFIED",
        "exposureEligible": True,
        "diagnosticEligible": True,
        "sourceMetadata": "Original JLPT N2 Listening Corpus #02",
        "examQNum": 28,
        "mondaiTitle": "Mondai 5: 統合理解 (Hiểu tổng hợp — Đối chiếu nhiều điều kiện)"
    })

    # Q29
    items.append({
        "id": "N2_02_M5_L02",
        "level": "N2",
        "skill": "Listening",
        "typeId": "N2-LIS-INTE",
        "stem": "女性課長が1番の会議室を即座に却下した決定的な理由は何ですか。",
        "stimulusId": "N2_02_M5_CASE1",
        "contextPassage": script_m5_case1,
        "options": [
            {"id": "A", "text": "座席が固定式で、グループワーク用の配置に変更できないから。"},
            {"id": "B", "text": "利用料金が予算の12万円を大幅に超えているから。"},
            {"id": "C", "text": "インターネットのWi-Fi設備がまったく導入されていないから。"},
            {"id": "D", "text": "駅から遠く、バスに乗らなければたどり着けないから。"}
        ],
        "correctAnswer": "A",
        "explanationVi": "Nữ trưởng phòng gạt bỏ ngay phòng số 1 vì ghế gắn cố định kiểu bậc thang không xếp nhóm làm workshop được: '固定席だとグループディスカッションができないから、いくら安くても無理ね'.",
        "distractorExplanations": {
            "B": "Phòng 1 giá 10 vạn nằm trong ngân sách 12 vạn chứ không vượt ngân sách.",
            "C": "Phòng 1 thiết bị tối tân, không phải không có mạng.",
            "D": "Phòng phải đi xe buýt 20 phút là phòng số 3 (グリーンガーデン)."
        },
        "difficultyEstimate": 3,
        "conceptId": "listening-integrated",
        "remediation": "Nắm bắt phản ứng trực tiếp của nhân vật: '固定席だと... いくら安くても無理ね'.",
        "status": "QA_VERIFIED",
        "exposureEligible": True,
        "diagnosticEligible": True,
        "sourceMetadata": "Original JLPT N2 Listening Corpus #02",
        "examQNum": 29,
        "mondaiTitle": "Mondai 5: 統合理解 (Hiểu tổng hợp — Phân tích lý do loại trừ)"
    })

    # Case 2: Office coffee maker selection -> 1 item (Q30)
    script_m5_case2 = """オフィスの給湯室で、総務部の男性社員と女性社員が新しく購入する共用コーヒーメーカーについて話しています。

男：「部署のみんなから要望が出ていた新しいコーヒーメーカー、予算5万円以内で4つのモデルを比較してみたよ。」
女：「助かるわ。毎朝20人以上が一斉に飲むから、一度に最低でも10杯分は抽出できる大容量タイプじゃないと困るわね。それから一番大事なのは毎日の手入れの簡単さよ。ミルクのノズルや複雑な配管があると、毎日分解して薬品洗浄するのが大変で誰も手入れしなくなっちゃうから。」
男：「そうだね。まず【1番の全自動カプチーノ機】。本格的なミルク泡立て機能付きで4万8,000円。ただ、一度に1杯ずつしか淹れられず、ミルク配管の毎日の分解清掃が必須なんだ。」
女：「それは朝の混雑時に大行列ができるし、手入れが面倒で絶対に放置されるわね。」
男：「【2番の大容量ドリップ式】は、一度に12杯抽出できて、真空ステンレス魔法瓶ポットに直接保温されるから煮詰まらない。フィルター容器は丸洗いできてミルク配管もないから、水洗いだけで済むよ。価格は4万2,000円。」
女：「まさに理想的じゃない！ 3番と4番は？」
男：「【3番のカプセル式】は3万円で手入れは最も楽だけど、専用カプセル代が1杯100円かかって毎月のランニングコストが高すぎる。【4番の本格エスプレッソ機】は6万5,000円で予算オーバーだ。」
女：「となると、容量も十分で手入れが一番手軽で、予算にも収まるあの一択ね。」
男：「よし、じゃあそのモデルを発注するよ。」"""

    # Q30
    items.append({
        "id": "N2_02_M5_L03",
        "level": "N2",
        "skill": "Listening",
        "typeId": "N2-LIS-INTE",
        "stem": "条件を総合的に考慮して、2人が購入することにしたコーヒーメーカーはどれですか。",
        "stimulusId": "N2_02_M5_CASE2",
        "contextPassage": script_m5_case2,
        "options": [
            {"id": "A", "text": "1番の全自動カプチーノ機"},
            {"id": "B", "text": "2番の大容量ドリップ式"},
            {"id": "C", "text": "3番のカプセル式"},
            {"id": "D", "text": "4番の本格エスプレッソ機"}
        ],
        "correctAnswer": "B",
        "explanationVi": "Máy số 2 (Đại dung lượng drip) thỏa mãn toàn diện: giá 42,000 yên (dưới trần 50,000 yên), pha một lần được 12 cốc cho hơn 20 người dùng buổi sáng, bình giữ nhiệt inox không khét, không có ống dẫn sữa phức tạp, chỉ cần tráng rửa nước là xong.",
        "distractorExplanations": {
            "A": "Máy 1 chỉ pha được 1 cốc mỗi lần gây ùn tắc và đòi hỏi tháo rửa ống dẫn sữa hàng ngày phức tạp.",
            "C": "Máy 3 giá rẻ lúc mua nhưng chi phí viên nén hàng tháng quá đắt (100 yên/ly) cho văn phòng 20 người.",
            "D": "Máy 4 giá 65,000 yên vượt mức ngân sách trần 50,000 yên."
        },
        "difficultyEstimate": 3,
        "conceptId": "listening-integrated",
        "remediation": "Đối chiếu bảng tiêu chí: ngân sách (< 5 vạn), dung tích (>= 10 cốc/lần), và vệ sinh dễ dàng không cần súc rửa ống sữa phức tạp.",
        "status": "QA_VERIFIED",
        "exposureEligible": True,
        "diagnosticEligible": True,
        "sourceMetadata": "Original JLPT N2 Listening Corpus #02",
        "examQNum": 30,
        "mondaiTitle": "Mondai 5: 統合理解 (Hiểu tổng hợp — So sánh tính năng sản phẩm)"
    })

    return items
