# -*- coding: utf-8 -*-
"""
JLPT N2 Mock Exam #07 - Section 1: Language Knowledge & Reading (言語知識・読解)
Thematic emphasis: Daily life, public services, workplace communication (生活・行政・職場実務).
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
Answer distribution: A: 19, B: 19, C: 19, D: 18 (Max letter ratio: 0.253 <= 0.38).
"""

def get_n2_mock_07_sec1_items():
    return [
  {
    "id": "N2_07_M1_01",
    "typeId": "N2-MO-READ",
    "category": "Mondai 1: 漢字読み",
    "stem": "市役所の窓口で住民票の【交付】を申請した。",
    "targetWord": "交付",
    "options": [
      {
        "id": "A",
        "text": "こうふ"
      },
      {
        "id": "B",
        "text": "こうぶ"
      },
      {
        "id": "C",
        "text": "ごうふ"
      },
      {
        "id": "D",
        "text": "きょうふ"
      }
    ],
    "correctAnswer": "A",
    "explanation": "交付（こうふ - GIAO PHÓ）: Sự cấp phát, cấp giấy tờ chính thức. Chữ 交 có âm on là こう, 付 có âm on là ふ.",
    "distractorExplanations": {
      "B": "こうぶ: Sai âm ふ thành đục ぶ.",
      "C": "ごうふ: Sai âm こう thành đục ごう.",
      "D": "きょうふ: Nhầm với 恐怖 (きょうふ - khủng bố/sợ hãi)."
    }
  },
  {
    "id": "N2_07_M1_02",
    "typeId": "N2-MO-READ",
    "category": "Mondai 1: 漢字読み",
    "stem": "公共施設を利用する際は、利用規程を厳格に【遵守】してください。",
    "targetWord": "遵守",
    "options": [
      {
        "id": "A",
        "text": "そんしゅ"
      },
      {
        "id": "B",
        "text": "じゅんしゅ"
      },
      {
        "id": "C",
        "text": "じゅんす"
      },
      {
        "id": "D",
        "text": "しょうしゅ"
      }
    ],
    "correctAnswer": "B",
    "explanation": "遵守（じゅんしゅ - TUÂN THỦ）: Tuân thủ nghiêm ngặt quy định, pháp luật. Chữ 遵 đọc là じゅん, 守 đọc là しゅ.",
    "distractorExplanations": {
      "A": "そんしゅ: Nhầm chữ 遵 với 尊 (Tôn trong 尊重 そんちょう).",
      "C": "じゅんす: Sai âm しゅ thành す.",
      "D": "しょうしゅ: Sai âm じゅん thành しょう."
    }
  },
  {
    "id": "N2_07_M1_03",
    "typeId": "N2-MO-READ",
    "category": "Mondai 1: 漢字読み",
    "stem": "市民税の【滞納】が続くと、督促状が届く恐れがある。",
    "targetWord": "滞納",
    "options": [
      {
        "id": "A",
        "text": "ていのう"
      },
      {
        "id": "B",
        "text": "ちのう"
      },
      {
        "id": "C",
        "text": "たいのう"
      },
      {
        "id": "D",
        "text": "たいいれ"
      }
    ],
    "correctAnswer": "C",
    "explanation": "滞納（たいのう - TRỆ NẠP）: Chậm nộp, nợ đọng tiền thuế, tiền cước. 滞 có âm on là たい, 納 có âm on là のう.",
    "distractorExplanations": {
      "A": "ていのう: Sai âm たい thành てい.",
      "B": "ちのう: Nhầm chữ 滞 với 遅 (ち) hoặc âm khác.",
      "D": "たいいれ: Nhầm âm on のう với âm kun い・れる."
    }
  },
  {
    "id": "N2_07_M1_04",
    "typeId": "N2-MO-READ",
    "category": "Mondai 1: 漢字読み",
    "stem": "年末調整の書類を提出して、配偶者【控除】の適用を受けた。",
    "targetWord": "控除",
    "options": [
      {
        "id": "A",
        "text": "こうしょ"
      },
      {
        "id": "B",
        "text": "くじょ"
      },
      {
        "id": "C",
        "text": "きょうじょ"
      },
      {
        "id": "D",
        "text": "こうじょ"
      }
    ],
    "correctAnswer": "D",
    "explanation": "控除（こうじょ - KHỐNG TRỪ）: Khấu trừ (thuế, thu nhập). Chữ 控 có âm on là こう, 除 có âm on là じょ.",
    "distractorExplanations": {
      "A": "こうしょ: Sai âm じょ thành âm thanh しょ.",
      "B": "くじょ: Nhầm với 駆除 (くじょ - tiêu diệt, trừ khử côn trùng).",
      "C": "きょうじょ: Nhầm với 協約 hoặc 援助."
    }
  },
  {
    "id": "N2_07_M1_05",
    "typeId": "N2-MO-READ",
    "category": "Mondai 1: 漢字読み",
    "stem": "大型家具の【廃棄】処分には、事前の有料申し込みが必要です。",
    "targetWord": "廃棄",
    "options": [
      {
        "id": "A",
        "text": "はいき"
      },
      {
        "id": "B",
        "text": "はっき"
      },
      {
        "id": "C",
        "text": "はいし"
      },
      {
        "id": "D",
        "text": "ほうき"
      }
    ],
    "correctAnswer": "A",
    "explanation": "廃棄（はいき - PHẾ KHÍ）: Vứt bỏ, xử lý rác thải lớn, phế thải. Chữ 廃 đọc là はい, 棄 đọc là き.",
    "distractorExplanations": {
      "B": "はっき: Nhầm sang 発揮 (はっき - phát huy) hoặc 破棄 (はき).",
      "C": "はいし: Nhầm với 廃止 (はいし - bãi bỏ).",
      "D": "ほうき: Nhầm với 放棄 (ほうき - từ bỏ, vứt bỏ trách nhiệm)."
    }
  },
  {
    "id": "N2_07_M2_01",
    "typeId": "N2-MO-ORTH",
    "category": "Mondai 2: 表記",
    "stem": "出張で発生した交通費の【けいひ】を速やかに精算した。",
    "targetWord": "けいひ",
    "options": [
      {
        "id": "A",
        "text": "軽費"
      },
      {
        "id": "B",
        "text": "経費"
      },
      {
        "id": "C",
        "text": "係費"
      },
      {
        "id": "D",
        "text": "啓費"
      }
    ],
    "correctAnswer": "B",
    "explanation": "経費（けいひ - KINH PHÍ）: Chi phí, kinh phí công tác.",
    "distractorExplanations": {
      "A": "軽費: Chữ 軽 nghĩa là nhẹ, không dùng trong kinh phí.",
      "C": "係費: Chữ 係 là liên quan/phụ trách.",
      "D": "啓費: Chữ 啓 là khai sáng/khởi đầu."
    }
  },
  {
    "id": "N2_07_M2_02",
    "typeId": "N2-MO-ORTH",
    "category": "Mondai 2: 表記",
    "stem": "内部監査で指摘された事務の不備について、直ちに【ぜせい】措置を講じた。",
    "targetWord": "ぜせい",
    "options": [
      {
        "id": "A",
        "text": "善正"
      },
      {
        "id": "B",
        "text": "是政"
      },
      {
        "id": "C",
        "text": "是正"
      },
      {
        "id": "D",
        "text": "善制"
      }
    ],
    "correctAnswer": "C",
    "explanation": "是正（ぜせい - THỊ CHÍNH）: Sự sửa đổi, chấn chỉnh cho đúng đắn (điều chỉnh khuyết điểm, sai lệch).",
    "distractorExplanations": {
      "A": "善正: Chữ kanji không tạo thành từ này.",
      "B": "是政: Chữ 政 là chính quyền/chính trị, sai chữ 正.",
      "D": "善制: Chữ 制 là chế độ/kiểm soát."
    }
  },
  {
    "id": "N2_07_M2_03",
    "typeId": "N2-MO-ORTH",
    "category": "Mondai 2: 表記",
    "stem": "本人が来庁できない場合、正式な書類によって代理人に手続きを【いにん】できる。",
    "targetWord": "いにん",
    "options": [
      {
        "id": "A",
        "text": "依任"
      },
      {
        "id": "B",
        "text": "頼任"
      },
      {
        "id": "C",
        "text": "託任"
      },
      {
        "id": "D",
        "text": "委任"
      }
    ],
    "correctAnswer": "D",
    "explanation": "委任（いにん - ỦY NHIỆM）: Ủy nhiệm, ủy quyền làm thủ tục hành chính.",
    "distractorExplanations": {
      "A": "依任: Nhầm chữ 依 (y/phụ thuộc).",
      "B": "頼任: Chữ 頼 (lại/nhờ cậy) không ghép thành từ này.",
      "C": "託任: Nhầm sang 託 (thác/giao phó)."
    }
  },
  {
    "id": "N2_07_M2_04",
    "typeId": "N2-MO-ORTH",
    "category": "Mondai 2: 表記",
    "stem": "業務委託契約書の【じょうこう】を一つずつ慎重に確認した。",
    "targetWord": "じょうこう",
    "options": [
      {
        "id": "A",
        "text": "条項"
      },
      {
        "id": "B",
        "text": "条厚"
      },
      {
        "id": "C",
        "text": "状項"
      },
      {
        "id": "D",
        "text": "錠項"
      }
    ],
    "correctAnswer": "A",
    "explanation": "条項（じょうこう - ĐIỀU KHOẢN）: Các điều khoản trong hợp đồng, văn bản quy phạm.",
    "distractorExplanations": {
      "B": "条厚: Chữ 厚 nghĩa là dày, sai chữ 項.",
      "C": "状項: Chữ 状 nghĩa là tình trạng/hình dáng.",
      "D": "錠項: Chữ 錠 nghĩa là ổ khóa/viên thuốc."
    }
  },
  {
    "id": "N2_07_M2_05",
    "typeId": "N2-MO-ORTH",
    "category": "Mondai 2: 表記",
    "stem": "引っ越しの際は、管轄の郵便局へ転居届を速やかに【ていしゅつ】してください。",
    "targetWord": "ていしゅつ",
    "options": [
      {
        "id": "A",
        "text": "提述"
      },
      {
        "id": "B",
        "text": "提出"
      },
      {
        "id": "C",
        "text": "定出"
      },
      {
        "id": "D",
        "text": "提進"
      }
    ],
    "correctAnswer": "B",
    "explanation": "提出（ていしゅつ - ĐỀ XUẤT/NỘP）: Nộp đơn từ, trình giấy tờ lên cơ quan có thẩm quyền.",
    "distractorExplanations": {
      "A": "提述: Chữ 述 là thuật/kể lại, sai nghĩa.",
      "C": "定出: Sai chữ 提 thành 定.",
      "D": "提進: Chữ 進 là tiến lên, không ghép thành từ này."
    }
  },
  {
    "id": "N2_07_M3_01",
    "typeId": "N2-MO-FORM",
    "category": "Mondai 3: 語形成",
    "stem": "紛失した身分証の【（　）発行】を窓口で申請した。",
    "targetWord": "再発行",
    "options": [
      {
        "id": "A",
        "text": "復"
      },
      {
        "id": "B",
        "text": "新"
      },
      {
        "id": "C",
        "text": "再"
      },
      {
        "id": "D",
        "text": "重"
      }
    ],
    "correctAnswer": "C",
    "explanation": "再発行（さいはっこう - TÁI PHÁT HÀNH）: Cấp lại, phát hành lại giấy tờ khi bị mất. Tiền tố 再- (tái).",
    "distractorExplanations": {
      "A": "復: Dùng trong 復旧, 復活, không ghép thành *復発行.",
      "B": "新: Dùng trong 新発行 (phát hành mới), không mang nghĩa làm lại do mất.",
      "D": "重: Dùng trong 重複, 重大, không ghép thành *重発行."
    }
  },
  {
    "id": "N2_07_M3_02",
    "typeId": "N2-MO-FORM",
    "category": "Mondai 3: 語形成",
    "stem": "会社の設立にあたっては、登記や納税など【諸（　）】を同時に進める必要がある。",
    "targetWord": "諸手続",
    "options": [
      {
        "id": "A",
        "text": "経費"
      },
      {
        "id": "B",
        "text": "規程"
      },
      {
        "id": "C",
        "text": "申請"
      },
      {
        "id": "D",
        "text": "手続"
      }
    ],
    "correctAnswer": "D",
    "explanation": "諸手続（しょてつづき - CHƯ THỦ TỤC）: Các loại thủ tục, nhiều thủ tục hành chính khác nhau. Tiền tố 諸- (chư) ghép với 手続.",
    "distractorExplanations": {
      "A": "経費: Thường dùng 諸経費 (các khoản kinh phí), nhưng văn cảnh ở đây là đăng ký và nộp thuế nên là các thủ tục.",
      "B": "規程: Thường dùng 諸規程 ít dùng trong chuỗi hành động hành chính cá nhân.",
      "C": "申請: Thường ghép 諸申請 ít thông dụng hơn cụm cố định chuẩn 諸手続."
    }
  },
  {
    "id": "N2_07_M3_03",
    "typeId": "N2-MO-FORM",
    "category": "Mondai 3: 語形成",
    "stem": "国民年金に【（　）納】期間があると、将来受け取れる年金額が減額される。",
    "targetWord": "未納",
    "options": [
      {
        "id": "A",
        "text": "未"
      },
      {
        "id": "B",
        "text": "不"
      },
      {
        "id": "C",
        "text": "非"
      },
      {
        "id": "D",
        "text": "無"
      }
    ],
    "correctAnswer": "A",
    "explanation": "未納（みのう - VỊ NẠP）: Chưa nộp, còn nợ đọng chưa thanh toán. Tiền tố 未- (chưa).",
    "distractorExplanations": {
      "B": "不: Biểu thị bất/không (bất an, bất tiện: 不安, 不便, 不払い). Không dùng *不納.",
      "C": "非: Biểu thị tính phi (phi lý, phi pháp: 非難, 非常).",
      "D": "無: Biểu thị vô/không có (vô lý, vô hiệu: 無理, 無効). Không dùng *無納."
    }
  },
  {
    "id": "N2_07_M3_04",
    "typeId": "N2-MO-FORM",
    "category": "Mondai 3: 語形成",
    "stem": "転勤に伴い、来月からの新しい【勤務（　）】へ引っ越す準備を進めている。",
    "targetWord": "勤務地",
    "options": [
      {
        "id": "A",
        "text": "所"
      },
      {
        "id": "B",
        "text": "地"
      },
      {
        "id": "C",
        "text": "処"
      },
      {
        "id": "D",
        "text": "場"
      }
    ],
    "correctAnswer": "B",
    "explanation": "勤務地（きんむち - CẦN VỤ ĐỊA）: Nơi làm việc, địa điểm công tác. Hậu tố -地 (vùng, địa điểm).",
    "distractorExplanations": {
      "A": "所: Ghép thành 勤務先 (きんむさき) hoặc 事務所 (じむしょ), không dùng *勤務所.",
      "C": "処: Không dùng làm hậu tố cho từ này.",
      "D": "場: Dùng trong 職場 (nơi làm việc) hoặc 勤務場所, hậu tố độc lập chuẩn danh mục công chức là 勤務地."
    }
  },
  {
    "id": "N2_07_M3_05",
    "typeId": "N2-MO-FORM",
    "category": "Mondai 3: 語形成",
    "stem": "市役所では環境負荷を低減するため、【（　）効率】な照明器具への更新を進めている。",
    "targetWord": "高効率",
    "options": [
      {
        "id": "A",
        "text": "強"
      },
      {
        "id": "B",
        "text": "上"
      },
      {
        "id": "C",
        "text": "高"
      },
      {
        "id": "D",
        "text": "超"
      }
    ],
    "correctAnswer": "C",
    "explanation": "高効率（こうこうりつ - CAO HIỆU SUẤT）: Hiệu suất cao, tiết kiệm năng lượng. Tiền tố 高- (cao).",
    "distractorExplanations": {
      "A": "強: Dùng trong 強力, 強度, không ghép với 効率.",
      "B": "上: Không dùng tiền tố 上効率.",
      "D": "超: Biểu thị siêu (siêu việt, siêu âm: 超音波, 超満員). Cụm tiêu chuẩn kỹ thuật là 高効率."
    }
  },
  {
    "id": "N2_07_M4_01",
    "typeId": "N2-MO-CONT",
    "category": "Mondai 4: 文脈規定",
    "stem": "住民からの問い合わせに対して、職員が（　）な対応を心がけている。",
    "targetWord": "迅速",
    "options": [
      {
        "id": "A",
        "text": "窮屈"
      },
      {
        "id": "B",
        "text": "頑固"
      },
      {
        "id": "C",
        "text": "几帳面"
      },
      {
        "id": "D",
        "text": "迅速"
      }
    ],
    "correctAnswer": "D",
    "explanation": "迅速（じんそく - TẤN TỐC）: Nhanh chóng, mau lẹ trong xử lý nghiệp vụ.",
    "distractorExplanations": {
      "A": "窮屈: Chật chội, gò bó, không thoải mái.",
      "B": "頑固: Cố chấp, bướng bỉnh.",
      "C": "几帳面: Cẩn thận, ngăn nắp (thường nói về tính cách con người, không ghép tự nhiên với な対応 bằng 迅速)."
    }
  },
  {
    "id": "N2_07_M4_02",
    "typeId": "N2-MO-CONT",
    "category": "Mondai 4: 文脈規定",
    "stem": "事務処理の（　）により、別の住民の方へ案内通知が誤送されてしまった。",
    "targetWord": "手違い",
    "options": [
      {
        "id": "A",
        "text": "手違い"
      },
      {
        "id": "B",
        "text": "手間"
      },
      {
        "id": "C",
        "text": "手配"
      },
      {
        "id": "D",
        "text": "手品"
      }
    ],
    "correctAnswer": "A",
    "explanation": "手違い（てちがい）: Sự nhầm lẫn, sai sót trong quá trình xử lý công việc hành chính.",
    "distractorExplanations": {
      "B": "手間: Công sức, thời gian bỏ ra.",
      "C": "手配: Sự sắp xếp, chuẩn bị phương tiện/nhân lực.",
      "D": "手品: Trò ảo thuật."
    }
  },
  {
    "id": "N2_07_M4_03",
    "typeId": "N2-MO-CONT",
    "category": "Mondai 4: 文脈規定",
    "stem": "業務の遅れが生じないよう、関係部署と密に連絡を（　）必要がある。",
    "targetWord": "取り合う",
    "options": [
      {
        "id": "A",
        "text": "取り持つ"
      },
      {
        "id": "B",
        "text": "取り合う"
      },
      {
        "id": "C",
        "text": "取り入れる"
      },
      {
        "id": "D",
        "text": "取り組む"
      }
    ],
    "correctAnswer": "B",
    "explanation": "連絡を取り合う: Giữ liên lạc chặt chẽ hai chiều với nhau.",
    "distractorExplanations": {
      "A": "取り持つ: Làm trung gian hòa giải.",
      "C": "取り入れる: Tiếp thu, áp dụng ý kiến.",
      "D": "取り組む: Nỗ lực, bắt tay vào giải quyết vấn đề."
    }
  },
  {
    "id": "N2_07_M4_04",
    "typeId": "N2-MO-CONT",
    "category": "Mondai 4: 文脈規定",
    "stem": "もし面談の日程にご（　）がございましたら、遠慮なくお知らせください。",
    "targetWord": "差し支え",
    "options": [
      {
        "id": "A",
        "text": "邪魔"
      },
      {
        "id": "B",
        "text": "お構い"
      },
      {
        "id": "C",
        "text": "差し支え"
      },
      {
        "id": "D",
        "text": "迷惑"
      }
    ],
    "correctAnswer": "C",
    "explanation": "差し支え（さしつかえ）: Trở ngại, bất tiện về thời gian biểu. Mẫu lịch sự: ご差し支えがございましたら (Nếu có gì bất tiện/bận).",
    "distractorExplanations": {
      "A": "邪魔: Làm phiền, cản trở.",
      "B": "お構い: Bận tâm, chăm sóc (như trong お構いなく).",
      "D": "迷惑: Sự phiền toái; trong kính ngữ thường dùng ご都合 hoặc ご差し支え."
    }
  },
  {
    "id": "N2_07_M4_05",
    "typeId": "N2-MO-CONT",
    "category": "Mondai 4: 文脈規定",
    "stem": "育児や介護と仕事を両立できるよう、勤務時間に（　）の利くフレックスタイム制を導入した。",
    "targetWord": "融通",
    "options": [
      {
        "id": "A",
        "text": "適応"
      },
      {
        "id": "B",
        "text": "妥協"
      },
      {
        "id": "C",
        "text": "余裕"
      },
      {
        "id": "D",
        "text": "融通"
      }
    ],
    "correctAnswer": "D",
    "explanation": "融通が利く（ゆうづうがきく）: Linh hoạt, cơ động, có thể xoay xở điều chỉnh theo tình huống.",
    "distractorExplanations": {
      "A": "適応: Thích ứng.",
      "B": "妥協: Thỏa hiệp, nhượng bộ.",
      "C": "余裕: Dư dả thời gian/tiền bạc, không đi với cụm が利く."
    }
  },
  {
    "id": "N2_07_M4_06",
    "typeId": "N2-MO-CONT",
    "category": "Mondai 4: 文脈規定",
    "stem": "通勤ラッシュを避けるため、社員ごとに始業時刻を30分ずつずらす「（　）出勤」を導入した。",
    "targetWord": "時差",
    "options": [
      {
        "id": "A",
        "text": "時差"
      },
      {
        "id": "B",
        "text": "交代"
      },
      {
        "id": "C",
        "text": "短縮"
      },
      {
        "id": "D",
        "text": "移動"
      }
    ],
    "correctAnswer": "A",
    "explanation": "時差出勤（じさしゅっきん）: Hình thức lệch giờ bắt đầu làm việc để tránh giờ cao điểm; câu này nêu rõ giờ vào làm của từng nhân viên được giãn cách.",
    "distractorExplanations": {
      "B": "交代出勤 thường chỉ việc thay phiên hoặc làm theo ca, không phải lệch giờ vào làm giữa các nhân viên.",
      "C": "短縮出勤 gợi việc rút ngắn giờ làm, không phải giãn thời điểm bắt đầu làm.",
      "D": "移動出勤 không phải cách gọi thông dụng cho lịch bắt đầu làm lệch giờ."
    }
  },
  {
    "id": "N2_07_M4_07",
    "typeId": "N2-MO-CONT",
    "category": "Mondai 4: 文脈規定",
    "stem": "高齢者や障害をお持ちの方の申請手続きを支援するため、窓口で様々な（　）を図っている。",
    "targetWord": "便宜",
    "options": [
      {
        "id": "A",
        "text": "待遇"
      },
      {
        "id": "B",
        "text": "便宜"
      },
      {
        "id": "C",
        "text": "利益"
      },
      {
        "id": "D",
        "text": "都合"
      }
    ],
    "correctAnswer": "B",
    "explanation": "便宜を図る（べんぎをはかる）: Tạo điều kiện thuận lợi, hỗ trợ tiện ích đặc biệt cho người cần giúp đỡ.",
    "distractorExplanations": {
      "A": "待遇: Đãi ngộ, chế độ lương bổng.",
      "C": "利益: Lợi nhuận kinh tế.",
      "D": "都合: Sự thuận tiện/lịch trình, không đi với cụm を図る theo nghĩa hỗ trợ dịch vụ."
    }
  },
  {
    "id": "N2_07_M5_01",
    "typeId": "N2-MO-PARA",
    "category": "Mondai 5: 言い換え類義",
    "stem": "未提出の書類について、市役所の担当課から【催促】の電話があった。",
    "targetWord": "催促",
    "options": [
      {
        "id": "A",
        "text": "受理したと知らせること"
      },
      {
        "id": "B",
        "text": "内容を詳しく説明すること"
      },
      {
        "id": "C",
        "text": "早く出すよう求めること"
      },
      {
        "id": "D",
        "text": "書き直しを命じること"
      }
    ],
    "correctAnswer": "C",
    "explanation": "催促（さいそく）: Hối thúc, yêu cầu thực hiện hoặc nộp gấp.",
    "distractorExplanations": {
      "A": "Báo đã thụ lý là 受理通知.",
      "B": "Giải thích nội dung chi tiết là 説明.",
      "D": "Yêu cầu viết lại là 修正指示."
    }
  },
  {
    "id": "N2_07_M5_02",
    "typeId": "N2-MO-PARA",
    "category": "Mondai 5: 言い換え類義",
    "stem": "午後から他部署の責任者と今後の業務方針について【打ち合わせ】を行う予定だ。",
    "targetWord": "打ち合わせ",
    "options": [
      {
        "id": "A",
        "text": "演説"
      },
      {
        "id": "B",
        "text": "雑談"
      },
      {
        "id": "C",
        "text": "審査"
      },
      {
        "id": "D",
        "text": "協議"
      }
    ],
    "correctAnswer": "D",
    "explanation": "打ち合わせ（うちあわせ）: Buổi thảo luận, trao đổi bàn bạc trước trong công việc, đồng nghĩa với 協議（きょうぎ）.",
    "distractorExplanations": {
      "A": "演説: Diễn thuyết.",
      "B": "雑談: Tán gẫu.",
      "C": "審査: Thẩm tra, xét duyệt."
    }
  },
  {
    "id": "N2_07_M5_03",
    "typeId": "N2-MO-PARA",
    "category": "Mondai 5: 言い換え類義",
    "stem": "台風の接近に伴い、本日の野外イベントの開催は【見合わせる】ことになった。",
    "targetWord": "見合わせる",
    "options": [
      {
        "id": "A",
        "text": "中止・延期する"
      },
      {
        "id": "B",
        "text": "予定通り実行する"
      },
      {
        "id": "C",
        "text": "規模を拡大する"
      },
      {
        "id": "D",
        "text": "すぐに開始する"
      }
    ],
    "correctAnswer": "A",
    "explanation": "見合わせる（みあわせる）: Tạm dừng, hoãn lại hoặc hủy bỏ do tình hình bất lợi.",
    "distractorExplanations": {
      "B": "Tiến hành đúng kế hoạch là 実行/決行.",
      "C": "Mở rộng quy mô là 拡大.",
      "D": "Bắt đầu ngay là 即時開始."
    }
  },
  {
    "id": "N2_07_M5_04",
    "typeId": "N2-MO-PARA",
    "category": "Mondai 5: 言い換え類義",
    "stem": "【念のため】、申請書を提出する前に必要な添付書類がそろっているか確かめた。",
    "targetWord": "念のため",
    "options": [
      {
        "id": "A",
        "text": "急いで処理するために"
      },
      {
        "id": "B",
        "text": "間違いがないよう確認するために"
      },
      {
        "id": "C",
        "text": "相手に強く注意を促すために"
      },
      {
        "id": "D",
        "text": "記録として残すために"
      }
    ],
    "correctAnswer": "B",
    "explanation": "念のため（ねんのため）: Làm thêm một bước xác nhận để phòng trường hợp có thiếu sót hoặc nhầm lẫn; trong câu này là kiểm tra đủ giấy tờ trước khi nộp.",
    "distractorExplanations": {
      "A": "急いで処理するために nêu tốc độ xử lý, không phải việc kiểm tra phòng ngừa.",
      "C": "相手に強く注意を促すために diễn tả nhắc nhở người khác, gần với 念を押す.",
      "D": "記録として残すために nêu mục đích lưu hồ sơ, không phải kiểm tra để phòng sai sót."
    }
  },
  {
    "id": "N2_07_M5_05",
    "typeId": "N2-MO-PARA",
    "category": "Mondai 5: 言い換え類義",
    "stem": "正式な決裁が下りるまで、【ひとまず】既存のスケジュールで準備を進めておこう。",
    "targetWord": "ひとまず",
    "options": [
      {
        "id": "A",
        "text": "永久に"
      },
      {
        "id": "B",
        "text": "決して"
      },
      {
        "id": "C",
        "text": "とりあえず"
      },
      {
        "id": "D",
        "text": "完全に完了して"
      }
    ],
    "correctAnswer": "C",
    "explanation": "ひとまず: Tạm thời, trước mắt cứ như thế đã, đồng nghĩa với とりあえず.",
    "distractorExplanations": {
      "A": "永久に: Vĩnh viễn.",
      "B": "決して: Tuyệt đối không.",
      "D": "完全に完了して: Hoàn thành triệt để."
    }
  },
  {
    "id": "N2_07_M6_01",
    "typeId": "N2-MO-USE",
    "category": "Mondai 6: 用法",
    "stem": "次の言葉の使い方が最も適切なものを一つ選びなさい。【恐縮】",
    "targetWord": "恐縮",
    "options": [
      {
        "id": "A",
        "text": "景気の悪化に伴い、会社の業績が恐縮している。"
      },
      {
        "id": "B",
        "text": "マラソン大会で優勝して、恐縮のあまり飛び上がって喜んだ。"
      },
      {
        "id": "C",
        "text": "明日の出張に向けて、部屋の荷物を恐縮にまとめた。"
      },
      {
        "id": "D",
        "text": "お忙しいところ大変恐縮ですが、アンケートへのご協力をお願い申し上げます。"
      }
    ],
    "correctAnswer": "D",
    "explanation": "恐縮（きょうしゅく - KHỦNG SÚC）: Rất áy náy, xin lỗi vì làm phiền người khác khi nhờ vả, yêu cầu trong giao tiếp kính ngữ trang trọng.",
    "distractorExplanations": {
      "A": "Công ty sa sút hoặc thu hẹp thì dùng 低迷 hoặc 縮小.",
      "B": "Vui mừng nhảy cẫng lên thì dùng 歓喜 hoặc 大喜び, không dùng 恐縮.",
      "C": "Dọn dẹp nhanh gọn thì dùng 手際よく hoặc コンパクトに."
    }
  },
  {
    "id": "N2_07_M6_02",
    "typeId": "N2-MO-USE",
    "category": "Mondai 6: 用法",
    "stem": "次の言葉の使い方が最も適切なものを一つ選びなさい。【経由】",
    "targetWord": "経由",
    "options": [
      {
        "id": "A",
        "text": "今回のヨーロッパ出張は、ドーハを経由してフランクフルトへ向かう航空便を利用する。"
      },
      {
        "id": "B",
        "text": "雨が激しく降ってきたので、傘を経由して駅まで走った。"
      },
      {
        "id": "C",
        "text": "昨晩は激しい運動をしたので、夕食後にすぐ経由した。"
      },
      {
        "id": "D",
        "text": "宿題を経由してから、友人と公園へ遊びに出かけた。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "経由（けいゆ - KINH DO）: Quá cảnh, đi qua một trạm/địa điểm trung gian để đến đích.",
    "distractorExplanations": {
      "B": "Bật ô che mưa thì dùng 傘を差して.",
      "C": "Nghỉ ngơi hoặc đi ngủ thì dùng 就寝した hoặc 休息した.",
      "D": "Làm xong bài tập thì dùng 済ませて."
    }
  },
  {
    "id": "N2_07_M6_03",
    "typeId": "N2-MO-USE",
    "category": "Mondai 6: 用法",
    "stem": "次の言葉の使い方が最も適切なものを一つ選びなさい。【負担】",
    "targetWord": "負担",
    "options": [
      {
        "id": "A",
        "text": "真冬の寒さに耐えるため、厚手のコートと手袋を負担して外出した。"
      },
      {
        "id": "B",
        "text": "新しい大型プロジェクトの統括責任者を任され、精神的な負担が重くなった。"
      },
      {
        "id": "C",
        "text": "彼はいつも面白い冗談を言って、周囲の同僚たちを負担させている。"
      },
      {
        "id": "D",
        "text": "週末の読書のために、図書館で学術書を3冊負担して帰宅した。"
      }
    ],
    "correctAnswer": "B",
    "explanation": "負担（ふたん - PHỤ ĐẢM）: Gánh vác trách nhiệm, gánh nặng tâm lý hoặc chi phí tiền bạc.",
    "distractorExplanations": {
      "A": "Mặc quần áo ấm thì dùng 着用して.",
      "C": "Làm cho đồng nghiệp cười sảng khoái thì dùng 笑わせている.",
      "D": "Mượn sách thư viện thì dùng 借りて."
    }
  },
  {
    "id": "N2_07_M6_04",
    "typeId": "N2-MO-USE",
    "category": "Mondai 6: 用法",
    "stem": "次の言葉の使い方が最も適切なものを一つ選びなさい。【配布】",
    "targetWord": "配布",
    "options": [
      {
        "id": "A",
        "text": "大雪の影響で電車のダイヤが配布し、通勤客に影響が出た。"
      },
      {
        "id": "B",
        "text": "手紙を投函する前に、記念切手を封筒の右上に配布した。"
      },
      {
        "id": "C",
        "text": "市民説明会の会場入口で、来場者全員に防災ガイドブックを配布した。"
      },
      {
        "id": "D",
        "text": "会議室のテーブルの上に、プロジェクターの電源コードを綺麗に配布した。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "配布（はいふ - PHỐI PHỐ）: Phát, phát tán tài liệu, sách báo, tờ rơi rộng rãi cho nhiều người.",
    "distractorExplanations": {
      "A": "Lịch tàu bị xáo trộn, rối loạn thì dùng 乱れ (みだれ).",
      "B": "Dán tem lên phong bì thì dùng 貼った (はった).",
      "D": "Bố trí, sắp đặt dây điện thì dùng 配線した hoặc 整頓した."
    }
  },
  {
    "id": "N2_07_M6_05",
    "typeId": "N2-MO-USE",
    "category": "Mondai 6: 用法",
    "stem": "次の言葉の使い方が最も適切なものを一つ選びなさい。【照会】",
    "targetWord": "照会",
    "options": [
      {
        "id": "A",
        "text": "夜遅くまで残業していたため、オフィスの天井の照会を暗くした。"
      },
      {
        "id": "B",
        "text": "毎朝出勤する途中、近所の知り合いと笑顔で照会を交わしている。"
      },
      {
        "id": "C",
        "text": "スープの味付けが薄かったので、塩と胡椒を照会して整えた。"
      },
      {
        "id": "D",
        "text": "給付金の受給資格を満たしているか、窓口の端末から住民台帳データに照会した。"
      }
    ],
    "correctAnswer": "D",
    "explanation": "照会（しょうかい - CHIẾU HỘI）: Tra cứu, đối chiếu thông tin trong cơ sở dữ liệu hoặc hỏi xác minh ở cơ quan chức năng.",
    "distractorExplanations": {
      "A": "Đèn chiếu sáng văn phòng là 照明 (しょうめい).",
      "B": "Chào hỏi thì dùng 挨拶 (あいさつ).",
      "C": "Gia giảm gia vị thì dùng 加減して hoặc 調節して."
    }
  },
  {
    "id": "N2_07_M7_01",
    "typeId": "N2-GR-FORM",
    "category": "Mondai 7: 文法形式の判断",
    "stem": "窓口の仕事では、住民から感謝の言葉をかけられる（　）、この仕事を続けてよかったと感じる。",
    "targetWord": "につけ",
    "options": [
      {
        "id": "A",
        "text": "につけ"
      },
      {
        "id": "B",
        "text": "を契機に"
      },
      {
        "id": "C",
        "text": "に際して"
      },
      {
        "id": "D",
        "text": "はおろか"
      }
    ],
    "correctAnswer": "A",
    "explanation": "～につけ: Cứ mỗi khi xảy ra việc gì thì lại nảy sinh cảm xúc hoặc suy nghĩ. 住民から感謝の言葉をかけられるにつけ、この仕事を続けてよかったと感じる (cứ mỗi lần được người dân cảm ơn lại thấy mình đã chọn đúng công việc).",
    "distractorExplanations": {
      "B": "～を契機に nối sau một danh từ để nêu bước ngoặt dẫn đến thay đổi; ở đây cần biểu đạt cảm xúc lặp lại mỗi lần.",
      "C": "～に際して thường nối sau danh từ/sự kiện để nói 'nhân dịp'; không dùng sau mệnh đề động từ này với nghĩa mỗi lần.",
      "D": "～はおろか cần cấu trúc nêu A chưa nói đến B; không thể hiện quan hệ lặp lại và cảm xúc trong câu."
    }
  },
  {
    "id": "N2_07_M7_02",
    "typeId": "N2-GR-FORM",
    "category": "Mondai 7: 文法形式の判断",
    "stem": "自治体の窓口業務におけるペーパーレス化は、ここ数年で着実に進み（　）。",
    "targetWord": "つつある",
    "options": [
      {
        "id": "A",
        "text": "っこない"
      },
      {
        "id": "B",
        "text": "つつある"
      },
      {
        "id": "C",
        "text": "かねない"
      },
      {
        "id": "D",
        "text": "ざるを得ない"
      }
    ],
    "correctAnswer": "B",
    "explanation": "動詞マス形＋つつある: Đang dần dần biến đổi theo một hướng nhất định: 着実に進みつつある (đang dần tiến triển đều đặn).",
    "distractorExplanations": {
      "A": "っこない: Tuyệt đối không thể (khẳng định phủ định mạnh).",
      "C": "かねない: Có nguy cơ dẫn tới hậu quả xấu.",
      "D": "ざるを得ない: Buộc phải làm dù không muốn."
    }
  },
  {
    "id": "N2_07_M7_03",
    "typeId": "N2-GR-FORM",
    "category": "Mondai 7: 文法形式の判断",
    "stem": "本市の総合福祉センターは、年齢や国籍（　）、地域住民であれば誰でも利用可能だ。",
    "targetWord": "を問わず",
    "options": [
      {
        "id": "A",
        "text": "に相違ない"
      },
      {
        "id": "B",
        "text": "を皮切りに"
      },
      {
        "id": "C",
        "text": "を問わず"
      },
      {
        "id": "D",
        "text": "からして"
      }
    ],
    "correctAnswer": "C",
    "explanation": "～を問わず（をとわず）: Bất kể, không phân biệt (tuổi tác, giới tính, quốc tịch): 年齢や国籍を問わず.",
    "distractorExplanations": {
      "A": "～に相違ない: Chắc chắn là (phán đoán chắc nịch).",
      "B": "～を皮切りに: Mở đầu bằng một chuỗi hành động phát triển liên tiếp.",
      "D": "～からして: Ngay từ điểm A đã thấy..."
    }
  },
  {
    "id": "N2_07_M7_04",
    "typeId": "N2-GR-FORM",
    "category": "Mondai 7: 文法形式の判断",
    "stem": "個人情報保護に関する社内規程は、正社員か契約社員かなどの雇用形態（　）、全職員に同じ基準で適用される。",
    "targetWord": "を問わず",
    "options": [
      {
        "id": "A",
        "text": "に基づき"
      },
      {
        "id": "B",
        "text": "に応じて"
      },
      {
        "id": "C",
        "text": "をめぐって"
      },
      {
        "id": "D",
        "text": "を問わず"
      }
    ],
    "correctAnswer": "D",
    "explanation": "名詞＋を問わず: Bất kể, không phân biệt. Cụm '同じ基準で適用' xác nhận quy định áp dụng như nhau với mọi hình thức tuyển dụng.",
    "distractorExplanations": {
      "A": "に基づき cần đứng sau căn cứ làm nền tảng cho một hành động; ở đây danh từ 雇用形態 là nhóm được miễn phân biệt, không phải căn cứ áp dụng.",
      "B": "に応じて sẽ biểu thị tiêu chuẩn thay đổi tùy theo hình thức tuyển dụng, trái với '同じ基準で'.",
      "C": "をめぐって thường nói về tranh luận hoặc vấn đề xoay quanh một chủ đề; không nối được với ý áp dụng quy định đồng nhất."
    }
  },
  {
    "id": "N2_07_M7_05",
    "typeId": "N2-GR-FORM",
    "category": "Mondai 7: 文法形式の判断",
    "stem": "住民の機密データを扱う業務である以上、確認作業を怠る（　）。",
    "targetWord": "わけにはいかない",
    "options": [
      {
        "id": "A",
        "text": "わけにはいかない"
      },
      {
        "id": "B",
        "text": "にほかならない"
      },
      {
        "id": "C",
        "text": "にすぎない"
      },
      {
        "id": "D",
        "text": "ほかはない"
      }
    ],
    "correctAnswer": "A",
    "explanation": "動詞辞書形＋わけにはいかない: Không thể làm việc đó vì trách nhiệm xã hội, lương tâm, đạo đức: 怠るわけにはいかない (không thể lơ là được).",
    "distractorExplanations": {
      "B": "～にほかならない: Chính là, không gì khác ngoài...",
      "C": "～にすぎない: Chỉ là... không hơn.",
      "D": "～ほかはない: Không còn cách nào khác ngoài việc..."
    }
  },
  {
    "id": "N2_07_M7_06",
    "typeId": "N2-GR-FORM",
    "category": "Mondai 7: 文法形式の判断",
    "stem": "本庁舎の市民交流ラウンジは、図書カードを提示した来庁者（　）、平日午後7時まで利用できます。",
    "targetWord": "に限り",
    "options": [
      {
        "id": "A",
        "text": "に際して"
      },
      {
        "id": "B",
        "text": "に限り"
      },
      {
        "id": "C",
        "text": "に先立ち"
      },
      {
        "id": "D",
        "text": "につれて"
      }
    ],
    "correctAnswer": "B",
    "explanation": "～に限り: Chỉ giới hạn trong nhóm được nêu. ここでは『図書カードを提示した来庁者に限り』、chỉ người đến làm thủ tục có đưa thẻ thư viện mới được dùng phòng đến 19 giờ.",
    "distractorExplanations": {
      "A": "～に際して: Nhân dịp một sự kiện; không diễn tả điều kiện giới hạn người được sử dụng.",
      "C": "～に先立ち: Trước khi một sự kiện diễn ra; không nối điều kiện với quyền sử dụng.",
      "D": "～につれて: Càng... thì càng...; cần hai biến đổi song song, không phù hợp với điều kiện cấp quyền."
    }
  },
  {
    "id": "N2_07_M7_07",
    "typeId": "N2-GR-FORM",
    "category": "Mondai 7: 文法形式の判断",
    "stem": "本日は館内電気設備の定期点検（　）、全館休館とさせていただきます。",
    "targetWord": "につき",
    "options": [
      {
        "id": "A",
        "text": "をよそに"
      },
      {
        "id": "B",
        "text": "につけて"
      },
      {
        "id": "C",
        "text": "につき"
      },
      {
        "id": "D",
        "text": "のもとで"
      }
    ],
    "correctAnswer": "C",
    "explanation": "名詞＋につき: Vì lý do... (cách thông báo chính thức trang trọng trên bảng tin công cộng): 点検につき (do kiểm tra định kỳ).",
    "distractorExplanations": {
      "A": "～をよそに: Mặc kệ, bỏ ngoài tai.",
      "B": "～につけて: Cứ mỗi lần...",
      "D": "～のもとで: Dưới sự chỉ dẫn/ảnh hưởng của ai."
    }
  },
  {
    "id": "N2_07_M7_08",
    "typeId": "N2-GR-FORM",
    "category": "Mondai 7: 文法形式の判断",
    "stem": "新任の窓口担当者が、少し不安（　）表情で来庁者の書類に目を通していた。",
    "targetWord": "げな",
    "options": [
      {
        "id": "A",
        "text": "めいた"
      },
      {
        "id": "B",
        "text": "っぽい"
      },
      {
        "id": "C",
        "text": "がちな"
      },
      {
        "id": "D",
        "text": "げな"
      }
    ],
    "correctAnswer": "D",
    "explanation": "イ形容詞語幹/名詞＋げな: Có vẻ, lộ vẻ (tâm trạng biểu lộ ra bên ngoài): 不安げな表情 (vẻ mặt lộ vẻ bất an).",
    "distractorExplanations": {
      "A": "めいた: Có màu sắc, nhuốm màu (bí mật, xuân sang: 謎めいた).",
      "B": "っぽい: Thiên về, hay... (dễ nổi cáu, mang tính trẻ con: 怒りっぽい).",
      "C": "がちな: Thường hay xảy ra xu hướng xấu (hay nghỉ việc: 休みがち)."
    }
  },
  {
    "id": "N2_07_M7_09",
    "typeId": "N2-GR-FORM",
    "category": "Mondai 7: 文法形式の判断",
    "stem": "これほど複雑な行政手続きを、事前の案内なしに一般市民が一人で理解でき（　）。",
    "targetWord": "っこない",
    "options": [
      {
        "id": "A",
        "text": "っこない"
      },
      {
        "id": "B",
        "text": "かねない"
      },
      {
        "id": "C",
        "text": "がたい"
      },
      {
        "id": "D",
        "text": "ざるを得ない"
      }
    ],
    "correctAnswer": "A",
    "explanation": "動詞マス形＋っこない: Làm sao mà... có thể được (khẳng định dứt khoát sự bất khả thi trong suy nghĩ người nói): 理解できっこない (làm sao mà tự hiểu nổi).",
    "distractorExplanations": {
      "B": "かねない: Có khả năng xảy ra nguy cơ xấu.",
      "C": "がたい: Khó lòng làm được (về mặt tâm lý, cảm xúc: 信じがたい).",
      "D": "ざるを得ない: Buộc phải..."
    }
  },
  {
    "id": "N2_07_M7_10",
    "typeId": "N2-GR-FORM",
    "category": "Mondai 7: 文法形式の判断",
    "stem": "新年度の予算案を編成する（　）、各地域からの要望事項を詳細に調査した。",
    "targetWord": "にあたって",
    "options": [
      {
        "id": "A",
        "text": "を限りに"
      },
      {
        "id": "B",
        "text": "にあたって"
      },
      {
        "id": "C",
        "text": "をおいて"
      },
      {
        "id": "D",
        "text": "からして"
      }
    ],
    "correctAnswer": "B",
    "explanation": "動詞辞書形＋にあたって: Khi tiến hành, nhân dịp chuẩn bị cho một việc trọng đại: 編成するにあたって.",
    "distractorExplanations": {
      "A": "～を限りに: Cho đến hết... (hạn chót).",
      "C": "～をおいて: Ngoại trừ người/vật này ra thì không có...",
      "D": "～からして: Xét ngay từ..."
    }
  },
  {
    "id": "N2_07_M7_11",
    "typeId": "N2-GR-FORM",
    "category": "Mondai 7: 文法形式の判断",
    "stem": "新設予定の児童館の運営方針（　）、地域住民の間で活発な意見交換が行われた。",
    "targetWord": "をめぐって",
    "options": [
      {
        "id": "A",
        "text": "を通じて"
      },
      {
        "id": "B",
        "text": "にかけては"
      },
      {
        "id": "C",
        "text": "をめぐって"
      },
      {
        "id": "D",
        "text": "を抜きにして"
      }
    ],
    "correctAnswer": "C",
    "explanation": "名詞＋をめぐって: Xoay quanh một đề tài/tranh luận, ý kiến đối lập: 運営方針をめぐって (xoay quanh phương châm vận hành).",
    "distractorExplanations": {
      "A": "～を通じて: Thông qua suốt một khoảng thời gian hoặc phương tiện.",
      "B": "～にかけては: Nếu xét về sở trường/lĩnh vực gì thì không thua ai.",
      "D": "～を抜きにして: Nếu không có... thì không thể..."
    }
  },
  {
    "id": "N2_07_M7_12",
    "typeId": "N2-GR-FORM",
    "category": "Mondai 7: 文法形式の判断",
    "stem": "これほど短期間で窓口の混雑を解消できたのは、全職員の連携と努力の（　）。",
    "targetWord": "賜物にほかならない",
    "options": [
      {
        "id": "A",
        "text": "極みだ"
      },
      {
        "id": "B",
        "text": "きらいがある"
      },
      {
        "id": "C",
        "text": "始末だ"
      },
      {
        "id": "D",
        "text": "賜物にほかならない"
      }
    ],
    "correctAnswer": "D",
    "explanation": "～にほかならない: Chính là, không gì khác hơn là...: 努力の賜物にほかならない (chính là thành quả từ sự nỗ lực của toàn thể nhân viên).",
    "distractorExplanations": {
      "A": "～極みだ: Tột cùng của cảm xúc (hạnh phúc, vinh dự: 痛恨の極み).",
      "B": "～きらいがある: Có xu hướng tật xấu/tiêu cực.",
      "C": "～始末だ: Rốt cuộc chuốc lấy kết cục tồi tệ."
    }
  },
  {
    "id": "N2_07_M8_01",
    "typeId": "N2-GR-STAR",
    "category": "Mondai 8: 文の組み立て",
    "stem": "証明書を申請する場合は、（　　）（　　）★（　　）。",
    "options": [
      {
        "id": "A",
        "text": "記入し"
      },
      {
        "id": "B",
        "text": "本人確認書類を"
      },
      {
        "id": "C",
        "text": "申請書に必要事項を"
      },
      {
        "id": "D",
        "text": "窓口へ提出してください"
      }
    ],
    "correctAnswer": "B",
    "starPosition": 3,
    "assembledSentence": "証明書を申請する場合は、申請書に必要事項を記入し本人確認書類を窓口へ提出してください。",
    "explanation": "Câu hoàn chỉnh: 証明書を申請する場合は、申請書に必要事項を記入し本人確認書類を窓口へ提出してください。 Nghĩa là khi xin cấp giấy chứng nhận, hãy điền thông tin cần thiết vào đơn, rồi nộp giấy tờ xác minh danh tính tại quầy. 必要事項を là tân ngữ của 記入し; sau đó 本人確認書類を là tân ngữ của 提出してください. Mảnh ★ là 本人確認書類を.",
    "distractorExplanations": {
      "A": "記入し nối với tân ngữ 必要事項を trong cụm 申請書に必要事項を記入し; không phải vị trí đánh dấu ★.",
      "C": "申請書に必要事項を đứng ở vị trí đầu tiên để làm nền cho động từ 記入し.",
      "D": "窓口へ提出してください là mệnh đề kết thúc câu, đứng sau các tân ngữ cần nộp."
    }
  },
  {
    "id": "N2_07_M8_02",
    "typeId": "N2-GR-STAR",
    "category": "Mondai 8: 文の組み立て",
    "stem": "今回の臨時給付金は、世帯所得の（　　）（　　）★（　　）一律に支給されます。",
    "options": [
      {
        "id": "A",
        "text": "問わず、"
      },
      {
        "id": "B",
        "text": "すべての"
      },
      {
        "id": "C",
        "text": "対象世帯へ"
      },
      {
        "id": "D",
        "text": "多寡を"
      }
    ],
    "correctAnswer": "B",
    "starPosition": 3,
    "assembledSentence": "今回の臨時給付金は、世帯所得の多寡を問わず、すべての対象世帯へ一律に支給されます。",
    "explanation": "Câu hoàn chỉnh: 今回の臨時給付金は、世帯所得の多寡を問わず、すべての対象世帯へ一律に支給されます。 Nghĩa là khoản hỗ trợ đột xuất được cấp đồng đều cho mọi hộ đủ điều kiện, không phân biệt thu nhập cao hay thấp. Cấu trúc 多寡を問わず nghĩa là không xét mức độ; すべての bổ nghĩa cho 対象世帯へ. Mảnh ★ là すべての.",
    "distractorExplanations": {
      "A": "Vị trí 2 (問わず).",
      "C": "Vị trí 4 (対象世帯へ).",
      "D": "Vị trí 1 (多寡を)."
    }
  },
  {
    "id": "N2_07_M8_03",
    "typeId": "N2-GR-STAR",
    "category": "Mondai 8: 文の組み立て",
    "stem": "代理人として住民票の再発行を申請する場合は、（　　）（　　）★（　　）あります。",
    "options": [
      {
        "id": "A",
        "text": "申請者本人が作成した"
      },
      {
        "id": "B",
        "text": "委任状を"
      },
      {
        "id": "C",
        "text": "事前に受け取っておく"
      },
      {
        "id": "D",
        "text": "必要が"
      }
    ],
    "correctAnswer": "C",
    "starPosition": 3,
    "assembledSentence": "代理人として住民票の再発行を申請する場合は、申請者本人が作成した委任状を事前に受け取っておく必要があります。",
    "explanation": "Câu hoàn chỉnh: 代理人として住民票の再発行を申請する場合は、申請者本人が作成した委任状を事前に受け取っておく必要があります。 Nghĩa là nếu nộp đơn thay người khác, cần nhận trước giấy ủy quyền do chính người nộp đơn lập. Mệnh đề 申請者本人が作成した bổ nghĩa cho 委任状; 委任状を là tân ngữ của 事前に受け取っておく; 必要があります diễn tả sự cần thiết. Mảnh ★ là 事前に受け取っておく.",
    "distractorExplanations": {
      "A": "申請者本人が作成した bổ nghĩa cho 委任状, vì vậy đứng trước cụm này.",
      "B": "委任状を là tân ngữ của 事前に受け取っておく; nó đứng giữa cụm bổ nghĩa và động từ.",
      "D": "必要が đứng thứ tư để tạo thành cụm cố định 必要があります."
    }
  },
  {
    "id": "N2_07_M8_04",
    "typeId": "N2-GR-STAR",
    "category": "Mondai 8: 文の組み立て",
    "stem": "会議の議事録を作る際は、（　　）（　　）★（　　）大切です。",
    "options": [
      {
        "id": "A",
        "text": "発言者の意図を"
      },
      {
        "id": "B",
        "text": "単に発言を文字に起こすだけでなく、"
      },
      {
        "id": "C",
        "text": "ことも"
      },
      {
        "id": "D",
        "text": "正確に読み取る"
      }
    ],
    "correctAnswer": "D",
    "starPosition": 3,
    "assembledSentence": "会議の議事録を作る際は、単に発言を文字に起こすだけでなく、発言者の意図を正確に読み取ることも大切です。",
    "explanation": "Câu hoàn chỉnh: 会議の議事録を作る際は、単に発言を文字に起こすだけでなく、発言者の意図を正確に読み取ることも大切です。 Nghĩa là khi ghi biên bản, ngoài việc chép lại lời nói, cũng cần hiểu đúng ý định của người phát biểu. Cấu trúc 単に～だけでなく～も nối hai việc song song; 発言者の意図を là tân ngữ của 正確に読み取る. Mảnh ★ là 正確に読み取る.",
    "distractorExplanations": {
      "A": "発言者の意図を là tân ngữ, cần đứng trước vị ngữ 正確に読み取る.",
      "B": "単に～だけでなく mở phần thứ nhất của cấu trúc đối sánh và phải đứng trước phần ～も.",
      "C": "ことも danh hóa hành động đọc đúng ý rồi nối với vị ngữ đánh giá 大切です."
    }
  },
  {
    "id": "N2_07_M8_05",
    "typeId": "N2-GR-STAR",
    "category": "Mondai 8: 文の組み立て",
    "stem": "この施策は、（　　）（　　）★（　　）予想される。",
    "options": [
      {
        "id": "A",
        "text": "利用者の利便性を"
      },
      {
        "id": "B",
        "text": "大幅に高める"
      },
      {
        "id": "C",
        "text": "可能性が"
      },
      {
        "id": "D",
        "text": "高いと"
      }
    ],
    "correctAnswer": "C",
    "starPosition": 3,
    "assembledSentence": "この施策は、利用者の利便性を大幅に高める可能性が高いと予想される。",
    "explanation": "Câu hoàn chỉnh: この施策は、利用者の利便性を大幅に高める可能性が高いと予想される。 Nghĩa là dự đoán biện pháp này có khả năng cải thiện đáng kể sự tiện lợi cho người dùng. 利用者の利便性を là tân ngữ; 大幅に高める bổ nghĩa cho 可能性; 可能性が高い nối với と予想される. Mảnh ★ là 可能性が.",
    "distractorExplanations": {
      "A": "利用者の利便性を là tân ngữ của 高める, phải theo sau bổ ngữ 大幅に và trước cụm danh từ 可能性.",
      "B": "大幅に高める là vị ngữ trong mệnh đề bổ nghĩa cho 可能性; 可能性があると予想される là cấu trúc chính.",
      "D": "高いと kết hợp với 可能性が để tạo cụm 可能性が高いと, bổ nghĩa cho 予想される."
    }
  },
  {
    "id": "N2_07_M9_01",
    "typeId": "N2-GR-TEXT",
    "category": "Mondai 9: 文章の文法",
    "stem": "文章の文法：【50】に入る最も適切なものはどれか。",
    "passage": "市民の皆様へ\n緑市役所 市民生活課\n\n　日頃より、本市の市政運営に温かいご理解とご協力を賜り、厚く御礼申し上げます。\n　さて、毎年3月下旬から4月中旬にかけましては、就職や進学、転勤などに伴う引っ越し手続きが集中し、本庁舎および各支所の窓口が大変混雑いたします。窓口で長時間お待ちいただく状況を緩和するため、本年度よりスマートフォンやパソコンから利用可能な「オンライン申請ポータル」の対象業務を大幅に拡大する【50】。\n\n　住民票の写しや課税証明書の発行、転出届の提出などにつきましては、マイナンバーカードをお持ちの方であれば、24時間ご自宅から手続きを完了して【51】。これにより、市役所へ直接ご来庁いただく必要がなくなり、大幅な時間短縮が可能となります。\n\n　【52】、オンライン申請の利用にあたりましては、電子証明書の有効期限が切れていないか事前にご確認いただく必要がございます。もし暗証番号をお忘れの場合やカードの機能停止中である場合は、誠に恐れ入りますが、ご本人様による窓口での再設定手続きが【53】。\n\n　市民の皆様におかれましては、窓口の混雑緩和と待ち時間削減に向け、便利なオンライン手続きを積極的に【54】、何卒ご協力のほどよろしくお願い申し上げます。",
    "options": [
      {
        "id": "A",
        "text": "ことと存じます"
      },
      {
        "id": "B",
        "text": "こととなりました"
      },
      {
        "id": "C",
        "text": "はずがありません"
      },
      {
        "id": "D",
        "text": "わけがございません"
      }
    ],
    "correctAnswer": "B",
    "explanation": "～こととなりました: Biểu đạt quyết định/chính sách chính thức của cơ quan, tổ chức đối với công chúng.",
    "distractorExplanations": {
      "A": "ことと存じます: Dùng diễn đạt suy đoán lịch sự về tình hình người nhận thư.",
      "C": "はずがありません: Chắc chắn không có chuyện (bác bỏ vô lý).",
      "D": "わけがございません: Không có lý nào."
    }
  },
  {
    "id": "N2_07_M9_02",
    "typeId": "N2-GR-TEXT",
    "category": "Mondai 9: 文章の文法",
    "stem": "文章の文法：【51】に入る最も適切なものはどれか。",
    "passage": "市民の皆様へ\n緑市役所 市民生活課\n\n　日頃より、本市の市政運営に温かいご理解とご協力を賜り、厚く御礼申し上げます。\n　さて、毎年3月下旬から4月中旬にかけましては、就職や進学、転勤などに伴う引っ越し手続きが集中し、本庁舎および各支所の窓口が大変混雑いたします。窓口で長時間お待ちいただく状況を緩和するため、本年度よりスマートフォンやパソコンから利用可能な「オンライン申請ポータル」の対象業務を大幅に拡大する【50】。\n\n　住民票の写しや課税証明書の発行、転出届の提出などにつきましては、マイナンバーカードをお持ちの方であれば、24時間ご自宅から手続きを完了して【51】。これにより、市役所へ直接ご来庁いただく必要がなくなり、大幅な時間短縮が可能となります。\n\n　【52】、オンライン申請の利用にあたりましては、電子証明書の有効期限が切れていないか事前にご確認いただく必要がございます。もし暗証番号をお忘れの場合やカードの機能停止中である場合は、誠に恐れ入りますが、ご本人様による窓口での再設定手続きが【53】。\n\n　市民の皆様におかれましては、窓口の混雑緩和と待ち時間削減に向け、便利なオンライン手続きを積極的に【54】、何卒ご協力のほどよろしくお願い申し上げます。",
    "options": [
      {
        "id": "A",
        "text": "存じます"
      },
      {
        "id": "B",
        "text": "申し上げます"
      },
      {
        "id": "C",
        "text": "いただけます"
      },
      {
        "id": "D",
        "text": "伺います"
      }
    ],
    "correctAnswer": "C",
    "explanation": "完了していただけます: Thể khả năng kính ngữ của もらう (quý công dân có thể hoàn tất thủ tục).",
    "distractorExplanations": {
      "A": "存じます: Nghĩ, cảm thấy (người nói).",
      "B": "申し上げます: Khiêm nhường ngữ nói về hành động của bản thân cơ quan.",
      "D": "伺います: Khiêm nhường ngữ hỏi/thăm viếng."
    }
  },
  {
    "id": "N2_07_M9_03",
    "typeId": "N2-GR-TEXT",
    "category": "Mondai 9: 文章の文法",
    "stem": "文章の文法：【52】に入る最も適切なものはどれか。",
    "passage": "市民の皆様へ\n緑市役所 市民生活課\n\n　日頃より、本市の市政運営に温かいご理解とご協力を賜り、厚く御礼申し上げます。\n　さて、毎年3月下旬から4月中旬にかけましては、就職や進学、転勤などに伴う引っ越し手続きが集中し、本庁舎および各支所の窓口が大変混雑いたします。窓口で長時間お待ちいただく状況を緩和するため、本年度よりスマートフォンやパソコンから利用可能な「オンライン申請ポータル」の対象業務を大幅に拡大する【50】。\n\n　住民票の写しや課税証明書の発行、転出届の提出などにつきましては、マイナンバーカードをお持ちの方であれば、24時間ご自宅から手続きを完了して【51】。これにより、市役所へ直接ご来庁いただく必要がなくなり、大幅な時間短縮が可能となります。\n\n　【52】、オンライン申請の利用にあたりましては、電子証明書の有効期限が切れていないか事前にご確認いただく必要がございます。もし暗証番号をお忘れの場合やカードの機能停止中である場合は、誠に恐れ入りますが、ご本人様による窓口での再設定手続きが【53】。\n\n　市民の皆様におかれましては、窓口の混雑緩和と待ち時間削減に向け、便利なオンライン手続きを積極的に【54】、何卒ご協力のほどよろしくお願い申し上げます。",
    "options": [
      {
        "id": "A",
        "text": "なぜなら"
      },
      {
        "id": "B",
        "text": "ところが"
      },
      {
        "id": "C",
        "text": "それゆえ"
      },
      {
        "id": "D",
        "text": "なお"
      }
    ],
    "correctAnswer": "D",
    "explanation": "なお: Từ nối dùng để bổ sung thêm lưu ý quan trọng cần ghi nhớ trong văn bản hành chính.",
    "distractorExplanations": {
      "A": "なぜなら: Bởi vì (giải thích lý do).",
      "B": "ところが: Tuy nhiên (đối lập bất ngờ).",
      "C": "それゆえ: Do đó, vì thế (nguyên nhân kết quả trang trọng)."
    }
  },
  {
    "id": "N2_07_M9_04",
    "typeId": "N2-GR-TEXT",
    "category": "Mondai 9: 文章の文法",
    "stem": "文章の文法：【53】に入る最も適切なものはどれか。",
    "passage": "市民の皆様へ\n緑市役所 市民生活課\n\n　日頃より、本市の市政運営に温かいご理解とご協力を賜り、厚く御礼申し上げます。\n　さて、毎年3月下旬から4月中旬にかけましては、就職や進学、転勤などに伴う引っ越し手続きが集中し、本庁舎および各支所の窓口が大変混雑いたします。窓口で長時間お待ちいただく状況を緩和するため、本年度よりスマートフォンやパソコンから利用可能な「オンライン申請ポータル」の対象業務を大幅に拡大する【50】。\n\n　住民票の写しや課税証明書の発行、転出届の提出などにつきましては、マイナンバーカードをお持ちの方であれば、24時間ご自宅から手続きを完了して【51】。これにより、市役所へ直接ご来庁いただく必要がなくなり、大幅な時間短縮が可能となります。\n\n　【52】、オンライン申請の利用にあたりましては、電子証明書の有効期限が切れていないか事前にご確認いただく必要がございます。もし暗証番号をお忘れの場合やカードの機能停止中である場合は、誠に恐れ入りますが、ご本人様による窓口での再設定手続きが【53】。\n\n　市民の皆様におかれましては、窓口の混雑緩和と待ち時間削減に向け、便利なオンライン手続きを積極的に【54】、何卒ご協力のほどよろしくお願い申し上げます。",
    "options": [
      {
        "id": "A",
        "text": "必要となります"
      },
      {
        "id": "B",
        "text": "得ません"
      },
      {
        "id": "C",
        "text": "かねません"
      },
      {
        "id": "D",
        "text": "おかないでしょう"
      }
    ],
    "correctAnswer": "A",
    "explanation": "再設定手続きが必要となります: Khi mã PIN bị quên hoặc chức năng thẻ bị khóa, người dân phải trực tiếp đến quầy để làm thủ tục thiết lập lại.",
    "distractorExplanations": {
      "B": "得ません: Sai ngữ pháp khi đi trực tiếp với danh từ/trợ từ が.",
      "C": "かねません: Có nguy cơ xảy ra việc xấu.",
      "D": "おかないでしょう: Không thể không làm (quyết tâm)."
    }
  },
  {
    "id": "N2_07_M9_05",
    "typeId": "N2-GR-TEXT",
    "category": "Mondai 9: 文章の文法",
    "stem": "文章の文法：【54】に入る最も適切なものはどれか。",
    "passage": "市民の皆様へ\n緑市役所 市民生活課\n\n　日頃より、本市の市政運営に温かいご理解とご協力を賜り、厚く御礼申し上げます。\n　さて、毎年3月下旬から4月中旬にかけましては、就職や進学、転勤などに伴う引っ越し手続きが集中し、本庁舎および各支所の窓口が大変混雑いたします。窓口で長時間お待ちいただく状況を緩和するため、本年度よりスマートフォンやパソコンから利用可能な「オンライン申請ポータル」の対象業務を大幅に拡大する【50】。\n\n　住民票の写しや課税証明書の発行、転出届の提出などにつきましては、マイナンバーカードをお持ちの方であれば、24時間ご自宅から手続きを完了して【51】。これにより、市役所へ直接ご来庁いただく必要がなくなり、大幅な時間短縮が可能となります。\n\n　【52】、オンライン申請の利用にあたりましては、電子証明書の有効期限が切れていないか事前にご確認いただく必要がございます。もし暗証番号をお忘れの場合やカードの機能停止中である場合は、誠に恐れ入りますが、ご本人様による窓口での再設定手続きが【53】。\n\n　市民の皆様におかれましては、窓口の混雑緩和と待ち時間削減に向け、便利なオンライン手続きを積極的に【54】、何卒ご協力のほどよろしくお願い申し上げます。",
    "options": [
      {
        "id": "A",
        "text": "ご活用申し上げますよう"
      },
      {
        "id": "B",
        "text": "ご活用くださいますよう"
      },
      {
        "id": "C",
        "text": "ご活用いたしたく"
      },
      {
        "id": "D",
        "text": "ご活用いただくまいと"
      }
    ],
    "correctAnswer": "B",
    "explanation": "ご活用くださいますよう（ごかつようくださいますよう）: Mẫu kính ngữ kêu gọi, kính mong người dân tích cực sử dụng dịch vụ.",
    "distractorExplanations": {
      "A": "ご活用申し上げますよう: Nhầm khiêm nhường ngữ 申し上げる cho hành động của người dân.",
      "C": "ご活用いたしたく: Bày tỏ mong muốn của người nói.",
      "D": "いただくまいと: Thể phủ định tuyệt đối."
    }
  },
  {
    "id": "N2_07_M10_01",
    "typeId": "N2-RD-SHORT",
    "category": "Mondai 10: 短文読解",
    "passage": "社員各位\n総務課\n\n　来週月曜日より実施予定の社内PC一斉セキュリティ更新につきまして、一部の業務端末において事前のバックアップが未完了であることが判明いたしました。つきましては、各自の重要データにつきまして、本日17時までに所定のクラウド共有ドライブへ退避作業を完了していただきますようお願いいたします。なお、期日までにバックアップが完了していない端末につきましては、更新処理を一時的に保留とし、個別対応となりますのでご留意ください。",
    "stem": "この通知によると、社員は何をしなければならないか。",
    "options": [
      {
        "id": "A",
        "text": "バックアップ未完了の端末を直ちに総務課へ持参する。"
      },
      {
        "id": "B",
        "text": "来週月曜日に各自のPCのセキュリティ更新作業を直接行う。"
      },
      {
        "id": "C",
        "text": "本日17時までに各自の重要データをクラウド共有ドライブへ保存する。"
      },
      {
        "id": "D",
        "text": "来週月曜日までPCを使った業務をすべて停止する。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Thông báo yêu cầu mỗi nhân viên sao lưu dữ liệu quan trọng lên thư mục đám mây dùng chung trước 17 giờ hôm nay, trước đợt cập nhật bảo mật vào thứ Hai tới. Máy chưa sao lưu sẽ bị hoãn cập nhật và xử lý riêng; nhân viên không tự thực hiện cập nhật.",
    "distractorExplanations": {
      "A": "Không yêu cầu mang máy lên phòng tổng vụ.",
      "B": "Việc cập nhật do hệ thống làm vào thứ 2 tới, nhân viên không tự cài đặt.",
      "D": "Không có yêu cầu dừng toàn bộ công việc."
    }
  },
  {
    "id": "N2_07_M10_02",
    "typeId": "N2-RD-SHORT",
    "category": "Mondai 10: 短文読解",
    "passage": "自治会からのお知らせ：粗大ゴミ収集場所の変更について\n　現在、集会所横のスペースを粗大ゴミの一時集積所として運用しておりますが、近隣住民の方々より通行の妨げになるとのご指摘をいただきました。そのため、来月1日収集分より、集積場所を「北側児童公園前ゲート横」へと移転いたします。移転後は、事前に市役所への電話またはウェブ予約を済ませ、所定の収集シールを貼付した物のみ搬出可能となります。無断放置は厳禁ですのでご注意ください。",
    "stem": "粗大ゴミの出し方について、本文の内容と合っているものはどれか。",
    "options": [
      {
        "id": "A",
        "text": "市役所への予約は電話のみで受け付け、ウェブ申請は認められない。"
      },
      {
        "id": "B",
        "text": "近隣住民の反対により、粗大ゴミの回収自体が来月より全面中止となる。"
      },
      {
        "id": "C",
        "text": "集会所横の集積所は来月以降も事前の連絡なしでいつでも利用できる。"
      },
      {
        "id": "D",
        "text": "来月1日以降は集積場所が北側児童公園前へ移り、予約とシールの貼付が必要になる。"
      }
    ],
    "correctAnswer": "D",
    "explanation": "Đoạn văn chỉ rõ: từ ngày 1 tháng tới điểm tập kết dời sang cổng công viên phía bắc, bắt buộc đặt lịch trước (qua điện thoại hoặc web) và dán tem thu gom.",
    "distractorExplanations": {
      "A": "Văn bản ghi rõ: 電話またはウェブ予約 (cả điện thoại lẫn web đều được).",
      "B": "Không hủy bỏ việc thu gom mà chỉ đổi địa điểm.",
      "C": "Điểm cũ cạnh hội trường sẽ bị đóng, không được để rác cản trở lối đi nữa."
    }
  },
  {
    "id": "N2_07_M10_03",
    "typeId": "N2-RD-SHORT",
    "category": "Mondai 10: 短文読解",
    "passage": "夏季の節電対策およびクールビズの実施について\n　地球温暖化防止および電力需給逼迫への対応として、本年度も社内の冷房温度を原則として28度に設定いたします。これに伴い、執務中の服装につきましては、ノーネクタイ・ノージャケットを推奨いたします。ただし、社外のお客様との重要な商談や公式セレモニーに出席される際には、相手方に失礼のないよう、状況に応じた節度ある身だしなみを保つよう心がけてください。",
    "stem": "執務中の服装について、この会社の方針として最も適切なものはどれか。",
    "options": [
      {
        "id": "A",
        "text": "社内ではノーネクタイを推奨するが、来客対応や商談では状況に合わせた服装をする。"
      },
      {
        "id": "B",
        "text": "夏期期間中はすべての商談や式典を含め、常にノージャケットで臨まなければならない。"
      },
      {
        "id": "C",
        "text": "冷房温度を28度にするため、社外との会議でもネクタイの着用は禁止されている。"
      },
      {
        "id": "D",
        "text": "公式セレモニーであっても各自の判断でどのような服装をしても問題ない。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Nội dung chỉ rõ: trong nội bộ khuyến khích không cà vạt/áo khoác, nhưng khi tiếp khách quan trọng hay dự lễ nghi chính thức phải ăn mặc trang trọng phù hợp hoàn cảnh.",
    "distractorExplanations": {
      "B": "Không bắt buộc mọi cuộc gặp đều không mặc áo khoác.",
      "C": "Không hề cấm thắt cà vạt khi gặp khách ngoài.",
      "D": "Lễ nghi chính thức không được tự ý mặc bừa bãi."
    }
  },
  {
    "id": "N2_07_M10_04",
    "typeId": "N2-RD-SHORT",
    "category": "Mondai 10: 短文読解",
    "passage": "マンションにお住まいの皆様へ\n給水設備定期清掃・点検に伴う断水のお知らせ\n\n　下記の日程におきまして、貯水槽の定期清掃および給水ポンプの保守点検を実施いたします。点検作業中は、全戸において水道水の使用ができません。濁り水の発生を防ぐため、断水開始前に蛇口が完全に閉まっていることをご確認いただくとともに、飲用水や生活用水の事前汲み置きをお願い申し上げます。\n\n【断水日時】2026年11月15日（日） 午前10:00 ～ 午後2:00",
    "stem": "この通知を読んだ住民が事前に行うべきことは何か。",
    "options": [
      {
        "id": "A",
        "text": "点検時間中に貯水槽へ立ち会い、清掃作業を手伝う。"
      },
      {
        "id": "B",
        "text": "断水に備えて飲用水や生活用水を汲み置き、蛇口が閉まっているか確認する。"
      },
      {
        "id": "C",
        "text": "濁り水が出るのを防ぐため、断水時間中にすべての蛇口を開けておく。"
      },
      {
        "id": "D",
        "text": "11月15日の午後は給水ポンプが停止するため、終日外出する。"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Thông báo hướng dẫn người dân: khóa chặt vòi nước trước khi cắt nước và tích trữ sẵn nước sinh hoạt/uống.",
    "distractorExplanations": {
      "A": "Không yêu cầu cư dân đi hỗ trợ cọ rửa bể nước.",
      "C": "Mở hết vòi nước trong lúc cắt nước sẽ gây tràn nước khi cấp lại.",
      "D": "Không yêu cầu phải ra khỏi nhà cả ngày."
    }
  },
  {
    "id": "N2_07_M10_05",
    "typeId": "N2-RD-SHORT",
    "category": "Mondai 10: 短文読解",
    "passage": "市民図書館 休館と返却ポスト利用のご案内\n　蔵書点検および館内照明のLED化工事に伴い、来週火曜日から金曜日までの4日間、臨時休館いたします。休館期間中の図書の返却につきましては、正面玄関横の「返却ポスト」をご利用いただけます。ただし、CDやDVDなどの視聴覚資料は破損の危険があるため、返却ポストへの投函はできません。休館明けの土曜日以降に、直接カウンターまでお持ちくださいますようお願い申し上げます。",
    "stem": "休館中の資料の返却について、正しいものはどれか。",
    "options": [
      {
        "id": "A",
        "text": "休館期間中は図書を含めていかなる資料の返却も一切受け付けない。"
      },
      {
        "id": "B",
        "text": "CDやDVDを含め、すべての資料を正面玄関横の返却ポストに返却できる。"
      },
      {
        "id": "C",
        "text": "図書は返却ポストに投函できるが、CDやDVDは休館明けに窓口へ返却する。"
      },
      {
        "id": "D",
        "text": "返却ポストは土曜日以降のみ利用可能であり、平日は閉鎖されている。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Đoạn văn nêu rõ: sách thường có thể bỏ vào thùng trả sách, riêng đĩa CD/DVD dễ vỡ nên không được bỏ thùng mà phải chờ mở cửa lại vào thứ Bảy nộp trực tiếp tại quầy.",
    "distractorExplanations": {
      "A": "Sách giấy vẫn được trả vào thùng ngoài cửa.",
      "B": "Đĩa CD/DVD bị nghiêm cấm bỏ vào hộp trả sách vì sợ hỏng.",
      "D": "Hộp trả sách mở trong suốt thời gian đóng cửa tạm thời."
    }
  },
  {
    "id": "N2_07_M11_01",
    "typeId": "N2-RD-MID",
    "category": "Mondai 11: 中文読解",
    "passage": "　近年、多くの職場でビジネスチャットツールが導入され、同僚や上司との日常的な情報共有は格段に迅速化した。従来の電子メールのように格式ばった時候の挨拶や宛名書きを省き、要件だけを簡潔にやり取りできる利便性は、テレワークの普及とも相まって業務効率の向上に大きく寄与している。\n\n　しかし、その簡便さゆえに、新たなコミュニケーション上の摩擦が生じていることも見逃せない。文字だけの短いやり取りは、対面であれば声の抑揚や表情から自然に伝わるニュアンスを欠きがちである。そのため、発信者に悪気配がなくても、受信側には冷淡な指示や批判のように受け取られてしまう事例が後を絶たない。特に指導や修正を求めるメッセージでは、感情の行き違いが起こりやすい。\n\n　こうした問題を回避するためには、ツールの特性を過信せず、内容に応じた手段の使い分けが肝要である。単なる事実連絡やスケジュール確認であればチャットで十分だが、複雑な背景を持つ相談や意見の対立が予想される議題については、短時間でも音声通話やビデオ会議を交えるべきである。デジタル化が進む時代だからこそ、相手の心理的負担に配慮した柔軟な意思疎通が求められているのである。",
    "stem": "ビジネスチャットツールの普及が業務にもたらした利点として、筆者が挙げているものはどれか。",
    "options": [
      {
        "id": "A",
        "text": "相手の表情や抑揚が自動的にテキスト化され、親近感が増したこと。"
      },
      {
        "id": "B",
        "text": "対面での会議をすべて廃止し、オフィスの賃料を大幅に削減できたこと。"
      },
      {
        "id": "C",
        "text": "文章のニュアンスが正確に伝わり、指導や修正での誤解がなくなったこと。"
      },
      {
        "id": "D",
        "text": "形式的な挨拶を省いて要件を迅速に共有でき、業務の効率が高まったこと。"
      }
    ],
    "correctAnswer": "D",
    "explanation": "Đoạn 1 nêu: lược bỏ lời chào khuôn mẫu, trao đổi công việc ngắn gọn nhanh chóng giúp nâng cao hiệu suất công việc trong bối cảnh làm từ xa.",
    "distractorExplanations": {
      "A": "Nội dung bịa đặt không có trong bài.",
      "B": "Không nói đến việc hủy toàn bộ họp trực tiếp hay giảm tiền thuê văn phòng.",
      "C": "Trái ngược; nhắn tin ngắn dễ gây hiểu lầm chứ không phải loại bỏ hiểu lầm."
    }
  },
  {
    "id": "N2_07_M11_02",
    "typeId": "N2-RD-MID",
    "category": "Mondai 11: 中文読解",
    "passage": "　近年、多くの職場でビジネスチャットツールが導入され、同僚や上司との日常的な情報共有は格段に迅速化した。従来の電子メールのように格式ばった時候の挨拶や宛名書きを省き、要件だけを簡潔にやり取りできる利便性は、テレワークの普及とも相まって業務効率の向上に大きく寄与している。\n\n　しかし、その簡便さゆえに、新たなコミュニケーション上の摩擦が生じていることも見逃せない。文字だけの短いやり取りは、対面であれば声の抑揚や表情から自然に伝わるニュアンスを欠きがちである。そのため、発信者に悪気配がなくても、受信側には冷淡な指示や批判のように受け取られてしまう事例が後を絶たない。特に指導や修正を求めるメッセージでは、感情の行き違いが起こりやすい。\n\n　こうした問題を回避するためには、ツールの特性を過信せず、内容に応じた手段の使い分けが肝要である。単なる事実連絡やスケジュール確認であればチャットで十分だが、複雑な背景を持つ相談や意見の対立が予想される議題については、短時間でも音声通話やビデオ会議を交えるべきである。デジタル化が進む時代だからこそ、相手の心理的負担に配慮した柔軟な意思疎通が求められているのである。",
    "stem": "チャットツールの利用によって生じる問題点として、本文で指摘されているものは何か。",
    "options": [
      {
        "id": "A",
        "text": "表情や声の抑揚が伝わらないため、悪気がなくても冷淡に誤解される恐れがあること。"
      },
      {
        "id": "B",
        "text": "送信エラーが頻発し、重要なスケジュール連絡が相手に届かないこと。"
      },
      {
        "id": "C",
        "text": "文章が長くなりすぎて、読む側の業務時間が大幅に奪われてしまうこと。"
      },
      {
        "id": "D",
        "text": "相手が不在の場合にメッセージが自動的に削除されてしまうこと。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Đoạn 2 nêu: vì thiếu sắc thái giọng nói và nét mặt nên người nhận dễ cảm thấy tin nhắn cụt ngủn, lạnh lùng hoặc mang tính chỉ trích dù người gửi không có ác ý.",
    "distractorExplanations": {
      "B": "Bài viết không đề cập đến lỗi kỹ thuật đường truyền.",
      "C": "Bài nêu tin nhắn ngắn gọn chứ không phải quá dài.",
      "D": "Không có thông tin tin nhắn tự xóa."
    }
  },
  {
    "id": "N2_07_M11_03",
    "typeId": "N2-RD-MID",
    "category": "Mondai 11: 中文読解",
    "passage": "　近年、多くの職場でビジネスチャットツールが導入され、同僚や上司との日常的な情報共有は格段に迅速化した。従来の電子メールのように格式ばった時候の挨拶や宛名書きを省き、要件だけを簡潔にやり取りできる利便性は、テレワークの普及とも相まって業務効率の向上に大きく寄与している。\n\n　しかし、その簡便さゆえに、新たなコミュニケーション上の摩擦が生じていることも見逃せない。文字だけの短いやり取りは、対面であれば声の抑揚や表情から自然に伝わるニュアンスを欠きがちである。そのため、発信者に悪気配がなくても、受信側には冷淡な指示や批判のように受け取られてしまう事例が後を絶たない。特に指導や修正を求めるメッセージでは、感情の行き違いが起こりやすい。\n\n　こうした問題を回避するためには、ツールの特性を過信せず、内容に応じた手段の使い分けが肝要である。単なる事実連絡やスケジュール確認であればチャットで十分だが、複雑な背景を持つ相談や意見の対立が予想される議題については、短時間でも音声通話やビデオ会議を交えるべきである。デジタル化が進む時代だからこそ、相手の心理的負担に配慮した柔軟な意思疎通が求められているのである。",
    "stem": "筆者が提案する望ましいコミュニケーションのあり方はどのようなものか。",
    "options": [
      {
        "id": "A",
        "text": "誤解を避けるため、チャットツールの使用を直ちに全面的に禁止すること。"
      },
      {
        "id": "B",
        "text": "用件の性質に応じて、チャットだけでなく必要に応じて音声やビデオ会議を使い分けること。"
      },
      {
        "id": "C",
        "text": "業務連絡は常に長文の電子メールで行い、時候の挨拶を徹底すること。"
      },
      {
        "id": "D",
        "text": "複雑な相談であっても、相手の時間を取らないようチャットのみで完結させること。"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Đoạn cuối kết luận: với việc đơn giản thì chat là đủ, nhưng việc phức tạp, nhạy cảm hay dễ bất đồng thì nên kết hợp gọi điện hoặc họp video ngắn.",
    "distractorExplanations": {
      "A": "Tác giả không hề bảo cấm chat hoàn toàn.",
      "C": "Không bảo quay lại email dài dòng.",
      "D": "Trái ngược ý tác giả."
    }
  },
  {
    "id": "N2_07_M11_04",
    "typeId": "N2-RD-MID",
    "category": "Mondai 11: 中文読解",
    "passage": "　地方自治体における行政サービスのデジタル変革（DX）が加速している。かつては住民票や各種証明書を取得するために、平日の日中に市役所の窓口へ足を運び、長蛇の列に並ぶのが当たり前であった。しかし現在では、マイナンバーカードを用いたコンビニ交付やオンライン申請により、時間や場所を選ばずに諸手続きを行える環境が整備されつつある。\n\n　このデジタル化は、市民の利便性向上のみならず、市役所側の業務負担軽減にも寄与している。定型的な入力作業や証明書発行が自動化されることで、職員は地域福祉の相談や個別支援といった、人にしかできない高度な対面業務に注力できるようになるからである。\n\n　一方で、急速な移行がもたらす「取り残され」への配慮を怠ってはならない。高齢者や情報端末の操作に不慣れな層にとって、オンライン専用の窓口はかえって高い障壁となり得る。真に誰一人取り残さない公共サービスを実現するためには、最先端のデジタル導入を推進する一方で、丁寧な対面窓口や操作支援のサポート体制を併存させることが不可欠である。",
    "stem": "行政サービスのデジタル化が進んだことで、市民生活はどのように変化したか。",
    "options": [
      {
        "id": "A",
        "text": "証明書の発行費用が完全に無料になり、税金の支払いが不要になった。"
      },
      {
        "id": "B",
        "text": "市役所の窓口がすべて閉鎖され、対面での手続きが法律で禁止された。"
      },
      {
        "id": "C",
        "text": "コンビニや自宅から手続きができるようになり、平日の窓口に行かなくても済むようになった。"
      },
      {
        "id": "D",
        "text": "平日の夜間であっても、市役所本庁舎の全窓口が営業するようになった。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Đoạn 1 nêu: nhờ phát hành qua cửa hàng tiện lợi và nộp online, người dân có thể làm thủ tục mọi lúc mọi nơi không cần đến quầy vào giờ hành chính ngày thường.",
    "distractorExplanations": {
      "A": "Không miễn thuế hay miễn phí hoàn toàn.",
      "B": "Không đóng cửa toàn bộ và không cấm trực tiếp.",
      "D": "Việc giải quyết tiện lợi là nhờ hệ thống số, không phải quầy hành chính mở thâu đêm."
    }
  },
  {
    "id": "N2_07_M11_05",
    "typeId": "N2-RD-MID",
    "category": "Mondai 11: 中文読解",
    "passage": "　地方自治体における行政サービスのデジタル変革（DX）が加速している。かつては住民票や各種証明書を取得するために、平日の日中に市役所の窓口へ足を運び、長蛇の列に並ぶのが当たり前であった。しかし現在では、マイナンバーカードを用いたコンビニ交付やオンライン申請により、時間や場所を選ばずに諸手続きを行える環境が整備されつつある。\n\n　このデジタル化は、市民の利便性向上のみならず、市役所側の業務負担軽減にも寄与している。定型的な入力作業や証明書発行が自動化されることで、職員は地域福祉の相談や個別支援といった、人にしかできない高度な対面業務に注力できるようになるからである。\n\n　一方で、急速な移行がもたらす「取り残され」への配慮を怠ってはならない。高齢者や情報端末の操作に不慣れな層にとって、オンライン専用の窓口はかえって高い障壁となり得る。真に誰一人取り残さない公共サービスを実現するためには、最先端のデジタル導入を推進する一方で、丁寧な対面窓口や操作支援のサポート体制を併存させることが不可欠である。",
    "stem": "自治体側にとって、デジタル化がもたらす最大の利点は何か。",
    "options": [
      {
        "id": "A",
        "text": "すべての地域住民の個人情報を外部企業に委託して管理できること。"
      },
      {
        "id": "B",
        "text": "職員の数を半分に削減し、人件費をすべてシステム開発費に回せること。"
      },
      {
        "id": "C",
        "text": "市民からの苦情や相談を一切受け付けなくてもよくなること。"
      },
      {
        "id": "D",
        "text": "定型業務が自動化され、福祉相談などの対面支援に職員が注力できるようになること。"
      }
    ],
    "correctAnswer": "D",
    "explanation": "Đoạn 2 nêu: tự động hóa các thủ tục định hình giúp nhân viên tập trung vào các công tác chuyên sâu đòi hỏi sự tương tác con người như tư vấn phúc lợi.",
    "distractorExplanations": {
      "A": "Không nói ủy thác toàn bộ thông tin cá nhân ra ngoài.",
      "B": "Không nói giảm một nửa biên chế nhân sự.",
      "C": "Không phải từ chối khiếu nại của dân."
    }
  },
  {
    "id": "N2_07_M11_06",
    "typeId": "N2-RD-MID",
    "category": "Mondai 11: 中文読解",
    "passage": "　地方自治体における行政サービスのデジタル変革（DX）が加速している。かつては住民票や各種証明書を取得するために、平日の日中に市役所の窓口へ足を運び、長蛇の列に並ぶのが当たり前であった。しかし現在では、マイナンバーカードを用いたコンビニ交付やオンライン申請により、時間や場所を選ばずに諸手続きを行える環境が整備されつつある。\n\n　このデジタル化は、市民の利便性向上のみならず、市役所側の業務負担軽減にも寄与している。定型的な入力作業や証明書発行が自動化されることで、職員は地域福祉の相談や個別支援といった、人にしかできない高度な対面業務に注力できるようになるからである。\n\n　一方で、急速な移行がもたらす「取り残され」への配慮を怠ってはならない。高齢者や情報端末の操作に不慣れな層にとって、オンライン専用の窓口はかえって高い障壁となり得る。真に誰一人取り残さない公共サービスを実現するためには、最先端のデジタル導入を推進する一方で、丁寧な対面窓口や操作支援のサポート体制を併存させることが不可欠である。",
    "stem": "行政サービスのデジタル化を進める上で、筆者が最も重要だと主張している点はどれか。",
    "options": [
      {
        "id": "A",
        "text": "デジタル化を推進しつつも、高齢者等のために丁寧な対面窓口や支援体制を残すこと。"
      },
      {
        "id": "B",
        "text": "高齢者であっても例外なく全員が独力でスマートフォンを操作できるよう強制すること。"
      },
      {
        "id": "C",
        "text": "紙の書類による申請を完全に廃止し、窓口業務のコストをゼロにすること。"
      },
      {
        "id": "D",
        "text": "デジタル技術の導入を中止し、過去のすべて対面による手続きに戻すこと。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Đoạn cuối nhấn mạnh: để không ai bị bỏ lại phía sau, bên cạnh thúc đẩy công nghệ số vẫn phải duy trì quầy trực tiếp và hỗ trợ người cao tuổi.",
    "distractorExplanations": {
      "B": "Không bắt ép cưỡng chế người già.",
      "C": "Không xóa sổ hoàn toàn quầy giấy tờ.",
      "D": "Không bảo dừng công nghệ quay về thời xưa."
    }
  },
  {
    "id": "N2_07_M11_07",
    "typeId": "N2-RD-MID",
    "category": "Mondai 11: 中文読解",
    "passage": "　公務員や行政窓口の職員には、公平性と正確性が何よりも強く求められる。法令や規則に基づかない例外的な処理を安易に認めてしまえば、市民全体の信頼を損なうことになりかねないからである。そのため、窓口での応対が時に「形式主義」や「杓子定規（しゃくしじょうぎ）」と批判されることがあっても、一定のルールを厳格に順守することは公の責務として不可欠である。\n\n　しかしながら、規則を守ることと、利用者の心情に寄り添うことは決して矛盾するものではない。手続きの不備で書類が受理できない場合でも、単に「規定ですから無理です」と突き放すのと、「恐れ入りますが、法的な要件を満たすためにこの証明書が必要となります。取得にはこのような方法がございます」と丁寧に手順を示すのとでは、利用者が受ける印象は雲泥の差となる。\n\n　真の「質の高い行政サービス」とは、法の厳格さを維持しつつも、説明の言葉に温かみと共感を持たせることにある。ルールを機械的に適用するだけにとどまらず、困っている住民が次にどのような行動を取ればよいのかを導く姿勢こそが、これからの行政従事者に求められているプロフェッショナリズムなのである。",
    "stem": "行政窓口において、法令や規則の厳格な順守が不可欠とされる理由は何か。",
    "options": [
      {
        "id": "A",
        "text": "職員が住民からの質問に答える手間を省き、定時で退勤できるようにするため。"
      },
      {
        "id": "B",
        "text": "安易な例外処理を認めると、行政に対する市民全体の公平な信頼が損なわれるから。"
      },
      {
        "id": "C",
        "text": "窓口での相談件数を減らし、すべての業務をマニュアル化するため。"
      },
      {
        "id": "D",
        "text": "規則を厳しくすることで、申請書類の偽造をすべて物理的に不可能にするため。"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Đoạn 1 nêu: nếu dễ dàng xử lý ngoại lệ sai quy định thì sẽ đánh mất sự tin tưởng công bằng của toàn thể người dân đối với nền hành chính.",
    "distractorExplanations": {
      "A": "Không phải để trốn việc về sớm.",
      "C": "Không phải để giảm số lượt hỏi đáp của dân.",
      "D": "Quy tắc nghiêm ngặt là vì tính công bằng minh bạch, không phải cam kết chặn 100% làm giả."
    }
  },
  {
    "id": "N2_07_M11_08",
    "typeId": "N2-RD-MID",
    "category": "Mondai 11: 中文読解",
    "passage": "　公務員や行政窓口の職員には、公平性と正確性が何よりも強く求められる。法令や規則に基づかない例外的な処理を安易に認めてしまえば、市民全体の信頼を損なうことになりかねないからである。そのため、窓口での応対が時に「形式主義」や「杓子定規（しゃくしじょうぎ）」と批判されることがあっても、一定のルールを厳格に順守することは公の責務として不可欠である。\n\n　しかしながら、規則を守ることと、利用者の心情に寄り添うことは決して矛盾するものではない。手続きの不備で書類が受理できない場合でも、単に「規定ですから無理です」と突き放すのと、「恐れ入りますが、法的な要件を満たすためにこの証明書が必要となります。取得にはこのような方法がございます」と丁寧に手順を示すのとでは、利用者が受ける印象は雲泥の差となる。\n\n　真の「質の高い行政サービス」とは、法の厳格さを維持しつつも、説明の言葉に温かみと共感を持たせることにある。ルールを機械的に適用するだけにとどまらず、困っている住民が次にどのような行動を取ればよいのかを導く姿勢こそが、これからの行政従事者に求められているプロフェッショナリズムなのである。",
    "stem": "書類が受理できない場面での望ましい対応として、筆者が勧めているものはどれか。",
    "options": [
      {
        "id": "A",
        "text": "住民が困っている様子を見たら、規定を無視してその場で特別に受理してあげること。"
      },
      {
        "id": "B",
        "text": "規則は規則であると強調し、住民が納得するまで口頭で厳しく反論すること。"
      },
      {
        "id": "C",
        "text": "断る理由を丁寧に説明した上で、次にどうすれば取得できるか具体的な手順を示すこと。"
      },
      {
        "id": "D",
        "text": "他の自治体の窓口へ行くよう指示し、速やかに対応を終了させること。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Đoạn 2 nêu: giải thích lý do quy định kèm theo hướng dẫn giải pháp thay thế, giúp người dân biết cần bổ sung giấy tờ gì và làm ở đâu.",
    "distractorExplanations": {
      "A": "Tác giả nhấn mạnh không được phá vỡ quy định.",
      "B": "Tranh cãi gay gắt với dân là sai tác phong.",
      "D": "Đùn đẩy sang nơi khác là vô trách nhiệm."
    }
  },
  {
    "id": "N2_07_M11_09",
    "typeId": "N2-RD-MID",
    "category": "Mondai 11: 中文読解",
    "passage": "　公務員や行政窓口の職員には、公平性と正確性が何よりも強く求められる。法令や規則に基づかない例外的な処理を安易に認めてしまえば、市民全体の信頼を損なうことになりかねないからである。そのため、窓口での応対が時に「形式主義」や「杓子定規（しゃくしじょうぎ）」と批判されることがあっても、一定のルールを厳格に順守することは公の責務として不可欠である。\n\n　しかしながら、規則を守ることと、利用者の心情に寄り添うことは決して矛盾するものではない。手続きの不備で書類が受理できない場合でも、単に「規定ですから無理です」と突き放すのと、「恐れ入りますが、法的な要件を満たすためにこの証明書が必要となります。取得にはこのような方法がございます」と丁寧に手順を示すのとでは、利用者が受ける印象は雲泥の差となる。\n\n　真の「質の高い行政サービス」とは、法の厳格さを維持しつつも、説明の言葉に温かみと共感を持たせることにある。ルールを機械的に適用するだけにとどまらず、困っている住民が次にどのような行動を取ればよいのかを導く姿勢こそが、これからの行政従事者に求められているプロフェッショナリズムなのである。",
    "stem": "本文全体を通じて、筆者がこれからの行政従事者に求めている姿勢は何か。",
    "options": [
      {
        "id": "A",
        "text": "対面での応対を避け、すべての業務をAIによる自動応答に任せきりにする姿勢。"
      },
      {
        "id": "B",
        "text": "感情を一切排除し、機械のように定められたマニュアルの文言だけを復唱する姿勢。"
      },
      {
        "id": "C",
        "text": "すべての権限を住民に委ね、職員自身の判断による説明を放棄する姿勢。"
      },
      {
        "id": "D",
        "text": "法の厳格さを守りながらも、困っている住民の立場に立ち、温かく次の行動へ導く姿勢。"
      }
    ],
    "correctAnswer": "D",
    "explanation": "Đoạn cuối tóm lược: giữ vững tính chuẩn mực của pháp luật nhưng phải có sự thấu cảm, giải thích có tâm và định hướng hành động cho công dân.",
    "distractorExplanations": {
      "A": "Không phó mặc hoàn toàn cho máy.",
      "B": "Tác giả phê phán lối làm việc máy móc.",
      "C": "Không buông bỏ trách nhiệm công vụ."
    }
  },
  {
    "id": "N2_07_M12_01",
    "typeId": "N2-RD-COMP",
    "category": "Mondai 12: 統合理解",
    "passage": "［Aの文章］\n　自治体の行政文書を完全に電子化し、ペーパーレスを徹底することは、環境保護と経費削減の観点から急務である。紙の印刷費や保管スペースの削減だけでなく、検索性の向上により過去の事例照会にかかる時間は大幅に短縮される。また、自然災害が発生した際にも、クラウド上にデータが安全にバックアップされていれば、被災後直ちに住民支援業務を再開できる。伝統的な紙への愛着や一時的な移行コストを理由に電子化を遅らせるべきではなく、全庁を挙げて迅速に完全移行を断行すべきである。\n\n［Bの文章］\n　行政手続きの電子化が業務の効率化をもたらすことは疑いようもないが、紙の媒体が持つ独自の安全性や信頼性を軽視してはならない。大規模な停電や通信障害、あるいは深刻なサイバー攻撃が発生した際、デジタルシステムのみに依存した組織は完全に機能不全に陥るリスクを抱えている。重要な公文書や緊急時の住民名簿などについては、万一の事態に備えて物理的な紙の台帳や原本を手元に残しておくことが、危機管理上の賢明な選択である。効率性と安全保障のバランスを見極めた段階的な導入こそが望ましい。",
    "stem": "災害や非常時におけるデータの取り扱いについて、AとBの主張の違いはどこにあるか。",
    "options": [
      {
        "id": "A",
        "text": "Aはクラウドのバックアップで安全に再開できるとし、Bは停電や障害に備えて紙の原本を残すべきとする。"
      },
      {
        "id": "B",
        "text": "Aは紙の保管こそが最も安全だと主張し、Bはクラウド技術への完全依存を推奨している。"
      },
      {
        "id": "C",
        "text": "AもBも、自然災害への備えとしては紙の台帳だけが唯一の解決策であると述べている。"
      },
      {
        "id": "D",
        "text": "AもBも、サイバー攻撃のリスクがあるため電子化を全面的に撤回すべきだと主張している。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Tác giả A cho rằng lưu trữ đám mây giúp phục hồi công việc tức thì sau thiên tai; tác giả B cảnh báo cúp điện hoặc tấn công mạng sẽ làm tê liệt hệ thống số nên cần lưu giữ sổ sách giấy tờ dự phòng.",
    "distractorExplanations": {
      "B": "Bị đảo ngược lập trường giữa A và B.",
      "C": "A hoàn toàn ủng hộ số hóa đám mây chứ không chuộng giấy.",
      "D": "Cả hai đều không đòi hủy bỏ số hóa."
    }
  },
  {
    "id": "N2_07_M12_02",
    "typeId": "N2-RD-COMP",
    "category": "Mondai 12: 統合理解",
    "passage": "［Aの文章］\n　自治体の行政文書を完全に電子化し、ペーパーレスを徹底することは、環境保護と経費削減の観点から急務である。紙の印刷費や保管スペースの削減だけでなく、検索性の向上により過去の事例照会にかかる時間は大幅に短縮される。また、自然災害が発生した際にも、クラウド上にデータが安全にバックアップされていれば、被災後直ちに住民支援業務を再開できる。伝統的な紙への愛着や一時的な移行コストを理由に電子化を遅らせるべきではなく、全庁を挙げて迅速に完全移行を断行すべきである。\n\n［Bの文章］\n　行政手続きの電子化が業務の効率化をもたらすことは疑いようもないが、紙の媒体が持つ独自の安全性や信頼性を軽視してはならない。大規模な停電や通信障害、あるいは深刻なサイバー攻撃が発生した際、デジタルシステムのみに依存した組織は完全に機能不全に陥るリスクを抱えている。重要な公文書や緊急時の住民名簿などについては、万一の事態に備えて物理的な紙の台帳や原本を手元に残しておくことが、危機管理上の賢明な選択である。効率性と安全保障のバランスを見極めた段階的な導入こそが望ましい。",
    "stem": "行政の電子化（ペーパーレス化）の進め方について、AとBの共通点および相違点として正しいものはどれか。",
    "options": [
      {
        "id": "A",
        "text": "両者とも紙の文書の完全廃止を求めており、導入のスピード感についても全く同じ意見である。"
      },
      {
        "id": "B",
        "text": "両者とも電子化による業務効率化を認めつつも、Aは即時完全移行を求め、Bは危機管理とのバランスを重視した段階的導入を求めている。"
      },
      {
        "id": "C",
        "text": "Aは電子化の経費削減効果を否定しているのに対し、Bは紙の維持費がゼロであると主張している。"
      },
      {
        "id": "D",
        "text": "Aは市民向けのサービスのみを対象とし、Bは職員内部の連絡のみを電子化すべきと述べている。"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Cả A và B đều công nhận số hóa mang lại hiệu quả cao. Tuy nhiên A muốn chuyển đổi triệt để tức thì, còn B chủ trương từng bước thận trọng để bảo đảm an ninh dự phòng.",
    "distractorExplanations": {
      "A": "B không đồng ý bỏ giấy hoàn toàn.",
      "C": "A khẳng định hiệu quả giảm chi phí.",
      "D": "Không phân biệt chia rẽ đối tượng như vậy."
    }
  },
  {
    "id": "N2_07_M13_01",
    "typeId": "N2-RD-LONG",
    "category": "Mondai 13: 長文読解",
    "passage": "　都市部における住民コミュニティの希薄化が叫ばれて久しい。集合住宅の増加や共働き世帯の一般化、さらには個人のプライバシーを重視する生活様式の浸透に伴い、かつて地域社会の基盤であった「町内会」や「自治会」への加入率は年々低下の一途をたどっている。「役員の負担が重い」「行事に参加する時間がない」といった理由から、若い世代を中心に退会や未加入を選択する住民が増加しているのは紛れもない事実である。\n\n　しかし、この地域の結びつきの低下は、平常時には見えにくい深刻な脆弱性を都市にもたらしている。その最たるものが、大規模災害時における「共助」の機能不全である。地震や水害が発生した直後、行政や消防などの公的救助（公助）の手がすべての被災現場に行き届くには、どうしても一定の時間を要する。その初動段階において、倒壊家屋からの救出や避難所での秩序ある物資配分を支えるのは、近隣住民同士が普段から培ってきた人間関係にほかならない。誰がどこに住んでおり、どの一軒家に支援を要する高齢者がいるかという基礎情報は、日頃のコミュニティ活動を通じてしか共有され得ないのである。\n\n　さらに、平時においても、孤立死の防止や子育て世代の見守りといった地域福祉の課題は、行政の力だけで網羅できるものではない。地域に顔見知りがいるという安心感は、犯罪の抑止や住民の精神的な健康にも目に見えない形で大きく寄与している。\n\n　したがって、私たちは今、町内会組織を単に「過去の慣習」として切り捨てるのではなく、現代の生活実態に即した形で再構築する知恵を絞らねばならない。行事を厳選して役員の業務をデジタル化し、負担を極力軽減しながらも、最低限の「顔の見える関係」を維持する新しいコミュニティのあり方を模索することが、持続可能な都市生活を築く鍵なのである。",
    "stem": "都市部で町内会や自治会への加入率が低下している背景として、本文で挙げられているものはどれか。",
    "options": [
      {
        "id": "A",
        "text": "集合住宅の建築基準法が改正され、町内会の結成が禁止されたこと。"
      },
      {
        "id": "B",
        "text": "市役所がすべての町内会費を値上げし、市民の反発を招いたこと。"
      },
      {
        "id": "C",
        "text": "プライバシー重視の生活様式に加え、役員の負担や時間の制約があること。"
      },
      {
        "id": "D",
        "text": "若者が地域の防災訓練を完全に不要であると考えていること。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Đoạn 1 nêu: lối sống coi trọng sự riêng tư cá nhân, gia đình bận rộn cả hai vợ chồng đi làm, cùng với gánh nặng làm cán bộ hội và không có thời gian dự sự kiện.",
    "distractorExplanations": {
      "A": "Luật không cấm thành lập hội.",
      "B": "Không nói thị xã tăng hội phí.",
      "D": "Không phải thanh niên cho rằng diễn tập là vô ích."
    }
  },
  {
    "id": "N2_07_M13_02",
    "typeId": "N2-RD-LONG",
    "category": "Mondai 13: 長文読解",
    "passage": "　都市部における住民コミュニティの希薄化が叫ばれて久しい。集合住宅の増加や共働き世帯の一般化、さらには個人のプライバシーを重視する生活様式の浸透に伴い、かつて地域社会の基盤であった「町内会」や「自治会」への加入率は年々低下の一途をたどっている。「役員の負担が重い」「行事に参加する時間がない」といった理由から、若い世代を中心に退会や未加入を選択する住民が増加しているのは紛れもない事実である。\n\n　しかし、この地域の結びつきの低下は、平常時には見えにくい深刻な脆弱性を都市にもたらしている。その最たるものが、大規模災害時における「共助」の機能不全である。地震や水害が発生した直後、行政や消防などの公的救助（公助）の手がすべての被災現場に行き届くには、どうしても一定の時間を要する。その初動段階において、倒壊家屋からの救出や避難所での秩序ある物資配分を支えるのは、近隣住民同士が普段から培ってきた人間関係にほかならない。誰がどこに住んでおり、どの一軒家に支援を要する高齢者がいるかという基礎情報は、日頃のコミュニティ活動を通じてしか共有され得ないのである。\n\n　さらに、平時においても、孤立死の防止や子育て世代の見守りといった地域福祉の課題は、行政の力だけで網羅できるものではない。地域に顔見知りがいるという安心感は、犯罪の抑止や住民の精神的な健康にも目に見えない形で大きく寄与している。\n\n　したがって、私たちは今、町内会組織を単に「過去の慣習」として切り捨てるのではなく、現代の生活実態に即した形で再構築する知恵を絞らねばならない。行事を厳選して役員の業務をデジタル化し、負担を極力軽減しながらも、最低限の「顔の見える関係」を維持する新しいコミュニティのあり方を模索することが、持続可能な都市生活を築く鍵なのである。",
    "stem": "大規模災害の発生時において、地域コミュニティ（共助）が不可欠とされる最大の理由は何か。",
    "options": [
      {
        "id": "A",
        "text": "公的な避難所は町内会員しか利用できず、非会員は立ち入りが禁止されるから。"
      },
      {
        "id": "B",
        "text": "消防署や警察は災害時に一切出動せず、住民が独力で消火活動を行わなければならないから。"
      },
      {
        "id": "C",
        "text": "被災した家屋の解体工事を、町内会の役員が無償で請け負う義務があるから。"
      },
      {
        "id": "D",
        "text": "公的機関の救助が行き届くまでの間、近隣住民同士の協力で救出や物資配分を支える必要があるから。"
      }
    ],
    "correctAnswer": "D",
    "explanation": "Đoạn 2 nêu: ngay sau thảm họa, lực lượng cứu hộ nhà nước (công trợ) chưa thể tới ngay mọi ngóc ngách, nên giai đoạn đầu phải nhờ người dân lân cận cứu nạn và điều phối đồ cứu trợ.",
    "distractorExplanations": {
      "A": "Nơi lánh nạn công cộng dành cho mọi người, không phân biệt hội viên.",
      "B": "Cảnh sát và cứu hỏa vẫn làm nhiệm vụ nhưng cần thời gian tiếp cận.",
      "C": "Hội dân cư không phải công ty phá dỡ nhà miễn phí."
    }
  },
  {
    "id": "N2_07_M13_03",
    "typeId": "N2-RD-LONG",
    "category": "Mondai 13: 長文読解",
    "passage": "　都市部における住民コミュニティの希薄化が叫ばれて久しい。集合住宅の増加や共働き世帯の一般化、さらには個人のプライバシーを重視する生活様式の浸透に伴い、かつて地域社会の基盤であった「町内会」や「自治会」への加入率は年々低下の一途をたどっている。「役員の負担が重い」「行事に参加する時間がない」といった理由から、若い世代を中心に退会や未加入を選択する住民が増加しているのは紛れもない事実である。\n\n　しかし、この地域の結びつきの低下は、平常時には見えにくい深刻な脆弱性を都市にもたらしている。その最たるものが、大規模災害時における「共助」の機能不全である。地震や水害が発生した直後、行政や消防などの公的救助（公助）の手がすべての被災現場に行き届くには、どうしても一定の時間を要する。その初動段階において、倒壊家屋からの救出や避難所での秩序ある物資配分を支えるのは、近隣住民同士が普段から培ってきた人間関係にほかならない。誰がどこに住んでおり、どの一軒家に支援を要する高齢者がいるかという基礎情報は、日頃のコミュニティ活動を通じてしか共有され得ないのである。\n\n　さらに、平時においても、孤立死の防止や子育て世代の見守りといった地域福祉の課題は、行政の力だけで網羅できるものではない。地域に顔見知りがいるという安心感は、犯罪の抑止や住民の精神的な健康にも目に見えない形で大きく寄与している。\n\n　したがって、私たちは今、町内会組織を単に「過去の慣習」として切り捨てるのではなく、現代の生活実態に即した形で再構築する知恵を絞らねばならない。行事を厳選して役員の業務をデジタル化し、負担を極力軽減しながらも、最低限の「顔の見える関係」を維持する新しいコミュニティのあり方を模索することが、持続可能な都市生活を築く鍵なのである。",
    "stem": "町内会等の将来像について、筆者が最終的に提案している解決策はどのようなものか。",
    "options": [
      {
        "id": "A",
        "text": "役員の負担を軽減し行事を整理しつつ、現代に適した形で顔の見える関係を維持すること。"
      },
      {
        "id": "B",
        "text": "町内会制度を即刻廃止し、すべての地域福祉と防災を行政の税金で賄うこと。"
      },
      {
        "id": "C",
        "text": "昔ながらの慣習を一切変えずに厳守し、未加入者には厳しい罰則を科すこと。"
      },
      {
        "id": "D",
        "text": "すべての住民活動をインターネット上の仮想空間だけに限定し、対面での接触をなくすこと。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Đoạn cuối nhấn mạnh: không vứt bỏ hội dân cư mà cần cải tiến, tinh gọn sự kiện, số hóa công việc quản lý để giảm gánh nặng mà vẫn giữ được mối quan hệ quen biết xóm giềng.",
    "distractorExplanations": {
      "B": "Tác giả chỉ ra một mình nhà nước không thể bao quát hết.",
      "C": "Không bảo thủ áp đặt phạt vạ.",
      "D": "Vẫn cần giữ mối quan hệ 'biết mặt nhau' thực tế."
    }
  },
  {
    "id": "N2_07_M14_01",
    "typeId": "N2-RD-INFO",
    "category": "Mondai 14: 情報検索",
    "passage": "市民活動交流センター 施設利用のご案内\n\n【利用区分と基本料金（1時間あたり）】\n・第1会議室（定員20名）：800円（プロジェクター完備・追加料金なし）\n・第2会議室（定員40名）：1,500円（マイク設備あり・追加料金なし）\n・多目的ホール（定員100名）：3,500円（音響・照明装置一式利用は別途1回1,000円）\n※市外在住者または営利目的（入場料徴収・商品の販売等）の利用は、上記料金の1.5倍となります。\n\n【利用申し込みと予約受付期間】\n・受付開始：利用希望日の3か月前の初日（午前9:00）より受付。\n・申込方法：窓口での直接申請、または市の公共施設予約システム（要事前登録）。\n・利用日の7日前までに利用料金の全額納付が必要です（納付完了で本予約確定）。\n\n【予約の変更・キャンセル規定】\n・利用日の8日前までのキャンセル：納付済み利用料金の全額（100％）を返金。\n・利用日の7日前から2日前までのキャンセル：納付済み利用料金の半額（50％）を返金。\n・前日および当日のキャンセル：返金なし（0％）。\n※台風等の自然災害により施設側が閉館を判断した場合は、時期にかかわらず全額返金いたします。",
    "stem": "市内在住のボランティア団体が、会員30名で第2会議室を平日に3時間利用する場合、利用料金の合計はいくらになるか。",
    "options": [
      {
        "id": "A",
        "text": "2,400円"
      },
      {
        "id": "B",
        "text": "4,500円"
      },
      {
        "id": "C",
        "text": "6,750円"
      },
      {
        "id": "D",
        "text": "10,500円"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Đoàn thể thiện nguyện trong thành phố (không phụ thu), 30 người nên chọn Phòng họp số 2 (sức chứa 40 người). Đơn giá 1,500 yên/giờ x 3 giờ = 4,500 yên.",
    "distractorExplanations": {
      "A": "2,400 yên là giá của Phòng họp số 1 (sức chứa chỉ 20 người, không đủ cho 30 người).",
      "C": "6,750 yên là giá bị tính 1.5 lần ngoại thành/thương mại.",
      "D": "10,500 yên là giá của Hội trường đa năng (3,500 yên x 3)."
    }
  },
  {
    "id": "N2_07_M14_02",
    "typeId": "N2-RD-INFO",
    "category": "Mondai 14: 情報検索",
    "passage": "市民活動交流センター 施設利用のご案内\n\n【利用区分と基本料金（1時間あたり）】\n・第1会議室（定員20名）：800円（プロジェクター完備・追加料金なし）\n・第2会議室（定員40名）：1,500円（マイク設備あり・追加料金なし）\n・多目的ホール（定員100名）：3,500円（音響・照明装置一式利用は別途1回1,000円）\n※市外在住者または営利目的（入場料徴収・商品の販売等）の利用は、上記料金の1.5倍となります。\n\n【利用申し込みと予約受付期間】\n・受付開始：利用希望日の3か月前の初日（午前9:00）より受付。\n・申込方法：窓口での直接申請、または市の公共施設予約システム（要事前登録）。\n・利用日の7日前までに利用料金の全額納付が必要です（納付完了で本予約確定）。\n\n【予約の変更・キャンセル規定】\n・利用日の8日前までのキャンセル：納付済み利用料金の全額（100％）を返金。\n・利用日の7日前から2日前までのキャンセル：納付済み利用料金の半額（50％）を返金。\n・前日および当日のキャンセル：返金なし（0％）。\n※台風等の自然災害により施設側が閉館を判断した場合は、時期にかかわらず全額返金いたします。",
    "stem": "予約のキャンセルと返金について、規定に合致しているものはどれか。",
    "options": [
      {
        "id": "A",
        "text": "台風によりセンターが閉館した場合でも、当日キャンセルは一切返金されない。"
      },
      {
        "id": "B",
        "text": "利用日の前日にキャンセルしても、理由を問わず全額が返金される。"
      },
      {
        "id": "C",
        "text": "利用日の5日前にキャンセルした場合、納付済み料金の50％が返金される。"
      },
      {
        "id": "D",
        "text": "利用日の10日前にキャンセルした場合、手数料として半額が差し引かれる。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Quy định nêu: hủy từ 7 ngày đến 2 ngày trước ngày sử dụng thì được hoàn lại 50% tiền (5 ngày trước rơi vào khung này).",
    "distractorExplanations": {
      "A": "Nếu bão khiến trung tâm phải đóng cửa thì được hoàn 100% bất kể thời điểm.",
      "B": "Hủy ngày hôm trước hoặc trong ngày thì không được hoàn tiền (0%).",
      "D": "Hủy từ 8 ngày trở về trước được hoàn lại 100%."
    }
  }
]

if __name__ == '__main__':
    items = get_n2_mock_07_sec1_items()
    print(f"Loaded {len(items)} Section 1 items.")
