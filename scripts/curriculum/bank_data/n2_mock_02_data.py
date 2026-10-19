# -*- coding: utf-8 -*-
"""
JLPT N2 Mock Exam #02 - Section 1: Language Knowledge & Reading (言語知識・読解)
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

def get_n2_mock_02_sec1_items():
    items = []

    # =========================================================================
    # MONDAI 1: 漢字読み (Kanji Reading - 5 items)
    # =========================================================================
    m1_raw = [
        (
            "N2_02_M1_01",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "新工場の建設予定地を慎重に【選定】した。",
            "せんてい",
            [("A", "せんじょう"), ("B", "せんてい"), ("C", "ぜんてい"), ("D", "せんちょう")],
            "B",
            "選定（せんてい - TUYỂN ĐỊNH）: Tuyển chọn, thẩm định và đưa ra quyết định chọn lựa. Chữ 選 có âm on là せん, chữ 定 có âm on là てい (hoặc じょう).",
            {
                "A": "せんじょう: Nhầm âm てい thành じょう (như trong 勘定 かんじょう).",
                "C": "ぜんてい: Nhầm âm せん thành ぜん (dễ lẫn với 前提 ぜんてい).",
                "D": "せんちょう: Nhầm âm đuôi てい thành ちょう."
            }
        ),
        (
            "N2_02_M1_02",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "予期せぬトラブルにも【冷静】に対処することが求められる。",
            "れいせい",
            [("A", "れいぜい"), ("B", "りょうせい"), ("C", "れいせい"), ("D", "れんせい")],
            "C",
            "冷静（れいせい - LÃNH TĨNH）: Điềm tĩnh, bình tĩnh. Chữ 冷 có âm on là れい, chữ 静 có âm on là せい.",
            {
                "A": "れいぜい: Sai biến âm đục ぜい ở chữ 静.",
                "B": "りょうせい: Nhầm âm れい thành りょう (như trong 両性 りょうせい).",
                "D": "れんせい: Nhầm âm れい thành れん (dễ nhầm với 連盟 れんめい)."
            }
        ),
        (
            "N2_02_M1_03",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "旧態依然とした組織体制を根本から【刷新】する。",
            "さっしん",
            [("A", "さつしん"), ("B", "さっしん"), ("C", "さくしん"), ("D", "ざっしん")],
            "B",
            "刷新（さっしん - XOÁT TÂN）: Đổi mới hoàn toàn, cải cách triệt để. Chữ 刷 (さつ) gặp chữ 新 (しん) phát sinh âm ngắt thành さっしん.",
            {
                "A": "さつしん: Không biến âm ngắt âm つ đứng trước しん.",
                "C": "さくしん: Nhầm âm on của 刷 (さつ) thành さく.",
                "D": "ざっしん: Sai biến âm đục ざ ở đầu từ."
            }
        ),
        (
            "N2_02_M1_04",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "法律の解釈をめぐって両者の意見が激しく【対立】した。",
            "たいりつ",
            [("A", "たいりつ"), ("B", "ついりつ"), ("C", "たいりゅう"), ("D", "だいりつ")],
            "A",
            "対立（たいりつ - ĐỐI LẬP）: Đối đầu, đối lập quan điểm. Chữ 対 có âm たい, chữ 立 có âm りつ.",
            {
                "B": "ついりつ: Nhầm âm on たい thành つい (như trong 対 つがい).",
                "C": "たいりゅう: Nhầm lẫn với 滞留 (たいりゅう - ứ đọng, đọng lại).",
                "D": "だいりつ: Sai biến âm đục だ ở chữ 対."
            }
        ),
        (
            "N2_02_M1_05",
            "N2-MO-READ",
            "Mondai 1: 漢字読み",
            "長年にわたる過酷な環境が金属パイプを【腐食】させた。",
            "ふしょく",
            [("A", "ふじき"), ("B", "ふじょく"), ("C", "ぶしょく"), ("D", "ふしょく")],
            "D",
            "腐食（ふしょく - HỦ THỰC）: Ăn mòn hóa học, rỉ sét, mục ruỗng. Chữ 腐 có âm ふ, chữ 食 có âm しょく.",
            {
                "A": "ふじき: Nhầm âm しょく thành じき.",
                "B": "ふじょく: Nhầm lẫn với 侮辱 (ぶじょく - sỉ nhục, lăng mạ).",
                "C": "ぶしょく: Sai âm đầu ふ thành ぶ."
            }
        )
    ]

    for qid, type_id, mtitle, stem, target, opts, ans, exp, dist in m1_raw:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Vocabulary",
            "typeId": type_id,
            "mondaiTitle": mtitle,
            "stem": stem,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 2,
            "status": "QA_VERIFIED"
        })

    # =========================================================================
    # MONDAI 2: 表記 (Orthography - 5 items)
    # =========================================================================
    m2_raw = [
        (
            "N2_02_M2_01",
            "N2-MO-ORTH",
            "Mondai 2: 表記",
            "海外進出に向けた事業計画を【けんとう】する。",
            "検討",
            [("A", "見当"), ("B", "検当"), ("C", "検討"), ("D", "検踏")],
            "C",
            "検討（けんとう - KIỂM THẢO）: Cân nhắc, xem xét, nghiên cứu phương án. Cụm từ cố định: 計画を検討する.",
            {
                "A": "見当（けんとう - KIẾN ĐƯƠNG）: Ước lượng, phỏng đoán phương hướng (見当がつく).",
                "B": "検当: Sai chữ Hán 當/当 ghép với 検.",
                "D": "検踏: Không tồn tại từ này trong tiếng Nhật hiện đại."
            }
        ),
        (
            "N2_02_M2_02",
            "N2-MO-ORTH",
            "Mondai 2: 表記",
            "長時間の交渉の末、ついに双方の合意に【たっした】。",
            "達した",
            [("A", "達した"), ("B", "建した"), ("C", "通した"), ("D", "到した")],
            "A",
            "達した（たっした - ĐẠT）: Đạt tới, đạt được (thỏa thuận, số lượng). Động từ 達する（たっする）.",
            {
                "B": "建した: Sai bộ thủ, 建 là KIẾN (xây dựng: 建てる たてる).",
                "C": "通した: 通 là THÔNG (thông qua: 通す とおす), phát âm khác.",
                "D": "到した: 到 là ĐÁO (đến: 到達 とうたつ hoặc 至る いたる), không đọc là たっした đơn lẻ."
            }
        ),
        (
            "N2_02_M2_03",
            "N2-MO-ORTH",
            "Mondai 2: 表記",
            "この制度は社会的な【かくさ】の是正を目指している。",
            "格差",
            [("A", "階差"), ("B", "格差"), ("C", "確差"), ("D", "隔差")],
            "B",
            "格差（かくさ - CÁCH SAI）: Chênh lệch, khoảng cách giàu nghèo/xã hội. Ví dụ: 貧富の格差 (khoảng cách giàu nghèo).",
            {
                "A": "階差（かいさ - GIAI SAI）: Dùng trong toán học (cấp số, hiệu số), không chỉ chênh lệch xã hội.",
                "C": "確差: Không tồn tại chữ này trong từ vựng N2.",
                "D": "隔差: Sai chữ 格 thành 隔 (cách biệt: 隔てる へだてる)."
            }
        ),
        (
            "N2_02_M2_04",
            "N2-MO-ORTH",
            "Mondai 2: 表記",
            "突然の停電に備えて非常用電源を【かくほ】する。",
            "確保",
            [("A", "確歩"), ("B", "獲保"), ("C", "確保"), ("D", "確補")],
            "C",
            "確保（かくほ - XÁC BẢO）: Đảm bảo, giữ vững (nguồn điện, chỗ ngồi, ngân sách).",
            {
                "A": "確歩: Không tồn tại từ ghép này trong tiếng Nhật.",
                "B": "獲保: Nhầm chữ 確 (XÁC) thành 獲 (HOẠCH - săn bắt/thu hoạch).",
                "D": "確補: Nhầm chữ 保 (BẢO - giữ gìn) thành 補 (BỔ - bổ sung)."
            }
        ),
        (
            "N2_02_M2_05",
            "N2-MO-ORTH",
            "Mondai 2: 表記",
            "彼の迅速な対応が会社の信頼を【かいふく】させた。",
            "回復",
            [("A", "回服"), ("B", "快復"), ("C", "改復"), ("D", "回復")],
            "D",
            "回復（かいふく - HỒI PHỤC）: Phục hồi, khôi phục lại (tin cậy, kinh tế, sức khỏe nói chung). Chú ý 快復 chỉ chuyên dùng cho khỏi ốm nặng.",
            {
                "A": "回服: Nhầm chữ 復 (PHỤC - quay lại) thành 服 (PHỤC - quần áo/uống thuốc).",
                "B": "快復: Chỉ dùng chuyên biệt cho lời chúc khỏi bệnh của cá nhân (全快), không dùng cho khôi phục niềm tin công ty.",
                "C": "改復: Không có từ này."
            }
        )
    ]

    for qid, type_id, mtitle, stem, target, opts, ans, exp, dist in m2_raw:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Vocabulary",
            "typeId": type_id,
            "mondaiTitle": mtitle,
            "stem": stem,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 2,
            "status": "QA_VERIFIED"
        })

    # =========================================================================
    # MONDAI 3: 語形成 (Word Formation - 5 items)
    # =========================================================================
    m3_raw = [
        (
            "N2_02_M3_01",
            "N2-MO-WORD",
            "Mondai 3: 語形成",
            "彼女の演技には（　　）現実的な迫力がある。",
            "非",
            [("A", "無"), ("B", "不"), ("C", "非"), ("D", "未")],
            "C",
            "非現実的（ひげんじつてき - PHI HIỆN THỰC ĐÍCH）: Phi thực tế, không có thật. Tiền tố 非 thường đi với các danh từ trừu tượng (非公式, 非常識, 非日常).",
            {
                "A": "無: Thường đi với danh từ chỉ sự sở hữu hoặc tồn tại cụ thể (無意味, 無責任, 無制限).",
                "B": "不: Thường đi với tính từ hoặc trạng thái đối lập tính chất (不可能, 不自然, 不公平).",
                "D": "未: Chỉ hành động hoặc giai đoạn chưa xảy ra (未解決, 未完成, 未経験)."
            }
        ),
        (
            "N2_02_M3_02",
            "N2-MO-WORD",
            "Mondai 3: 語形成",
            "本日のセミナーは（　　）会員の方でも自由にご参加いただけます。",
            "非",
            [("A", "未"), ("B", "非"), ("C", "不"), ("D", "無")],
            "B",
            "非会員（ひかいいん - PHI HỘI VIÊN）: Người không phải là hội viên. Tiền tố 非 dùng để chỉ tư cách đối lập với một tổ chức/thành phần xã hội.",
            {
                "A": "未: Chỉ người chưa trở thành (ví dụ 未成年 - vị thành niên), không dùng 未会員.",
                "C": "不: Không dùng cho tư cách thành viên.",
                "D": "無: Không kết hợp thành từ chuẩn trong văn phong hành chính này."
            }
        ),
        (
            "N2_02_M3_03",
            "N2-MO-WORD",
            "Mondai 3: 語形成",
            "地球温暖化を防ぐため、省エネルギー（　　）の家電が推奨されている。",
            "型",
            [("A", "風"), ("B", "式"), ("C", "製"), ("D", "型")],
            "D",
            "省エネルギー型（しょうエネルギーがた - TỈNH HÌNH）: Kiểu mẫu / chủng loại tiết kiệm năng lượng. Hậu tố 型 chỉ chủng loại, mẫu mã kỹ thuật mang đặc tính nhất định.",
            {
                "A": "風（ふう）: Mang phong cách, hơi hướng nghệ thuật/thời trang (和風, 西洋風).",
                "B": "式（しき）: Cơ chế, phương thức vận hành hệ thống (日本式, 組み立て式).",
                "C": "製（せい）: Nơi sản xuất hoặc chất liệu (日本製, プラスチック製)."
            }
        ),
        (
            "N2_02_M3_04",
            "N2-MO-WORD",
            "Mondai 3: 語形成",
            "今期の営業利益は、当初の予想を（　　）回る見込みだ。",
            "上",
            [("A", "高"), ("B", "上"), ("C", "大"), ("D", "優")],
            "B",
            "上回る（うわまわる - THƯỢNG HỒI）: Vượt quá con số dự toán, cao hơn mức kỳ vọng. Trái nghĩa là 下回る（したまわる）.",
            {
                "A": "高回る: Không tồn tại động từ này trong tiếng Nhật.",
                "C": "大回る: 大回（おおまわ）り là danh từ chỉ đi đường vòng, không mang nghĩa vượt mức dự kiến.",
                "D": "優回る: Không tồn tại trong ngữ pháp cấu tạo từ tiếng Nhật."
            }
        ),
        (
            "N2_02_M3_05",
            "N2-MO-WORD",
            "Mondai 3: 語形成",
            "あの地域は長年にわたり、（　　）開発の自然がそのまま残されている。",
            "未",
            [("A", "無"), ("B", "非"), ("C", "未"), ("D", "不")],
            "C",
            "未開発（みかいはつ - VỊ KHAI PHÁT）: Chưa được khai phá, chưa được phát triển. Tiền tố 未 nhấn mạnh trạng thái còn nguyên sơ chưa bị tác động.",
            {
                "A": "無開発: Không phải là thuật ngữ tự nhiên.",
                "B": "非開発: Không dùng tiền tố 非 với 開発.",
                "D": "不開発: Không kết hợp với từ này."
            }
        )
    ]

    for qid, type_id, mtitle, stem, target, opts, ans, exp, dist in m3_raw:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Vocabulary",
            "typeId": type_id,
            "mondaiTitle": mtitle,
            "stem": stem,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 2,
            "status": "QA_VERIFIED"
        })

    # =========================================================================
    # MONDAI 4: 文脈規定 (Contextual Expressions - 7 items)
    # =========================================================================
    m4_raw = [
        (
            "N2_02_M4_01",
            "N2-MO-CONT",
            "Mondai 4: 文脈規定",
            "長時間のパソコン作業で目が（　　）して痛むので、目薬をさした。",
            "しょぼしょぼ",
            [("A", "さらさら"), ("B", "しょぼしょぼ"), ("C", "すらすら"), ("D", "ぞくぞく")],
            "B",
            "しょぼしょぼ: (Mắt) cay xè, mỏi mệt chớp liên tục không mở to được do thiếu ngủ hoặc nhìn màn hình vi tính lâu.",
            {
                "A": "さらさら: Mượt mà, róc rách (tóc mượt, suối chảy).",
                "C": "すらすら: Trôi chảy, vanh vách (trả lời trôi chảy, đọc vanh vách).",
                "D": "ぞくぞく: Run rẩy vì sốt rét hoặc rùng mình hồi hộp."
            }
        ),
        (
            "N2_02_M4_02",
            "N2-MO-CONT",
            "Mondai 4: 文脈規定",
            "新製品の発売日を延期することは、経営上（　　）の決断だった。",
            "苦渋",
            [("A", "苦情"), ("B", "苦痛"), ("C", "苦渋"), ("D", "苦境")],
            "C",
            "苦渋の決断（くじゅうのけつだん）: Quyết định đau đớn, khó khăn trong tình thế tiến thoái lưỡng nan của người lãnh đạo.",
            {
                "A": "苦情（くじょう）: Lời phàn nàn, khiếu nại của khách hàng (苦情を言う).",
                "B": "苦痛（くつう）: Đau đớn thể xác hoặc tinh thần do bệnh tật, chấn thương.",
                "D": "苦境（くきょう）: Hoàn cảnh khốn đốn (苦境に陥る), là danh từ chỉ tình cảnh chứ không bổ nghĩa cho 決断."
            }
        ),
        (
            "N2_02_M4_03",
            "N2-MO-CONT",
            "Mondai 4: 文脈規定",
            "台風の影響で、列車のダイヤが（　　）乱れている。",
            "大幅に",
            [("A", "大層"), ("B", "大幅に"), ("C", "大まかに"), ("D", "大げさに")],
            "B",
            "大幅に（おおはばに）: Một cách đáng kể, trên quy mô lớn (thay đổi lịch trình, tăng giảm giá cả). Đi cùng 乱れる (rối loạn nghiêm trọng).",
            {
                "A": "大層（たいそう）: Rất, vô cùng (thường dùng trong văn nói cổ hoặc ngạc nhiên: 大層なごちそう).",
                "C": "大まかに（おおまかに）: Đại khái, sơ lược, chung chung (大まかに説明する).",
                "D": "大げさに（おおげさに）: Nói quá, làm quá, phóng đại lên (大げさに話す)."
            }
        ),
        (
            "N2_02_M4_04",
            "N2-MO-CONT",
            "Mondai 4: 文脈規定",
            "彼の書いた論文は構成が（　　）で、論理の飛躍が一切見られない。",
            "綿密",
            [("A", "厳重"), ("B", "綿密"), ("C", "粗末"), ("D", "寛大")],
            "B",
            "綿密（めんみつ - MIÊN MẬT）: Tỉ mỉ, chi tiết, kỹ lưỡng không có kẽ hở logic (綿密な計画, 綿密な調査).",
            {
                "A": "厳重（げんじゅう - NGHIÊM TRỌNG）: Nghiêm ngặt, cẩn mật (phòng ngự nghiêm ngặt: 厳重に警備する).",
                "C": "粗末（そまつ - THÔ MẠT）: Sơ sài, tồi tàn, coi thường (粗末にする).",
                "D": "寛大（かんだい - KHOAN ĐẠI）: Rộng lượng, bao dung với lỗi lầm người khác."
            }
        ),
        (
            "N2_02_M4_05",
            "N2-MO-CONT",
            "Mondai 4: 文脈規定",
            "長年の研究開発が実を結び、ついにライバル企業に（　　）をつけた。",
            "差",
            [("A", "隙"), ("B", "筋"), ("C", "差"), ("D", "跡")],
            "C",
            "差をつける（さをつける）: Tạo ra khoảng cách cách biệt, bỏ xa đối thủ cạnh tranh.",
            {
                "A": "隙（すき）: Kẽ hở, sơ hở (隙を突く - lợi dụng sơ hở).",
                "B": "筋（すじ）: Cốt truyện, mạch lý luận, cơ bắp.",
                "D": "跡（あと）: Dấu vết, vết tích."
            }
        ),
        (
            "N2_02_M4_06",
            "N2-MO-CONT",
            "Mondai 4: 文脈規定",
            "初対面の相手にも（　　）と挨拶ができる人は、第一印象が良い。",
            "にこやか",
            [("A", "しとやか"), ("B", "にこやか"), ("C", "さわやか"), ("D", "おろそか")],
            "B",
            "にこやかに: Mỉm cười niềm nở, tươi cười rạng rỡ (にこやかに挨拶する).",
            {
                "A": "しとやか: Dịu dàng, đoan trang, thùy mị (thường miêu tả cử chỉ phụ nữ truyền thống).",
                "C": "さわやか: Sảng khoái, tươi mát (thời tiết mát mẻ, giọng nói thanh thoát).",
                "D": "おろそか: Lơ là, sao nhãng nhiệm vụ (おろそかにする)."
            }
        ),
        (
            "N2_02_M4_07",
            "N2-MO-CONT",
            "Mondai 4: 文脈規定",
            "予期せぬ停電で、エレベーターの中に1時間も（　　）に遭った。",
            "閉じ込め",
            [("A", "包み込み"), ("B", "閉じ込め"), ("C", "抱き込み"), ("D", "繰り込み")],
            "B",
            "閉じ込め（とじこめ）: Bị nhốt kín, bị kẹt lại bên trong (エレベーターの閉じ込め事故).",
            {
                "A": "包み込み: Bọc kín lại, bao trùm.",
                "C": "抱き込み: Lôi kéo, mua chuộc phe cánh.",
                "D": "繰り込み: Đưa vào danh sách tính toán dồn cấp."
            }
        )
    ]

    for qid, type_id, mtitle, stem, target, opts, ans, exp, dist in m4_raw:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Vocabulary",
            "typeId": type_id,
            "mondaiTitle": mtitle,
            "stem": stem,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 2,
            "status": "QA_VERIFIED"
        })

    # =========================================================================
    # MONDAI 5: 言い換え類義 (Paraphrases / Synonyms - 5 items)
    # =========================================================================
    m5_raw = [
        (
            "N2_02_M5_01",
            "N2-MO-PARA",
            "Mondai 5: 言い換え類義",
            "この文書の内容を【ざっと】確認してください。",
            "おおまかに",
            [("A", "精密に"), ("B", "おおまかに"), ("C", "静かに"), ("D", "完全に")],
            "B",
            "ざっと: Lướt qua, đại khái, sơ bộ = おおまかに (xem nhanh nắm ý chính, không đi sâu từng chi tiết nhỏ).",
            {
                "A": "精密に（せいみつに）: Một cách tỉ mỉ, chính xác từng ly (nghĩa trái ngược).",
                "C": "静かに（しずかに）: Lặng lẽ, êm ả.",
                "D": "完全に（かんぜんに）: Hoàn toàn, triệt để."
            }
        ),
        (
            "N2_02_M5_02",
            "N2-MO-PARA",
            "Mondai 5: 言い換え類義",
            "彼の発言はいつも【皮肉】が込められている。",
            "嫌味",
            [("A", "好意"), ("B", "冗談"), ("C", "嫌味"), ("D", "熱意")],
            "C",
            "皮肉（ひにく）: Mỉa mai, châm chọc, cay độc = 嫌味（いやみ - lời lẽ xỏ xiên khiến người khác khó chịu).",
            {
                "A": "好意（こうい）: Thiện chí, lòng tốt (nghĩa trái ngược).",
                "B": "冗談（じょうだん）: Nói đùa, pha trò vô hại.",
                "D": "熱意（ねつい）: Nhiệt huyết, lòng nhiệt tình."
            }
        ),
        (
            "N2_02_M5_03",
            "N2-MO-PARA",
            "Mondai 5: 言い換え類義",
            "古い友人と街角で【ばったり】出会った。",
            "偶然に",
            [("A", "約束して"), ("B", "偶然に"), ("C", "無理に"), ("D", "急いで")],
            "B",
            "ばったり: Tình cờ, ngẫu nhiên chạm mặt không hề hẹn trước = 偶然に（ぐうぜんに）.",
            {
                "A": "約束して（やくそくして）: Có hẹn ước trước (nghĩa trái ngược).",
                "C": "無理に（むりに）: Ép buộc, gượng gạo.",
                "D": "急いで（いそいで）: Vội vàng, gấp gáp."
            }
        ),
        (
            "N2_02_M5_04",
            "N2-MO-PARA",
            "Mondai 5: 言い換え類義",
            "その計画は予算不足のため【頓挫】した。",
            "途中で挫折",
            [("A", "成功"), ("B", "延期"), ("C", "途中で挫折"), ("D", "急加速")],
            "C",
            "頓挫（とんざ - ĐỐN TỎA）: Gặp bế tắc đổ vỡ giữa chừng, thất bại đứt gánh = 途中で挫折（とちゅうでざせつ）.",
            {
                "A": "成功（せいこう）: Thành công tốt đẹp (nghĩa hoàn toàn trái ngược).",
                "B": "延期（えんき）: Hoãn lại sang ngày khác.",
                "D": "急加速（きゅうかそく）: Tăng tốc đột ngột."
            }
        ),
        (
            "N2_02_M5_05",
            "N2-MO-PARA",
            "Mondai 5: 言い換え類義",
            "彼は周囲の批判を【意に介さない】様子だった。",
            "気に留めない",
            [("A", "深く悩む"), ("B", "気に留めない"), ("C", "怒り狂う"), ("D", "恐れおののく")],
            "B",
            "意に介さない（いにかいさない）: Không để tâm, xem như không có chuyện gì, không bận lòng = 気に留めない（きにとめない）.",
            {
                "A": "深く悩む: Trăn trở phiền muộn sâu sắc (nghĩa trái ngược).",
                "C": "怒り狂う: Nổi giận đùng đùng mất kiểm soát.",
                "D": "恐れおののく: Run rẩy khiếp sợ."
            }
        )
    ]

    for qid, type_id, mtitle, stem, target, opts, ans, exp, dist in m5_raw:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Vocabulary",
            "typeId": type_id,
            "mondaiTitle": mtitle,
            "stem": stem,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 2,
            "status": "QA_VERIFIED"
        })

    # =========================================================================
    # MONDAI 6: 用法 (Usage - 5 items)
    # =========================================================================
    m6_raw = [
        (
            "N2_02_M6_01",
            "N2-MO-USAG",
            "Mondai 6: 用法",
            "【手薄（てうす）】の使い方として最も適切なものを選びなさい。",
            "手薄",
            [
                ("A", "この本はページ数が手薄なので、すぐに読み終わった。"),
                ("B", "連休中は警備員が手薄になるため、戸締まりを厳重にする必要がある。"),
                ("C", "彼の書いたレポートは内容が手薄で説得力に欠ける。"),
                ("D", "冬になると木の葉が手薄になり、枝だけが目立つ。")
            ],
            "B",
            "手薄（てうす）: Thiếu hụt nhân lực, mỏng quân số phòng thủ, bảo vệ hoặc quản lý (警備が手薄, 人員が手薄). Đáp án B dùng chuẩn xác.",
            {
                "A": "Sách mỏng dùng ページ数が少ない hoặc 薄い, không dùng 手薄.",
                "C": "Nội dung bài viết sơ sài dùng 内容が薄い hoặc 不十分, không dùng 手薄.",
                "D": "Lá cây rụng thưa thớt dùng 葉がまばらになる, không dùng 手薄."
            }
        ),
        (
            "N2_02_M6_02",
            "N2-MO-USAG",
            "Mondai 6: 用法",
            "【配慮（はいりょ）】の使い方として最も適切なものを選びなさい。",
            "配慮",
            [
                ("A", "高齢者や車椅子の利用者に配慮して、駅にエレベーターを増設した。"),
                ("B", "部屋が暗いので、窓を開けて光を配慮した。"),
                ("C", "毎朝ジョギングをして体力を配慮している。"),
                ("D", "明日の天気を配慮して傘を持って出かけた。")
            ],
            "A",
            "配慮（はいりょ）: Quan tâm, để ý chu đáo, thấu hiểu khó khăn của người khác để hỗ trợ (配慮が行き届く, 〜に配慮する). Đáp án A thể hiện sự quan tâm đến người già và xe lăn.",
            {
                "B": "Đón ánh sáng vào phòng dùng 光を取り入れた, không dùng 配慮.",
                "C": "Rèn luyện thể lực dùng 体力を養う hoặc 維持する.",
                "D": "Tính đến thời tiết dùng 天気を考慮して hoặc 心配して."
            }
        ),
        (
            "N2_02_M6_03",
            "N2-MO-USAG",
            "Mondai 6: 用法",
            "【無難（ぶなん）】の使い方として最も適切なものを選びなさい。",
            "無難",
            [
                ("A", "この試験は非常に無難だったので、全員が満点を取った。"),
                ("B", "服装に迷ったときは、落ち着いた色のスーツを着ていくのが無難だ。"),
                ("C", "彼女は無難な笑顔でみんなから大人気を集めている。"),
                ("D", "台風が無難に通過して被害が出なかった。")
            ],
            "B",
            "無難（ぶなん）: An toàn, không có gì xuất sắc nhưng không sợ mắc lỗi, phương án dung hòa tránh bị phê bình. Đáp án B chuẩn xác.",
            {
                "A": "Đề thi dễ dùng 平易な hoặc 簡単な, không dùng 無難.",
                "C": "Nụ cười duyên dáng đáng yêu dùng 魅力的な hoặc 素敵な笑顔.",
                "D": "Bão đi qua an toàn không gây hại dùng 無事に（ぶじに）."
            }
        ),
        (
            "N2_02_M6_04",
            "N2-MO-USAG",
            "Mondai 6: 用法",
            "【目途（めど）】の使い方として最も適切なものを選びなさい。",
            "目途",
            [
                ("A", "資金調達の目途が立ち、新工場の建設を再開できることになった。"),
                ("B", "遠くの景色を見るために双眼鏡で目途を合わせた。"),
                ("C", "彼の話は目途がはっきりしていて非常に分かりやすい。"),
                ("D", "次の駅まであと少しで目途に到着する。")
            ],
            "A",
            "目途（めど）: Triển vọng, manh mối khả thi hoàn thành mục tiêu (cụm từ cố định: 目途が立つ - nhìn thấy triển vọng; 目途をつける - nhắm tới mục tiêu). Đáp án A dùng đúng chuẩn.",
            {
                "B": "Lấy nét ống nhòm dùng ピントを合わせた.",
                "C": "Mạch câu chuyện rõ ràng dùng 要点（ようてん） hoặc 筋道（すじみち）.",
                "D": "Đến đích dùng 目的地（もくてきち）."
            }
        ),
        (
            "N2_02_M6_05",
            "N2-MO-USAG",
            "Mondai 6: 用法",
            "【妥協（だきょう）】の使い方として最も適切なものを選びなさい。",
            "妥協",
            [
                ("A", "どんなに困難な壁にぶつかっても、最後まで決して妥協しない。"),
                ("B", "二人は妥協して結婚式を盛大に挙げた。"),
                ("C", "商品の品質を高めるために、最高の素材を妥協した。"),
                ("D", "先生の妥協のおかげで、無事に進学できた。")
            ],
            "A",
            "妥協（だきょう）: Thỏa hiệp, chịu nhượng bộ, hạ thấp tiêu chuẩn bản thân (妥協しない - kiên quyết không nhượng bộ; 妥協点を見出す - tìm điểm chung thỏa hiệp). Đáp án A hoàn toàn chính xác.",
            {
                "B": "Kết hôn không dùng 妥協 mà dùng 合意 hoặc 意気投合.",
                "C": "Chọn nguyên liệu cao cấp nhất dùng 厳選した, không ai dùng 妥協.",
                "D": "Sự hướng dẫn chỉ bảo của thầy cô dùng ご指導 hoặc おかげ."
            }
        )
    ]

    for qid, type_id, mtitle, stem, target, opts, ans, exp, dist in m6_raw:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Vocabulary",
            "typeId": type_id,
            "mondaiTitle": mtitle,
            "stem": stem,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 3,
            "status": "QA_VERIFIED"
        })

    # =========================================================================
    # MONDAI 7: 文法形式 (Grammar Forms - 12 items)
    # =========================================================================
    m7_raw = [
        (
            "N2_02_M7_01",
            "N2-GR-FORM",
            "Mondai 7: 文法形式",
            "彼は多忙なスケジュールの（　　）、ボランティア活動を続けている。",
            "合間を縫って",
            [("A", "合間を縫って"), ("B", "合間を割いて"), ("C", "合間を惜しんで"), ("D", "合間を踏まえて")],
            "A",
            "合間を縫って（あいまをぬって）: Tranh thủ khoảng thời gian rảnh rỗi hiếm hoi giữa lịch trình bận rộn để làm việc gì đó. Quán ngữ cố định cấp độ N2.",
            {
                "B": "時間を割く（じかんをさく） là dành thời gian, không ghép với 合間を割く.",
                "C": "時間を惜しむ（じかんをおしむ） là quý trọng thời gian, không đi với 合間.",
                "D": "を踏まえて là dựa trên nền tảng/kinh nghiệm, không ăn khớp ngữ nghĩa."
            }
        ),
        (
            "N2_02_M7_02",
            "N2-GR-FORM",
            "Mondai 7: 文法形式",
            "プロの料理人（　　）、包丁の手入れには人一倍気を使っている。",
            "とあって",
            [("A", "とあって"), ("B", "にしては"), ("C", "と相まって"), ("D", "とあれば")],
            "A",
            "〜とあって: Vì tình huống đặc biệt là... nên đương nhiên là... (Vì là đầu bếp chuyên nghiệp nên việc chăm sóc dao bếp là điều đặc biệt chú trọng hơn người bình thường).",
            {
                "B": "〜にしては: Diễn tả sự không tương xứng với tiêu chuẩn (Là đầu bếp chuyên nghiệp mà nấu dở thì mới dùng にしては).",
                "C": "〜と相まって: Kết hợp hai yếu tố tạo nên hiệu quả tương hỗ (A cộng hưởng với B).",
                "D": "〜とあれば: Nếu là vì... thì bất cứ việc gì cũng làm."
            }
        ),
        (
            "N2_02_M7_03",
            "N2-GR-FORM",
            "Mondai 7: 文法形式",
            "事態がここまで悪化した以上、もはや社長自ら謝罪（　　）。",
            "せざるを得ない",
            [("A", "するにすぎない"), ("B", "せざるを得ない"), ("C", "するわけにはいかない"), ("D", "しないものでもない")],
            "B",
            "〜ざるを得ない: Không thể không..., đành phải... (dù không muốn nhưng tình thế bắt buộc phải làm). Chú ý động từ する biến thành せざるを得ない.",
            {
                "A": "〜にすぎない: Chỉ là... chẳng qua chỉ là (giảm nhẹ mức độ).",
                "C": "〜わけにはいかない: Không thể làm được do rào cản đạo đức/xã hội (ở đây tình hình tồi tệ nên bắt buộc phải xin lỗi).",
                "D": "〜ないものでもない: Không hẳn là không thể (thể hiện khả năng dè dặt)."
            }
        ),
        (
            "N2_02_M7_04",
            "N2-GR-FORM",
            "Mondai 7: 文法形式",
            "これほど精密な技術は、長年の鍛錬を重ねた熟練の職人（　　）可能だ。",
            "ならでは",
            [("A", "をはじめ"), ("B", "ならでは"), ("C", "にあって"), ("D", "をよそに")],
            "B",
            "〜ならでは: Chỉ có... mới có thể làm được (nhấn mạnh đặc tính độc đáo, tài năng độc nhất vô nhị). Đi kèm với職人ならでは.",
            {
                "A": "〜をはじめ: Tiêu biểu trước hết là A (kéo theo B, C...).",
                "C": "〜にあって: Trong hoàn cảnh đặc biệt đó...",
                "D": "〜をよそに: Bất chấp, phớt lờ dư luận/cảnh báo xung quanh."
            }
        ),
        (
            "N2_02_M7_05",
            "N2-GR-FORM",
            "Mondai 7: 文法形式",
            "彼の説明は専門用語ばかりで、一般の人には理解（　　）ものだった。",
            "がたい",
            [("A", "やすい"), ("B", "かねる"), ("C", "がたい"), ("D", "っこない")],
            "C",
            "V-masu + がたい: Khó lòng mà... (về mặt tâm lý, nhận thức, tình cảm: 理解しがたい - khó mà hiểu nổi, 信じがたい - khó mà tin được).",
            {
                "A": "やすい: Dễ dàng (trái ngược hoàn toàn ngữ cảnh toàn thuật ngữ chuyên môn).",
                "B": "かねる: Đứng sau thể liên từ lịch sự để từ chối dịch vụ (分かりかねます, 引き受けかねます), không ghép trực tiếp thành 理解かねるもの.",
                "D": "っこない: Tuyệt đối không thể (văn nói thân mật, không dùng trong văn viết trang trọng này)."
            }
        ),
        (
            "N2_02_M7_06",
            "N2-GR-FORM",
            "Mondai 7: 文法形式",
            "どんなに科学技術が進歩（　　）、自然の驚異を完全に支配することはできない。",
            "しようと",
            [("A", "しようと"), ("B", "したところで"), ("C", "するにつけ"), ("D", "するからには")],
            "A",
            "どんなに + V-よう（意向形） + と（も）: Dù cho... đến mức nào đi chăng nữa thì kết quả vẫn không đổi (どんなに進歩しようと - Dù công nghệ có tiến bộ đến đâu).",
            {
                "B": "したところで: Dù đã làm việc đó rồi thì cũng vô ích (thường không đi trực tiếp với phó từ どんなに ở đầu câu mang nghĩa giả định tiến trình).",
                "C": "するにつけ: Cứ mỗi lần nhìn/nghe thấy A là lại cảm thấy B.",
                "D": "からには: Một khi đã... thì phải..."
            }
        ),
        (
            "N2_02_M7_07",
            "N2-GR-FORM",
            "Mondai 7: 文法形式",
            "新店舗の開店準備で、休む（　　）食事をする時間すらない。",
            "どころか",
            [("A", "ばかりか"), ("B", "どころか"), ("C", "反面"), ("D", "わりに")],
            "B",
            "AどころかB: Nói chi đến A, ngay cả B còn không có/không thể. Ở đây: Nói chi đến nghỉ ngơi, đến thời gian ăn cơm còn không có.",
            {
                "A": "ばかりか: Không những A mà còn thêm B (thường cùng chiều tăng tiến, không đi với câu phủ định hoàn toàn すらない).",
                "C": "反面: Mặt khác, trái lại (hai mặt của cùng một vấn đề).",
                "D": "わりに: So với tiêu chuẩn thì..."
            }
        ),
        (
            "N2_02_M7_08",
            "N2-GR-FORM",
            "Mondai 7: 文法形式",
            "これまでの実績とチームワーク（　　）、今回の大会も優勝できるに違いない。",
            "から見て",
            [("A", "から見て"), ("B", "を契機に"), ("C", "を皮切りに"), ("D", "に先立って")],
            "A",
            "〜から見て / 〜から見ると: Nhìn từ góc độ, căn cứ vào dữ liệu/thực tế đó mà đưa ra phán đoán logic.",
            {
                "B": "〜を契機に: Nhân cơ hội, bước ngoặt từ một sự kiện.",
                "C": "〜を皮切りに: Khởi đầu mở màn bằng hành động A, sau đó hàng loạt hành động tương tự tiếp diễn.",
                "D": "〜に先立って: Trước khi tiến hành một sự kiện lớn..."
            }
        ),
        (
            "N2_02_M7_09",
            "N2-GR-FORM",
            "Mondai 7: 文法形式",
            "お客様のご要望（　　）、柔軟にサービスプランをカスタマイズいたします。",
            "に応じて",
            [("A", "に際して"), ("B", "に応じて"), ("C", "に反して"), ("D", "にわたって")],
            "B",
            "〜に応じて（におうじて）: Ứng với, tương ứng với nguyện vọng/thay đổi của khách hàng. Quán ngữ thông dụng: ご要望に応じて.",
            {
                "A": "に際して: Nhân dịp, khi tiến hành một sự việc trang trọng.",
                "C": "に反して: Ngược lại với kỳ vọng/dự đoán.",
                "D": "にわたって: Kéo dài suốt trên một diện tích hoặc khoảng thời gian."
            }
        ),
        (
            "N2_02_M7_10",
            "N2-GR-FORM",
            "Mondai 7: 文法形式",
            "部長、先ほどメールでお送りした企画書を、もう（　　）でしょうか。",
            "ご覧になりました",
            [("A", "拝見しました"), ("B", "ご覧になりました"), ("C", "お見せになりました"), ("D", "お目にかかりました")],
            "B",
            "ご覧になりましたでしょうか: Kính ngữ (Tôn kính ngữ - 尊敬語) hỏi hành động xem tài liệu của cấp trên (部長).",
            {
                "A": "拝見しました: Khiêm nhường ngữ (謙譲語) dùng cho hành động của chính người nói (tôi xem), không dùng hỏi sếp.",
                "C": "お見せになりました: Nhầm lẫn ngữ pháp khiêm nhường/tôn kính.",
                "D": "お目にかかりました: Khiêm nhường ngữ của 会う (gặp gỡ)."
            }
        ),
        (
            "N2_02_M7_11",
            "N2-GR-FORM",
            "Mondai 7: 文法形式",
            "あんなに温厚な田中さんが声を荒らげるなんて、よほどのことがあった（　　）。",
            "に違いない",
            [("A", "に違いない"), ("B", "にすぎない"), ("C", "にほかならない"), ("D", "に越したことはない")],
            "A",
            "〜に違いない: Chắc chắn là... (phán đoán quả quyết dựa trên bằng chứng gián tiếp xác thực: Người hiền lành như Tanaka mà nổi giận thì chắc chắn phải có chuyện rất ghê gớm).",
            {
                "B": "〜にすぎない: Chẳng qua chỉ là...",
                "C": "〜にほかならない: Chính là, không gì khác ngoài...",
                "D": "〜に越したことはない: ...là tốt nhất."
            }
        ),
        (
            "N2_02_M7_12",
            "N2-GR-FORM",
            "Mondai 7: 文法形式",
            "今回のプロジェクトの成功は、チーム全員の協力（　　）語れない。",
            "なくしては",
            [("A", "ぬきにして"), ("B", "なくしては"), ("C", "をおいて"), ("D", "によらず")],
            "B",
            "〜なくしては（...ない）: Nếu không có A thì không thể nào có B (vế sau luôn đi kèm thể phủ định). Cụm: 協力なくしては語れない.",
            {
                "A": "ぬきにして: Bỏ qua A, không bàn tới A (thường đi với thể khẳng định: 冗談はぬきにして本題に入ろう).",
                "C": "をおいて: Ngoại trừ người này ra thì không ai khác (thường đi với danh từ chỉ người: 彼をおいて他にいない).",
                "D": "によらず: Bất kể, không phụ thuộc vào..."
            }
        )
    ]

    for qid, type_id, mtitle, stem, target, opts, ans, exp, dist in m7_raw:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Grammar",
            "typeId": type_id,
            "mondaiTitle": mtitle,
            "stem": stem,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 2,
            "status": "QA_VERIFIED"
        })

    # =========================================================================
    # MONDAI 8: 文の組み立て ★ (Star Sentence Composition - 5 items)
    # =========================================================================
    m8_raw = [
        (
            "N2_02_M8_01",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "環境問題の解決には、行政だけでなく＿＿　＿＿　★　＿＿　欠かせない。",
            "一人ひとりの　／　意識の改革が　／　市民　／　何より",
            [("A", "一人ひとりの"), ("B", "意識の改革が"), ("C", "市民"), ("D", "何より")],
            "B", # Thứ tự: 市民 (C) 一人ひとりの (A) ★ 意識の改革が (B) 何より (D) => Vị trí sao ở số 3 là "B" (意識の改革が)
            "Thứ tự đúng: 行政だけでなく【市民 (C)】【一人ひとりの (A)】【★ 意識の改革が (B)】【何より (D)】欠かせない. Vị trí ngôi sao là B (意識の改革が).",
            {
                "A": "一人ひとりの bổ nghĩa cho 意識の改革が (vị trí 3 - sao).",
                "C": "市民 đi trước 一人ひとりの (市民一人ひとりの - từng người dân một).",
                "D": "何より đứng trước 欠かせない (何より欠かせない - không thể thiếu hơn bất cứ điều gì)."
            }
        ),
        (
            "N2_02_M8_02",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "一度引き受けた仕事である以上、＿＿　＿＿　★　＿＿　責任がある。",
            "やり遂げる　／　困難があろうと　／　最後まで　／　いかに",
            [("A", "やり遂げる"), ("B", "困難があろうと"), ("C", "最後まで"), ("D", "いかに")],
            "C", # Thứ tự: いかに (D) 困難があろうと (B) ★ 最後まで (C) やり遂げる (A) => Vị trí 3 là "C" (最後まで)
            "Thứ tự đúng: 一度引き受けた仕事である以上、【いかに (D)】【困難があろうと (B)】【★ 最後まで (C)】【やり遂げる (A)】責任がある. Vị trí ngôi sao là C (最後まで).",
            {
                "A": "やり遂げる đứng trước 責任がある (bổ nghĩa danh từ: やり遂げる責任がある).",
                "B": "いかに ... あろうと (Dù có khó khăn đến mức nào).",
                "D": "いかに mở đầu mệnh đề nhượng bộ."
            }
        ),
        (
            "N2_02_M8_03",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "健康を維持する上で、栄養バランスの取れた食事は＿＿　＿＿　★　＿＿　言えない。",
            "極めて　／　十分とは　／　それだけで　／　大切だが",
            [("A", "極めて"), ("B", "十分とは"), ("C", "それだけで"), ("D", "大切だが")],
            "C", # Thứ tự: 極めて (A) 大切だが (D) ★ それだけで (C) 十分とは (B) 言えない => Vị trí sao là C (それだけで)
            "Thứ tự đúng: 食事は【極めて (A)】【大切だが (D)】【★ それだけで (C)】【十分とは (B)】言えない. Vị trí ngôi sao là C (それだけで).",
            {
                "A": "極めて bổ nghĩa cho 大切だが.",
                "B": "十分とは đứng trước 言えない.",
                "D": "大切だが tạo liên kết tương phản."
            }
        ),
        (
            "N2_02_M8_04",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "現代社会において、インターネットの普及は＿＿　＿＿　★　＿＿　変革をもたらした。",
            "私たちの　／　生活様式に　／　劇的な　／　かつてない",
            [("A", "私たちの"), ("B", "生活様式に"), ("C", "劇的な"), ("D", "かつてない")],
            "D", # Thứ tự: 私たちの (A) 生活様式に (B) ★ かつてない (D) 劇的な (C) => Vị trí sao là D (かつてない)
            "Thứ tự đúng: インターネットの普及は【私たちの (A)】【生活様式に (B)】【★ かつてない (D)】【劇的な (C)】変革をもたらした. Vị trí ngôi sao là D (かつてない).",
            {
                "A": "私たちの bổ nghĩa cho 生活様式に.",
                "B": "生活様式に bổ nghĩa cho 変革をもたらした.",
                "C": "劇的な đứng ngay trước danh từ 変革 (劇的な変革)."
            }
        ),
        (
            "N2_02_M8_05",
            "N2-GR-STAR",
            "Mondai 8: 文の組み立て ★",
            "チームの勝利は、選手たちの努力もさることながら、＿＿　＿＿　★　＿＿　大きい。",
            "的確な指導に　／　監督の　／　ところが　／　負う",
            [("A", "的確な指導に"), ("B", "監督の"), ("C", "ところが"), ("D", "負う")],
            "D", # Thứ tự: 監督の (B) 的確な指導に (A) ★ 負う (D) ところが (C) 大きい
            "Thứ tự đúng: 選手たちの努力もさることながら、【監督の (B)】【的確な指導に (A)】【★ 負う (D)】【ところが (C)】大きい. Cấu trúc cố định: 〜に負うところが大きい (nhờ vào / đóng góp rất lớn bởi). Vị trí sao là D (負う).",
            {
                "A": "的確な指導に đi với động từ 負う (〜に負う).",
                "B": "監督の bổ nghĩa cho 的確な指導.",
                "C": "ところが kết hợp với 大きい (ところ・部分が sẽ lớn)."
            }
        )
    ]

    for qid, type_id, mtitle, stem, target, opts, ans, exp, dist in m8_raw:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Grammar",
            "typeId": type_id,
            "mondaiTitle": mtitle,
            "stem": stem,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 3,
            "status": "QA_VERIFIED"
        })

    # =========================================================================
    # MONDAI 9: 文章の文法 (Text Grammar - 5 items on 1 passage)
    # =========================================================================
    m9_passage = """【読書がもたらす共感の力】
現代社会では、SNSの普及により短文での即時的なコミュニケーションが主流となった。しかし、その一方で、他者の複雑な感情や文脈を深く読み取る能力の低下が（　46　）。
文学作品を読むという行為は、単なる情報の受容ではない。自分とは全く異なる時代や境遇に生きる登場人物の視点に立ち、その喜びや苦悩を追体験することである。登場人物の葛藤に寄り添うことを（　47　）、私たちは自己の中心的な世界から抜け出し、他者への想像力を養うことができる。
他者の痛みに共感する力は、先天的に備わっているもの（　48　）、後天的に磨かれる技術でもある。もし社会全体が効率性ばかりを追い求め、物語を読む時間を失ってしまったら、人間関係は極めて殺伐としたものに（　49　）。
だからこそ、忙しい日々の生活のなかにこそ、一冊の本と静かに向き合う時間を（　50　）のではないだろうか。"""

    m9_raw = [
        (
            "N2_02_M9_01",
            "46番に入る最も適切なものを選びなさい。",
            [("A", "懸念されている"), ("B", "懸念するべきだ"), ("C", "懸念せざるを得ない"), ("D", "懸念されるはずだ")],
            "A",
            "懸念されている（けねんされている）: Đang bị xã hội lo ngại, là sự thật khách quan đang diễn ra trong cộng đồng.",
            {
                "B": "懸念するべきだ: Áp đặt nghĩa vụ chủ quan, không hợp ngữ cảnh miêu tả hiện trạng.",
                "C": "懸念せざるを得ない: Thể hiện người nói đành phải lo ngại, không diễn tả xu hướng chung.",
                "D": "懸念されるはずだ: Phán đoán chắc chắn có cơ sở logic, nhưng ở đây là thực trạng đã được ghi nhận."
            }
        ),
        (
            "N2_02_M9_02",
            "47番に入る最も適切なものを選びなさい。",
            [("A", "皮切りにして"), ("B", "通じて"), ("C", "めぐって"), ("D", "問わず")],
            "B",
            "〜を通じて（をつうじて）: Thông qua phương tiện, qua trải nghiệm gắn kết với sự giằng xé của nhân vật mà con người nuôi dưỡng trí tưởng tượng.",
            {
                "A": "皮切りにして: Mở đầu bằng một hành động cụ thể.",
                "C": "めぐって: Xoay quanh một tranh chấp, chủ đề bàn tán.",
                "D": "問わず: Bất kể (không phân biệt)."
            }
        ),
        (
            "N2_02_M9_03",
            "48番に入る最も適切なものを選びなさい。",
            [("A", "ばかりではなく"), ("B", "といえども"), ("C", "に反して"), ("D", "をはじめ")],
            "A",
            "〜ばかりではなく: Không chỉ là bẩm sinh sẵn có mà còn là kỹ năng được mài giũa về sau. Cặp liên từ: AばかりではなくBも.",
            {
                "B": "といえども: Dẫu cho là...",
                "C": "に反して: Ngược lại với...",
                "D": "をはじめ: Tiêu biểu là..."
            }
        ),
        (
            "N2_02_M9_04",
            "49番に入る最も適切なものを選びなさい。",
            [("A", "なりかねない"), ("B", "なるわけがない"), ("C", "なるに決まっている"), ("D", "なりっこない")],
            "A",
            "〜かねない: Có nguy cơ dẫn tới hậu quả tiêu cực (mối quan hệ con người có nguy cơ trở nên vô cùng tàn nhẫn, lạnh lùng).",
            {
                "B": "なるわけがない: Tuyệt đối không thể trở thành (phủ định vô lý).",
                "C": "なるに決まっている: Chắc chắn sẽ trở thành (quá mang tính áp đặt).",
                "D": "なりっこない: Văn nói suồng sã, không dùng trong tiểu luận."
            }
        ),
        (
            "N2_02_M9_05",
            "50番に入る最も適切なものを選びなさい。",
            [("A", "確保するべきではない"), ("B", "確保したいものだ"), ("C", "確保しようとする"), ("D", "確保するべきな")],
            "D",
            "〜べきなのではないだろうか: Phải chăng chúng ta nên dành ra thời gian... (Cách kết bài đề xuất quan điểm mang tính xây dựng, lịch sự của tác giả).",
            {
                "A": "確保するべきではない: Phủ định (không nên dành thời gian), trái ngược với tư tưởng bài viết.",
                "B": "確保したいものだ: Thể hiện mong muốn cá nhân, không ghép hợp ngữ pháp với のではないだろうか.",
                "C": "確保しようとする: Đang toan tính làm gì."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m9_raw:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Grammar",
            "typeId": "N2-GR-TEXT",
            "mondaiTitle": "Mondai 9: 文章の文法 (Ngữ pháp văn bản)",
            "stem": stem,
            "contextPassage": m9_passage,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 3,
            "status": "QA_VERIFIED"
        })

    # =========================================================================
    # MONDAI 10: 短文読解 (Short Reading - 5 passages x 1 item = 5 items)
    # =========================================================================
    m10_passages = [
        (
            "N2_02_M10_01",
            "短文 1：職人の技とデジタル化",
            """伝統工芸の世界でも、3DプリンターやAIによる自動化の導入が進んでいる。熟練職人の手の動きをデータ化し、寸分の狂いもなく再現する技術は、後継者不足に悩む産地にとって画期的な救世主に見える。しかし、職人が真に継承しているのは、単なる正確な身体動作ではない。その日の気温や湿度、木材の微細な個体差を肌で感じ取り、瞬時に刃物の当て方を微調整する「臨機応変の勘」である。データ化できる部分と、現場の身体知としてしか伝えられない部分の境界を見極めることこそが、伝統を未来へ繋ぐ鍵となる。""",
            "筆者が最も言いたいことは何か。",
            [
                ("A", "伝統工芸はAIに任せれば、職人の修業期間をゼロに短縮できる。"),
                ("B", "職人の勘はすべて迷信であり、3Dプリンターの正確さのみを信じるべきだ。"),
                ("C", "環境変化に即応する職人の身体知とデジタル技術の境界を見極めることが重要だ。"),
                ("D", "伝統を守るためには、いかなるデジタル技術の導入も断固拒否すべきだ。")
            ],
            "C",
            "Tác giả chỉ ra rằng công nghệ có thể số hóa thao tác nhưng không thể thay thế 'trực giác ứng biến' (臨機応変の勘) theo nhiệt độ, độ ẩm của nghệ nhân. Do đó mấu chốt là phải nhận rõ ranh giới giữa tri thức cơ thể và phần có thể số hóa.",
            {
                "A": "Tác giả không nói thời gian học nghề rút về 0.",
                "B": "Tác giả khẳng định trực giác nghệ nhân là tri thức cơ thể (身体知) quý giá, không phải mê tín.",
                "D": "Tác giả thừa nhận số hóa là cứu tinh giải quyết thiếu người nối nghiệp, không hề bài xích cực đoan."
            }
        ),
        (
            "N2_02_M10_02",
            "短文 2：マルチタスクの落とし穴",
            """現代のビジネスパーソンは、複数の画面を開き、メールを返信しながら会議に参加する「マルチタスク」を効率的だと捉えがちである。しかし、認知心理学の研究によれば、人間の脳は複数の認知的作業を同時に処理することはできず、実際には極めて短時間で注意を切り替えているにすぎない。この「タスクの頻繁な切り替え」は、脳に過度な認知的負荷を与え、作業速度を落とすだけでなく、思考の深化を決定的に妨げる。真の生産性とは、一度に多くのことをこなすことではなく、一つの重要課題に意識を集中させる能力にある。""",
            "「マルチタスク」について、筆者の主張と合致するものはどれか。",
            [
                ("A", "マルチタスクは脳を鍛え、思考を深める最良の訓練法である。"),
                ("B", "人間の脳は複数の作業を同時に並行処理できる優れた構造を持つ。"),
                ("C", "作業の切り替えは脳に過大な負荷を与え、かえって生産性を低下させる。"),
                ("D", "ビジネスで成功するためには、メール返信を最優先にして常に画面を注視すべきだ。")
            ],
            "C",
            "Nghiên cứu chỉ ra não người không làm được nhiều việc cùng lúc mà chỉ đang chuyển đổi chú ý liên tục, gây quá tải nhận thức và làm giảm sút năng suất thực sự.",
            {
                "A": "Tác giả chỉ ra đa nhiệm cản trở việc suy nghĩ sâu sắc (思考の深化を妨げる).",
                "B": "Trái ngược với nhận định của tâm lý học nhận thức rằng não người không thể xử lý đồng thời.",
                "D": "Không có ý khuyên chăm chăm nhìn màn hình trả lời mail."
            }
        ),
        (
            "N2_02_M10_03",
            "短文 3：都市の緑地と生物多様性",
            """都市部における公園や街路樹の整備は、単に人間に癒やしや景観美を提供するだけの設備ではない。孤立したコンクリートの海の中で、緑地は鳥や昆虫が移動するための「生態系の回廊（コリドー）」としての決定的な役割を果たしている。点在する小規模な庭や屋上緑化であっても、それらが互いに近接してネットワークを形成していれば、生物は都市を横断して生息域を広げることができる。都市計画においては、個々の緑地の面積だけでなく、緑地同士の空間的な連続性を考慮することが不可欠なのだ。""",
            "都市の緑地計画について、筆者はどのように考えているか。",
            [
                ("A", "都市の緑地は人間のストレス解消だけを目的として設計されるべきだ。"),
                ("B", "小規模な緑地は生態系にとって何の価値もないため、撤去してビルを建てるべきだ。"),
                ("C", "生物が移動できるように、緑地同士がつながる空間的連続性を重視すべきだ。"),
                ("D", "鳥や昆虫が都市に入り込まないよう、防虫ネットで公園を囲む必要がある。")
            ],
            "C",
            "Tác giả nhấn mạnh trong quy hoạch đô thị cần phải xem xét 'tính liên tục trong không gian' (空間的な連続性) để tạo hành lang sinh thái kết nối các mảng xanh cho sinh vật di chuyển.",
            {
                "A": "Tác giả khẳng định công viên không chỉ phục vụ sự thư giãn của con người.",
                "B": "Tác giả nêu rõ ngay cả mảng xanh nhỏ hay mái nhà xanh nếu kết nối mạng lưới vẫn mang giá trị to lớn.",
                "D": "Không hề đề cập đến việc giăng lưới đuổi côn trùng."
            }
        ),
        (
            "N2_02_M10_04",
            "短文 4：批判的思考（クリティカル・シンキング）の本質",
            """批判的思考と聞くと、他者の意見のあら探しをしたり、否定的な見解を述べたりすることだと誤解されやすい。しかし本来の批判的思考とは、自分自身の前提や常識をも疑い、物事を多角的な視点から客観的に再吟味する知的態度のことを指す。「自分が正しいと信じている根拠は本当に妥当か」「見落としている前提はないか」と問い続けることで、私たちは感情的な偏見から自由になり、より合理的な判断に到達することができる。他者を論破するためではなく、自分自身の思考を更新するための道具なのだ。""",
            "筆者が考える「本来の批判的思考」とはどのようなものか。",
            [
                ("A", "他人の意見の弱点を見つけ出し、議論で相手を言い負かす技術。"),
                ("B", "自分自身の前提や思い込みを疑い、客観的に再検討して判断を高める態度。"),
                ("C", "あらゆる社会通念や法律を完全に無視して、自分の感情のままに行動すること。"),
                ("D", "専門家の意見には一切逆らわず、提示された情報をそのまま受け入れること。")
            ],
            "B",
            "Tư duy phản biện đích thực là thái độ trí tuệ biết tự vấn các tiền đề và định kiến của chính mình, nhìn nhận đa chiều để đưa ra quyết định hợp lý, không phải để bắt bẻ người khác.",
            {
                "A": "Đây là ngộ nhận phổ biến mà tác giả phê phán ở đầu bài.",
                "C": "Không hề bảo bài xích pháp luật hay làm theo cảm tính.",
                "D": "Trái ngược với tinh thần tự vấn và kiểm chứng khách quan."
            }
        ),
        (
            "N2_02_M10_05",
            "短文 5：美術館における「対話型鑑賞」",
            """従来の美術館鑑賞は、作品の解説パネルを読み、美術史的な正解知識を学ぶスタイルが主流であった。これに対し近年注目されている「対話型鑑賞」は、解説をあえて読まず、鑑賞者同士が「作品のどこからそう感じたか」を言葉にして語り合う試みである。正解のない問いに向き合い、他者の異なる見方に触れることで、自分一人では気づけなかった作品の新たな側面に目が開かれる。作品を「消費」するのではなく、自らの主体的な対話を通じて「意味を共同で生成する」体験こそが、現代の美術館に求められている。""",
            "「対話型鑑賞」の特徴として、本文で述べられているものはどれか。",
            [
                ("A", "学芸員の解説講義を静かに聴き、年表を完全に暗記するスタイル。"),
                ("B", "解説に頼らず、鑑賞者同士が感じた根拠を語り合いながら意味を深める方法。"),
                ("C", "絵画を鑑賞しながら大声で音楽を流し、身体を動かして踊る鑑賞法。"),
                ("D", "有名画家の絵だけを高額で買い取り、個人宅で鑑賞する展示方法。")
            ],
            "B",
            "Đặc trưng của thưởng lãm tương tác (対話型鑑賞) là không dựa vào bảng giải thích có sẵn, mà những người xem cùng trao đổi cảm nhận và căn cứ của mình để cùng nhau kiến tạo ý nghĩa tác phẩm.",
            {
                "A": "Đây là phương pháp truyền thống thụ động mà tác giả đối chiếu.",
                "C": "Không hề nói về việc bật nhạc hay nhảy múa trong bảo tàng.",
                "D": "Không liên quan đến việc đấu giá tranh của cá nhân."
            }
        )
    ]

    for qid, title, passage, stem, opts, ans, exp, dist in m10_passages:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Reading",
            "typeId": "N2-RD-SHOR",
            "mondaiTitle": "Mondai 10: 短文読解 (Đọc hiểu đoạn ngắn)",
            "stem": stem,
            "contextPassage": passage,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 2,
            "status": "QA_VERIFIED"
        })

    # =========================================================================
    # MONDAI 11: 中文読解 (Medium Reading - 3 passages x 3 items = 9 items)
    # =========================================================================
    # Passage 1: 日本の木造建築と持続可能性
    m11_p1_text = """【日本の伝統木造建築に見る知恵】
世界最古の木造建築である法隆寺をはじめ、日本の伝統的な神社仏閣は千年以上もの風雪に耐えて今日にその姿を伝えている。高温多湿で地震が多いという過酷な風土において、なぜこれほどまでに長寿命な建築が可能であったのだろうか。その秘密は、金属の釘やボルトを極力使わず、木材同士の複雑な凹凸を組み合わせる「木組み（きぐみ）」の技術にある。

木組み構造の最大の特徴は、地震などの外力が加わった際に、接合部がわずかに滑り、摩擦によって揺れのエネルギーを吸収・分散させる点にある。完全に固定された硬い構造物は強い衝撃で一気に破断する危険があるが、木組みは柔軟にしなることで倒壊を防ぐのだ。これは現代の免震工学の思想と完全に一致している。

さらに、木造建築は「解体と部材交換」を前提として設計されている。傷んだ柱や梁だけを取り外し、新しい木材に差し替えることができるため、建物全体を壊すことなく何百年も維持できる。木材という自然素材の伸縮や狂いを計算に入れ、次世代の大工が修理しやすいように細工を残しておく――。そこには、自然をねじ伏せるのではなく、自然の理に寄り添い、時間の流れを味方につける持続可能な設計思想が息づいている。"""

    m11_p1_questions = [
        (
            "N2_02_M11_01",
            "日本の木組み構造が地震に強い理由として、筆者はどのように説明しているか。",
            [
                ("A", "金属の太いボルトで隙間なく完全に固定されているため。"),
                ("B", "接合部がわずかに滑ることで、地震の揺れのエネルギーを吸収・分散させるため。"),
                ("C", "木材の内部に鉄筋を埋め込んで頑丈な強度を持たせているため。"),
                ("D", "地面と建物を完全に切り離し、宙に浮かせる仕組みになっているため。")
            ],
            "B",
            "Đoạn 2 giải thích rõ: Khớp nối gỗ trượt nhẹ khi có lực chấn động, ma sát giúp hấp thụ và triệt tiêu năng lượng rung lắc (接合部がわずかに滑り、揺れのエネルギーを吸収・分散).",
            {
                "A": "Ngược lại, bài nhấn mạnh 'không dùng đinh ốc kim loại' (金属の釘やボルトを極力使わず).",
                "C": "Không hề có chuyện nhét lõi sắt vào trong thân gỗ cổ.",
                "D": "Không phải công nghệ bay lơ lửng trên không trung."
            }
        ),
        (
            "N2_02_M11_02",
            "「解体と部材交換」ができることの利点として、合致するものはどれか。",
            [
                ("A", "建物を毎回ゼロから作り直す費用を節約し、観光客を増やすこと。"),
                ("B", "傷んだ部材だけを取り替えることで、建物を何百年も維持し続けられること。"),
                ("C", "大工の仕事を増やして、地域の若者の雇用を無理に確保すること。"),
                ("D", "木材の代わりにコンクリートを流し込んで現代風に改築できること。")
            ],
            "B",
            "Đoạn 3 khẳng định: Nhờ tháo dỡ và thay thế được từng cây cột xà bị mục nên có thể bảo tồn công trình qua hàng trăm năm mà không cần đập bỏ toàn bộ.",
            {
                "A": "Mục đích không phải để thu hút du khách hay xây mới từ con số không.",
                "C": "Không phải để giải quyết việc làm gượng ép.",
                "D": "Không đề cập đến việc đổ bê tông vào kiến trúc cổ."
            }
        ),
        (
            "N2_02_M11_03",
            "この文章全体で、筆者が伝統木造建築から最も学べると考えている思想は何か。",
            [
                ("A", "自然を力で支配するのではなく、自然の性質に寄り添う持続可能な設計思想。"),
                ("B", "金属や最新技術はすべて有害であり、古代の道具だけを使うべきだという主張。"),
                ("C", "地震が起きたら諦めて逃げ、新しい土地に引っ越すべきだという諦念。"),
                ("D", "木材資源を大量に伐採して、経済成長を最優先させる産業政策。")
            ],
            "A",
            "Câu kết luận nêu rõ: '自然をねじ伏せるのではなく、自然の理に寄り添い、時間の流れを味方につける持続可能な設計思想' (Tư tưởng thiết kế bền vững nương theo quy luật tự nhiên thay vì dùng sức mạnh chế ngự tự nhiên).",
            {
                "B": "Tác giả chỉ ra kiến trúc cổ đồng điệu với kỹ thuật giảm chấn hiện đại, không cực đoan bài trừ kỹ thuật mới.",
                "C": "Không hề nói về việc bỏ chạy hay buông xuôi.",
                "D": "Ngược lại hoàn toàn với tư tưởng phát triển bền vững."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m11_p1_questions:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Reading",
            "typeId": "N2-RD-MEDI",
            "mondaiTitle": "Mondai 11: 中文読解 (Đọc hiểu trung văn)",
            "stem": stem,
            "contextPassage": m11_p1_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 3,
            "status": "QA_VERIFIED"
        })

    # Passage 2: 時間の知覚と年齢
    m11_p2_text = """【なぜ年をとると時間が早く過ぎるのか】
子供の頃の1年間は永遠のように長く感じられたのに、大人になると「あっという間に1年が過ぎてしまった」と口にする人が多い。この年齢に伴う時間感覚の加速現象は、19世紀のフランスの哲学者ジャネが提唱した「ジャネの法則」によって心理学的に説明されることが多い。すなわち、5歳の子供にとっての1年は人生の5分の1（20％）に相当するが、50歳の大人にとっての1年は人生のわずか50分の1（2％）にすぎないという比率の論理である。

しかし、近年の認知科学では、単なる主観的な比率の問題だけでなく、「新奇な体験の密度」が時間知覚に深く関わっていることが明らかになってきた。子供の頃は、見るもの聞くものすべてが未知であり、脳は新しい情報を処理するために膨大な認知的注意を注ぎ込む。その結果、記憶の中に刻み込まれる「情報のエピソード数」が極めて多くなり、後から振り返ったときに「長い時間だった」と知覚されるのである。

一方、大人の日常生活は、慣れ親しんだルーティンの連続になりがちである。通勤ルート、仕事の手順、会話のパターンなどが自動化されると、脳は省エネモードで稼働し、記憶に記録される新しい情報が劇的に減少する。その結果、過去を振り返ったときの記憶の密度が希薄になり、時間が一瞬で過ぎ去ったかのように錯覚してしまう。時間を豊かに、そして長く生きるための秘訣は、大人になっても意識して新しい挑戦を続け、日常に「未知の体験」を意図的に織り込んでいくことにある。"""

    m11_p2_questions = [
        (
            "N2_02_M11_04",
            "子供の頃の時間が長く感じられる理由として、近年の認知科学はどのように説明しているか。",
            [
                ("A", "子供は体内時計の針が大人よりも物理的に遅く進んでいるため。"),
                ("B", "未知の体験が多く、脳が多くの新しい情報を記憶に刻み込んでいるため。"),
                ("C", "勉強や運動で疲労し、毎日退屈な時間を過ごしているため。"),
                ("D", "大人のように仕事の責任がなく、遊んでばかりいるため。")
            ],
            "B",
            "Đoạn 2 nêu rõ: Đối với trẻ em, mọi thứ đều mới mẻ nên não bộ phải tập trung xử lý, số lượng ký ức khắc ghi (情報のエピソード数) rất nhiều, khi nhìn lại sẽ thấy thời gian rất dài.",
            {
                "A": "Đồng hồ sinh học vật lý không hề chạy chậm hơn.",
                "C": "Không hề nói trẻ em buồn chán mệt mỏi.",
                "D": "Không bàn về gánh nặng trách nhiệm công việc."
            }
        ),
        (
            "N2_02_M11_05",
            "大人の時間が「あっという間に過ぎる」と感じられる直接的な原因は何か。",
            [
                ("A", "年齢とともに脳の処理速度が劇的に向上し、すべての作業が一瞬で終わるから。"),
                ("B", "日々の行動がルーティン化し、記憶に記録される新しい情報が減少するから。"),
                ("C", "睡眠時間が極端に短くなり、意識が朦朧としている時間が増えるから。"),
                ("D", "人間関係のストレスによって、過去の記憶が完全に消去されてしまうから。")
            ],
            "B",
            "Đoạn 3 giải thích: Cuộc sống người lớn bị thói quen lặp lại (ルーティンの連続) chi phối, não vận hành chế độ tiết kiệm năng lượng nên thông tin mới lưu vào bộ nhớ giảm sút nghiêm trọng, tạo ảo giác thời gian trôi vèo.",
            {
                "A": "Không phải do não bộ xử lý nhanh như siêu máy tính.",
                "C": "Bài không đề cập tới thiếu ngủ.",
                "D": "Không phải ký ức bị xóa bỏ do căng thẳng quan hệ."
            }
        ),
        (
            "N2_02_M11_06",
            "筆者が最後に提案している「時間を豊かに長く生きるための秘訣」は何か。",
            [
                ("A", "仕事を辞めて、子供時代と全く同じ遊びを毎日繰り返すこと。"),
                ("B", "時計を見る回数を減らし、過去の出来事を一切思い出さないこと。"),
                ("C", "大人になっても新しい挑戦を続け、未知の体験を日常に取り入れること。"),
                ("D", "すべての行動を完璧に自動化し、脳を休ませ続けること。")
            ],
            "C",
            "Câu kết của bài viết đề xuất: '意識して新しい挑戦を続け、日常に未知の体験を意図的に織り込んでいくこと' (Chủ động thử thách những điều mới mẻ và đưa trải nghiệm mới vào đời sống thường nhật).",
            {
                "A": "Không khuyên nghỉ việc hay chơi trò trẻ con.",
                "B": "Không khuyên vứt bỏ đồng hồ.",
                "D": "Tự động hóa hoàn toàn chỉ khiến thời gian trôi nhanh hơn nữa."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m11_p2_questions:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Reading",
            "typeId": "N2-RD-MEDI",
            "mondaiTitle": "Mondai 11: 中文読解 (Đọc hiểu trung văn)",
            "stem": stem,
            "contextPassage": m11_p2_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 3,
            "status": "QA_VERIFIED"
        })

    # Passage 3: リモートワークと企業文化
    m11_p3_text = """【リモートワーク時代における「雑談」の価値】
在宅勤務の普及は、通勤ストレスの解消や業務効率の向上など、多くの恩恵を労働者にもたらした。あらかじめ設定されたオンライン会議では、アジェンダに沿って無駄のない議論が行われ、時間管理の面でも高い生産性が実現されているように見える。しかし、その陰で多くの企業が直面しているのが、「組織の一体感の希薄化」と「偶発的なアイデアの枯渇」という新たな課題である。

オフィスで顔を合わせていた時代には、給湯室での立ち話や、エレベーターを待つ間の何気ない「雑談」が存在していた。業務とは直接関係のない天気の話題や個人的な趣味の共有は、一見すると非効率な時間の浪費に思えるかもしれない。しかし実は、こうした心理的安全性を生み出す余白こそが、同僚への信頼関係の土台を築き、部署の垣根を越えた相談を容易にしていたのである。

また、予期せぬイノベーションの多くは、会議室の厳格な議論からではなく、雑談の中で発せられたふとした一言から着想を得ていることが多い。完全な効率性を追求するあまり、業務上の必要連絡だけにコミュニケーションを絞り込んでしまえば、組織の創造性は次第に失われていく。リモートワーク全盛の今だからこそ、企業はあえて「計画された無駄」としての雑談の場を意識的に設計する必要がある。"""

    m11_p3_questions = [
        (
            "N2_02_M11_07",
            "オンライン会議の普及によって生じた課題として、筆者が挙げているものはどれか。",
            [
                ("A", "通勤時間が長くなり、従業員の体力が激しく消耗すること。"),
                ("B", "アジェンダの設定が難しく、会議の時間が何倍にも長引くこと。"),
                ("C", "組織の一体感が薄れ、偶発的な新しいアイデアが生まれにくくなったこと。"),
                ("D", "通信費が高騰し、企業の経営利益が完全に失われたこと。")
            ],
            "C",
            "Đoạn 1 chỉ ra 2 vấn đề lớn: '組織の一体感の希薄化' (gắn kết tổ chức mờ nhạt) và '偶発的なアイデアの枯渇' (cạn kiệt những ý tưởng sáng tạo tình cờ).",
            {
                "A": "Ngược lại, làm việc tại nhà giúp xóa bỏ áp lực đi lại (通勤ストレスの解消).",
                "B": "Online meeting thảo luận bám sát chương trình nghị sự rất gọn gàng, không kéo dài.",
                "D": "Không đề cập đến việc phá sản vì tiền cước internet."
            }
        ),
        (
            "N2_02_M11_08",
            "オフィスでの「雑談」が果たしていた重要な役割は何だったか。",
            [
                ("A", "仕事の手を抜いて、勤務時間中にサボるための口実を提供すること。"),
                ("B", "信頼関係の土台を築き、創造的な着想を生み出すきっかけになること。"),
                ("C", "他人のプライベートな秘密を暴き、社内での競争を有利に進めること。"),
                ("D", "会議室の利用料を節約するために、廊下で重要な契約を結ぶこと。")
            ],
            "B",
            "Đoạn 2 & 3 phân tích: Tán gẫu tạo ra tâm lý thoải mái an tâm, xây dựng lòng tin đồng nghiệp và nảy sinh những ý tưởng đổi mới sáng tạo bất ngờ.",
            {
                "A": "Tác giả chỉ ra tuy nhìn ngoài tưởng lãng phí thời gian nhưng thực chất có giá trị cốt lõi, không phải trốn việc.",
                "C": "Không phải để soi mói đời tư đấu đá lẫn nhau.",
                "D": "Không phải để tiết kiệm tiền thuê phòng họp."
            }
        ),
        (
            "N2_02_M11_09",
            "筆者が企業に対して最も求めている提言は何か。",
            [
                ("A", "リモートワークを全面的に廃止し、全員を強制的に出社させること。"),
                ("B", "オンライン上での無駄話を一切禁止し、監視カメラを導入すること。"),
                ("C", "業務連絡以外の会話を意識的に行える「雑談の場」を計画的に設けること。"),
                ("D", "給料を一律に減額し、その分で社内カフェを豪華に改装すること。")
            ],
            "C",
            "Câu kết luận: 'あえて「計画された無駄」としての雑談の場を意識的に設計する必要がある' (Doanh nghiệp cần chủ động thiết kế không gian cho sự tán gẫu như một khoảng lùi hữu ích có chủ đích).",
            {
                "A": "Không yêu cầu xóa sổ hoàn toàn làm việc từ xa.",
                "B": "Trái ngược hoàn toàn với tinh thần bài viết khuyến khích tán gẫu.",
                "D": "Không liên quan đến giảm lương nhân viên."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m11_p3_questions:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Reading",
            "typeId": "N2-RD-MEDI",
            "mondaiTitle": "Mondai 11: 中文読解 (Đọc hiểu trung văn)",
            "stem": stem,
            "contextPassage": m11_p3_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 3,
            "status": "QA_VERIFIED"
        })

    # =========================================================================
    # MONDAI 12: 統合理解 (Comparison / Integrated - 2 items on Text A & Text B)
    # =========================================================================
    m12_text = """【A】（経済アナリストの視点）
近年のキャッシュレス決済の急速な普及は、社会全体に計り知れない利便性と経済効果をもたらしている。現金管理に伴う輸送や警備のコストを大幅に削減できるだけでなく、購買履歴のデータ分析を通じて、消費者一人ひとりに最適化された商品提案が可能となった。スマートフォンの決済アプリひとつで完結する社会は、取引の透明性を高め、不正な脱税を防ぐ上でも極めて有効である。今後は現金支払いにこだわることなく、官民が連携して完全なキャッシュレス社会への移行を加速させるべきだ。

【B】（社会学者・消費者心理の視点）
キャッシュレス決済がもたらす利便性を否定するつもりはない。しかし、お金という物理的な実体から数値データへの移行は、私たちの金銭感覚に無視できない変容を迫っている。紙幣が財布から減っていくという身体的な痛みを伴わないため、特に若年層や高齢者において、自覚のないまま過度な消費に陥るリスクが高まっている。また、災害時の大規模停電や通信障害が発生した際、デジタル決済だけに依存する脆弱性は深刻である。効率性のみを追求するのではなく、現金というフェイルセーフ（安全装置）の重要性を再認識すべきである。"""

    m12_questions = [
        (
            "N2_02_M12_01",
            "キャッシュレス決済について、AとBの共通する認識はどれか。",
            [
                ("A", "キャッシュレス決済は社会に利便性をもたらしているという点。"),
                ("B", "現金支払いは完全に廃止し、法律で禁止すべきだという点。"),
                ("C", "スマートフォンの決済は消費者の浪費を激増させるという点。"),
                ("D", "災害時にもデジタル決済は100％安全に機能するという点。")
            ],
            "A",
            "Cả A ('計り知れない利便性をもたらしている') và B ('利便性を否定するつもりはない') đều thừa nhận thanh toán không tiền mặt mang lại sự tiện lợi to lớn cho xã hội.",
            {
                "B": "Chỉ có A kêu gọi chuyển đổi hoàn toàn, B muốn giữ tiền mặt làm chốt chặn an toàn.",
                "C": "Chỉ có B cảnh báo về nguy cơ tiêu xài quá đà không kiểm soát.",
                "D": "B chỉ ra khi mất điện thảm họa thì thanh toán số rất mong manh dễ vỡ."
            }
        ),
        (
            "N2_02_M12_02",
            "完全なキャッシュレス化への移行について、AとBの主張の違いとして最も適切なものはどれか。",
            [
                ("A", "Aは治安悪化を恐れているが、Bは犯罪防止になると歓迎している。"),
                ("B", "Aは完全な移行を加速すべきだと主張し、Bは現金の安全装置としての役割を残すべきだと慎重である。"),
                ("C", "Aは若者の消費を抑えたいと考え、Bは高齢者の利便性向上だけを願っている。"),
                ("D", "Aは現金の輸送コストを増やすべきだと考え、Bは通信網の完全停止を望んでいる。")
            ],
            "B",
            "A ủng hộ đẩy nhanh chuyển đổi toàn diện sang xã hội không tiền mặt; trong khi B cẩn trọng nhắc nhở vai trò thiết yếu của tiền mặt như một chốt chặn an toàn khi thảm họa hoặc kiểm soát tâm lý tiêu dùng.",
            {
                "A": "A nói thanh toán số giúp minh bạch ngăn trốn thuế, không hề nói sợ mất an ninh.",
                "C": "Không phản ánh đúng trọng tâm so sánh hai bài.",
                "D": "Hoàn toàn sai lệch ý tứ của các tác giả."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m12_questions:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Reading",
            "typeId": "N2-RD-INTE",
            "mondaiTitle": "Mondai 12: 統合理解 (Đọc hiểu so sánh A & B)",
            "stem": stem,
            "contextPassage": m12_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 3,
            "status": "QA_VERIFIED"
        })

    # =========================================================================
    # MONDAI 13: 長文読解 (Long Reading - 1 passage x 3 items = 3 items)
    # =========================================================================
    m13_text = """【「弱さ」を認め合う組織の強靭さ】
近代以降の組織論は、長らく「強さ」と「無謬性（むびゅうせい：過ちを犯さないこと）」を至上命題として掲げてきた。リーダーは常に揺るぎない確信を持ち、部下は弱音を吐かずに与えられた目標を達成する――。このような軍隊的な規律と効率至上主義は、工業化社会において一定の成果を収めたことは確かである。あらかじめ正解が分かっている時代には、指示通りに迅速に動く機械のような組織が最も強かったからだ。

しかし、VUCA（変動性、不確実性、複雑性、曖昧性）と呼ばれる現代の予測困難な社会において、かつての「強固な組織」は脆さを露呈し始めている。失敗や弱みを隠蔽する風土は、重大な不正や事故の温床となり、現場からの率直な警鐘を上層部が握りつぶしてしまう事態を招く。完璧さを装うことへのプレッシャーが、組織の柔軟な学習能力を奪ってしまうのである。

近年、世界的な先進企業が相次いで導入しているのが、「心理的安全性」と「脆弱性（バルネラビリティ）の受容」を核とした組織開発である。ここで言う脆弱性とは、単なる能力不足を意味するのではない。自分の知識の限界を認め、「分からない」「助けてほしい」と率直に口にできる勇気のことである。

リーダーが自らの不完全さを隠さず、率直に支援を求める姿を見せるとき、チームのメンバーもまた、失敗への恐怖から解放され、前例のない革新的な挑戦に踏み出すことができる。互いの弱さを補い合い、異なる専門性を掛け合わせる関係性こそが、予測不可能な環境変化を乗り越える「真のレジリエンス（回復力・強靭さ）」を生み出すのだ。自己防衛のための強さを手放し、互いの不完全さを認め合うこと。逆説的ではあるが、そこにこそ未来の組織の持続可能な強さが宿っているのである。"""

    m13_questions = [
        (
            "N2_02_M13_01",
            "工業化社会において「強固な組織」が成果を収められたのはなぜか。",
            [
                ("A", "リーダーが常に弱音を吐き、部下に指示を仰いでいたから。"),
                ("B", "あらかじめ正解が決まっており、指示通りに動く規律と効率が有効だったから。"),
                ("C", "失敗を隠蔽することが法的に奨励されていたから。"),
                ("D", "社員全員が専門知識を持たず、機械の操作だけに専念できたから。")
            ],
            "B",
            "Đoạn 1 nêu rõ: Trong xã hội công nghiệp hóa khi đáp án đúng đã được định sẵn, một tổ chức kỷ luật thép vận hành nhanh chóng như cỗ máy là mô hình hiệu quả nhất.",
            {
                "A": "Thời đó lãnh đạo không được phép để lộ sự yếu đuối.",
                "C": "Pháp luật không bao giờ khuyến khích che giấu sai phạm.",
                "D": "Không phản ánh đúng nguyên nhân tác giả nêu."
            }
        ),
        (
            "N2_02_M13_02",
            "本文における「脆弱性の受容」とは、具体的にどのような行動を指すか。",
            [
                ("A", "自分の知識の限界を認め、率直に助けを求めたり分からないと言えたりすること。"),
                ("B", "仕事の納期を破っても悪びれず、他人のせいにして開き直ること。"),
                ("C", "チームの機密情報を競合他社に漏洩させて、会社の弱みを暴くこと。"),
                ("D", "失敗した部下を厳しく叱責し、完璧になるまで徹夜で働かせること。")
            ],
            "A",
            "Đoạn 3 định nghĩa rõ ràng: Chấp nhận sự dễ tổn thương (脆弱性の受容) là dũng cảm thừa nhận giới hạn kiến thức bản thân, dám nói 'tôi không biết' và 'xin hãy giúp đỡ tôi'.",
            {
                "B": "Đây là hành vi vô trách nhiệm, tác giả không cổ vũ việc này.",
                "C": "Đây là hành vi vi phạm pháp luật rò rỉ dữ liệu.",
                "D": "Đây chính là kiểu quản lý sai lầm của mô hình cũ bị phê phán."
            }
        ),
        (
            "N2_02_M13_03",
            "この文章全体を通じて、筆者が現代の組織において最も重要だと主張している結論は何か。",
            [
                ("A", "完璧さを装って弱さを隠し続けるリーダーこそが、最も部下に信頼される。"),
                ("B", "予測困難な時代を乗り越えるには、互いの不完全さを認め合い補い合う関係性が不可欠だ。"),
                ("C", "軍隊のような厳しい規律を現代のオフィスにも完全に復活させるべきだ。"),
                ("D", "チームワークよりも個人の突出した能力を競わせることが唯一の正解だ。")
            ],
            "B",
            "Đoạn kết khẳng định nghịch lý: Buông bỏ lớp vỏ bọc hoàn hảo phòng thủ, công nhận sự bất toàn của nhau để cùng bù đắp chuyên môn mới là nguồn gốc của sự kiên cường bền vững thực sự trong thời đại biến động.",
            {
                "A": "Ngược lại, tác giả chỉ ra việc giả vờ hoàn hảo sẽ tước đi khả năng học hỏi và sáng tạo.",
                "C": "Mô hình kỷ luật quân đội đã bộc lộ sự mong manh dễ vỡ trong thời đại VUCA.",
                "D": "Tác giả đề cao sức mạnh hợp tác bổ khuyết lẫn nhau chứ không phải chủ nghĩa anh hùng cá nhân đơn độc."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m13_questions:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Reading",
            "typeId": "N2-RD-LONG",
            "mondaiTitle": "Mondai 13: 長文読解 (Đọc hiểu trường văn)",
            "stem": stem,
            "contextPassage": m13_text,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 3,
            "status": "QA_VERIFIED"
        })

    # =========================================================================
    # MONDAI 14: 情報検索 (Information Retrieval - 1 notice x 2 items = 2 items)
    # =========================================================================
    m14_notice = """【令和8年度 地域中小企業「DX推進補助金」公募案内】

本制度は、市内の中小企業がデジタル技術（ITツール、クラウドシステム、AI等）を導入し、業務効率化や新ビジネス創出を図る経費の一部を支援するものです。

■ 補助対象者：
市内に本社を有し、1年以上継続して事業を営んでいる中小企業者（製造業、飲食・小売業、サービス業等）。
※ 市税の滞納がある場合、または過去2年以内に本補助金を受給した企業は対象外。

■ 補助コースと支援内容：
【一般枠】
・対象経費：会計・受発注ソフト導入、テレワーク環境整備
・補助率：対象経費の 1/2 以内
・補助上限額：50万円（下限額：10万円）

【高度DX枠】
・対象経費：AI画像認識による検品自動化、IoTセンサーによる生産管理
・補助率：対象経費の 2/3 以内
・補助上限額：200万円（下限額：50万円）
※ 高度DX枠の申請には、専門家（ITコーディネーター等）による事業計画の事前確認書が必須。

■ 申請期間：
令和8年5月1日（金）〜 6月15日（月）17:00必着
※ 専用のオンラインポータルサイトより電子申請のみ受付（郵送・持参は不可）。

■ 採択発表：令和8年7月下旬予定"""

    m14_questions = [
        (
            "N2_02_M14_01",
            "この補助金について、申請条件に合致する企業はどれか。",
            [
                ("A", "市外に本社があるが、市内に支店を置く創業3年目のIT企業。"),
                ("B", "市内に本社があり、3年間事業を営んでいて市税の滞納がない製造業者。"),
                ("C", "市内に本社があるが、昨年度すでに本補助金を50万円受給した飲食店。"),
                ("D", "市内に本社があり、先月新しく創業したばかりの小売業者。")
            ],
            "B",
            "Tiêu chuẩn quy định: '市内に本社を有し、1年以上継続して事業を営んでいる... 市税の滞納がない' (Trụ sở chính trong thành phố, kinh doanh liên tục trên 1 năm, không nợ thuế thành phố). Doanh nghiệp B đáp ứng hoàn hảo.",
            {
                "A": "Trụ sở chính ở ngoài thành phố là không đủ điều kiện (市内に本社を有し).",
                "C": "Đã nhận trợ cấp năm ngoái vi phạm điều kiện loại trừ: '過去2年以内に本補助金を受給した企業は対象外'.",
                "D": "Mới thành lập tháng trước chưa đủ điều kiện 1 năm kinh doanh liên tục."
            }
        ),
        (
            "N2_02_M14_02",
            "工場で「AI画像認識による検品自動化システム」を総額240万円で導入したい場合、申請方法と補助額の上限はどうなるか。",
            [
                ("A", "【一般枠】で郵送申請し、上限50万円の補助を受ける。"),
                ("B", "【高度DX枠】で専門家の事前確認書を添えて電子申請し、上限160万円（240万の2/3）の補助を受ける。"),
                ("C", "【高度DX枠】で書類を持参して窓口申請し、一律200万円の補助を受ける。"),
                ("D", "【一般枠】で電子申請し、総額の全額である240万円の補助を受ける。")
            ],
            "B",
            "Hệ thống kiểm tra tự động bằng AI thuộc 【高度DX枠】 (tỷ lệ 2/3, 240万 x 2/3 = 160万円, nằm dưới mức trần 200万円). Bắt buộc phải có bản xác nhận của chuyên gia IT và chỉ nộp qua cổng điện tử trực tuyến (電子申請).",
            {
                "A": "AI kiểm tra sản phẩm thuộc Khung DX nâng cao, và không nhận nộp qua bưu điện (郵送不可).",
                "C": "Không nhận nộp trực tiếp tại quầy (持参不可), và số tiền trợ cấp tính theo tỷ lệ 2/3 chứ không nhận tròn 200 triệu cố định.",
                "D": "Không có chương trình nào trợ cấp 100% toàn bộ 240 vạn yên."
            }
        )
    ]

    for qid, stem, opts, ans, exp, dist in m14_questions:
        items.append({
            "id": qid,
            "level": "N2",
            "skill": "Reading",
            "typeId": "N2-RD-INFO",
            "mondaiTitle": "Mondai 14: 情報検索 (Tra cứu thông tin)",
            "stem": stem,
            "contextPassage": m14_notice,
            "options": [{"id": o[0], "text": o[1]} for o in opts],
            "correctAnswer": ans,
            "explanationVi": exp,
            "distractorExplanations": dist,
            "difficultyEstimate": 2,
            "status": "QA_VERIFIED"
        })

    return items
