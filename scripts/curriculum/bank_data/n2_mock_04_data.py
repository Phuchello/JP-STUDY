# -*- coding: utf-8 -*-
"""
JLPT N2 Mock Exam #04 - Section 1: Language Knowledge & Reading (言語知識・読解)
Blueprint (75 items / 105 minutes):
- Mondai 1: 漢字読み (5 items) [Q1 - Q5]
- Mondai 2: 表記 (5 items) [Q6 - Q10]
- Mondai 3: 語形成 (3 items) [Q11 - Q13]
- Mondai 4: 文脈規定 (7 items) [Q14 - Q20]
- Mondai 5: 言い換え類義 (5 items) [Q21 - Q25]
- Mondai 6: 用法 (5 items) [Q26 - Q30]
- Mondai 7: 文法形式 (12 items) [Q31 - Q42]
- Mondai 8: 文の組み立て ★ (5 items) [Q43 - Q47]
- Mondai 9: 文章の文法 (5 items) [Q48 - Q52]
- Mondai 10: 短文読解 (5 items) [Q53 - Q57]
- Mondai 11: 中文読解 (9 items) [Q58 - Q66]
- Mondai 12: 統合理解 (2 items) [Q67 - Q68]
- Mondai 13: 長文読解 (3 items) [Q69 - Q71]
- Mondai 14: 情報検索 (2 items) [Q72 - Q73]
Total Section 1: 75 items
"""

def get_n2_mock_04_sec1_items():
    items = []

    # =========================================================================
    # MONDAI 1: 漢字読み (Kanji Reading - 5 items)
    # =========================================================================
    m1_raw = [
        (
            "N2_04_M1_01",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "変化の激しい現代市場において、企業は常に新たな活路を【模索】している。",
            "もさく",
            [("A", "ぼさく"), ("B", "もさく"), ("C", "めいさく"), ("D", "ぼうさく")],
            "B",
            "模索（もさく - MÔ TÁC）: Tìm kiếm, lần mò phương hướng/giải pháp trong hoàn cảnh khó khăn. Chữ 模 có âm on là も, chữ 索 có âm on là さく.",
            {
                "A": "ぼさく: Âm ぼ là cách đọc sai cho chữ 模 (âm on chuẩn là も hoặc ぼ trong quy tắc cũ, nhưng từ ghép 模索 chỉ đọc là もさく).",
                "C": "めいさく: Nhầm sang từ 迷作 (めいさく) hoặc 名作 (kiệt tác).",
                "D": "ぼうさく: Nhầm sang 謀策 (mưu chước, mưu kế)."
            }
        ),
        (
            "N2_04_M1_02",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "豊かな自然の恵みを【享受】することは、人々の心身の健康につながる。",
            "きょうじゅ",
            [("A", "きょうじゅ"), ("B", "こうじゅ"), ("C", "きょうしゅ"), ("D", "ごうじゅ")],
            "A",
            "享受（きょうじゅ - HƯỞNG THỤ）: Thụ hưởng, đón nhận và tận hưởng lợi ích tốt đẹp. Chữ 享 có âm on là きょう, chữ 受 có âm on là じゅ.",
            {
                "B": "こうじゅ: Nhầm âm きょう thành こう.",
                "C": "きょうしゅ: Nhầm âm đục じゅ thành âm thanh しゅ.",
                "D": "ごうじゅ: Sai âm đầu きょう thành ごう."
            }
        ),
        (
            "N2_04_M1_03",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "政府は経済活動の活性化を目指し、長年続いていた規制の【緩和】を発表した。",
            "かんわ",
            [("A", "がんわ"), ("B", "かんか"), ("C", "かんわ"), ("D", "けいわ")],
            "C",
            "緩和（かんわ - HOÃN HÒA）: Nới lỏng, làm nhẹ bớt mức độ nghiêm ngặt hoặc căng thẳng. Chữ 緩 có âm on là かん, chữ 和 có âm on là わ.",
            {
                "A": "がんわ: Nhầm âm thanh かん thành âm đục がん.",
                "B": "かんか: Nhầm âm 和 (わ) thành 化 (か).",
                "D": "けいわ: Nhầm âm 緩 thành âm けい."
            }
        ),
        (
            "N2_04_M1_04",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "長年にわたる現場での経験の【蓄積】が、今回の新技術開発の基盤となった。",
            "ちくせき",
            [("A", "ちくせき"), ("B", "ちゅうせき"), ("C", "ちくしゃく"), ("D", "ちょくせき")],
            "A",
            "蓄積（ちくせき - SÚC TÍCH）: Tích lũy, dồn chứa qua thời gian dài (kinh nghiệm, kiến thức, vốn). Chữ 蓄 có âm on là ちく, chữ 積 có âm on là せき.",
            {
                "B": "ちゅうせき: Nhầm âm ちく thành ちゅう.",
                "C": "ちくしゃく: Nhầm âm せき thành しゃく.",
                "D": "ちょくせき: Nhầm âm ちく thành ちょく."
            }
        ),
        (
            "N2_04_M1_05",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "自治体は地域経済の活性化を【促進】するため、創業支援制度を大幅に拡充した。",
            "そくしん",
            [("A", "そくしん"), ("B", "ぞくしん"), ("C", "そくじん"), ("D", "しょうしん")],
            "A",
            "促進（そくしん - XÚC TIẾN）: Thúc đẩy, đẩy mạnh sự phát triển hoặc tiến trình của một sự việc. Chữ 促 có âm on là そく, chữ 進 có âm on là しん.",
            {
                "B": "ぞくしん: Nhầm âm thanh そく thành âm đục ぞく.",
                "C": "そくじん: Nhầm âm しん thành âm đục じん.",
                "D": "しょうしん: Nhầm sang 昇進 (しょうしん - thăng tiến, thăng chức)."
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
            "N2_04_M2_01",
            "N2-MO-WRITE",
            "Mondai 2: 表記",
            "彼は地域社会の発展に多大な【こうけん】を果たした功労者として表彰された。",
            "こうけん",
            [("A", "効献"), ("B", "貢献"), ("C", "貢研"), ("D", "効建")],
            "B",
            "貢献（こうけん - CỐNG HIẾN）: Cống hiến, đóng góp công sức to lớn cho cộng đồng, xã hội. Chữ 貢 (Cống) đi với chữ 献 (Hiến).",
            {
                "A": "効献: Viết sai chữ đầu thành 効 (Hiệu trong hiệu quả).",
                "C": "貢研: Viết sai chữ sau thành 研 (Nghiên trong nghiên cứu).",
                "D": "効建: Viết sai cả hai chữ thành 効 (Hiệu) và 建 (Kiến trong xây dựng)."
            }
        ),
        (
            "N2_04_M2_02",
            "N2-MO-WRITE",
            "Mondai 2: 表記",
            "スマートフォンが急速に【ふきゅう】したことで、人々の生活様式は劇的に変化した。",
            "ふきゅう",
            [("A", "普及"), ("B", "普給"), ("C", "布及"), ("D", "敷及")],
            "A",
            "普及（ふきゅう - PHỔ CẬP）: Phổ biến rộng rãi đến số đông dân chúng. Chữ 普 (Phổ trong phổ thông) đi với 及 (Cập trong lan tới).",
            {
                "B": "普給: Viết sai chữ 及 thành 給 (Cấp trong cung cấp).",
                "C": "布及: Viết sai chữ 普 thành 布 (Bố trong tuyên bố).",
                "D": "敷及: Viết sai chữ 普 thành 敷 (Phu trong trải thảm, lắp đặt)."
            }
        ),
        (
            "N2_04_M2_03",
            "N2-MO-WRITE",
            "Mondai 2: 表記",
            "重大な投資決定を下す前に、市場の動向を【しんちょう】に見極める必要がある。",
            "しんちょう",
            [("A", "慎重"), ("B", "真重"), ("C", "慎調"), ("D", "深重")],
            "A",
            "慎重（しんちょう - THẬN TRỌNG）: Cẩn trọng, thấu đáo, không hấp tấp. Chữ 慎 (Thận trong cẩn thận) đi với chữ 重 (Trọng).",
            {
                "B": "真重: Viết sai chữ 慎 thành 真 (Chân trong chân thực).",
                "C": "慎調: Viết sai chữ 重 thành 調 (Điều trong điều tra, nhịp điệu).",
                "D": "深重: Viết sai chữ 慎 thành 深 (Thâm trong sâu sắc)."
            }
        ),
        (
            "N2_04_M2_04",
            "N2-MO-WRITE",
            "Mondai 2: 表記",
            "幾多の試練を【こくふく】した経験こそが、チームの結束を強固にした。",
            "こくふく",
            [("A", "刻服"), ("B", "克服"), ("C", "克復"), ("D", "告服")],
            "B",
            "克服（こくふく - KHẮC PHỤC）: Vượt qua khó khăn, bệnh tật, trở ngại nhờ ý chí và nỗ lực. Chữ 克 (Khắc) đi với 服 (Phục).",
            {
                "A": "刻服: Viết sai chữ 克 thành 刻 (Khắc trong chạm khắc, khắc cốt).",
                "C": "克復: Chữ 復 là Phục trong hồi phục, khôi phục, không tạo thành từ đúng 'khắc phục khó khăn'.",
                "D": "告服: Viết sai chữ 克 thành 告 (Cáo trong thông báo)."
            }
        ),
        (
            "N2_04_M2_05",
            "N2-MO-WRITE",
            "Mondai 2: 表記",
            "試験会場では不正行為を未然に防ぐため、【げんかく】な本人確認が行われる。",
            "げんかく",
            [("A", "厳格"), ("B", "厳確"), ("C", "原格"), ("D", "険格")],
            "A",
            "厳格（げんかく - NGHIÊM CÁCH）: Nghiêm khắc, chặt chẽ đúng quy tắc chuẩn mực. Chữ 厳 (Nghiêm) đi với chữ 格 (Cách).",
            {
                "B": "厳確: Viết sai chữ 格 thành 確 (Xác trong chính xác).",
                "C": "原格: Viết sai chữ 厳 thành 原 (Nguyên trong nguyên thủy).",
                "D": "険格: Viết sai chữ 厳 thành 険 (Hiểm trong nguy hiểm, dốc hiểm trở)."
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
    # MONDAI 3: 語形成 (Word Formation - 3 items)
    # =========================================================================
    m3_raw = [
        (
            "N2_04_M3_01",
            "N2-MO-FORM",
            "Mondai 3: 語形成",
            "最先端の次世代バッテリーを実用化するため、巨額の（　　）費が投じられた。",
            [("A", "研究"), ("B", "開発"), ("C", "修繕"), ("D", "製造")],
            "B",
            "開発費（かいはつひ - KHAI PHÁT PHÍ）: Chi phí phát triển (sản phẩm/công nghệ mới). Đi với cụm '実用化するため' (để đưa vào ứng dụng thực tế), danh từ ghép '開発費' là tự nhiên và chính xác nhất theo quy chuẩn kinh doanh công nghệ.",
            {
                "A": "研究: '研究費' nhấn mạnh nghiên cứu lý thuyết cơ bản hơn là đưa vào ứng dụng thực tế (実用化).",
                "C": "修繕: '修繕費' là chi phí sửa chữa bảo trì tài sản hiện có, không phù hợp với việc tạo ra pin thế hệ mới.",
                "D": "製造: '製造費' là chi phí sản xuất hàng loạt, không đi với giai đoạn đưa vào thực tế (実用化)."
            }
        ),
        (
            "N2_04_M3_02",
            "N2-MO-FORM",
            "Mondai 3: 語形成",
            "相次ぐ競合他社の台頭に対し、社内にはこれまでにない強い（　　）感が漂っている。",
            [("A", "危険"), ("B", "危機"), ("C", "不安"), ("D", "不信")],
            "B",
            "危機感（ききかん - NGUY CƠ CẢM）: Cảm giác khủng hoảng, nhận thức sâu sắc về mối nguy hiểm cận kề. Hậu tố '〜感' kết hợp với danh từ '危機' tạo thành cụm cố định '強い危機感を持つ／危機感が漂う'.",
            {
                "A": "危険: '危険感' không phải là từ ghép tự nhiên trong tiếng Nhật (người Nhật dùng '危機感').",
                "C": "不安: '不安感' có nghĩa là cảm giác bất an chung chung, không chuẩn bằng '危機感' khi nói về đối thủ cạnh tranh đe dọa sự tồn vong doanh nghiệp.",
                "D": "不信: '不信感' mang nghĩa là cảm giác mất lòng tin, nghi ngờ lẫn nhau, không phù hợp bối cảnh này."
            }
        ),
        (
            "N2_04_M3_03",
            "N2-MO-FORM",
            "Mondai 3: 語形成",
            "この山岳地帯には、まだ人の手がほとんど入っていない（　　）開発の森林が広がっている。",
            [("A", "無"), ("B", "非"), ("C", "未"), ("D", "不")],
            "C",
            "未開発（みかいはつ - VỊ KHAI PHÁT）: Chưa được khai phá, chưa phát triển. Tiền tố '未〜' biểu thị trạng thái một việc gì đó chưa xảy ra nhưng có khả năng sẽ diễn ra trong tương lai.",
            {
                "A": "無: Tiền tố '無〜' biểu thị không có (như 無意味, 無責任), không kết hợp với 開発.",
                "B": "非: Tiền tố '非〜' biểu thị tính chất phi/ngược lại (như 非公式, 非常識), không kết hợp với 開発.",
                "D": "不: Tiền tố '不〜' biểu thị phủ định tính chất (như 不可能, 不便), không kết hợp thành *不開発."
            }
        ),
        (
            "N2_04_M3_04",
            "N2-MO-FORM",
            "Mondai 3: 語形成",
            "この地域は古くからの住民が多く、隣人同士の（　　）帯感も非常に強い。",
            [("A", "連"), ("B", "団"), ("C", "結"), ("D", "親")],
            "A",
            "連帯感（れんたいかん - LIÊN ĐỚI CẢM）: Tinh thần đoàn kết, ý thức gắn bó tương trợ lẫn nhau giữa các thành viên trong tập thể/cộng đồng.",
            {
                "B": "団: Thường ghép trong 団体 (đoàn thể), 団結 (đoàn kết), không ghép thành *団帯感.",
                "C": "結: Thường ghép trong 結束 (kết thúc, đoàn kết chặt chẽ), 結合 (kết hợp), không ghép thành *結帯感.",
                "D": "親: Ghép trong 親近感 (cảm giác thân thiết gần gũi), không tạo từ *親帯感."
            }
        ),
        (
            "N2_04_M3_05",
            "N2-MO-FORM",
            "Mondai 3: 語形成",
            "資源循環型社会の構築に向けて、使用済み製品の（　　）利用が一段と推進されている。",
            [("A", "再"), ("B", "復"), ("C", "新"), ("D", "重")],
            "A",
            "再利用（さいりよう - TÁI LỢI DỤNG）: Tái sử dụng, dùng lại tài nguyên/vật phẩm đã qua sử dụng để giảm rác thải.",
            {
                "B": "復: Tiền tố 復- ghép trong 復興 (phục hưng), 復活 (phục hoạt), không tạo từ *復利用.",
                "C": "新: Tiền tố 新- mang nghĩa mới (như 新開発, 新製品), không mang nghĩa dùng lại đồ cũ (tái sử dụng).",
                "D": "重: Ghép trong 重複 (trùng lặp), 重大 (trọng đại), không ghép thành *重利用."
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
            "N2_04_M4_01",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "大規模な防災訓練を成功させるには、消防署と警察、地域住民が緊密に（　　）することが不可欠だ。",
            [("A", "連携"), ("B", "連行"), ("C", "連帯"), ("D", "連続")],
            "A",
            "連携（れんけい - LIÊN HUYỆN）: Phối hợp, liên kết hành động chặt chẽ giữa các tổ chức/đoàn thể để cùng đạt mục tiêu. Đi với phó từ '緊密に連携する' (phối hợp chặt chẽ).",
            {
                "B": "連行: Áp giải, dẫn giải tội phạm (như 警察に連行される).",
                "C": "連帯: Tinh thần đoàn kết, gắn kết trách nhiệm chung (như 連帯責任).",
                "D": "連続: Liên tục, diễn ra không ngừng nghỉ theo chuỗi thời gian."
            }
        ),
        (
            "N2_04_M4_02",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "新サービスの設計においては、高齢者や障害者など多様な利用者の利便性を（　　）に置いて進めるべきだ。",
            [("A", "心中"), ("B", "念頭"), ("C", "本音"), ("D", "思惑")],
            "B",
            "念頭（ねんとう - NIỆM ĐẦU）: Đi với quán dụng ngữ '〜を念頭に置く' nghĩa là luôn ghi nhớ, để tâm, tính đến yếu tố nào đó khi lập kế hoạch hay hành động.",
            {
                "A": "心中: '心中' (cân nhắc trong lòng, hoặc tự tử đôi) không dùng trong cụm *心中に置く.",
                "C": "本音: Suy nghĩ thật trong lòng, đối lập với 建前 (xã giao bề ngoài), không đi với *本音に置く.",
                "D": "思惑: Toan tính cá nhân, mưu đồ riêng, không phù hợp ngữ cảnh thiết kế dịch vụ công cộng."
            }
        ),
        (
            "N2_04_M4_03",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "プロジェクトリーダーには、予期せぬトラブルが生じても最後まで責任を持って任務を（　　）する能力が求められる。",
            [("A", "遂行"), ("B", "履行"), ("C", "敢行"), ("D", "励行")],
            "A",
            "遂行（すいこう - TOẠI HÀNH）: Hoàn thành, tiến hành trọn vẹn nhiệm vụ/kế hoạch được giao đến cùng. Đi với tân ngữ '任務を遂行する' (hoàn thành xuất sắc nhiệm vụ).",
            {
                "B": "履行: Thực hiện cam kết, thi hành điều khoản hợp đồng (như 契約を履行する).",
                "C": "敢行: Dũng cảm quyết tâm làm dù gặp nhiều nguy hiểm hoặc thời tiết xấu (như 悪天候の中決行/敢行する).",
                "D": "励行: Tự giác thực hành nghiêm túc thói quen tốt/quy định hàng ngày (như うがい手洗いの励行)."
            }
        ),
        (
            "N2_04_M4_04",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "トラブルの原因究明を行うため、事故が発生するに至った詳しい（　　）を調査報告書にまとめた。",
            [("A", "経歴"), ("B", "経緯"), ("C", "経路"), ("D", "経過")],
            "B",
            "経緯（けいい - KINH VĨ）: Toàn bộ ngọn ngành quá trình diễn biến của một sự việc từ đầu đến cuối. Thường dùng trong báo cáo sự cố (事件・事故の詳しい経緯).",
            {
                "A": "経歴: Lý lịch, quá trình học tập và làm việc của cá nhân.",
                "C": "経路: Lộ trình di chuyển từ điểm A đến điểm B (như 避難経路, 感染経路).",
                "D": "経過: Sự trôi qua của thời gian hoặc tiến trình phát triển tình trạng (như 手術後の経過)."
            }
        ),
        (
            "N2_04_M4_05",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "両国間の交渉は難航したが、双方が少しずつ条件を（　　）したことで無事に合意へと至った。",
            [("A", "譲歩"), ("B", "妥協"), ("C", "協調"), ("D", "容認")],
            "A",
            "譲歩（じょうほ - NHƯỢNG BỘ）: Nhượng bộ, lùi một bước trong đàm phán để nhường quyền lợi cho đối phương cùng đạt thỏa thuận. Thường dùng '条件を譲歩する／互いに譲歩する'.",
            {
                "B": "妥協: Thỏa hiệp. Đi với động từ する nhưng thường dùng '妥協する' đơn độc chứ không dùng trực tiếp làm tân ngữ cụm '条件を妥協する'.",
                "C": "協調: Hợp tác, phối hợp hòa thuận (như 協調性), không đi với '条件を協調する'.",
                "D": "容認: Chấp nhận, thừa nhận cho phép tồn tại một sự việc (như 存在を容認する)."
            }
        ),
        (
            "N2_04_M4_06",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "創業当初は赤字続きだった新事業も、ようやく黒字化を達成して（　　）に乗ってきた。",
            [("A", "軌道"), ("B", "航路"), ("C", "順路"), ("D", "路線")],
            "A",
            "軌道（きどう - QUỸ ĐẠO）: Quán dụng ngữ '軌道に乗る' nghĩa là công việc/dự án đã đi vào guồng ổn định, vận hành trơn tru và bắt đầu gặt hái kết quả khả quan.",
            {
                "B": "航路: Tuyến đường biển hoặc đường hàng không.",
                "C": "順路: Lối đi theo chỉ dẫn theo thứ tự (như trong bảo tàng, triển lãm).",
                "D": "路線: Tuyến đường xe lửa, tuyến bus, hoặc đường lối chủ trương (như 経営路線)."
            }
        ),
        (
            "N2_04_M4_07",
            "N2-VOC-CTX",
            "Mondai 4: 文脈規定",
            "物価の上昇に伴い、家計の支出をできる限り（　　）しようと節約に励む家庭が増えている。",
            [("A", "抑制"), ("B", "制圧"), ("C", "圧迫"), ("D", "束縛")],
            "A",
            "抑制（よくせい - ỨC CHẾ）: Kiềm chế, kìm hãm, hạn chế không để bùng phát hoặc tăng quá mức (như 支出の抑制, 感情を抑制する).",
            {
                "B": "制圧: Trấn áp bạo loạn, khống chế đối tượng nguy hiểm bằng vũ lực.",
                "C": "圧迫: Chèn ép, đè nén, gây áp lực nặng nề (như 血管を圧迫する, 財政を圧迫する).",
                "D": "束縛: Ràng buộc, trói buộc tự do thân thể hoặc thời gian của người khác."
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
    # MONDAI 5: 言い換え類義 (Paraphrases - 5 items)
    # =========================================================================
    m5_raw = [
        (
            "N2_04_M5_01",
            "N2-VOC-PARA",
            "Mondai 5: 言い換え類義",
            "今年度の売上高は、【おおむね】計画どおりに推移している。",
            "おおむね",
            [("A", "だいたい"), ("B", "まったく"), ("C", "かろうじて"), ("D", "めったに")],
            "A",
            "おおむね: Đại khái, phần lớn, nhìn chung (khoảng 80-90% trở lên) = だいたい.",
            {
                "B": "まったく: Hoàn toàn (hoàn toàn không, hoặc hoàn toàn đúng).",
                "C": "かろうじて: Suýt soát, chật vật lắm mới làm được gì đó.",
                "D": "めったに: Hiếm khi (đi với phủ định)."
            }
        ),
        (
            "N2_04_M5_02",
            "N2-VOC-PARA",
            "Mondai 5: 言い換え類義",
            "この地域では、冬でも雪が降ることは【まれだ】。",
            "まれだ",
            [("A", "めったにない"), ("B", "当たり前だ"), ("C", "日常茶飯事だ"), ("D", "避けられない")],
            "A",
            "まれだ（稀だ）: Hiếm có, rất ít khi xảy ra = めったにない.",
            {
                "B": "当たり前だ: Đương nhiên, chuyện bình thường hiển nhiên.",
                "C": "日常茶飯事だ: Chuyện thường ngày ở huyện, xảy ra như cơm bữa.",
                "D": "避けられない: Không thể tránh khỏi."
            }
        ),
        (
            "N2_04_M5_03",
            "N2-VOC-PARA",
            "Mondai 5: 言い換え類義",
            "司会者が手で【合図】を送ると、スピーカーが登壇した。",
            "合図",
            [("A", "サイン"), ("B", "拍手"), ("C", "挨拶"), ("D", "抗議")],
            "A",
            "合図（あいず）: Ra hiệu, gửi tín hiệu = サイン (sign / signal).",
            {
                "B": "拍手: Vỗ tay tán thưởng.",
                "C": "挨拶: Chào hỏi, phát biểu chào mừng.",
                "D": "抗議: Khiếu nại, phản đối."
            }
        ),
        (
            "N2_04_M5_04",
            "N2-VOC-PARA",
            "Mondai 5: 言い換え類義",
            "海外赴任の打診を受けたが、家族のことを考えて返答を【ためらった】。",
            "ためらった",
            [("A", "迷った"), ("B", "焦った"), ("C", "断った"), ("D", "喜んだ")],
            "A",
            "ためらう: Lưỡng lự, do dự, phân vân chưa đưa ra quyết định ngay = 迷った (do dự, băn khoăn).",
            {
                "B": "焦った: Vội vàng, cuống cuồng lo lắng.",
                "C": "断った: Đã từ chối dứt khoát.",
                "D": "喜んだ: Đã vui mừng hân hoan."
            }
        ),
        (
            "N2_04_M5_05",
            "N2-VOC-PARA",
            "Mondai 5: 言い換え類義",
            "彼は誰にも告げずに、【ひそかに】転職の準備を進めていた。",
            "ひそかに",
            [("A", "こっそり"), ("B", "堂々と"), ("C", "公然と"), ("D", "着実に")],
            "A",
            "ひそかに（密かに）: Lén lút, âm thầm, giấu giếm không để người khác biết = こっそり.",
            {
                "B": "堂々と: Đường hoàng, đàng hoàng công khai.",
                "C": "公然と: Công khai trước bàn dân thiên hạ.",
                "D": "着実に: Một cách vững chắc, từng bước vững chãi."
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
            "N2_04_M6_01",
            "N2-VOC-USE",
            "Mondai 6: 用法",
            "「けなす」の使い方が最も適切なものを選びなさい。",
            "けなす",
            [
                ("A", "どんなに努力しても、他人の欠点ばかりをけなす態度は改めるべきだ。"),
                ("B", "彼女は毎日部屋を綺麗にけなして、快適な空間を保っている。"),
                ("C", "激しい雨で川の水が氾濫し、周囲の田畑をけなしてしまった。"),
                ("D", "素晴らしい成果を上げた同僚の功績を、皆で心からけなした。")
            ],
            "A",
            "けなす（貶す）: Chê bai thậm tệ, nói xấu, hạ thấp giá trị của người khác một cách ác ý. Câu A dùng đúng ngữ cảnh chê bai khuyết điểm của người khác.",
            {
                "B": "Dọn dẹp phòng sạch sẽ phải dùng 掃除する hoặc 片付ける, không dùng けなす.",
                "C": "Nước sông tràn làm ngập ruộng đồng phải dùng 飲み込む hoặc 押し流す, không dùng けなす.",
                "D": "Khen ngợi công tích đồng nghiệp phải dùng 称える (たたえる) hoặc 褒める (ほめる), けなす mang nghĩa ngược lại hoàn toàn."
            }
        ),
        (
            "N2_04_M6_02",
            "N2-VOC-USE",
            "Mondai 6: 用法",
            "「てきぱき」の使い方が最も適切なものを選びなさい。",
            "てきぱき",
            [
                ("A", "新しく配属された事務員は、指示された書類整理を手際よくてきぱきと処理した。"),
                ("B", "彼はいつも優柔不断で、何を決めるにもてきぱきと時間がかかってしまう。"),
                ("C", "階段から落ちて足を怪我してしまい、痛くててきぱきと歩くことができない。"),
                ("D", "スープの味が薄かったので、塩とコショウをてきぱきと加えた。")
            ],
            "A",
            "てきぱき: Tháo vát, nhanh nhẹn, dứt khoát giải quyết công việc đâu ra đấy. Câu A mô tả xử lý tài liệu gọn gàng nhanh nhẹn là hoàn toàn chính xác.",
            {
                "B": "Do dự tốn nhiều thời gian thì mâu thuẫn trực tiếp với てきぱき (nhanh gọn).",
                "C": "Bị đau chân đi khập khiễng hoặc không đi được bình thường (chậm chạp), không dùng てきぱき.",
                "D": "Nêm gia vị vừa phải thì dùng さっと hoặc 少々, không dùng てきぱき."
            }
        ),
        (
            "N2_04_M6_03",
            "N2-VOC-USE",
            "Mondai 6: 用法",
            "「なだらか」の使い方が最も適切なものを選びなさい。",
            "なだらか",
            [
                ("A", "この山は傾斜がなだらかなので、登山初心者や子供連れでも無理なく登れる。"),
                ("B", "彼の性格はなだらかで、いつも些細なことで激しく怒り出す。"),
                ("C", "道路工事のせいでアスファルトがなだらかに壊れて通行止めになった。"),
                ("D", "締め切りが迫っているため、プロジェクトの進行をなだらかに早めよう。")
            ],
            "A",
            "なだらか: Thoai thoải, là là, độ dốc nhẹ nhàng êm ả (dùng cho địa hình sườn núi, đồi dốc). Câu A mô tả sườn núi dốc thoai thoải rất dễ leo là chuẩn xác.",
            {
                "B": "Tính cách dễ nổi nóng mâu thuẫn với ý nhẹ nhàng ôn hòa (nếu nói tính tình hiền hậu dùng 穏やか).",
                "C": "Đường hỏng hóc vỡ nát dùng ひどく hoặc 無残に, không dùng なだらか.",
                "D": "Đẩy nhanh tiến độ dùng 急速に hoặc 大幅に, なだらか không dùng bổ nghĩa cho động từ 早める."
            }
        ),
        (
            "N2_04_M6_04",
            "N2-VOC-USE",
            "Mondai 6: 用法",
            "「気が散る」の使い方が最も適切なものを選びなさい。",
            "気が散る",
            [
                ("A", "隣の部屋から大音量の音楽が聞こえてくると、集中できずに気が散ってしまう。"),
                ("B", "春になって庭の桜の花が満開になり、美しい気が散った。"),
                ("C", "長年の悩みが解決して、ようやく胸のつかえが取れて気が散った。"),
                ("D", "彼の無礼な態度を見ていたら、だんだん怒りで気が散ってきた。")
            ],
            "A",
            "気が散る（きがちる）: Bị phân tâm, xao nhãng, không thể tập trung tư tưởng vào việc đang làm. Câu A mô tả tiếng ồn làm mất tập trung là tự nhiên và chính xác.",
            {
                "B": "Hoa anh đào rơi rụng dùng 花が散る, không dùng 気が散る.",
                "C": "Trút bỏ được gánh nặng lo âu dùng 安心した hoặc 気が晴れた, không dùng 気が散る.",
                "D": "Cơn giận bốc lên dùng 腹が立つ hoặc 怒りがこみ上げる, không dùng 気が散る."
            }
        ),
        (
            "N2_04_M6_05",
            "N2-VOC-USE",
            "Mondai 6: 用法",
            "「重宝」の使い方が最も適切なものを選びなさい。",
            "重宝",
            [
                ("A", "この小型多機能ハサミは、段ボールの開封から細かい作業まで幅広く使えて重宝している。"),
                ("B", "彼女は重宝な性格なので、誰とでもすぐに喧嘩をしてしまう。"),
                ("C", "今夜の月は重宝に美しく輝いていて、夜空に見とれてしまった。"),
                ("D", "電車が遅延したせいで、大事な商談の時間に重宝に遅刻してしまった。")
            ],
            "A",
            "重宝（ちょうほう）: Tiện dụng, hữu ích, quý báu và được trân trọng sử dụng thường xuyên (như 重宝している / 重宝な道具). Câu A mô tả cây kéo đa năng tiện ích dùng hàng ngày là chuẩn xác.",
            {
                "B": "Tính cách hay gây gổ không thể dùng 重宝 (tính từ/danh từ chỉ sự tiện ích có ích).",
                "C": "Trăng sáng đẹp dùng 非常に hoặc とても, không dùng phó từ *重宝に.",
                "D": "Đến muộn giờ dùng 大幅に遅刻した, không dùng 重宝."
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
    # MONDAI 7: 文法形式の判断 (Sentential Grammar 1 - 12 items)
    # =========================================================================
    m7_raw = [
        (
            "N2_04_M7_01",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "毎晩これほど夜遅くまで机に向かって猛勉強しているのだから、今回の国家試験には必ず合格する（　　）。",
            [("A", "に相違ない"), ("B", "っこない"), ("C", "にすぎない"), ("D", "わけがない")],
            "A",
            "〜に相違ない（にそういない）: Chắc chắn là, không thể sai được (suy đoán chắc nịch dựa trên căn cứ rõ ràng: học chăm chỉ mỗi đêm).",
            {
                "B": "っこない: Tuyệt đối không thể nào (mang nghĩa phủ định hoàn toàn, trái ngược ngữ cảnh khen ngợi nỗ lực).",
                "C": "にすぎない: Chỉ là... không hơn không kém (đánh giá thấp, không hợp ngữ cảnh).",
                "D": "わけがない: Lẽ nào lại... không có lý nào (phủ định tính khả thi, ngược ý câu)."
            }
        ),
        (
            "N2_04_M7_02",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "親友が長年の苦労を乗り越えて夢を叶えたという知らせを聞いて、嬉しさのあまり涙を（　　）。",
            [("A", "流すわけにはいかない"), ("B", "流さずにはいられなかった"), ("C", "流すはずがなかった"), ("D", "流すどころではなかった")],
            "B",
            "〜ずにはいられない: Không thể không... / không kìm nén được cảm xúc tuôn trào. Khi nghe tin bạn thân thành công sau bao gian nan, quá vui sướng nên không kìm được nước mắt (涙を流さずにはいられなかった).",
            {
                "A": "流すわけにはいかない: Không thể khóc được vì định kiến xã hội hoặc lý do luân lý (không hợp tâm trạng vui mừng).",
                "C": "流すはずがなかった: Lẽ ra không bao giờ khóc (mang tính phán đoán khách quan, không hợp trải nghiệm cảm xúc cá nhân).",
                "D": "流すどころではなかった: Không có tâm trí đâu mà khóc (ngữ cảnh nguy cấp, bận rộn, không hợp)."
            }
        ),
        (
            "N2_04_M7_03",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "今年で会社設立30周年を迎えたのを（　　）、ロゴマークのデザインを一新することにした。",
            [("A", "機に"), ("B", "末に"), ("C", "あげくに"), ("D", "ついでに")],
            "A",
            "〜を機に（〜をきに）: Nhân dịp, lấy cơ hội/cột mốc quan trọng này làm động lực thay đổi (nhân dịp kỷ niệm 30 năm thành lập công ty).",
            {
                "B": "末に: Sau một hồi đắn đo/vất vả gian nan (thường dùng sau chuỗi hành động trăn trở, như 悩んだ末に).",
                "C": "あげくに: Rốt cuộc chuốc lấy kết cục tiêu cực sau thời gian dài.",
                "D": "ついでに: Tiện thể, nhân tiện làm việc phụ khi đang làm việc chính (không phù hợp với quyết định chiến lược đổi logo kỷ niệm 30 năm)."
            }
        ),
        (
            "N2_04_M7_04",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "事前準備も練習も全くしていない素人の彼が、プロの大会で優勝など（　　）。",
            [("A", "できっこない"), ("B", "できるに違いない"), ("C", "できないことはない"), ("D", "できるはずだ")],
            "A",
            "〜っこない: Tuyệt đối không thể nào / làm sao mà làm được (khẩu ngữ khẳng định tính bất khả thi dựa trên thực tế không chuẩn bị gì).",
            {
                "B": "できるに違いない: Chắc chắn làm được (trái ngược hoàn toàn với tiền đề người nghiệp dư không tập luyện).",
                "C": "できないことはない: Không phải là không làm được (khẳng định nhẹ có thể làm được, mâu thuẫn).",
                "D": "できるはずだ: Đương nhiên làm được (mâu thuẫn tiền đề)."
            }
        ),
        (
            "N2_04_M7_05",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "新工場の建設を始める（　　）、周辺地域の住民を対象とした環境説明会が開かれた。",
            [("A", "にあたって"), ("B", "につれて"), ("C", "にしては"), ("D", "に反して")],
            "A",
            "〜にあたって: Nhân dịp, khi chuẩn bị bắt đầu một sự kiện quan trọng có tính bước ngoặt (trước khi khởi công xây nhà máy mới).",
            {
                "B": "につれて: Càng ngày càng... kéo theo sự biến đổi tỷ lệ thuận.",
                "C": "にしては: Tuy... nhưng mà lại (ngạc nhiên trái với tiêu chuẩn thông thường).",
                "D": "に反して: Trái với dự đoán/kỳ vọng."
            }
        ),
        (
            "N2_04_M7_06",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "大切な友人との約束だから、たとえどんな事情があろうとも破る（　　）と心に誓った。",
            [("A", "まい"), ("B", "ものか"), ("C", "べきだ"), ("D", "ことか")],
            "A",
            "〜まい: Quyết không... (ý chí phủ định mạnh mẽ của người nói). Động từ nhóm 1 破る kết hợp thành 破るまい (quyết không phá vỡ lời thề).",
            {
                "B": "ものか: Tuyệt đối không bao giờ (khẩu ngữ thách thức, không đi kèm trực tiếp với '心に誓った' như cấu trúc 〜まいと誓う).",
                "C": "べきだ: Nên làm (khuyên bảo, không phải ý chí phủ định bảo vệ lời hứa).",
                "D": "ことか: Biết bao nhiêu (cảm thán, không hợp ngữ pháp)."
            }
        ),
        (
            "N2_04_M7_07",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "彼がこれほどの短期間で大きな成果を上げられたのは、日々の地道な努力の（　　）。",
            [("A", "たまものにほかならない"), ("B", "わけではない"), ("C", "どころではない"), ("D", "おそれがある")],
            "A",
            "〜にほかならない: Chính là, không gì khác ngoài... (khẳng định bản chất duy nhất: chính là kết tinh của nỗ lực bền bỉ hàng ngày).",
            {
                "B": "わけではない: Không hẳn là (phủ định một phần, làm giảm giá trị nỗ lực).",
                "C": "どころではない: Không phải lúc để làm gì (không hợp ngữ nghĩa).",
                "D": "おそれがある: Có e ngại/nguy cơ xảy ra điều xấu (không đi với thành quả tốt đẹp)."
            }
        ),
        (
            "N2_04_M7_08",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "故郷を離れて一人暮らしを始めてから、母の手料理が食べたくて（　　）。",
            [("A", "たまらない"), ("B", "かなわない"), ("C", "ならない"), ("D", "すまない")],
            "A",
            "〜たくてたまらない: Rất muốn... / vô cùng thèm muốn đến mức không kìm lòng được (biểu thị mong muốn thể xác/cảm xúc mãnh liệt của ngôi thứ nhất).",
            {
                "B": "かなわない: Không thể chịu nổi sự bất tiện/phiền toái do ngoại cảnh gây ra (như うるさくてかなわない).",
                "C": "ならない: Thường đi với cảm xúc lo âu, băn khoăn tự nhiên khởi phát (như 心配でならない), ít đi với 〜たくて.",
                "D": "すまない: Có lỗi, áy náy (không tạo thành mẫu ngữ pháp chỉ mong muốn)."
            }
        ),
        (
            "N2_04_M7_09",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "新入社員たちは、会社の基本理念や行動規範に（　　）誠実に業務を遂行している。",
            [("A", "沿って"), ("B", "めぐって"), ("C", "関して"), ("D", "わたって")],
            "A",
            "〜に沿って（〜にそって）: Men theo, tuân thủ đúng theo đường lối, quy chuẩn, phương châm đã định (theo đúng triết lý cơ bản và quy tắc ứng xử của công ty).",
            {
                "B": "めぐって: Xoay quanh tranh chấp/bàn tán về một chủ đề (như 遺産をめぐって争う).",
                "C": "関して: Liên quan đến (chỉ nói về chủ đề thông tin, không mang nghĩa tuân thủ hành vi).",
                "D": "わたって: Suốt cả một không gian rộng lớn hoặc khoảng thời gian dài."
            }
        ),
        (
            "N2_04_M7_10",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "健康診断で医師から運動不足を指摘されたのを（　　）、毎朝のジョギングを始めた。",
            [("A", "契機に"), ("B", "中心に"), ("C", "もとに"), ("D", "先立って")],
            "A",
            "〜を契機に（〜をけいきに）: Lấy biến cố/sự kiện làm mốc thời điểm đánh dấu sự thay đổi tích cực trong lối sống hoặc tổ chức (lấy việc bị bác sĩ cảnh báo làm cột mốc bắt đầu chạy bộ).",
            {
                "B": "中心に: Lấy cái gì làm trung tâm/trọng tâm hoạt động.",
                "C": "もとに: Dựa trên nền tảng/chất liệu nguyên bản.",
                "D": "先立って: Trước khi tiến hành một sự kiện lớn (chuẩn bị trước)."
            }
        ),
        (
            "N2_04_M7_11",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "今日の会議は重要な経営方針を決定する場なので、冗談（　　）で真剣に議論を進めたい。",
            [("A", "ぬき"), ("B", "ぎみ"), ("C", "がち"), ("D", "げ")],
            "A",
            "〜ぬきで（〜抜きで）: Bỏ qua, dẹp sang một bên, không tính tới (gạt chuyện đùa giỡn sang một bên để thảo luận nghiêm túc).",
            {
                "B": "ぎみ: Có triệu chứng, hơi có vẻ tiêu cực (như 風邪ぎみ).",
                "C": "がち: Hay bị, có xu hướng dễ xảy ra (như 留守がち, 遅刻しがち).",
                "D": "げ: Trông có vẻ (như 悲しげ, 自慢げ)."
            }
        ),
        (
            "N2_04_M7_12",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "留学生活の1年間を（　　）、語学力だけでなく異文化を柔軟に受け入れる寛容さも身につけた。",
            [("A", "通じて"), ("B", "おいて"), ("C", "応じて"), ("D", "対して")],
            "A",
            "〜を通じて（〜をつうじて）: Thông qua toàn bộ quá trình hoặc phương tiện trung gian (thông qua suốt 1 năm sống du học).",
            {
                "B": "おいて: Tại địa điểm hoặc lĩnh vực (như 会場において).",
                "C": "応じて: Tùy theo, tương ứng với điều kiện (như 予算に応じて).",
                "D": "対して: Đối với, đối nghịch lại với (như 質問に対して)."
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
    # Strict syntactic locks enforcing exactly ONE valid permutation out of 24
    # =========================================================================
    m8_raw = [
        (
            "N2_04_M8_01",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "新人研修を（　　）（　　） ★ （　　）実践で役立つ。",
            [
                ("A", "受けるにあたって、"),
                ("B", "教わったビジネスマナーは、"),
                ("C", "現場の"),
                ("D", "日々の")
            ],
            "D",
            "Thứ tự đúng: A - B - D - C (受けるにあたって、 教わったビジネスマナーは、 日々の 現場の). Cấu trúc: 〜にあたって (khi bắt đầu). Vế 1: [A 受けるにあたって、] đi liền sau danh từ 新人研修を. Vế 2: [B 教わったビジネスマナーは、] đóng vai trò chủ ngữ có trợ từ は. Cụm định ngữ bổ nghĩa cho 実践: [D 日々の] bổ nghĩa cho [C 現場の], nối tiếp vào 実践で役立つ. Thứ tự duy nhất: A -> B -> D -> C. Vị trí ngôi sao ★ là D (日々の).",
            {
                "A": "[Vị trí 1] Cụm động từ kết hợp với tân ngữ 新人研修を.",
                "B": "[Vị trí 2] Chủ ngữ chính của câu, có dấu phẩy ngắt vế.",
                "C": "[Vị trí 4] Đứng liền trước danh từ 実践."
            }
        ),
        (
            "N2_04_M8_02",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "どんなに困難な課題で（　　）（　　） ★ （　　）見出せるはずだ。",
            [
                ("A", "あろうとも、"),
                ("B", "諦めずに考え抜けば、"),
                ("C", "解決の"),
                ("D", "糸口を")
            ],
            "C",
            "Thứ tự đúng: A - B - C - D (あろうとも、 諦めずに考え抜けば、 解決の 糸口を). Cấu trúc: どんなに〜ようとも (cho dù... đến mức nào đi chăng nữa). [A あろうとも、] đi với どんなに困難な課題で. Vế điều kiện tiếp theo: [B 諦めずに考え抜けば、]. Vế sau: [C 解決の] bổ nghĩa cho tân ngữ [D 糸口を] của động từ 見出せる. Thứ tự duy nhất: A -> B -> C -> D. Vị trí ngôi sao ★ là C (解決の).",
            {
                "A": "[Vị trí 1] Hoàn thiện cấu trúc nhượng bộ どんなに〜あろうとも.",
                "B": "[Vị trí 2] Vế điều kiện giả định có dấu phẩy.",
                "D": "[Vị trí 4] Tân ngữ đứng liền trước động từ 見出せる."
            }
        ),
        (
            "N2_04_M8_03",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "今回の省エネ対策は、（　　）（　　） ★ （　　）寄与する。",
            [
                ("A", "コスト削減に"),
                ("B", "とどまらず、"),
                ("C", "地球温暖化の"),
                ("D", "防止にも")
            ],
            "C",
            "Thứ tự đúng: A - B - C - D (コスト削減に とどまらず、 地球温暖化の 防止にも). Cấu trúc ngữ pháp N2: 〜にとどまらず (không chỉ dừng lại ở...). [A コスト削減に] đi với [B とどまらず、]. Vế tích lũy tiếp theo: [C 地球温暖化の] bổ nghĩa cho danh từ [D 防止にも], đi liền trước động từ 寄与する. Thứ tự duy nhất: A -> B -> C -> D. Vị trí ngôi sao ★ là C (地球温暖化の).",
            {
                "A": "[Vị trí 1] Đi sau chủ ngữ 今回の省エネ対策は.",
                "B": "[Vị trí 2] Mẫu liên kết 〜にとどまらず、 có dấu phẩy.",
                "D": "[Vị trí 4] Đứng liền trước động từ 寄与する (đóng góp vào việc phòng chống)."
            }
        ),
        (
            "N2_04_M8_04",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "一度引き受けた仕事で（　　）（　　） ★ （　　）責任がある。",
            [
                ("A", "あるからには、"),
                ("B", "途中で投げ出さずに"),
                ("C", "最後まで"),
                ("D", "やり抜く")
            ],
            "C",
            "Thứ tự đúng: A - B - C - D (あるからには、 途中で投げ出さずに 最後まで やり抜く). Cấu trúc ngữ pháp N2: 〜からには (một khi đã... thì phải). [A あるからには、] đi với 一度引き受けた仕事で. Vế sau thể hiện nghĩa vụ: [B 途中で投げ出さずに] đi với trạng từ [C 最後まで], bổ nghĩa cho động từ [D やり抜く] (định ngữ cho danh từ 責任). Thứ tự duy nhất: A -> B -> C -> D. Vị trí ngôi sao ★ là C (最後まで).",
            {
                "A": "[Vị trí 1] Hoàn thành vế điều kiện tiền đề 〜あるからには、.",
                "B": "[Vị trí 2] Cụm trạng từ phủ định liên kết.",
                "D": "[Vị trí 4] Động từ thể từ điển bổ nghĩa cho danh từ 責任."
            }
        ),
        (
            "N2_04_M8_05",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "市場調査の（　　）（　　） ★ （　　）開発を進めるべきだ。",
            [
                ("A", "客観的な"),
                ("B", "データに"),
                ("C", "基づいて、"),
                ("D", "新製品の")
            ],
            "C",
            "Thứ tự đúng: A - B - C - D (客観的な データに 基づいて、 新製品の). Cấu trúc ngữ pháp N2: 〜に基づいて (dựa trên cơ sở...). Tính từ [A 客観的な] bổ nghĩa cho danh từ [B データに]. Đi liền sau là mẫu ngữ pháp [C 基づいて、]. Cụm định ngữ [D 新製品の] bổ nghĩa trực tiếp cho danh từ 開発. Thứ tự duy nhất: A -> B -> C -> D. Vị trí ngôi sao ★ là C (基づいて、).",
            {
                "A": "[Vị trí 1] Tính từ đuôi な bổ nghĩa cho danh từ データ.",
                "B": "[Vị trí 2] Danh từ đi với trợ từ に trước 基づいて.",
                "D": "[Vị trí 4] Danh từ sở hữu bổ nghĩa cho danh từ 開発."
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
    # =========================================================================
    p9_text = """人工知能（AI）技術の急速な進展に伴い、ビジネスの現場では業務の自動化や効率化がめざましい勢いで進んでいる。これまで熟練の社員が多大な時間を費やして行ってきたデータ分析や定型的な書類作成などは、今やAIが瞬時に高精度で処理できるようになった。こうした変化は、生産性の向上という観点から見れば大いに歓迎すべきこと（ 43 ）。

しかし、ここで忘れてはならないのは、AIが出力する結果はあくまで過去の膨大なデータの統計的処理に基づいた「推論」にすぎないという点である。（ 44 ）、前例のない突発的な事態への対応や、組織における倫理的な価値判断が求められる局面においては、機械任せにするわけにはいかない。

複雑に利害が対立する状況で最適な合意点を見出し、関係者の納得感を得るための対話を進める能力は、生身の人間（ 45 ）発揮できない固有の強みである。AIが提示するデータを鵜呑みにするのではなく、その背景にある文脈や人間の感情を深く読み取った上で最終的な意思決定を下す力（ 46 ）、これからの時代を生きるビジネスパーソンに真に求められているのではないだろうか。

技術の進化を恐れて拒絶するのではなく、AIの長所を賢く活用し（ 47 ）、人間ならではの創造性や判断力を磨き続ける姿勢が不可欠である。"""

    m9_raw = [
        (
            "N2_04_M9_01",
            "N2-GR-TXT",
            "Mondai 9: 文章の文法 (43)",
            "空欄（ 43 ）に入る最も適切なものを選びなさい。",
            [("A", "にほかならない"), ("B", "わけがない"), ("C", "にすぎない"), ("D", "おそれがある")],
            "A",
            "Cấu trúc 〜にほかならない (chính là, không gì khác ngoài...). Đoạn văn khẳng định việc tăng năng suất nhờ AI chắc chắn là điều đáng hoan nghênh (大いに歓迎すべきことにほかならない).",
            {
                "B": "わけがない: Tuyệt đối không thể (phủ định, trái ngữ cảnh tích cực).",
                "C": "にすぎない: Chỉ là... không đáng kể (hạ thấp ý nghĩa, chưa phù hợp với ý khẳng định ở đoạn 1).",
                "D": "おそれがある: Có nguy cơ xảy ra điều xấu (không đi với điều tích cực 歓迎すべきこと)."
            }
        ),
        (
            "N2_04_M9_02",
            "N2-GR-TXT",
            "Mondai 9: 文章の文法 (44)",
            "空欄（ 44 ）に入る最も適切なものを選びなさい。",
            [("A", "したがって"), ("B", "それゆえに"), ("C", "とはいえ"), ("D", "なぜなら")],
            "C",
            "Liên từ nghịch xích 〜とはいえ (mặc dù là như vậy, tuy nói là thế nhưng...). Dùng để chuyển ý sang mặt hạn chế của AI đối với các tình huống chưa có tiền lệ.",
            {
                "A": "したがって: Do đó, vì vậy (chỉ kết quả thuận, không tạo tính đối lập).",
                "B": "それゆえに: Do nguyên nhân đó mà (nguyên nhân kết quả thuận).",
                "D": "なぜなら: Bởi vì là (giải thích lý do cho câu trước, không hợp ngữ cảnh chuyển ý)."
            }
        ),
        (
            "N2_04_M9_03",
            "N2-GR-TXT",
            "Mondai 9: 文章の文法 (45)",
            "空欄（ 45 ）に入る最も適切なものを選びなさい。",
            [("A", "ならでは"), ("B", "ならではの"), ("C", "にとって"), ("D", "として")],
            "A",
            "Mẫu ngữ pháp 〜ならでは (chỉ có ở... / chỉ riêng... mới có). '生身の人間ならでは発揮できない' (chỉ có con người bằng xương bằng thịt mới có thể phát huy).",
            {
                "B": "ならではの: Đi trực tiếp bổ nghĩa cho danh từ phía sau (như 人間ならではの強み), ở đây đi trước động từ 発揮できない nên phải dùng ならでは.",
                "C": "にとって: Đối với (chỉ góc độ lập trường, không diễn tả tính độc nhất như ならでは).",
                "D": "として: Với tư cách là (không diễn tả sự độc quyền năng lực)."
            }
        ),
        (
            "N2_04_M9_04",
            "N2-GR-TXT",
            "Mondai 9: 文章の文法 (46)",
            "空欄（ 46 ）に入る最も適切なものを選びなさい。",
            [("A", "こそが"), ("B", "ばかりが"), ("C", "さえも"), ("D", "までも")],
            "A",
            "Trợ từ nhấn mạnh 〜こそが (chính là...). '意思決定を下す力こそが、...求められているのではないだろうか' (Chính năng lực đưa ra quyết định cuối cùng mới là điều được đòi hỏi).",
            {
                "B": "ばかりが: Chỉ toàn là (mang sắc thái tiêu cực hoặc hạn định thu hẹp).",
                "C": "さえも: Ngay cả... cũng (nhấn mạnh mức độ cực đoan).",
                "D": "までも: Đến cả... (chỉ phạm vi lan tới, không hợp để nhấn mạnh chủ ngữ trọng tâm)."
            }
        ),
        (
            "N2_04_M9_05",
            "N2-GR-TXT",
            "Mondai 9: 文章の文法 (47)",
            "空欄（ 47 ）に入る最も適切なものを選びなさい。",
            [("A", "つつも"), ("B", "ながらに"), ("C", "きりに"), ("D", "げに")],
            "A",
            "Cấu trúc liên kết 〜つつも (vừa... nhưng đồng thời...). 'AIの長所を賢く活用しつつも、人間ならではの創造性や判断力を磨き続ける' (Vừa tận dụng thông minh thế mạnh của AI, nhưng đồng thời vẫn phải mài giũa óc phán đoán sáng tạo của con người).",
            {
                "B": "ながらに: Giữ nguyên trạng thái (như 涙ながらに, 生まれながらに).",
                "C": "きりに: Sau khi... không có gì tiếp diễn (như 出かけたきり).",
                "D": "げに: Trông có vẻ (như 自慢げに)."
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
            "N2_04_M10_01",
            "社員向けセキュリティ通知",
            """社員各位
テレワークの普及に伴い、社外から社内ネットワークへ接続する機会が増加しています。これに伴い、第三者による不正アクセスや情報漏洩のリスクが高まっています。
社外で業務を行う際は、必ず会社から貸与された専用端末を使用し、カフェ等の暗号化されていない公衆無線LAN（フリーWi-Fi）への接続は厳禁とします。やむを得ず外出先で通信を行う場合は、会社支給のモバイルWi-Fiルーターまたはスマートフォンのテザリング機能を活用してください。
情報セキュリティの遵守は、全社員の重大な責務です。一人ひとりが高い危機意識を持って日々の業務に臨んでください。""",
            "この通知で社員に対して最も強く求められていることは何か。",
            [
                ("A", "社外で作業する際は、フリーWi-Fiを使わず指定された安全な通信手段を用いること。"),
                ("B", "情報漏洩を防ぐため、社外でのテレワーク業務を全面的に中止すること。"),
                ("C", "専用端末の貸与を希望する社員は、事前にセキュリティ講習を受講すること。"),
                ("D", "カフェなどの公共の場所では、長時間のパソコン作業を控えること。")
            ],
            "A",
            "Thông báo nhấn mạnh: cấm tuyệt đối kết nối Wi-Fi công cộng không mã hóa tại quán cà phê ('公衆無線LANへの接続は厳禁') và bắt buộc dùng thiết bị phát Wi-Fi hoặc tethering được cấp phát an toàn.",
            {
                "B": "Thông báo không yêu cầu ngừng làm việc từ xa (テレワーク) mà chỉ quy định về an toàn bảo mật mạng.",
                "C": "Không đề cập đến việc phải học khóa tập huấn mới được mượn máy tính.",
                "D": "Không cấm ngồi làm việc lâu ở quán cà phê, cốt lõi là cấm dùng mạng Wi-Fi chùa không bảo mật."
            }
        ),
        (
            "N2_04_M10_02",
            "SNS時代の情報リテラシーに関する論説",
            """SNSの普及により、私たちは誰でも手軽に世界中の情報を瞬時に入手できるようになった。しかし、その手軽さの裏で、真偽の不確かな情報や極端な偏見を含んだ言説が爆発的に拡散するリスクも増大している。
私たちは、自らの価値観に心地よい情報ばかりを無批判に受け入れ、都合の悪い事実を無視してしまう心理的傾向（確証バイアス）を持っている。情報を受け取った際には、発信者の意図や根拠となるデータの出所を立ち止まって検証する「批判的思考（クリティカル・シンキング）」の習慣こそが、情報社会を主体的に生きるための防波堤となる。""",
            "筆者が現代の情報環境において重要だと主張していることは何か。",
            [
                ("A", "自分が信じたい情報だけでなく、根拠や発信元を吟味して客観的に判断すること。"),
                ("B", "誤った情報の拡散を防ぐため、SNSの利用時間をできる限り制限すること。"),
                ("C", "自分と異なる意見を持つ発信者に対して、積極的に反論のコメントを送ること。"),
                ("D", "公的機関が発表した公式データ以外の情報には一切触れないようにすること。")
            ],
            "A",
            "Tác giả cảnh báo xu hướng tâm lý chỉ tin những gì mình muốn tin (確証バイアス) và nhấn mạnh sự cần thiết của tư duy phản biện: dừng lại kiểm tra dụng ý của người đăng và nguồn gốc dữ liệu khách quan.",
            {
                "B": "Tác giả không khuyên hạn chế thời gian dùng mạng xã hội mà khuyên nâng cao năng lực thẩm định thông tin.",
                "C": "Không hề đề cập đến việc đi tranh luận hay phản bác gay gắt người khác.",
                "D": "Không khuyên tuyệt đối tẩy chay thông tin không chính thống, mà là phải có tư duy chọn lọc và kiểm chứng."
            }
        ),
        (
            "N2_04_M10_03",
            "オンライン決済システム定期メンテナンスのお知らせ",
            """お客様各位
日頃より当オンラインショップをご利用いただき、誠にありがとうございます。
下記の日程におきまして、決済システムの安全性向上およびサーバー増強のための定期メンテナンスを実施いたします。
メンテナンス期間中は、クレジットカード決済およびコンビニ後払い決済がご利用いただけません。なお、代金引換でのお買い物につきましては通常通りご利用いただけます。
お客様には大変ご不便をおかけいたしますが、何卒ご理解とご協力を賜りますようお願い申し上げます。
【実施日時】2026年11月15日（日）午前2:00 〜 午前6:00""",
            "このメンテナンス期間中における買い物の利用について、正しいものはどれか。",
            [
                ("A", "代金引換を選択すれば、メンテナンス中であっても注文を完了できる。"),
                ("B", "すべての決済方法が停止するため、商品の閲覧のみが可能となる。"),
                ("C", "コンビニ後払い決済に限り、手数料無料で利用できる。"),
                ("D", "午前2時前にカートに入れた商品であれば、クレジットカード決済が可能である。")
            ],
            "A",
            "Thông báo ghi rõ: '代金引換でのお買い物につきましては通常通りご利用いただけます' (Thanh toán khi nhận hàng COD vẫn sử dụng bình thường trong thời gian bảo trì).",
            {
                "B": "Sai vì phương thức thanh toán COD vẫn hoạt động bình thường, không phải ngừng toàn bộ.",
                "C": "Thanh toán qua cửa hàng tiện lợi bị tạm dừng hoàn toàn, không phải được miễn phí.",
                "D": "Trong khung giờ 2:00 - 6:00 sáng, thanh toán thẻ tín dụng bị khóa hoàn toàn, bất kể thêm vào giỏ hàng lúc nào."
            }
        ),
        (
            "N2_04_M10_04",
            "読書習慣の効用についてのコラム",
            """忙しい日々の中で「本を読む時間がない」と嘆く人は多い。しかし、読書とは単なる知識の蓄積ではなく、他者の視点を追体験し、自分の思考の枠組みを揺さぶる対話のプロセスである。
1日わずか15分でも本を開く習慣を持つことで、日常の喧騒から一時的に距離を置き、物事を複眼的に捉える心の余裕が生まれる。読書を通じて培われる深い集中力と想像力は、AIが台頭するこれからの時代において、人間にしか持ち得ない創造性の源泉となるに違いない。""",
            "この文章で筆者が読書について述べたいことは何か。",
            [
                ("A", "短時間でも本を読む習慣は、視野を広げ独自の思考力や創造性を育む。"),
                ("B", "仕事で成果を上げるためには、専門分野の実用書を多読することが不可欠である。"),
                ("C", "読書に没頭するためには、まとまった休日を確保して静かな環境を作らねばならない。"),
                ("D", "電子書籍の普及により、紙の本をじっくり読む価値は失われつつある。")
            ],
            "A",
            "Tác giả chỉ ra: chỉ cần 15 phút mỗi ngày đọc sách cũng giúp tạm rời xa ồn ào, mở rộng tư duy nhiều chiều và nuôi dưỡng tính sáng tạo độc đáo của con người.",
            {
                "B": "Tác giả nói về việc mở rộng tư duy và đồng cảm với góc nhìn người khác, không hề nói phải đọc nhiều sách kỹ năng thực dụng công việc.",
                "C": "Tác giả nhấn mạnh chỉ cần 15 phút mỗi ngày trong lúc bận rộn, không cần phải đợi có kỳ nghỉ dài ngày.",
                "D": "Không hề đề cập hay so sánh giữa sách giấy và sách điện tử."
            }
        ),
        (
            "N2_04_M10_05",
            "読者の声（都市のごみ分別に関する投稿）",
            """市が導入した新しいプラスチックごみの分別ルールについて、市民の間で戸惑いの声が広がっている。プラスチック製容器包装と製品プラスチックを一括して回収する方針自体はリサイクル推進として理解できるが、品目ごとの細かな基準が周知不足で、収集場所に放置されるケースが目立つ。
制度の趣旨がどんなに素晴らしくても、実際に分別を行う住民の理解と協力が得られなければ実効性は伴わない。市はわかりやすい図解パンフレットの全戸配布や多言語での説明動画の配信など、丁寧な広報活動を早急に行うべきだ。""",
            "投稿者が市に対して求めていることは何か。",
            [
                ("A", "住民が正しく分別できるよう、分かりやすい広報や案内を速やかに行うこと。"),
                ("B", "市民の混乱を避けるため、新しいプラスチック分別制度を直ちに廃止すること。"),
                ("C", "ごみ出しルールに違反した住民に対して、厳しい罰則を科すこと。"),
                ("D", "プラスチックのリサイクル処理施設を増設し、回収回数を増やすこと。")
            ],
            "A",
            "Người gửi bài đồng ý với ý nghĩa tái chế nhưng yêu cầu thành phố phải khẩn trương tuyên truyền rõ ràng (phát tờ rơi hình ảnh dễ hiểu, video đa ngôn ngữ) để người dân hiểu và thực hiện đúng.",
            {
                "B": "Người viết tán thành mục đích bảo vệ môi trường của quy định ('方針自体は...理解できる'), không đòi bãi bỏ.",
                "C": "Không hề đòi hỏi đưa ra hình phạt nghiêm khắc với người dân.",
                "D": "Không đề cập đến việc xây thêm nhà máy rác hay tăng tần suất xe thu gom."
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
    p11_1_text = """組織におけるイノベーションの創出において、近年「心理的安全性（Psychological Safety）」という概念が注目を集めている。心理的安全性とは、チームのメンバーが「自分の考えや率直な意見を発言しても、拒絶されたり嘲笑されたりする恐れがない」と確信できる状態を指す。

かつての伝統的な職場では、上司の指示に忠実に従い、波風を立てないことこそが美徳とみなされる傾向が強かった。しかし、変化が激しく未来の予測が困難な現代において、過去の成功体験にしがみつくトップダウンの意思決定だけでは、新たな価値を生み出すことはできない。現場の社員が失敗を過度に恐れず、未成熟なアイデアや疑問点であっても自由に口にできる環境があって初めて、革新的なブレイクスルーが生まれるのである。

もちろん、心理的安全性とは、単に職場の人間関係が仲良しで居心地が良い「ぬるま湯」の状態を意味するものではない。互いの立場を尊重しながらも、業務の目的や成果に対しては高い基準を共有し、率直に建設的な批判や議論を交わし合える関係性こそが真の心理的安全性である。リーダーの役割は、部下に完璧を求めることではなく、自らも弱みを見せ、誰もが安心して発言できる土壌を粘り強く耕し続けることにある。"""

    m11_1_items = [
        (
            "N2_04_M11_01",
            "「心理的安全性」が組織で重要視されるようになった背景として、筆者が挙げているのはどれか。",
            [
                ("A", "変化の激しい現代では、過去のやり方にとらわれない自由な発言が革新を生むから。"),
                ("B", "若手社員が人間関係のストレスで早期離職するのを防ぐことが最優先だから。"),
                ("C", "上司の指示に従うことよりも、業務の効率化を優先する社員が増えたから。"),
                ("D", "伝統的なトップダウン組織のほうが、不測の事態に迅速に対応できるから。")
            ],
            "A",
            "Đoạn 2 giải thích: trong thời đại biến động khôn lường, các quyết định áp đặt từ trên xuống dựa vào thành công quá khứ không còn tạo ra giá trị mới, mà phải nhờ môi trường nhân viên không sợ thất bại, tự do nói lên ý tưởng thì mới tạo ra đột phá sáng tạo.",
            {
                "B": "Bài viết không bàn về việc ngăn chặn nhân viên trẻ bỏ việc do áp lực quan hệ.",
                "C": "Không nói nhân viên tự ý coi trọng hiệu suất hơn mệnh lệnh cấp trên.",
                "D": "Đoạn 2 chỉ ra mô hình top-down truyền thống không còn thích ứng được, trái ngược hoàn toàn với phương án D."
            }
        ),
        (
            "N2_04_M11_02",
            "筆者が述べる「真の心理的安全性」の説明として、最も適切なものはどれか。",
            [
                ("A", "互いを尊重しつつ高い基準を持ち、建設的な議論や率直な批判を交わせる状態。"),
                ("B", "厳しい指摘や対立を避け、メンバー全員が常に笑顔で心地よく過ごせる状態。"),
                ("C", "失敗したメンバーを一切責めず、個人の責任を組織全体で肩代わりする状態。"),
                ("D", "リーダーが指示を出さず、すべての意思決定を部下の多数決に委ねる状態。")
            ],
            "A",
            "Đoạn 3 khẳng định: an toàn tâm lý thực chất không phải là môi trường dĩ hòa vi quý nhàn hạ (ぬるま湯), mà là mối quan hệ tôn trọng lẫn nhau nhưng cùng chia sẻ tiêu chuẩn cao về công việc, sẵn sàng tranh luận và phê bình mang tính xây dựng.",
            {
                "B": "Đây chính là trạng thái 'ぬるま湯' (dĩ hòa vi quý bề ngoài) mà tác giả đã bác bỏ.",
                "C": "Tác giả không nói xóa bỏ hoàn toàn trách nhiệm cá nhân.",
                "D": "Tác giả nhấn mạnh vai trò của người lãnh đạo trong việc tạo dựng nền tảng cởi mở, chứ không phải buông bỏ trách nhiệm cho cấp dưới biểu quyết."
            }
        ),
        (
            "N2_04_M11_03",
            "この文章において、筆者がリーダーに期待している役割は何か。",
            [
                ("A", "自らの不完全さも開示しながら、誰もが気兼ねなく発言できる環境を整えること。"),
                ("B", "部下の些細なミスも見逃さず、常に完璧な成果を厳格に要求すること。"),
                ("C", "職場の対立を防ぐため、社員間の議論を最小限に抑えて業務を進めること。"),
                ("D", "過去の成功パターンを徹底的にマニュアル化し、部下に忠実に実行させること。")
            ],
            "A",
            "Câu cuối bài viết đúc kết rõ: 'リーダーの役割は、部下に完璧を求めることではなく、自らも弱みを見せ、誰もが安心して発言できる土壌を粘り強く耕し続けることにある' (Vai trò của người lãnh đạo là dám bộc lộ điểm yếu của chính mình và kiên trì vun xới mảnh đất để bất kỳ ai cũng an tâm phát ngôn).",
            {
                "B": "Trái ngược hoàn toàn (tác giả viết '部下に完璧を求めることではなく').",
                "C": "Tác giả khuyến khích thảo luận thẳng thắn xây dựng chứ không khuyên kìm nén tranh luận.",
                "D": "Tác giả phản đối việc máy móc rập khuôn quá khứ."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m11_1_items:
        items.append({
            "id": qid,
            "typeId": "N2-RD-MID",
            "skill": "Reading",
            "category": "Mondai 11: 中文読解 — 組織における心理的安全性",
            "stem": stem,
            "contextPassage": p11_1_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    p11_2_text = """新年の始まりや新生活の節目に、「今年こそは運動を続けよう」「毎日英語を勉強しよう」と意気込んで高い目標を掲げる人は多い。しかし、その決意の多くがわずか数週間で挫折してしまうのはなぜだろうか。認知心理学の研究によれば、人間の脳は急激な変化を「生命を脅かす危険」と感知し、無意識のうちに元の慣れ親しんだ状態に戻ろうとする強力な防御本能（ホメオスタシス）を備えているからである。

意志の力（ウィルパワー）は無限ではなく、日々の仕事や意思決定によって急速に消耗する有限な資源である。したがって、疲弊した状態で「今日も気合を入れて1時間勉強しよう」と念じるやり方は、脳の仕組みから見て極めて持続性に乏しい。

そこで有効となるのが、「マイクロ・ハビット（微小な習慣）」と呼ばれるアプローチである。これは、「腕立て伏せを1回だけする」「テキストを1ページだけ開く」といった、努力を意識することさえ不要なほど極小の行動から始める手法である。行動のハードルを極限まで下げることで、脳の警戒反応を刺激することなく、行動の開始を自動化できる。小さな達成感を脳が報酬として記憶すれば、やがてその行動は意志の力を必要としない無意識の日常習慣へと自然に発展していくのである。"""

    m11_2_items = [
        (
            "N2_04_M11_04",
            "大きな目標を掲げた決意が短期間で挫折しやすい理由として、本文で述べられているのはどれか。",
            [
                ("A", "脳が急激な変化を警戒し、元の安定した状態に戻そうとする本能が働くから。"),
                ("B", "目標を設定する際に、具体的な期限や数値基準を決めていないから。"),
                ("C", "周囲からの応援や励ましが得られず、モチベーションが低下するから。"),
                ("D", "人間には本来、新しい知識を学ぶことに対する強い恐怖心があるから。")
            ],
            "A",
            "Đoạn 1 nêu rõ: theo tâm lý học nhận thức, não bộ xem sự thay đổi đột ngột là nguy hiểm đe dọa sinh tồn và theo bản năng nội cân bằng (homeostasis) sẽ tự động quay trở lại trạng thái quen thuộc cũ.",
            {
                "B": "Đoạn văn không nói do thiếu số liệu hay thời hạn.",
                "C": "Không đề cập đến sự ủng hộ của người xung quanh.",
                "D": "Không phải con người sợ học kiến thức mới, mà là sợ sự xáo trộn thói quen đột ngột."
            }
        ),
        (
            "N2_04_M11_05",
            "筆者が「意志の力」について説明している内容として正しいものはどれか。",
            [
                ("A", "有限な資源であり、日々の活動や判断によって消耗していく性質を持つ。"),
                ("B", "強い信念を持ち続ける限り、疲労に関係なく無限に湧き出るエネルギーである。"),
                ("C", "生まれつきの才能によって決まっており、後天的に鍛えることはできない。"),
                ("D", "目標の難易度が高ければ高いほど、脳内で自動的に補充される。")
            ],
            "A",
            "Đoạn 2 chỉ ra: ý chí (willpower) không phải vô hạn mà là một nguồn tài nguyên hữu hạn bị tiêu hao nhanh chóng qua công việc và các quyết định hàng ngày.",
            {
                "B": "Ngược với tác giả (ý chí không phải là vô hạn).",
                "C": "Tác giả không nói ý chí là do bẩm sinh không rèn luyện được.",
                "D": "Mục tiêu càng cao càng dễ làm kiệt sức ý chí chứ không hề được não tự nạp thêm."
            }
        ),
        (
            "N2_04_M11_06",
            "「マイクロ・ハビット」が習慣化に効果的である最大の理由は何か。",
            [
                ("A", "行動のハードルを最小限にすることで、脳に警戒されずに行動を開始できるから。"),
                ("B", "1回あたりの時間が短いため、1日に何十回も同じ動作を繰り返せるから。"),
                ("C", "誰でも簡単にできる運動を取り入れることで、基礎体力が急速に向上するから。"),
                ("D", "家族や友人と一緒に取り組むことで、サボれない強制力を働かせられるから。")
            ],
            "A",
            "Đoạn 3 kết luận: bằng cách hạ thấp rào cản hành động xuống mức tối thiểu (như chống đẩy 1 cái, mở sách 1 trang), não bộ không bị kích hoạt phản ứng tự vệ chống cự, giúp biến việc bắt đầu hành động thành phản xạ tự động.",
            {
                "B": "Mục đích là bắt đầu dễ dàng chứ không phải lặp lại mấy chục lần mỗi ngày.",
                "C": "Mục tiêu là xây dựng thói quen tâm lý, không phải nâng cao thể lực cấp tốc.",
                "D": "Không đề cập đến việc tập cùng gia đình hay dùng áp lực người khác."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m11_2_items:
        items.append({
            "id": qid,
            "typeId": "N2-RD-MID",
            "skill": "Reading",
            "category": "Mondai 11: 中文読解 — マイクロ・ハビットの心理学",
            "stem": stem,
            "contextPassage": p11_2_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    p11_3_text = """都市の近代化に伴い、コンクリートやアスファルトに覆われた人工的な空間が拡大し、身近な自然は長らく生活の邪魔者として排除される傾向にあった。しかし、地球温暖化による都市部のヒートアイランド現象や豪雨による水害リスクが深刻化する中で、自然が持つ多面的な機能を都市計画に積極的に取り入れる「グリーンインフラ」の思想が世界的な潮流となっている。

グリーンインフラの具体例としては、ビルの屋上や壁面の緑化、透水性舗装、雨水を一時的に貯留して地下に浸透させる雨水庭園（レインガーデン）などが挙げられる。これらは単に街の美観を整えるだけでなく、気温の上昇を抑え、都市型洪水を緩和する防災機能を発揮する。さらに、街路樹や公園が有機的につながることで、鳥や昆虫などの小動物の移動経路（エコロジカル・ネットワーク）が形成され、都市部における生物多様性の保全にも寄与している。

自然を人為的にコントロールすべき対象として捉えるのではなく、自然の循環システムそのものを都市のインフラとして共生させていく発想の転換こそが、気候変動の時代において持続可能な都市を築くための不可欠な鍵なのである。"""

    m11_3_items = [
        (
            "N2_04_M11_07",
            "都市計画において「グリーンインフラ」が注目されるようになった直接の契機は何か。",
            [
                ("A", "ヒートアイランド現象や水害など、都市環境の悪化や災害リスクが深刻化したこと。"),
                ("B", "コンクリート建築の老朽化が進み、建物の建て替え費用が高騰したこと。"),
                ("C", "都市部の住民が自然と触れ合う観光レジャーを強く求めるようになったこと。"),
                ("D", "農作物を都市部で自家栽培するアーバンファーミングが流行したこと。")
            ],
            "A",
            "Đoạn 1 nêu rõ nguyên nhân: hiện tượng đảo nhiệt đô thị (ヒートアイランド) do biến đổi khí hậu và nguy cơ ngập lụt do mưa lớn trở nên trầm trọng, thúc đẩy tư duy đưa chức năng tự nhiên vào quy hoạch hạ tầng xanh.",
            {
                "B": "Không đề cập đến chi phí bảo trì bê tông.",
                "C": "Không phải vì nhu cầu du lịch nghỉ dưỡng giải trí.",
                "D": "Không nói về trào lưu trồng trọt đô thị."
            }
        ),
        (
            "N2_04_M11_08",
            "本文で挙げられているグリーンインフラの機能に含まれないものはどれか。",
            [
                ("A", "太陽光発電パネルを屋上に設置して、都市の消費電力を100%自給すること。"),
                ("B", "雨水を地面に浸透させて、集中豪雨による都市型洪水を和らげること。"),
                ("C", "ビルの緑化や街路樹によって気温の上昇を抑え、景観を整えること。"),
                ("D", "公園や緑地をつなぐことで、小動物が移動できる生態系ネットワークを形成すること。")
            ],
            "A",
            "Đoạn 2 liệt kê các chức năng: giảm lũ lụt (雨水庭園), hạ nhiệt và làm đẹp cảnh quan (屋上緑化), tạo mạng lưới sinh thái cho động vật nhỏ di chuyển (エコロジカル・ネットワーク). Bài viết KHÔNG hề đề cập đến việc lắp pin năng lượng mặt trời tự cung tự cấp 100% điện năng.",
            {
                "B": "Có nêu ở đoạn 2 ('都市型洪水を緩和する').",
                "C": "Có nêu ở đoạn 2 ('美観を整えるだけでなく、気温の上昇を抑え').",
                "D": "Có nêu ở đoạn 2 ('鳥や昆虫などの小動物の移動経路...が形成され')."
            }
        ),
        (
            "N2_04_M11_09",
            "この文章を通じて筆者が最も訴えたい中心的な主張は何か。",
            [
                ("A", "自然を制御するのではなく、その循環機能を活かして共生する都市づくりが不可欠である。"),
                ("B", "都市の拡大を完全に停止し、すべての人工構造物を森林へと戻すべきである。"),
                ("C", "災害を防ぐためには、コンクリート堤防などの人工インフラをさらに強固にすべきである。"),
                ("D", "都市の緑化工事は莫大な費用がかかるため、まずは住民の寄付金を集めるべきである。")
            ],
            "A",
            "Đoạn cuối nhấn mạnh: thay vì xem thiên nhiên là đối tượng cần kiểm soát, việc chuyển đổi tư duy sang cùng cộng sinh và tận dụng hệ thống tuần hoàn tự nhiên làm hạ tầng là chìa khóa xây dựng đô thị bền vững.",
            {
                "B": "Cực đoan hóa, tác giả không đòi phá bỏ toàn bộ thành phố để trồng rừng.",
                "C": "Ngược lại với tư duy hạ tầng xanh (tác giả muốn chuyển dịch khỏi việc chỉ dựa vào bê tông nhân tạo).",
                "D": "Không bàn về vấn đề quyên góp tiền của người dân."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m11_3_items:
        items.append({
            "id": qid,
            "typeId": "N2-RD-MID",
            "skill": "Reading",
            "category": "Mondai 11: 中文読解 — 都市と自然の共生（グリーンインフラ）",
            "stem": stem,
            "contextPassage": p11_3_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 12: 統合理解 (Comparative Reading - 2 items)
    # =========================================================================
    p12_text = """【A】
近年、欧州を中心に勤務時間外の業務連絡への対応を拒否できる権利「つながらない権利（Right to Disconnect）」を法律で保障する動きが広がっている。スマートフォンやチャットツールの普及により、労働者は退勤後や休日であっても常に業務の通知に脅かされ、精神的な休息を奪われている。法的な強制力を持って時間外の連絡を禁止することは、過労死やメンタルヘルス不調を未然に防ぎ、労働者の心身の健康と私生活を守る上で極めて妥当かつ必要な措置である。企業側が業務プロセスの見直しを迫られるのは当然の代償といえる。

【B】
退勤後の過度な業務連絡が労働者に過度なストレスを与えている現状には同情するし、改善の必要性も痛感する。しかし、これを一律に法律で厳格に禁止することには慎重であるべきだ。現代のビジネスは国境を越えた時差のある取引や、予期せぬ緊急トラブルへの迅速な対応が不可欠である。法で画一的に遮断してしまえば、企業の競争力を削ぎ、かえって現場の柔軟な対応力を麻痺させかねない。法制化による罰則ではなく、各企業の実情に応じた労使間のガイドライン策定や、業務時間外の対応に対する正当な手当の支給など、現場主導の柔軟な運用こそが現実的な解決策ではないか。"""

    m12_raw = [
        (
            "N2_04_M12_01",
            "N2-RD-COMP",
            "Mondai 12: 統合理解",
            "AとBの両者が共通して認識している課題は何か。",
            [
                ("A", "勤務時間外の業務連絡が、労働者に精神的負担やストレスを与えていること。"),
                ("B", "法的な規制を導入すれば、企業の国際的な競争力が著しく低下すること。"),
                ("C", "チャットツールを業務に利用すること自体を全面的に禁止すべきであること。"),
                ("D", "時間外の対応に対しては、昼間の2倍以上の時間外手当を支給すべきであること。")
            ],
            "A",
            "Cả A và B đều công nhận thực tế: việc liên lạc công việc ngoài giờ hành chính đang gây áp lực tinh thần và cướp đi thời gian nghỉ ngơi của người lao động (A: '精神的な休息を奪われている', B: '過度なストレスを与えている現状には同情するし、改善の必要性も痛感する').",
            {
                "B": "Chỉ có tác giả B lo ngại về việc giảm sức cạnh tranh quốc tế của doanh nghiệp, tác giả A coi đó là cái giá đương nhiên phải trả.",
                "C": "Cả hai không ai đòi cấm hoàn toàn phần mềm chat trong công việc.",
                "D": "Không có tác giả nào đề xuất trả lương gấp đôi cho thời gian ngoài giờ."
            }
        ),
        (
            "N2_04_M12_02",
            "N2-RD-COMP",
            "Mondai 12: 統合理解",
            "「つながらない権利」に対するAとBの主張の相違点として、最も適切なものはどれか。",
            [
                ("A", "Aは法律による一律の強制禁止を支持し、Bは企業ごとの実情に即した柔軟な運用を求めている。"),
                ("B", "Aは金銭的な手当の支給を重視し、Bは労働時間の短縮を最優先すべきだと主張している。"),
                ("C", "Aは国内企業のみを対象とすべきとし、Bは多国籍企業への適用を推奨している。"),
                ("D", "Aは個人の自己責任に任せるべきとし、Bは政府による厳格な監督を求めている。")
            ],
            "A",
            "Sự khác biệt rõ nét: Tác giả A ủng hộ luật hóa bắt buộc cấm liên lạc ngoài giờ hành chính ('法的な強制力を持って...禁止することは...極めて妥当かつ必要な措置'), trong khi Tác giả B phản đối luật hóa rập khuôn mà đề xuất giải pháp linh hoạt nội bộ doanh nghiệp qua thỏa ước lao động và chế độ phụ cấp ('法制化による罰則ではなく、各企業の実情に応じた...柔軟な運用こそが現実的').",
            {
                "B": "Tác giả B mới là người nhắc tới phụ cấp (手当), tác giả A tập trung vào cấm bằng luật.",
                "C": "Không bàn về phạm vi phân chia doanh nghiệp nội địa hay đa quốc gia.",
                "D": "Ngược hoàn toàn: A đòi luật pháp can thiệp, B muốn tự chủ linh hoạt nội bộ."
            }
        )
    ]

    for qid, tid, cat, stem, opts, ans, exp, dist in m12_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Reading",
            "category": cat,
            "stem": stem,
            "contextPassage": p12_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 13: 長文読解 (Thematic Long Passage - 3 items)
    # =========================================================================
    p13_text = """インターネットとスマートフォンの普及によって、現代人はかつてないほど「常時接続」された世界を生きている。SNSを開けば世界中の人々の日常がタイムラインに流れ込み、メッセンジャーを使えば地球の裏側にいる相手とも瞬時にメッセージをやり取りできる。形式的な意味において、現代ほど他者との距離が縮まった時代は歴史上存在しない。しかしその一方で、現代社会において「孤独感」や「孤立感」を訴える人の割合は、皮肉にも過去最高水準に達していると言われている。この奇妙なパラドックスは、一体なぜ生じているのだろうか。

私たちはしばしば、他者と「つながっている量」と「つながりの質」を混同してしまう。画面を通じて交換される大量の「いいね！」や短いテキストメッセージは、一時的な承認欲求を満たすことはできても、人間の根源的な孤独を癒やすことはできない。むしろ、SNS上で演出された他者の華やかな生活や成功体験を日常的に目撃し続けることで、自分自身の地味で平凡な日常との落差に苦しみ、無力感や疎外感を深めてしまうケースが後を絶たない。画面の向こうに数千人の「フォロワー」を抱えながらも、深夜に本当の苦しみを打ち明けられる相手が一人もいないという現実は、現代のハイパーコネクテッド社会が孕む深い闇である。

真の人間的なつながりとは、単なる情報の伝達や記号の交換ではなく、お互いの弱さや不完全さをも共有し合える関係性の中にこそ宿る。対面でのコミュニケーションにおいては、発せられる言葉そのものだけでなく、微妙な声のトーンや沈黙、視線の揺らぎ、表情の翳りといった無数の非言語的な手がかり（ノンバーバル・シグナル）がやり取りされる。私たちはそうした微細なシグナルを五感で察知することによって、相手の痛みに共感し、自分が他者から全人格的に受け入れられているという深い安心感を獲得するのである。オンラインのデジタルなやり取りは極めて効率的であるがゆえに、そうした「非効率で曖昧な人間的ノイズ」を徹底的に削ぎ落としてしまう。

孤独から抜け出すために真に必要なのは、さらなるフォロワーの獲得やスマートフォンの閲覧時間を増やすことではない。時にはデジタルデバイスの通知をオフにし、目の前にいる具体的な他者と向き合い、あるいは自分自身の内なる声と静かに対話する「豊かな孤独（ソリチュード）」を取り戻すことである。他者との真摯な対話と、孤独を恐れずに自己を見つめ直す静謐な時間。この両輪が揃って初めて、私たちはバーチャルな情報の海に溺れることなく、確固たる自己の足で人生を歩み出すことができるのではないだろうか。"""

    m13_raw = [
        (
            "N2_04_M13_01",
            "第1段落で筆者が述べている「奇妙なパラドックス」の内容として、最も適切なものはどれか。",
            [
                ("A", "通信技術の発達で世界中と常時つながれる時代になったのに、孤独を感じる人が急増していること。"),
                ("B", "スマートフォンの普及で読書量が減ったのに、人々の情報処理能力が格段に向上したこと。"),
                ("C", "SNSで簡単に知り合えるようになったのに、直接会って話す機会を望む人が増えていること。"),
                ("D", "他者のプライバシーが守られにくくなったのに、個人の秘密を隠そうとする意識が薄れていること。")
            ],
            "A",
            "Đoạn 1 nêu rõ nghịch lý: '現代ほど他者との距離が縮まった時代は歴史上存在しない。しかしその一方で、現代社会において「孤独感」や「孤立感」を訴える人の割合は、皮肉にも過去最高水準に達している' (Chưa bao giờ khoảng cách với người khác lại thu hẹp như hiện nay nhờ công nghệ kết nối liên tục, nhưng trớ trêu thay tỉ lệ người cảm thấy cô đơn lại chạm mức cao nhất trong lịch sử).",
            {
                "B": "Không bàn về lượng đọc sách hay năng lực xử lý thông tin.",
                "C": "Đoạn 1 nói người ta cô đơn chứ không nói người ta thích gặp mặt trực tiếp nhiều hơn.",
                "D": "Không bàn về quyền riêng tư hay ý thức giấu bí mật cá nhân."
            }
        ),
        (
            "N2_04_M13_02",
            "第3段落において、対面コミュニケーションが深い安心感をもたらす理由として筆者が挙げているのはどれか。",
            [
                ("A", "言葉だけでなく表情や声のトーンなど微細な非言語シグナルを通じて、全人格的な共感が生まれるから。"),
                ("B", "オンラインのやり取りに比べて、短時間で膨大な情報を正確かつ効率的に伝達できるから。"),
                ("C", "相手の社会的地位や経歴を直接確認できるため、詐欺や騙しの被害を防ぐことができるから。"),
                ("D", "対面で話すことで、自分の意見の正しさを相手に論理的に納得させやすくなるから。")
            ],
            "A",
            "Đoạn 3 phân tích: giao tiếp trực tiếp mặt-đối-mặt truyền tải vô số tín hiệu phi ngôn ngữ (tông giọng, khoảng lặng, ánh mắt, biểu cảm), qua đó các giác quan cảm nhận được nỗi đau và sự chấp nhận trọn vẹn của đối phương, tạo nên sự an tâm sâu sắc.",
            {
                "B": "Giao tiếp mặt-đối-mặt nhiều 'nhiễu' và chậm hơn online chứ không hề hiệu quả, nhanh gọn hơn thông tin số.",
                "C": "Không bàn về việc xác minh địa vị hay phòng chống lừa đảo.",
                "D": "Tác giả nói về sự đồng cảm chia sẻ điểm yếu, không phải tranh luận thuyết phục ai đúng ai sai."
            }
        ),
        (
            "N2_04_M13_03",
            "この文章全体を通じて、筆者が現代人に提案している生き方はどのようなものか。",
            [
                ("A", "デジタル接続から時には離れ、対面の対話と自己を見つめる静かな時間を大切にすること。"),
                ("B", "SNSのフォロワー数を増やし、より多くの人々とオンライン上で常に交流し続けること。"),
                ("C", "現代の通信技術を完全に放棄し、インターネットの存在しない昔ながらの生活に戻ること。"),
                ("D", "他者との関わりを一切断ち切り、孤独の中で専門的なスキルの習得に没頭すること。")
            ],
            "A",
            "Đoạn kết đúc kết thông điệp cốt lõi: đôi khi hãy tắt thông báo thiết bị số, đối diện với người đang ở trước mắt và lấy lại khoảng thời gian tĩnh lặng đối thoại với nội tâm mình ('豊かな孤独を取り戻すこと... 他者との真摯な対話と、孤独を恐れずに自己を見つめ直す静謐な時間').",
            {
                "B": "Trái ngược với cảnh báo của tác giả (tác giả nói tăng follower không giải quyết được cô đơn).",
                "C": "Cực đoan hóa, tác giả không kêu gọi vứt bỏ hoàn toàn công nghệ để sống thời đồ đá.",
                "D": "Tác giả đề cao cả 2 bánh xe: đối thoại chân thành với người khác VÀ tĩnh lặng với bản thân, chứ không bảo cắt đứt với xã hội."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m13_raw:
        items.append({
            "id": qid,
            "typeId": "N2-RD-LONG",
            "skill": "Reading",
            "category": "Mondai 13: 長文読解 — 現代社会における接続と孤独",
            "stem": stem,
            "contextPassage": p13_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 14: 情報検索 (Information Retrieval - 2 items)
    # =========================================================================
    p14_text = """【地域イノベーション＆起業家育成フォーラム2026】参加案内

地域経済の活性化と新規事業の創出を目指し、国内外の第一線で活躍する起業家や専門家を招いたフォーラムを開催いたします。

1. 開催日時：2026年12月5日（土）10:00 〜 17:30（開場 9:30）
2. 会場：みらい国際会議場 メインホール（JR中央駅西口より徒歩5分）
3. プログラム概要：
   ・10:00〜12:00 基調講演「テクノロジーが拓く地方創生の未来」
   ・13:00〜15:00 パネルディスカッション「持続可能な地域ビジネスモデル」
   ・15:30〜17:30 ピッチコンテスト＆交流ネットワーキング会

4. 参加費および定員：
   ・一般参加者：3,000円（先着150名）
   ・市内在住または在勤者：2,000円（先着100名、身分証明書の提示が必要）
   ・学生（高校生・大学生・大学院生）：無料（先着50名、要学生証提示）
   ※交流ネットワーキング会への参加を希望される方は、上記参加費に加えて別途飲食費1,500円（学生は1,000円）が必要です。

5. 申込方法およびキャンセル規定：
   ・公式ウェブサイトの専用フォームより、11月25日（水）23:59までにお申し込みください。
   ・定員に達し次第、期日前であっても受付を締め切ります。
   ・キャンセル料：11月28日（土）までの取消は全額返金、11月29日（日）以降の取消または当日不参加は返金いたしかねます。"""

    m14_raw = [
        (
            "N2_04_M14_01",
            "市内に住む大学3年生のグエンさんが、午後の交流ネットワーキング会も含めて全プログラムに参加する場合、支払う金額はいくらになるか。",
            [
                ("A", "1,000円"),
                ("B", "2,000円"),
                ("C", "3,000円"),
                ("D", "無料")
            ],
            "A",
            "Mục 4 quy định: Sinh viên (学生) được miễn phí tham gia hội thảo chính ('学生: 無料'). Đối với tiệc giao lưu networking chiều, sinh viên trả riêng 1,000 yên ('別途飲食費1,500円（学生は1,000円）'). Như vậy tổng cộng Nguyễn phải trả 0 + 1,000 = 1,000 yên.",
            {
                "B": "2,000 yên là vé hội thảo của người sinh sống/làm việc tại thành phố (市内在住/在勤者), nhưng Nguyễn là sinh viên nên được miễn phí vé vào cổng.",
                "C": "3,000 yên là giá vé hội thảo chung của người bình thường.",
                "D": "Miễn phí chỉ áp dụng cho phần hội thảo ban ngày, tiệc giao lưu chiều bắt buộc đóng tiền ăn uống 1,000 yên."
            }
        ),
        (
            "N2_04_M14_02",
            "このフォーラムの申し込みおよびキャンセルについて、正しいものはどれか。",
            [
                ("A", "11月28日までにキャンセル手続きを行えば、支払った参加費は全額返金される。"),
                ("B", "申込期日は11月25日なので、定員に達していなくても当日の飛び込み参加が可能である。"),
                ("C", "市内在住者であっても、学生であれば一般参加費の3,000円を支払わなければならない。"),
                ("D", "11月30日に都合が悪くなってキャンセルした場合でも、半額は返金される。")
            ],
            "A",
            "Mục 5 quy định rõ: '11月28日（土）までの取消は全額返金' (Hủy trước hoặc trong ngày 28/11 sẽ được hoàn lại 100% tiền phí đã đóng).",
            {
                "B": "Phải đăng ký trước qua website trước hạn chót 25/11, không có chuyện tự do đến tham dự ngày thi.",
                "C": "Sinh viên được ưu tiên diện miễn phí (0 yên), không bị ép trả 3,000 yên.",
                "D": "Hủy từ ngày 29/11 trở đi hoặc không đến sẽ không được hoàn tiền (返金いたしかねます), không có chính sách hoàn nửa tiền."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m14_raw:
        items.append({
            "id": qid,
            "typeId": "N2-RD-INFO",
            "skill": "Reading",
            "category": "Mondai 14: 情報検索 — 地域イノベーションフォーラム参加案内",
            "stem": stem,
            "contextPassage": p14_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    assert len(items) == 75, f"Expected exactly 75 items for Section 1, got {len(items)}"
    return items

if __name__ == '__main__':
    items = get_n2_mock_04_sec1_items()
    print(f"Successfully generated {len(items)} items for Section 1 of N2-MOCK-04.")
