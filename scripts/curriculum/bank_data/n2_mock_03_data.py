# -*- coding: utf-8 -*-
"""
JLPT N2 Mock Exam #03 - Section 1: Language Knowledge & Reading (言語知識・読解)
Blueprint (75 items / 105 minutes):
- Mondai 1: 漢字読み (5 items)
- Mondai 2: 表記 (5 items)
- Mondai 3: 語形成 (5 items)
- Mondai 4: 文脈規定 (7 items)
- Mondai 5: 言い換え類義 (5 items)
- Mondai 6: 用法 (5 items)
- Mondai 7: 文法形式 (12 items)
- Mondai 8: 文の組み立て ★ (5 items)
- Mondai 9: 文章の文法 (5 items)
- Mondai 10: 短文読解 (5 items)
- Mondai 11: 中文読解 (9 items)
- Mondai 12: 統合理解 (2 items)
- Mondai 13: 長文読解 (3 items)
- Mondai 14: 情報検索 (2 items)
Total Section 1: 75 items
"""

def get_n2_mock_03_sec1_items():
    items = []

    # =========================================================================
    # MONDAI 1: 漢字読み (Kanji Reading - 5 items)
    # =========================================================================
    m1_raw = [
        (
            "N2_03_M1_01",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "業務の一部を外部の専門業者に【委託】することに決めた。",
            "いたく",
            [("A", "いたく"), ("B", "いしょく"), ("C", "いぞく"), ("D", "いしん")],
            "A",
            "委託（いたく - ỦY THÁC）: Giao phó, ủy thác công việc cho bên ngoài. Chữ 委 có âm on là い, chữ 託 có âm on là たく.",
            {
                "B": "いしょく: Nhầm lẫn với 移植 (いしょく - cấy ghép) hoặc 委嘱 (いしょく - bổ nhiệm, giao phó chức trách).",
                "C": "いぞく: Nhầm lẫn với 遺族 (いぞく - gia quyến người đã mất).",
                "D": "いしん: Nhầm lẫn với 威信 (いしん - uy tín, uy tín vị thế)."
            }
        ),
        (
            "N2_03_M1_02",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "彼の長年の研究成果がこの一冊に【凝縮】されている。",
            "ぎょうしゅく",
            [("A", "こうしゅく"), ("B", "ぎょうしゅく"), ("C", "ぎょうしん"), ("D", "こんしゅく")],
            "B",
            "凝縮（ぎょうしゅく - NGƯNG SÚC）: Ngưng tụ, cô đọng tinh hoa. Chữ 凝 có âm on là ぎょう, chữ 縮 có âm on là しゅく.",
            {
                "A": "こうしゅく: Nhầm âm ぎょう thành こう (như trong 拘束 こうそく).",
                "C": "ぎょうしん: Nhầm âm đuôi しゅく thành しん.",
                "D": "こんしゅく: Sai âm đầu ぎょう thành こん."
            }
        ),
        (
            "N2_03_M1_03",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "踏切の警報機が鳴り、【遮断】機がゆっくりと下りてきた。",
            "しゃだん",
            [("A", "さだん"), ("B", "しゃだん"), ("C", "しゃたん"), ("D", "せいだん")],
            "B",
            "遮断（しゃだん - GIÀ ĐOẠN）: Chặn đứng, ngăn cách, cách ly. Chữ 遮 có âm on là しゃ, chữ 断 có âm on là だん.",
            {
                "A": "さだん: Sai phát âm しゃ thành さ.",
                "C": "しゃたん: Sai biến âm đục だん thành âm trong たん.",
                "D": "せいだん: Nhầm âm しゃ thành せい (như trong 正当 せいとう)."
            }
        ),
        (
            "N2_03_M1_04",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "光が水面を通過するときに【屈折】する現象を観察した。",
            "くっせつ",
            [("A", "くつおり"), ("B", "ぐっせつ"), ("C", "くっせつ"), ("D", "くっしょう")],
            "C",
            "屈折（くっせつ - KHUẤT CHIẾT）: Khúc xạ (ánh sáng), uốn cong, quanh co. Chữ 屈 có âm on là くつ (biến âm ngắt thành くっ), chữ 折 có âm on là せつ.",
            {
                "A": "くつおり: Nhầm âm on せつ thành âm kun おり của 折る (おる).",
                "B": "ぐっせつ: Sai biến âm đục ぐ ở đầu từ.",
                "D": "くっしょう: Nhầm lẫn với 屈従 (くつじゅう) hoặc 折 tượng hình thành しょう."
            }
        ),
        (
            "N2_03_M1_05",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "状況に応じて柔軟に【融通】を利かせることが大切だ。",
            "ゆうずう",
            [("A", "ゆうづう"), ("B", "ゆずう"), ("C", "ゆうつう"), ("D", "ゆうずう")],
            "D",
            "融通（ゆうずう - DUNG THÔNG）: Linh hoạt ứng biến, sự xoay xở (融通が利く). Chữ 融 có âm ゆう, chữ 通 có âm つう biến âm thành ずう.",
            {
                "A": "ゆうづう: Sai quy tắc gõ kana và ngữ âm kanji lịch sử (chính thức là ずう).",
                "B": "ゆずう: Thiếu trường âm ゆう ở chữ 融.",
                "C": "ゆうつう: Không biến âm đục chữ 通 (つう -> ずう trong từ ghép này)."
            }
        ),
    ]

    for qid, tid, cat, stem, target, opts, ans, exp, dist in m1_raw:
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
    # MONDAI 2: 表記 (Orthography / Kanji Selection - 5 items)
    # =========================================================================
    m2_raw = [
        (
            "N2_03_M2_01",
            "N2-MO-WRIT",
            "Mondai 2: 表記",
            "景気回復の傾向が統計データに【けんちょ】に現れている。",
            "けんちょ",
            [("A", "顕著"), ("B", "賢著"), ("C", "顕暑"), ("D", "倹著")],
            "A",
            "顕著（けんちょ - HIỂN TRỨ）: Nổi bật, rõ ràng, hiển nhiên. Chữ 顕 (hiển hiển nhiên) ghép với chữ 著 (trứ trứ danh/nổi bật).",
            {
                "B": "賢著: Nhầm chữ 顕 thành 賢 (Hiền - thông minh, hiền hậu).",
                "C": "顕暑: Nhầm chữ 著 thành 暑 (Thử - nắng nóng).",
                "D": "倹著: Nhầm chữ 顕 thành 倹 (Kiệm - tiết kiệm)."
            }
        ),
        (
            "N2_03_M2_02",
            "N2-MO-WRIT",
            "Mondai 2: 表記",
            "海外の支社へ技術指導のために専門スタッフを【はけん】した。",
            "はけん",
            [("A", "派遺"), ("B", "派遣"), ("C", "破遣"), ("D", "旅遣")],
            "B",
            "派遣（はけん - PHÁI KHIỂN）: Phái cử, điều động nhân sự đến một địa điểm/nhiệm vụ. Chữ 派 ghép với chữ 遣 (khiển phái).",
            {
                "A": "派遺: Nhầm bộ dẫn chữ 遣 thành bộ quai xước chữ 遺 (Di - di sản, để lại).",
                "C": "破遣: Nhầm chữ 派 (Phái) thành 破 (Phá - phá vỡ).",
                "D": "旅遣: Nhầm bộ thủy của 派 thành bộ phương của 旅 (Lữ - du lịch)."
            }
        ),
        (
            "N2_03_M2_03",
            "N2-MO-WRIT",
            "Mondai 2: 表記",
            "専門知識を要する作業に対して正当な【ほうしゅう】を支払うべきだ。",
            "ほうしゅう",
            [("A", "報集"), ("B", "豊酬"), ("C", "報酬"), ("D", "報修")],
            "C",
            "報酬（ほうしゅう - BÁO THÙ）: Thù lao, tiền công tương xứng cho sức lao động hoặc dịch vụ chuyên môn. Chữ 報 ghép với chữ 酬 (thù thù lao).",
            {
                "A": "報集: Nhầm chữ 酬 (Thù) thành 集 (Tập - tập hợp).",
                "B": "豊酬: Nhầm chữ 報 (Báo) thành 豊 (Phong - phong phú).",
                "D": "報修: Nhầm chữ 酬 thành 修 (Tu - sửa chữa, tu luyện)."
            }
        ),
        (
            "N2_03_M2_04",
            "N2-MO-WRIT",
            "Mondai 2: 表記",
            "厳しい登山を経て頂上に立ち、困難を【こくふく】した喜びを味わった。",
            "こくふく",
            [("A", "刻服"), ("B", "克副"), ("C", "告復"), ("D", "克服")],
            "D",
            "克服（こくふく - KHẮC PHỤC）: Vượt qua gian khổ, khắc phục khó khăn. Chữ 克 (khắc vượt qua) ghép với chữ 服 (phục quy phục).",
            {
                "A": "刻服: Nhầm chữ 克 (Khắc vượt qua) thành 刻 (Khắc - điêu khắc, khắc cốt).",
                "B": "克副: Nhầm chữ 服 (Phục) thành 副 (Phó - phụ tá, phụ cấp).",
                "C": "告復: Nhầm 克 thành 告 (Cáo - báo cáo) và 服 thành 復 (Phục - hồi phục)."
            }
        ),
        (
            "N2_03_M2_05",
            "N2-MO-WRIT",
            "Mondai 2: 表記",
            "市場の需要に応えるため、生産ラインの規模を【かくだい】する方針だ。",
            "かくだい",
            [("A", "拡犬"), ("B", "拡大"), ("C", "鉱大"), ("D", "拡代")],
            "B",
            "拡大（かくだい - KHUẾCH ĐẠI）: Mở rộng quy mô, bành trướng kích cỡ. Chữ 拡 (khuếch mở rộng) ghép với 大 (đại to lớn).",
            {
                "A": "拡犬: Nhầm chữ 大 (Đại) thành 犬 (Khuyển - con chó).",
                "C": "鉱大: Nhầm chữ 拡 (Khuếch) thành 鉱 (Khoáng - quặng khoáng sản).",
                "D": "拡代: Nhầm chữ 大 thành 代 (Đại - thay thế, thời đại)."
            }
        ),
    ]

    for qid, tid, cat, stem, target, opts, ans, exp, dist in m2_raw:
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
    # MONDAI 3: 語形成 (Word Formation - 5 items)
    # =========================================================================
    m3_raw = [
        (
            "N2_03_M3_01",
            "N2-VOC-CONT",
            "Mondai 3: 語形成",
            "面接での丁寧な受け答えが面接官に（　　）印象を与えた。",
            [("A", "好"), ("B", "良"), ("C", "優"), ("D", "美")],
            "A",
            "好印象（こういんしょう）: Ấn tượng tốt đẹp. Tiền tố 好- kết hợp với các danh từ như 好条件 (điều kiện thuận lợi), 好景気 (kinh tế hưng thịnh), 好印象 (ấn tượng tốt).",
            {
                "B": "良: Thường kết hợp trong 良識 (lương tri), 良心 (lương tâm), không ghép thành *良印象.",
                "C": "優: Ghép trong 優先 (ưu tiên), 優位 (ưu thế), không ghép trực tiếp trước 印象.",
                "D": "美: Ghép trong 美辞麗句, 美徳, không tạo từ *美印象 trong tiếng Nhật chuẩn."
            }
        ),
        (
            "N2_03_M3_02",
            "N2-VOC-CONT",
            "Mondai 3: 語形成",
            "（　　）事情により、本日の特別講演会は延期となりました。",
            [("A", "各"), ("B", "諸"), ("C", "多"), ("D", "連")],
            "B",
            "諸事情（しょじじょう）: Do nhiều hoàn cảnh/lý do khác nhau (cụm từ trang trọng thường dùng trong thông báo hoãn/hủy sự kiện). Tiền tố 諸- (Chư) mang nghĩa 'các, nhiều'.",
            {
                "A": "各: Mang nghĩa 'từng, mỗi', ghép trong 各国 (các nước), 各自 (mỗi người), không ghép thành *各事情.",
                "C": "多: Mang nghĩa 'nhiều', ghép trong 多目的, 多方面, không dùng *多事情.",
                "D": "連: Mang nghĩa 'liên tục, liên đới', ghép trong 連休, 連日, không dùng *連事情."
            }
        ),
        (
            "N2_03_M3_03",
            "N2-VOC-CONT",
            "Mondai 3: 語形成",
            "その難事件の真相は、発生から10年経った今も（　　）解決のままだ。",
            [("A", "不"), ("B", "非"), ("C", "無"), ("D", "未")],
            "D",
            "未解決（みかいけつ）: Chưa được giải quyết (vẫn còn dang dở). Tiền tố 未- chỉ trạng thái 'chưa đạt tới', rất hay gặp với 未定 (chưa quyết định), 未完成 (chưa hoàn thành), 未解決 (chưa giải quyết).",
            {
                "A": "不: Chỉ sự phủ định tính chất hoặc không làm: 不可能, 不完全, 不愉快, không nói *不解決.",
                "B": "非: Chỉ tính phi, trái quy tắc: 非公式, 非常識, 非公開, không nói *非解決.",
                "C": "無: Chỉ sự không tồn tại, trống rỗng: 無意味, 無責任, 無関係, không nói *無解決."
            }
        ),
        (
            "N2_03_M3_04",
            "N2-VOC-CONT",
            "Mondai 3: 語形成",
            "この新型スマートフォンは超（　　）性能のカメラを搭載している。",
            [("A", "高"), ("B", "上"), ("C", "貴"), ("D", "豪")],
            "A",
            "高性能（こうせいのう）: Hiệu năng cao, tính năng vượt trội. Tiền tố 高- chỉ mức độ/chất lượng vượt trội: 高品質, 高性能, 高精度, 高収入.",
            {
                "B": "上: Ghép trong 上位 (vị trí cao), 上級 (cao cấp), không tạo danh từ *上性能.",
                "C": "貴: Ghép trong 貴重 (quý trọng), 貴金属 (kim loại quý), không đi với 性能.",
                "D": "豪: Ghép trong 豪華 (xa hoa), 豪快 (hào sảng), không đi với 性能."
            }
        ),
        (
            "N2_03_M3_05",
            "N2-VOC-CONT",
            "Mondai 3: 語形成",
            "最新のアンケート調査を実施し、顧客の満足（　　）を詳細に測定した。",
            [("A", "性"), ("B", "率"), ("C", "度"), ("D", "感")],
            "C",
            "満足度（まんぞくど）: Mức độ thỏa mãn, độ hài lòng (CS - Customer Satisfaction). Hậu tố -度 chỉ cấp độ, chỉ số đo lường: 注目度, 知名度, 信頼度, 満足度.",
            {
                "A": "性: Hậu tố chỉ tính chất: 危険性, 可能性, 安全性, không dùng *満足性.",
                "B": "率: Hậu tố chỉ tỷ lệ phần trăm: 合格率, 成功率, 視聴率, không dùng *満足率.",
                "D": "感: Hậu tố chỉ cảm giác: 責任感, 緊張感, 満足感 (nhưng khi 'đo lường bằng khảo sát' theo thang điểm thống kê, phải dùng 満足度)."
            }
        ),
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
    # MONDAI 4: 文脈規定 (Contextual Vocabulary - 7 items)
    # =========================================================================
    m4_raw = [
        (
            "N2_03_M4_01",
            "N2-VOC-CONT",
            "Mondai 4: 文脈規定",
            "会議で明確な合意に至らず、肝心な問題を（　　）のまま終わらせてしまった。",
            [("A", "ぎくしゃく"), ("B", "うやむや"), ("C", "ぼんやり"), ("D", "めちゃくちゃ")],
            "B",
            "うやむや（うやむやにする / うやむやのまま）: Mập mờ, không dứt khoát, để lấp liếm qua chuyện mà không làm rõ trắng đen.",
            {
                "A": "ぎくしゃく: Gượng gạo, trục trặc, bất hòa trong quan hệ (người với người): 人間関係がぎくしゃくする.",
                "C": "ぼんやり: Mờ ảo, đãng trí, mất tập trung: 景色がぼんやり見える / ぼんやりと過ごす.",
                "D": "めちゃくちゃ: Lộn xộn, bừa bãi, vô lý đổ vỡ: 部屋がめちゃくちゃだ / めちゃくちゃな要求."
            }
        ),
        (
            "N2_03_M4_02",
            "N2-VOC-CONT",
            "Mondai 4: 文脈規定",
            "急な体調不良のため、楽しみにしていたマラソン大会への参加を（　　）した。",
            [("A", "棄権"), ("B", "解約"), ("C", "辞退"), ("D", "脱退")],
            "C",
            "辞退（じたい）: Từ chối khéo, xin rút lui không nhận lời mời, giải thưởng hoặc không tham gia một sự kiện một cách lịch sự.",
            {
                "A": "棄権: Bỏ phiếu trắng trong bầu cử hoặc bỏ cuộc giữa chừng trong trận đấu thể thao đang diễn ra.",
                "B": "解約: Hủy hợp đồng, hủy thỏa ước dịch vụ (như hủy hợp đồng điện thoại, phòng trọ).",
                "D": "脱退: Rút khỏi một tổ chức, đảng phái, liên minh (EUから脱退する)."
            }
        ),
        (
            "N2_03_M4_03",
            "N2-VOC-CONT",
            "Mondai 4: 文脈規定",
            "彼は過去の成功体験に（　　）することなく、常に新しい手法に挑戦している。",
            [("A", "依存"), ("B", "没頭"), ("C", "束縛"), ("D", "執着")],
            "D",
            "執着（しゅうちゃく / しゅうじゃく）: Chấp niệm, khư khư giữ chặt lấy, bám riết không chịu buông bỏ (thường đi với quá khứ, danh lợi, tiền tài).",
            {
                "A": "依存: Dựa dẫm, phụ thuộc hoàn toàn vào người khác hoặc thứ khác (親に依存する).",
                "B": "没頭: Mải mê, chìm đắm hết mình vào công việc/sở thích với nghĩa tích cực (研究に没頭する).",
                "C": "束縛: Trói buộc, giam hãm, hạn chế tự do của người khác (自由を束縛する)."
            }
        ),
        (
            "N2_03_M4_04",
            "N2-VOC-CONT",
            "Mondai 4: 文脈規定",
            "地域社会との交流活動の（　　）として、毎月第1土曜日に清掃活動を行っている。",
            [("A", "一環"), ("B", "一端"), ("C", "一面"), ("D", "一体")],
            "A",
            "一環（いっかん - 〜の一環として）: Một khâu, một phần nằm trong một chuỗi hoạt động hoặc kế hoạch tổng thể.",
            {
                "B": "一端: Một manh mối nhỏ, một đầu mối ban đầu: 事件の一端が明らかになる.",
                "C": "一面: Một phương diện, một mặt khác của vấn đề: 物事の一面だけを見る.",
                "D": "一体: Toàn thể/đồng lòng nhất trí (一体となる) hoặc từ nhấn mạnh nghi vấn (いったい...)."
            }
        ),
        (
            "N2_03_M4_05",
            "N2-VOC-CONT",
            "Mondai 4: 文脈規定",
            "高齢者や子供にも安全に利用できるよう、段差をなくすなど細部まで（　　）した設計にした。",
            [("A", "考慮"), ("B", "配慮"), ("C", "遠慮"), ("D", "気配")],
            "B",
            "配慮（はいりょ - 〜に配慮する）: Quan tâm chu đáo, chiếu cố, để tâm tới quyền lợi và sự an toàn tiện lợi của đối tượng yếu thế/xung quanh.",
            {
                "A": "考慮: Xem xét, cân nhắc lý tính các điều kiện trước khi đưa ra quyết định (事情を考慮に入れる).",
                "C": "遠慮: Ngại ngùng, kiêng dè, giữ kẽ không dám làm phiền người khác (遠慮なくどうぞ).",
                "D": "気配: Linh cảm, dấu hiệu, thoang thoảng có sự hiện diện của ai đó (人の気配がする)."
            }
        ),
        (
            "N2_03_M4_06",
            "N2-VOC-CONT",
            "Mondai 4: 文脈規定",
            "忙しい上司への業務報告は、要点を絞って（　　）に伝えることが求められる。",
            [("A", "手軽"), ("B", "器用"), ("C", "簡潔"), ("D", "素朴")],
            "C",
            "簡潔（かんけつ - 簡潔にまとめる / 簡潔に伝える）: Ngắn gọn, súc tích, đi thẳng vào trọng tâm mà vẫn đủ ý.",
            {
                "A": "手軽: Tiện lợi, dễ dàng, không cầu kỳ công phu (手軽な軽食).",
                "B": "器用: Khéo tay, tháo vát xử lý việc chân tay hay đối nhân xử thế (手先が器用だ).",
                "D": "素朴: Giản dị, chân chất mộc mạc tự nhiên (素朴な疑問 / 素朴な人柄)."
            }
        ),
        (
            "N2_03_M4_07",
            "N2-VOC-CONT",
            "Mondai 4: 文脈規定",
            "豪雨による河川氾濫の恐れがあるため、住民に早めの避難を（　　）警報が発令された。",
            [("A", "拒む"), ("B", "阻む"), ("C", "脅かす"), ("D", "促す")],
            "D",
            "促す（うながす - 避難を促す / 行動を促す）: Thúc giục, khuyến khích, nhắc nhở ai đó nhanh chóng hành động.",
            {
                "A": "拒む: Từ chối quyết liệt, cự tuyệt yêu cầu hoặc lời đề nghị (要求を拒む).",
                "B": "阻む: Cản trở, chặn đứng đường đi lối lại hoặc sự tiến bộ (行く手を阻む).",
                "C": "脅かす: Đe dọa, uy hiếp sự an nguy hoặc vị thế (平和を脅かす)."
            }
        ),
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
    # MONDAI 5: 言い換え類義 (Synonyms / Paraphrases - 5 items)
    # =========================================================================
    m5_raw = [
        (
            "N2_03_M5_01",
            "N2-VOC-SYNO",
            "Mondai 5: 言い換え類義",
            "彼女は自分の意見を【ストレートに】伝えた。",
            [("A", "率直に"), ("B", "慎重に"), ("C", "大げさに"), ("D", "巧妙に")],
            "A",
            "ストレートに（straight）: Thẳng thắn, trực tiếp, không vòng vo uốn khúc = 率直に（そっちょくに）.",
            {
                "B": "慎重に: Cẩn trọng, dè dặt, kỹ càng từng bước (ngược hướng với nói thẳng).",
                "C": "大げさに: Cường điệu, phóng đại, làm quá mức vấn đề lên.",
                "D": "巧妙に: Khéo léo, tinh vi xảo quyệt (dùng mưu mẹo)."
            }
        ),
        (
            "N2_03_M5_02",
            "N2-VOC-SYNO",
            "Mondai 5: 言い換え類義",
            "新しい難問に対して従来とは異なる【アプローチ】を試みた。",
            [("A", "結論"), ("B", "取り組み方"), ("C", "口実"), ("D", "合意")],
            "B",
            "アプローチ（approach）: Phương thức tiếp cận, cách đặt vấn đề và bắt tay giải quyết = 取り組み方（とりくみかた）.",
            {
                "A": "結論: Kết luận cuối cùng, kết quả suy luận.",
                "C": "口実: Cớ, lý do bao biện mượn cớ để thoái thác.",
                "D": "合意: Sự đồng thuận, thống nhất ý kiến giữa các bên."
            }
        ),
        (
            "N2_03_M5_03",
            "N2-VOC-SYNO",
            "Mondai 5: 言い換え類義",
            "会議の所要時間は【おおよそ】2時間を見込んでいます。",
            [("A", "せいぜい"), ("B", "かろうじて"), ("C", "だいたい"), ("D", "とっくに")],
            "C",
            "おおよそ: Đại khái, ước chừng, xấp xỉ = だいたい（約・およそ）.",
            {
                "A": "せいぜい: Tối đa cũng chỉ, cùng lắm là (chỉ giới hạn cao nhất).",
                "B": "かろうじて: Suýt soát, chật vật lắm mới kịp/qua được hiểm cảnh.",
                "D": "とっくに: Đã từ rất lâu rồi (quá khứ xa so với thời điểm nói)."
            }
        ),
        (
            "N2_03_M5_04",
            "N2-VOC-SYNO",
            "Mondai 5: 言い換え類義",
            "明日の最終プレゼンテーションの結果がどうなるか、一日中【気がかりだ】。",
            [("A", "退屈だ"), ("B", "心強い"), ("C", "不満だ"), ("D", "心配だ")],
            "D",
            "気がかりだ（きがかりだ）: Luôn bận tâm, thấp thỏm lo âu trong lòng = 心配だ（しんぱいだ）.",
            {
                "A": "退屈だ: Buồn chán, tẻ nhạt không có gì làm.",
                "B": "心強い: Cảm thấy an tâm, vững dạ vì có chỗ dựa.",
                "C": "不満だ: Bất mãn, không vừa lòng, ấm ức."
            }
        ),
        (
            "N2_03_M5_05",
            "N2-VOC-SYNO",
            "Mondai 5: 言い換え類義",
            "納期の遅れによりご迷惑をおかけしましたことを、深く【お詫び】申し上げます。",
            [("A", "謝罪し"), ("B", "感謝し"), ("C", "報告し"), ("D", "要求し")],
            "A",
            "お詫びする（おわびする）: Xin lỗi, tạ lỗi chân thành = 謝罪する（しゃざいする）.",
            {
                "B": "感謝し: Cảm ơn, tri ân sâu sắc.",
                "C": "報告し: Báo cáo tình hình công việc.",
                "D": "要求し: Yêu cầu, đòi hỏi đối phương đáp ứng."
            }
        ),
    ]

    for qid, tid, cat, stem, opts, ans, exp, dist in m5_raw:
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
    # MONDAI 6: 用法 (Usage in Sentence - 5 items)
    # =========================================================================
    m6_raw = [
        (
            "N2_03_M6_01",
            "N2-VOC-USAG",
            "Mondai 6: 用法",
            "次の言葉の使い方として最も適切なものを一つ選びなさい。【ニュアンス】",
            [
                ("A", "この部屋は防音がしっかりしているので、外のニュアンスが全く聞こえない。"),
                ("B", "言葉の微妙なニュアンスの違いを正確に理解して使い分けるのは難しい。"),
                ("C", "新入社員の挨拶からは、若者らしい元気なニュアンスが漂っていた。"),
                ("D", "スマートフォンの充電器のニュアンスが壊れてしまい、画面がつかなくなった。")
            ],
            "B",
            "ニュアンス（nuance）: Sắc thái nghĩa, sắc thái cảm xúc tinh tế khó diễn tả bằng từ ngữ thông thường. Thường dùng với '言葉の微妙なニュアンス'.",
            {
                "A": "Âm thanh bên ngoài phải dùng 音（おと）hoặc 騒音（そうおん）, không dùng ニュアンス.",
                "C": "Không khí tràn đầy năng lượng phải dùng 雰囲気（ふんいき）hoặc 活気（かっき）.",
                "D": "Bộ phận linh kiện sạc hỏng phải dùng 端子（たんし）hoặc 部品（ぶひん）."
            }
        ),
        (
            "N2_03_M6_02",
            "N2-VOC-USAG",
            "Mondai 6: 用法",
            "次の言葉の使い方として最も適切なものを一つ選びなさい。【案の定】",
            [
                ("A", "彼は日頃の努力が実を結び、案の定難関大学の医学部に合格した。"),
                ("B", "明日から旅行に行くのに、案の定パスポートを紛失して大変喜んでいる。"),
                ("C", "空が急に暗くなってきたと思ったら、案の定激しい夕立が降り始めた。"),
                ("D", "彼女は予想もしなかった案の定のサプライズプレゼントに涙を流した。")
            ],
            "C",
            "案の定（あんのじょう）: Quả nhiên, đúng như dự đoán từ trước (thường dùng nhiều nhất với những diễn biến tiêu cực, xấu, hoặc diễn biến thời tiết xấu đã lường trước).",
            {
                "A": "Kết quả nỗ lực thi đỗ tốt đẹp thường dùng 期待通り（きたいどおり）hoặc 見事に（みごとに）.",
                "B": "Mất hộ chiếu mà 'vui mừng' là phi lý, và 案の定 không bổ nghĩa cho cảm xúc tích cực bất thường như vậy.",
                "D": "Không ngờ tới thì hoàn toàn mâu thuẫn với 案の定 (vốn là đúng như đã nghĩ)."
            }
        ),
        (
            "N2_03_M6_03",
            "N2-VOC-USAG",
            "Mondai 6: 用法",
            "次の言葉の使い方として最も適切なものを一つ選びなさい。【著しい】",
            [
                ("A", "近年における再生可能エネルギー技術の進歩には著しいものがある。"),
                ("B", "今日は朝から天気が著しくて、遠くの富士山までくっきりと見えた。"),
                ("C", "このスープはスパイスの著しい味がして、一口飲んだだけで汗が出た。"),
                ("D", "彼は著しい体格をしていて、どんな重い荷物でも軽々と持ち上げる。")
            ],
            "A",
            "著しい（いちじるしい）: Đáng kể, rõ rệt, vượt bậc (thường dùng cho sự biến đổi, tiến bộ, suy giảm rõ nét: 進歩が著しい, 著しい変化).",
            {
                "B": "Thời tiết trong xanh nhìn xa dùng 快晴（かいせい）hoặc 天気が良くて.",
                "C": "Vị cay nồng của gia vị dùng 刺激的な（しげきてきな）hoặc 強烈な（きょうれつな）.",
                "D": "Thân hình to lớn vạm vỡ dùng がっしりした hoặc たくましい."
            }
        ),
        (
            "N2_03_M6_04",
            "N2-VOC-USAG",
            "Mondai 6: 用法",
            "次の言葉の使い方として最も適切なものを一つ選びなさい。【手際】",
            [
                ("A", "あの店のラーメンは、スープの手際が他店とは決定的に違っている。"),
                ("B", "彼は毎日ジョギングを欠かさない手際の良い性格をしている。"),
                ("C", "会議室のプロジェクターの手際が悪くて、映像が途中で途切れた。"),
                ("D", "彼女は長年の経験を生かした鮮やかな手際で、トラブルを短時間で収束させた。")
            ],
            "D",
            "手際（てぎわ）: Kỹ năng xử lý, tài tháo vát, sự khéo léo gọn gàng khi làm việc (thường đi với 手際が良い, 手際よく処理する, 鮮やかな手際).",
            {
                "A": "Vị nước dùng của mì ramen phải dùng 味付け（あじつけ）hoặc 仕込み（しこみ）.",
                "B": "Tính cách kiên trì tập thể dục phải dùng 几帳面な（きちょうめんな）hoặc 根気強い.",
                "C": "Máy móc hoạt động chập chờn phải dùng 機器の調子（ちょうし）hoặc 接続（せつぞく）."
            }
        ),
        (
            "N2_03_M6_05",
            "N2-VOC-USAG",
            "Mondai 6: 用法",
            "次の言葉の使い方として最も適切なものを一つ選びなさい。【まばら】",
            [
                ("A", "テストの範囲がまばらすぎて、どこから勉強を始めればいいか分からない。"),
                ("B", "彼女の歌声はまばらで美しく、会場中の聴衆を魅了した。"),
                ("C", "開場直後は観客もまばらだったが、開演時刻が近づくにつれて満席になった。"),
                ("D", "この道は車のスピードがまばらなので、歩行者は十分注意が必要だ。")
            ],
            "C",
            "まばら（まばらだ / まばらに）: Thưa thớt, rải rác, không đều, lưa thưa (thường dùng cho mật độ người, cây cối, tóc: 人影がまばらだ).",
            {
                "A": "Phạm vi bài thi quá rộng phải dùng 広範（こうはん）hoặc 広すぎる.",
                "B": "Giọng hát du dương trong trẻo phải dùng 澄んだ（すんだ）hoặc 伸びやかな.",
                "D": "Tốc độ xe cộ không ổn định phải dùng ばらばらだ hoặc 不揃い（ふぞろい）."
            }
        ),
    ]

    for qid, tid, cat, stem, opts, ans, exp, dist in m6_raw:
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
    # MONDAI 7: 文法形式 (Sentential Grammar Form - 12 items)
    # =========================================================================
    m7_raw = [
        (
            "N2_03_M7_01",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "今回のプロジェクトの成功は、チーム全員の献身的な努力の賜物に（　　）。",
            [("A", "ほかならない"), ("B", "かぎらない"), ("C", "相違ない"), ("D", "すぎない")],
            "A",
            "〜にほかならない: Chính là, không gì khác ngoài... Dùng để khẳng định mạnh mẽ nguyên nhân cốt lõi hoặc bản chất của sự việc.",
            {
                "B": "〜にかぎらない: Không chỉ giới hạn ở... (chỉ phạm vi), không đi với 賜物に.",
                "C": "〜に相違ない: Chắc chắn là... (phỏng đoán có căn cứ của người nói), không dùng mẫu danh từ + に相違ない mang tính bản chất như ほかならない.",
                "D": "〜にすぎない: Chỉ là... (mang ý hạ thấp mức độ, xem nhẹ sự việc)."
            }
        ),
        (
            "N2_03_M7_02",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "来週の東京公演を（　　）、全国12都市を巡る大規模なツアーが幕を開ける。",
            [("A", "きっかけに"), ("B", "皮切りに"), ("C", "契機として"), ("D", "はじめに")],
            "B",
            "〜を皮切りに（して/として）: Khởi đầu bằng... rồi liên tiếp diễn ra hàng loạt hoạt động cùng quy mô. Đặc trưng đi với chuyến lưu diễn (ツアー), chuỗi sự kiện.",
            {
                "A": "〜をきっかけに: Xuất phát từ duyên cớ ngẫu nhiên dẫn tới thay đổi về sau, không mang sắc thái chuỗi hoạt động mở rộng liên tiếp.",
                "C": "〜を契機として: Lấy bước ngoặt trọng đại làm thời cơ chuyển biến (thường mang tính lịch sử/chính sách lớn).",
                "D": "〜をはじめ（として）: Trước tiên phải kể đến đại diện tiêu biểu (A là đại diện trong nhóm)."
            }
        ),
        (
            "N2_03_M7_03",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "前回の利用客アンケートで寄せられた改善要望を（　　）、新しいメニューを開発した。",
            [("A", "めぐって"), ("B", "通して"), ("C", "踏まえて"), ("D", "問わず")],
            "C",
            "〜を踏まえて: Dựa trên cơ sở, căn cứ vào (kinh nghiệm, kết quả khảo sát, phản ánh) để tiến hành hành động mới.",
            {
                "A": "〜をめぐって: Xoay quanh tranh cãi, thảo luận mâu thuẫn giữa các bên.",
                "B": "〜を通して: Thông qua phương tiện trung gian hoặc suốt một khoảng thời gian.",
                "D": "〜を問わず: Bất kể, không phân biệt (tuổi tác, giới tính, quốc tịch)."
            }
        ),
        (
            "N2_03_M7_04",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "こんな複雑な精密機器の修理は、十分な訓練を受けていない素人にはでき（　　）。",
            [("A", "がたい"), ("B", "かねない"), ("C", "ざるを得ない"), ("D", "っこない")],
            "D",
            "動詞ます形 + っこない: Tuyệt đối không thể, làm sao mà có thể... Phủ định dứt khoát khả năng xảy ra theo phán đoán chủ quan mạnh mẽ của người nói.",
            {
                "A": "〜がたい: Khó lòng mà làm được (thường dùng với động từ tâm lý, biểu cảm như 信じがたい, 理解しがたい, không ghép *できがたい).",
                "B": "〜かねない: Có nguy cơ, e rằng sẽ xảy ra kết quả xấu, không dùng để phủ định khả năng của động từ でき.",
                "C": "〜ざるを得ない: Đành phải, buộc phải làm dù không muốn."
            }
        ),
        (
            "N2_03_M7_05",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "あの雄大な山々の美しい写真を見る（　　）、学生時代に仲間と登った記憶が鮮やかによみがえる。",
            [("A", "につけ"), ("B", "につれて"), ("C", "にしたがって"), ("D", "に際して")],
            "A",
            "〜につけ: Mỗi lần... thì lại (tự nhiên nảy sinh cảm xúc, hồi tưởng tâm lý). Đặc biệt hay đi với 見るにつけ, 聞くにつけ.",
            {
                "B": "〜につれて: Cùng với sự thay đổi của vế A thì vế B thay đổi theo (biến đổi tự nhiên mang tính tỷ lệ thuận).",
                "C": "〜にしたがって: Vừa chỉ sự biến đổi tỷ lệ, vừa chỉ việc tuân theo mệnh lệnh/quy tắc.",
                "D": "〜に際して: Nhân dịp, khi tiến hành một sự kiện đặc biệt (khi kết hôn, khi nhập học)."
            }
        ),
        (
            "N2_03_M7_06",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "安全基準を無視した危険な運行をこのまま放置すれば、取り返しのつかない大事故を引き起こし（　　）。",
            [("A", "かねる"), ("B", "かねない"), ("C", "がちだ"), ("D", "きれない")],
            "B",
            "動詞ます形 + かねない: Có nguy cơ, rất có thể sẽ dẫn đến kết quả xấu/nguy hiểm.",
            {
                "A": "〜かねる: Khó lòng có thể, từ chối một cách lịch sự vì lý do lập trường (引き受けかねます).",
                "C": "〜がちだ: Thường hay có xu hướng (xảy ra thường xuyên như 忘れがち, 曇りがち).",
                "D": "〜きれない: Không thể làm hết trọn vẹn (数えきれない)."
            }
        ),
        (
            "N2_03_M7_07",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "市役所では、国の基本方針（　　）、市民向けの災害時避難行動マニュアルを改定した。",
            [("A", "を皮切りに"), ("B", "に反して"), ("C", "に沿って"), ("D", "をよそに")],
            "C",
            "〜に沿って（にそって）: Men theo, tuân theo sát sao (kế hoạch, đường lối, quy chuẩn, phương châm).",
            {
                "A": "〜を皮切りに: Khởi đầu chuỗi sự kiện, không đi với 方針.",
                "B": "〜に反して: Trái ngược lại hoàn toàn với (kỳ vọng, dự đoán).",
                "D": "〜をよそに: Mặc kệ, phớt lờ không bận tâm đến (lời khuyên, sự can ngăn)."
            }
        ),
        (
            "N2_03_M7_08",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "彼は何か言い（　　）な表情を浮かべたが、結局唇を結んだまま立ち去ってしまった。",
            [("A", "っぽい"), ("B", "がち"), ("C", "ぎみ"), ("D", "たげ")],
            "D",
            "〜たげ: Có vẻ, dường như muốn... Đi sau tính từ hoặc thể たい (bỏ い) -> 言いたげ (vẻ như muốn nói điều gì đó).",
            {
                "A": "〜っぽい: Thiên về tính chất, dễ nổi cáu hay màu nhờ nhờ (怒りっぽい, 安っぽい).",
                "B": "〜がち: Hay bị, có xu hướng hay xảy ra (遠慮がち, 病気がち, không ghép *言いたがち).",
                "C": "〜ぎみ: Hơi có triệu chứng, hơi có chiều hướng tiêu cực (風邪ぎみ, 疲れぎみ)."
            }
        ),
        (
            "N2_03_M7_09",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "週末は家でゆっくり静養する（　　）、急なトラブル対応で二日間とも徹夜する羽目になった。",
            [("A", "どころか"), ("B", "ばかりか"), ("C", "反面"), ("D", "あげく")],
            "A",
            "〜どころか: Đâu mà được... trái lại còn tồi tệ hơn nhiều. Biểu thị sự tương phản cực độ giữa mong muốn/kỳ vọng và thực tế nghiệt ngã.",
            {
                "B": "〜ばかりか: Không những... mà còn (vế sau bổ sung tăng tiến thêm, không mang nghĩa trái ngược phủ định hoàn toàn vế trước).",
                "C": "〜反面: Mặt khác (nêu hai mặt của cùng một vấn đề).",
                "D": "〜あげく: Sau một hồi dằng dai thì dẫn đến kết quả xấu (phải đi sau thể た: 話し合ったあげく)."
            }
        ),
        (
            "N2_03_M7_10",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "創立50周年の節目を（　　）、企業イメージを一新するための新たなロゴマークが発表された。",
            [("A", "皮切りに"), ("B", "契機として"), ("C", "もとに"), ("D", "ぬきにして")],
            "B",
            "〜を契機として（をけいきとして）: Lấy làm cơ hội, lấy làm bước ngoặt lớn để tạo ra sự đổi mới, chuyển biến tích cực.",
            {
                "A": "〜を皮切りに: Bắt đầu chuỗi sự kiện cùng loại liên tiếp (tour diễn, đợt mở rộng).",
                "C": "〜をもとに: Dựa trên chất liệu, dữ liệu thực tế để tạo ra tác phẩm/sản phẩm mới (事実をもとに小説を書く).",
                "D": "〜をぬきにして: Nếu không có, bỏ qua yếu tố A thì không thể nói tới B."
            }
        ),
        (
            "N2_03_M7_11",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "社内で幾度にもわたる激しい議論を重ねた（　　）、不採算事業から撤退する方針を固めた。",
            [("A", "際して"), ("B", "次第で"), ("C", "末に"), ("D", "あまり")],
            "C",
            "動詞た形 / 名詞の + 末に（すえに）: Sau một thời gian dài trải qua nhiều khó khăn, trăn trở thì cuối cùng cũng đi đến kết quả.",
            {
                "A": "〜に際して: Nhân dịp tiến hành một sự kiện quan trọng.",
                "B": "〜次第で: Tùy thuộc vào yếu tố A mà vế B thay đổi.",
                "D": "〜あまり: Vì quá mức... nên dẫn tới một kết quả bất thường (心配のあまり)."
            }
        ),
        (
            "N2_03_M7_12",
            "N2-GR-SENT",
            "Mondai 7: 文法形式の判断",
            "現場に残された足跡と防犯カメラの映像から判断して、容疑者はこの人物に（　　）。",
            [("A", "及ばない"), ("B", "すぎない"), ("C", "かぎらない"), ("D", "相違ない")],
            "D",
            "〜に相違ない: Chắc chắn là, không thể sai được. Khẳng định phán đoán của người nói dựa trên bằng chứng, chứng cứ rõ ràng.",
            {
                "A": "〜にほかならない: Chính là (nêu bản chất/nguyên nhân cốt lõi, không mang tính phán đoán danh tính nghi phạm).",
                "B": "〜にすぎない: Chỉ là... (xem nhẹ mức độ).",
                "C": "〜にかぎらない: Không chỉ có... (phủ định tính giới hạn)."
            }
        ),
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
    # =========================================================================
    m8_raw = [
        (
            "N2_03_M8_01",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "彼が今回の難関試験に一発で合格できたのは、（　　）（　　） ★ （　　）ほかならない。",
            [
                ("A", "毎日の地道な"),
                ("B", "努力を"),
                ("C", "怠らなかった"),
                ("D", "結果に")
            ],
            "C",
            "Thứ tự đúng: A - B - C - D (毎日の地道な 努力を 怠らなかった 結果に). Cấu trúc ngữ pháp N2: 〜にほかならない (chính là, không gì khác ngoài...). [A 毎日の地道な] bổ nghĩa cho [B 努力を]. Cụm [B 努力を] [C 怠らなかった] làm định ngữ bổ nghĩa cho danh từ [D 結果に]. Kết hợp với đuôi câu: 結果にほかならない. Vị trí ngôi sao ★ là C (怠らなかった).",
            {
                "A": "[Vị trí 1] Tính từ đuôi な bổ nghĩa cho danh từ 努力.",
                "B": "[Vị trí 2] Tân ngữ trực tiếp của động từ 怠らなかった.",
                "D": "[Vị trí 4] Danh từ đi với trợ từ に trước ほかならない."
            }
        ),
        (
            "N2_03_M8_02",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て",
            "どんなに科学技術が（　　）（　　） ★ （　　）失ってはならない。",
            [("A", "発展しようとも、"), ("B", "私たちは"), ("C", "自然への"), ("D", "畏敬の念を")],
            "C",
            "Thứ tự đúng: A - B - C - D (発展しようとも、 私たちは 自然への 畏敬の念を). Cấu trúc: どんなに〜ようとも (cho dù... đến mức nào đi chăng nữa). Vế chính: [B 私たちは] [C 自然への] [D 畏敬の念を] 失ってはならない (chúng ta không được đánh mất lòng kính sợ đối với tự nhiên). Vị trí ngôi sao ★ là C (自然への).",
            {
                "A": "A đứng ở vị trí thứ nhất đi liền với どんなに科学技術が.",
                "B": "B đứng ở vị trí thứ hai làm chủ ngữ cho mệnh đề chính.",
                "D": "D đứng ở vị trí thứ tư làm tân ngữ trực tiếp cho 失ってはならない."
            }
        ),
        (
            "N2_03_M8_03",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て",
            "今回の不祥事は、（　　）（　　） ★ （　　）問題である。",
            [("A", "個人の過失に"), ("B", "とどまらず、"), ("C", "組織全体の"), ("D", "管理体制に関わる")],
            "C",
            "Thứ tự đúng: A - B - C - D (個人の過失に とどまらず、 組織全体の 管理体制に関わる). Mẫu ngữ pháp: 〜にとどまらず (không chỉ dừng lại ở...). [A 個人の過失に] [B とどまらず、] [C 組織全体の] [D 管理体制に関わる] 問題である (vấn đề liên quan tới cơ chế quản lý của toàn bộ tổ chức). Vị trí ngôi sao ★ là C (組織全体の).",
            {
                "A": "A đứng ở vị trí thứ nhất đi với に.",
                "B": "B đứng ở vị trí thứ hai (〜にとどまらず).",
                "D": "D đứng ở vị trí thứ tư bổ nghĩa cho danh từ 問題."
            }
        ),
        (
            "N2_03_M8_04",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "プロの演奏家として（　　）（　　） ★ （　　）怠ってはならない。",
            [
                ("A", "観客の前に"),
                ("B", "立つからには、"),
                ("C", "日々の地道な"),
                ("D", "練習を")
            ],
            "C",
            "Thứ tự đúng: A - B - C - D (観客の前に 立つからには、 日々の地道な 練習を). Cấu trúc ngữ pháp N2: 〜からには (một khi đã... thì phải). [A 観客の前に] [B 立つからには、] tạo thành vế điều kiện tiền đề. Vế sau: [C 日々の地道な] bổ nghĩa trực tiếp cho tân ngữ [D 練習を] của động từ 怠ってはならない. Vị trí ngôi sao ★ là C (日々の地道な).",
            {
                "A": "[Vị trí 1] Cụm trạng ngữ chỉ địa điểm gắn liền trước động từ 立つ.",
                "B": "[Vị trí 2] Vế điều kiện 〜からには, có dấu phẩy ngắt vế rõ ràng.",
                "D": "[Vị trí 4] Tân ngữ đứng liền trước động từ 怠ってはならない."
            }
        ),
        (
            "N2_03_M8_05",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "彼がこれほど短期間で大きな成果を上げられたのは、（　　）（　　） ★ （　　）賜物だ。",
            [
                ("A", "地道に努力を"),
                ("B", "重ねてきた"),
                ("C", "素直に耳を傾け、"),
                ("D", "周囲の助言に")
            ],
            "A",
            "Thứ tự đúng: D - C - A - B (周囲の助言に 素直に耳を傾け、 地道に努力を 重ねてきた). Cấu trúc ngữ pháp N2: 〜賜物だ (kết quả/hoa trái của...). [D 周囲の助言に] kết hợp với [C 素直に耳を傾け、] tạo vế tiếp thu ý kiến xung quanh. Vế sau: [A 地道に努力を] là tân ngữ của [B 重ねてきた] bổ nghĩa trực tiếp cho danh từ 賜物だ. Thứ tự duy nhất hợp cú pháp và tự nhiên là D - C - A - B. Vị trí ngôi sao ★ là A (地道に努力を).",
            {
                "B": "B (重ねてきた) đứng ở vị trí thứ tư bổ nghĩa trực tiếp cho danh từ 賜物だ.",
                "C": "C (素直に耳を傾け、) đứng ở vị trí thứ hai làm vế liên kết nối tiếp.",
                "D": "D (周囲の助言に) đứng ở vị trí thứ nhất đi liền với cụm động từ 耳を傾ける."
            }
        ),
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
    m9_passage = """近年、在宅勤務やテレワークの普及により、働く場所の自由度は飛躍的に向上した。通勤ラッシュのストレスから解放され、個人の裁量で時間を有効活用できるメリットは計り知れない。（ 46 ）、自宅という私的な空間で長時間高い集中力を維持することは、決して容易ではない。同僚の目がなく、周囲に誘惑が多い環境下では、自制心が緩んでしまいがちだからである。

心理学の研究によれば、人間の意志の力には限界があり、集中を持続させるためには環境設計が極めて重要だとされている。つまり、単に「気合で集中しよう」と力むのではなく、集中を妨げる要因を物理的に遠ざける工夫（ 47 ）。たとえば、作業中はスマートフォンの通知を切り、視界に入らない場所に置くだけでも、脳への認知的負荷は劇的に軽減される。

さらに、休憩の取り方にも工夫が求められる。疲労を感じてから休むのではなく、一定時間集中したら意図的に小休止を挟む（ 48 ）、持続的なパフォーマンスを発揮できるようになる。長時間の作業をぶっ続けで行うことは、一見すると効率的に見えるかもしれない。（ 49 ）、実際には後半になるほど著しい集中力の低下を招き、ミスの温床となりかねないのだ。

テレワーク時代における真の「自由」とは、単に好きな場所でだらだらと働くことではない。環境を自律的にデザインし、自らの集中と休息をコントロールする規律を身につけることこそが、豊かな職業人生を実現するための必須要件と（ 50 ）。"""

    m9_raw = [
        (
            "N2_03_M9_01",
            "N2-GR-TEXT",
            "Mondai 9: 文章の文法",
            "（ 46 ）に入る最も適切なものはどれか。",
            m9_passage,
            [("A", "しかしながら"), ("B", "それゆえに"), ("C", "さらに"), ("D", "すなわち")],
            "A",
            "46: Đoạn trước nêu mặt lợi thế to lớn của làm việc từ xa (tiết kiệm thời gian, giảm stress đi lại). Ngay sau đó là việc duy trì tập trung ở nhà không hề đơn giản. Mối quan hệ tương phản đối lập rõ rệt -> dùng liên từ đối lập trang trọng 'しかしながら' (Tuy nhiên).",
            {
                "B": "それゆえに: Do đó, vì lý do đó (chỉ hệ quả tất yếu).",
                "C": "さらに: Hơn nữa (bổ sung thông tin cùng chiều tích cực).",
                "D": "すなわち: Tức là, nói cách khác (giải thích từ ngữ/khái niệm vừa nêu)."
            }
        ),
        (
            "N2_03_M9_02",
            "N2-GR-TEXT",
            "Mondai 9: 文章の文法",
            "（ 47 ）に入る最も適切なものはどれか。",
            m9_passage,
            [("A", "にほかならない"), ("B", "こそが求められる"), ("C", "にすぎない"), ("D", "わけがない")],
            "B",
            "47: Tác giả nhấn mạnh: thay vì cố gắng bằng ý chí suông, điều thực sự được đòi hỏi chính là các biện pháp thiết kế môi trường vật lý ngăn chặn phân tâm -> dùng trợ từ nhấn mạnh 'こそが' đi cùng dạng bị động yêu cầu '求められる' (chính điều này mới là cái được đòi hỏi).",
            {
                "A": "にほかならない: Không gì khác ngoài (khẳng định bản chất danh từ, câu ở đây cần vị ngữ hành động đòi hỏi giải pháp).",
                "C": "にすぎない: Chỉ là (mang tính hạ thấp, xem nhẹ, trái với ý nhấn mạnh tầm quan trọng của tác giả).",
                "D": "わけがない: Lẽ nào lại, không đời nào (phủ định tính logic)."
            }
        ),
        (
            "N2_03_M9_03",
            "N2-GR-TEXT",
            "Mondai 9: 文章の文法",
            "（ 48 ）に入る最も適切なものはどれか。",
            m9_passage,
            [("A", "ものの"), ("B", "反面"), ("C", "ことによって"), ("D", "うえに")],
            "C",
            "48: Câu trình bày phương pháp nghỉ ngơi: 'bằng việc chủ động nghỉ giải lao ngắn sau một khoảng thời gian tập trung' -> dẫn đến kết quả 'trở nên có thể duy trì phong độ làm việc liên tục'. Chỉ phương thức, cách thức dẫn đến kết quả tốt -> dùng 'ことによって' (bằng việc, nhờ vào việc).",
            {
                "A": "ものの: Mặc dù... nhưng (chỉ sự đối lập nhượng bộ).",
                "B": "反面: Trái lại, mặt khác (đối chiếu hai mặt đối lập).",
                "D": "うえに: Thêm vào đó, hơn nữa (đồng thời có hai tính chất)."
            }
        ),
        (
            "N2_03_M9_04",
            "N2-GR-TEXT",
            "Mondai 9: 文章の文法",
            "（ 49 ）に入る最も適切なものはどれか。",
            m9_passage,
            [
                ("A", "そのうえ"),
                ("B", "それにもかかわらず"),
                ("C", "したがって"),
                ("D", "それにひきかえ")
            ],
            "B",
            "49: Vế trước đưa ra nhận định mang tính nhượng bộ: '長時間の作業をぶっ続けで行うことは、一見すると効率的に見えるかもしれない' (Làm việc liên tục suốt thời gian dài thoạt nhìn có vẻ hiệu quả). Vế sau chỉ ra thực tế trái ngược: '実際には後半になるほど著しい集中力の低下を招き...' (nhưng trong thực tế càng về sau càng giảm sút tập trung). Liên từ nghịch đề chỉ sự tương phản đối lập với nhượng bộ trước đó phù hợp nhất là 'それにもかかわらず' (tuy nhiên, mặc dù vậy).",
            {
                "A": "そのうえ: Hơn nữa (bổ sung thông tin cùng chiều, không dùng sau vế nhượng bộ 一見〜見えるかもしれない).",
                "C": "したがって: Do đó (quan hệ nhân quả thuận, không hợp văn cảnh nghịch đối).",
                "D": "それにひきかえ: So với điều đó thì... (dùng so sánh đối chiếu hai sự vật khác nhau)."
            }
        ),
        (
            "N2_03_M9_05",
            "N2-GR-TEXT",
            "Mondai 9: 文章の文法",
            "（ 50 ）に入る最も適切なものはどれか。",
            m9_passage,
            [("A", "言えるのではないだろうか"), ("B", "言うまでもないことだ"), ("C", "言うはずがない"), ("D", "言わざるを得ないのだ")],
            "A",
            "50: Câu kết luận toàn bài nêu nhận định khái quát mang tính chiêm nghiệm và đề xuất quan điểm của tác giả một cách nhã nhặn, chuẩn mực văn phong nghị luận JLPT: '〜と言えるのではないだろうか' (Chẳng phải là có thể nói rằng... hay sao).",
            {
                "B": "言うまでもないことだ: Là điều không cần nói cũng rõ (giọng điệu quá hiển nhiên, không phù hợp cho câu kết đúc kết quan điểm mở).",
                "C": "言うはずがない: Chắc chắn không đời nào nói (phủ định phi lý).",
                "D": "言わざるを得ないのだ: Buộc lòng đành phải nói (chỉ sự bất đắc dĩ, không hợp với giọng điệu tích cực xây dựng ở phần kết)."
            }
        ),
    ]

    for qid, tid, cat, stem, pass_text, opts, ans, exp, dist in m9_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Language Knowledge",
            "category": cat,
            "stem": stem,
            "contextPassage": pass_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist
        })

    # =========================================================================
    # MONDAI 10: 短文読解 (Short Reading Comprehension - 5 items)
    # =========================================================================
    p10_1 = """職場のコミュニケーションにおいて、「話す力」ばかりが注目されがちだが、真に信頼関係を築くために不可欠なのは「聴く力」である。相手の言葉の表面だけをなぞるのではなく、その発言の背景にある懸念や熱意にまで耳を傾ける姿勢があって初めて、相手は「理解された」という安心感を得る。的確なアドバイスを急ぐよりも、まずは相手の話を遮らずに最後まで受け止めること。それこそが、円滑な協力体制を生み出すための最も堅実な土台となるのである。"""
    
    p10_2 = """都市部における緑地空間の整備は、単なる景観の美化にとどまらない深い意義を持っている。近年の環境心理学の知見によれば、日常的に樹木や水辺に触れる生活環境は、ストレスホルモンの分泌を有意に抑制し、住民の精神的な回復力を高める効果があるという。無機質なコンクリートに囲まれた現代社会において、自然の息吹を感じられる場所を意識的に確保することは、市民の健康維持における不可欠な予防医療の一環と位置づけられるべきである。"""

    p10_3 = """伝統工芸の技術を次世代へ継承するにあたり、昔ながらの技法を忠実に守り続けることだけが正解とは限らない。時代の変化に伴い、人々の生活様式や美的感覚も刻々と移り変わっていくからである。伝統とは、固定された過去の遺物ではなく、その時代の需要や感性と対話を繰り返しながら更新されていく生きた営みである。本質的な精神を受け継ぎつつも、現代のライフスタイルに調和する新たなデザインや用途を果敢に模索する姿勢こそが、伝統を未来へと息づかせる。"""

    p10_4 = """【社内通知：クラウドストレージ運用ルールの改定について】
来月1日より、セキュリティ強化を目的として、全社共通クラウドストレージのアクセス権限および保存期間に関する新ルールを適用します。これまで個人の判断で無期限に保管可能だった業務関連データのうち、プロジェクト終了から1年以上が経過したファイルについては、専用のアーカイブ領域へ自動移行されます。なお、社外秘に指定されている重要文書を外部パートナーと共有する際は、事前の所属長承認が必須となりますのでご注意ください。"""

    p10_5 = """読書において、一つの専門分野を体系的に深く掘り下げる「精読」が重んじられる一方で、あえて多分野の書籍に無目的に手を伸ばす「乱読」の効用も見逃せない。予期せぬ分野の知識や視点が、自分の中に蓄積されていた既存の概念と偶発的に結びつくことで、これまでにない斬新な着想が生まれるからである。一見すると無駄に思える寄り道のような読書体験こそが、思考の硬直化を防ぎ、柔軟な創造力を育む豊かな土壌となる。"""

    m10_raw = [
        (
            "N2_03_M10_01",
            "N2-RE-SHORT",
            "Mondai 10: 短文読解",
            "筆者が職場のコミュニケーションにおいて最も重要だと考えていることは何か。",
            p10_1,
            [
                ("A", "相手の話を途中で遮らず、背景にある心情まで深く受け止めること。"),
                ("B", "相手の抱える問題に対して、即座に的確な解決アドバイスを与えること。"),
                ("C", "自分の意見や主張を論理的かつ説得力豊かに相手に伝えること。"),
                ("D", "言葉の表現方法を磨き、表面的な会話をスムーズに進めること。")
            ],
            "A",
            "Tác giả nhấn mạnh: điều không thể thiếu để tạo dựng lòng tin là 'lắng nghe'. Thay vì vội vã đưa ra lời khuyên, trước hết phải tiếp nhận trọn vẹn câu chuyện của đối phương và lắng nghe cả những âu lo, nhiệt huyết đằng sau đó mà không ngắt lời. Đáp án đúng là A.",
            {
                "B": "Văn bản nêu rõ '的確なアドバイスを急ぐよりも' (thay vì vội đưa lời khuyên), việc này không phải ưu tiên hàng đầu.",
                "C": "Văn bản phê phán việc quá chú trọng vào 'nói' (話す力ばかりが注目されがちだが).",
                "D": "Văn bản khẳng định không được chỉ lướt trên bề mặt từ ngữ (相手の言葉の表面だけをなぞるのではなく)."
            }
        ),
        (
            "N2_03_M10_02",
            "N2-RE-SHORT",
            "Mondai 10: 短文読解",
            "都市の緑地空間について、筆者の主張と合致するものはどれか。",
            p10_2,
            [
                ("A", "都市の観光価値を高めるための景観美化が最大の目的である。"),
                ("B", "住民のストレスを軽減し、健康維持に寄与する予防医療的な価値を持つ。"),
                ("C", "コンクリート建造物の建設コストを削減するための代替策である。"),
                ("D", "自然環境の完全な保護のために、人間が立ち入れない区域にすべきである。")
            ],
            "B",
            "Tác giả chỉ ra rằng không gian xanh đô thị không chỉ làm đẹp cảnh quan mà giúp ức chế hormone stress, nâng cao khả năng phục hồi tinh thần của cư dân, được coi là một khâu y tế dự phòng không thể thiếu. Đáp án B đúng.",
            {
                "A": "Văn bản nói rõ '単なる景観の美化にとどまらない' (không chỉ dừng lại ở việc làm đẹp cảnh quan).",
                "C": "Văn bản không hề đề cập đến việc giảm chi phí xây dựng bê tông.",
                "D": "Tác giả muốn người dân được thường xuyên tiếp xúc với thiên nhiên trong cuộc sống hàng ngày, chứ không phải cấm người vào."
            }
        ),
        (
            "N2_03_M10_03",
            "N2-RE-SHORT",
            "Mondai 10: 短文読解",
            "伝統工芸の継承に関して、筆者が述べていることはどれか。",
            p10_3,
            [
                ("A", "過去の技法をいささかも変更せずに完全に維持することだけが使命である。"),
                ("B", "人々の生活様式に関わらず、伝統の本質的なデザインのみを守るべきだ。"),
                ("C", "本質を受け継ぎながらも、現代の生活に調和する新しい用途やデザインを模索すべきだ。"),
                ("D", "過去の伝統技法をすべて捨て去り、最新の工業技術に置き換えるべきだ。")
            ],
            "C",
            "Tác giả khẳng định truyền thống không phải cổ vật cố định mà là sự đối thoại sống động với thời đại: vừa tiếp thu tinh thần cốt lõi vừa dũng cảm tìm tòi ứng dụng và thiết kế mới hài hòa với lối sống hiện đại. Đáp án C hoàn toàn chính xác.",
            {
                "A": "Văn bản phủ định điều này ngay câu đầu: '昔ながらの技法を忠実に守り続けることだけが正解とは限らない'.",
                "B": "Trái với ý tác giả là phong cách sống thay đổi nên truyền thống cũng cần cập nhật.",
                "D": "Tác giả khẳng định '本質的な精神を受け継ぎつつも' (vừa kế thừa tinh thần cốt lõi), không hề bảo vứt bỏ truyền thống."
            }
        ),
        (
            "N2_03_M10_04",
            "N2-RE-SHORT",
            "Mondai 10: 短文読解",
            "この社内通知の内容として正しいものはどれか。",
            p10_4,
            [
                ("A", "プロジェクト終了後すぐにすべての業務データがストレージから削除される。"),
                ("B", "社外秘文書を外部と共有する際は、個人の判断で自由に送信してよい。"),
                ("C", "来月1日以降も、すべてのデータは無期限に個人領域で保管できる。"),
                ("D", "プロジェクト終了から1年を経過したファイルは専用領域へ自動的に移行される。")
            ],
            "D",
            "Thông báo nêu rõ: 'プロジェクト終了から1年以上が経過したファイルについては、専用のアーカイブ領域へ自動移行されます' (các file sau khi kết thúc dự án quá 1 năm sẽ tự động chuyển vào vùng lưu trữ chuyên dụng). Đáp án D đúng.",
            {
                "A": "Không phải xóa ngay lập tức mà sau 1 năm sẽ chuyển vào vùng lưu trữ chuyên dụng.",
                "B": "Chia sẻ tài liệu mật với đối tác bắt buộc phải có phê duyệt trước của trưởng bộ phận ('事前の所属長承認が必須').",
                "C": "Quy định cũ mới là lưu vô thời hạn, quy định mới đã thay đổi điều này."
            }
        ),
        (
            "N2_03_M10_05",
            "N2-RE-SHORT",
            "Mondai 10: 短文読解",
            "読書における「乱読」について、筆者はどのように考えているか。",
            p10_5,
            [
                ("A", "予期せぬ知識の結合を促し、柔軟で創造的な発想を生み出す土壌となる。"),
                ("B", "専門的な深い知識の習得を妨げるため、極力避けるべき無駄な行為である。"),
                ("C", "一つの専門書を最初から最後まで完全に理解するために不可欠な手法である。"),
                ("D", "思考を硬直化させ、既存の知識を忘れさせてしまう危険な読書法である。")
            ],
            "A",
            "Tác giả chỉ ra rằng việc đọc tản mạn nhiều lĩnh vực giúp các kiến thức khác nhau tình cờ kết nối với ý niệm cũ trong đầu, tạo ra cảm hứng sáng tạo mới và nuôi dưỡng mảnh đất tư duy linh hoạt. Đáp án A đúng.",
            {
                "B": "Trái ngược quan điểm tác giả: tác giả coi đây là trải nghiệm giá trị chứ không phải hành vi vô ích cần tránh.",
                "C": "Đọc sâu chuyên môn là 精読, không phải 乱読.",
                "D": "Tác giả nói việc này 'ngăn chặn sự xơ cứng tư duy' (思考の硬直化を防ぎ), chứ không phải làm tư duy xơ cứng."
            }
        ),
    ]

    for qid, tid, cat, stem, pass_text, opts, ans, exp, dist in m10_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Reading",
            "category": cat,
            "stem": stem,
            "contextPassage": pass_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "stimulusType": "reading_passage"
        })

    # =========================================================================
    # MONDAI 11: 中文読解 (Medium Reading Comprehension - 9 items / 3 texts)
    # =========================================================================
    # Text 1: 人工知能と人間の創造性
    p11_1 = """近年、生成AIをはじめとする人工知能の急速な進歩により、文章の執筆やイラストの作成、さらには楽曲の作曲までもが機械によって高精度に行われるようになった。これに伴い、「いずれ人間の創造的な仕事はすべてAIに奪われてしまうのではないか」という懸念が各方面で囁かれている。

しかし、AIが生成する作品の仕組みを冷静に観察すれば、それらが過去の膨大な学習データに基づき、統計的な確率計算によって最も調和のとれた組み合わせを出力しているにすぎないことがわかる。AIは驚異的な速度で完成度の高い成果物を提示できるが、自らの内発的な動機や感情、あるいは社会に対する実感を起点として「何かを表現したい」という情熱を抱いているわけではない。

これに対して、人間の創造性の根源には、常に個人的な「葛藤」や「切実な経験」が存在する。理不尽な現実に直面したときの悲しみや、誰かと深く通じ合えたときの喜びといった生々しい感情の揺らぎこそが、これまでにない独自の視点や表現を生み出す原動力となるのだ。既存の枠組みを逸脱し、時に不完全でありながらも人々の心を揺さぶる作品を生み出せるのは、生身の身体を持ち、有限の時間を生きる人間ならではの特権である。

したがって、AIの登場によって人間の役割が失われると悲観するのではなく、AIを思考の補助ツールとして活用しながら、人間にしか持ち得ない問いを立てる力や、意味を紡ぎ出す感性をいかに磨くかこそが、これからの時代に問われているのである。"""

    # Text 2: 地方創生と新しいコミュニティ
    p11_2 = """少子高齢化と過疎化が進む地方都市において、人口減少を食い止めるための様々な施策が模索されている。かつては工場の誘致や大規模な観光開発など、外的な資本に依存した地域振興策が主流であった。しかし、そうした手法の多くは景気の変動に弱く、持続的な地域社会の自立には結びつきにくかった。

そうした中、近年注目を集めているのが、都市部からの移住者や関係人口を核とした「小規模で有機的なコミュニティ」の再生である。地方に移住してくる人々の多くは、物質的な豊かさや利便性よりも、自然豊かな環境での子育てや、顔の見える人間関係、自己実現の機会を求めている。彼らは古民家を活用したカフェの開業や、地域の特産品を生かした独自ビジネスなど、従来の住民には見落とされていた地域の潜在的価値を再発見し、新たな活力を吹き込んでいる。

重要なのは、新旧の住民が相互に尊重し合える寛容な土壌をいかに醸成するかである。新参者の斬新なアイデアを受け入れつつも、地域に古くから伝わる伝統行事や共同体維持のためのルールを軽視してはならない。双方が歩み寄り、世代や出身地を超えた対話を重ねることで初めて、画一的な経済開発とは異なる、しなやかで強靭な新しい地域共同体が育まれるのである。"""

    # Text 3: デジタル時代における手書きの意義
    p11_3 = """キーボードやタッチパネルによる文字入力が日常化した現代において、ペンを握って紙に文字を手書きする機会は劇的に減少した。検索機能や予測変換の恩恵により、文章作成の速度と効率性は飛躍的に向上したことは否定できない事実である。

しかし、手で文字を書くという行為には、単なる情報伝達の効率化を超えた認知的な深まりが伴っている。脳科学の実験によれば、キーボードでのタイピングと比較して、手書きでノートを取る行為は、複雑な運動機能を刺激し、記憶の定着や概念理解を格段に促進することが判明している。手書きの場合、話された言葉を一言一句そのまま記録することは不可能なため、人間は自然と耳に入った情報を頭の中で要約し、自分の言葉に咀嚼して紙の上に配置するという高度な情報処理を無意識に行っているからである。

さらに、手書きの文字には書き手のその時々の感情や呼吸、迷いといった身体性がそのまま痕跡として刻まれる。手紙を受け取った人が、活字のメールでは味わえない温もりや親近感を覚えるのは、まさにそこに書き手の存在そのものが宿っているからに他ならない。効率性と即時性が至上命題とされるデジタル社会だからこそ、立ち止まって思考を深め、心を込めて文字を綴る手書きの価値を再評価すべき時が来ているのではないだろうか。"""

    m11_raw = [
        # Passage 1 Questions
        (
            "N2_03_M11_01",
            "N2-RE-MED",
            "Mondai 11: 中文読解",
            "AIが作品を生成する仕組みについて、筆者はどのように説明しているか。",
            p11_1,
            [
                ("A", "独自の感情や意志を持ち、社会への熱い情熱に基づいて表現している。"),
                ("B", "過去の膨大な学習データから統計的な確率計算によって出力を組み立てている。"),
                ("C", "人間の葛藤や切実な体験を身体的に模倣して作品を創り出している。"),
                ("D", "既存の枠組みを完全に無視し、全く新しい概念をゼロから生み出している。")
            ],
            "B",
            "Đoạn 2 nêu rõ: các tác phẩm AI sinh ra chỉ là '過去の膨大な学習データに基づき、統計的な確率計算によって最も調和のとれた組み合わせを出力しているにすぎない' (chỉ là xuất ra sự kết hợp hài hòa nhất bằng tính toán xác suất thống kê dựa trên dữ liệu học khổng lồ trong quá khứ). Đáp án B đúng.",
            {
                "A": "Văn bản khẳng định ngược lại: AI không hề có động cơ nội tại hay tình cảm, cũng không có nhiệt huyết muốn biểu đạt gì.",
                "C": "Sự giằng xé và trải nghiệm thiết tha là đặc trưng của con người, AI không có cơ thể sống để trải nghiệm điều này.",
                "D": "AI làm việc dựa trên thống kê dữ liệu có sẵn, không phải sáng tạo ra từ con số 0."
            }
        ),
        (
            "N2_03_M11_02",
            "N2-RE-MED",
            "Mondai 11: 中文読解",
            "筆者によると、人間の創造性の真の根源とは何か。",
            p11_1,
            [
                ("A", "膨大な情報を短時間で処理し、ミスのない完璧な成果物を提示する能力。"),
                ("B", "高度なプログラミング技術を駆使して、最新のデジタルツールを操作する力。"),
                ("C", "生身の身体で経験する悲しみや喜びといった個人的な葛藤や切実な感情の揺らぎ。"),
                ("D", "過去のあらゆる芸術作品の様式を正確に記憶し、忠実に再現する技術。")
            ],
            "C",
            "Đoạn 3 khẳng định: gốc rễ sáng tạo của con người bắt nguồn từ những 'giằng xé' và 'trải nghiệm thiết tha cá nhân', sự dao động cảm xúc chân thực của hỉ nộ ái ố mà chỉ con người bằng xương bằng thịt mới có. Đáp án C đúng.",
            {
                "A": "Xử lý thông tin nhanh và không lỗi là thế mạnh của máy móc, không phải gốc rễ sáng tạo con người.",
                "B": "Thao tác công nghệ chỉ là kỹ năng sử dụng công cụ.",
                "D": "Tái hiện chính xác phong cách quá khứ là việc tính toán dữ liệu của AI."
            }
        ),
        (
            "N2_03_M11_03",
            "N2-RE-MED",
            "Mondai 11: 中文読解",
            "AI時代の到来に対して、筆者が提案している人間の姿勢はどれか。",
            p11_1,
            [
                ("A", "AIの利用を完全に禁止し、すべての創作活動を手作業に戻すこと。"),
                ("B", "人間の仕事が失われる現実に諦めをつけ、AIの指示に全面的に従うこと。"),
                ("C", "AIよりも速く正確に文章や楽曲を完成させるスピード競争に勝つこと。"),
                ("D", "AIを思考の補助ツールとし、人間にしかできない問いを立てる力や感性を磨くこと。")
            ],
            "D",
            "Câu kết đoạn cuối nhấn mạnh: không nên bi quan cho rằng con người mất hết vai trò, mà hãy dùng AI như công cụ hỗ trợ tư duy, đồng thời rèn luyện năng lực đặt câu hỏi và xúc cảm dệt nên ý nghĩa mà chỉ con người mới có. Đáp án D đúng.",
            {
                "A": "Tác giả ủng hộ việc dùng AI như công cụ hỗ trợ tư duy, không bài xích cấm đoán.",
                "B": "Tác giả phản đối thái độ bi quan buông xuôi.",
                "C": "Tác giả khẳng định con người không cạnh tranh về tốc độ hay sự hoàn mỹ cơ học với AI."
            }
        ),

        # Passage 2 Questions
        (
            "N2_03_M11_04",
            "N2-RE-MED",
            "Mondai 11: 中文読解",
            "従来の地方振興策について、筆者はどのような問題点を指摘しているか。",
            p11_2,
            [
                ("A", "工場誘致や観光開発などの外的資本依存は、景気変動に弱く自立に結びつきにくかった。"),
                ("B", "地域の特産品や古民家の価値を過剰に宣伝しすぎたため、住民の負担が増えた。"),
                ("C", "都市部からの移住者を過度に優遇したため、元からの住民が全員流出してしまった。"),
                ("D", "自然環境の保護を最優先にしすぎた結果、産業開発が全く行われなかった。")
            ],
            "A",
            "Đoạn 1 nêu rõ: trước đây chủ yếu dựa vào thu hút nhà máy và phát triển du lịch quy mô lớn phụ thuộc vốn ngoài, các phương thức này '景気の変動に弱く、持続的な地域社会の自立には結びつきにくかった' (yếu ớt trước biến động kinh tế và khó dẫn tới sự tự lập bền vững). Đáp án A đúng.",
            {
                "B": "Việc khám phá giá trị nhà cổ và đặc sản là xu hướng tích cực mới đây của người di cư, không phải lỗi của chính sách cũ.",
                "C": "Văn bản không hề nói cư dân cũ bỏ đi hết vì ưu đãi người mới.",
                "D": "Chính sách cũ tập trung vào phát triển kinh tế quy mô lớn chứ không phải bảo vệ môi trường quá đà."
            }
        ),
        (
            "N2_03_M11_05",
            "N2-RE-MED",
            "Mondai 11: 中文読解",
            "都市部から地方への移住者が地域にもたらしている変化として、適切なものはどれか。",
            p11_2,
            [
                ("A", "都市部の大企業を誘致して、巨大な工場団地を次々と建設している。"),
                ("B", "古民家カフェや特産品ビジネスを通じ、見落とされていた地域の潜在的価値を再発見している。"),
                ("C", "地域の伝統行事や昔からのルールをすべて廃止し、都市型の生活様式を強制している。"),
                ("D", "物質的な豊かさのみを追い求め、利便性の高い高層マンションを建設している。")
            ],
            "B",
            "Đoạn 2 nêu: người di cư mở quán cafe tận dụng nhà cổ, kinh doanh đặc sản địa phương, '従来の住民には見落とされていた地域の潜在的価値を再発見し、新たな活力を吹き込んでいる' (tái phát hiện giá trị tiềm năng vốn bị cư dân cũ bỏ quên và thổi luồng sinh khí mới). Đáp án B đúng.",
            {
                "A": "Người di cư phát triển quy mô nhỏ hữu cơ, không phải xây khu công nghiệp lớn.",
                "C": "Tác giả cảnh báo không được coi nhẹ quy tắc truyền thống, người di cư không hề ép buộc xóa bỏ truyền thống.",
                "D": "Người di cư tìm kiếm môi trường nuôi dạy con gần gũi thiên nhiên và quan hệ gắn bó, không phải tìm sự phồn vinh vật chất hay nhà cao tầng."
            }
        ),
        (
            "N2_03_M11_06",
            "N2-RE-MED",
            "Mondai 11: 中文読解",
            "新しい地域共同体を育むために、最も重要だと述べられていることは何か。",
            p11_2,
            [
                ("A", "新参者の意見だけを全面的に採用し、古くからの伝統はすべて過去のものとして捨てること。"),
                ("B", "外部からの移住を制限し、昔から住んでいる住民だけの閉じた関係を維持すること。"),
                ("C", "新旧の住民が互いを尊重し、伝統を守りつつも対話を重ねて歩み寄ること。"),
                ("D", "国の補助金に頼り切って、住民同士の直接的なコミュニケーションを減らすこと。")
            ],
            "C",
            "Đoạn cuối khẳng định: điều cốt yếu là sự tôn trọng lẫn nhau giữa cư dân mới và cũ, vừa đón nhận ý tưởng mới vừa không coi nhẹ truyền thống và quy tắc cộng đồng, đôi bên nhượng bộ và đối thoại xuyên thế hệ. Đáp án C đúng.",
            {
                "A": "Văn bản nhấn mạnh không được coi nhẹ truyền thống lâu đời.",
                "B": "Tác giả coi cộng đồng cởi mở với người di cư là động lực phát triển mới.",
                "D": "Tác giả đề cao sự tự lập và gắn kết người với người, phê phán phụ thuộc bên ngoài."
            }
        ),

        # Passage 3 Questions
        (
            "N2_03_M11_07",
            "N2-RE-MED",
            "Mondai 11: 中文読解",
            "手書きでノートを取る行為が記憶や理解を促進する理由として、筆者が挙げているのはどれか。",
            p11_3,
            [
                ("A", "キーボードよりも速くタイピングできるため、一言一句漏らさず正確に記録できるから。"),
                ("B", "パソコンの画面を見つめ続けることによる視覚的な疲労を完全に防げるから。"),
                ("C", "文字の美しさばかりに意識が向くため、他の余計な雑念を排除できるから。"),
                ("D", "話された内容を頭の中で自然と要約し、自分の言葉に咀嚼して配置する処理が行われるから。")
            ],
            "D",
            "Đoạn 2 giải thích: vì viết tay không thể chép kịp từng từ một như gõ máy, nên não bộ buộc phải tự động tóm tắt thông tin nghe được, nghiền ngẫm bằng ngôn từ của mình rồi mới sắp xếp lên giấy -> kích thích xử lý thông tin mức độ cao. Đáp án D đúng.",
            {
                "A": "Viết tay chậm hơn gõ máy và không thể chép từng từ một, chính sự giới hạn này buộc não phải tư duy tóm tắt.",
                "B": "Lý do tác giả đưa ra là kích thích chức năng vận động và tóm tắt thông tin của não, không bàn về mỏi mắt nhìn màn hình.",
                "C": "Tập trung nắn nót chữ đẹp không phải là lý do tăng cường hiểu khái niệm."
            }
        ),
        (
            "N2_03_M11_08",
            "N2-RE-MED",
            "Mondai 11: 中文読解",
            "手書きの文字が受け手に温もりを与える理由として、本文で述べられていることはどれか。",
            p11_3,
            [
                ("A", "書き手の感情や呼吸、迷いといった身体性の痕跡がそのまま文字に宿るから。"),
                ("B", "活字メールよりもインクの匂いや紙の質感が高級感を漂わせるから。"),
                ("C", "手紙は郵送に日数がかかるため、待つ時間の長さが相手への愛着を高めるから。"),
                ("D", "手書きの手紙には一切の誤字や脱字が含まれないという信頼感があるから。")
            ],
            "A",
            "Đoạn 3 nêu: chữ viết tay khắc ghi những dấu vết thể tính thực tế của người viết như cảm xúc, nhịp thở, sự phân vân lúc đó; người nhận cảm thấy hơi ấm chính vì sự hiện diện sống động của người viết gửi gắm vào đó. Đáp án A đúng.",
            {
                "B": "Tác giả bàn về dấu vết cảm xúc con người gửi vào nét chữ, không nói về chất lượng giấy mực cao cấp.",
                "C": "Văn bản không giải thích hơi ấm qua việc thời gian gửi thư lâu.",
                "D": "Chữ viết tay thường dễ có vết xóa hay sửa, điều đó thể hiện tính chân thật chứ không phải không có lỗi."
            }
        ),
        (
            "N2_03_M11_09",
            "N2-RE-MED",
            "Mondai 11: 中文読解",
            "この文章全体を通じて、筆者が読者に伝えたかった主張は何か。",
            p11_3,
            [
                ("A", "デジタル端末での文字入力を一切やめ、すべてのビジネス業務を手書きに戻すべきだ。"),
                ("B", "効率と即時性が優先される今こそ、思考を深め心を込める手書きの価値を再評価すべきだ。"),
                ("C", "キーボードのタイピング速度を上げることこそが、現代人の知的能力を高める唯一の道だ。"),
                ("D", "手紙を書く習慣が廃れた原因は、若者の国語力低下にあるため学校教育を改革すべきだ。")
            ],
            "B",
            "Câu cuối kết luận toàn bài: chính trong xã hội số coi trọng tính tức thì và hiệu suất, đây là lúc chúng ta cần dừng chân suy ngẫm sâu sắc và đánh giá lại giá trị của việc viết tay dồn cả tâm trí. Đáp án B đúng.",
            {
                "A": "Tác giả thừa nhận lợi ích to lớn của công nghệ số, không cực đoan bắt bỏ hết.",
                "C": "Trái ngược hoàn toàn với luận điểm đề cao tư duy sâu của viết tay.",
                "D": "Văn bản không đổ lỗi cho giới trẻ hay bàn về cải cách giáo dục."
            }
        ),
    ]

    for qid, tid, cat, stem, pass_text, opts, ans, exp, dist in m11_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Reading",
            "category": cat,
            "stem": stem,
            "contextPassage": pass_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "stimulusType": "reading_passage"
        })

    # =========================================================================
    # MONDAI 12: 統合理解 (Comparative / Integrated Reading - 2 items)
    # =========================================================================
    p12_combined = """【A：経営コンサルタントの論考】
社内ビジネスチャットツールの導入は、企業の意思決定スピードを劇的に加速させる。かつてのように形式的なメールの挨拶文を作成したり、日程調整のためだけに会議を開いたりする無駄が省かれ、案件ごとの迅速な情報共有と即時レスポンスが可能となるからだ。チャット上でのオープンなやり取りは組織内の風通しを良くし、部署の垣根を越えたコラボレーションを活性化させる。現代の激変する市場環境を勝ち抜くためには、全社員が常に繋がるリアルタイムなコミュニケーション基盤の構築こそが、競争優位の源泉となるのである。

【B：労働心理学者の論考】
ビジネスチャットの常時接続がもたらす弊害について、私たちはもっと警戒的であるべきだ。メッセージが届けば数分以内の返信を期待されるという無言の社会的圧力は、労働者に絶え間ない緊張感と認知的断片化を強いる。何時間も没頭して思索を深める「ディープワーク」の時間は奪われ、思考は常に浅い即応性に終始してしまう。さらに、退勤後や休日にも通知が届く環境は、心身の回復に不可欠な心理的デタッチメント（仕事からの心理的隔離）を著しく阻害する。真に創造的な成果を求めるならば、あえて「即レス」を求めず、オフラインで集中できる時間を制度として保障することこそが急務である。"""

    m12_raw = [
        (
            "N2_03_M12_01",
            "N2-RE-INTEG",
            "Mondai 12: 統合理解",
            "ビジネスチャットツールがもたらす影響について、AとBはそれぞれどのように捉えているか。",
            p12_combined,
            [
                ("A", "AもBも、組織の意思決定スピードを遅らせる原因になると批判している。"),
                ("B", "AもBも、社員のメンタルヘルスを向上させる決定打になると評価している。"),
                ("C", "Aは情報共有の迅速化と競争力強化を評価し、Bは思考の断片化や休養阻害の弊害を懸念している。"),
                ("D", "Aは社外秘情報の漏洩リスクを警告し、Bは部署間のコミュニケーション活性化を称賛している。")
            ],
            "C",
            "Tác giả A coi chat nội bộ là công cụ đẩy nhanh tốc độ chia sẻ thông tin, tăng sức cạnh tranh. Ngược lại, tác giả B lo ngại việc kết nối liên tục gây phân mảnh tư duy, triệt tiêu thời gian suy nghĩ sâu sắc và ngăn cản sự hồi phục tâm lý khi nghỉ ngơi. Đáp án C tóm tắt hoàn toàn chính xác.",
            {
                "A": "A ca ngợi đẩy nhanh tốc độ, chỉ có B nêu mặt trái.",
                "B": "B chỉ trích việc gây căng thẳng tinh thần, không hề ca ngợi nâng cao sức khỏe tâm thần.",
                "D": "A không bàn về rò rỉ bảo mật, B cũng không khen ngợi việc này."
            }
        ),
        (
            "N2_03_M12_02",
            "N2-RE-INTEG",
            "Mondai 12: 統合理解",
            "「即時レスポンス（即座の返信）」に対する両者の姿勢の違いとして、最も適切なものはどれか。",
            p12_combined,
            [
                ("A", "Aは即レスを避けるべきだとし、Bは全社員に24時間即レスを義務付けるべきだと主張している。"),
                ("B", "Aは休日の即レスだけを禁止すべきとし、Bは勤務時間中のみ即レスを徹底すべきだとしている。"),
                ("C", "Aは対面での会話を最優先すべきとし、Bはメールのみを正式な連絡手段と認めるべきだとしている。"),
                ("D", "Aは即応性が競争優位を生むと肯定的に捉え、Bは即レスを求めずオフラインで集中する時間を保障すべきと主張している。")
            ],
            "D",
            "A coi phản hồi tức thì (即時レスポンス) là cội nguồn của ưu thế cạnh tranh thị trường. B yêu cầu các tổ chức phải đảm bảo cơ chế không bắt người lao động phải 'trả lời ngay' để có thời gian làm việc tập trung sâu và nghỉ ngơi thực thụ. Đáp án D phản ánh chuẩn xác.",
            {
                "A": "Trái ngược hoàn toàn: A ủng hộ phản hồi nhanh, B phản đối áp lực phải trả lời ngay.",
                "B": "A không cấm ngày nghỉ, B cũng không đòi hỏi triệt để trả lời ngay trong giờ làm.",
                "C": "Cả hai đều bàn về công cụ chat số, không ai đòi quay lại chỉ dùng gặp mặt hay chỉ dùng email."
            }
        ),
    ]

    for qid, tid, cat, stem, pass_text, opts, ans, exp, dist in m12_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Reading",
            "category": cat,
            "stem": stem,
            "contextPassage": pass_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "stimulusType": "reading_passage"
        })

    # =========================================================================
    # MONDAI 13: 長文読解 (Thematic Long Reading - 3 items)
    # =========================================================================
    p13_text = """現代社会を特徴づける最も顕著な現象の一つは、「時間の効率化」に対する過剰な執着である。タイパ（タイムパフォーマンス）という言葉が広く浸透したことからも窺えるように、私たちは動画を倍速で視聴し、音楽をイントロや間奏を飛ばしてサビだけを聴き、本を読む代わりに要約アプリで要点だけを効率的に摂取しようとする。あらゆる無駄を削ぎ落とし、最短時間で最大の効果を得ることこそが、合理的で賢い生き方であるかのように喧伝されているのだ。

しかし、立ち止まって考えてみれば、私たちが切り捨てようとしている「無駄」の中にこそ、人間的な営みの豊かさが宿っていたのではないだろうか。たとえば、音楽における長い前奏や静寂は、次に訪れる主旋律への期待感を高め、感情の振幅を広げるために周到に配置された表現の一部である。物語の冗長に見える寄り道描写は、登場人物の生きてきた風土や生活の匂いを読者に追体験させるために不可欠な装置であったはずだ。それらを「要点ではない」と切り落として骨組みだけを取り出したとき、私たちが受け取っているのは単なる抽象的な情報であって、もはや心を揺さぶる「芸術」や「物語」ではない。

効率化の強迫観念は、個人の内省的な時間すらも侵食している。少しでも何もしない空白の時間が生じると、私たちは焦燥感に駆られてスマートフォンを手に取り、情報の濁流に身を委ねてしまう。しかし、退屈や沈黙と向き合い、あてもなく物思いに耽る「ゆとりの時間」こそが、自分自身の内面を見つめ直し、独自の思想や価値観を醸成するために不可欠なプロセスである。外部からの刺激を遮断し、思考をじっくりと熟成させる時間を持てない人間は、他者の意見や世間の流行に流されやすい脆さを抱えることになる。

効率を追求すること自体を否定するつもりはない。科学技術の進歩や社会システムの合理化は、私たちの生活を物理的に豊かで安全なものにしてくれた。しかし、効率化はあくまでも人生を豊かに生きるための「手段」であって、「目的」そのものではないはずだ。最短距離で駆け抜けることばかりに気を取られ、道端に咲く花の色や足元の土の感触に気づけない旅に、果たしてどれほどの意味があるだろうか。合理性の檻から一歩踏み出し、あえて「無駄」や「非効率」に身を浸す勇気を持つことこそが、私たちが人間らしさを取り戻すための第一歩なのである。"""

    m13_raw = [
        (
            "N2_03_M13_01",
            "N2-RE-LONG",
            "Mondai 13: 長文読解",
            "現代における「倍速視聴」や「要約の摂取」について、筆者はどのように考えているか。",
            p13_text,
            [
                ("A", "要点だけを取り出すことで、心を揺さぶる表現の豊かさや本来の価値を失っている。"),
                ("B", "情報過多の時代を生き抜くために、すべての人が身につけるべき合理的で優れた手法である。"),
                ("C", "芸術作品を鑑賞するための時間を節約し、より多くの作品に出会える画期的な進化である。"),
                ("D", "若者の知的能力を著しく高め、論理的思考力を養うために最適な学習法である。")
            ],
            "A",
            "Đoạn 2 nêu rõ: những thứ bị gọt giũa coi là 'thừa thãi' thực chất là phần cấu thành quan trọng tạo nên rung động cảm xúc của nghệ thuật. Khi chỉ lọc lấy khung xương cốt lõi, thứ chúng ta nhận được chỉ là thông tin trừu tượng chứ không còn là nghệ thuật hay câu chuyện lay động lòng người nữa. Đáp án A đúng.",
            {
                "B": "Tác giả phê phán xu hướng này là thái độ ám ảnh thái quá, không hề khen ngợi đó là cách sống sáng suốt.",
                "C": "Tác giả chỉ ra rằng việc này phá hủy giá trị trải nghiệm nghệ thuật chứ không phải sự tiến hóa tốt đẹp.",
                "D": "Văn bản không hề coi đây là phương pháp rèn luyện tư duy logic tối ưu."
            }
        ),
        (
            "N2_03_M13_02",
            "N2-RE-LONG",
            "Mondai 13: 長文読解",
            "空白の時間にスマートフォンを手にしてしまう現代人について、筆者はどのような懸念を示しているか。",
            p13_text,
            [
                ("A", "スマートフォンの通信料金が高騰し、家計を圧迫すること。"),
                ("B", "沈黙や退屈と向き合って思考を熟成させることができず、世間の意見に流されやすくなること。"),
                ("C", "視力の低下や睡眠障害を引き起こし、身体の健康を損なうこと。"),
                ("D", "情報処理速度が速くなりすぎて、他者との日常的な会話がかみ合わなくなること。")
            ],
            "B",
            "Đoạn 3 giải thích: việc không thể đối diện với sự tĩnh lặng, buồn chán để nghiền ngẫm tư duy nội tâm khiến con người không thể nuôi dưỡng hệ giá trị riêng, dẫn đến sự yếu ớt, dễ bị cuốn theo trào lưu và ý kiến của số đông. Đáp án B đúng.",
            {
                "A": "Văn bản không bàn về cước viễn thông hay kinh tế gia đình.",
                "C": "Văn bản tập trung vào chiều sâu tư duy và tâm lý, không bàn về thị lực hay mất ngủ.",
                "D": "Không có ý nào nói về việc xử lý thông tin quá nhanh làm lệch pha hội thoại."
            }
        ),
        (
            "N2_03_M13_03",
            "N2-RE-LONG",
            "Mondai 13: 長文読解",
            "筆者がこの文章で最も強く主張している結論はどれか。",
            p13_text,
            [
                ("A", "現代の科学技術や社会システムを全否定し、原始的な自給自足の生活に戻るべきだ。"),
                ("B", "効率化を人生の自己目的とせず、あえて無駄や非効率な時間を受け入れる勇気を持つべきだ。"),
                ("C", "あらゆる娯楽や芸術を排除し、最短距離で社会的成功を収めることに集中すべきだ。"),
                ("D", "他者の意見を完全に無視し、自分の直感だけを信じて生きるべきだ。")
            ],
            "B",
            "Đoạn cuối đúc kết: hiệu quả chỉ là phương tiện chứ không phải mục đích sống; cần bước ra khỏi chiếc lồng duy lý và dũng cảm đón nhận những khoảng thời gian 'vô dụng, phi hiệu quả' để tìm lại nhân tính thực sự. Đáp án B đúng.",
            {
                "A": "Tác giả nói rõ '効率を追求すること自体を否定するつもりはない' (không có ý phủ định sự tiến bộ của khoa học công nghệ), không hề bảo quay về thời nguyên thủy.",
                "C": "Trái ngược hoàn toàn với quan điểm phê phán ám ảnh hiệu suất.",
                "D": "Văn bản không khuyên bài xích người khác mà khuyên xây dựng chiều sâu nội tâm."
            }
        ),
    ]

    for qid, tid, cat, stem, pass_text, opts, ans, exp, dist in m13_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Reading",
            "category": cat,
            "stem": stem,
            "contextPassage": pass_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "stimulusType": "reading_passage"
        })

    # =========================================================================
    # MONDAI 14: 情報検索 (Information Retrieval - 2 items)
    # =========================================================================
    p14_guide = """【緑が丘市民センター 施設利用・予約案内】

当センターの会議室・多目的ホールをご利用の際は、以下の利用規約をご確認ください。

1. 開館時間および区分
・午前区分：09:00〜12:00
・午後区分：13:00〜17:00
・夜間区分：18:00〜21:30
※各区分の間の時間（12:00〜13:00、17:00〜18:00）は清掃・換気時間のため入室できません。

2. 施設および利用料金（1区分あたり）
・第1会議室（定員20名）：1,500円
・第2会議室（定員40名）：2,800円
・視聴覚室（定員30名・音響プロジェクター完備）：3,500円
・多目的ホール（定員150名・ステージ付き）：8,000円
※営利目的（商品の販売、有料セミナー等）での利用は、上記料金の2倍となります。
※市内在住・在勤者で構成される非営利団体は、上記料金の30%割引が適用されます。

3. 予約受付期間
・市内登録団体：利用日の3か月前の初日より受付開始
・一般・市外利用者：利用日の1か月前の初日より受付開始

4. キャンセル規定および返金率
・利用日の14日前までのキャンセル：利用料金の全額（100%）返金
・利用日の3日前までのキャンセル：利用料金の半額（50%）返金
・利用日の前日および当日のキャンセル：返金不可（0%）
※天災地変等の不可抗力により施設が休館した場合は、期日に関わらず全額返金します。"""

    m14_raw = [
        (
            "N2_03_M14_01",
            "N2-RE-INFO",
            "Mondai 14: 情報検索",
            "市内在住のメンバーで構成される非営利の読書サークル（会員15名）が、第1会議室を土曜日の午前区分に利用する場合、利用料金はいくらになるか。",
            p14_guide,
            [
                ("A", "1,500円"),
                ("B", "3,000円"),
                ("C", "2,800円"),
                ("D", "1,050円")
            ],
            "D",
            "第1会議室 (đủ cho 15 người) có giá tiêu chuẩn 1区分 là 1,500円. Mục 2 nêu: '市内在住・在勤者で構成される非営利団体は、上記料金の30%割引が適用されます' (Đoàn thể phi lợi nhuận gồm người trong thành phố được giảm giá 30%). Giá sau giảm: 1,500 x (1 - 0.3) = 1,050円. Đáp án D đúng.",
            {
                "A": "1,500円 là giá gốc khi chưa áp dụng ưu đãi giảm 30% cho đoàn thể phi lợi nhuận trong thành phố.",
                "B": "3,000円 là giá khi nhân đôi cho mục đích sinh lợi/thương mại.",
                "C": "2,800円 là giá của 第2会議室."
            }
        ),
        (
            "N2_03_M14_02",
            "N2-RE-INFO",
            "Mondai 14: 情報検索",
            "施設の予約およびキャンセルに関して、案内規約と一致しているものはどれか。",
            p14_guide,
            [
                ("A", "利用日の10日前に予約をキャンセルした場合、利用料金の半額（50%）が返金される。"),
                ("B", "市外に在住する一般利用者は、利用日の3か月前から予約を申し込むことができる。"),
                ("C", "午前の区分を利用した後、そのまま12:00〜13:00の間も会議室に残って飲食できる。"),
                ("D", "有料セミナーを開催する営利利用であっても、非営利団体と同じ通常料金で利用できる。")
            ],
            "A",
            "Mục 4 quy định hủy: 14日前まで hoàn 100%, 3日前まで hoàn 50%. Khi hủy vào 10 ngày trước ngày dùng (nằm trong khoảng từ sau 14 ngày đến trước 3 ngày) sẽ được hoàn 50%. Đáp án A hoàn toàn đúng.",
            {
                "B": "Người ngoài thành phố / đại chúng chỉ được đăng ký từ 1 tháng trước (利用日の1か月前の初日より), chỉ đoàn thể trong thành phố mới được từ 3 tháng trước.",
                "C": "Mục 1 ghi rõ: thời gian chuyển giao giữa các ca (12:00〜13:00) là để vệ sinh thông gió nên không được ở trong phòng ('入室できません').",
                "D": "Mục 2 ghi rõ: mục đích thương mại/sinh lợi phải trả gấp đôi mức phí thông thường ('上記料金の2倍')."
            }
        ),
    ]

    for qid, tid, cat, stem, pass_text, opts, ans, exp, dist in m14_raw:
        items.append({
            "id": qid,
            "typeId": tid,
            "skill": "Reading",
            "category": cat,
            "stem": stem,
            "contextPassage": pass_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "stimulusType": "reading_passage"
        })

    return items
