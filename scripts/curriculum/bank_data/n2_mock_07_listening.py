# -*- coding: utf-8 -*-
"""
JLPT N2 Mock Exam #07 - Section 2: Listening Comprehension (聴解)
Full 30-item exam structure:
- Mondai 1: 課題理解 (5 items) [Q1 - Q5] (Task-based)
- Mondai 2: ポイント理解 (6 items) [Q6 - Q11] (Point comprehension, 6.0s pause)
- Mondai 3: 概要理解 (5 items) [Q12 - Q16] (Summary/Gist, 4 spoken choices)
- Mondai 4: 即時応答 (11 items) [Q17 - Q27] (Strictly 3 spoken choices: 1番, 2番, 3番)
- Mondai 5: 統合理解 (3 items) [Q28 - Q30] (Integrated: 2 discussion, 1 comparative)
Total: 30 items
"""

def get_n2_mock_07_listening_items():
    return [
  {
    "id": "N2_07_M1_L01",
    "typeId": "N2-LIS-TASK",
    "category": "Mondai 1: 課題理解",
    "script": "市役所の市民課窓口で、男性と女性の職員が転出届の手続きについて話しています。男性はこの後、まず何をしなければなりませんか。\n\n男：「すみません、来月他県へ引っ越すことになったので、転出の手続きをしたいのですが。」\n女：「ご転出ですね。ご本人様確認のため、マイナンバーカードか運転免許証はお持ちでしょうか。」\n男：「はい、マイナンバーカードを持っています。」\n女：「ありがとうございます。マイナンバーカードをお持ちでしたら、転出証明書の発行を受ける代わりに、カードを用いた特例転出が可能です。ただし、転出届の申請用紙に新住所と転出予定日をご記入いただく必要があります。」\n男：「分かりました。用紙はあちらの記載台にありますか。」\n女：「はい、記載台の『3番』の用紙です。ご記入後、番号札をお取りになってお待ちください。順番が来ましたら、カードの暗証番号を入力していただきます。」\n男：「承知しました。では、まず用紙に書いてきます。」",
    "stem": "男性はこの後、まず何をしなければなりませんか。",
    "options": [
      {
        "id": "A",
        "text": "記載台へ行って転出届の申請用紙を記入する。"
      },
      {
        "id": "B",
        "text": "順番待ちの番号札を取ってロビーで待つ。"
      },
      {
        "id": "C",
        "text": "窓口の端末にマイナンバーカードの暗証番号を入力する。"
      },
      {
        "id": "D",
        "text": "転出証明書の紙の原本を窓口で受け取る。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Nữ nhân viên hướng dẫn: trước tiên cần lấy tờ khai số 3 tại bàn hướng dẫn và điền địa chỉ mới cùng ngày chuyển đi ('申請用紙に新住所と転出予定日をご記入いただく必要があります'). Nam công dân xác nhận sẽ đi viết đơn trước ('まず用紙に書いてきます').",
    "distractorExplanations": {
      "B": "Lấy số thứ tự sau khi đã điền xong đơn.",
      "C": "Nhập mã PIN khi đến lượt gọi số tại quầy.",
      "D": "Người có thẻ My Number chuyển đi theo dạng đặc thù không cần phát hành giấy chứng nhận chuyển đi bằng giấy."
    }
  },
  {
    "id": "N2_07_M1_L02",
    "typeId": "N2-LIS-TASK",
    "category": "Mondai 1: 課題理解",
    "script": "会社で、男性の課長と女性社員が来月発行する社内報の原稿について話しています。女性社員はこの後、何を修正しますか。\n\n男：「高橋さん、社内報の最終ゲラ、確認させてもらったよ。レイアウトも写真の配置も見やすくていいね。」\n女：「ありがとうございます、課長。」\n男：「ただね、3ページの『新任マネージャー紹介』の記事なんだけど、営業二課の鈴木さんの役職名が『課長代理』になっているよ。彼は先月の昇進で『課長』になっているから直しておいて。」\n女：「あっ、大変失礼いたしました。すぐに直します。あと、隣の座談会記事の日時ですが、来週月曜日になっていますが大丈夫でしょうか。」\n男：「ああ、そっちは先週の役員会で承認済みだからそのままでいいよ。それと、裏表紙の印刷部数の表記も確認しておいてね。」\n女：「はい、部数は印刷会社に確認済みです。では、役職の箇所を直ちに修正して再出力します。」",
    "stem": "女性社員はこの後、何を修正しますか。",
    "options": [
      {
        "id": "A",
        "text": "写真の配置とページレイアウトを変更する。"
      },
      {
        "id": "B",
        "text": "新任マネージャーの役職名の表記を直す。"
      },
      {
        "id": "C",
        "text": "座談会記事に記載された開催日時を修正する。"
      },
      {
        "id": "D",
        "text": "裏表紙の社内報の印刷部数の数値を変更する。"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Trưởng phòng chỉ ra lỗi duy nhất cần sửa: chức vụ của anh Suzuki bài trang 3 bị ghi là 'Phó phòng', trong khi tháng trước đã thăng chức lên 'Trưởng phòng' ('役職名が課長代理になっているよ...課長になっているから直しておいて').",
    "distractorExplanations": {
      "A": "Bố cục ảnh và trình bày được khen đẹp, không cần đổi.",
      "C": "Ngày giờ tọa đàm đã được duyệt, giữ nguyên.",
      "D": "Số lượng in đã xác nhận chuẩn với nhà in."
    }
  },
  {
    "id": "N2_07_M1_L03",
    "typeId": "N2-LIS-TASK",
    "category": "Mondai 1: 課題理解",
    "script": "マンションの集会所で、管理組合の理事長の女性と役員の男性が定期総会の準備について話しています。男性役員はこの後、まず何をしなければなりませんか。\n\n女：「中村さん、来週日曜日の定期総会ですが、議案書の印刷は無事に終わりましたね。」\n男：「はい、全120戸分の印刷と封筒への封入作業は完了しています。」\n女：「助かりました。それで、総会に出席できない住民の方から『委任状』や『議決権行使書』を事前に集める必要がありますね。」\n男：「はい。各住戸の郵便受けに議案書を投函して、回収期日を今週金曜日に設定してあります。」\n女：「ええ。ただ、投函する前に、案内状の出欠返信締切日の日付に誤記がないか、もう一度だけ確認してほしいの。去年、日付の曜日が間違っていて混乱したことがあったから。」\n男：「分かりました。全戸投函を始める前に、案内状の日付と曜日を今すぐ照合します。」\n女：「お願いね。会場のマイク設備や机の配置は前日の土曜日に確認すれば間に合うから。」",
    "stem": "男性役員はこの後、まず何をしなければなりませんか。",
    "options": [
      {
        "id": "A",
        "text": "集会所のマイク設備と机の配置を点検する。"
      },
      {
        "id": "B",
        "text": "全住戸の郵便受けに議案書の封筒を投函する。"
      },
      {
        "id": "C",
        "text": "議案書に同封する案内状の日付と曜日を確認する。"
      },
      {
        "id": "D",
        "text": "全120戸分の議案書を印刷機で印刷する。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Bà chủ tịch yêu cầu kiểm tra kỹ lại ngày tháng và thứ trong giấy hẹn trước khi phát đơn vào hòm thư ('投函する前に、案内状の出欠返信締切日の日付に誤記がないか、もう一度だけ確認してほしいの'). Nam cán bộ xác nhận sẽ đối chiếu ngay lập tức.",
    "distractorExplanations": {
      "A": "Kiểm tra loa đài hội trường để thứ Bảy trước ngày họp làm sau.",
      "B": "Phát vào hòm thư chỉ làm sau khi đã kiểm tra xong ngày tháng.",
      "D": "Việc in 120 bộ đã hoàn tất từ trước."
    }
  },
  {
    "id": "N2_07_M1_L04",
    "typeId": "N2-LIS-TASK",
    "category": "Mondai 1: 課題理解",
    "script": "オフィスで、男性社員と女性の先輩社員が部署の備品購入について話しています。男性社員はこの後、まず何を提出しなければなりませんか。\n\n男：「先輩、プロジェクトルームのホワイトボードとプロジェクターの買い替えですが、カタログから候補を選定しました。」\n女：「ありがとう。合計金額はいくらくらいになりそう？」\n男：「2点合わせて約8万円です。」\n女：「うちの会社の規程では、5万円を超える備品を購入する場合、先に発注するんじゃなくて、見積書を添えて『事前購入伺い書』を経理課に出さないといけないのよ。」\n男：「あっ、そうだったんですね。ネット通販の領収書を後から精算すればいいと思っていました。」\n女：「それは5万円未満の場合ね。業者から取り寄せた正式な見積書のPDFがある？」\n男：「はい、先ほど販売店からメールで届きました。」\n女：「じゃあ、社内ポータルから『事前伺い書』を作成して、見積書を添付して部長へ決裁申請を上げてちょうだい。」\n男：「承知しました。すぐに申請データを作成します。」",
    "stem": "男性社員はこの後、まず何を提出しなければなりませんか。",
    "options": [
      {
        "id": "A",
        "text": "販売店への正式な注文書と支払請求書。"
      },
      {
        "id": "B",
        "text": "ネット通販で購入した商品の領収書。"
      },
      {
        "id": "C",
        "text": "プロジェクトルームの備品廃棄申請書。"
      },
      {
        "id": "D",
        "text": "見積書を添付した備品の事前購入伺い書。"
      }
    ],
    "correctAnswer": "D",
    "explanation": "Nữ tiền bối giải thích quy định công ty: thiết bị trên 5 vạn yên phải nộp giấy trình duyệt mua trước (事前購入伺い書) kèm báo giá (見積書) lên trưởng phòng ('事前伺い書を作成して、見積書を添付して部長へ決裁申請を上げてちょうだい').",
    "distractorExplanations": {
      "A": "Chưa được đặt hàng khi chưa duyệt dự toán.",
      "B": "Hóa đơn thanh toán sau chỉ áp dụng cho đồ dưới 5 vạn yên.",
      "C": "Không có yêu cầu nộp đơn thanh lý thiết bị cũ."
    }
  },
  {
    "id": "N2_07_M1_L05",
    "typeId": "N2-LIS-TASK",
    "category": "Mondai 1: 課題理解",
    "script": "地域センターで、訓練本部の男性責任者と女性職員が当日の進行について話しています。女性職員はこの後、どこへ向かわなければなりませんか。\n\n男：「間もなく午前9時から総合防災訓練が始まります。各自の持ち場を確認します。」\n女：「はい、本部長。私は当初、中央広場での初期消火体験コーナーの担当でしたが、予定通りでよろしいでしょうか。」\n男：「あ、実はさっき第1避難所の小学校体育館から連絡があってね。受付の受付名簿の配布と高齢者の誘導スタッフが1名急病で来られなくなったそうなんだ。」\n女：「そうなんですか。それは大変ですね。」\n男：「消火器体験の方は消防署の隊員さんが2名増員されたから大丈夫だ。悪いんだけど、君は今すぐ小学校の体育館へ行って、受付誘導の応援に入ってくれないか。」\n女：「分かりました。避難者名簿の用紙を持って、直ちに小学校へ向かいます。」",
    "stem": "女性職員はこの後、どこへ向かわなければなりませんか。",
    "options": [
      {
        "id": "A",
        "text": "第1避難所となっている小学校の体育館。"
      },
      {
        "id": "B",
        "text": "初期消火体験を行う中央広場のコーナー。"
      },
      {
        "id": "C",
        "text": "訓練機材を保管している消防署の車庫。"
      },
      {
        "id": "D",
        "text": "本部が設置されている地域センターの救護室。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Trưởng ban điều động nhân sự khẩn cấp: điểm lánh nạn trường tiểu học bị thiếu người tiếp đón và hướng dẫn người già do có người ốm đột xuất, nên yêu cầu nữ nhân viên sang đó tiếp viện ngay ('今すぐ小学校の体育館へ行って、受付誘導の応援に入ってくれないか').",
    "distractorExplanations": {
      "B": "Khu dập lửa quảng trường trung tâm đã có lính cứu hỏa tiếp viện.",
      "C": "Không phải đi gara trạm cứu hỏa.",
      "D": "Không đến phòng cứu trợ."
    }
  },
  {
    "id": "N2_07_M2_L01",
    "typeId": "N2-LIS-POINT",
    "category": "Mondai 2: ポイント理解",
    "script": "市役所の交通対策課で、男性職員と女性職員がコミュニティバスの見直しについて話しています。今回ルートを変更することになった最大の理由は何ですか。\n\n（6.0秒の無音）\n\n男：「来月から運行が始まる新しいコミュニティバスの巡回ルート、市民説明会でも好評だったね。」\n女：「ええ。当初は駅と市役所を最短距離で結ぶルートを検討していましたが、最終的には総合病院と大型スーパーを経由する大回りルートに変更しましたね。」\n男：「うん。燃料費の高騰や運転手不足の面からは直線ルートの方が望ましかったんだけど、アンケート調査を見たら、高齢者の通院や日用品の買い物手段がなくて困っているという声が圧倒的に多かったからね。」\n女：「そうですね。運行本数を少し減らしてでも、生活に直結する医療機関や商店街へのアクセスを優先した判断は正しかったと思います。」\n男：「ああ。地域の生活インフラとしての役割を一番に考えた結果だね。」",
    "stem": "今回ルートを変更することになった最大の理由は何ですか。",
    "options": [
      {
        "id": "A",
        "text": "バスの燃料費を削減し、運行コストを下げるため。"
      },
      {
        "id": "B",
        "text": "高齢者の通院や買い物の利便性を確保するため。"
      },
      {
        "id": "C",
        "text": "駅と市役所の間を最短時間で結ぶため。"
      },
      {
        "id": "D",
        "text": "バスの運転手の不足を解消するため。"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Nam nhân viên nêu rõ lý do quyết định: khảo sát ý kiến cho thấy người cao tuổi gặp khó khăn lớn về đi khám bệnh và đi chợ, nên tuyến xe được uốn qua bệnh viện và siêu thị ('高齢者の通院や日用品の買い物手段がなくて困っているという声が圧倒的に多かったからね').",
    "distractorExplanations": {
      "A": "Tuyến đường vòng tốn xăng hơn, không phải để giảm chi phí nhiên liệu.",
      "C": "Đã từ bỏ tuyến đường thẳng ngắn nhất.",
      "D": "Không phải để giải quyết thiếu lái xe."
    }
  },
  {
    "id": "N2_07_M2_L02",
    "typeId": "N2-LIS-POINT",
    "category": "Mondai 2: ポイント理解",
    "script": "会社で、人事課の女性社員が新入社員にテレワークの留意点について説明しています。勤怠管理において特に注意すべき点として何が挙げられていますか。\n\n（6.0秒の無音）\n\n女：「在宅勤務を行う際の勤怠ルールについて説明します。自宅での作業は通勤のストレスがない反面、私生活との境界が曖昧になりがちです。業務開始と終了の打刻はもちろん必須ですが、それ以上に徹底してほしいのは『途中離席』の申告です。例えば、急な宅配便の受け取りや家事などで15分以上パソコンを離れる場合は、必ずチャットツールのステータスを離席にし、事後にシステムへ中抜け時間を登録してください。これを怠ると、実労働時間の把握ができなくなり、労務管理上のトラブルにつながります。」",
    "stem": "勤怠管理において特に注意すべき点として何が挙げられていますか。",
    "options": [
      {
        "id": "A",
        "text": "在宅勤務中のパソコン画面を常にカメラで録画すること。"
      },
      {
        "id": "B",
        "text": "毎朝8時までに全社員宛てに業務計画メールを送ること。"
      },
      {
        "id": "C",
        "text": "15分以上席を離れる際のステータス変更と中抜け登録。"
      },
      {
        "id": "D",
        "text": "終業後に上司と30分間の反省面談を毎日行うこと。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Nhân viên nhân sự nhấn mạnh điều đặc biệt cần chú ý: khi rời khỏi bàn máy tính từ 15 phút trở lên vì việc riêng thì bắt buộc đổi trạng thái sang 'vắng mặt' và đăng ký thời gian rời bàn ('15分以上パソコンを離れる場合は、必ずチャットツールのステータスを離席にし、事後にシステムへ中抜け時間を登録してください').",
    "distractorExplanations": {
      "A": "Không có yêu cầu quay video màn hình liên tục.",
      "B": "Không yêu cầu gửi email cho toàn thể công ty lúc 8h sáng.",
      "D": "Không họp kiểm điểm 30 phút mỗi ngày."
    }
  },
  {
    "id": "N2_07_M2_L03",
    "typeId": "N2-LIS-POINT",
    "category": "Mondai 2: ポイント理解",
    "script": "電話で、市民の男性と公民館の職員が施設利用について話しています。男性の予約申し込みが却下された理由は何ですか。\n\n（6.0秒の無音）\n\n男：「もしもし、先週申し込んだ来月10日の第1会議室の予約結果が『不許可』で届いたのですが、理由を教えていただけますか。」\n女：「はい、お名前とお申し込み内容を確認いたします。……佐藤様ですね。お申し込みいただいた『ギター教室』ですが、講師の方が入場料や受講料を生徒から徴収される予定となっておりますでしょうか。」\n男：「ええ、参加費として1人2,000円集める計画ですが。」\n女：「恐れ入ります。当公民館は社会教育法に基づく公共施設のため、営利を目的とした私塾や個人レッスンの事業にはご利用いただけない規定となっております。サークル等の会員同士の実費割り勘であれば可能ですが、講師報酬を伴う有償講座は対象外となります。」\n男：「ああ、営利目的とみなされたわけですね。理解しました。」",
    "stem": "男性の予約申し込みが却下された理由は何ですか。",
    "options": [
      {
        "id": "A",
        "text": "利用希望人数が会議室の定員を超えていたため。"
      },
      {
        "id": "B",
        "text": "利用申請の締め切り期日を過ぎて申し込んだため。"
      },
      {
        "id": "C",
        "text": "ギターの演奏音が騒音基準を超えていたため。"
      },
      {
        "id": "D",
        "text": "受講料を徴収する営利目的の利用に該当したため。"
      }
    ],
    "correctAnswer": "D",
    "explanation": "Nhân viên nhà văn hóa giải thích: cơ sở công cộng phi lợi nhuận cấm các lớp dạy có thu học phí mang tính thương mại/lợi nhuận cá nhân ('営利を目的とした私塾や個人レッスンの事業にはご利用いただけない規定となっております').",
    "distractorExplanations": {
      "A": "Không phải do quá số lượng người.",
      "B": "Đơn nộp đúng hạn, không quá hạn.",
      "C": "Chưa xét đến tiêu chuẩn âm thanh."
    }
  },
  {
    "id": "N2_07_M2_L04",
    "typeId": "N2-LIS-POINT",
    "category": "Mondai 2: ポイント理解",
    "script": "会社で、男性社員と女性社員が研修の感想について話しています。男性社員が研修で最も感銘を受けた指導法は何ですか。\n\n（6.0秒の無音）\n\n女：「課長、昨日までの新任管理職研修、いかがでしたか。」\n男：「うん、リーダーシップ論や目標管理の手法など色々学んだけど、一番ハッとさせられたのは『部下の自発的な課題発見を促す問いかけ方』だったよ。」\n女：「問いかけ方、ですか？」\n男：「そう。部下がミスをした時、つい『なぜできなかったのか』と過去の原因を詰問しがちだけど、それだと相手は萎縮して言い訳を探してしまう。そうではなくて、『次にどうすれば防げると思うか』と未来の行動へ意識を向けさせる質問をするんだ。これだけで部下の主体性が全く違ってくるという話にとても納得したよ。」\n女：「なるほど、反省ではなく次の改善策を自分で考えさせるわけですね。」",
    "stem": "男性社員が研修で最も感銘を受けた指導法は何ですか。",
    "options": [
      {
        "id": "A",
        "text": "原因を詰問せず、再発防止の行動を自ら考えさせる問いかけ。"
      },
      {
        "id": "B",
        "text": "部下の小さなミスも見逃さずにその場で厳しく叱責すること。"
      },
      {
        "id": "C",
        "text": "すべての業務指示を詳細なマニュアルにして配布すること。"
      },
      {
        "id": "D",
        "text": "目標達成度に応じて部下の給与や賞与を厳密に差別化すること。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Nam quản lý chia sẻ điều tâm đắc nhất: không truy vấn lý do thất bại trong quá khứ mà hỏi hướng tới tương lai để cấp dưới tự phát hiện giải pháp khắc phục ('部下の自発的な課題発見を促す問いかけ方...次にどうすれば防げると思うかと未来の行動へ意識を向けさせる').",
    "distractorExplanations": {
      "B": "Quát mắng ngay tại chỗ là điều tác giả khuyên nên tránh.",
      "C": "Không nói về việc phát cẩm nang chi tiết.",
      "D": "Không nói về phân hóa thưởng phạt."
    }
  },
  {
    "id": "N2_07_M2_L05",
    "typeId": "N2-LIS-POINT",
    "category": "Mondai 2: ポイント理解",
    "script": "町内会の集会で、役員の女性がゴミ集積所の対策について報告しています。今年新しく導入された効果的な対策は何ですか。\n\n（6.0秒の無音）\n\n女：「環境衛生部から、ゴミ収集ステーションのカラス被害対策についてご報告します。これまで防鳥ネットをかぶせていましたが、隙間から突かれて散乱する事例が多発していました。そこで先月より、各ステーションに『折りたたみ式の大型メッシュボックス』を試験配備いたしました。収集日以外はコンパクトに畳んで壁際に収納でき、ゴミ袋を完全に密閉して四方を囲む構造のため、カラスの被害が劇的に減少しました。住民の皆様にもボックス内への確実な収納をお願いいたします。」",
    "stem": "今年新しく導入された効果的な対策は何ですか。",
    "options": [
      {
        "id": "A",
        "text": "ステーション周辺に監視カメラを24時間設置したこと。"
      },
      {
        "id": "B",
        "text": "ゴミ袋を完全に密閉できる折りたたみ式メッシュボックスの配備。"
      },
      {
        "id": "C",
        "text": "夜間にカラスを追い払う強力なライトを導入したこと。"
      },
      {
        "id": "D",
        "text": "ゴミの収集時間を朝から夕方へ変更したこと。"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Báo cáo chỉ rõ biện pháp mới đem lại hiệu quả cao là lồng lưới kim loại dạng gập có thể bao bọc kín rác thải ('折りたたみ式の大型メッシュボックスを試験配備いたしました...ゴミ袋を完全に密閉して四方を囲む構造のため、カラスの被害が劇的に減少しました').",
    "distractorExplanations": {
      "A": "Không gắn camera giám sát.",
      "C": "Không dùng đèn đuổi ban đêm.",
      "D": "Không đổi giờ thu gom rác."
    }
  },
  {
    "id": "N2_07_M2_L06",
    "typeId": "N2-LIS-POINT",
    "category": "Mondai 2: ポイント理解",
    "script": "ラジオで、市民マラソン大会の実行委員がボランティア募集について案内しています。今年から変更された募集条件は何ですか。\n\n（6.0秒の無音）\n\n男：「今年で第10回を迎える緑市市民マラソン大会の運営ボランティアを募集しています。給水所でのドリンク配布やコース沿道の走路誘導など、大会を支えていただく大切な役割です。なお、昨年までは『市内在住または在勤・在学の高校生以上』に限定しておりましたが、遠方からの参加希望者が急増したことを受け、今年度より『市外在住の方』のエントリーも広く受け付けることといたしました。緑市のスポーツ振興に熱意のある皆様のご応募をお待ちしております。」",
    "stem": "今年から変更された募集条件は何ですか。",
    "options": [
      {
        "id": "A",
        "text": "ボランティア参加者全員に日当が支給されるようになったこと。"
      },
      {
        "id": "B",
        "text": "中学生や小学生の参加も認められるようになったこと。"
      },
      {
        "id": "C",
        "text": "市外に住んでいる人でもボランティアに応募できるようになったこと。"
      },
      {
        "id": "D",
        "text": "給水所の作業が廃止され、走路誘導のみの募集になったこと。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Ban tổ chức nêu rõ điểm mới của năm nay: trước đây chỉ nhận người sống/làm việc trong thành phố, nay mở rộng tiếp nhận cả người sống ngoài thành phố ('今年度より市外在住の方のエントリーも広く受け付けることといたしました').",
    "distractorExplanations": {
      "A": "Là hoạt động tình nguyện không nhận thù lao ngày.",
      "B": "Vẫn giữ độ tuổi từ học sinh cấp 3 trở lên, không nhận học sinh cấp 1, 2.",
      "D": "Vẫn có các nhiệm vụ phân phát nước uống bình thường."
    }
  },
  {
    "id": "N2_07_M3_L01",
    "typeId": "N2-LIS-GIST",
    "category": "Mondai 3: 概要理解",
    "script": "テレビの広報番組で、市役所の職員が話しています。\n\n男：「緑市では、子育て世帯の皆様が行政手続きをよりスムーズに行えるよう、今月より市役所本庁舎1階に『こども家庭支援総合窓口』を開設いたしました。これまで、児童手当の申請は市民課、保育園の入所相談は保育支援課、予防接種の問診票は健康増進課と、庁舎内の複数のフロアを回っていただく必要がございました。新しい総合窓口では、これらすべての相談や申請を一括して専任スタッフが承ります。小さなお子様連れでも安心して来庁いただけるよう、キッズスペースや授乳室も併設しておりますので、どうぞお気軽にご利用ください。」\n\n市の職員は何について話していますか。\n1番：子育て関連の行政手続きが一箇所でできるようになったこと\n2番：保育園の保育料が全額免除される新しい制度\n3番：市役所本庁舎の耐震改修工事のスケジュール\n4番：市内で開催される親子向けイベントの開催案内",
    "stem": "市の職員は何について話していますか。",
    "options": [
      {
        "id": "A",
        "text": "市内で開催される親子向けイベントの開催案内。"
      },
      {
        "id": "B",
        "text": "保育園の保育料が全額免除される新しい制度。"
      },
      {
        "id": "C",
        "text": "市役所本庁舎の耐震改修工事のスケジュール。"
      },
      {
        "id": "D",
        "text": "子育て関連の行政手続きが一箇所でできるようになったこと。"
      }
    ],
    "correctAnswer": "D",
    "explanation": "Nhân viên thị xã giới thiệu quầy một cửa mới: gộp toàn bộ các thủ tục con cái vốn phải đi nhiều tầng trước đây lại thành một quầy tổng hợp duy nhất tại tầng 1 ('これらすべての相談や申請を一括して専任スタッフが承ります').",
    "distractorExplanations": {
      "A": "Không phải thông báo sự kiện vui chơi.",
      "B": "Không nói miễn học phí nhà trẻ.",
      "C": "Không phải công trình sửa chữa trụ sở chống động đất."
    }
  },
  {
    "id": "N2_07_M3_L02",
    "typeId": "N2-LIS-GIST",
    "category": "Mondai 3: 概要理解",
    "script": "会社で、朝礼の場で社長が社員に話しています。\n\n男：「皆さん、おはようございます。今期、我が社は売上目標を大幅に達成し、順調な成長を続けています。しかし、業績の拡大と同じくらい、あるいはそれ以上に重要なのは『法令遵守と高い倫理観』です。どんなに優れた製品を世に送り出しても、一度の不正や情報の隠蔽があれば、長年築き上げた企業の社会的信用は一瞬で崩壊します。社内で少しでも疑問に思う慣行や不正の兆候を見かけた際は、決して見て見ぬ振りをせず、社内ホットラインやコンプライアンス相談窓口を迷わず活用してください。透明で誠実な組織風土を築くことが、持続的な成長の土台です。」\n\n社長が最も伝えたいことは何ですか。\n1番：売上目標を達成するための営業戦略\n2番：法令遵守の徹底と不正を許さない誠実な企業風土の重要性\n3番：新入社員の基本マナーと挨拶の徹底\n4番：社内ホットラインの電話番号変更の案内",
    "stem": "社長が最も伝えたいことは何ですか。",
    "options": [
      {
        "id": "A",
        "text": "法令遵守の徹底と不正を許さない誠実な企業風土の重要性。"
      },
      {
        "id": "B",
        "text": "売上目標を達成するための営業戦略。"
      },
      {
        "id": "C",
        "text": "新入社員の基本マナーと挨拶の徹底。"
      },
      {
        "id": "D",
        "text": "社内ホットラインの電話番号変更の案内。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Tổng giám đốc nhấn mạnh trọng tâm cốt lõi: tuân thủ pháp luật, giữ gìn đạo đức doanh nghiệp, không bao che sai phạm và xây dựng văn hóa công ty minh bạch ('法令遵守と高い倫理観...透明で誠実な組織風土を築くことが、持続的な成長の土台です').",
    "distractorExplanations": {
      "B": "Doanh số đã đạt rồi, điều muốn nhấn mạnh là đạo đức tuân thủ pháp luật.",
      "C": "Không nói về tác phong chào hỏi tân binh.",
      "D": "Không phải thông báo đổi số điện thoại."
    }
  },
  {
    "id": "N2_07_M3_L03",
    "typeId": "N2-LIS-GIST",
    "category": "Mondai 3: 概要理解",
    "script": "地域の集会で、防災専門家が講話を行っています。\n\n女：「皆様、地震への備えと聞くと、非常用持出袋や乾パンの用意を思い浮かべる方が多いと思います。もちろん備蓄も重要ですが、地震発生時の負傷原因の約半数は『家具の転倒や落下物』によるものです。つまり、家具の固定こそが、命を守るための第一歩なのです。寝室に背の高いタンスや本棚を置かないこと、突っ張り棒やL字金具で家具を壁に固定すること、そして食器棚の扉に開き防止ストッパーを付けること。これらは今日からでも実践できる対策です。まずは家の中の危険箇所を点検してみてください。」\n\n防災専門家は何が最も大切だと述べていますか。\n1番：非常用の食料や飲料水を1週間分備蓄すること\n2番：地震によるケガを防ぐために家具を固定すること\n3番：避難訓練に地域住民全員が必ず参加すること\n4番：地震保険に加入して住宅の損害に備えること",
    "stem": "防災専門家は何が最も大切だと述べていますか。",
    "options": [
      {
        "id": "A",
        "text": "非常用の食料や飲料水を1週間分備蓄すること。"
      },
      {
        "id": "B",
        "text": "地震によるケガを防ぐために家具を固定すること。"
      },
      {
        "id": "C",
        "text": "避難訓練に地域住民全員が必ず参加すること。"
      },
      {
        "id": "D",
        "text": "地震保険に加入して住宅の損害に備えること。"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Chuyên gia phòng chống thiên tai nêu rõ: nguyên nhân gây thương tích chiếm một nửa là đồ đạc đổ ngã, nên bước bảo vệ tính mạng đầu tiên và quan trọng nhất là chằng cố định bàn tủ, giá sách ('家具の固定こそが、命を守るための第一歩なのです').",
    "distractorExplanations": {
      "A": "Tích trữ đồ ăn thức uống có ích nhưng không phải trọng tâm bài nói.",
      "C": "Không nói về diễn tập cư dân.",
      "D": "Không nói về bảo hiểm nhà đất."
    }
  },
  {
    "id": "N2_07_M3_L04",
    "typeId": "N2-LIS-GIST",
    "category": "Mondai 3: 概要理解",
    "script": "カルチャーセンターの講座説明会で、館長が挨拶をしています。\n\n男：「定年退職を迎えた後、どのように日々を過ごすかは人生の後半における大きなテーマです。趣味を持つことは素晴らしいことですが、当センターでは単に新しい知識や技術を学ぶだけでなく、学んだことを地域に還元する講座に力を入れております。例えば、郷土史を学んだ方が観光ボランティアガイドとして活躍したり、パソコン講座を修了した方がシニア向けのITサポート役を務めたりしています。学ぶ喜びを他者とのつながりや社会貢献へと広げていく、そんな充実したセカンドライフを皆様と共に応援したいと考えております。」\n\n館長は何を伝えたいと考えていますか。\n1番：退職後の学びを社会貢献や人とのつながりに広げていくこと\n2番：定年退職後に再就職するための資格取得の方法\n3番：カルチャーセンターの講座受講料の割引制度\n4番：パソコン講座のカリキュラムと操作方法",
    "stem": "館長は何を伝えたいと考えていますか。",
    "options": [
      {
        "id": "A",
        "text": "カルチャーセンターの講座受講料の割引制度。"
      },
      {
        "id": "B",
        "text": "定年退職後に再就職するための資格取得の方法。"
      },
      {
        "id": "C",
        "text": "退職後の学びを社会貢献や人とのつながりに広げていくこと。"
      },
      {
        "id": "D",
        "text": "パソコン講座のカリキュラムと操作方法。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Viện trưởng trung tâm văn hóa truyền tải thông điệp: không dừng lại ở học sở thích cá nhân mà biến kiến thức đó thành hoạt động kết nối và cống hiến cho cộng đồng địa phương ('学ぶ喜びを他者とのつながりや社会貢献へと広げていく...そんな充実したセカンドライフ').",
    "distractorExplanations": {
      "A": "Không nói về chính sách giảm học phí.",
      "B": "Không nói về thi chứng chỉ để tái tuyển dụng kiếm tiền.",
      "D": "Lớp máy tính chỉ là một ví dụ minh họa."
    }
  },
  {
    "id": "N2_07_M3_L05",
    "typeId": "N2-LIS-GIST",
    "category": "Mondai 3: 概要理解",
    "script": "市議会の本会議中継で、議員が質問を行っています。\n\n女：「子育て世代が安心して暮らせるまちづくりの観点から、夜間および休日の小児初期救急医療体制について提言いたします。現在、本市では夜間の急な発熱などに対応できる小児科医院が当番制となっておりますが、当番医の数が限られており、夜間に隣の市の総合病院まで車を走らせなければならないケースが頻発しております。特に小さなお子様を持つ保護者の心理的不安は極めて深刻です。近隣自治体との広域連携やオンライン診療システムの導入を含め、市として夜間小児救急の受け入れ体制を抜本的に拡充することを強く求めます。」\n\n議員は何を改善するよう求めていますか。\n1番：夜間や休日の子どもの救急医療を受け入れる体制\n2番：市内の小児科医院の診療報酬と薬の価格\n3番：子育て世帯に対するガソリン代の補助金給付\n4番：夜間の道路交通渋滞を解消するための道路整備",
    "stem": "議員は何を改善するよう求めていますか。",
    "options": [
      {
        "id": "A",
        "text": "夜間の道路交通渋滞を解消するための道路整備。"
      },
      {
        "id": "B",
        "text": "市内の小児科医院の診療報酬と薬の価格。"
      },
      {
        "id": "C",
        "text": "子育て世帯に対するガソリン代の補助金給付。"
      },
      {
        "id": "D",
        "text": "夜間や休日の子どもの救急医療を受け入れる体制。"
      }
    ],
    "correctAnswer": "D",
    "explanation": "Nữ nghị sĩ chất vấn và yêu cầu nâng cấp hệ thống y tế cấp cứu ban đêm và ngày nghỉ cho trẻ nhỏ ('夜間および休日の小児初期救急医療体制について提言いたします...受け入れ体制を抜本的に拡充することを強く求めます').",
    "distractorExplanations": {
      "A": "Không phải công trình mở rộng đường sá.",
      "B": "Không nói về giá thuốc hay thù lao bác sĩ.",
      "C": "Việc lái xe sang thành phố bên là dẫn chứng cho sự bất tiện, không phải đòi trợ cấp xăng."
    }
  },
  {
    "id": "N2_07_M4_L01",
    "typeId": "N2-LIS-RESP",
    "category": "Mondai 4: 即時応答",
    "script": "課長、先ほどお願いした新プロジェクトの企画書の決裁、いただけますでしょうか。",
    "stem": "課長、先ほどお願いした新プロジェクトの企画書の決裁、いただけますでしょうか。",
    "options": [
      {
        "id": "A",
        "text": "ああ、先ほど目を通して印鑑を押しておいたから、机の上にあるよ。"
      },
      {
        "id": "B",
        "text": "ええ、来週までに企画書を作成して提出してください。"
      },
      {
        "id": "C",
        "text": "はい、私が企画書を白紙に戻すよう指示したはずです。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Nhân viên hỏi xin phê duyệt bản kế hoạch đã trình trước đó. Trưởng phòng đáp hợp lý: đã xem qua và đóng dấu duyệt rồi, để trên bàn ('目を通して印鑑を押しておいたから、机の上にあるよ').",
    "distractorExplanations": {
      "B": "Lạc đề; nhân viên đang xin duyệt bản đã nộp, không phải bảo đi làm bản mới.",
      "C": "Vô lý và bất lịch sự."
    }
  },
  {
    "id": "N2_07_M4_L02",
    "typeId": "N2-LIS-RESP",
    "category": "Mondai 4: 即時応答",
    "script": "山田さん、明日の市民説明会の配布資料、念のためもう一部多めに刷っておいた方がいいんじゃない？",
    "stem": "山田さん、明日の市民説明会の配布資料、念のためもう一部多めに刷っておいた方がいいんじゃない？",
    "options": [
      {
        "id": "A",
        "text": "ええ、資料はすべて破棄してしまったので間に合いません。"
      },
      {
        "id": "B",
        "text": "そうですね、来場者が予想より増えるかもしれませんから、刷っておきます。"
      },
      {
        "id": "C",
        "text": "いいえ、説明会は昨日無事に終了いたしましたよ。"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Đồng nghiệp khuyên nên in dôi ra vài bộ tài liệu cho an tâm (念のためもう一部多めに...). Câu đáp tán đồng chuẩn mực: 'Đúng vậy anh ạ, phòng khi người đến đông hơn dự kiến nên em sẽ in thêm' ('刷っておきます').",
    "distractorExplanations": {
      "A": "Phi lý; tự nhiên lại vứt hết tài liệu.",
      "C": "Buổi giải trình diễn ra vào ngày mai, không thể nói đã kết thúc hôm qua."
    }
  },
  {
    "id": "N2_07_M4_L03",
    "typeId": "N2-LIS-RESP",
    "category": "Mondai 4: 即時応答",
    "script": "この度の事務処理の不手際につきまして、何とお詫び申し上げればよいか、言葉もございません。",
    "stem": "この度の事務処理の不手際につきまして、何とお詫び申し上げればよいか、言葉もございません。",
    "options": [
      {
        "id": "A",
        "text": "ええ、最初から謝罪の言葉など聞きたくありませんでした。"
      },
      {
        "id": "B",
        "text": "はい、これからはもっと言葉遣いを丁寧に勉強してください。"
      },
      {
        "id": "C",
        "text": "どうぞお気になさらないでください。迅速に修正対応していただいたので問題ありませんよ。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Lời xin lỗi hết sức trang trọng vì sơ suất công việc: 何とお詫び申し上げればよいか、言葉もございません. Đáp lại một cách hòa nhã và chuyên nghiệp: 'Xin anh/chị đừng bận tâm, bên anh/chị đã sửa sai rất nhanh chóng nên không sao đâu ạ'.",
    "distractorExplanations": {
      "A": "Quá thô lỗ và phi lý trong giao tiếp công sở.",
      "B": "Hiểu nhầm 'không còn lời nào để tạ lỗi' thành 'học lại cách dùng từ'."
    }
  },
  {
    "id": "N2_07_M4_L04",
    "typeId": "N2-LIS-RESP",
    "category": "Mondai 4: 即時応答",
    "script": "鈴木さん、午後からの他部署とのオンライン協議、回線の接続テストはどう？",
    "stem": "鈴木さん、午後からの他部署とのオンライン協議、回線の接続テストはどう？",
    "options": [
      {
        "id": "A",
        "text": "先ほどテストを済ませましたが、音声も映像も非常にクリアでしたよ。"
      },
      {
        "id": "B",
        "text": "ええ、インターネット回線は来月解約する予定です。"
      },
      {
        "id": "C",
        "text": "はい、午後からの協議は先週のうちに終わりました。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Hỏi thăm kết quả chạy thử đường truyền họp online buổi chiều. Câu trả lời chính xác: vừa thử xong, cả hình lẫn tiếng đều rất rõ nét ('音声も映像も非常にクリアでしたよ').",
    "distractorExplanations": {
      "B": "Tự nhiên nói tháng sau cắt mạng.",
      "C": "Cuộc họp diễn ra chiều nay, không thể nói đã xong từ tuần trước."
    }
  },
  {
    "id": "N2_07_M4_L05",
    "typeId": "N2-LIS-RESP",
    "category": "Mondai 4: 即時応答",
    "script": "あれほど準備したのに、台風の接近で地域のお祭りが中止になるなんて、やりきれないね。",
    "stem": "あれほど準備したのに、台風の接近で地域のお祭りが中止になるなんて、やりきれないね。",
    "options": [
      {
        "id": "A",
        "text": "ええ、台風が直撃してくれて本当に助かりましたね。"
      },
      {
        "id": "B",
        "text": "本当にね。みんなで何週間も前から準備してきたのに、悔しいよね。"
      },
      {
        "id": "C",
        "text": "うん、来週のお祭りの開催が待ち遠しいね。"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Mẫu biểu đạt tâm trạng N2: 〜やりきれない (thật buồn bực/không cam lòng). Đồng cảm với sự tiếc nuối: 'Thực sự vậy anh ạ, mọi người chuẩn bị từ mấy tuần trước mà đành chịu, ấm ức thật' ('悔しいよね').",
    "distractorExplanations": {
      "A": "Nói bão vào giúp ích là vô lý.",
      "C": "Lễ hội đã bị hủy bỏ do bão, không thể bảo đang ngóng chờ tuần sau."
    }
  },
  {
    "id": "N2_07_M4_L06",
    "typeId": "N2-LIS-RESP",
    "category": "Mondai 4: 即時応答",
    "script": "お忙しいところ大変恐縮ですが、こちらの申請書類に目を通していただけないでしょうか。",
    "stem": "お忙しいところ大変恐縮ですが、こちらの申請書類に目を通していただけないでしょうか。",
    "options": [
      {
        "id": "A",
        "text": "いいえ、私は忙しいので誰も見てくれませんよ。"
      },
      {
        "id": "B",
        "text": "はい、書類は明日までにすべて処分しておいてください。"
      },
      {
        "id": "C",
        "text": "ええ、ちょうど今手が空いたところですので、拝見しますね。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Nhờ cấp trên hoặc tiền bối xem qua hồ sơ: 目を通していただけないでしょうか. Câu đáp nhận lời lịch sự khiêm nhường: 'Vâng, vừa khéo tôi cũng vừa xong việc, để tôi xem cho nhé' ('拝見しますね').",
    "distractorExplanations": {
      "A": "Cách nói ngô nghê và sai ngữ dụng.",
      "B": "Kêu vứt tài liệu đi là sai hoàn cảnh."
    }
  },
  {
    "id": "N2_07_M4_L07",
    "typeId": "N2-LIS-RESP",
    "category": "Mondai 4: 即時応答",
    "script": "佐藤さん、さっきの定例会議での発言、ちょっと先方に言い過ぎたんじゃない？",
    "stem": "佐藤さん、さっきの定例会議での発言、ちょっと先方に言い過ぎたんじゃない？",
    "options": [
      {
        "id": "A",
        "text": "申し訳ありません。議論が熱くなって、相手への配慮が足りませんでした。"
      },
      {
        "id": "B",
        "text": "はい、もっと厳しい言葉で相手を責め立てるべきでしたね。"
      },
      {
        "id": "C",
        "text": "ええ、会議は明日から始まる予定なので気をつけます。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Lời nhắc nhở nhẹ nhàng của đồng nghiệp: 'Cậu nói với đối tác lúc nãy hơi quá lời chăng?'. Câu đáp nhận lỗi biết điều: 'Em xin lỗi, lúc đó tranh luận gay gắt quá nên em thiếu chu đáo với đối tác ạ'.",
    "distractorExplanations": {
      "B": "Tiếp tục hung hăng chỉ trích đối tác là sai tác phong làm việc.",
      "C": "Cuộc họp vừa diễn ra rồi chứ không phải ngày mai."
    }
  },
  {
    "id": "N2_07_M4_L08",
    "typeId": "N2-LIS-RESP",
    "category": "Mondai 4: 即時応答",
    "script": "今回の広報誌リニューアルの担当リーダー、引き受けてくださる気はありませんか。",
    "stem": "今回の広報誌リニューアルの担当リーダー、引き受けてくださる気はありませんか。",
    "options": [
      {
        "id": "A",
        "text": "はい、リーダーの席はすでに他の課長に決まりましたよ。"
      },
      {
        "id": "B",
        "text": "私のような若手でよろしければ、ぜひ喜んで挑戦させてください。"
      },
      {
        "id": "C",
        "text": "いいえ、広報誌は今年度で廃刊になることが決まりました。"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Lời mời nhận nhiệm vụ quan trọng: 〜気はありませんか. Câu đáp khiêm tốn chuẩn mực của người Nhật: 'Nếu một người trẻ như em mà được tin tưởng thì xin cho em cơ hội được thử sức ạ' ('ぜひ喜んで挑戦させてください').",
    "distractorExplanations": {
      "A": "Người hỏi đang mở lời mời mình, không thể nói ghế đã chia cho người khác.",
      "C": "Nói tạp chí bị đình bản là mâu thuẫn với việc đang cải tiến."
    }
  },
  {
    "id": "N2_07_M4_L09",
    "typeId": "N2-LIS-RESP",
    "category": "Mondai 4: 即時応答",
    "script": "市民窓口の待ち時間、新しいオンライン予約システムのおかげで大幅に短縮されたそうですね。",
    "stem": "市民窓口の待ち時間、新しいオンライン予約システムのおかげで大幅に短縮されたそうですね。",
    "options": [
      {
        "id": "A",
        "text": "いいえ、新システムは来年まで一度も稼働しない予定です。"
      },
      {
        "id": "B",
        "text": "はい、待ち時間が2倍に延びて苦情が殺到しています。"
      },
      {
        "id": "C",
        "text": "ええ、来庁者の皆様からも混雑が緩和されたと大変好評をいただいております。"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Người đối thoại khen ngợi: nghe nói thời gian chờ tại quầy giảm mạnh nhờ hệ thống hẹn trực tuyến mới. Câu đáp xác nhận niềm vui phục vụ: 'Vâng, người dân đến làm thủ tục cũng phản hồi rất tích cực vì quầy thông thoáng hẳn ạ'.",
    "distractorExplanations": {
      "A": "Hệ thống đang chạy rồi nên mới có kết quả thực tế.",
      "B": "Mâu thuẫn với vế đầu 'thời gian chờ giảm mạnh'."
    }
  },
  {
    "id": "N2_07_M4_L10",
    "typeId": "N2-LIS-RESP",
    "category": "Mondai 4: 即時応答",
    "script": "部長、取引先から契約単価の引き下げ要求が届きましたが、これを承諾するわけにはいきませんよね。",
    "stem": "部長、取引先から契約単価の引き下げ要求が届きましたが、これを承諾するわけにはいきませんよね。",
    "options": [
      {
        "id": "A",
        "text": "ああ、弊社の採算ラインを割り込むことになるから、安易な妥協はできないね。"
      },
      {
        "id": "B",
        "text": "うん、すぐに先方の要求通りに全額値引きの契約書を作成して。"
      },
      {
        "id": "C",
        "text": "ええ、先月すでに取引を完全に停止したはずだよ。"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Ngữ pháp N2: 〜わけにはいきませんよね (không thể nào chấp nhận được đúng không ạ). Trưởng phòng đồng tình bảo vệ quyền lợi công ty: 'Ừ, làm vậy sẽ dưới mức hòa vốn nên chúng ta tuyệt đối không thể nhượng bộ dễ dàng' ('安易な妥協はできないね').",
    "distractorExplanations": {
      "B": "Trái ngược hoàn toàn ý đồ của câu hỏi.",
      "C": "Đang nhận yêu cầu xem xét đơn giá thì hợp đồng vẫn đang trao đổi."
    }
  },
  {
    "id": "N2_07_M4_L11",
    "typeId": "N2-LIS-RESP",
    "category": "Mondai 4: 即時応答",
    "script": "新入社員のOJT指導員、色々と準備が大変そうだけど、指導経験豊富な田中さんならお手の物でしょう？",
    "stem": "新入社員のOJT指導員、色々と準備が大変そうだけど、指導経験豊富な田中さんならお手の物でしょう？",
    "options": [
      {
        "id": "A",
        "text": "ええ、指導員なんて誰でも目をつぶって簡単にこなせますよ。"
      },
      {
        "id": "B",
        "text": "とんでもない、新入社員の個性に合わせて教えるのは毎回手探りで緊張しますよ。"
      },
      {
        "id": "C",
        "text": "はい、今年の新入社員は全員研修を辞退して帰宅しました。"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Thành ngữ N2: 〜お手の物（おてのもの - sở trường, làm cái là được ngay). Bạn khen ngợi anh Tanaka dạy người mới chắc dễ như trở bàn tay. Đáp lại khiêm tốn: 'Đâu có đâu bạn, mỗi lứa tân binh một tính cách nên lần nào mình cũng phải vừa làm vừa mày mò căng thẳng lắm' ('とんでもない...手探りで緊張しますよ').",
    "distractorExplanations": {
      "A": "Khoe khoang quá đà, bất lịch sự.",
      "C": "Vô lý; tân binh không bỏ về hết."
    }
  },
  {
    "id": "N2_07_M5_L01",
    "typeId": "N2-LIS-INTEG",
    "category": "Mondai 5: 統合理解",
    "script": "市民会館の事務室で、地域団体の代表の男性と女性職員が、会館改修工事期間中の代替施設について話しています。\n\n男：「市民会館が来月から半年間改修工事に入ると聞いて、私どもの団体が定期的に利用している催しの会場を探しているんです。」\n女：「ご不便をおかけして申し訳ありません。どのような用途でご利用になられますか。」\n男：「実は2つの活動がありましてね。1つ目は、地域のアマチュア演劇サークルの『定期公演会』です。音響設備と照明装置が本格的で、客席が200席ほどある舞台ホールが必要です。2つ目は、高齢者向けの『健康ストレッチ体操教室』です。こちらは週に1回、床が板張りで手すりがあり、参加者のためにエレベーターや広い駐車場が完備されている部屋を希望しています。」\n女：「承知いたしました。現在、市内でご利用いただける代替施設は4つございます。\n　まず、1番の『東部文化センター』は、250席のホールがあり、音響や照明は市民会館と同等の充実度です。ただし、エレベーターがなく階段のみの設計となっております。\n　次に、2番の『総合福祉プラザ』は、全館バリアフリーでエレベーターと大型駐車場を備えており、多目的室の床は衝撃吸収のフローリングで手すりも付いています。ただ、舞台装置や音響設備は簡易的なものしかございません。\n　3番の『青少年スポーツセンター』は、広い体育館とトレーニング室がありますが、板張りではなく樹脂マット床で、土足禁止となっております。\n　4番の『中央公民館』は、100席の小ホールと和室がありますが、駐車スペースが5台分しかなく、本格的な舞台照明設備はございません。」\n男：「なるほど。それぞれの条件がよく分かりました。では、演劇サークルの公演会と、高齢者の体操教室の会場をそれぞれ決めたいと思います。」",
    "stem": "質問1：アマチュア演劇サークルの公演会場として、男性はどの施設を選びますか。",
    "options": [
      {
        "id": "A",
        "text": "1番の東部文化センター"
      },
      {
        "id": "B",
        "text": "2番の総合福祉プラザ"
      },
      {
        "id": "C",
        "text": "3番の青少年スポーツセンター"
      },
      {
        "id": "D",
        "text": "4番の中央公民館"
      }
    ],
    "correctAnswer": "A",
    "explanation": "Buổi biểu diễn kịch cần khán phòng khoảng 200 chỗ ngồi có hệ thống âm thanh, ánh sáng sân khấu chuyên nghiệp. Trung tâm văn hóa Đông bộ (1番) có 250 chỗ, âm thanh ánh sáng đầy đủ tương đương hội trường thành phố.",
    "distractorExplanations": {
      "B": "Trung tâm phúc lợi tổng hợp chỉ có âm thanh ánh sáng đơn giản.",
      "C": "Trung tâm thể thao thanh thiếu niên là sàn đệm nhựa thể thao, không có sân khấu kịch.",
      "D": "Nhà văn hóa trung tâm chỉ có 100 chỗ và không có đèn sân khấu chuyên dụng."
    }
  },
  {
    "id": "N2_07_M5_L02",
    "typeId": "N2-LIS-INTEG",
    "category": "Mondai 5: 統合理解",
    "script": "市民会館の事務室で、地域団体の代表の男性と女性職員が、会館改修工事期間中の代替施設について話しています。\n\n男：「市民会館が来月から半年間改修工事に入ると聞いて、私どもの団体が定期的に利用している催しの会場を探しているんです。」\n女：「ご不便をおかけして申し訳ありません。どのような用途でご利用になられますか。」\n男：「実は2つの活動がありましてね。1つ目は、地域のアマチュア演劇サークルの『定期公演会』です。音響設備と照明装置が本格的で、客席が200席ほどある舞台ホールが必要です。2つ目は、高齢者向けの『健康ストレッチ体操教室』です。こちらは週に1回、床が板張りで手すりがあり、参加者のためにエレベーターや広い駐車場が完備されている部屋を希望しています。」\n女：「承知いたしました。現在、市内でご利用いただける代替施設は4つございます。\n　まず、1番の『東部文化センター』は、250席のホールがあり、音響や照明は市民会館と同等の充実度です。ただし、エレベーターがなく階段のみの設計となっております。\n　次に、2番の『総合福祉プラザ』は、全館バリアフリーでエレベーターと大型駐車場を備えており、多目的室の床は衝撃吸収のフローリングで手すりも付いています。ただ、舞台装置や音響設備は簡易的なものしかございません。\n　3番の『青少年スポーツセンター』は、広い体育館とトレーニング室がありますが、板張りではなく樹脂マット床で、土足禁止となっております。\n　4番の『中央公民館』は、100席の小ホールと和室がありますが、駐車スペースが5台分しかなく、本格的な舞台照明設備はございません。」\n男：「なるほど。それぞれの条件がよく分かりました。では、演劇サークルの公演会と、高齢者の体操教室の会場をそれぞれ決めたいと思います。」",
    "stem": "質問2：高齢者の健康ストレッチ体操教室の会場として、男性はどの施設を選びますか。",
    "options": [
      {
        "id": "A",
        "text": "1番の東部文化センター"
      },
      {
        "id": "B",
        "text": "2番の総合福祉プラザ"
      },
      {
        "id": "C",
        "text": "3番の青少年スポーツセンター"
      },
      {
        "id": "D",
        "text": "4番の中央公民館"
      }
    ],
    "correctAnswer": "B",
    "explanation": "Lớp tập thể dục cho người cao tuổi cần sàn gỗ có tay vịn, có thang máy và bãi đỗ xe rộng rãi. Plaza Phúc lợi tổng hợp (2番) đáp ứng toàn diện: không rào cản, có thang máy, bãi đỗ xe lớn, sàn gỗ giảm chấn và có tay vịn.",
    "distractorExplanations": {
      "A": "Trung tâm văn hóa Đông bộ không có thang máy, chỉ có cầu thang bộ nên người già đi lại nguy hiểm.",
      "C": "Trung tâm thể thao không có sàn gỗ lát mà dùng đệm nhựa.",
      "D": "Nhà văn hóa trung tâm chỉ có 5 chỗ đỗ xe."
    }
  },
  {
    "id": "N2_07_M5_L03",
    "typeId": "N2-LIS-INTEG",
    "category": "Mondai 5: 統合理解",
    "script": "会社で、女性社員と男性社員が新しく導入される福利厚生の選択型支援メニュー（カフェテリアプラン）について話しています。\n\n女：「来期から導入される福利厚生メニューの案内が配られたわね。各自のポイントを使って4つのプランから1つ選べるそうよ。」\n男：「へえ、どんなメニューがあるの？」\n女：「1番の『スキルアップ支援プラン』は、語学学校や資格取得講座の受講料を年最大5万円補助してくれるの。\n　2番の『ヘルスケア促進プラン』は、フィットネスクラブの月会費補助や人間ドックのオプション検査が無料になるわ。\n　3番の『ファミリーサポートプラン』は、育児施設や介護サービスの利用料割引と、家事代行サービスの補助券が出るの。\n　4番の『トラベル・リフレッシュプラン』は、提携リゾートホテルやテーマパークの宿泊費が半額になるチケットがもらえるわ。」\n男：「なるほど。僕は今年、健康診断で運動不足を指摘されたから、ジム通いを習慣にしたいと思っていたんだよね。」\n女：「それならピッタリのプランがあるじゃない！ 私は来年、海外事業部への異動を目指しているから、ビジネス英語のオンラインレッスンを受けたいと思っていたの。」\n男：「お互い自分に一番必要なプランが決まったみたいだね。」\n\n質問：男性社員と女性社員は、それぞれどのプランを選びますか。",
    "stem": "質問：男性社員と女性社員は、それぞれどのプランを選びますか。",
    "options": [
      {
        "id": "A",
        "text": "男性は4番（トラベル）、女性は3番（ファミリー）"
      },
      {
        "id": "B",
        "text": "男性は1番（スキルアップ）、女性は4番（トラベル）"
      },
      {
        "id": "C",
        "text": "男性は2番（ヘルスケア）、女性は1番（スキルアップ）"
      },
      {
        "id": "D",
        "text": "男性は2番（ヘルスケア）、女性は3番（ファミリー）"
      }
    ],
    "correctAnswer": "C",
    "explanation": "Nam nhân viên muốn đi tập gym khắc phục thiếu vận động -> chọn gói số 2 (Chăm sóc sức khỏe - ヘルスケア). Nữ nhân viên muốn học thêm tiếng Anh thương mại để chuyển sang bộ phận hải ngoại -> chọn gói số 1 (Nâng cao kỹ năng - スキルアップ).",
    "distractorExplanations": {
      "A": "Sai cả nam và nữ.",
      "B": "Sai cả nam và nữ.",
      "D": "Nữ nhân viên không chọn gói hỗ trợ gia đình số 3."
    }
  }
]

if __name__ == '__main__':
    items = get_n2_mock_07_listening_items()
    print(f"Loaded {len(items)} Section 2 Listening items.")
