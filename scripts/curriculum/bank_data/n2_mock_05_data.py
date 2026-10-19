# -*- coding: utf-8 -*-
"""
JLPT N2 Mock Exam #05 - Section 1: Language Knowledge & Reading (言語知識・読解)
Blueprint (75 items / 105 minutes):
- Mondai 1: 漢字読み (5 items) [Q1 - Q5]
- Mondai 2: 表記 (5 items) [Q6 - Q10]
- Mondai 3: 語形成 (5 items) [Q11 - Q15]
- Mondai 4: 文脈規定 (7 items) [Q16 - Q22]
- Mondai 5: 言い換え類義 (5 items) [Q23 - Q27]
- Mondai 6: 用法 (5 items) [Q28 - Q32]
- Mondai 7: 文法形式 (12 items) [Q33 - Q44]
- Mondai 8: 文の組み立て ★ (5 items) [Q45 - Q49] (Strictly verified permutations)
- Mondai 9: 文章の文法 (5 items) [Q50 - Q54]
- Mondai 10: 短文読解 (5 items) [Q55 - Q59]
- Mondai 11: 中文読解 (9 items) [Q60 - Q68]
- Mondai 12: 統合理解 (2 items) [Q69 - Q70]
- Mondai 13: 長文読解 (3 items) [Q71 - Q73]
- Mondai 14: 情報検索 (2 items) [Q74 - Q75]
Total Section 1: 75 items
"""

def get_n2_mock_05_sec1_items():
    items = []

    # =========================================================================
    # MONDAI 1: 漢字読み (Kanji Reading - 5 items)
    # =========================================================================
    m1_raw = [
        (
            "N2_05_M1_01",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "大雪のため、山頂へと続く道路の通行が完全に【遮断】された。",
            "しゃだん",
            [("A", "さだん"), ("B", "しゃてん"), ("C", "しゃだん"), ("D", "さてん")],
            "C",
            "遮断（しゃだん - GIÁ ĐOẠN）: Cắt đứt, ngăn chặn, chặn lối lưu thông. Chữ 遮 có âm on là しゃ, chữ 断 có âm on là だん.",
            {
                "A": "さだん: Âm さ là âm đọc sai của chữ 遮 (âm chuẩn duy nhất trong từ này là しゃ).",
                "B": "しゃてん: Nhầm chữ 断 (だん) thành chữ 点 (てん).",
                "D": "さてん: Sai cả âm đầu lẫn âm cuối."
            }
        ),
        (
            "N2_05_M1_02",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "不測の事態に備えて、会社は迅速かつ適切な【措置】を講じる必要がある。",
            "そち",
            [("A", "そち"), ("B", "しょち"), ("C", "そじ"), ("D", "しょじ")],
            "A",
            "措置（そち - THỐ TRÍ）: Biện pháp, đối sách xử lý tình huống. Chữ 措 có âm on là そ, chữ 置 có âm on là ち.",
            {
                "B": "しょち: Nhầm sang từ 処置 (しょち - xử trí y tế, cấp cứu vết thương).",
                "C": "そじ: Nhầm âm thanh ち thành âm đục じ.",
                "D": "しょじ: Nhầm cả sang 処 (しょ) lẫn âm đục じ."
            }
        ),
        (
            "N2_05_M1_03",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "複雑に絡み合う問題の本質を正確に【把握】することが解決への第一歩だ。",
            "はあく",
            [("A", "はわく"), ("B", "ほあく"), ("C", "ほうあく"), ("D", "はあく")],
            "D",
            "把握（はあく - BẢ ÁC）: Nắm bắt, thấu hiểu tường tận bản chất của vấn đề. Chữ 把 có âm on là は, chữ 握 có âm on là あく.",
            {
                "A": "はわく: Nhầm âm あく của chữ 握 thành わく.",
                "B": "ほあく: Nhầm âm は của chữ 把 thành ほ.",
                "C": "ほうあく: Kéo dài trường âm sai quy tắc."
            }
        ),
        (
            "N2_05_M1_04",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "提出期限を過ぎても連絡のない取引先に対して、支払いの【催促】を行った。",
            "さいそく",
            [("A", "さいそっ"), ("B", "さいそく"), ("C", "せいそく"), ("D", "しゅくそく")],
            "B",
            "催促（さいそく - THÔI XÚC）: Thúc giục, hối thúc (yêu cầu thanh toán, nộp bài). Chữ 催 có âm on là さい, chữ 促 có âm on là そく.",
            {
                "A": "さいそっ: Âm ngắt cụt không tồn tại trong tiếng Nhật chuẩn cho từ này.",
                "C": "せいそく: Nhầm sang 生息 (せいそく - sinh sống) hoặc 正則 (せいそく).",
                "D": "しゅくそく: Sai hoàn toàn âm đầu さい thành しゅく."
            }
        ),
        (
            "N2_05_M1_05",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "この短編小説には、著者の波乱に満ちた半生と思索が【凝縮】されている。",
            "ぎょうしゅく",
            [("A", "こんしゅく"), ("B", "ぎょうそく"), ("C", "ぎょうしゅく"), ("D", "こうしゅく")],
            "C",
            "凝縮（ぎょうしゅく - NGƯNG SÚC）: Cô đọng, ngưng tụ, dồn nén tinh hoa tư tưởng. Chữ 凝 có âm on là ぎょう, chữ 縮 có âm on là しゅく.",
            {
                "A": "こんしゅく: Nhầm âm ぎょう thành こん.",
                "B": "ぎょうそく: Nhầm âm しゅく thành そく.",
                "D": "こうしゅく: Thiếu âm ngắt và biến âm sai."
            }
        )
    ]

    for qid, tid, cat, stem, tgt, opts, ans, exp, dist in m1_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Language Knowledge",
            "category": cat,
            "stem": stem,
            "targetWord": tgt,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 2: 表記 (Orthography - 5 items)
    # =========================================================================
    m2_raw = [
        (
            "N2_05_M2_01",
            "N2-MO-ORTH",
            "Mondai 2: 表記",
            "少子高齢化の急速な進展により、地方都市の経済は【すいたい】の一途をたどっている。",
            "すいたい",
            [("A", "衰態"), ("B", "衰退"), ("C", "粋退"), ("D", "遂退")],
            "B",
            "衰退（すいたい - SUY THOÁI）: Suy thoái, tàn lụi, sa sút. Chữ 衰 (suy yếu) kết hợp với chữ 退 (thoái lui).",
            {
                "A": "衰態: Chữ 態 mang nghĩa trạng thái/thái độ, không tạo thành từ vựng chỉ sự suy giảm kinh tế.",
                "C": "粋退: Chữ 粋 mang nghĩa tinh tế/thuần khiết, sai ngữ nghĩa.",
                "D": "遂退: Chữ 遂 mang nghĩa hoàn thành/thực hiện (như 未遂), sai tự dạng."
            }
        ),
        (
            "N2_05_M2_02",
            "N2-MO-ORTH",
            "Mondai 2: 表記",
            "市民に対して、非常時の備えとして飲料水や食料の備蓄を【うながす】ポスターが貼られた。",
            "うながす",
            [("A", "催す"), ("B", "迫る"), ("C", "励す"), ("D", "促す")],
            "D",
            "促す（うながす - XÚC）: Khuyến khích, thúc đẩy, nhắc nhở ai đó thực hiện hành động cần thiết.",
            {
                "A": "催す: Đọc là もよおす (tổ chức sự kiện hoặc cảm thấy buồn nôn/buồn ngủ).",
                "B": "迫る: Đọc là せまる (tiến sát tới, dồn ép, cận kề kỳ hạn).",
                "C": "励す: Chữ 励 có động từ là 励ます (はげます - cổ vũ, động viên)."
            }
        ),
        (
            "N2_05_M2_03",
            "N2-MO-ORTH",
            "Mondai 2: 表記",
            "工場からの有害物質流出事故により、近隣住民に対して十分な【ほしょう】が行われた。",
            "ほしょう",
            [("A", "補償"), ("B", "保障"), ("C", "保証"), ("D", "補正")],
            "A",
            "補償（ほしょう - BỔ THƯỜNG）: Bồi thường thiệt hại về vật chất hoặc sức khỏe do tổn thất gây ra.",
            {
                "B": "保障: Đọc là ほしょう (BẢO CHƯỚNG - đảm bảo an ninh, quyền lợi xã hội, như 社会保障).",
                "C": "保証: Đọc là ほしょう (BẢO CHỨNG - bảo hành sản phẩm, bảo lãnh người, như 保証人).",
                "D": "補正: Đọc là ほせい (BỔ CHÍNH - chỉnh sửa, bù đắp sai số)."
            }
        ),
        (
            "N2_05_M2_04",
            "N2-MO-ORTH",
            "Mondai 2: 表記",
            "出張先での業務が長引き、現地のホテルにさらに3日間【たいざい】することになった。",
            "たいざい",
            [("A", "帯在"), ("B", "待在"), ("C", "滞在"), ("D", "滞存")],
            "C",
            "滞在（たいざい - TRỆ TẠI）: Lưu trú, ở lại tạm thời tại một nơi xa nhà.",
            {
                "A": "帯在: Chữ 帯 mang nghĩa dải đai/mang theo (như 携帯), sai tự dạng.",
                "B": "待在: Chữ 待 mang nghĩa chờ đợi, không tạo thành từ vựng này.",
                "D": "滞存: Chữ 存 mang nghĩa tồn tại, không đúng chữ 在 (ở tại)."
            }
        ),
        (
            "N2_05_M2_05",
            "N2-MO-ORTH",
            "Mondai 2: 表記",
            "彼は契約内容の不当性を理由に、契約書への署名をきっぱりと【こばんだ】。",
            "こばんだ",
            [("A", "阻んだ"), ("B", "拒んだ"), ("C", "排んだ"), ("D", "否んだ")],
            "B",
            "拒む（こばむ - CỰ）: Cự tuyệt, kiên quyết từ chối yêu cầu hoặc hành động của đối phương.",
            {
                "A": "阻んだ: Đọc là はばんだ (TRỞ - ngăn cản, cản trở bước tiến).",
                "C": "排んだ: Chữ 排 không có dạng động từ độc lập こばむ (thường đọc はい trong 排除).",
                "D": "否んだ: Đọc là いなんだ (PHỦ - từ chối nhưng ít dùng phổ biến bằng 拒む trong ngữ cảnh hợp đồng)."
            }
        )
    ]

    for qid, tid, cat, stem, tgt, opts, ans, exp, dist in m2_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Language Knowledge",
            "category": cat,
            "stem": stem,
            "targetWord": tgt,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 3: 語形成 (Word Formation - 5 items)
    # =========================================================================
    m3_raw = [
        (
            "N2_05_M3_01",
            "N2-VOC-FORM",
            "Mondai 3: 語形成",
            "現代社会が抱える（　　）問題を解決するためには、国際的な連携が不可欠である。",
            [("A", "諸"), ("B", "各"), ("C", "多"), ("D", "連")],
            "A",
            "諸〜（しょ〜 - CHƯ）: Tiền tố đứng trước danh từ để chỉ 'nhiều, các loại vấn đề khác nhau': 諸問題 (các vấn đề), 諸事情 (các lý do).",
            {
                "B": "各〜: Chỉ từng cá thể riêng rẽ (như 各国 - mỗi quốc gia, 各自 - mỗi người).",
                "C": "多〜: Thường ghép thành từ Hán tự có sẵn như 多目的, 多方面, không ghép thành 多問題.",
                "D": "連〜: Thường chỉ sự nối tiếp liên tục như 連休, 連続, không ghép thành 連問題."
            }
        ),
        (
            "N2_05_M3_02",
            "N2-VOC-FORM",
            "Mondai 3: 語形成",
            "新幹線の延伸に伴い、東京からの日帰り（　　）が大幅に拡大した。",
            [("A", "界"), ("B", "帯"), ("C", "圏"), ("D", "域")],
            "C",
            "〜圏（〜けん - QUYỂN）: Hậu tố chỉ phạm vi không gian, khu vực hoạt động: 日帰り圏 (phạm vi đi về trong ngày), 首都圏 (vùng thủ đô).",
            {
                "A": "界: Thường chỉ giới xã hội hoặc lĩnh vực ngành nghề (như 芸能界, 経済界).",
                "B": "帯: Thường chỉ vành đai địa lý trải dài (như 時間帯, 火山帯).",
                "D": "域: Thường dùng trong 地域, 区域, không kết hợp trực tiếp thành 日帰り域."
            }
        ),
        (
            "N2_05_M3_03",
            "N2-VOC-FORM",
            "Mondai 3: 語形成",
            "今期の決算発表によると、当社の（　　）売上高は過去最高を記録した。",
            [("A", "全"), ("B", "総"), ("C", "丸"), ("D", "満")],
            "B",
            "総〜（そう〜 - TỔNG）: Tiền tố chỉ tổng thể toàn bộ gộp lại: 総売上高 (tổng doanh thu), 総人口 (tổng dân số).",
            {
                "A": "全〜: Thường chỉ toàn vẹn tất cả thành viên hoặc phạm vi (như 全世界, 全校, 全社員).",
                "C": "丸〜: Thường chỉ trọn vẹn thời gian hoặc hình khối (như 丸一日, 丸三年).",
                "D": "満〜: Thường chỉ tròn độ tuổi hoặc sức chứa (như 満席, 満20歳)."
            }
        ),
        (
            "N2_05_M3_04",
            "N2-VOC-FORM",
            "Mondai 3: 語形成",
            "長引く不況の影響で、多くのベンチャー企業が資金（　　）に陥っている。",
            [("A", "苦"), ("B", "害"), ("C", "損"), ("D", "難")],
            "D",
            "〜難（〜なん - NẠN）: Hậu tố chỉ tình trạng khó khăn, khan hiếm: 資金難 (nạn khan hiếm vốn), 人手難 (thiếu hụt nhân lực).",
            {
                "A": "苦: Thường dùng trong 資金繰りの苦労, ít khi ghép thành từ cụm danh từ chuẩn 資金苦 trong văn bản kinh tế.",
                "B": "害: Chỉ thiệt hại, nguy hại (như 公害, 水害).",
                "C": "損: Chỉ sự thua lỗ, tổn thất tài chính."
            }
        ),
        (
            "N2_05_M3_05",
            "N2-VOC-FORM",
            "Mondai 3: 語形成",
            "このカフェは伝統的な日本家屋を改装した、和（　　）の落ち着いた空間が魅力だ。",
            [("A", "風"), ("B", "式"), ("C", "流"), ("D", "様")],
            "A",
            "〜風（〜ふう - PHONG）: Hậu tố chỉ phong cách, dáng dấp, hơi hướng mỹ thuật: 和風 (phong cách Nhật), 洋風 (phong cách phương Tây).",
            {
                "B": "式: Thường chỉ phương thức, hình thức cơ chế (như 日本式, 西洋式).",
                "C": "流: Thường chỉ trường phái nghệ thuật, phong cách cá nhân (như 自己流, 我流).",
                "D": "様: Thường chỉ kiểu cách dáng vẻ bên ngoài (như 模様, 様式)."
            }
        )
    ]

    for qid, tid, cat, stem, opts, ans, exp, dist in m3_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Language Knowledge",
            "category": cat,
            "stem": stem,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 4: 文脈規定 (Context Vocabulary - 7 items)
    # =========================================================================
    m4_raw = [
        (
            "N2_05_M4_01",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "ビッグデータの解析には、（　　）な計算能力を持つ高性能サーバーが欠かせない。",
            [("A", "重大"), ("B", "膨大"), ("C", "壮大"), ("D", "極大")],
            "B",
            "膨大（ぼうだい - BÀNH ĐẠI）: Khổng lồ, đồ sộ (thường dùng bổ nghĩa cho số liệu, dữ liệu, năng lực tính toán).",
            {
                "A": "重大: Nghiêm trọng, trọng đại (thường đi với 重大な責任, 重大な過失).",
                "C": "壮大: Tráng lệ, hùng vĩ (thường đi với 壮大な計画, 壮大なスケール).",
                "D": "極大: Cực đại (thuật ngữ toán học thuần túy, không dùng trong văn cảnh năng lực máy tính tự nhiên)."
            }
        ),
        (
            "N2_05_M4_02",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "外国語を学ぶ際は、単語の意味だけでなく微妙な言葉の（　　）を感じ取ることが大切だ。",
            [("A", "アクセント"), ("B", "リズム"), ("C", "テンポ"), ("D", "ニュアンス")],
            "D",
            "ニュアンス (nuance): Sắc thái ý nghĩa tinh tế, hàm ý cảm xúc ngầm ẩn trong ngôn từ mà từ điển không giải thích hết.",
            {
                "A": "アクセント: Trọng âm, dấu nhấn của từ.",
                "B": "リズム: Nhịp điệu, tiết tấu âm nhạc hoặc nhịp sống.",
                "C": "テンポ: Tốc độ nhịp độ diễn tiến công việc."
            }
        ),
        (
            "N2_05_M4_03",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "よく似た名前の二つの会社があるため、取引先から（　　）とクレームが入った。",
            [("A", "紛らわしい"), ("B", "煩わしい"), ("C", "目覚ましい"), ("D", "頼もしい")],
            "A",
            "紛らわしい（まぎらわしい）: Dễ gây nhầm lẫn, mập mờ, khó phân biệt giữa hai vật thể hay tên gọi.",
            {
                "B": "煩わしい（わずらわしい）: Phiền toái, rườm rà, nhức đầu về thủ tục quan hệ.",
                "C": "目覚ましい（めざましい）: Nổi bật, tiến bộ vượt bậc đáng kinh ngạc.",
                "D": "頼もしい（たのもしい）: Đáng tin cậy, vững tâm có thể nương tựa."
            }
        ),
        (
            "N2_05_M4_04",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "千載一遇のチャンスを前にして、失敗を恐れて（　　）していては成功をつかめない。",
            [("A", "奮闘"), ("B", "念願"), ("C", "躊躇"), ("D", "配慮")],
            "C",
            "躊躇（ちゅうちょ - TRÙ TRỪ）: Ngập ngừng, do dự, chần chừ không dứt khoát trước quyết định.",
            {
                "A": "奮闘（ふんとう）: Phấn đấu, chiến đấu hết mình nỗ lực.",
                "B": "念願（ねんがん）: Tâm nguyện, ước mong ấp ủ từ lâu.",
                "D": "配慮（はいりょ）: Chu đáo quan tâm, để ý chăm sóc người khác."
            }
        ),
        (
            "N2_05_M4_05",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "天候にも恵まれ、新造船の就航に向けた試運転は極めて（　　）に進んでいる。",
            [("A", "簡潔"), ("B", "順調"), ("C", "露骨"), ("D", "妥協")],
            "B",
            "順調（じゅんちょう - THUẬN ĐIỀU）: Thuận lợi, suôn sẻ, tiến triển tốt đẹp không gặp sự cố.",
            {
                "A": "簡潔: Ngắn gọn súc tích trong cách hành văn.",
                "C": "露骨: Trắng trợn, lộ liễu (thái độ tiêu cực).",
                "D": "妥協: Thỏa hiệp nhượng bộ trong tranh chấp."
            }
        ),
        (
            "N2_05_M4_06",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "どんなに念入りに推敲しても、自分一人では誤字脱字を（　　）しまいがちだ。",
            [("A", "見つめて"), ("B", "見届けて"), ("C", "見下ろして"), ("D", "見落として")],
            "D",
            "見落とす（みおとす - KIẾN LẠC）: Nhìn sót, bỏ sót lỗi sai hoặc chi tiết quan trọng trong văn bản.",
            {
                "A": "見つめる: Nhìn chằm chằm, dõi mắt quan sát.",
                "B": "見届ける: Theo dõi chứng kiến đến cùng kết cục.",
                "C": "見下ろす: Nhìn từ trên cao xuống dưới đất."
            }
        ),
        (
            "N2_05_M4_07",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "若手社員たちの積極的な提案を受け入れ、職場全体の学習（　　）が高まった。",
            [("A", "意欲"), ("B", "欲望"), ("C", "熱意"), ("D", "野心")],
            "A",
            "意欲（いよく - Ý DỤC）: Động lực, ý chí hăng hái muốn cống hiến hoặc học tập (thường kết hợp 学習意欲, 労働意欲).",
            {
                "B": "欲望: Ham muốn bản năng xác thịt hoặc lòng tham vật chất.",
                "C": "熱意: Nhiệt tình, lòng nhiệt huyết (thường đi với 熱意を持って).",
                "D": "野心: Dã tâm, tham vọng thăng tiến cá nhân."
            }
        )
    ]

    for qid, tid, cat, stem, opts, ans, exp, dist in m4_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Language Knowledge",
            "category": cat,
            "stem": stem,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 5: 言い換え類義 (Paraphrases/Synonyms - 5 items)
    # =========================================================================
    m5_raw = [
        (
            "N2_05_M5_01",
            "N2-VOC-SYN",
            "Mondai 5: 言い換え類義",
            "新製品の開発作業は、【おおむね】予定通りに進展している。",
            "おおむね",
            [("A", "まったく"), ("B", "めったに"), ("C", "だいたい"), ("D", "ようやく")],
            "C",
            "おおむね（概ね）: Nhìn chung, đại để, hầu như gần hết = だいたい.",
            {
                "A": "まったく: Hoàn toàn (đi với phủ định là hoàn toàn không).",
                "B": "めったに: Hiếm khi (đi kèm thể phủ định).",
                "D": "ようやく: Cuối cùng thì (sau bao vất vả chờ đợi)."
            }
        ),
        (
            "N2_05_M5_02",
            "N2-VOC-SYN",
            "Mondai 5: 言い換え類義",
            "インターネットの普及により、最新の流行は【たちまち】世界中に拡散する。",
            "たちまち",
            [("A", "すぐに"), ("B", "徐々に"), ("C", "次々に"), ("D", "時々")],
            "A",
            "たちまち（忽ち）: Ngay lập tức, trong chớp mắt, thoắt cái = すぐに.",
            {
                "B": "徐々に: Từ từ, dần dần từng bước.",
                "C": "次々に: Lần lượt liên tiếp hết cái này đến cái khác.",
                "D": "時々: Thỉnh thoảng, đôi khi."
            }
        ),
        (
            "N2_05_M5_03",
            "N2-VOC-SYN",
            "Mondai 5: 言い換え類義",
            "難航していた事件の捜査だったが、防犯カメラの映像が有力な【手がかり】となった。",
            "手がかり",
            [("A", "証拠"), ("B", "結論"), ("C", "目的"), ("D", "ヒント")],
            "D",
            "手がかり（てがかり）: Manh mối, dấu vết gợi ý dẫn tới lời giải = ヒント / 糸口.",
            {
                "A": "証拠: Bằng chứng xác thực không thể chối cãi (thường là kết quả chứng minh, rộng hơn手がかり).",
                "B": "結論: Kết luận chung cuộc.",
                "C": "目的: Mục tiêu, mục đích nhắm tới."
            }
        ),
        (
            "N2_05_M5_04",
            "N2-VOC-SYN",
            "Mondai 5: 言い換え類義",
            "顧客第一の精神を常に【念頭に置いて】、日々の営業活動を行っている。",
            "念頭に置いて",
            [("A", "深く後悔して"), ("B", "いつも意識して"), ("C", "無理に我慢して"), ("D", "他人に任せて")],
            "B",
            "念頭に置く（ねんとうにおく）: Luôn khắc ghi trong tâm trí, luôn ý thức và chú tâm đến = いつも意識して.",
            {
                "A": "深く後悔して: Hối hận sâu sắc vì sai lầm trong quá khứ.",
                "C": "無理に我慢して: Miễn cưỡng chịu đựng nhẫn nhịn.",
                "D": "他人に任せて: Giao phó cho người khác làm."
            }
        ),
        (
            "N2_05_M5_05",
            "N2-VOC-SYN",
            "Mondai 5: 言い換え類義",
            "パソコンが突然フリーズしてデータが消えてしまい、私には【お手上げ】だ。",
            "お手上げ",
            [("A", "とても満足だ"), ("B", "大したことない"), ("C", "どうすることもできない"), ("D", "非常に幸運だ")],
            "C",
            "お手上げ（おてあげ）: Bó tay, bất lực hoàn toàn, không còn cách nào cứu vãn = どうすることもできない.",
            {
                "A": "とても満足だ: Rất hài lòng mãn nguyện (ngược hẳn nghĩa thất bại bất lực).",
                "B": "大したことない: Không có gì to tát đâu.",
                "D": "非常に幸運だ: Vô cùng may mắn."
            }
        )
    ]

    for qid, tid, cat, stem, tgt, opts, ans, exp, dist in m5_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Language Knowledge",
            "category": cat,
            "stem": stem,
            "targetWord": tgt,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 6: 用法 (Usage - 5 items)
    # =========================================================================
    m6_raw = [
        (
            "N2_05_M6_01",
            "N2-VOC-USE",
            "Mondai 6: 用法",
            "「妥協」の使い方が最も適切なものを選びなさい。",
            "妥協",
            [
                ("A", "毎朝欠かさずジョギングをして、健康管理を妥協している。"),
                ("B", "彼女は絵画の才能に妥協して、個展を開催した。"),
                ("C", "激しい雨で川の水位が妥協し、住民に避難指示が出た。"),
                ("D", "労使間の交渉はお互いに歩み寄り、ようやく妥協点を見出すことができた。")
            ],
            "D",
            "妥協（だきょう - THỎA HIỆP）: Nhượng bộ đôi bên để đi tới điểm chung trong đàm phán mâu thuẫn. Câu D dùng đúng mẫu 妥協点を見出す (tìm ra điểm thỏa hiệp).",
            {
                "A": "Tập thể dục duy trì sức khỏe phải dùng 徹底する hoặc 励む, không dùng 妥協.",
                "B": "Dựa vào tài năng để mở triển lãm dùng 発揮する hoặc 生かす, không dùng 妥協.",
                "C": "Mực nước sông dâng cao dùng 上昇する, 妥協 không dùng cho hiện tượng tự nhiên."
            }
        ),
        (
            "N2_05_M6_02",
            "N2-VOC-USE",
            "Mondai 6: 用法",
            "「乏しい」の使い方が最も適切なものを選びなさい。",
            "乏しい",
            [
                ("A", "春の陽気に包まれて、花壇には色とりどりの乏しい花が咲いている。"),
                ("B", "彼は知識や経験が乏しいにもかかわらず、困難な課題に果敢に挑戦した。"),
                ("C", "今週は仕事が一段落したので、スケジュールが乏しくて退屈だ。"),
                ("D", "最新のスマートフォンの画面はとても乏しくて見やすい。")
            ],
            "B",
            "乏しい（とぼしい）: Thiếu thốn, nghèo nàn, ít ỏi (dùng cho tri thức, kinh nghiệm, tài nguyên: 経験が乏しい, 資源が乏しい). Câu B dùng hoàn toàn chính xác.",
            {
                "A": "Hoa nở rực rỡ phong phú dùng 鮮やかな hoặc 豊かな, ngược nghĩa với 乏しい.",
                "C": "Lịch trình trống rỗi dùng 空いている hoặc 余裕がある, không dùng 乏しい.",
                "D": "Màn hình rõ nét dễ nhìn dùng 鮮明な, không thể dùng 乏しい."
            }
        ),
        (
            "N2_05_M6_03",
            "N2-VOC-USE",
            "Mondai 6: 用法",
            "「念願」の使い方が最も適切なものを選びなさい。",
            "念願",
            [
                ("A", "10年間の努力が実を結び、ついに念願の自分の店を構えることができた。"),
                ("B", "天候の念願により、明日の遠足は中止とさせていただきます。"),
                ("C", "この電卓は計算の念願が速く、実務で非常に重宝している。"),
                ("D", "突然の雷の音に驚いて、飼い犬が念願そうに震え出した。")
            ],
            "A",
            "念願（ねんがん - NIỆM NGUYỆN）: Tâm nguyện bấy lâu nay, ước muốn ấp ủ qua nhiều năm (念願の〜). Câu A dùng chuẩn xác với tâm nguyện mở cửa hàng riêng sau 10 năm.",
            {
                "B": "Do thời tiết xấu dùng 天候の悪化 hoặc 都合, không dùng 念願.",
                "C": "Tốc độ xử lý tính toán nhanh dùng 処理速度, không dùng 念願.",
                "D": "Chó run rẩy vì sợ hãi dùng 恐ろしそうに hoặc 不安そうに, không dùng 念願."
            }
        ),
        (
            "N2_05_M6_04",
            "N2-VOC-USE",
            "Mondai 6: 用法",
            "「露骨」の使い方が最も適切なものを選びなさい。",
            "露骨",
            [
                ("A", "先生の分かりやすい説明のおかげで、数学の定理が露骨に理解できた。"),
                ("B", "彼女の料理は素材の持ち味が露骨に引き出されていて美味しい。"),
                ("C", "自分の思い通りにならないと、彼はすぐに露骨に嫌な顔をする。"),
                ("D", "公園のベンチで風に吹かれながら、露骨な午後をのんびり過ごした。")
            ],
            "C",
            "露骨（ろこつ - LỘ CỐT）: Lộ liễu, không chút che đậy, trắng trợn (biểu hiện cảm xúc bất mãn, ganh ghét ra mặt: 露骨に嫌な顔をする). Câu C dùng hoàn toàn chính xác.",
            {
                "A": "Hiểu rõ ràng minh bạch dùng はっきりと hoặc よく, không dùng 露骨.",
                "B": "Tôn vinh hương vị tự nhiên của nguyên liệu dùng 見事に, không dùng 露骨.",
                "D": "Buổi chiều êm ả thảnh thơi dùng 穏やかな, không dùng 露骨."
            }
        ),
        (
            "N2_05_M6_05",
            "N2-VOC-USE",
            "Mondai 6: 用法",
            "「充当」の使い方が最も適切なものを選びなさい。",
            "充当",
            [
                ("A", "彼は体力を充当するために、毎朝栄養ドリンクを飲んでいる。"),
                ("B", "国から支給された特別助成金は、全額が新施設の建設費用に充当された。"),
                ("C", "部屋の窓を大きく開けて、外の新鮮な空気を部屋いっぱいに充当した。"),
                ("D", "友人の結婚式に招待されたので、お祝いのメッセージを充当した。")
            ],
            "B",
            "充当（じゅうとう - SUNG ĐƯƠNG）: Phân bổ, trích tiền hoặc tài nguyên vào một mục đích chi tiêu cụ thể (費用に充当する). Câu B dùng chuẩn xác.",
            {
                "A": "Bồi bổ thể lực dùng 回復する hoặc つける, không dùng 充当.",
                "C": "Làm ngập tràn không khí tươi mới dùng 満たした hoặc 取り入れた, không dùng 充当.",
                "D": "Gửi lời chúc mừng đám cưới dùng 送った hoặc 伝えた, không dùng 充当."
            }
        )
    ]

    for qid, tid, cat, stem, tgt, opts, ans, exp, dist in m6_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Language Knowledge",
            "category": cat,
            "stem": stem,
            "targetWord": tgt,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 7: 文法形式 (Grammar Forms - 12 items)
    # =========================================================================
    m7_raw = [
        (
            "N2_05_M7_01",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "あんなに難解な専門書の内容を、たった一人で一日で理解できる（　　）。",
            [("A", "っこない"), ("B", "に違いない"), ("C", "はずだ"), ("D", "かねない")],
            "A",
            "〜っこない: Tuyệt đối không thể, chắc chắn không thể làm nổi (phủ định tuyệt đối khả năng của động từ thể ます bỏ ます).",
            {
                "B": "に違いない: Chắc chắn là... (khẳng định độ chắc chắn cao, mâu thuẫn với ý bất khả thi).",
                "C": "はずだ: Đương nhiên là sẽ... (kỳ vọng tích cực, không hợp lý).",
                "D": "かねない: Có nguy cơ dẫn tới kết quả xấu."
            }
        ),
        (
            "N2_05_M7_02",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "記録的な台風の直撃を受け、主催者は野外フェスティバルの開催中止を（　　）。",
            [("A", "余儀なくさせた"), ("B", "よぎりなくした"), ("C", "余儀なくされた"), ("D", "余儀なくある")],
            "C",
            "〜を余儀なくされた（〜をよぎなくされた）: Bị buộc phải rơi vào tình thế không mong muốn do hoàn cảnh ngoại cảnh khách quan bắt buộc.",
            {
                "A": "余儀なくさせた: Mang nghĩa chủ động bắt ai đó phải chịu, chủ ngữ ở đây là người tổ chức bị hoàn cảnh ép buộc nên phải dùng dạng bị động 余儀なくされた.",
                "B": "よぎりなくした: Sai cách đọc kanji và cấu trúc ngữ pháp.",
                "D": "余儀なくある: Cấu trúc ngữ pháp sai dạng."
            }
        ),
        (
            "N2_05_M7_03",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "当プロジェクトは、当初策定された環境保護ガイドラインに（　　）厳格に実施される。",
            [("A", "反して"), ("B", "沿って"), ("C", "めぐって"), ("D", "こたえて")],
            "B",
            "〜に沿って（〜にそって）: Tuân thủ theo, men theo định hướng, đường lối, quy tắc định sẵn (theo đúng hướng dẫn bảo vệ môi trường).",
            {
                "A": "反して: Trái ngược lại với quy tắc.",
                "C": "めぐって: Xoay quanh tranh chấp/bàn cãi về một chủ đề.",
                "D": "こたえて: Đáp lại kỳ vọng/nhu cầu của mọi người."
            }
        ),
        (
            "N2_05_M7_04",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "これほどの国家的事業の成功は、全国民の一致団結した協力（　　）語ることはできない。",
            [("A", "において"), ("B", "に関して"), ("C", "を通じて"), ("D", "ぬきでは")],
            "D",
            "〜ぬきでは（〜抜きでは）: Nếu thiếu đi, nếu không có... thì không thể thành (thường đi với vế sau mang tính phủ định '語ることはできない').",
            {
                "A": "において: Tại địa điểm/trong bối cảnh lĩnh vực.",
                "B": "に関して: Liên quan đến chủ đề thông tin.",
                "C": "を通じて: Thông qua suốt cả quá trình."
            }
        ),
        (
            "N2_05_M7_05",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "小さな機器の故障であっても放置しておくと、工場全体の操業停止を招き（　　）。",
            [("A", "かねない"), ("B", "かねる"), ("C", "そうもない"), ("D", "得ない")],
            "A",
            "〜かねない: Có khả năng, rất có nguy cơ dẫn tới hậu quả tiêu cực khôn lường (chiếu theo đà hiện tại).",
            {
                "B": "かねる: Khó lòng làm được do tâm lý/vị thế (như 賛成しかねます).",
                "C": "そうもない: Rất khó có khả năng xảy ra.",
                "D": "得ない: Tuyệt đối không thể xảy ra về mặt logic lý tính."
            }
        ),
        (
            "N2_05_M7_06",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "海外旅行に出かける際は、万一の病気や盗難に備えて保険に加入して（　　）。",
            [("A", "おくわけがない"), ("B", "おくほかない"), ("C", "おくに越したことはない"), ("D", "おかないつもりだ")],
            "C",
            "〜に越したことはない: Được như vậy thì tốt nhất, là phương án an toàn nhất không bao giờ thừa (mua bảo hiểm trước khi đi nước ngoài là cẩn thận nhất).",
            {
                "A": "おくわけがない: Tuyệt đối không có lý do gì phải mua trước (trái lẽ thường).",
                "B": "おくほかない: Chỉ còn cách mua trước (mang tính ép buộc cùng đường, không phù hợp lời khuyên cẩn tắc vô ưu).",
                "D": "おかないつもりだ: Dự định không mua (sai ngữ cảnh phòng ngừa rủi ro)."
            }
        ),
        (
            "N2_05_M7_07",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "信頼してくれた恩師の顔に泥を塗るような不正行為は、断じてする（　　）と心に誓った。",
            [("A", "べきだ"), ("B", "まい"), ("C", "ものか"), ("D", "はずだ")],
            "B",
            "〜まい: Quyết không làm... (ý chí phủ định đanh thép của ngôi thứ nhất, thường đi kèm と心に誓った). Động từ する chia thành するまい hoặc すまい.",
            {
                "A": "べきだ: Nên làm gì (khuyên bảo, ngược nghĩa hoàn toàn).",
                "C": "ものか: Tuyệt đối không đời nào (khẩu ngữ phản bác đối thoại trực tiếp, không đi thành するものかと心に誓った).",
                "D": "はずだ: Đương nhiên là."
            }
        ),
        (
            "N2_05_M7_08",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "故郷の美しい山河の風景を目に（　　）、幼い頃の懐かしい思い出が胸に迫ってくる。",
            [("A", "かけると"), ("B", "際して"), ("C", "限って"), ("D", "するにつけ")],
            "D",
            "〜につけ: Mỗi lần... lại cảm thấy (thường đi với các động từ liên quan đến cảm xúc/nhận thức: 目にするにつけ, 聞くにつけ).",
            {
                "A": "かけると: Đang làm dở hoặc suýt nữa (như 言いかける).",
                "B": "際して: Nhân dịp thời điểm bắt đầu một sự kiện lớn.",
                "C": "限って: Đúng vào lúc không may hoặc riêng đối tượng đặc biệt."
            }
        ),
        (
            "N2_05_M7_09",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "東京にいらっしゃる（　　）には、ぜひ弊社オフィスにもお立ち寄りください。",
            [("A", "折"), ("B", "末"), ("C", "節"), ("D", "際")],
            "A",
            "〜折（〜おり）: Nhân dịp, vào cơ hội thuận tiện (kính ngữ trang trọng khi mời khách: 東京にいらっしゃる折には).",
            {
                "B": "末（すえ）: Sau một hồi đắn đo suy nghĩ (như 悩んだ末).",
                "C": "節: Thường dùng trong dạng 節は nhưng văn cảnh lịch thiệp mời ghé thăm chuẩn nhất là 折には.",
                "D": "際: Có thể dùng 際には nhưng 折 mang sắc thái thanh lịch, ấm áp hơn trong giao tiếp xã giao."
            }
        ),
        (
            "N2_05_M7_10",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "住民アンケートで寄せられた切実な意見を（　　）、新しい公共交通網の再編案が作成された。",
            [("A", "問わず"), ("B", "よそに"), ("C", "踏まえて"), ("D", "限らず")],
            "C",
            "〜を踏まえて（〜をふまえて）: Dựa trên cơ sở cân nhắc kỹ lưỡng dữ liệu, ý kiến thực tế (dựa trên các phản hồi từ khảo sát người dân).",
            {
                "A": "問わず: Bất kể không phân biệt.",
                "B": "よそに: Mặc kệ phớt lờ ý kiến người khác.",
                "D": "限らず: Không chỉ giới hạn ở."
            }
        ),
        (
            "N2_05_M7_11",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "10年前に大学を卒業（　　）、母校のキャンパスを訪れる機会が一度もなかった。",
            [("A", "したきり"), ("B", "して以来"), ("C", "したところで"), ("D", "する反面")],
            "B",
            "〜て以来: Kể từ sau khi... cho đến tận bây giờ (kể từ khi tốt nghiệp 10 năm trước tới nay chưa từng ghé thăm trường cũ).",
            {
                "A": "したきり: Thường đi với trạng thái kéo dài không lặp lại (như 連絡がない), nhưng cấu trúc chuẩn chỉ mốc thời gian lịch sử kết hợp hiện tại hoàn thành là 〜て以来.",
                "C": "したところで: Dù cho có làm thế đi chăng nữa thì cũng vô ích.",
                "D": "する反面: Trái ngược lại với mặt tốt."
            }
        ),
        (
            "N2_05_M7_12",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "今回の大ヒット商品は、顧客の潜在的な不満を徹底的に掘り下げた努力の成果（　　）。",
            [("A", "にすぎない"), ("B", "どころではない"), ("C", "わけがない"), ("D", "にほかならない")],
            "D",
            "〜にほかならない: Chính là, không gì khác ngoài... (khẳng định bản chất nguyên nhân duy nhất dẫn đến thành công).",
            {
                "A": "にすぎない: Chỉ là... chẳng qua chỉ là (hạ thấp tầm quan trọng).",
                "B": "どころではない: Không phải lúc để làm gì.",
                "C": "わけがない: Tuyệt đối không thể nào có chuyện đó."
            }
        )
    ]

    for qid, tid, cat, stem, opts, ans, exp, dist in m7_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Language Knowledge",
            "category": cat,
            "stem": stem,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 8: 文の組み立て ★ (Sentence Composition - 5 items)
    # Rigorously verified mathematically across all 24 permutations (unique solution)
    # =========================================================================
    m8_raw = [
        (
            "N2_05_M8_01",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "地球温暖化を（　　）（　　） ★ （　　）不可欠である。",
            [
                ("A", "市民一人ひとりの"),
                ("B", "防止するにあたって、"),
                ("C", "企業だけでなく"),
                ("D", "地道な協力も")
            ],
            "A",
            "Thứ tự đúng: B -> C -> A -> D (防止するにあたって、 企業だけでなく 市民一人ひとりの 地道な協力も). Câu hoàn chỉnh: 地球温暖化を防止するにあたって、企業だけでなく市民一人ひとりの地道な協力も不可欠である。 Cấu trúc: 〜にあたって (khi bắt đầu/tiến hành việc lớn). [B 防止するにあたって、] đi với tân ngữ 地球温暖化を. Tiếp theo là liên kết liệt kê: [C 企業だけでなく] đi với chủ ngữ mở rộng [A 市民一人ひとりの] bổ nghĩa cho [D 地道な協力も], làm chủ ngữ cho vị ngữ 不可欠である. Vị trí ngôi sao ★ là A (市民一人ひとりの).",
            {
                "B": "[Vị trí 1] Cụm động từ kết hợp với tân ngữ 地球温暖化を.",
                "C": "[Vị trí 2] Mẫu liên kết liệt kê 〜だけでなく có dấu phẩy ngắt vế.",
                "D": "[Vị trí 4] Danh từ làm chủ ngữ đứng liền trước vị ngữ 不可欠である."
            }
        ),
        (
            "N2_05_M8_02",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "いかに科学技術が（　　）（　　） ★ （　　）決して消えない。",
            [
                ("A", "進歩しようとも、"),
                ("B", "その根底にある"),
                ("C", "人の温もりという"),
                ("D", "価値は")
            ],
            "C",
            "Thứ tự đúng: A -> B -> C -> D (進歩しようとも、 その根底にある 人の温もりという 価値は). Cấu trúc nhượng bộ いかに〜ようとも. [A 進歩しようとも、] đi với chủ ngữ 科学技術が. Tiếp theo [B その根底にある] bổ nghĩa cho [C 人の温もりという], bổ nghĩa tiếp cho chủ ngữ [D 価値は], đi liền trước vị ngữ 決して消えない. Thứ tự duy nhất: A -> B -> C -> D. Vị trí ngôi sao ★ là C (人の温もりという).",
            {
                "A": "[Vị trí 1] Cụm vị ngữ nhượng bộ いかに〜進歩しようとも、.",
                "B": "[Vị trí 2] Định ngữ bổ nghĩa cho cụm 人の温もりという価値.",
                "D": "[Vị trí 4] Danh từ làm chủ ngữ chính đứng trước phó từ 決して消えない."
            }
        ),
        (
            "N2_05_M8_03",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "長年の対立を（　　）（　　） ★ （　　）合意に達した。",
            [
                ("A", "乗り越えるべく、"),
                ("B", "双方が"),
                ("C", "粘り強く"),
                ("D", "協議を重ねた末に")
            ],
            "C",
            "Thứ tự đúng: A -> B -> C -> D (乗り越えるべく、 双方が 粘り強く 協議を重ねた末に). Cấu trúc mục đích trang trọng N2: 〜べく (để vượt qua mâu thuẫn nhiều năm). [A 乗り越えるべく、] đi liền sau tân ngữ 長年の対立を. Vế tiếp theo: [B 双方が] là chủ ngữ, [C 粘り強く] là phó từ bổ nghĩa cho [D 協議を重ねた末に], đi liền trước kết quả 合意に達した. Thứ tự duy nhất: A -> B -> C -> D. Vị trí ngôi sao ★ là C (粘り強く).",
            {
                "A": "[Vị trí 1] Cụm mục đích 〜べく đi liền sau tân ngữ 長年の対立を.",
                "B": "[Vị trí 2] Chủ ngữ 双方が của vế sau.",
                "D": "[Vị trí 4] Cụm 〜た末に đứng liền trước kết quả 合意に達した."
            }
        ),
        (
            "N2_05_M8_04",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "どんなに優れた才能が（　　）（　　） ★ （　　）大成しない。",
            [
                ("A", "あろうと、"),
                ("B", "日々の"),
                ("C", "努力なくしては"),
                ("D", "決して")
            ],
            "C",
            "Thứ tự đúng: A -> B -> C -> D (あろうと、 日々の 努力なくしては 決して). Câu hoàn chỉnh: どんなに優れた才能があろうと、日々の努力なくしては決して大成しない。 Cấu trúc: どんなに〜ようと (cho dù có... đi chăng nữa). [A あろうと、] đi với 才能が. Cấu trúc N2 tiếp theo: 〜なくしては〜ない (nếu không có thì không thể). [B 日々の] bổ nghĩa cho [C 努力なくしては], và phó từ phủ định [D 決して] đi liền trước vị ngữ 大成しない. Thứ tự duy nhất: A -> B -> C -> D. Vị trí ngôi sao ★ là C (努力なくしては).",
            {
                "A": "[Vị trí 1] Hoàn thành cấu trúc giả định nhượng bộ どんなに〜あろうと.",
                "B": "[Vị trí 2] Định ngữ bổ nghĩa cho 努力.",
                "D": "[Vị trí 4] Phó từ 決して bổ nghĩa trực tiếp cho động từ phủ định 大成しない."
            }
        ),
        (
            "N2_05_M8_05",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "新薬の開発は、（　　）（　　） ★ （　　）貢献する。",
            [
                ("A", "人々の健康増進に"),
                ("B", "経済の活性化にも"),
                ("C", "とどまらず、"),
                ("D", "大きく")
            ],
            "B",
            "Thứ tự đúng: A -> C -> B -> D (人々の健康増進に とどまらず、 経済の活性化にも 大きく). Câu hoàn chỉnh: 新薬の開発は、人々の健康増進にとどまらず、経済の活性化にも大きく貢献する。 Cấu trúc ngữ pháp N2: 〜にとどまらず (không chỉ dừng lại ở...). [A 人々の健康増進に] đi với [C とどまらず、]. Vế tiếp diễn: [B 経済の活性化にも] đi với phó từ [D 大きく] bổ nghĩa cho động từ 貢献する. Thứ tự duy nhất: A -> C -> B -> D. Vị trí ngôi sao ★ là B (経済の活性化にも).",
            {
                "A": "[Vị trí 1] Tân ngữ đi liền sau chủ ngữ 新薬の開発は.",
                "C": "[Vị trí 2] Mẫu ngữ pháp 〜にとどまらず、 có dấu phẩy.",
                "D": "[Vị trí 4] Phó từ 大きく bổ nghĩa trực tiếp cho động từ 貢献する."
            }
        )
    ]

    for qid, tid, cat, stem, opts, ans, exp, dist in m8_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Language Knowledge",
            "category": cat,
            "stem": stem,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })


    # =========================================================================
    # MONDAI 9: 文章の文法 (Text Grammar - 5 items)
    # Topic: 行動変容を促す建築デザイン（ナッジ理論の空間設計への応用）
    # =========================================================================
    p9_text = """私たちが日々利用する駅やオフィスビル、商業施設などの建築空間は、単に風雨をしのぎ人を収容するだけの物理的構造物ではない。近年、行動経済学の「ナッジ（nudge：肘でそっと突くように自発的な良い行動を促す手法）」の概念が建築設計の分野に導入され、空間そのものが人間の無意識の行動を誘導する役割を果たしている。

たとえば、健康増進のためにオフィスビルの利用者にエレベーターではなく階段を使ってもらいたいとする。（ 50 ）、従来のように「健康のために階段を使いましょう」という張り紙を掲示するだけでは、ほとんど効果が期待できない。そこで、エントランスを入ってすぐの最も目立つ明るく開放的な場所に、歩きたくなるような美しいデザインの階段を配置し、エレベーターは少し奥まった目立たない場所に設置する。そうすると、人々は強制される感覚を抱く（ 51 ）、自然と階段を選択するようになる。

（ 52 ）アプローチは、ゴミのポイ捨て防止や省エネルギーの推進など、さまざまな公共空間の課題解決に応用されつつある。重要なのは、規則で人々の行動を縛るのではなく、選択の自由を確保したまま望ましい方向へと心理的な負担なく導く点にある。

空間デザインが人々の心理や行動に与える影響は、私たちが自覚している以上に大きい。これからの建築家や都市計画家には、単なる機能性や美しさを追求する（ 53 ）、人々がより豊かで健やかに暮らせるような無意識の行動環境を設計する知恵が（ 54 ）。"""

    m9_raw = [
        (
            "N2_05_M9_01",
            "N2-GR-TXT",
            "Mondai 9: 文章の文法 (50)",
            "空欄（ 50 ）に入る最も適切なものを選びなさい。",
            [("A", "しかし"), ("B", "つまり"), ("C", "したがって"), ("D", "さらに")],
            "A",
            "Liên từ mang tính chuyển ý nghịch tiếp: đoạn trước nêu mục tiêu muốn mọi người đi cầu thang bộ, nhưng (しかし) cách dán thông báo truyền thống thì hầu như không có hiệu quả.",
            {
                "B": "つまり: Tóm lại, tức là (dùng để diễn giải tương đương, không thể hiện sự bất cập đối lập).",
                "C": "したがって: Do đó, vì vậy (chỉ kết quả thuận theo logic).",
                "D": "さらに: Hơn nữa, ngoài ra (bổ sung thông tin cùng chiều)."
            }
        ),
        (
            "N2_05_M9_02",
            "N2-GR-TXT",
            "Mondai 9: 文章の文法 (51)",
            "空欄（ 51 ）に入る最も適切なものを選びなさい。",
            [("A", "ことなく"), ("B", "ばかりに"), ("C", "うえに"), ("D", "反面")],
            "A",
            "Cấu trúc 〜ことなく (mà không hề... = 〜ないで): '人々は強制される感覚を抱くことなく、自然と階段を選択する' (Mọi người tự nhiên lựa chọn cầu thang bộ mà không hề có cảm giác bị ép buộc).",
            {
                "B": "ばかりに: Chỉ vì... mà dẫn đến kết quả tệ hại ngoài ý muốn.",
                "C": "うえに: Thêm vào đó, không những mà còn.",
                "D": "反面: Mặt khác trái ngược lại."
            }
        ),
        (
            "N2_05_M9_03",
            "N2-GR-TXT",
            "Mondai 9: 文章の文法 (52)",
            "空欄（ 52 ）に入る最も適切なものを選びなさい。",
            [("A", "あの"), ("B", "このような"), ("C", "どういう"), ("D", "どれほどの")],
            "B",
            "Chỉ thị từ nối đoạn: 'このようなアプローチ' (Cách tiếp cận như thế này) chỉ phương pháp thiết kế gợi ý hành vi (nudge) vừa được minh họa cụ thể ở đoạn trước.",
            {
                "A": "あの: Chỉ sự vật ở xa cả người nói lẫn người nghe, không dùng để quy chiếu mạch văn vừa nêu.",
                "C": "どういう: Dùng trong câu hỏi tìm hiểu bản chất (như どういう意味ですか).",
                "D": "どれほどの: Dùng chỉ mức độ số lượng không đếm xuể trong câu cảm thán hoặc nghi vấn."
            }
        ),
        (
            "N2_05_M9_04",
            "N2-GR-TXT",
            "Mondai 9: 文章の文法 (53)",
            "空欄（ 53 ）に入る最も適切なものを選びなさい。",
            [("A", "ものの"), ("B", "ばかりか"), ("C", "だけでなく"), ("D", "わりに")],
            "C",
            "Cấu trúc 〜だけでなく (không chỉ dừng lại ở... mà còn): '単なる機能性や美しさを追求するだけでなく、人々がより豊かで健やかに暮らせるような...設計する' (Không chỉ theo đuổi vẻ đẹp và công năng đơn thuần, mà còn thiết kế môi trường sống). Đáp án chính xác là C (だけでなく).",
            {
                "A": "ものの: Mặc dù... nhưng (chỉ sự đối lập, không thể hiện quan hệ mở rộng song hành).",
                "B": "ばかりか: Thường mang sắc thái tiêu cực hoặc bất ngờ tăng tiến quá mức, trong cấu trúc chuẩn khuyến nghị đi với だけでなく.",
                "D": "わりに: Dù là... nhưng mà lại (ngạc nhiên trái với mức độ)."
            }

        ),
        (
            "N2_05_M9_05",
            "N2-GR-TXT",
            "Mondai 9: 文章の文法 (54)",
            "空欄（ 54 ）に入る最も適切なものを選びなさい。",
            [("A", "求められているのではないだろうか"), ("B", "求められるべきではない"), ("C", "求められるはずがない"), ("D", "求められるにすぎない")],
            "A",
            "Dạng câu kết mang tính khẳng định ý kiến cá nhân một cách khiêm tốn, lịch thiệp và sâu sắc của tác giả: 〜のではないだろうか (Phải chăng là đang đòi hỏi trí tuệ của các kiến trúc sư...).",
            {
                "B": "求められるべきではない: Tuyệt đối không nên đòi hỏi (ngược hoàn toàn với thông điệp bài viết).",
                "C": "求められるはずがない: Làm sao mà có chuyện đòi hỏi được (phủ định vô lý).",
                "D": "求められるにすぎない: Chẳng qua chỉ là bị đòi hỏi (hạ thấp tầm quan trọng)."
            }
        )
    ]

    for qid, tid, cat, stem, opts, ans, exp, dist in m9_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Language Knowledge",
            "category": cat,
            "stem": stem,
            "contextPassage": p9_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 10: 短文読解 (Short Passages - 5 items)
    # =========================================================================
    m10_data = [
        (
            "N2_05_M10_01",
            "在宅勤務における通信手当と申請ルール",
            """社員各位
テレワークの恒常化に伴い、来月より在宅勤務時の通信費補助として「リモートワーク手当（月額5,000円）」を一律支給することとなりました。
なお、業務で使用するインターネット回線につきましては、セキュリティ確保のため、個人の領収書提出による個別精算は廃止し、今後は本手当に一本化いたします。また、通信速度やセキュリティ要件（暗号化WPA3対応ルーターの利用等）が会社の基準を満たしているか、年1回の自己点検チェックシートの提出が義務付けられます。期日までに提出がない場合、手当の支給が一時停止されることがありますのでご注意ください。""",
            "この通知で社員に義務付けられていることは何か。",
            [
                ("A", "セキュリティ基準を満たしているか点検シートを年に一度提出すること。"),
                ("B", "毎月のインターネット料金の領収書を経理部に提出すること。"),
                ("C", "通信手当を受け取るために、会社の指定する回線業者と新規契約すること。"),
                ("D", "在宅勤務を行う日数を事前に上司へ申請して許可を得ること。")
            ],
            "A",
            "Thông báo nêu rõ: hủy bỏ việc nộp hóa đơn thanh toán riêng lẻ và bắt buộc mỗi năm một lần nộp bảng tự kiểm tra bảo mật ('年1回の自己点検チェックシートの提出が義務付けられます').",
            {
                "B": "Nộp hóa đơn hàng tháng đã bị bãi bỏ hoàn toàn ('個人の領収書提出による個別精算は廃止').",
                "C": "Không bắt buộc ký hợp đồng với nhà mạng do công ty chỉ định, chỉ cần router đáp ứng chuẩn WPA3.",
                "D": "Thông báo không đề cập đến việc phải xin phép số ngày làm việc tại nhà."
            }
        ),
        (
            "N2_05_M10_02",
            "マルチタスクの落とし穴とシングルタスクの重要性",
            """多くの現代人は、メールを返信しながらオンライン会議に参加し、合間に資料を作成するという「マルチタスク（同時並行作業）」を効率的だと信じ込んでいる。しかし、脳科学の研究によれば、人間の脳は複数の作業を同時に処理しているのではなく、注意の対象を猛スピードで切り替えているにすぎない。
この頻繁な切り替えは脳に莫大な疲労を蓄積させ、結果として集中力や判断力の低下、ミスや作業時間の増大を招く。本当に高い生産性を上げたいのであれば、一度に一つの作業にのみ深く没頭する「シングルタスク」の時間を意識的に確保すべきである。""",
            "筆者が仕事の生産性について主張していることはどれか。",
            [
                ("A", "同時に複数の作業を行うよりも、一つの作業に集中する時間を設けるほうが効率的である。"),
                ("B", "メールの返信や資料作成などの単純作業は、すべてAIに任せるべきである。"),
                ("C", "集中力を高めるためには、オンライン会議の回数をできる限り減らすべきである。"),
                ("D", "作業を素早く切り替える訓練を積むことで、脳の処理速度を向上させることができる。")
            ],
            "A",
            "Tác giả chỉ ra rằng đa nhiệm thực chất chỉ là chuyển đổi sự chú ý liên tục gây kiệt sức cho não bộ; muốn năng suất cao thực sự thì phải dành thời gian tập trung vào từng việc một (single-task).",
            {
                "B": "Tác giả không hề đề cập đến việc giao hết tác vụ cho AI.",
                "C": "Không khuyên giảm số lượng cuộc họp mà khuyên không làm việc khác trong lúc họp.",
                "D": "Tác giả phê phán việc chuyển đổi qua lại giữa các công việc, chứ không hề khuyên rèn luyện chuyển đổi nhanh."
            }
        ),
        (
            "N2_05_M10_03",
            "マンション駐輪場の一斉整理に関するお知らせ",
            """居住者の皆様へ
当マンションの駐輪場におきまして、長期間放置されたと見られる自転車が増加し、日常の利用に支障をきたしております。
つきましては、不要自転車の撤去作業を以下の要領で実施いたします。
現在駐輪場をご利用の自転車すべてに、本日より「確認用黄色テープ」を取り付けます。引き続き駐輪場をご利用される方は、11月20日（金）までにテープを取り外してください。期日を過ぎてもテープが貼られたままの自転車は放置車両とみなし、一時保管場所へ移動のうえ、1ヶ月後に処分いたします。ご理解のほどよろしくお願いいたします。""",
            "駐輪場を利用し続けたい居住者は、何をしなければならないか。",
            [
                ("A", "11月20日までに自転車に貼られた黄色いテープを自分で外すこと。"),
                ("B", "管理事務所に出向いて新しい駐輪許可証のシールを発行してもらうこと。"),
                ("C", "放置自転車の一時保管場所へ自転車を一時的に移動させること。"),
                ("D", "11月20日までに自転車の防犯登録番号を管理組合へ連絡すること。")
            ],
            "A",
            "Thông báo ghi rõ: ai tiếp tục sử dụng bãi đỗ xe thì trước ngày 20/11 phải tự mình gỡ bỏ dải băng màu vàng đã được dán lên xe ('引き続き駐輪場をご利用される方は、11月20日（金）までにテープを取り外してください').",
            {
                "B": "Không yêu cầu đến văn phòng xin cấp tem mới.",
                "C": "Khu vực lưu giữ tạm thời là nơi quản lý di chuyển các xe bị nghi bỏ rơi đến, không phải cư dân tự dắt sang.",
                "D": "Không yêu cầu nộp số đăng ký chống trộm của xe."
            }
        ),
        (
            "N2_05_M10_04",
            "信頼関係を築く「傾聴」の力",
            """他者と良好な信頼関係を築くためには、自分の主張を上手に伝えるプレゼンテーション能力よりも、相手の話に真摯に耳を傾ける「傾聴力」のほうがはるかに決定的な役割を果たす。
人は誰しも、自分の感情や考えを否定されずに受け止めてもらえたときに深い安心感を覚える。相手の言葉の表面だけをなぞって安易なアドバイスをするのではなく、相手が言葉の裏に込めた思いや背景にある事情まで共感的に想像しながら聴くこと。この「聴く姿勢」そのものが、言葉以上に雄弁に相手への敬意と信頼を伝えるのである。""",
            "この文章で筆者が「傾聴」について最も伝えたいことは何か。",
            [
                ("A", "安易に助言するのではなく、相手の感情や背景に共感して聴く姿勢が信頼を生む。"),
                ("B", "会話を円滑に進めるためには、自分の意見を相手より先に主張することが大切である。"),
                ("C", "相手の意見に論理的な誤りがあれば、その場ですぐに指摘して正すべきである。"),
                ("D", "良好な関係を保つためには、相手の話に常に同調して反論を控えるべきである。")
            ],
            "A",
            "Tác giả nhấn mạnh: không đưa ra lời khuyên hời hợt mà phải lắng nghe thấu cảm, đặt mình vào bối cảnh cảm xúc của đối phương để tạo dựng sự tôn trọng và tin cậy.",
            {
                "B": "Ngược hoàn toàn với ý bài viết (bài viết coi trọng việc lắng nghe hơn là tranh giành nói trước).",
                "C": "Tác giả khuyên không phán xét bác bỏ cảm xúc của người khác, không phải đi vạch lỗi sai logic.",
                "D": "Lắng nghe thấu cảm không đồng nghĩa với việc gió chiều nào theo chiều nấy hay giả vờ tán thành mọi lúc."
            }
        ),
        (
            "N2_05_M10_05",
            "地域社会における食品ロス削減の取り組み",
            """まだ食べられるにもかかわらず廃棄される「食品ロス」の削減に向けて、各地の自治体や飲食店で新たな試みが始まっている。
ある商店街では、閉店間近に余った惣菜やパンをスマートフォンアプリで通知し、近隣の住民が割安で購入できる仕組みを導入した。この取り組みは、店舗にとっては廃棄コストの削減と売上確保につながり、消費者にとっては手頃な価格で食品を入手できるというメリットがある。環境負荷の軽減という大義名分だけでなく、関わるすべての人に実利がある仕組みを構築することこそが、持続可能な社会づくりの鍵となる。""",
            "この文章で筆者が強調している、食品ロス削減を成功させるための要因は何か。",
            [
                ("A", "環境理念を掲げるだけでなく、参加する店舗と消費者の双方に実際の利益があること。"),
                ("B", "賞味期限が切れた食品の販売を法律によって厳しく規制すること。"),
                ("C", "飲食店に対して売れ残った食品の廃棄税を一律に課すこと。"),
                ("D", "行政からの補助金に頼り、すべての売れ残り食品を無料で配布すること。")
            ],
            "A",
            "Tác giả đúc kết bài học: không chỉ dừng ở khẩu hiệu môi trường suông mà phải xây dựng mô hình mang lại lợi ích thiết thực cho cả người bán lẫn người mua ('関わるすべての人に実利がある仕組みを構築することこそが...鍵となる').",
            {
                "B": "Không đề cập đến việc thắt chặt luật cấm bán đồ hết hạn.",
                "C": "Không hề đề xuất đánh thuế rác thải đối với nhà hàng.",
                "D": "Mô hình này là bán giảm giá mang lại doanh thu, không phải phát miễn phí dựa vào tiền trợ cấp nhà nước."
            }
        )
    ]

    for qid, title, passage, stem, opts, ans, exp, dist in m10_data:
        items.append({
            "id": qid,
            "typeId": "N2-RD-SHORT",
            "skill": "Reading",
            "category": f"Mondai 10: 短文読解 — {title}",
            "stem": stem,
            "contextPassage": passage,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 11: 中文読解 (Medium Passages - 3 passages x 3 items = 9 items)
    # =========================================================================
    # Passage 1: 「贈与の経済学」と現代社会の人間関係
    p11_1_text = """現代の資本主義社会において、私たちはあらゆるモノやサービスをお金で売買する「市場交換」を当たり前の前提として生きている。商品に値段がつけられ、対価を支払うことで取引が完了する関係は、極めて合理的で無駄がない。取引が終われば互いに何の義務も残らず、しがらみのない自由な個人として振る舞うことができるからだ。

しかし、かつての伝統的な地域社会では、近隣同士でおすそ分けをしたり、労働力を無償で貸し借りしたりする「贈与（ギフト）」の慣習が生活の基盤にあった。贈与の特徴は、受け取った側に「いつか何かをお返ししなければならない」という心理的な負債感、すなわち緩やかな義務感を生み出す点にある。この借りと返しの終わりのない循環こそが、人々の間に見えない絆を結び、相互扶助のセーフティネットを形成していたのである。

市場交換の浸透は、人々を煩わしい人間関係から解放した一方で、他者との有機的な結びつきを希薄化させ、深刻な孤独や孤立を生み出す原因にもなった。すべてをお金で解決できる社会は便利ではあるが、困ったときに利害関係を越えて助け合える関係性は育ちにくい。現代において、シェアハウスや子育ての共同支援、スキルシェアなど、非金銭的な分かち合いのコミュニティが再び注目されているのは、私たちが市場経済の合理性の向こう側に、贈与を通じた温かなつながりを本能的に求めている証拠と言えるだろう。"""

    m11_1_items = [
        (
            "N2_05_M11_01",
            "筆者によると、「市場交換」が持つ利点とは何か。",
            [
                ("A", "お金を支払って取引が完了すれば、相手に対して心理的なしがらみや義務が残らない点。"),
                ("B", "地域住民同士が互いに助け合える強力なセーフティネットを自然に形成できる点。"),
                ("C", "商品の品質や安全性が公的に保証され、トラブルが絶対に起こらない点。"),
                ("D", "お金のない人であっても、自分の労働力を提供すれば平等にモノが入手できる点。")
            ],
            "A",
            "Đoạn 1 nêu rõ: ưu điểm của trao đổi thị trường bằng tiền là giao dịch xong là xong, đôi bên không bị vướng bận ràng buộc nghĩa vụ nợ nần ân tình ('対価を支払うことで取引が完了...何の義務も残らず、しがらみのない自由な個人として振る舞うことができる').",
            {
                "B": "Mạng lưới an sinh tương trợ là ưu điểm của hình thức tặng quà/trao đổi truyền thống (贈与), không phải trao đổi thị trường bằng tiền.",
                "C": "Không hề nói thị trường bảo đảm không bao giờ xảy ra sự cố.",
                "D": "Đổi sức lao động lấy đồ là đặc tính của kinh tế tặng quà/tương trợ không dùng tiền mặt."
            }
        ),
        (
            "N2_05_M11_02",
            "「贈与」が伝統的な地域社会で果たしていた役割として、文章の説明と合致するものはどれか。",
            [
                ("A", "お返しをしなければならないという終わりのない循環が、人々の絆と支え合いを生み出していた。"),
                ("B", "金銭的な富の格差を完全に解消し、すべての住民の生活水準を均等に保っていた。"),
                ("C", "不要なモノを効率的に処分することで、環境破壊や資源の浪費を防いでいた。"),
                ("D", "外部からの侵入者を監視し、村の伝統的なルールを強制的に守らせていた。")
            ],
            "A",
            "Đoạn 2 phân tích: việc tặng quà làm phát sinh tâm lý muốn trả ơn, chu kỳ nợ-trả ân tình tiếp diễn không hồi kết chính là sợi dây vô hình kết nối con người thành tấm lưới bảo trợ lẫn nhau.",
            {
                "B": "Tác giả không nói tặng quà xóa bỏ hoàn toàn bất bình đẳng giàu nghèo.",
                "C": "Không bàn về khía cạnh xả rác hay tiết kiệm tài nguyên môi trường.",
                "D": "Không nói về việc canh phòng gián điệp hay bắt ép tuân thủ luật lệ một cách bạo lực."
            }
        ),
        (
            "N2_05_M11_03",
            "現代において、シェアコミュニティなどの非金銭的なつながりが再評価されている理由として、筆者が述べているのはどれか。",
            [
                ("A", "市場経済の便利さの一方で失われた、損得勘定を越えた人間同士の温かな絆を人々が求めているから。"),
                ("B", "景気低迷により個人の可処分所得が減少し、金銭での売買が困難になったから。"),
                ("C", "政府が財政難のため、地域の福祉サービスを全面的に民間コミュニティに移管したから。"),
                ("D", "インターネットの普及により、見知らぬ他人を信用するリスクが完全になくなったから。")
            ],
            "A",
            "Đoạn cuối khẳng định: con người dù được giải phóng nhờ tiền nhưng lại cô đơn, việc quay lại với mô hình chia sẻ là minh chứng cho thấy bản năng con người luôn khao khát sự gắn kết ấm áp vượt lên trên toan tính tiền bạc.",
            {
                "B": "Tác giả giải thích dưới góc độ tâm lý xã hội và nhu cầu kết nối, không quy kết do nghèo đói không có tiền mua sắm.",
                "C": "Không đề cập đến việc chính phủ trốn tránh trách nhiệm phúc lợi.",
                "D": "Mạng Internet không làm triệt tiêu rủi ro lừa đảo, không liên quan đến lập luận tác giả."
            }
        )
    ]

    # Passage 2: 人工知能（AI）は真の「共感」を持ち得るか
    p11_2_text = """近年、対話型AIの急速な進化により、まるで生身の人間と会話しているかのように自然で心温まる受け答えをするシステムが登場している。利用者の愚痴や悩みを優しく聞き、適切な慰めの言葉をかけてくれるAIカウンセラーや癒やし系ロボットは、多くの人々の孤独感を和らげる存在として歓迎されている。

しかし、ここで一つの根源的な問いが浮かび上がる。AIが提示する「共感」は、本当に人間が他者に寄せる共感と同じものなのだろうか。

現在のAIの仕組みは、膨大なテキストデータを統計的に分析し、「どのような言葉を投げかけられたときに、どのような応答を返せば人間が満足するか」という確率的なパターンを再現しているにすぎない。AI自身が悲しみを味わい、身体的な痛みに苦しみ、死の恐怖に怯えているわけではない。つまり、AIが行っているのは共感の「シミュレーション（模倣）」であって、そこに主観的な感情体験は存在しないのである。

真の共感とは、自らも傷つきやすい不完全な肉体と心を持つ存在だからこそ、他者の痛みを「我がことのように」想像できる痛切な能力である。AIの言葉に慰めを見出すこと自体を否定する必要はないが、私たちがその模倣を本物の共感と混同し、生身の他者と傷つき合いながら関係を深める労力を放棄してしまえば、人間の感情の奥行きそのものが痩せ細ってしまうのではないだろうか。"""

    m11_2_items = [
        (
            "N2_05_M11_04",
            "現在実用化されている対話型AIの応答について、筆者はどのように説明しているか。",
            [
                ("A", "過去の膨大なデータを統計的に分析し、人間が好む確率の高い言葉のパターンを再現している。"),
                ("B", "対話を重ねる中で機械独自の感情や意識が芽生え、自発的に相手を思いやっている。"),
                ("C", "利用者の脳波や心拍数をリアルタイムで測定し、医学的に最適な慰めの言葉を選んでいる。"),
                ("D", "開発者の道徳観や人生経験がそのままプログラムとして埋め込まれて出力されている。")
            ],
            "A",
            "Đoạn 3 giải thích cơ chế: AI thực chất là phân tích thống kê lượng dữ liệu văn bản khổng lồ để tái hiện các khuôn mẫu phản hồi có xác suất khiến con người hài lòng cao nhất.",
            {
                "B": "Tác giả khẳng định AI hoàn toàn không có ý thức hay cảm xúc chủ quan nảy sinh.",
                "C": "Không đề cập đến việc đo sóng não hay nhịp tim sinh học.",
                "D": "Không phải do kinh nghiệm sống cá nhân của lập trình viên cấy trực tiếp vào."
            }
        ),
        (
            "N2_05_M11_05",
            "筆者が考える、人間ならではの「真の共感」の根源とは何か。",
            [
                ("A", "自らも痛みや死を恐れる傷つきやすい存在だからこそ、他者の苦痛を想像できること。"),
                ("B", "感情に流されることなく、相手の悩みを客観的・論理的に分析して解決策を示すこと。"),
                ("C", "高度な心理学の知識を身につけ、相手の言葉の裏にある無意識の欲求を見抜くこと。"),
                ("D", "どのような過ちを犯した相手であっても、無条件でその行動を全肯定して受け入れること。")
            ],
            "A",
            "Đoạn 4 nhấn mạnh: sự thấu cảm thực sự bắt nguồn từ việc chính bản thân con người là một thực thể dễ bị tổn thương, có thể trải qua nỗi đau và cái chết, từ đó mới có thể đau nỗi đau của người khác như của chính mình.",
            {
                "B": "Phân tích logic không cảm xúc là cách máy móc làm, trái ngược với bản chất thấu cảm.",
                "C": "Thấu cảm xuất phát từ tâm cảm của cơ thể sinh học, không phải đòi hỏi bằng cấp tâm lý học.",
                "D": "Thấu cảm không phải là dung túng hay khen ngợi mù quáng mọi hành vi sai trái."
            }
        ),
        (
            "N2_05_M11_06",
            "この文章の結論として、筆者が最も警鐘を鳴らしていることは何か。",
            [
                ("A", "AIの模倣を真の共感と勘違いし、生身の人間と深く向き合う努力を怠ってしまうこと。"),
                ("B", "対話型AIの開発が急速に進むことで、カウンセラーなどの専門職が職を失うこと。"),
                ("C", "AIロボットに過度の感情移入をしてしまい、高額な課金を続けて破産する人が増えること。"),
                ("D", "人間がAIに依存しすぎるあまり、言語能力や文章作成能力が著しく退化すること。")
            ],
            "A",
            "Câu cuối bài cảnh báo: nếu con người nhầm lẫn sự bắt chước của máy móc là thấu cảm thực sự, rồi từ bỏ nỗ lực kết nối đối thoại với đồng loại ngoài đời thực thì chiều sâu cảm xúc của con người sẽ bị lụi tàn.",
            {
                "B": "Không bàn về vấn đề mất việc làm hay thị trường lao động.",
                "C": "Không đề cập đến khía cạnh lừa đảo tài chính hay nạp tiền chơi game.",
                "D": "Không bàn về sự suy thoái khả năng viết lách ngữ pháp."
            }
        )
    ]

    # Passage 3: ヒートアイランド現象と都市の「風の道」計画
    p11_3_text = """大都市圏において、アスファルトやコンクリートで覆われた地表面の蓄熱や、ビル空調・自動車などからの人工排熱によって、都心部の気温が周辺の郊外よりも異常に高くなる「ヒートアイランド現象」が深刻化している。この現象は熱中症のリスクを高めるだけでなく、夜間の寝苦しさによる睡眠障害や、都市型集中豪雨の頻発など、市民生活や防災に多大な悪影響を及ぼしている。

この問題に対する都市計画上の画期的なアプローチとして、近年「風の道（Wind Corridor）」という概念に基づいた空間設計が注目を集めている。「風の道」とは、海や大規模な森林、河川敷などから吹き込む涼しい新鮮な風を、遮ることなく都心の過熱したエリアへとスムーズに引き込むための環境的な動線のことである。

従来の都市開発では、土地の利用効率や経済性を最優先し、河川沿いや海岸沿いに壁のように巨大な高層ビル群が隙間なく建設される傾向があった。その結果、海からの心地よい風がビルの壁に遮断され、内陸部に熱気が滞留する悪循環が生じていたのである。

現在進められている先進的な再開発計画では、川沿いの建物の高さを制限して開放的な緑地帯を確保したり、建物の配置や向きを地域の卓越風（年間を通じて最も頻繁に吹く風）の方向に合わせて斜めに整列させたりする工夫が導入されている。都市の発展と自然の気象メカニズムを調和させる知恵こそが、持続可能な未来都市の基盤となるのである。"""

    m11_3_items = [
        (
            "N2_05_M11_07",
            "都市部で「ヒートアイランド現象」が発生する主な原因として、筆者が挙げているものはどれか。",
            [
                ("A", "地表面のアスファルト等による熱の蓄積と、建物や車両からの人工排熱。"),
                ("B", "地球全体の温暖化により、海水の温度が年間を通じて急激に上昇したこと。"),
                ("C", "郊外の農地や森林が開発され、都市への農産物の供給がストップしたこと。"),
                ("D", "高層ビルの建設により日照時間が短縮され、地表の湿度が異常に高まったこと。")
            ],
            "A",
            "Đoạn 1 nêu rõ 2 nguyên nhân cốt lõi: nhiệt lượng tích tụ trên mặt đường nhựa/bê tông ('アスファルトやコンクリートで覆われた地表面の蓄熱') và nhiệt nhân tạo thải ra từ điều hòa các tòa nhà, động cơ ô tô ('ビル空調・自動車などからの人工排熱').",
            {
                "B": "Nhiệt độ nước biển toàn cầu là hiện tượng vĩ mô, không phải nguyên nhân cục bộ nội đô được nêu.",
                "C": "Không liên quan đến nguồn cung cấp nông sản.",
                "D": "Nhà cao tầng chắn nắng không làm tăng độ ẩm mà nguyên nhân là tích nhiệt và thải nhiệt."
            }
        ),
        (
            "N2_05_M11_08",
            "都市計画における「風の道」の基本的な役割とは何か。",
            [
                ("A", "海や河川から吹き込む涼しい風を遮らず、都心の熱気があるエリアへとスムーズに導くこと。"),
                ("B", "超高層ビルの上層部に巨大な風力発電機を設置し、クリーンな電力を供給すること。"),
                ("C", "台風などの強風が直接ビル街に衝突するのを防ぐため、沿岸部に高い防風林を築くこと。"),
                ("D", "自動車の排気ガスを上空へと急速に吸い上げるための専用の大型排気ダクトを作ること。")
            ],
            "A",
            "Đoạn 2 định nghĩa rõ ràng: '風の道' là luồng lưu thông môi trường nhằm dẫn luồng gió mát tươi mới từ biển, sông hồ vào sâu trong nội đô mà không bị cản trở ('涼しい新鮮な風を、遮ることなく都心の過熱したエリアへとスムーズに引き込む').",
            {
                "B": "Không phải là lắp tua-bin phát điện gió trên nóc nhà.",
                "C": "Không phải là trồng rừng phòng hộ chắn gió bão mà là mở đường cho gió mát vào.",
                "D": "Không phải ống thông gió hút khí thải xe cộ."
            }
        ),
        (
            "N2_05_M11_09",
            "文章中で紹介されている、先進的な再開発における具体的な工夫はどれか。",
            [
                ("A", "川沿いの建物の高さを抑え、建物の向きを年間で最もよく吹く風の方向に合わせて配置すること。"),
                ("B", "すべての道路のアスファルトを剥がし、全面を芝生や樹木に置き換えること。"),
                ("C", "夏の間はすべてのビル空調の稼働を一律に停止し、窓を開けて自然換気を行うこと。"),
                ("D", "海岸沿いに巨大な人工壁を建設し、海からの湿った風が市街地に入るのを防ぐこと。")
            ],
            "A",
            "Đoạn cuối liệt kê giải pháp công nghệ: khống chế chiều cao công trình ven sông để tạo dải xanh, đồng thời điều chỉnh góc quay của tòa nhà khớp với hướng gió chủ đạo (卓越風) để đón gió tối đa.",
            {
                "B": "Không thể bóc hết đường nhựa thay bằng cỏ trên toàn đô thị hiện đại.",
                "C": "Không bắt buộc tắt toàn bộ điều hòa giữa mùa hè nóng bức.",
                "D": "Xây tường ngăn gió biển là nguyên nhân gây tích nhiệt ở quá khứ, hoàn toàn trái ngược với giải pháp '風の道'."
            }
        )
    ]

    for p_items, p_text in [(m11_1_items, p11_1_text), (m11_2_items, p11_2_text), (m11_3_items, p11_3_text)]:
        for qid, stem, opts, ans, exp, dist in p_items:
            items.append({
                "id": qid,
                "typeId": "N2-RD-MID",
                "skill": "Reading",
                "category": "Mondai 11: 中文読解",
                "stem": stem,
                "contextPassage": p_text,
                "options": [{"id": o[0], "text": o[1]} for o in opts],
                "correctAnswer": ans,
                "explanationVi": exp,
                "distractorExplanations": dist
            })

    # =========================================================================
    # MONDAI 12: 統合理解 (Comparative Reading - 2 items)
    # Topic: キャリアにおける「失敗」の価値とリスク管理
    # =========================================================================
    p12_text = """【A】
若手ビジネスパーソンが成長するためには、「早い段階で多くの失敗を経験すること」こそが何よりの財産となる。机の上でいくら綿密な計画を練っても、実際のビジネスの現場では予測不能な事態の連続である。自ら果敢に挑戦し、手痛い失敗を経験して初めて、自分の実力不足を痛感し、教科書には載っていない実践的な知恵や柔軟な軌道修正力が身につく。失敗を過度に恐れて安全な道ばかりを選ぶ人間は、致命的な過ちを犯さない代わりに、自らの可能性を大きく広げることもできない。失敗から学び立ち直る「回復力（レジリエンス）」こそが、不確実な時代を生き抜く真の武器となるのである。

【B】
近年、ビジネスの世界で「失敗を恐れずに挑戦せよ」「失敗は成功の母だ」という言説が無批判に賛美される風潮があるが、これには強い警戒が必要だ。確かに失敗から得られる教訓はあるが、現代の複雑化したビジネス環境において、準備不足や無謀な判断による失敗は、個人の信用失墜や組織への甚大な経済的打撃につながりかねない。賢明なプロフェッショナルが目指すべきは、自ら泥をかぶって無駄な失敗を繰り返すことではなく、先人の失敗事例を徹底的に分析し、計算されたリスク管理のもとで「防げる失敗を確実に回避すること」である。無傷で目的を達成できるのであれば、それに越したことはないのだ。"""

    m12_items = [
        (
            "N2_05_M12_01",
            "AとBの筆者が共に認めている点は何か。",
            [
                ("A", "失敗を経験すること自体から、何らかの教訓や学びを得ることはできるという点。"),
                ("B", "若いうちはどれほど大きな経済的損失を出しても、失敗を繰り返すべきだという点。"),
                ("C", "教科書通りの安全な計画を立てていれば、ビジネスで失敗することは絶対にないという点。"),
                ("D", "他人の過去の失敗を分析しても、自分の実際の現場では全く役に立たないという点。")
            ],
            "A",
            "Cả hai tác giả đều thừa nhận thất bại đem lại bài học: Tác giả A coi đó là tài sản quý báu rèn luyện bản lĩnh; Tác giả B dù cảnh giác cũng thừa nhận '確かに失敗から得られる教訓はある' (Đúng là có những bài học rút ra được từ thất bại).",
            {
                "B": "Tác giả B phản đối kịch liệt việc gây tổn thất kinh tế hay hủy hoại uy tín.",
                "C": "Cả hai đều hiểu kinh doanh nhiều biến số, không ai nói làm theo sách là tuyệt đối không thất bại.",
                "D": "Tác giả B đánh giá rất cao việc học hỏi từ thất bại của người đi trước để tránh lặp lại."
            }
        ),
        (
            "N2_05_M12_02",
            "失敗に対する向き合い方について、AとBの主張の違いとして最も適切なものはどれか。",
            [
                ("A", "Aは失敗を恐れず果敢に挑戦して立ち直る力を養うべきだとし、Bは事前分析で防げる失敗は避けるべきだと説く。"),
                ("B", "Aは個人の信用を第一に守るべきだと主張し、Bは組織の利益のためなら個人の失敗は問わないと考える。"),
                ("C", "Aは先人の失敗事例を研究することの重要性を強調し、Bは自分の直感を信じて行動することを勧める。"),
                ("D", "Aは不確実な時代には挑戦自体を控えるべきだと考え、Bはどんな無謀なリスクも歓迎すべきだと主張する。")
            ],
            "A",
            "Tác giả A cổ vũ dũng cảm dấn thân và rèn luyện sức bật sau vấp ngã (レジリエンス); Tác giả B phản đối lãng mạn hóa thất bại liều lĩnh, khuyên phân tích kỹ tiền lệ và quản trị rủi ro để né tránh những sai lầm có thể phòng ngừa.",
            {
                "B": "Ngược lại, tác giả B mới là người lo ngại mất uy tín cá nhân và thiệt hại tổ chức.",
                "C": "Nghiên cứu tiền lệ của người đi trước là quan điểm của B, không phải A.",
                "D": "Hoàn toàn đảo ngược lập trường của cả hai tác giả."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m12_items:
        items.append({
            "id": qid,
            "typeId": "N2-RD-COMP",
            "skill": "Reading",
            "category": "Mondai 12: 統合理解 — キャリアにおける失敗の捉え方",
            "stem": stem,
            "contextPassage": p12_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 13: 長文読解 (Thematic Long Passage - 3 items)
    # Topic: 加速化する現代社会と「時間の哲学」
    # =========================================================================
    p13_text = """科学技術の進歩は、私たちに前例のない「スピード」と「効率」をもたらした。新幹線や航空機は物理的な移動時間を劇的に短縮し、インターネットやスマートフォンの普及は、地球の裏側の情報であっても一瞬で手元に届けてくれる。本来、これらの技術革新は、人々の生活から無駄な手間を省き、余暇や休息のための「ゆとりのある時間」を大量に生み出してくれるはずであった。

ところが、現実はどうだろうか。私たちは過去のどの時代の人々よりも時間に追われ、常に「時間がない」と焦燥感を募らせている。技術が処理速度を上げれば上げるほど、単位時間あたりに処理すべきタスクの量が加速度的に増大し、結果として私たちはより過密なスケジュールに縛られることになった。かつては職場を離れれば仕事から解放されていたはずが、常時接続の通信網によって、いつでもどこでも連絡が取れる状態になり、プライベートな時間と労働時間の境界線は完全に曖昧になってしまったのである。

社会学者のローザは、現代社会を特徴づけるこの現象を「社会の加速化」と呼んだ。技術の加速、社会変動の加速、そして生活ペースの加速が相互に絡み合い、私たちは立ち止まること自体に罪悪感や取り残される恐怖を抱くようになる。効率性を追求するあまり、物事をじっくりと熟成させる時間や、他者と非効率に対話を重ねる時間、何もしない空白の時間が「無駄」として次々と切り捨てられていく。

しかし、人間にとって時間とは、単にデジタル時計の針が刻む均質な量（クロノス）に尽きるものではない。古代ギリシャ人は、客観的に流れる時間とは別に、意味や充足感に満ちた主観的な決定的一瞬を「カイロス」と呼んで区別した。夕焼けの美しさに心を奪われるひとときや、親しい友と語り合うかけがえのない時間には、生産性や効率という物差しは通用しない。

私たちが真の豊かさを取り戻すためには、効率性の競争から一度意識的に距離を置き、自らの時間を主体的に選び取る勇気を持つ必要がある。「すべての時間を有効活用しなければならない」という強迫観念を手放し、無駄の中にこそ潜む人生の深い味わいに気づくこと。それこそが、加速し続ける現代社会に対する最も人間的で根源的な抵抗なのである。"""

    m13_items = [
        (
            "N2_05_M13_01",
            "技術の進歩によって本来期待されていたことと、現代の現実とのギャップとして筆者が指摘しているのはどれか。",
            [
                ("A", "技術革新で自由なゆとり時間が生まれるはずだったが、かえって処理すべき仕事が増えて時間に追われている。"),
                ("B", "物理的な移動時間が短縮された結果、人々が旅行や観光に全く興味を示さなくなってしまった。"),
                ("C", "通信技術の発達によって職場の人間関係が円滑になるはずだったが、対面での対話が完全に途絶えた。"),
                ("D", "インターネットの普及で誰でも専門知識を持てるようになったが、読書をする習慣が失われた。")
            ],
            "A",
            "Đoạn 1 và 2 đối chiếu rõ: ban đầu kỳ vọng công nghệ giúp tiết kiệm sức lao động để con người có nhiều thời gian rảnh rỗi nghỉ ngơi, nhưng thực tế tốc độ xử lý nhanh khiến lượng việc dồn về trong một đơn vị thời gian tăng theo cấp số nhân, khiến con người luôn bận rộn hối hả hơn trước.",
            {
                "B": "Không hề nói con người không còn hứng thú đi du lịch.",
                "C": "Không bàn về sự gián đoạn tuyệt đối trong giao tiếp công sở.",
                "D": "Không đề cập đến việc phổ cập tri thức hay thói quen đọc sách."
            }
        ),
        (
            "N2_05_M13_02",
            "筆者が述べる「カイロス」とは、どのような時間を指しているか。",
            [
                ("A", "生産性や効率とは無関係な、意味や充足感に満ちた主観的なかけがえのない一瞬。"),
                ("B", "時計の針が正確に刻む、すべての人間に対して平等に流れる客観的な物理時間。"),
                ("C", "将来のキャリアアップのために、資格取得や勉強に充てるべき自己投資の時間。"),
                ("D", "社会の急速な変化に取り残されないよう、最新の情報を常に収集し続ける時間。")
            ],
            "A",
            "Đoạn 4 định nghĩa: trái với thời gian cơ học định lượng đều đều (Chronos), Kairos là khoảnh khắc thời gian chủ quan ngập tràn ý nghĩa và sự viên mãn (ngắm hoàng hôn, đàm đạo bên bạn bè), nơi mà thước đo năng suất hiệu quả hoàn toàn vô nghĩa.",
            {
                "B": "Thời gian vật lý khách quan do đồng hồ tích tắc chính là Chronos (均質な量・クロノス).",
                "C": "Học tập để thăng tiến nghề nghiệp vẫn thuộc phạm trù tối ưu hóa năng suất hiệu quả.",
                "D": "Cập nhật tin tức liên tục là biểu hiện của việc bị cuốn theo guồng quay gia tốc xã hội."
            }
        ),
        (
            "N2_05_M13_03",
            "この文章を通じて、筆者が現代人に提案している生き方として最も適切なものはどれか。",
            [
                ("A", "すべての時間を効率的に使う強迫観念を手放し、一見無駄に見える時間の中に人生の豊かさを見出すこと。"),
                ("B", "スマートフォンなどの通信機器の使用を完全にやめ、文明を拒絶して自給自足の生活に戻ること。"),
                ("C", "過密なスケジュールを完璧にこなすため、最新のタスク管理アプリを駆使して自己管理を徹底すること。"),
                ("D", "会社の労働時間を法律で厳しく制限するよう、労働組合を通じて経営陣に強く抗議すること。")
            ],
            "A",
            "Đoạn kết đúc kết thông điệp: cần dũng cảm buông bỏ nỗi ám ảnh 'phải tận dụng hiệu quả từng giây từng phút', nhận ra phong vị sâu sắc của cuộc đời ẩn trong những khoảng thời gian tưởng chừng như vô dụng, đó mới là sự phản kháng nhân văn nhất.",
            {
                "B": "Tác giả khuyên có khoảng cách ý thức, không hề cổ súy bài trừ công nghệ hay về rừng tự cấp tự túc.",
                "C": "Dùng ứng dụng quản lý tác vụ để nhồi nhét việc càng làm tăng thêm áp lực gia tốc.",
                "D": "Bài viết mang tính triết học nhân sinh, không bàn về kiến nghị công đoàn đấu tranh pháp lý."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m13_items:
        items.append({
            "id": qid,
            "typeId": "N2-RD-LONG",
            "skill": "Reading",
            "category": "Mondai 13: 長文読解 — 加速化する現代社会と時間の哲学",
            "stem": stem,
            "contextPassage": p13_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 14: 情報検索 (Information Retrieval - 2 items)
    # Topic: 市民文化センター ホール利用規約および附帯設備利用案内
    # =========================================================================
    p14_text = """【市民文化センター ホールおよび練習室の利用案内】

1. 施設概要および利用時間区分
・大ホール（定員800名）：午前（9:00〜12:00）、午後（13:00〜17:00）、夜間（18:00〜22:00）
・多目的室（定員50名）：上記区分に加え、全日（9:00〜22:00）の一括利用が可能。
※準備および原状復帰（清掃含む）は、必ず承認された利用時間内に完了してください。

2. 利用料金および減免制度
・基本利用料：大ホール（平日：午前15,000円、午後25,000円、夜間30,000円／土日祝は2割増）
・市内在住・在勤者が過半数を占める非営利団体が利用する場合、基本利用料が30%減額されます。
・入場料を徴収する催し（営利目的）の場合、基本利用料に50%の割増料金が加算されます。

3. 附帯設備利用料（1区分あたり・税込）
・グランドピアノ（調律代別）：5,000円
・ステージ照明セット一式：3,000円
・ワイヤレスマイク（2本1組）：1,500円
・大型プロジェクターおよびスクリーン：4,000円
※附帯設備の利用料金には減免制度は適用されません。

4. 予約取消（キャンセル）および還付規定
・利用日の30日前までに所定の取消届を提出した場合：納入済み利用料の70%を返金。
・利用日の14日前までに所定の取消届を提出した場合：納入済み利用料の50%を返金。
・利用日の13日前以降の取消：返金不可（0%）。
※自然災害等、不可抗力により施設が使用不能となった場合は、全額（100%）返金いたします。"""

    m14_items = [
        (
            "N2_05_M14_01",
            "市内に勤務するメンバーが過半数を占める非営利の市民合唱団が、平日の午後に大ホールを利用し、グランドピアノとワイヤレスマイクを使用する場合、合計料金はいくらになるか。入場料は無料とする。",
            [
                ("A", "24,000円"),
                ("B", "21,500円"),
                ("C", "17,000円"),
                ("D", "19,500円")
            ],
            "A",
            "Cách tính chuẩn xác theo điều lệ:\n1. Giá thuê cơ bản đại sảnh buổi chiều ngày thường: 25,000 yên.\n2. Đoàn phi lợi nhuận có trên 50% thành viên đi làm trong thành phố được giảm 30% giá phòng cơ bản: 25,000 x (1 - 0.3) = 17,500 yên.\n3. Thiết bị kèm theo (không áp dụng giảm giá):\n   - Đàn Grand Piano: 5,000 yên.\n   - Bộ 2 mic không dây: 1,500 yên.\n   -> Tổng phụ kiện: 6,500 yên.\n4. Tổng chi phí: 17,500 + 6,500 = 24,000 yên.",
            {
                "B": "21,500円: Tính nhầm giảm 30% lên cả phụ kiện (6,500 x 0.7 = 4,550 -> 17,500 + 4,550 = 22,050) hoặc trừ sai.",
                "C": "17,000円: Quên cộng tiền thuê mic và đàn piano.",
                "D": "19,500円: Tính sai tỷ lệ giảm giá phòng."
            }
        ),
        (
            "N2_05_M14_02",
            "利用予約のキャンセルおよび返金に関する説明として、正しいものはどれか。",
            [
                ("A", "台風などの自然災害によって施設自体が使えなくなった場合、利用料金は全額返金される。"),
                ("B", "利用日の20日前にキャンセル届を提出した場合、納入した料金の70%が返金される。"),
                ("C", "入場料を徴収する営利イベントの場合、いかなる理由であってもキャンセル時の返金はない。"),
                ("D", "利用日の前日であっても、やむを得ない事情があれば半額が返金される。")
            ],
            "A",
            "Điều 4 ghi rõ: trường hợp bất khả kháng do thiên tai cơ sở không thể hoạt động thì hoàn trả 100% ('自然災害等、不可抗力により施設が使用不能となった場合は、全額（100%）返金いたします').",
            {
                "B": "20 ngày trước ngày diễn thuộc mốc '14日前までに' (từ ngày thứ 14 đến 29) chỉ được hoàn 50%, mốc 70% bắt buộc phải trước từ 30 ngày trở lên.",
                "C": "Quy định hoàn tiền áp dụng chung, không phân biệt sự kiện có thu vé hay không.",
                "D": "Trước ngày diễn 1 ngày (13日前以降) thì tỷ lệ hoàn tiền là 0% (không được hoàn trả)."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m14_items:
        items.append({
            "id": qid,
            "typeId": "N2-RD-INFO",
            "skill": "Reading",
            "category": "Mondai 14: 情報検索 — 市民文化センター利用案内",
            "stem": stem,
            "contextPassage": p14_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # REBALANCE READING KEYS (Distribute keys naturally across A, B, C, D)
    # =========================================================================
    swap_targets = {
        'N2_05_M10_01': 'B',
        'N2_05_M10_02': 'C',
        'N2_05_M10_03': 'D',
        'N2_05_M10_04': 'B',
        'N2_05_M10_05': 'C',
        'N2_05_M11_01': 'D',
        'N2_05_M11_02': 'B',
        'N2_05_M11_03': 'C',
        'N2_05_M11_04': 'D',
        'N2_05_M11_05': 'B',
        'N2_05_M11_06': 'C',
        'N2_05_M11_07': 'D',
        'N2_05_M11_08': 'B',
        'N2_05_M11_09': 'C',
        'N2_05_M12_01': 'D',
        'N2_05_M12_02': 'B',
        'N2_05_M13_01': 'C',
        'N2_05_M13_02': 'D',
        'N2_05_M13_03': 'B',
        'N2_05_M14_01': 'C',
        'N2_05_M14_02': 'D',
    }

    for it in items:
        qid = it['id']
        if qid in swap_targets and it['correctAnswer'] == 'A':
            tgt = swap_targets[qid]
            opt_map = {o['id']: o['text'] for o in it['options']}
            text_correct = opt_map['A']
            text_tgt = opt_map[tgt]
            for o in it['options']:
                if o['id'] == 'A':
                    o['text'] = text_tgt
                elif o['id'] == tgt:
                    o['text'] = text_correct
            dist = it.get('distractorExplanations', {})
            old_tgt_exp = dist.get(tgt, '')
            new_dist = {}
            for k, v in dist.items():
                if k == tgt:
                    new_dist['A'] = old_tgt_exp
                else:
                    new_dist[k] = v
            it['distractorExplanations'] = new_dist
            it['correctAnswer'] = tgt

    return items

