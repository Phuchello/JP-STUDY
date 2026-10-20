# -*- coding: utf-8 -*-
"""
JLPT N2 Mock Exam #06 - Section 1: Language Knowledge & Reading (言語知識・読解)
Blueprint (75 items / 105 minutes):
  - Mondai 1: 漢字読み (5 items) [Q1 - Q5]
  - Mondai 2: 表記 (5 items) [Q6 - Q10]
  - Mondai 3: 語形成 (5 items) [Q11 - Q15]
  - Mondai 4: 文脈規定 (7 items) [Q16 - Q22]
  - Mondai 5: 言い換え類義 (5 items) [Q23 - Q27]
  - Mondai 6: 用法 (5 items) [Q28 - Q32]
  - Mondai 7: 文法形式の判断 (12 items) [Q33 - Q44]
  - Mondai 8: 文の組み立て ★ (5 items) [Q45 - Q49] (Mathematically verified 4! = 24 permutations)
  - Mondai 9: 文章の文法 (5 items) [Q50 - Q54]
  - Mondai 10: 短文読解 (5 items) [Q55 - Q59]
  - Mondai 11: 中文読解 (9 items) [Q60 - Q68] (3 passages x 3 items)
  - Mondai 12: 統合理解 (2 items) [Q69 - Q70] (2 passages x 1 comparative pair)
  - Mondai 13: 長文読解 (3 items) [Q71 - Q73]
  - Mondai 14: 情報検索 (2 items) [Q74 - Q75]

Total Section 1: exactly 75 items.
Answer Key Target Distribution: ~18-20 each across A, B, C, D.
"""

def get_n2_mock_06_sec1_items():
    items = []

    # =========================================================================
    # MONDAI 1: 漢字読み (Kanji Reading - 5 items)
    # =========================================================================
    m1_raw = [
        (
            "N2_06_M1_01", "N2-MO-READ", "Mondai 1: 漢字読み",
            "気体の温度が上昇すると、体積が急速に【膨張】する。",
            "ぼうちょう",
            [("A", "ぼうちょう"), ("B", "ほうちょう"), ("C", "ぼうちゅう"), ("D", "ぼんちょう")],
            "A",
            "膨張（ぼうちょう - BÀNH TRƯƠNG）: Sự giãn nở, phình to ra về thể tích do áp suất hoặc nhiệt độ. Chữ 膨 có âm on là ぼう, chữ 張 có âm on là ちょう.",
            {
                "B": "ほうちょう: Sai âm đục ぼう thành âm thanh ほう (nhầm với 包丁 - con dao bếp).",
                "C": "ぼうちゅう: Sai âm ちょう thành ちゅう.",
                "D": "ぼんちょう: Sai âm ぼう thành âm ngắt ぼん."
            }
        ),
        (
            "N2_06_M1_02", "N2-MO-READ", "Mondai 1: 漢字読み",
            "著者の長年の研究成果が、この一冊の学術書に【凝縮】されている。",
            "ぎょうしゅく",
            [("A", "こうしゅく"), ("B", "ぎょうしゅく"), ("C", "きょうしゅく"), ("D", "ぎょうしょう")],
            "B",
            "凝縮（ぎょうしゅく - NGƯNG SÚC）: Sự ngưng tụ vật lý hoặc cô đọng, đúc kết tinh hoa kiến thức. Chữ 凝 có âm on là ぎょう, chữ 縮 có âm on là しゅく.",
            {
                "A": "こうしゅく: Sai âm ぎょう thành こう.",
                "C": "きょうしゅく: Nhầm sang 恐縮 (きょうしゅく - áy náy, làm phiền).",
                "D": "ぎょうしょう: Sai âm しゅく thành しょう."
            }
        ),
        (
            "N2_06_M1_03", "N2-MO-READ", "Mondai 1: 漢字読み",
            "相手企業の提案条件を検討した結果、正式に【承諾】の返答を送った。",
            "しょうだく",
            [("A", "じょうだく"), ("B", "しょうちょく"), ("C", "しょうだく"), ("D", "しょうしゃく")],
            "C",
            "承諾（しょうだく - THỪA NẶC）: Chấp thuận, đồng ý tiếp nhận lời yêu cầu/đề nghị. Chữ 承 có âm on là しょう, chữ 諾 có âm on là だく.",
            {
                "A": "じょうだく: Sai âm thanh しょう thành âm đục じょう.",
                "B": "しょうちょく: Sai âm だく thành ちょく.",
                "D": "しょうしゃく: Sai âm だく thành しゃく."
            }
        ),
        (
            "N2_06_M1_04", "N2-MO-READ", "Mondai 1: 漢字読み",
            "ウイルス感染の拡大を防ぐため、蚊が病原体を【媒介】する経路を調査している。",
            "ばいかい",
            [("A", "まいかい"), ("B", "ばいけい"), ("C", "はいかい"), ("D", "ばいかい")],
            "D",
            "媒介（ばいかい - MÔI GIỚI）: Làm vật trung gian truyền dẫn, truyền bệnh (như muỗi truyền mầm bệnh). Chữ 媒 có âm on là ばい, chữ 介 có âm on là かい.",
            {
                "A": "まいかい: Sai âm ばい thành まい.",
                "B": "ばいけい: Sai âm かい thành けい.",
                "C": "はいかい: Sai âm đục ばい thành âm thanh はい (nhầm sang 徘徊 - đi lang thang)."
            }
        ),
        (
            "N2_06_M1_05", "N2-MO-READ", "Mondai 1: 漢字読み",
            "市民団体は、不正な資金流用を行った市長の責任を厳しく【糾弾】した。",
            "きゅうだん",
            [("A", "きゅうだん"), ("B", "きょうだん"), ("C", "きゅうたん"), ("D", "こうだん")],
            "A",
            "糾弾（きゅうだん - CỦ ĐẠN）: Lên án, chất vấn và truy cứu trách nhiệm tội lỗi một cách gay gắt. Chữ 糾 có âm on là きゅう, chữ 弾 có âm on là だん.",
            {
                "B": "きょうだん: Sai âm きゅう thành きょう (nhầm sang 教壇 - bục giảng).",
                "C": "きゅうたん: Sai âm đục だん thành âm thanh たん.",
                "D": "こうだん: Sai âm きゅう thành こう (nhầm sang 講談)."
            }
        ),
    ]

    for qid, tid, cat, stem, word, opts, ans, exp, dist in m1_raw:
        items.append({
            "id": qid, "typeId": tid, "skill": "Language Knowledge", "category": cat,
            "stem": stem, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 2: 表記 (Orthography - 5 items)
    # =========================================================================
    m2_raw = [
        (
            "N2_06_M2_01", "N2-MO-READ", "Mondai 2: 表記",
            "彼は複雑な人形を指先で巧みに【あやつる】名人として知られている。",
            "操る",
            [("A", "操る"), ("B", "握る"), ("C", "扱る"), ("D", "捕る")],
            "A",
            "操る（あやつる - THAO）: Điều khiển, vận hành thuần thục (con rối, máy móc, ngoại ngữ). Chữ Hán chuẩn xác là 操 (trong 操作, 操縦).",
            {
                "B": "握る: Đọc là にぎる (nắm chặt, cầm lấy), sai nghĩa và âm đọc.",
                "C": "扱る: Chữ 扱 thường đi trong động từ 扱う (あつかう - đối xử, xử lý), không có dạng あやつる.",
                "D": "捕る: Đọc là とる (bắt, tóm được con mồi)."
            }
        ),
        (
            "N2_06_M2_02", "N2-MO-READ", "Mondai 2: 表記",
            "最新の科学技術を【たずさえて】、未知の海洋深層部の探査へと出発した。",
            "携えて",
            [("A", "揃えて"), ("B", "携えて"), ("C", "導えて"), ("D", "抱えて")],
            "B",
            "携える（たずさえる - HUỀ）: Mang theo bên mình, cầm trong tay (vật phẩm, tri thức, công nghệ). Chữ Hán chuẩn là 携 (trong 携帯, 連携).",
            {
                "A": "揃えて: Đọc là そろえて (gom đủ, sắp xếp chỉnh tề).",
                "C": "導えて: Chữ 導 đi trong 導く (みちびく - hướng dẫn, dẫn lối), không đọc là たずさえる.",
                "D": "抱えて: Đọc là かかえて (ôm, gánh vác món nợ/vấn đề khó khăn)."
            }
        ),
        (
            "N2_06_M2_03", "N2-MO-READ", "Mondai 2: 表記",
            "若き研究者たちが、難病の治療法を見つけるために日夜研究に【はげんでいる】。",
            "励んでいる",
            [("A", "努んでいる"), ("B", "奮んでいる"), ("C", "励んでいる"), ("D", "勤んでいる")],
            "C",
            "励む（はげむ - LỆ）: Nỗ lực hết mình, dồn sức vào công việc/học tập. Chữ Hán chuẩn là 励 (trong 激励, 勉励).",
            {
                "A": "努んでいる: Chữ 努 đi trong 努める (つとめる - cố gắng).",
                "B": "奮んでいる: Chữ 奮 đi trong 奮う (ふるう - phấn khởi, vung cờ).",
                "D": "勤んでいる: Chữ 勤 đi trong 勤める (つとめる - làm việc ở công ty)."
            }
        ),
        (
            "N2_06_M2_04", "N2-MO-READ", "Mondai 2: 表記",
            "過度な規制は、自由な経済活動の発展を【さまたげる】要因になりかねない。",
            "妨げる",
            [("A", "阻げる"), ("B", "遮げる"), ("C", "拒げる"), ("D", "妨げる")],
            "D",
            "妨げる（さまたげる - PHƯƠNG）: Gây trở ngại, ngăn cản sự tiến bộ/phát triển. Chữ Hán chuẩn là 妨 (trong 妨害).",
            {
                "A": "阻げる: Chữ 阻 đi trong 阻む (はばむ - ngăn cản), không có cách đọc さまたげる.",
                "B": "遮げる: Đọc là さえぎる (chắn ngang tầm mắt, cắt ngang lời nói: 視界を遮る).",
                "C": "拒げる: Chữ 拒 đi trong 拒む (こばむ - từ chối, cự tuyệt)."
            }
        ),
        (
            "N2_06_M2_05", "N2-MO-READ", "Mondai 2: 表記",
            "政府は省エネルギー住宅の普及を【うながす】ため、補助金制度の新設を決定した。",
            "促す",
            [("A", "促す"), ("B", "催す"), ("C", "勧す"), ("D", "薦す")],
            "A",
            "促す（うながす - XÚC）: Thúc đẩy, khích lệ tiến hành nhanh hoặc nhắc nhở hành động. Chữ Hán chuẩn là 促 (trong 促進, 催促).",
            {
                "B": "催す: Đọc là もよおす (tổ chức lễ hội / có triệu chứng buồn ngủ).",
                "C": "勧す: Viết sai chữ 勧める (すすめる - khuyên bảo).",
                "D": "薦す: Viết sai chữ 薦める (すすめる - tiến cử, giới thiệu)."
            }
        ),
    ]

    for qid, tid, cat, stem, word, opts, ans, exp, dist in m2_raw:
        items.append({
            "id": qid, "typeId": tid, "skill": "Language Knowledge", "category": cat,
            "stem": stem, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 3: 語形成 (Word Formation - 5 items)
    # =========================================================================
    m3_raw = [
        (
            "N2_06_M3_01", "N2-MO-FORM", "Mondai 3: 語形成",
            "近年のデジタル技術革新により、金融とITが融合した新たな経済（　　）が誕生した。",
            "圏",
            [("A", "界"), ("B", "圏"), ("C", "帯"), ("D", "区")],
            "B",
            "経済圏（けいざいけん）: Vùng kinh tế, hệ sinh thái kinh tế có mối liên kết chặt chẽ (hậu tố 〜圏 chỉ phạm vi/khu vực ảnh hưởng: 首都圏, 経済圏).",
            {
                "A": "界: Thường dùng chỉ giới/ngành nghề (như 経済界, 芸能界), không ghép thành cụm 'kinh tế số tạo ra kinh giới'.",
                "C": "帯: Thường dùng chỉ dải/vành đai địa lý (như 火山帯, 時間帯).",
                "D": "区: Chỉ phân khu hành chính địa phương (như 住宅区, 特別区)."
            }
        ),
        (
            "N2_06_M3_02", "N2-MO-FORM", "Mondai 3: 語形成",
            "緊急事態に対処するため、警察と消防の全戦力が（　　）動員された。",
            "総",
            [("A", "大"), ("B", "全"), ("C", "総"), ("D", "本")],
            "C",
            "総動員（そうどういん）: Tổng động viên toàn bộ nhân lực và lực lượng (tiền tố 総〜 chỉ quy mô tập hợp tất cả: 総動員, 総責任者, 総売上).",
            {
                "A": "大: Ghép thành 大動員 là cách kết hợp không tự nhiên trong tiếng Nhật chuẩn.",
                "B": "全: Thường dùng trong 全力, 全体, 全員, nhưng danh từ huy động lực lượng chuẩn là 総動員.",
                "D": "本: Thường chỉ bản thân/chính thức (như 本会議, 本部)."
            }
        ),
        (
            "N2_06_M3_03", "N2-MO-FORM", "Mondai 3: 語形成",
            "地元住民が行政と連携し、地域（　　）で高齢者の見守り活動に取り組んでいる。",
            "ぐるみ",
            [("A", "ぐるみ"), ("B", "だらけ"), ("C", "ずくめ"), ("D", "まみれ")],
            "A",
            "地域ぐるみ（ちいきぐるみ）: Quy mô toàn thể khu vực, tất cả mọi người trong vùng đều chung tay tham gia (hậu tố 〜ぐるみ: 町ぐるみ, 地域ぐるみ, 家族ぐるみ).",
            {
                "B": "だらけ: Đầy rẫy những thứ tiêu cực (như ゴミだらけ, 泥だらけ).",
                "C": "ずくめ: Toàn là điều gì đó (thường dùng trong 良いことずくめ, 黒ずくめ).",
                "D": "まみれ: Dính nhớp nháp trên bề mặt (như 血まみれ, 汗まみれ)."
            }
        ),
        (
            "N2_06_M3_04", "N2-MO-FORM", "Mondai 3: 語形成",
            "他業種との交流を通じて、従来の枠組みにとらわれない（　　）分野の融合を図る。",
            "異",
            [("A", "他"), ("B", "外"), ("C", "対"), ("D", "異")],
            "D",
            "異分野（いぶんや）: Các lĩnh vực khác biệt, không cùng chuyên môn (tiền tố 異〜: 異分野, 異業種, 異文化).",
            {
                "A": "他: Thường dùng trong 他社, 他人, 他国, nhưng khi chỉ lĩnh vực khác biệt ghép đôi chuyên ngành người ta dùng 異分野.",
                "B": "外: Dùng chỉ bên ngoài (như 外国, 社外).",
                "C": "対: Dùng chỉ đối kháng/đối xứng (như 対外, 対立)."
            }
        ),
        (
            "N2_06_M3_05", "N2-MO-FORM", "Mondai 3: 語形成",
            "休日の朝は、潮風を感じながら海岸（　　）をジョギングするのが日課だ。",
            "沿い",
            [("A", "沿い"), ("B", "端"), ("C", "側"), ("D", "並び")],
            "A",
            "海岸沿い（かいがんぞい）: Dọc theo bờ biển (hậu tố 〜沿い chỉ vị trí chạy men theo tuyến đường/bờ sông/bờ biển: 海岸沿い, 川沿い, 線路沿い).",
            {
                "B": "端: Đọc là はし (mép, rìa), không tạo cụm vị trí ven bờ chạy dài.",
                "C": "側: Đọc là がわ (phía bên: 海側, 窓側).",
                "D": "並び: Đọc là ならび (dãy nhà xếp kề nhau)."
            }
        ),
    ]

    for qid, tid, cat, stem, word, opts, ans, exp, dist in m3_raw:
        items.append({
            "id": qid, "typeId": tid, "skill": "Language Knowledge", "category": cat,
            "stem": stem, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 4: 文脈規定 (Context Vocabulary - 7 items)
    # =========================================================================
    m4_raw = [
        (
            "N2_06_M4_01", "N2-MO-CTX", "Mondai 4: 文脈規定",
            "論文の要点を手短に説明するため、最も重要な実験結果のデータのみを【　　】して提示した。",
            [("A", "抜粋"), ("B", "省略"), ("C", "縮小"), ("D", "控除")],
            "A",
            "抜粋（ばっすい - BẠT TÚY）: Trích tuyển, rút ra phần quan trọng/tiêu biểu từ văn bản, dữ liệu để trình bày.",
            {
                "B": "省略（しょうりゃく）: Lược bỏ bớt, không mang nghĩa chọn phần tinh túy để đưa ra.",
                "C": "縮小（しゅくしょう）: Thu nhỏ kích thước/quy mô vật lý.",
                "D": "控除（こうじょ）: Khấu trừ tiền bạc/thuế má."
            }
        ),
        (
            "N2_06_M4_02", "N2-MO-CTX", "Mondai 4: 文脈規定",
            "過去の失敗に過度に【　　】していては、新しい挑戦への一歩を踏み出すことはできない。",
            [("A", "依存"), ("B", "執着"), ("C", "束縛"), ("D", "専念")],
            "B",
            "執着（しゅうちゃく - CHẤP TRƯỚC）: Vương vấn, cố chấp bám riết lấy một việc/tình cảm trong quá khứ không chịu buông bỏ.",
            {
                "A": "依存（いぞん）: Phụ thuộc vào người khác hoặc thói quen.",
                "C": "束縛（そくばく）: Trói buộc, hạn chế tự do của ai đó.",
                "D": "専念（せんねん）: Chuyên tâm, cống hiến hết mình cho công việc."
            }
        ),
        (
            "N2_06_M4_03", "N2-MO-CTX", "Mondai 4: 文脈規定",
            "相手の素早い攻撃を【　　】な身のこなしでかわし、見事に反撃に転じた。",
            [("A", "簡潔"), ("B", "鮮明"), ("C", "敏捷"), ("D", "軽率")],
            "C",
            "敏捷（びんしょう - MẪN TIỆP）: Nhanh nhẹn, lanh lẹ trong cử động thân thể hoặc tư duy (thường đi với 敏捷な動き, 敏捷な身のこなし).",
            {
                "A": "簡潔（かんけつ）: Ngắn gọn, súc tích (văn phong).",
                "B": "鮮明（せんめい）: Rõ ràng, sắc nét (hình ảnh, ký ức).",
                "D": "軽率（けいそつ）: Khinh suất, nông nổi."
            }
        ),
        (
            "N2_06_M4_04", "N2-MO-CTX", "Mondai 4: 文脈規定",
            "日々の健康管理を【　　】にしていると、年齢を重ねてから大きな病気につながる恐れがある。",
            [("A", "わずか"), ("B", "かすか"), ("C", "なだらか"), ("D", "おろそか")],
            "D",
            "疎か（おろそか - SƠ）: Chểnh mảng, lơ là, không coi trọng (thường dùng trong 健康管理をおろそかにする, 勉強をおろそかにする).",
            {
                "A": "わずか: Chỉ một lượng nhỏ, ít ỏi (わずかな差).",
                "B": "かすか: Mờ nhạt, thoang thoảng (かすかな声, かすかな光).",
                "C": "なだらか: Thoai thoải, êm ả (なだらかな坂)."
            }
        ),
        (
            "N2_06_M4_05", "N2-MO-CTX", "Mondai 4: 文脈規定",
            "悪天候の平日の午後だったため、普段は賑わう商店街も人通りは【　　】だった。",
            [("A", "まばら"), ("B", "おおまか"), ("C", "ひそか"), ("D", "のどか")],
            "A",
            "まばら: Thưa thớt, rải rác ít ỏi (thường miêu tả mật độ người: 人通りはまばらだ, 観客はまばらだった).",
            {
                "B": "おおまか: Đại khái, sơ lược (おおまかな見積もり).",
                "C": "ひそか: Kín đáo, thầm kín (ひそかに計画する).",
                "D": "のどか: Thanh bình, yên ả nơi đồng quê (のどかな田園風景)."
            }
        ),
        (
            "N2_06_M4_06", "N2-MO-CTX", "Mondai 4: 文脈規定",
            "想定外のアクシデントに見舞われ、新入社員はすっかり【　　】、指示を待つことしかできなかった。",
            [("A", "しがみついて"), ("B", "うろたえて"), ("C", "くつろいで"), ("D", "とまどって")],
            "B",
            "うろたえる: Hoảng hốt, lúng túng mất phương hướng vì bất ngờ trước tai họa/sự cố (すっかりうろたえる).",
            {
                "A": "しがみつく: Bám chặt, níu chặt lấy.",
                "C": "くつろぐ: Thư giãn, nghỉ ngơi thoải mái.",
                "D": "とまどう: Bỡ ngỡ, lúng túng do chưa quen việc (không biểu đạt mức độ hoảng hốt mất bình tĩnh cao như うろたえる trong sự cố bất ngờ)."
            }
        ),
        (
            "N2_06_M4_07", "N2-MO-CTX", "Mondai 4: 文脈規定",
            "意見の対立が続いて以来、二人の関係はどこか【　　】していて口数も減った。",
            [("A", "ぎくしゃく"), ("B", "ごたごた"), ("C", "もたもた"), ("D", "ぐずぐず")],
            "A",
            "ぎくしゃく: Gượng gạo, sượng sùng, căng thẳng mất đi sự ăn ý tự nhiên trong mối quan hệ (二人の関係がぎくしゃくする).",
            {
                "B": "ごたごた: Hỗn loạn, tranh chấp rắc rối (ごたごた揉める).",
                "C": "もたもた: Lề mề, chậm chạp vụng về trong thao tác.",
                "D": "ぐずぐず: Nhùng nhằng, chần chừ không dứt khoát."
            }
        ),
    ]

    for qid, tid, cat, stem, opts, ans, exp, dist in m4_raw:
        items.append({
            "id": qid, "typeId": tid, "skill": "Language Knowledge", "category": cat,
            "stem": stem, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 5: 言い換え類義 (Paraphrases - 5 items)
    # =========================================================================
    m5_raw = [
        (
            "N2_06_M5_01", "N2-MO-PARA", "Mondai 5: 言い換え類義",
            "十分な事前準備をしていたため、交渉は【たやすく】成立した。",
            [("A", "あっさり"), ("B", "かろうじて"), ("C", "すみやかに"), ("D", "あらかじめ")],
            "A",
            "たやすく（容易く）: Dễ dàng, trôi chảy không gặp trở ngại nào = あっさり（chóng vánh, nhẹ nhàng đạt được kết quả mà không tốn công sức đấu tranh）。",
            {
                "B": "かろうじて: Suýt soát, khó khăn lắm mới đạt được.",
                "C": "すみやかに: Nhanh chóng, mau lẹ về mặt thời gian.",
                "D": "あらかじめ: Sẵn từ trước."
            }
        ),
        (
            "N2_06_M5_02", "N2-MO-PARA", "Mondai 5: 言い換え類義",
            "新規事業を立ち上げるにあたり、チーム全員の【意気込み】が感じられた。",
            [("A", "誠意"), ("B", "やる気"), ("C", "自負"), ("D", "警戒")],
            "B",
            "意気込み（いきごみ）: Nhiệt huyết, khí thế hăng hái quyết tâm làm việc = やる気 / 意欲。",
            {
                "A": "誠意（せいい）: Lòng chân thành, thật tâm.",
                "C": "自負（じふ）: Tự hào, kiêu hãnh về năng lực.",
                "D": "警戒（けいかい）: Cảnh giác, đề phòng rủi ro."
            }
        ),
        (
            "N2_06_M5_03", "N2-MO-PARA", "Mondai 5: 言い換え類義",
            "厳しい叱責を受けた後、彼は一言も話さず【うつむいて】いた。",
            [("A", "横を向いて"), ("B", "後ろを向いて"), ("C", "下を向いて"), ("D", "上を向いて")],
            "C",
            "うつむく（俯く）: Cúi gằm mặt xuống vì xấu hổ, ân hận hoặc buồn rầu = 下を向く。",
            {
                "A": "横を向いて: Quay mặt sang ngang.",
                "B": "後ろを向いて: Quay người lại phía sau.",
                "D": "上を向いて: Ngước nhìn lên trên."
            }
        ),
        (
            "N2_06_M5_04", "N2-MO-PARA", "Mondai 5: 言い換え類義",
            "海外赴任に伴う税務手続きは、専門用語が多く非常に【わずらわしい】。",
            [("A", "ばかばかしい"), ("B", "みっともない"), ("C", "まぎらわしい"), ("D", "めんどうな")],
            "D",
            "わずらわしい（煩わしい）: Phiền toái, rườm rà, phức tạp khiến người ta phát ngán = めんどうな / 煩雑な。",
            {
                "A": "ばかばかしい: Ngớ ngẩn, vô nghĩa lố bịch.",
                "B": "みっともない: Khó coi, nhục nhã, bẽ mặt.",
                "C": "まぎらわしい: Nhập nhằng, dễ gây nhầm lẫn."
            }
        ),
        (
            "N2_06_M5_05", "N2-MO-PARA", "Mondai 5: 言い換え類義",
            "明日の会議は書類の確認のみですので、私服で参加されても【さしつかえありません】。",
            [("A", "問題ありません"), ("B", "おすすめしません"), ("C", "遠慮してください"), ("D", "義務づけられています")],
            "A",
            "差し支えない（さしつかえない）: Không có gì cản trở, không sao, hoàn toàn được phép = 問題ない / 構わない。",
            {
                "B": "おすすめしません: Không khuyến khích.",
                "C": "遠慮してください: Xin hãy tránh/đừng làm.",
                "D": "義務づけられています: Bắt buộc phải tuân theo."
            }
        ),
    ]

    for qid, tid, cat, stem, opts, ans, exp, dist in m5_raw:
        items.append({
            "id": qid, "typeId": tid, "skill": "Language Knowledge", "category": cat,
            "stem": stem, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 6: 用法 (Usage - 5 items)
    # =========================================================================
    m6_raw = [
        (
            "N2_06_M6_01", "N2-MO-USE", "Mondai 6: 用法",
            "【模倣】",
            [
                ("A", "優れた芸術作品を観察し、その技法を模倣することから独自の創作が始まる。"),
                ("B", "試験の模倣として過去問を何度も解くことで、本番の感覚に慣れておく。"),
                ("C", "災害発生時に備えて、全社員で避難の模倣を迅速に実施した。"),
                ("D", "新商品の模倣を測るため、街頭で大規模なアンケート調査を行った。")
            ],
            "A",
            "模倣（もほう - MÔ PHỎNG）: Bắt chước, học theo phong cách/hành vi của người khác. Dùng đúng trong A: học tập mô phỏng kỹ thuật của tác phẩm nghệ thuật.",
            {
                "B": "Dùng sai. Luyện tập tương tự bài thi thực tế dùng từ 模擬 (もぎ: 模擬試験).",
                "C": "Dùng sai. Diễn tập phòng chống thiên tai dùng từ 訓練 (くんれん: 避難訓練).",
                "D": "Dùng sai. Đo lường mức độ đón nhận của thị trường dùng từ 評判 / 反響."
            }
        ),
        (
            "N2_06_M6_02", "N2-MO-USE", "Mondai 6: 用法",
            "【蓄積】",
            [
                ("A", "彼は毎月の給料から一定額を銀行口座に蓄積して家を買った。"),
                ("B", "長年の地道な現場実験によって得られたデータと知見の蓄積が、今回の発見を生んだ。"),
                ("C", "昨夜の大雪が道路に激しく蓄積し、朝の通勤ラッシュを麻痺させた。"),
                ("D", "会議で出た意見をノートに蓄積し、後で議事録として清書した。")
            ],
            "B",
            "蓄積（ちくせき - SÚC TÍCH）: Tích lũy dần dần qua thời gian dài (kiến thức, dữ liệu, mệt mỏi, kinh nghiệm). Dùng đúng trong B: tích lũy dữ liệu và hiểu biết.",
            {
                "A": "Dùng sai. Tích lũy tiền bạc trong tài khoản dùng 貯金 / 貯蓄.",
                "C": "Dùng sai. Tuyết đóng đọng dày đặc trên đường dùng 積もる / 堆積.",
                "D": "Dùng sai. Ghi chép thu thập ý kiến dùng 記録 / 整理."
            }
        ),
        (
            "N2_06_M6_03", "N2-MO-USE", "Mondai 6: 用法",
            "【画期的】",
            [
                ("A", "彼女は毎朝時間を画期的に使って、読書と運動の両立を図っている。"),
                ("B", "この画期的な壁画は、地元出身の若手画家によって丁寧に描かれた。"),
                ("C", "従来の治療法の概念を根底から覆す、画期的な新薬が開発された。"),
                ("D", "画期的な天候の急変により、予定されていた屋外コンサートは中止となった。")
            ],
            "C",
            "画期的（かっきてき - HỌA KỲ ĐÍCH）: Mang tính bước ngoặt lịch sử, mở ra kỷ nguyên mới chưa từng có. Dùng đúng trong C: loại thuốc đột phá mang tính thời đại làm đảo lộn quan niệm cũ.",
            {
                "A": "Dùng sai. Sử dụng thời gian hiệu quả dùng 効率的.",
                "B": "Dùng sai. Bức tranh ấn tượng dùng 印象的 / 壮大.",
                "D": "Dùng sai. Thời tiết thay đổi đột ngột dùng 劇的 / 突発的."
            }
        ),
        (
            "N2_06_M6_04", "N2-MO-USE", "Mondai 6: 用法",
            "【妥当】",
            [
                ("A", "市場の平均相場や品質を総合的に考慮すれば、この価格設定は極めて妥当だ。"),
                ("B", "彼は時間に妥当な性格で、一度も待ち合わせに遅刻したことがない。"),
                ("C", "この部屋は日当たりがよく、風通しも妥当なのでとても過ごしやすい。"),
                ("D", "試験で満点を取るという妥当な目標に向かって、毎日猛勉強を続けている。")
            ],
            "A",
            "妥当（だとう - THỎA ĐƯƠNG）: Hợp lý, thỏa đáng, đúng mực sau khi cân nhắc các khía cạnh khách quan. Dùng đúng trong A: mức giá định ra là cực kỳ thỏa đáng.",
            {
                "B": "Dùng sai. Người nghiêm túc về giờ giấc dùng きっちりした / 几帳面な.",
                "C": "Dùng sai. Độ thông thoáng vừa phải/tốt dùng 良好 / 適切.",
                "D": "Dùng sai. Mục tiêu cao vời vợi dùng 困難な / 遠大な."
            }
        ),
        (
            "N2_06_M6_05", "N2-MO-USE", "Mondai 6: 用法",
            "【執拗】",
            [
                ("A", "相手の弱点を見つけると、執拗に同じ論点を突いて攻撃を繰り返した。"),
                ("B", "この料理はスープの味が執拗で、一口食べただけで濃厚な旨味が広がる。"),
                ("C", "彼女は執拗な性格で、困っている人を見ると放っておけない優しさがある。"),
                ("D", "最新のスマートフォンの画面は執拗に美しく、細部まで鮮やかに映し出される。")
            ],
            "A",
            "執拗（しつよう - CHẤP ẤU）: Dai dẳng, ngoan cố bám riết lấy một cách dai như đỉa (thường mang sắc thái tiêu cực hoặc quấy rối). Dùng đúng trong A: công kích dai dẳng lặp đi lặp lại vào cùng một điểm yếu.",
            {
                "B": "Dùng sai. Vị nước dùng đậm đà dùng 濃厚 / こってり.",
                "C": "Dùng sai. Tấm lòng nhân hậu, chu đáo dùng 親切 / 几帳面.",
                "D": "Dùng sai. Màn hình đẹp vô cùng dùng 圧倒的 / 驚くほど."
            }
        ),
    ]

    for qid, tid, cat, stem, opts, ans, exp, dist in m6_raw:
        items.append({
            "id": qid, "typeId": tid, "skill": "Language Knowledge", "category": cat,
            "stem": stem, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 7: 文法形式の判断 (Grammar Forms - 12 items)
    # =========================================================================
    m7_raw = [
        (
            "N2_06_M7_01", "N2-GR-FORM", "Mondai 7: 文法形式の判断",
            "過去の失敗の経験（　　）、今回の新しいプロジェクトではリスク管理を徹底した。",
            [("A", "を皮切りに"), ("B", "を踏まえて"), ("C", "を抜きにして"), ("D", "を契機に")],
            "B",
            "〜を踏まえて: Dựa trên cơ sở/tiền đề, rút kinh nghiệm từ N (văn viết trang trọng: 過去の経験を踏まえて - dựa trên bài học thất bại trong quá khứ).",
            {
                "A": "〜を皮切りに: Bắt đầu với phát súng đầu tiên, theo sau là hàng loạt sự kiện tương tự dồn dập.",
                "C": "〜を抜きにして: Nếu không có N thì không thể (mang ý nghĩa thiếu vắng).",
                "D": "〜を契機に: Lấy làm cột mốc bước ngoặt lịch sử mở ra thay đổi mới (không mang nghĩa lấy bài học làm tiền đề vững chắc như 踏まえて)."
            }
        ),
        (
            "N2_06_M7_02", "N2-GR-FORM", "Mondai 7: 文法形式の判断",
            "来月に控えた新製品の全国発売（　　）、関係者を集めた大規模な記者会見が開催された。",
            [("A", "に先立ち"), ("B", "に基づいて"), ("C", "に応じて"), ("D", "に伴い")],
            "A",
            "〜に先立ち / 〜に先立って: Trước khi bước vào sự kiện lớn/dự án quan trọng (chuẩn bị trước: 発売に先立ち - trước khi tung sản phẩm ra toàn quốc vào tháng tới thì họp báo trước).",
            {
                "B": "〜に基づいて: Dựa trên căn cứ pháp luật/dữ liệu chuẩn.",
                "C": "〜に応じて: Phù hợp với, tùy theo (không mang nghĩa thời gian chuẩn bị trước sự kiện).",
                "D": "〜に伴い: Cùng với sự thay đổi của vế trước dẫn đến thay đổi ở vế sau."
            }
        ),
        (
            "N2_06_M7_03", "N2-GR-FORM", "Mondai 7: 文法形式の判断",
            "連日の猛特訓に耐え抜いた彼のことだから、明日の本番でも実力を発揮する（　　）。",
            [("A", "にすぎない"), ("B", "に相違ない"), ("C", "にほかならない"), ("D", "わけがない")],
            "B",
            "〜に相違ない: Chắc chắn là, không còn nghi ngờ gì nữa (phán đoán quả quyết dựa trên căn cứ vững chắc: 彼のことだから...発揮するに相違ない).",
            {
                "A": "〜にすぎない: Chỉ là... không hơn không kém (hạ thấp mức độ).",
                "C": "〜にほかならない: Chính là, không gì khác ngoài (giải thích bản chất/nguyên nhân duy nhất).",
                "D": "〜わけがない: Tuyệt đối không có lý nào (nghi ngờ phủ định hoàn toàn)."
            }
        ),
        (
            "N2_06_M7_04", "N2-GR-FORM", "Mondai 7: 文法形式の判断",
            "会社の経営方針が大きく転換した以上、我々現場の社員も変革を受け入れ（　　）。",
            [("A", "ざるを得ない"), ("B", "かねない"), ("C", "っこない"), ("D", "そうにない")],
            "A",
            "〜ざるを得ない: Đành phải, buộc phải làm dù không muốn do hoàn cảnh ép buộc (V-nai bỏ nai + ざるを得ない: 受け入れざるを得ない).",
            {
                "B": "〜かねない: Có nguy cơ dẫn tới kết quả tiêu cực.",
                "C": "〜っこない: Tuyệt đối không thể nào làm được.",
                "D": "〜そうにない: Không có vẻ gì là sẽ xảy ra."
            }
        ),
        (
            "N2_06_M7_05", "N2-GR-FORM", "Mondai 7: 文法形式の判断",
            "彼がこれほどの成功を収めたのは、人知れず流した汗と努力の（　　）。",
            [("A", "おそれがある"), ("B", "たまものだ"), ("C", "かぎりだ"), ("D", "ものがある")],
            "B",
            "〜賜物だ（たまものだ）: Chính là kết tinh, hoa trái thành quả của những nỗ lực quý giá (努力の賜物だ).",
            {
                "A": "〜おそれがある: E rằng có nguy cơ xảy ra rủi ro.",
                "C": "〜かぎりだ: Cực kỳ, hết sức (chỉ cảm xúc tột cùng: 嬉しいかぎりだ).",
                "D": "〜ものがある: Có cảm giác rất... (đánh giá sâu sắc: 感慨深いものがある)."
            }
        ),
        (
            "N2_06_M7_06", "N2-GR-FORM", "Mondai 7: 文法形式の判断",
            "子供は母親の顔をどこか（　　）に見つめながら、小さな声で嘘をついたことを謝った。",
            [("A", "不安げ"), ("B", "不安ぎみ"), ("C", "不安がち"), ("D", "不安っぽく")],
            "A",
            "〜げ: Có vẻ, toát lên sắc thái cảm xúc từ ánh mắt/vẻ mặt (tính từ bỏ な/い + げ: 不安げに見つめる - nhìn với ánh mắt đượm vẻ bất an lo lắng).",
            {
                "B": "〜ぎみ: Có triệu chứng nhẹ về thể chất (風邪ぎみ, 疲れぎみ).",
                "C": "〜がち: Hay bị, có khuynh hướng tiêu cực xảy ra thường xuyên (留守がち, 病気がち).",
                "D": "〜っぽく: Có tính chất, hay (怒りっぽい, 忘れっぽい)."
            }
        ),
        (
            "N2_06_M7_07", "N2-GR-FORM", "Mondai 7: 文法形式の判断",
            "台風による土砂崩れの影響で、一部の鉄道区間では終日運休を（　　）。",
            [("A", "余儀なくされた"), ("B", "やむを得なかった"), ("C", "余儀なくさせた"), ("D", "免れなかった")],
            "A",
            "〜を余儀なくされる: Bị buộc phải rơi vào tình trạng bất đắc dĩ do thiên tai, ngoại cảnh tác động (運休を余儀なくされた). Thể bị động biểu thị phía đường sắt/hành khách phải gánh chịu.",
            {
                "B": "〜やむを得なかった: Đi với động từ thể từ điển hoặc câu độc lập, không dùng cấu trúc tân ngữ trực tiếp [N + をやむを得ない].",
                "C": "〜余儀なくさせた: Thể sai khiến chủ động (khiến cho phải...), sai chủ ngữ vì câu đang là [鉄道区間では...運休を余儀なくされた].",
                "D": "〜免れなかった: Không tránh khỏi (chỉ trách nhiệm/phạt: 責任を免れない)."
            }
        ),
        (
            "N2_06_M7_08", "N2-GR-FORM", "Mondai 7: 文法形式の判断",
            "「こんなに複雑な機械の修理、素人の僕たちにはでき（　　）よ。」",
            [("A", "っこない"), ("B", "かねない"), ("C", "がたい"), ("D", "ざるを得ない")],
            "A",
            "〜っこない: Tuyệt đối không thể nào... Cấu trúc N2 chuẩn kết hợp với V-masu (でき＋っこない) trong văn giao tiếp thân mật, biểu đạt sự quả quyết dứt khoát không thể xảy ra (できっこないよ = đời nào dân nghiệp dư chúng mình lại sửa nổi chiếc máy phức tạp thế này).",
            {
                "B": "〜かねない: Có nguy cơ/e rằng sẽ dẫn đến kết quả xấu (事故が起きかねない). Mang nghĩa có khả năng xảy ra điều tiêu cực, không dùng để phủ định hoàn toàn khả năng như っこない.",
                "C": "〜がたい: Khó lòng... Kết hợp với động từ mang tính tâm lý, nhận thức (信じがたい, 理解しがたい, 許しがたい) để biểu thị sự khó khăn về mặt cảm xúc/tinh thần. Không kết hợp với động từ khả năng できる (*できがたい) để chỉ sự bất lực về mặt kỹ thuật/thực tế.",
                "D": "〜ざるを得ない: Buộc phải làm gì (không có sự lựa chọn khác). Cấu trúc kết hợp với thể V-nai bỏ nai (行かざるを得ない; する -> せざるを得ない), không kết hợp với động từ khả năng (không tồn tại *できざるを得ない). Ngoài ra mang ý nghĩa bắt buộc phải làm, trái ngược hoàn toàn với ngữ cảnh không thể sửa nổi của người nghiệp dư."
            }
        ),
        (
            "N2_06_M7_09", "N2-GR-FORM", "Mondai 7: 文法形式の判断",
            "事前に十分な説明を受けた（　　）、実際に契約書にサインする時は緊張した。",
            [("A", "ものの"), ("B", "ものなら"), ("C", "ものの見事に"), ("D", "ものだから")],
            "A",
            "〜ものの: Mặc dù... nhưng sự thực là (vế sau diễn tả thực tế trái với kỳ vọng thông thường: 説明を受けたものの - dù đã được giải thích kỹ rồi nhưng lúc ký vẫn run).",
            {
                "B": "〜ものなら: Nếu lỡ làm gì (hậu quả khôn lường) hoặc giả định khó thành.",
                "C": "ものの見事に: Thành ngữ chỉ sự thất bại hoàn toàn.",
                "D": "〜ものだから: Bởi vì (biện bạch lý do khách quan cá nhân)."
            }
        ),
        (
            "N2_06_M7_10", "N2-GR-FORM", "Mondai 7: 文法形式の判断",
            "新店舗の開店（　　）、地域の皆様へ感謝の気持ちを込めて記念品を贈呈いたします。",
            [("A", "にあたり"), ("B", "を皮切りに"), ("C", "を踏まえ"), ("D", "のもとに")],
            "A",
            "〜にあたって / 〜にあたり: Nhân dịp, vào thời điểm bắt đầu sự kiện trọng đại đặc biệt (開店にあたり - nhân dịp khai trương cửa hàng mới).",
            {
                "B": "〜を皮切りに: Khởi đầu bằng một chuỗi mở màn liên tiếp.",
                "C": "〜を踏まえ: Dựa trên bài học kinh nghiệm.",
                "D": "〜のもとに: Dưới sự bảo trợ/ảnh hưởng của ai đó (指導のもとに)."
            }
        ),
        (
            "N2_06_M7_11", "N2-GR-FORM", "Mondai 7: 文法形式の判断",
            "一度失敗したからといって、夢を諦めてなる（　　）か。",
            [("A", "もの"), ("B", "こと"), ("C", "わけ"), ("D", "はず")],
            "A",
            "〜てなるものか / 〜ものか: Tuyệt đối không bao giờ chịu nhượng bộ/đầu hàng (諦めてなるものか - đời nào lại bỏ cuộc chỉ vì một lần thất bại).",
            {
                "B": "〜ことか: Thật là biết bao (cảm thán: どんなに喜んだことか).",
                "C": "〜わけか: Câu hỏi xác nhận nguyên nhân.",
                "D": "〜はずか: Cấu trúc hỏi tính logic nhưng không tạo thành ngữ khí quyết tâm như てなるものか."
            }
        ),
        (
            "N2_06_M7_12", "N2-GR-FORM", "Mondai 7: 文法形式の判断",
            "家族旅行で訪れた海の写真を見る（　　）、幼い頃の懐かしい思い出が胸に蘇る。",
            [("A", "につけ"), ("B", "につれて"), ("C", "にしたがって"), ("D", "に際して")],
            "A",
            "〜につけ: Mỗi lần... lại nảy sinh cảm xúc/ký ức tự nhiên (見るにつけ - hễ nhìn tấm ảnh lại nhớ về kỷ niệm tuổi thơ).",
            {
                "B": "〜につれて: Kéo theo sự thay đổi về lượng theo tỉ lệ thuận.",
                "C": "〜にしたがって: Đi kèm sự biến đổi tuần tự theo thời gian/quy trình.",
                "D": "〜に際して: Vào thời điểm bắt đầu trang trọng."
            }
        ),
    ]

    for qid, tid, cat, stem, opts, ans, exp, dist in m7_raw:
        items.append({
            "id": qid, "typeId": tid, "skill": "Language Knowledge", "category": cat,
            "stem": stem, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 8: 文の組み立て ★ (Star Sentence Composition - 5 items)
    # Strict permutation mathematical verification (4! = 24 sequences tested)
    # =========================================================================
    m8_raw = [
        (
            "N2_06_M8_01", "N2-GR-STAR", "Mondai 8: 文の組み立て ★",
            "定年退職を（　　）（　　） ★ （　　）ことにした。",
            [
                ("A", "機に、"),
                ("B", "念願だった"),
                ("C", "かねてから"),
                ("D", "陶芸を始める")
            ],
            "B",
            "Thứ tự đúng: A - C - B - D (定年退職を 機に、 かねてから 念願だった 陶芸を始める ことにした). Cấu trúc ngữ pháp N2: 〜を機に (nhân cơ hội...). [A 機に、] kết hợp sau 定年退職を. Vế sau: [C かねてから] bổ nghĩa cho [B 念願だった] (niềm mong mỏi từ lâu), sau đó làm định ngữ bổ nghĩa cho [D 陶芸を始める] trước [ことにした]. Thứ tự duy nhất hợp cú pháp là A - C - B - D. Vị trí ngôi sao ★ là B (念願だった).",
            {
                "A": "A (機に、) đứng ở vị trí thứ nhất đi liền sau 定年退職を.",
                "C": "C (かねてから) đứng ở vị trí thứ hai sau dấu phẩy ngắt vế.",
                "D": "D (陶芸を始める) đứng ở vị trí thứ tư trước ことにした."
            }
        ),
        (
            "N2_06_M8_02", "N2-GR-STAR", "Mondai 8: 文の組み立て ★",
            "本場の職人が（　　）（　　） ★ （　　）格別だ。",
            [
                ("A", "手作りした"),
                ("B", "だけあって、"),
                ("C", "風味の良さは"),
                ("D", "このパンの")
            ],
            "D",
            "Thứ tự đúng: A - B - D - C (本場の職人が 手作りした だけあって、 このパンの 風味の良さは 格別だ). Cấu trúc ngữ pháp N2: 〜だけあって (thảo nào/quả đúng là... nên kết quả nổi bật tương xứng). [A 手作りした] kết hợp sau chủ ngữ 本場の職人が để hoàn thiện vế bổ nghĩa cho [B だけあって、]. Vế sau: [D このパンの] làm định ngữ cho [C 風味の良さは] trước vị ngữ [格別だ]. Thứ tự duy nhất hợp cú pháp là A - B - D - C. Vị trí ngôi sao ★ là D (このパンの).",
            {
                "A": "A (手作りした) đứng ở vị trí thứ nhất sau 本場の職人が.",
                "B": "B (だけあって、) đứng ở vị trí thứ hai ngắt vế điều kiện tương xứng.",
                "C": "C (風味の良さは) đứng ở vị trí thứ tư liền trước 格別だ."
            }
        ),
        (
            "N2_06_M8_03", "N2-GR-STAR", "Mondai 8: 文の組み立て ★",
            "関係者との（　　）（　　） ★ （　　）いかない。",
            [
                ("A", "計画を勝手に"),
                ("B", "進めるわけには"),
                ("C", "十分な合意を"),
                ("D", "得ることなしに、")
            ],
            "A",
            "Thứ tự đúng: C - D - A - B (関係者との 十分な合意を 得ることなしに、 計画を勝手に 進めるわけには いかない). Cấu trúc ngữ pháp N2: 〜ことなしに (nếu không có A thì không thể B) và 〜わけにはいかない (không thể/không được phép làm vì đạo lý/trách nhiệm). [C 十分な合意を] làm tân ngữ cho [D 得ることなしに、]. Vế sau: [A 計画を勝手に] là hành động bị phủ định đi liền với [B 進めるわけには] trước [いかない]. Thứ tự duy nhất hợp lý là C - D - A - B. Vị trí ngôi sao ★ là A (計画を勝手に).",
            {
                "B": "B (進めるわけには) đứng ở vị trí thứ tư đi với いかない.",
                "C": "C (十分な合意を) đứng ở vị trí thứ nhất làm tân ngữ cho 得る.",
                "D": "D (得ることなしに、) đứng ở vị trí thứ hai kết nối điều kiện phủ định."
            }
        ),
        (
            "N2_06_M8_04", "N2-GR-STAR", "Mondai 8: 文の組み立て ★",
            "年齢や性別の（　　）（　　） ★ （　　）努めている。",
            [
                ("A", "社内において"),
                ("B", "誰もが働きやすい"),
                ("C", "違いにかかわらず、"),
                ("D", "環境を整えるよう")
            ],
            "B",
            "Thứ tự đúng: C - A - B - D (年齢や性別の 違いにかかわらず、 社内において 誰もが働きやすい 環境を整えるよう 努めている). Cấu trúc ngữ pháp N2: 〜にかかわらず (bất kể, không phân biệt). [C 違いにかかわらず、] đi liền sau danh từ 年齢や性別の. Vế sau: [A 社内において] xác định phạm vi, [B 誰もが働きやすい] bổ nghĩa cho [D 環境を整えるよう] trước [努めている]. Thứ tự duy nhất chuẩn xác là C - A - B - D. Vị trí ngôi sao ★ là B (誰もが働きやすい).",
            {
                "A": "A (社内において) đứng ở vị trí thứ hai xác định phạm vi thực hiện.",
                "C": "C (違いにかかわらず、) đứng ở vị trí thứ nhất ngắt vế không phân biệt.",
                "D": "D (環境を整えるよう) đứng ở vị trí thứ tư đi liền trước 努めている."
            }
        ),
        (
            "N2_06_M8_05", "N2-GR-STAR", "Mondai 8: 文の組み立て ★",
            "彼の失言は（　　）（　　） ★ （　　）招きかねない。",
            [
                ("A", "批判を浴びる"),
                ("B", "国際問題さえ"),
                ("C", "どころか、"),
                ("D", "国内での")
            ],
            "C",
            "Thứ tự đúng: D - A - C - B (彼の失言は 国内での 批判を浴びる どころか、 国際問題さえ 招きかねない). Cấu trúc ngữ pháp N2: 〜どころか...さえ〜 (không chỉ A mà thậm chí đến cả B mức độ nghiêm trọng hơn cũng có thể xảy ra). [D 国内での] bổ nghĩa cho [A 批判を浴びる]. [C どころか、] ngắt vế so sánh tăng cấp. [B 国際問題さえ] làm tân ngữ mức độ cao đi với [招きかねない]. Thứ tự duy nhất hợp logic là D - A - C - B. Vị trí ngôi sao ★ là C (どころか、).",
            {
                "A": "A (批判を浴びる) đứng ở vị trí thứ hai làm định ngữ.",
                "B": "B (国際問題さえ) đứng ở vị trí thứ tư trước vị ngữ 招きかねない.",
                "D": "D (国内での) đứng ở vị trí thứ nhất xác định phạm vi."
            }
        ),
    ]

    for qid, tid, cat, stem, opts, ans, exp, dist in m8_raw:
        items.append({
            "id": qid, "typeId": tid, "skill": "Language Knowledge", "category": cat,
            "stem": stem, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 9: 文章の文法 (Text Grammar - 5 items)
    # Organic passage on the psychological mechanisms of procrastination
    # =========================================================================
    m9_passage = (
        "【問題9】次の文章を読んで、文章全体の趣旨を踏まえて、【50】から【54】の中に入る最もよいものを一つ選びなさい。\n\n"
        "多くの人が「やらなければならないと分かっているのに、つい先延ばしにしてしまう」という経験を持っているだろう。"
        "かつて先延ばしは単なる怠惰や意志の弱さの表れだと考えられていたが、近年の行動心理学の研究によって、"
        "それが脳の自己防衛反応の一種であることが【 50 】。\n\n"
        "脳は本能的に、大きな負担や失敗への恐れを「脅威」として感知する。難解な課題や期限の迫った仕事に直面した際、"
        "不快なストレスから逃れようと一時的な安心感を求める【 51 】、手軽な快楽をもたらすスマートフォンの閲覧などに"
        "逃避してしまうのである。つまり、先延ばしは時間管理の失敗ではなく、感情の制御をめぐる葛藤に【 52 】。\n\n"
        "では、この心理的メカニズムにどう対処すべきなのだろうか。専門家が推奨するのは、「課題を極限まで小さく分解する」ことだ。"
        "最初の一歩を「机の上にノートを開くだけ」「パソコンを起動するだけ」といった極めて小さな行動に設定すれば、"
        "脳はそれを脅威とは見なさず、スムーズに行動へ移行できる。どんなに壮大な目標であっても、小さな第一歩を【 53 】"
        "前進することはあり得ない。\n\n"
        "日々の小さな達成感を積み重ねる習慣こそが、先延ばしの悪循環を断ち切り、自己肯定感を育む鍵となる【 54 】。"
    )

    m9_raw = [
        (
            "N2_06_M9_01", "N2-GR-TEXT", "Mondai 9: 文章の文法",
            "文章中の【 50 】に入る最も適切なものを選びなさい。", m9_passage,
            [("A", "明らかになりつつある"), ("B", "明らかにするわけがない"), ("C", "明らかになったにすぎない"), ("D", "明らかにならざるを得ない")],
            "A",
            "〜つつある: Đang dần dần sáng tỏ theo tiến trình của các nghiên cứu khoa học gần đây (研究によって明らかになりつつある).",
            {
                "B": "〜わけがない: Tuyệt đối không có lý nào (nghi ngờ phủ định).",
                "C": "〜にすぎない: Chỉ là... không hơn không kém (hạ thấp mức độ).",
                "D": "〜ざるを得ない: Buộc phải đành chấp nhận."
            }
        ),
        (
            "N2_06_M9_02", "N2-GR-TEXT", "Mondai 9: 文章の文法",
            "文章中の【 51 】に入る最も適切なものを選びなさい。", m9_passage,
            [("A", "末に"), ("B", "あまり"), ("C", "うえに"), ("D", "ついでに")],
            "B",
            "〜あまり: Vì quá mức... dẫn đến kết quả tiêu cực vượt ngoài tầm kiểm soát (求めたあまり - vì quá khao khát tìm kiếm cảm giác an tâm tạm thời mà trốn tránh sang lướt điện thoại).",
            {
                "A": "〜末に: Sau một hồi đắn đo suy nghĩ lâu dài (ở đây là phản xạ tâm lý bột phát, không phải suy tính).",
                "C": "〜うえに: Hơn nữa, thêm vào đó.",
                "D": "〜ついでに: Tiện thể nhân tiện làm gì."
            }
        ),
        (
            "N2_06_M9_03", "N2-GR-TEXT", "Mondai 9: 文章の文法",
            "文章中の【 52 】に入る最も適切なものを選びなさい。", m9_passage,
            [("A", "ほかならない"), ("B", "相違ない"), ("C", "かぎらない"), ("D", "にすぎない")],
            "A",
            "〜にほかならない: Chính là, không gì khác ngoài... (giải thích bản chất cốt lõi: 感情の制御をめぐる葛藤にほかならない - chính là sự giằng xé trong việc kiểm soát cảm xúc).",
            {
                "B": "〜相違ない: Chắc chắn là (phán đoán chứng cứ).",
                "C": "〜かぎらない: Không nhất thiết là.",
                "D": "〜にすぎない: Chỉ dừng lại ở."
            }
        ),
        (
            "N2_06_M9_04", "N2-GR-TEXT", "Mondai 9: 文章の文法",
            "文章中の【 53 】に入る最も適切なものを選びなさい。", m9_passage,
            [("A", "踏み出すことなしに"), ("B", "踏み出す契機に"), ("C", "踏み出すにつれて"), ("D", "踏み出したあげく")],
            "A",
            "〜ことなしに（〜ない）: Nếu không có A thì không thể có B (小さな第一歩を踏み出すことなしに、前進することはあり得ない - nếu không bước đi bước đầu tiên thì không thể nào có sự tiến bộ).",
            {
                "B": "〜契機に: Lấy làm cơ hội bước ngoặt.",
                "C": "〜につれて: Cùng với, càng... càng... (không đi với vị ngữ phủ định tuyệt đối あり得ない).",
                "D": "〜あげく: Sau một hồi dẫn tới kết cục cay đắng."
            }
        ),
        (
            "N2_06_M9_05", "N2-GR-TEXT", "Mondai 9: 文章の文法",
            "文章中の【 54 】に入る最も適切なものを選びなさい。", m9_passage,
            [("A", "のではないだろうか"), ("B", "わけにはいかないだろう"), ("C", "にちがいないはずだ"), ("D", "はずがないのではないか")],
            "A",
            "〜のではないだろうか: Chẳng phải là... hay sao (câu kết luận quan điểm tác giả một cách sâu sắc, gợi mở và thuyết phục: 育む鍵となるのではないだろうか).",
            {
                "B": "〜わけにはいかない: Không thể vì đạo đức xã hội.",
                "C": "〜にちがいないはずだ: Cấu trúc lặp thừa đuôi phán đoán bất tự nhiên.",
                "D": "〜はずがない: Phủ định gắt gao không phù hợp đúc kết bài viết."
            }
        ),
    ]

    for qid, tid, cat, stem, pass_text, opts, ans, exp, dist in m9_raw:
        items.append({
            "id": qid, "typeId": tid, "skill": "Language Knowledge", "category": cat,
            "stem": stem, "contextPassage": pass_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 10: 短文読解 (Short Passages - 5 items)
    # =========================================================================
    m10_passages = [
        (
            "ビジネスにおける「報告」と「相談」は似ているようで本質が異なる。"
            "報告とは過去に発生した事実や現在の進捗を正確に伝える行為であり、そこに対話の余地は少ない。"
            "一方の相談は、将来の不確実な判断に対して他者の知恵を借りる協働のプロセスである。"
            "部下が上司に相談を持ちかけるのを躊躇するのは、自らの未熟さを露呈することを恐れるためだが、"
            "相談を通じて思考を深めることこそが、組織における成長の近道なのである。",
            "筆者によると、ビジネスにおける「相談」の重要性はどこにあるか。",
            [
                ("A", "上司に責任を転嫁し、判断の負担を減らせる点"),
                ("B", "他者の知恵を借りて思考を深め、自身の成長につながる点"),
                ("C", "過去の失敗を早期に報告し、損害を最小限に抑える点"),
                ("D", "自分の優れた能力を上司に効果的にアピールできる点")
            ],
            "B",
            "Thông tin nằm trực tiếp ở câu cuối: '相談を通じて思考を深めることこそが、組織における成長の近道なのである' (Thông qua trao đổi mà đào sâu tư duy, chính là con đường ngắn nhất để trưởng thành trong tổ chức). Đáp án đúng là B.",
            {
                "A": "Đổ lỗi/đùn đẩy trách nhiệm cho cấp trên là suy diễn sai trái.",
                "C": "Báo cáo sớm sai lầm là thuộc về định nghĩa của 'báo cáo' (報告), không phải 'thảo luận' (相談).",
                "D": "Khoe khoang năng lực trái ngược với việc thừa nhận cần học hỏi trong bài."
            }
        ),
        (
            "都市の緑地化は、単に美しい景観を創出するだけでなく、ヒートアイランド現象の緩和に不可欠な役割を担っている。"
            "アスファルトやコンクリートは日中の熱を吸収・蓄積し、夜間に放射することで都市の気温を高止まりさせる。"
            "これに対し、樹木や草花は根から吸い上げた水分を葉から蒸発させる「蒸散作用」によって周囲の熱を奪う。"
            "わずか数十平方メートルの小規模な公園であっても、周囲数ブロックの気温を1度前後下げる効果があるという。",
            "樹木が都市のヒートアイランド現象を和らげるメカニズムとして、文章で述べられているのはどれか。",
            [
                ("A", "葉からの蒸散作用によって周囲の熱を奪うこと"),
                ("B", "コンクリートの反射光を遮断して日差しを和らげること"),
                ("C", "夜間に蓄積した冷気を都市全体に風として循環させること"),
                ("D", "地中の水分を凍結させて地表温度の急上昇を抑えること")
            ],
            "A",
            "Đoạn văn nêu rõ: '樹木や草花は根から吸い上げた水分を葉から蒸発させる「蒸散作用」によって周囲の熱を奪う'. Đáp án đúng là A.",
            {
                "B": "Chặn ánh sáng phản xạ không phải là cơ chế làm mát được giải thích trong bài.",
                "C": "Tuần hoàn gió lạnh ban đêm là thông tin tự suy diễn không có trong bài.",
                "D": "Đóng băng nước trong lòng đất hoàn toàn sai khoa học và không có trong bài."
            }
        ),
        (
            "消費者が「期間限定」や「数量限定」という文言に抗えないのは、行動経済学でいう「損失回避性」が働くためである。"
            "人間は同じ価値であっても、何かを得る喜びよりも、それを失う痛みを約2倍強く感じる傾向がある。"
            "「今買わなければ二度と手に入らないかもしれない」という焦燥感は、得られる商品の実質的価値以上に、"
            "機会の損失を恐れる心理を強く刺激し、衝動的な購買行動へと駆り立てるのである。",
            "文章によると、消費者が「限定商品」を思わず買ってしまう根本的な心理的要因は何か。",
            [
                ("A", "他者よりも早く優位な立場に立ちたいという競争心"),
                ("B", "手に入れる喜びよりも機会を逃す痛みを強く恐れる心理"),
                ("C", "限定品ほど品質や安全性が保証されているという信頼感"),
                ("D", "価格が通常品よりも大幅に割引されているという経済的計算")
            ],
            "B",
            "Đoạn văn giải thích: '人間は同じ価値であっても、何かを得る喜びよりも、それを失う痛みを約2倍強く感じる傾向がある... 機会の損失を恐れる心理を強く刺激し'. Đáp án đúng là B.",
            {
                "A": "Lòng cạnh tranh tranh giành vị thế không phải là tâm lý cốt lõi được bài viết phân tích.",
                "C": "Bài không hề đề cập đến việc hàng giới hạn thì chất lượng an toàn hơn.",
                "D": "Hàng giới hạn không phải vì giảm giá rẻ hơn mà vì sợ mất cơ hội."
            }
        ),
        (
            "日本語のオノマトペ（擬音語・擬態語）の豊かさは、微妙な感覚や感情を直感的に共有する上で極めて有効である。"
            "「さらさら」と「ざらざら」のように、子音や母音の微細な響きの違いだけで手触りの変化を鮮やかに描き分けることができる。"
            "論理的な長文を用いずとも、一語で五感に訴えかけることができるオノマトペは、"
            "合理的効率を重んじる現代社会において、むしろ人間らしい共感を促す貴重な言語資源といえるだろう。",
            "筆者は現代社会におけるオノマトペをどのように評価しているか。",
            [
                ("A", "論理的な思考力を低下させるため、公式な文書では使用を控えるべきもの"),
                ("B", "一語で五感に訴えかけ、人間らしい共感を促す貴重な資源"),
                ("C", "若者の語彙力を貧困化させ、正確なコミュニケーションを妨げるもの"),
                ("D", "日本独自の文化であり、外国語への正確な翻訳が不可能なもの")
            ],
            "B",
            "Câu cuối khẳng định: '一語で五感に訴えかけることができるオノマトペは、合理的効率を重んじる現代社会において、むしろ人間らしい共感を促す貴重な言語資源といえるだろう'. Đáp án đúng là B.",
            {
                "A": "Tác giả đánh giá tích cực, không hề cho rằng làm giảm tư duy logic hay cần hạn chế.",
                "C": "Làm nghèo vốn từ của giới trẻ là suy diễn hoàn toàn ngược lại ý tác giả.",
                "D": "Bài không bàn về tính bất khả dịch sang tiếng nước ngoài."
            }
        ),
        (
            "科学の歴史において、数々の重大な発見が「偶然」を契機として生まれてきた。"
            "ペニシリンの発見やポストイットの粘着剤の開発など、意図しない失敗や異変がブレイクスルーをもたらした例は枚挙にいとまがない。"
            "しかし、偶然が発見に結びつくのは、あらかじめ問題意識を研ぎ澄まし、徹底的な観察を続けていた者に限られる。"
            "準備のない者の前を偶然が通り過ぎても、それはただの「見過ごされた日常の出来事」に終わってしまうのだ。",
            "科学における「偶然の発見」について、筆者が最も主張したいことは何か。",
            [
                ("A", "計画的な研究よりも、運や偶然に頼る方が画期的な成果を生みやすい。"),
                ("B", "偶然を捉えて発見につなげるには、日頃の徹底的な準備と問題意識が不可欠である。"),
                ("C", "失敗した実験のデータは価値がないため、すぐに破棄して新しい計画に移行すべきだ。"),
                ("D", "優れた科学者であっても、偶然の好機に恵まれなければ偉大な業績は残せない。")
            ],
            "B",
            "Đoạn văn nhấn mạnh: '偶然が発見に結びつくのは、あらかじめ問題意識を研ぎ澄まし、徹底的な観察を続けていた者に限られる... 準備のない者の前を偶然が通り過ぎても、それはただの「見過ごされた日常の出来事」に終わってしまう'. Đáp án đúng là B.",
            {
                "A": "Tác giả không khuyên dựa vào vận may hơn là nghiên cứu có kế hoạch.",
                "C": "Vứt bỏ dữ liệu thất bại là ngược lại với bài học tìm ra đột phá từ thất bại.",
                "D": "Không phải nhấn mạnh sự phụ thuộc vào may mắn, mà nhấn mạnh sự chuẩn bị kỹ càng để nắm bắt cơ hội."
            }
        ),
    ]

    for idx, (p_text, q_stem, opts, ans, exp, dist) in enumerate(m10_passages, 1):
        items.append({
            "id": f"N2_06_M10_{idx:02d}", "typeId": "N2-RD-SHORT", "skill": "Reading",
            "category": "Mondai 10: 短文読解", "stem": q_stem, "contextPassage": p_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 11: 中文読解 (Medium Passages - 9 items, 3 passages x 3 items)
    # =========================================================================
    # Medium Passage 1: Organizational Psychology - Psychological Safety
    m11_p1_text = (
        "現代の急速に変化するビジネス環境において、チームの生産性を左右する決定的な要因として「心理的安全性（Psychological Safety）」が注目されている。"
        "心理的安全性とは、チームのメンバーが「この集団内では、自分の無知や失敗を率直にさらけ出しても、他者から非難されたり嘲笑されたりすることはない」と確信できる状態を指す。\n\n"
        "多くの組織では、知識やスキルの高い優秀な個人を集めれば、自動的に優れた成果が上がると考えられがちであった。"
        "しかし実証研究が明らかにしたのは、どれほど個人の能力が卓越していても、心理的安全性が欠如した職場では、ミスを隠蔽し、新しい提案を躊躇する空気が支配的になるという事実である。"
        "質問をすれば「そんなことも知らないのか」と思われ、新しいアイデアを出せば「前例がない」と一蹴される環境では、誰もがリスクを避けて現状維持に終始するようになる。\n\n"
        "真の心理的安全性とは、単にメンバー同士が仲良くお互いに気遣い合う「生ぬるい居心地の良さ」ではない。"
        "むしろ、目指すべき高い目標に向かって、率直な意見の対立や建設的な批判を恐れずにぶつけ合える関係性こそが本質なのである。"
        "リーダーが自らの不完全さを認め、部下の率直な発言を歓迎する姿勢を示すことこそが、チームに心理的安全性をもたらす第一歩となる。"
    )

    m11_p1_questions = [
        (
            "N2_06_M11_01", "文章で説明されている「心理的安全性」の定義として最も適切なものはどれか。",
            [
                ("A", "チーム内の全員が高い専門スキルを持ち、ミスを犯さずに業務を遂行できる状態"),
                ("B", "失敗や疑問を率直に口にしても、仲間から否定や攻撃を受けないと確信できる状態"),
                ("C", "厳しいノルマや納期が存在せず、精神的なストレスを感じずに過ごせる状態"),
                ("D", "メンバー同士が親友のようにプライベートを共有し、常に意見が一致する状態")
            ],
            "B",
            "Đoạn 1 nêu rõ: '自分の無知や失敗を率直にさらけ出しても、他者から非難されたり嘲笑されたりすることはないと確信できる状態'. Đáp án đúng là B.",
            {
                "A": "Kỹ năng cao không phạm lỗi là điều kiện cá nhân, không phải định nghĩa an toàn tâm lý.",
                "C": "Không có áp lực chỉ tiêu là sự thoải mái về nhiệm vụ, không phản ánh môi trường cởi mở giao tiếp.",
                "D": "Chia sẻ đời tư và luôn đồng thuận ý kiến là sai với bản chất chấp nhận đối thoại phản biện ở đoạn 3."
            }
        ),
        (
            "N2_06_M11_02", "心理的安全性が欠如した組織では、どのような問題が生じると述べられているか。",
            [
                ("A", "個人間の競争が激化しすぎて、業務の効率が極端に低下する。"),
                ("B", "失敗の隠蔽や提案の躊躇が生じ、リスクを避けて現状維持にとどまる。"),
                ("C", "社員同士の個人的なトラブルが多発し、離職率が急増する。"),
                ("D", "優秀なリーダーばかりが集まり、指示系統に混乱が生じる。")
            ],
            "B",
            "Đoạn 2 nêu rõ: 'ミスを隠蔽し、新しい提案を躊躇する空気が支配的になる... 誰もがリスクを避けて現状維持に終始するようになる'. Đáp án đúng là B.",
            {
                "A": "Cạnh tranh cá nhân quá khốc liệt không phải là hệ quả được nhắc đến.",
                "C": "Mâu thuẫn đời tư và tỉ lệ nghỉ việc không được phân tích là trọng tâm của đoạn.",
                "D": "Quá nhiều lãnh đạo giỏi gây rối loạn chỉ huy là suy diễn ngoài văn bản."
            }
        ),
        (
            "N2_06_M11_03", "「真の心理的安全性」の本質について、筆者の考えと合致するものはどれか。",
            [
                ("A", "衝突を避けてお互いの意見を無条件に認め合う、居心地の良い関係を築くこと"),
                ("B", "高い目標の達成に向けて、率直な対立や建設的な批判を恐れずにぶつけ合えること"),
                ("C", "リーダーが完璧な手本を示し、部下に一切の疑問を抱かせないようにすること"),
                ("D", "業務上の失敗に対する責任の所在を曖昧にし、個人の精神的負担をなくすこと")
            ],
            "B",
            "Đoạn 3 phân tích: '単にメンバー同士が仲良くお互いに気遣い合う生ぬるい居心地の良さではない... 高い目標に向かって、率直な意見の対立や建設的な批判を恐れずにぶつけ合える関係性こそが本質'. Đáp án đúng là B.",
            {
                "A": "Né tránh xung đột để dĩ hòa vi quý chính là '生ぬるい居心地の良さ' mà tác giả bác bỏ.",
                "C": "Lãnh đạo hoàn hảo không có nghi ngờ là trái ngược với việc lãnh đạo cần thừa nhận sự chưa hoàn hảo của mình.",
                "D": "Làm mập mờ trách nhiệm là hoàn toàn sai với tinh thần xây dựng trách nhiệm tập thể."
            }
        ),
    ]

    for qid, q_stem, opts, ans, exp, dist in m11_p1_questions:
        items.append({
            "id": qid, "typeId": "N2-RD-MID", "skill": "Reading", "category": "Mondai 11: 中文読解",
            "stem": q_stem, "contextPassage": m11_p1_text, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # Medium Passage 2: Environmental Technology - Life Cycle Assessment
    m11_p2_text = (
        "脱炭素社会の実現に向け、走行時に温室効果ガスを排出しない電気自動車（EV）へのシフトが世界中で加速している。"
        "しかし、製品が環境に与える負荷を真に評価するためには、走行時のみならず、製造から廃棄に至る全プロセスを網羅した"
        "「ライフサイクルアセスメント（LCA）」の視点が不可欠である。\n\n"
        "EVの核心部であるバッテリーの製造には、リチウムやコバルトなどの希少金属の大規模な採掘と精錬が必要となる。"
        "この工程では膨大なエネルギーが消費され、現時点では火力発電に頼る地域が多いため、製造段階だけで大量のCO2が排出される。"
        "ある試算によれば、再生可能エネルギーによる電力比率が低い国では、EVが走行中に削減するCO2量が製造段階の排出量を相殺するまでに、"
        "数万キロメートル以上の走行が必要とされるケースもあるという。\n\n"
        "これはEVへの移行を否定するものではなく、技術革新の方向性を正しく見極めるべきであることを示唆している。"
        "単にガソリン車をEVに置き換えるだけでなく、発電構成そのものの脱炭素化を進めると同時に、"
        "バッテリーのリサイクル技術や代替材料の開発を車の普及と車の製造の両輪で進めなければ、真の環境保護には結びつかないのである。"
    )

    m11_p2_questions = [
        (
            "N2_06_M11_04", "筆者が「ライフサイクルアセスメント（LCA）」の視点が必要だと主張する理由は何か。",
            [
                ("A", "EVの走行時のCO2排出量が、ガソリン車よりも大幅に増加することが判明したため"),
                ("B", "走行時だけでなく、原材料の採掘・製造から廃棄までの全段階の環境負荷を評価するため"),
                ("C", "希少金属の価格高騰によって、自動車メーカーの採算が悪化しているため"),
                ("D", "火力発電による電力供給が完全に停止し、EVの充電が困難になりつつあるため")
            ],
            "B",
            "Đoạn 1 nêu rõ: '走行時のみならず、製造から廃棄に至る全プロセスを網羅した「ライフサイクルアセスメント（LCA）」の視点が不可欠である'. Đáp án đúng là B.",
            {
                "A": "EV khi chạy không phát thải khí nhà kính (走行時に温室効果ガスを排出しない), phương án A sai hoàn toàn.",
                "C": "Giá kim loại quý làm giảm lợi nhuận kinh tế không phải là lý do môi trường của LCA.",
                "D": "Nhiệt điện bị dừng hoàn toàn là thông tin sai lệch tự bịa đặt."
            }
        ),
        (
            "N2_06_M11_05", "文章によると、現在のEV製造において生じている環境上の課題は何か。",
            [
                ("A", "バッテリー製造に必要な希少金属の採掘や精錬に膨大なエネルギーが消費され、CO2が排出されること"),
                ("B", "EVのバッテリーが数千キロメートルの走行で劣化し、頻繁な交換が必要になること"),
                ("C", "走行時に発生する微細な粒子が、大気汚染の新たな原因となっていること"),
                ("D", "再生可能エネルギーだけで充電を行うと、バッテリーの寿命が大幅に縮むこと")
            ],
            "A",
            "Đoạn 2 nêu rõ: 'バッテリーの製造には、リチウムやコバルトなどの希少金属の大規模な採掘と精錬が必要となる。この工程では膨大なエネルギーが消費され... 製造段階だけで大量のCO2が排出される'. Đáp án đúng là A.",
            {
                "B": "Pin bị chai sau vài ngàn cây số là chi tiết sai sự thật không có trong bài.",
                "C": "Hạt bụi mịn khi chạy không hề được đề cập trong bài viết.",
                "D": "Năng lượng tái tạo làm giảm tuổi thọ pin là suy diễn vô căn cứ."
            }
        ),
        (
            "N2_06_M11_06", "真の環境保護を達成するために必要なこととして、筆者が提言しているのはどれか。",
            [
                ("A", "EVの開発を即座に中止し、従来のガソリン車の燃費向上に専念すること"),
                ("B", "希少金属の採掘量を制限し、自動車の生産台数そのものを大幅に削減すること"),
                ("C", "車両の普及だけでなく、発電の脱炭素化やバッテリーのリサイクル技術を併せて進めること"),
                ("D", "すべての国で均一な環境基準を適用し、未達成の国からの輸出入を禁止すること")
            ],
            "C",
            "Đoạn 3 kết luận: '単にガソリン車をEVに置き換えるだけでなく、発電構成そのものの脱炭素化を進めると同時に、バッテリーのリサイクル技術や代替材料の開発を車の普及と車の製造の両輪で進めなければ、真の環境保護には結びつかない'. Đáp án đúng là C.",
            {
                "A": "Dừng phát triển EV là trái ngược với câu mở đầu đoạn 3: 'これはEVへの移行を否定するものではなく'.",
                "B": "Cắt giảm sản lượng xe không phải là giải pháp tác giả đưa ra.",
                "D": "Cấm xuất nhập khẩu là giải pháp cực đoan mang tính suy diễn sai."
            }
        ),
    ]

    for qid, q_stem, opts, ans, exp, dist in m11_p2_questions:
        items.append({
            "id": qid, "typeId": "N2-RD-MID", "skill": "Reading", "category": "Mondai 11: 中文読解",
            "stem": q_stem, "contextPassage": m11_p2_text, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # Medium Passage 3: Cognitive Science - Digital Reading vs Deep Reading
    m11_p3_text = (
        "電子書籍やウェブ記事の普及により、私たちはかつてないほど大量のテキスト情報に日常的にアクセスできるようになった。"
        "しかし、スクロールしながら画面上の文字を追う「デジタル読書」と、紙の書物をめくる「紙の読書」とでは、"
        "脳内における情報処理の様式に決定的な相違があることが認知神経科学の研究で指摘されている。\n\n"
        "デジタル画面を読む際、読者は無意識のうちにキーワードを拾い読みする「スキャニング（拾い読み）」のモードに入りやすい。"
        "リンクや通知が点在する画面上では注意が分散し、文章の論理構成を深く吟味する前に次の情報へと視線が移ってしまう。"
        "これに対して紙の書籍では、読者は本の厚みや手触り、ページの空間的配置を手がかりにしながら、物語や論理の全体像を立体的に把握する。"
        "ページを行きつ戻りつしながら行間を味わい、著者の意図に反論や問いを投げかける「深い読み（Deep Reading）」は、紙という物理的実体と不可分なのである。\n\n"
        "デジタル読書がもたらす情報収集の即時性と利便性は疑いようがない。"
        "だが、効率的な情報消費だけに偏重すれば、文脈を洞察し複雑な概念を統合する知的能力が衰弱しかねない。"
        "目的に応じて情報収集のためのデジタル読書と、思索を深めるための紙の読書を自覚的に使い分ける「認知的バイリンガル」の姿勢が今こそ求められている。"
    )

    m11_p3_questions = [
        (
            "N2_06_M11_07", "デジタル画面で文章を読む際の特徴として、文章で述べられているのはどれか。",
            [
                ("A", "文字の視認性が低いため、目の疲労が紙よりも早く蓄積する。"),
                ("B", "注意が分散しやすく、キーワードを拾い読みするモードに入りやすい。"),
                ("C", "著者の論理構成を過剰に分析し、読む速度が極端に遅くなる。"),
                ("D", "ページの空間的配置を直感的に記憶し、詳細な事実を忘れにくくなる。")
            ],
            "B",
            "Đoạn 2 nêu rõ: '読者は無意識のうちにキーワードを拾い読みする「スキャニング（拾い読み）」のモードに入りやすい... 注意が分散し、文章の論理構成を深く吟味する前に次の情報へと視線が移ってしまう'. Đáp án đúng là B.",
            {
                "A": "Mỏi mắt do độ nhìn kém không được nhắc đến như là đặc trưng xử lý thông tin nhận thức.",
                "C": "Đọc chậm do phân tích quá mức là trái ngược với việc đọc lướt nhanh chuyển tiếp.",
                "D": "Ghi nhớ cấu trúc không gian là đặc trưng của đọc sách giấy, không phải đọc màn hình kỹ thuật số."
            }
        ),
        (
            "N2_06_M11_08", "「深い読み（Deep Reading）」について、紙の書籍が適している理由として筆者が挙げるのはどれか。",
            [
                ("A", "厚みやページの空間配置を手がかりに、論理の全体像を把握し思索を深められるため"),
                ("B", "文字のフォントやレイアウトを読者が自由に変更でき、理解度が高まるため"),
                ("C", "外部の誘惑を遮断するため、長時間の連続読書でも集中力が途切れないため"),
                ("D", "紙の書籍の方がデジタル媒体よりも、掲載されている情報の正確性が高いため")
            ],
            "A",
            "Đoạn 2 giải thích: '読者は本の厚みや手触り、ページの空間的配置を手がかりにしながら、物語や論理の全体像を立体的に把握する... 行間を味わい、著者の意図に反論や問いを投げかける「深い読み（Deep Reading）」は、紙という物理的実体と不可分'. Đáp án đúng là A.",
            {
                "B": "Tự do đổi font chữ layout là tính năng của sách điện tử số, không phải sách giấy.",
                "C": "Tập trung không mệt mỏi trong nhiều giờ là suy diễn không có trong bài.",
                "D": "Độ chính xác của thông tin sách giấy không phải luận điểm của đoạn văn."
            }
        ),
        (
            "N2_06_M11_09", "これからの時代における読書のあり方として、筆者が提言しているのはどれか。",
            [
                ("A", "デジタル媒体の利用を完全にやめ、すべての学習を紙の書物に戻すこと"),
                ("B", "情報収集のデジタル読書と思索を深める紙の読書を、目的に応じて使い分けること"),
                ("C", "読書速度を向上させる速読技術を習得し、より多くの情報を網羅すること"),
                ("D", "電子書籍の技術を進化させ、紙の書籍の質感や厚みを画面上に完全再現すること")
            ],
            "B",
            "Đoạn 3 kết luận: '目的に応じて情報収集のためのデジタル読書と、思索を深めるための紙の読書を自覚的に使い分ける「認知的バイリンガル」の姿勢が今こそ求められている'. Đáp án đúng là B.",
            {
                "A": "Từ bỏ hoàn toàn kỹ thuật số là cực đoan, trái ngược với việc tác giả công nhận tính tiện lợi của nó.",
                "C": "Học kỹ năng đọc nhanh không phải là đề xuất của tác giả.",
                "D": "Mô phỏng xúc giác trên màn hình là suy diễn công nghệ ngoài lề."
            }
        ),
    ]

    for qid, q_stem, opts, ans, exp, dist in m11_p3_questions:
        items.append({
            "id": qid, "typeId": "N2-RD-MID", "skill": "Reading", "category": "Mondai 11: 中文読解",
            "stem": q_stem, "contextPassage": m11_p3_text, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 12: 統合理解 (Comparative Reading - 2 items)
    # =========================================================================
    m12_text = (
        "【文章A】\n"
        "生成AIによる文章作成技術の進化は、人間の創作活動に革命をもたらしつつある。"
        "膨大な言語データを学習したAIは、人間が思いつかないような斬新な比喩やプロットの展開を瞬時に提示してくれる。"
        "執筆者がアイデアの枯渇に悩んだ際、AIとの壁打ち（対話）を通じて思考の枠組みを拡張し、新たな着想を得ることができる。"
        "AIは人間の創造性を奪う脅威ではなく、むしろ作家の能力を増幅させ、より豊かな表現へと導く強力な共作者（コ・クリエイター）なのである。\n\n"
        "【文章B】\n"
        "AIが生成する流暢な文章に触れるたび、私は表現の「均質化」という深刻な危機感を覚える。"
        "AIの文章は過去のデータの統計的確率に基づいて生成されるため、文法的に整っている一方で、平均的で無難な表現に収束しやすい。"
        "真の文学的価値とは、個人の独自の苦悩や生の体験から搾り出された、ときに不器用で破調を伴う唯一無二の言葉にこそ宿る。"
        "AIの安易な利用に慣れてしまえば、創作者自身の特異な個性の刃が削ぎ落とされ、誰が書いても同じような無個性な作品ばかりが氾濫することになるだろう。"
    )

    m12_questions = [
        (
            "N2_06_M12_01", "生成AIが文章の創作活動に与える影響について、AとBの筆者はどのように捉えているか。",
            [
                ("A", "Aは思考の枠組みを広げる共作者として評価し、Bは表現が平均化・無個性化する危機を指摘している。"),
                ("B", "AはAIによって人間の作家が不要になると警告し、BはAIを活用することで文章の完成度が高まると歓迎している。"),
                ("C", "AもBも、AIが生成する文章の文法的な誤りが多すぎるため、実用には耐えないと批判している。"),
                ("D", "AもBも、AIと人間の共同制作がこれからの文学の標準的な形式になると肯定的に予測している。")
            ],
            "A",
            "Bài A nhìn nhận AI là '強力な共作者' giúp mở rộng tư duy sáng tạo; trong khi Bài B cảnh báo nguy cơ '表現の均質化' (đồng nhất hóa, bình quân hóa dẫn đến mất đi bản sắc cá tính độc nhất). Đáp án đúng là A.",
            {
                "B": "Ngược hoàn toàn: A không nói nhà văn bị thừa thãi, B không hề hoan nghênh AI.",
                "C": "Cả hai bài đều không chê ngữ pháp của AI (ngược lại B còn khen là 文法的に整っている).",
                "D": "Bài B chỉ trích sâu sắc việc lạm dụng AI, không hề đồng tình biến nó thành chuẩn mực chung."
            }
        ),
        (
            "N2_06_M12_02", "両方の文章に共通して見られる前提認識はどれか。",
            [
                ("A", "AIは人間の生の苦悩や感情を完全に模倣することに成功したという点"),
                ("B", "AIが極めて高度で流暢な文章を生成する能力を持っているという点"),
                ("C", "AIの利用によって、すべての作家の文章執筆速度が格段に向上したという点"),
                ("D", "AIが普及した結果、紙の書籍の出版数が急速に減少しているという点")
            ],
            "B",
            "Cả Bài A ('人間が思いつかないような斬新な比喩やプロットの展開を瞬時に提示') và Bài B ('AIが生成する流暢な文章') đều thừa nhận năng lực tạo sinh ngôn ngữ của AI hiện nay đã đạt mức độ hết sức thông loát và tinh vi. Đáp án đúng là B.",
            {
                "A": "Bài B khẳng định giá trị văn học đúc kết từ nỗi khổ của con người là điều AI không có (chỉ thống kê xác suất).",
                "C": "Tốc độ viết của mọi tác giả tăng vọt không phải là tiền đề chung được bàn luận.",
                "D": "Sách giấy giảm ấn bản là vấn đề ngoài lề không xuất hiện trong bài."
            }
        ),
    ]

    for qid, q_stem, opts, ans, exp, dist in m12_questions:
        items.append({
            "id": qid, "typeId": "N2-RD-COMP", "skill": "Reading", "category": "Mondai 12: 統合理解",
            "stem": q_stem, "contextPassage": m12_text, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 13: 長文読解 (Thematic Long Passage - 3 items)
    # Aesthetics & Design: "用と美" (Utility and Beauty) in Modern Life
    # =========================================================================
    m13_text = (
        "近代以降の産業社会において、「美」と「実用性（用）」は長らく対立するものとして捉えられてきた。"
        "装飾過剰な工芸品を「鑑賞のための美」として高尚視する一方で、日々の暮らしで使い古される実用的な道具は、"
        "機能的であれば十分であり、美的な価値とは無縁であると見なされがちであった。\n\n"
        "しかし、大正から昭和初期にかけて柳宗悦らが提唱した「民藝（民衆的工芸）運動」は、この二項対立に根本的な疑問を投げかけた。"
        "無名の職人が人々の日常生活のために作った茶碗や着物、ざるなどの日用品の中に、"
        "意図的な装飾や作為を超えた、健康で無駄のない「用の美」が宿っていることを彼らは見出したのである。"
        "毎日繰り返し使われる道具は、機能に奉仕する過程で無駄な要素が自然と削ぎ落とされ、"
        "使えば使うほどに手になじみ、時間の経過とともに風合いを深めていく。"
        "美は実用性の対極にあるのではなく、誠実に実用を極めた先にこそ自然と立ち現れるものなのだ。\n\n"
        "この思想は、大量生産と大量消費が行き詰まりを見せる現代において、再び切実な意味を持ち始めている。"
        "めまぐるしく新製品が消費され、わずかな機能追加で買い替えを促される今日、私たちは「所有する喜び」を本当に味わえているだろうか。"
        "物質的な豊かさを手に入れたはずの私たちがどこか満たされないのは、道具との間に「共に時間を重ねる関係」を結べていないからではないか。"
        "シンプルで無駄のないデザインを愛で、手入れをしながら一つのものを長く愛用する現代のミニマリズムの根底には、"
        "かつて民藝が示した「用と美の調和」に対する無意識の渇望が息づいているように思えてならない。"
    )

    m13_questions = [
        (
            "N2_06_M13_01", "近代以降の産業社会における「美」と「用」の捉え方について、文章で述べられているのはどれか。",
            [
                ("A", "実用的な道具ほど装飾を増やすことで、芸術的な価値を高めるべきだと考えられていた。"),
                ("B", "鑑賞のための美が高尚視される一方、日用品の実用性は美と無縁なものと見なされていた。"),
                ("C", "機能性を極限まで高めた工業製品こそが、最高峰の芸術であると広く認識されていた。"),
                ("D", "職人の手作業で作られた工芸品は品質が劣るため、市場から排除されるべきだとされた。")
            ],
            "B",
            "Đoạn 1 nêu rõ: '装飾過剰な工芸品を「鑑賞のための美」として高尚視する一方で、日々の暮らしで使い古される実用的な道具は、機能的であれば十分であり、美的な価値とは無縁であると見なされがちであった'. Đáp án đúng là B.",
            {
                "A": "Tăng trang trí cho đồ dùng sinh hoạt là hiểu sai tinh thần phân chia nhị nguyên của thời kỳ này.",
                "C": "Coi đồ công nghiệp là nghệ thuật đỉnh cao là suy diễn sai, bài nêu đồ gia dụng bị coi là vô duyên với thẩm mỹ.",
                "D": "Loại trừ đồ thủ công là suy diễn ngoài văn bản."
            }
        ),
        (
            "N2_06_M13_02", "民藝運動が見出した「用の美」の特徴として、最も適切なものはどれか。",
            [
                ("A", "有名な芸術家が計算し尽くした幾何学的な装飾を施していること"),
                ("B", "機能に奉仕する過程で無駄が削ぎ落とされ、使い込むほどに風合いを深めること"),
                ("C", "鑑賞専用の美術品として大切に保管され、決して日常で使われないこと"),
                ("D", "最新の機械設備を用いて短時間で均一かつ大量に生産できること")
            ],
            "B",
            "Đoạn 2 phân tích: '毎日繰り返し使われる道具は、機能に奉仕する過程で無駄な要素が自然と削ぎ落とされ、使えば使うほどに手になじみ、時間の経過とともに風合いを深めていく... 誠実に実用を極めた先にこそ自然と立ち現れる'. Đáp án đúng là B.",
            {
                "A": "Do nghệ nhân vô danh làm ra không vì trang trí cầu kỳ tính toán, trái ngược với nghệ sĩ danh tiếng.",
                "C": "Cất giữ trưng bày không dùng là trái hoàn toàn với việc dùng hàng ngày (用の美).",
                "D": "Sản xuất hàng loạt bằng máy móc hiện đại không phải là đặc trưng của đồ dân nghệ thủ công."
            }
        ),
        (
            "N2_06_M13_03", "現代社会における道具との付き合い方について、筆者の主張と合致するものはどれか。",
            [
                ("A", "消費を活性化させるため、新機能が追加された製品へ常に買い替え続けるべきだ。"),
                ("B", "伝統工芸品のみを購入し、工業的に生産されたプラスチック製品の使用を全廃すべきだ。"),
                ("C", "無駄のないシンプルな道具を手入れしながら長く愛用し、共に時間を重ねる関係を築くべきだ。"),
                ("D", "道具のデザインよりも価格の安さを最優先し、壊れたらすぐに買い替えるのが合理的だ。")
            ],
            "C",
            "Đoạn 3 kết luận: '道具との間に「共に時間を重ねる関係」を結べていないからではないか... シンプルで無駄のないデザインを愛で、手入れをしながら一つのものを長く愛用する... 「用と美の調和」に対する無意識の渇望'. Đáp án đúng là C.",
            {
                "A": "Liên tục mua mới theo kích cầu tiêu dùng là điều tác giả phê phán mang tính trống rỗng.",
                "B": "Xóa bỏ hoàn toàn đồ nhựa là cực đoan hóa, không có trong thông điệp tác giả.",
                "D": "Ưu tiên giá rẻ hỏng thì vứt là chủ nghĩa tiêu dùng đối lập hoàn toàn với việc trân trọng đồng hành cùng đồ vật."
            }
        ),
    ]

    for qid, q_stem, opts, ans, exp, dist in m13_questions:
        items.append({
            "id": qid, "typeId": "N2-RD-LONG", "skill": "Reading", "category": "Mondai 13: 長文読解",
            "stem": q_stem, "contextPassage": m13_text, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 14: 情報検索 (Information Retrieval - 2 items)
    # Notice: International Cultural Exchange Grant Application Guide
    # =========================================================================
    m14_info_text = (
        "【緑川市国際文化交流助成金 申請の手引き】\n\n"
        "緑川市では、市民による草の根の国際交流および多文化共生を促進するため、以下の要領で助成金を交付します。\n\n"
        "■ 助成対象区分および助成額\n"
        "・区分A（イベント事業）：市内在住の外国人と市民が交流するフェスティバル、公演、展示等。\n"
        "  助成限度額：30万円（対象経費の3分の2以内）\n"
        "・区分B（学習支援事業）：外国人市民を対象とした日本語学習支援教室、生活相談会等の継続事業。\n"
        "  助成限度額：20万円（対象経費の全額以内）\n"
        "・区分C（青少年交流事業）：市内の小・中・高校生を対象とする国際理解教育ワークショップ。\n"
        "  助成限度額：15万円（対象経費の2分の1以内）\n\n"
        "■ 対象となる経費\n"
        "講師謝礼、会場使用料、広報チラシ印刷費、通訳翻訳費用、消耗品費（事業専用に限る）。\n"
        "※対象外経費：団体の経常的な事務所維持費、飲食費（参加者への軽食含む）、懇親会費用、備品購入費（パソコン等の購入）。\n\n"
        "■ 申請期間および提出方法\n"
        "・前期募集（6月〜10月実施事業）：4月1日〜4月25日必着\n"
        "・後期募集（11月〜翌年3月実施事業）：9月1日〜9月25日必着\n"
        "提出先：緑川市役所 市民協働課（本庁舎3階）へ直接持参、または特定記録郵便で郵送。\n\n"
        "■ 注意事項\n"
        "1. 同一団体への助成は1年度につき1回限りとします。\n"
        "2. 政治的、宗教的活動、または営利を主たる目的とする事業は対象外です。\n"
        "3. 事業終了後、30日以内に実績報告書および領収書原本の提出が必要です。"
    )

    m14_questions = [
        (
            "N2_06_M14_01", "ある市民団体が「外国人市民向けの日本語学習支援教室」を7月から半年間開催する場合、助成金の申請区分と申請時期の組み合わせとして正しいものはどれか。",
            [
                ("A", "区分A で、4月1日〜4月25日の期間に申請する。"),
                ("B", "区分B で、4月1日〜4月25日の期間に申請する。"),
                ("C", "区分B で、9月1日〜9月25日の期間に申請する。"),
                ("D", "区分C で、事業開始の30日前までに随時申請する。")
            ],
            "B",
            "Dự án lớp hỗ trợ tiếng Nhật cho người nước ngoài (外国人市民を対象とした日本語学習支援教室) thuộc '区分B'. Dự án tổ chức vào tháng 7 (nằm trong khoảng tháng 6 đến tháng 10) nên phải nộp vào đợt đầu (前期募集: 4月1日〜4月25日必着). Do đó đáp án đúng là B.",
            {
                "A": "区分A dành cho sự kiện biểu diễn/lễ hội (イベント事業), không phải lớp học định kỳ.",
                "C": "Đợt sau (後期募集: 9/1 - 9/25) chỉ dành cho các dự án tổ chức từ tháng 11 đến tháng 3 năm sau.",
                "D": "区分C dành cho thanh thiếu niên học sinh, và hạn nộp có kỳ hạn cố định chứ không phải nộp tự do trước 30 ngày."
            }
        ),
        (
            "N2_06_M14_02", "この助成金の対象経費として認められるものはどれか。",
            [
                ("A", "イベント参加者全員に配布するお弁当やお茶などの飲食代"),
                ("B", "事業の案内チラシを市内の施設に配布するための印刷費用"),
                ("C", "団体の事務局で使用する新しいノートパソコンの購入費"),
                ("D", "事業終了後にスタッフやボランティアで開催する打ち上げ懇親会の費用")
            ],
            "B",
            "Mục '対象となる経費' bao gồm rõ ràng '広報チラシ印刷費' (chi phí in tờ rơi thông báo tuyên truyền). Các mục khác đều bị loại trừ: A loại trừ ở mục '飲食費', C loại trừ ở mục '備品購入費（パソコン等の購入）', D loại trừ ở mục '懇親会費用'. Đáp án đúng là B.",
            {
                "A": "Tiền ăn uống của người tham gia (飲食費・軽食) nằm trong danh mục không được trợ cấp (対象外).",
                "C": "Mua sắm máy móc thiết bị (パソコン等の備品購入費) nằm trong danh mục không được trợ cấp.",
                "D": "Tiệc liên hoan cảm ơn (懇親会費用) là chi phí không được trợ cấp."
            }
        ),
    ]

    for qid, q_stem, opts, ans, exp, dist in m14_questions:
        items.append({
            "id": qid, "typeId": "N2-RD-INFO", "skill": "Reading", "category": "Mondai 14: 情報検索",
            "stem": q_stem, "contextPassage": m14_info_text, "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans, "explanationVi": exp, "distractorExplanations": dist
        })

    # Apply balanced answer key permutation across non-star items
    target_moves = {
        'N2_06_M7_02': 'C',
        'N2_06_M7_04': 'D',
        'N2_06_M7_06': 'C',
        'N2_06_M7_07': 'D',
        'N2_06_M7_08': 'C',
        'N2_06_M7_09': 'D',
        'N2_06_M7_10': 'C',
        'N2_06_M7_11': 'D',
        'N2_06_M7_12': 'C',
        'N2_06_M9_01': 'D',
        'N2_06_M9_02': 'C',
        'N2_06_M9_03': 'D',
        'N2_06_M9_04': 'C',
        'N2_06_M10_01': 'C',
        'N2_06_M10_02': 'D',
        'N2_06_M10_03': 'C',
        'N2_06_M10_04': 'D',
        'N2_06_M11_01': 'C',
        'N2_06_M11_02': 'D',
        'N2_06_M11_03': 'D',
        'N2_06_M11_04': 'D',
        'N2_06_M13_01': 'D'
    }

    import copy
    for q in items:
        qid = q['id']
        if qid in target_moves:
            new_key = target_moves[qid]
            orig_key = q['correctAnswer']
            orig_opts = {o['id']: o['text'] for o in q['options']}
            correct_text = orig_opts[orig_key]
            swap_text = orig_opts[new_key]
            for o in q['options']:
                if o['id'] == new_key:
                    o['text'] = correct_text
                elif o['id'] == orig_key:
                    o['text'] = swap_text
            orig_dist = copy.deepcopy(q.get('distractorExplanations', {}))
            new_dist = {}
            for lid in ['A', 'B', 'C', 'D']:
                if lid == new_key:
                    continue
                elif lid == orig_key:
                    new_dist[lid] = orig_dist.get(new_key, f'Giải thích cho {lid}.')
                else:
                    new_dist[lid] = orig_dist.get(lid, f'Giải thích cho {lid}.')
            q['correctAnswer'] = new_key
            q['distractorExplanations'] = new_dist

    assert len(items) == 75, f"Section 1 must contain exactly 75 items, got {len(items)}"
    return items

if __name__ == "__main__":
    from collections import Counter
    items = get_n2_mock_06_sec1_items()
    counts = Counter(it['correctAnswer'] for it in items)
    print(f"Total Section 1 items: {len(items)}")
    print(f"Answer distribution: {counts}")
