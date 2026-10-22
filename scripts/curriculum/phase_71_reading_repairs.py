# -*- coding: utf-8 -*-
"""Versioned editorial repairs for the M11-M13 reading candidate.

The published mocks remain untouched until the materially changed items receive
fresh current-version review. These overrides are applied only when rebuilding
authoring candidates from the tracked source banks.
"""
from __future__ import annotations

from scripts.curriculum.phase_71_reading_rationales import (
    DISTRACTOR_RATIONALES,
    validate_distractor_rationales,
)


PATCHES = {
    # M11 short reading: add a real workplace context and plausible competing
    # explanations while preserving the question's assessed purpose.
    "N2_11_M10_01": {
        "passage": "部署では複数の担当者が同じ共有フォルダーを使い、修正のたびに別名で保存していた。そのため似たファイルが並び、開いて内容を確かめるまで最新版が分からないことがあった。担当者は、作成日と版番号をファイル名に入れるルールを設け、ファイルを開く前に新旧を区別できるようにした。",
        "stem": "作成日と版番号を付けることで、担当者ができるようにしたことは何か。",
        "correctText": "ファイルを開かなくても、新旧を見分けること",
        "distractors": ["修正した人の評価を記録すること", "古いファイルを自動的に削除すること", "保存先を担当者ごとに分けること"],
        "distractorRationales": ["作成者の評価や責任記録については述べていません。", "旧版の削除ではなく、日付と版番号で区別する方法です。", "共有フォルダーは引き続き部署で使い、保存先を分けるとは書かれていません。"],
        "explanationVi": "Nhiều người lưu các bản sửa có tên gần giống nhau nên khó nhận ra bản mới nhất. Ngày tạo và số phiên bản giúp phân biệt mới–cũ ngay trên tên tệp, trước khi mở tệp.",
    },
    "N2_11_M10_02": {
        "passage": "取引先から届いた見積書に、説明のない金額が一つあった。以前の案件と似た数字ではあったが、納品条件が変われば金額も変わる。担当者は過去の数字を空欄に当てはめず、該当箇所を示して先方へ問い合わせた。確認が取れるまでは、その金額を社内の原価計算にも使わないようチームに伝えた。",
        "stem": "担当者が金額を入力する前に先方へ確認したのはなぜか。",
        "correctText": "条件が同じとは限らず、過去の金額を当てはめられないから",
        "distractors": ["見積書の総額も変更されたと分かったから", "契約を断る判断をすでに済ませていたから", "記載された項目をすべて削除するため"],
        "distractorRationales": ["本文で確認が必要なのは説明のない一項目で、総額変更とは述べていません。", "担当者は金額の根拠を確認しており、取引を断る判断はしていません。", "削除ではなく、該当箇所を示して先方へ質問しています。"],
        "explanationVi": "Con số cũ trông giống một vụ trước nhưng điều kiện giao hàng có thể khác. Vì vậy người phụ trách không tự điền số liệu chưa có căn cứ và hỏi đối tác trước khi dùng nó.",
    },
    "N2_11_M10_03": {
        "passage": "社内研修の録画を、後日、社外の参加者にも共有することになった。映像には講師の説明だけでなく、画面共有に映った社員名や通知も残っている。講師は、個人が特定される場面を切るかぼかし、内容を確認してから共有するよう依頼した。研修の説明自体は残し、公開前に個人情報だけを点検する手順にした。",
        "stem": "講師が名前の映る場面を共有前に処理するよう求めた主な理由は何か。",
        "correctText": "個人が特定される情報を社外に公開しないため",
        "distractors": ["社外向けの映像を一定の長さに整えるため", "研修の説明を外部向けに全面的に書き換えるため", "社員名の読み方を字幕で補足し、視聴者に正確に伝えるため"],
        "distractorRationales": ["編集する場面は社員名や通知が映る箇所です。動画の長さを一定にする作業は本文の目的ではありません。", "講師は研修の説明自体を残すよう依頼しています。内容を全面的に書き換える話ではありません。", "名前は字幕で補うのではなく、切るかぼかして個人を特定できないようにします。"],
        "explanationVi": "Video sẽ được chia sẻ ra ngoài công ty. Tên nhân viên và thông báo hiện trên màn hình có thể nhận diện cá nhân, nên cần che hoặc cắt chúng trước khi phát hành; nội dung đào tạo vẫn được giữ lại.",
    },
    "N2_11_M10_04": {
        "passage": "会議の参加希望が増え、総務担当者は全員が入れる別の部屋に変更した。最初の案内はすでに送ってあり、何人かは旧会場の情報を保存していた。そこで総務は、時間と議題は変えず、会場だけを訂正した案内を再送した。古い情報のまま来て会議に遅れる人を防ぐためである。",
        "stem": "担当者が訂正版を再送した狙いは何か。",
        "correctText": "旧会場へ行ってしまう参加者を防ぐこと",
        "distractors": ["参加希望者が増えたことを知らせ、追加の申込みを受けること", "会場変更に合わせ、開始時刻と議題も更新して伝えること", "新しい会場の定員に合わせ、参加者数を再調整すること"],
        "distractorRationales": ["参加希望者を募り直すとは書かれていません。再送の直接の理由は、旧会場の情報を持つ人が間違った場所へ行くのを防ぐことです。", "本文では時間と議題は変更しないと明記されています。訂正するのは会場情報だけです。", "総務は希望者全員が入れる部屋へ変更しています。参加者を減らす手続きや再調整には触れていません。"],
        "explanationVi": "Thông báo đầu tiên còn ghi phòng cũ và một số người đã lưu lại. Gửi bản sửa giúp họ không đến nhầm địa điểm và bị trễ cuộc họp; giờ họp và nội dung vẫn giữ nguyên.",
    },
    "N2_11_M10_05": {
        "passage": "毎週の報告では予定作業の時間だけでなく、急な問い合わせや手直しに使った時間も記録することにした。予定外の作業は月によって差があり、計画時の見積もりから漏れやすい。担当者はこの記録を翌月の業務量や人員の予測に使うが、個人の処理速度を評価する目的には使わない。",
        "stem": "予定外の対応時間を記録する主な目的は何か。",
        "correctText": "次月の業務量や必要な人員を現実に近く見積もるため",
        "distractors": ["予定外の対応にかかった時間を、担当者ごとの人事評価に反映するため", "翌月にも起きる急な仕事をなくす手順を決めるため", "計画した作業と突発的な対応を、別々の報告欄で管理するため"],
        "distractorRationales": ["時間の記録は個人の処理速度を評価する目的には使わないと本文で区別しています。", "記録の目的は次月の業務量や人員の見積もりです。突発的な仕事をなくす方法を決めるとは書かれていません。", "本文は両方の時間を記録すると述べていますが、欄を分けることは目的として示していません。"],
        "explanationVi": "Việc phát sinh thay đổi theo từng tháng và dễ bị bỏ sót khi lập kế hoạch. Ghi cả thời gian đó giúp dự báo khối lượng công việc và nhân lực tháng sau sát thực tế hơn; không dùng để xếp hạng tốc độ cá nhân.",
    },
    # M11 long reading: build the reasoning chain and ask for synthesis rather
    # than a single repeated phrase.
    "N2_11_M13_01": {
        "passage": "【業務改善の進め方】\n業務を改善するとき、時間のかかる作業をすべて機械に置き換えればよい、と考えられることがある。しかし作業時間だけを基準にすると、例外への対応、利用者への説明、入力後の確認など、数字に表れにくい仕事が抜け落ちる。短縮した時間が大きくても、別の確認作業が増えれば、仕事全体が効率化したとは言えない。\n\nある企業では、まず一週間、作業の種類と発生条件、誰がどの判断をしているかを記録した。その後、繰り返しが多く判断基準の明確な作業から自動化を試した。例外が起きた場合に誰が確認するかを決め、利用者にも変更点と問い合わせ先を説明した。\n\n試験運用では入力作業が減った一方、特定の条件では確認に時間がかかることが分かった。企業は自動化の対象をすぐに広げず、その条件を調べ、記録にない仕事がないか現場にも聞いた。改善は導入した技術の数や一部の作業時間だけでなく、安全性、利用者への影響、仕事全体の分かりやすさを合わせて判断する方針である。",
        "stem": "この企業が自動化の対象を段階的に広げようとしているのはなぜか。",
        "correctText": "一部の時間短縮だけでなく、例外時の確認や利用者への影響も確かめるため",
        "distractors": ["定型作業では入力時間がまったく減らなかったため", "例外が起きた場合は利用者に説明しないため", "作業を記録すると自動化ができなくなるため"],
        "distractorRationales": ["試験運用では入力作業が減ったと述べています。", "本文では変更点と問い合わせ先を利用者に説明しています。", "記録は自動化の対象と条件を選ぶために活用されています。"],
        "explanationVi": "Do thời gian nhập liệu giảm nhưng có điều kiện khiến khâu xác nhận lâu hơn, công ty kiểm tra ngoại lệ và tác động đến người dùng trước khi mở rộng tự động hóa. Tác giả đánh giá toàn bộ quy trình, không chỉ một thao tác.",
    },
    "N2_11_M13_02": {
        "passage": "【意見を集める意味】\n新しい制度を作る際、アンケートは広く意見を集めるのに便利である。ただし回答数が多くても、結果がそのまま全利用者の考えを表すとは限らない。制度に関心が強い人や利用経験の多い人ほど回答し、忙しい人や制度を知らない人は回答しない可能性があるからだ。\n\n市の担当者は、回答を年齢や利用頻度ごとに分け、どの層から返事が少ないかを確かめた。さらに、回答しなかった人にも短い聞き取りを行い、自由記述に出た具体例を「手続き」「費用」「利用時間」などに分類した。数字だけでは、何に困っているのか、どの条件で問題が起きるのか分かりにくい場合がある。\n\nこうした確認には時間がかかるが、アンケートの数字を捨てる必要はない。数字で全体の傾向をつかみ、別の方法で回答の偏りや理由を確かめれば、制度のどこを直すべきかをより適切に判断できる。市は調査の限界も公表し、得られた意見を全利用者の総意だと扱わないことにした。",
        "stem": "アンケートと聞き取りを組み合わせる主な理由は何か。",
        "correctText": "回答者の偏りや数字だけでは分からない困りごとの背景を確かめるため",
        "distractors": ["回答数を増やして全利用者の意見を完全に再現するため", "結果を数値だけにそろえ、具体例を使わないため", "回答しなかった人の意見を制度から除くため"],
        "distractorRationales": ["本文は回答数だけで全利用者を代表できるとは限らないと述べています。", "自由記述や聞き取りの具体例も分類して使います。", "非回答者にも短い聞き取りを行うとあります。"],
        "explanationVi": "Người trả lời khảo sát có thể khác người không trả lời về mức độ quan tâm và kinh nghiệm. Kết hợp số liệu với phỏng vấn ngắn giúp nhận ra thiên lệch và lý do đằng sau các vấn đề, thay vì coi mẫu trả lời là ý kiến của tất cả mọi người.",
    },
    "N2_11_M13_03": {
        "passage": "【専門知識を伝える】\n専門家の知識を社会に伝えるには、正確さを保ちながら、受け手が理解できる形にする工夫がいる。用語をすべて簡単な言葉に置き換えると、専門上の区別まで失われることがある。一方、説明を省き専門用語だけを並べれば、初めて読む人は何が重要かつかみにくい。\n\n博物館の解説チームは、展示の中心となる考えを先に決め、専門用語を残す場合は短い説明や具体例をすぐ近くに置いた。公開前には専門外の職員にも読んでもらい、意味が取れなかった箇所を記録した。来館者がどこで立ち止まり、どの説明を読み直すかも観察し、文章の順番や図の位置を調整した。\n\n伝え方を変えることは、内容を薄めることではない。何を理解してほしいかを明確にし、必要な情報へ段階的に導くことである。受け手の反応を確かめながら説明を直す作業は、公開後も続ける必要がある。",
        "stem": "博物館の説明を改善する際の考えとして、本文に合うものはどれか。",
        "correctText": "中心となる考えを定め、専門語には説明を添えて読み手の反応で順序を直す",
        "distractors": ["専門用語をすべて削除し、図だけで説明する", "専門外の人には見せず、公開後の反応も調べない", "解説を短くするため、研究の正確さより読みやすさを優先する"],
        "distractorRationales": ["用語をすべて置き換えると、重要な区別まで失われる場合があると述べています。", "専門外の職員や来館者の反応を確認し、公開後も改善します。", "正確さと理解しやすさを両立させることが方針です。"],
        "explanationVi": "Nhóm xác định ý cốt lõi, giải thích thuật ngữ cần giữ lại, rồi quan sát chỗ người đọc vướng để điều chỉnh thứ tự và hình minh họa. Bài viết không đề nghị xóa hết thuật ngữ hay hy sinh độ chính xác để rút ngắn.",
    },
    # M12 short reading: retain compact notices but supply enough operational
    # context to support condition-sensitive reading.
    "N2_12_M10_01": {
        "passage": "市役所では、平日の受付時間に来られない勤務者から相談が寄せられたため、来月から毎週水曜日だけ午後七時まで窓口を延長する。予約は不要で、相談や証明書の申請に利用できる。ただし、戸籍関係など一部の証明書は別の窓口で扱うため、来庁後に案内を確認してほしい。",
        "explanationVi": "Thứ Tư được kéo dài giờ tiếp nhận để người không thể đến trong giờ thường có thêm lựa chọn. Không cần đặt trước, nhưng một số giấy tờ vẫn phải làm tại quầy khác.",
    },
    "N2_12_M10_02": {
        "passage": "町内の公園では今週末、遊歩道沿いの樹木を剪定する。作業中は東側の通路を閉鎖するが、西側入口から入って芝生広場を利用することはできる。雨天時は安全のため翌週に延期し、実施日が変わった場合は市のウェブサイトと公園入口の掲示で知らせる。",
        "explanationVi": "Trong lúc cắt tỉa, lối phía Đông đóng nhưng công viên vẫn vào được từ cổng phía Tây. Nếu mưa, việc bị hoãn sang tuần sau; ngày mới được thông báo trên trang web và bảng ở cổng.",
    },
    "N2_12_M10_03": {
        "passage": "地域の団体は、まだ食べられる食品を集め、必要な世帯へ届けるため回収を行う。回収箱は図書館の正面ではなく、隣の交流センターに置く。未開封で期限まで一週間以上ある食品のみ、平日の午前九時から午後五時に受け付ける。",
        "explanationVi": "Hộp quyên góp nằm ở trung tâm giao lưu cạnh thư viện. Chỉ nhận thực phẩm chưa mở, còn hạn ít nhất một tuần và được mang đến vào ngày thường từ 9 giờ đến 17 giờ.",
    },
    "N2_12_M10_04": {
        "passage": "市民プールは設備点検のため二十日から二十二日まで休館する。期間中に予定していた水泳教室は二十五日に振り替える。通常の入館券は使えなかった日数分だけ有効期限を延長するため、利用者が窓口で手続きをする必要はない。点検後の営業は二十三日から再開する。",
        "explanationVi": "Hồ bơi đóng cửa từ ngày 20 đến 22, mở lại ngày 23; lớp học được chuyển sang ngày 25. Hạn vé vào cửa kéo dài theo số ngày không sử dụng và người mua không cần làm thủ tục.",
    },
    "N2_12_M10_05": {
        "passage": "移動図書館は、道路工事に合わせ、来月から山側の三地区を回る順番を変える。道路事情を避けるため図書館の出発時刻は十五分早めるが、各地区での到着時刻と滞在時間は調整して現在の予定を保つ。新しい巡回順は停車場所の掲示と市の案内で確認できる。",
        "explanationVi": "Thứ tự đi qua ba khu vực thay đổi, còn giờ đến và thời gian dừng được điều chỉnh để giữ như hiện tại. Chỉ giờ xe rời thư viện sớm hơn 15 phút; thứ tự mới có trên thông báo.",
    },
    # M13 medium reading: expand each compact text with relevant cause,
    # limitation, or counter-consideration; preserve the existing keyed task.
    "N2_13_M11_01": {
        "passage": "大学の授業で、学生が作った解説動画を教材として使う試みが始まった。動画は教員の説明を置き換えるものではなく、初めて学ぶ人が疑問を整理し、授業で質問しやすくするために用いる。公開前には別の学生が出典や説明の順序も確かめ、誤りがあれば制作者と相談して直す。再生回数を競わせると、目立つ演出や短さが優先され、内容の正確さが後回しになる恐れがある。そのため、評価では、初学者が要点を追えるか、根拠を示して説明しているかを中心に見ることにした。",
        "explanationVi": "Video chỉ hỗ trợ người mới sắp xếp thắc mắc chứ không thay bài giảng. Vì lượt xem có thể khuyến khích trình diễn hơn nội dung, nhóm đánh giá độ chính xác và mạch giải thích, đồng thời kiểm tra nguồn trước khi đăng.",
    },
    "N2_13_M11_02": {
        "passage": "ある大学は、授業録画を希望者だけに公開していたが、学生から「どこに何があるか分かりにくい」と意見が出た。そこで、動画に章見出しを付け、授業資料から該当箇所へ移動できるリンクを設けた。一方、映像の公開期間を延ばす要望には応じず、試験問題が外部に広がる可能性を避けるため、学期末から二週間後に視聴できなくする方針を維持した。大学は、探しやすさの改善と閲覧範囲の管理は別々に考える必要があるとして、録画を教材として残す期間を長くする案は採用しなかった。",
        "explanationVi": "Trường cải thiện khả năng tìm nội dung bằng tiêu đề chương và liên kết, nhưng không kéo dài thời gian xem vì nguy cơ đề thi bị phát tán. Họ giải quyết tiện ích tìm kiếm mà vẫn giữ giới hạn truy cập.",
    },
    "N2_13_M11_03": {
        "passage": "学生新聞の編集部は、SNSで話題になった情報を記事にする際、投稿画面を保存するだけでは不十分だと考えている。投稿者に確認を取り、日時や場所を別の資料と照らすほか、画像が過去の出来事から再利用されていないかも調べる。確認できた情報でも、別の資料と食い違う場合はその違いを記録し、すぐに一つの説明へまとめない。記事では、確定した事実と未確認の情報を分け、確認が取れなかった点も残す。読者が情報の確かさを自分で判断できるようにするためである。",
        "explanationVi": "Chỉ lưu ảnh chụp màn hình chưa đủ để xác minh tin. Ban biên tập đối chiếu thời gian, địa điểm và nguồn ảnh; bài báo tách điều đã xác nhận khỏi phần chưa chắc để người đọc đánh giá độ tin cậy.",
    },
    "N2_13_M11_04": {
        "passage": "講義で自動字幕を使う学生が増えたため、教員は誤認識の例を授業資料に加えた。専門用語や固有名詞は正しく表示されない場合があり、字幕だけを見て覚えると、意味を誤って理解することがあるからだ。学生には重要な箇所を録音や配布資料でも確かめるよう伝え、誤りを報告する仕組みも設けた。ただし、一語ずつ確認する作業には人手が必要で、授業ごとの優先順位もある。報告が届いても、すべてを即日直すとは約束していない。",
        "explanationVi": "Phụ đề tự động hỗ trợ học nhưng có thể nhận sai thuật ngữ và tên riêng, nên điểm quan trọng cần kiểm tra bằng âm thanh hoặc tài liệu. Báo lỗi giúp nhóm sửa nhưng không bảo đảm sửa ngay trong ngày.",
    },
    "N2_13_M11_05": {
        "passage": "学習記録アプリを導入した学科では、毎日の学習時間を入力する方式をやめ、週ごとに振り返りを書く方法を試している。時間の長さを競うと、理解が深まったかより記録を増やす行動が起きるという意見があったためだ。振り返りでは、できたことだけでなく、つまずいた点と次週に試す方法も書く。教員は記録を成績には使わず、本人と話し合う際に支援が必要かを考える手がかりにする。入力の正確さを採点する制度にはしない。",
        "explanationVi": "Thi đua số giờ có thể khiến sinh viên chú trọng tăng số ghi hơn là hiểu bài. Bài viết hằng tuần nêu cả điều đã làm, vướng mắc và cách thử tiếp theo; giáo viên dùng để trao đổi hỗ trợ, không chấm điểm.",
    },
    "N2_13_M11_06": {
        "passage": "研究室のウェブサイトでは、論文の要約を一般向けに載せている。専門用語を簡単な言葉に置き換える一方、研究で確かめた範囲を超えて「この方法なら必ず改善する」と断定しないようにしている。対象者が特定の地域や年齢に限られる場合は、その条件を示し、追加の検証が必要な点も末尾に記す。読みやすさを高めることと、研究の限界を隠さないことは両立できるという考えだ。要約から詳しい方法へ進めるリンクも置き、読者が根拠を確認できるようにしている。",
        "explanationVi": "Phòng nghiên cứu dùng lời dễ hiểu nhưng nêu cả nhóm đối tượng, điều kiện và phần cần kiểm chứng thêm. Liên kết đến phương pháp chi tiết giúp người đọc xem căn cứ; họ không khẳng định quá phạm vi dữ liệu.",
    },
    "N2_13_M11_07": {
        "passage": "大学の電子申請には、提出後に内容を修正できない手続きがある。以前は警告文が最後の画面にしかなく、添付ファイルを間違えたまま送る例が続いた。そこで申請を始める前と送信直前の二か所に確認を表示し、対象書類と提出先を見直せるようにした。操作が増えると面倒だという意見も受け、確認項目は必要なものだけに絞った。入力を間違えた場合に戻って直す方法も同じ画面に置き、誤りを防ぎながら手続きを複雑にしないようにしている。",
        "explanationVi": "Do có thủ tục không thể sửa sau khi nộp và nhiều người đính kèm nhầm tệp, trường nhắc kiểm tra cả lúc bắt đầu lẫn trước khi gửi. Họ vẫn giữ màn hình ngắn gọn và chỉ rõ cách quay lại sửa.",
    },
    "N2_13_M11_08": {
        "passage": "ある授業では、学生同士で論文を読んでコメントする活動を行っている。以前はコメント数を評価したため、短い指摘を大量に書く学生が増えたが、どの記述を問題にしたのか、根拠は何かが分かりにくかった。現在は一つのコメントに、対象となる記述、気になった理由、確かめるための資料を含めるよう求めている。教員は意見の数ではなく、コメントを受けて論文を読み直し、考えを修正した記録も見ている。",
        "explanationVi": "Khi chấm theo số lượng, góp ý ngắn nhưng thiếu căn cứ tăng lên. Tiêu chí mới yêu cầu nêu chỗ bị nhận xét, lý do và cách kiểm chứng; giáo viên cũng xem quá trình đọc lại và điều chỉnh suy nghĩ.",
    },
    "N2_13_M11_09": {
        "passage": "地方の大学は、対面で相談しにくい学生も利用できるよう、オンライン相談窓口を試験導入した。しかし、文章で状況を説明するのが難しい人や、家族と端末を共有し履歴を残したくない人もいる。そこで大学はオンラインだけに集約せず、電話と対面予約も続けることにした。利用件数が増えても、相談した人の問題が解決したとは限らないため、匿名アンケートで役立った点や使いにくかった点も聞き、窓口の見直しに使う。",
        "explanationVi": "Hình thức trực tuyến có ích với một số sinh viên nhưng không phù hợp với người khó viết hoặc cần giữ riêng tư trên thiết bị dùng chung. Trường duy trì cả điện thoại và gặp trực tiếp, đồng thời hỏi phản hồi ẩn danh vì số lượt dùng không tự chứng minh hiệu quả.",
    },
}

# The N2 item-purpose guide describes medium passages as approximately 500
# Japanese characters. These shared M11/M12 texts previously sat around half
# that size. Extend each text with task-relevant process, trade-offs, and
# evaluation criteria; all three linked questions keep their shared context.
MEDIUM_READING_OVERRIDES = {
    **{f"N2_11_M11_{i:02}": """【引き継ぎの方法】
担当者が休暇を取るとき、仕事の状況を口頭で伝えるだけでは、細かな条件が抜けることがある。そこで、ある部署では、未完了の作業、次に確認する日、連絡先を一枚の表にまとめることにした。
表を作っても、更新しなければ情報は古くなる。作業が終わった人がその日のうちに状態を直し、次の担当者が朝に確認する手順も決めた。
運用を始めた月には、引き継ぎの漏れが起きた案件を全員で振り返り、表に書く項目を整理した。相手の返事を待っている案件には、返事を待つ期限と、連絡がない場合に誰がどう確認するかを分けて記す。これにより、休暇中の担当者に電話で尋ねる回数が減り、期限の近い作業も朝の時点で把握しやすくなった。一方、項目を増やし過ぎると更新に時間がかかり、重要点が見えにくくなる。決定済みの手順は簡潔にし、例外的な判断が必要な案件は表だけで済ませず、引き継ぎの時間を設けている。顧客情報を必要以上に共有しないよう、閲覧できる人も限っている。""" for i in range(1, 4)},
    **{f"N2_11_M11_{i:02}": """【短い会議の準備】
会議を短くするために、開始時刻だけを厳守しても、議論がまとまるとは限らない。参加者が資料を読まずに集まると、前提の確認に時間を使い、決めるべき点に進めないからだ。
あるチームは、会議の前日までに資料を共有し、各自が疑問点を一つ書いておく方法を試した。会議では説明を繰り返さず、質問と選択肢の比較から始める。
この方法を一か月試すと、会議そのものの時間だけでなく、終了後に決定事項を聞き直す連絡も少なくなった。一方、資料の読み込みに慣れていない人からは、どこを判断すればよいか分からないという声があった。そこで資料の先頭に「今日決めること」と「持ち帰ること」を明記し、会議の冒頭には必要最低限の前提を確認する時間を残した。準備に時間をかけ過ぎる人もいたため、資料は結論と判断材料を中心に二ページ以内とし、詳細は必要な人だけが参照する別紙に分けた。事前読解を求めても、全員が同じ知識を持つとは限らないためである。""" for i in range(4, 7)},
    **{f"N2_11_M11_{i:02}": """【相談しやすい職場】
仕事上の失敗を早く共有すれば、問題が大きくなる前に対応できる。しかし、報告した人が責められると感じる職場では、小さな失敗ほど隠されやすい。
ある会社では、報告を受けた上司が、まず事実と影響範囲を確認し、個人の評価とは分けて再発防止を話し合うようにした。報告した人にも、原因を振り返る作業に参加してもらう。
報告後は、起きた事実、影響を受けた相手、手順が守られていたかを分けて記録する。確認不足が原因なら、チェック表や担当の割り振りを見直す。意図的な規則違反なら就業規則に沿って対応するが、いずれの場合も再発防止の議論は続ける。会社は報告件数だけを目標にせず、決めた対策が実行されたかも月ごとに確認している。この仕組みは責任をなくすためのものではない。意図的な違反と、手順や情報が不足して起きた失敗を区別し、改善できる点を組織で直すことを目的としている。""" for i in range(7, 10)},
    **{f"N2_12_M11_{i:02}": """市の環境課は、家庭ごみの量を減らすため、食品ロス対策の実証事業を始めた。協力店では、閉店前に残った食品を割引して販売する。市は当初、値引きの割合を店ごとに任せていたが、利用者から「どの程度安くなるか分からず、選びにくい」という声が出た。そこで、割引率を三段階の表示にそろえたところ、買い手が比較しやすくなり、店員の説明も短くなった。
ただし、食品ごとに期限や保存状態、売れ残りやすい時間帯は異なる。表示が同じでも値引きの価値が同じように受け取られるとは限らず、値下げだけで需要が生まれるわけでもない。実証事業では、値下げ前後の販売数だけでなく、廃棄量が減ったか、購入者が必要な量を選べたかも店から聞き取る。市は、売れ残りの件数、廃棄量、利用者の意見を合わせて確認し、事業を続けるか判断する予定である。価格表示の分かりやすさと食品ロスの削減効果を分けて評価する必要がある。""" for i in range(1, 4)},
    **{f"N2_12_M11_{i:02}": """山間部の移動手段を守るため、町は路線バスの一部を予約制の乗合車に切り替えた。従来のバスは決まった時刻に全ての停留所を回るため、利用者が少ない日も運行費がかかっていた。乗合車は予約のあった地区を通り、病院や買い物施設の近くで乗り降りできる。開始直後は予約方法が分かりにくいという声があり、町は電話の受付時間を延ばし、停留所にも説明を掲示した。
利用者は増えたが、予約が重なる朝には希望時刻から遅れる場合がある。利用者数だけを成果とすると、予約できずにあきらめた人や到着の遅れを見落とす。町は地区別の予約件数、希望時刻との差、通院や通学への影響を記録し、運転手の負担も聞くことにした。朝の便を増やせば遅れを減らせる一方、費用と人員が必要になるため、乗降地点や受付方法を調整する案も比べる。費用だけを基準にせず、必要な時間帯が保てているかを見ながら、利用者と運行担当者の意見をもとに運行範囲を決める考えだ。""" for i in range(4, 7)},
    **{f"N2_12_M11_{i:02}": """市の図書館では、利用者が本を予約して受け取る仕組みを見直した。以前は中央館に届いた本を分館へ運ぶ回数が限られており、受け取りまで長く待つ場合があった。そこで、予約が多い本は複数館に置き、各館の貸し出し状況を共通システムで確認できるようにした。導入後、平均待ち日数は短くなったが、利用が一部の館に集中する本もあり、追加購入の判断が難しい。
予約が集中する時期には、学校の課題や話題作の需要が短期間に変化する。図書館は館ごとの貸出数を一か月単位で比べ、予約取消しが多い本については、冊数を増やす前に待ち時間や受け取り場所を確かめる。貸し出し件数だけでは、予約を取り消した理由や希望する受取館までは分からないため、利用者の意見も集める方針だ。共通システムは本の所在を探しやすくするが、配送回数を増やせば費用もかかる。便利さだけで運用を決めず、複数の情報を見ながら所蔵数を調整する。""" for i in range(7, 10)},
}

# Add substantive qualifications/examples to M13's medium-text drafts. The
# extensions deepen each construct without changing the question or its key.
MEDIUM_READING_CONTINUATIONS = {
    "N2_13_M11_01": "\n\n教員は公開後の感想だけでなく、授業で同じ誤解が減ったかも確かめる予定だ。ただし成績が上がっても動画だけの効果とは限らず、課題の説明や授業内容が変わった可能性もある。作成者には根拠資料、更新日、変更点を記録してもらい、古い情報が残った場合は新しい版への案内を付ける。",
    "N2_13_M11_02": "\n\n録画を一律に消すのではなく期限を設ければ、その学期の復習には使える一方、試験問題が長期間残るのを防げる。期限後も必要部分だけ見たいという要望はあるが、切り出した映像にも問題文や発言が含まれる可能性があり、単純には延長できない。大学は検索性と、誰がいつまで見られるかという権限設定を別の課題として扱う。",
    "N2_13_M11_03": "\n\n事実が食い違うときに一方を消すと、後から訂正の経緯を確かめられない。編集部は資料の公開日、発信者、掲載日時を記録し、訂正時には訂正履歴へのリンクを付ける。取材を急ぐ場合でも未確認情報にはその旨を示し、複数の人で掲載前に確認する。読者が判断する手がかりを残すことを、話題の速さを追うことより優先している。",
    "N2_13_M11_04": "\n\n学生には、誤りを知らせる際、授業名、時間、誤認識した語も添えてもらう。語だけでは音声の該当箇所を探しにくいからだ。修正候補を教材に反映する前に、教員か補助者が録音を聞いて確かめる。字幕を直しても聞き取り方を誤ることはあり得るため、全文を暗記する資料ではなく、内容にアクセスする手がかりとして使うよう説明している。",
    "N2_13_M11_05": "\n\n週単位の振り返りなら毎日の入力負担は減るが、週末に思い出して書くため細かな学習を忘れることがある。そこで学生は、印象に残った例や理解を確かめた方法を短く記録できる。教員は記述が少ないことを怠けと決めつけず、本人と話す入口として使う。記録は能力や努力を一つの数字に置き換える評価表ではない。",
    "N2_13_M11_06": "\n\n例えば対象者が一つの地域に偏った研究では、結果を別の地域にも当てはめられるかはまだ分からない。要約では対象の条件を示し、対象外の人については追加調査が必要だと記す。読みやすさを優先して因果関係を確かめたように誤解させないため、「関連が見られた」と「原因を証明した」を使い分ける。詳しい方法へのリンクでは測定方法と対象の選び方も確認できる。",
    "N2_13_M11_07": "\n\n入力中に誤りに気づけば戻って直せるが、送信後に窓口へ連絡しても、すべての手続きで訂正できるわけではない。そのため画面には提出先と添付ファイル名を具体的に表示し、一般的な警告だけにしない。一方、確認を何度も求めると読み飛ばされるため、申請内容が変わる場面に絞って表示する。誤送信を防ぎながら、利用者に過度な操作を求めない設計を目指している。",
    "N2_13_M11_08": "\n\n以前のコメントは「分かりにくい」「説明を足すべきだ」といった感想にとどまり、書き手が何を直せばよいか伝わらないことがあった。現在は対象段落を示し、前後の定義と矛盾していないか、出典で確かめられるかを書く。受け手は指摘を必ず採用する必要はなく、理由を確かめた上で修正しない判断も記録する。評価では指摘通りに直したかより、根拠をもとに検討した過程を見る。",
    "N2_13_M11_09": "\n\n利用者の属性を尋ねると窓口改善に役立つ一方、匿名性を損なう恐れもあるため、アンケートでは個人を特定できる質問を避ける。相談員は同じ回答が続いても、個別の事情で役立つ方法は異なると考える。見直しの際は相談方法ごとの件数に加え、途中で相談をやめた理由や案内の分かりやすさも見る。ただし配置は利用者の声だけで決めず、対応時間や地域差も合わせて検討する。",
}

# M13 short texts were still much shorter than the JLPT's approximate short-
# text description. These additions provide a concrete policy consequence or
# constraint while keeping the items focused on information retrieval.
SHORT_READING_CONTINUATIONS = {
    "N2_11_M10_01": "\n\nこの表記を始めてから、担当者は版番号の小さい資料を最新版として送る間違いを減らせた。旧版を消すのではなく、必要な記録として残しながら、新しい版を名前で見つけられるようにしている。",
    "N2_11_M10_02": "\n\n問い合わせ中の欄には「確認待ち」と記し、回答を受けた日も残すことにした。過去の案件に似ているという理由だけで金額を確定すると、後から条件の違いに気づく恐れがあるためだ。",
    "N2_11_M10_05": "\n\n翌月には記録と実績を比べ、計画から漏れやすい対応が何かを確かめる。記録方法が担当者の負担になっていないかも確認し、予測に必要な項目だけを残すことにした。",
    "N2_12_M10_01": "\n\n相談の内容によっては担当窓口が異なるため、来庁後は入口の案内板を見て該当する番号札を取る。延長日に利用できる手続きの一覧は、市のウェブサイトにも掲載している。",
    "N2_13_M10_01": "\n\n質問は他の学生も読めるため、個人名や具体的な相談事情を書くと、匿名でも本人が分かる場合がある。担当窓口では個別情報を含む相談を受け付け、掲示板は授業内容を共有して確認する場として使い分ける。",
    "N2_13_M10_02": "\n\n質問への回答は任意で、回答しないことによる貸出制限もない。回答者の記録を集める調査ではないため、利用者ごとの読書履歴を作ることも目的としていない。図書館は三か月間の回答を集計し、利用状況を契約の検討に役立てる。",
    "N2_13_M10_03": "\n\n報告を受けても、担当部署が録音を確認するまでは、入力された表現が正しいとは限らない。そのため報告後すぐの修正を約束せず、確認に時間がかかる場合は予定日だけを先に知らせる。動画の視聴を止める必要はない。",
    "N2_13_M10_04": "\n\n要約を保存するときは掲載日を残し、同じ話題を扱う記事を時期や見出しで探せるようにする。全文の閲覧と外部への再掲載は契約条件に従うため、要約を利用できる範囲と記事そのものの利用範囲を混同しないよう案内している。",
    "N2_13_M10_05": "\n\n初期設定は全員共通だが、仕事や授業の時間は人によって違うため、利用者が自分に合う時刻に直せる。通知を受け取らない選択もできる一方、試験日を登録すると通知が増える仕組みではない。",
}

# The JLPT describes long thematic texts as approximately 900 characters.
# These evidence, limitation, and decision-process continuations strengthen
# the longer reasoning tasks without padding them with unrelated material.
LONG_READING_CONTINUATIONS = {
    "N2_11_M13_01": "\n\n評価の際には、導入前後の時間だけを比べるのではなく、確認の差し戻しが何件あったか、利用者から同じ問い合わせが増えていないかも見る。担当者が変わった後に問題が起きた場合は、その人の習熟度だけで説明せず、説明資料や例外手順が十分だったかを調べる。現場の担当者には、機械に任せた後に新しく生じた作業も記録してもらう。もし安全性や利用者への影響が想定より悪ければ、対象を広げずに設定を戻す選択肢も残している。",
    "N2_11_M13_02": "\n\n調査の案内を紙だけで配ると、施設を利用しない人に届きにくい。そこで市は、窓口、郵送、ウェブの複数の方法を用意し、回答にかかる時間も短くした。それでも、返事のない人の事情をすべて把握することはできないため、聞き取りの対象は年齢や利用頻度が異なる人から選ぶ。質問の順番によって答えが変わる可能性も考え、職員同士で質問文を確認してから実施する。市は結果を公表するとき、集めた回答の数と方法を示し、調査で分かった範囲と分からなかった点を分けて説明する。",
    "N2_11_M13_03": "\n\n説明を直すとき、チームは読み手が誤解した箇所だけでなく、誤解が生じた理由も検討した。専門用語の定義が先に必要だったのか、例が一般的すぎて展示物とのつながりが見えなかったのかによって、直す場所は変わるからだ。ある来館者の反応だけを基準にすると、別の読み手にはかえって分かりにくくなる場合もある。そこで、複数の職員や来館者の反応を比べ、展示の目的に照らして修正案を決める。どの説明を残すかは専門家が確認し、読みやすさを高めても、根拠のない内容に置き換えないようにしている。",
    **{f"N2_12_M13_{i:02}": "\n\n市は試験結果を比較する際、雨量や季節、工事区間の違いを記録し、一度の大雨や一種類の生き物の観察だけで結論を出さない方針だ。水害への備えは住民の安全に関わるため、環境面でよい変化が見られても、避難や堤防の機能を弱める案は採用できない。反対に、短期的な維持費だけを見ると、将来の修繕費や生態系への影響を見落とす可能性がある。観察会で寄せられた意見は、専門家の測定結果と並べて検討し、どの条件で利点と課題が現れたかを設計資料に残す。" for i in range(1, 4)},
    **{f"N2_13_M13_{i:02}": "\n\n公開後も、質問や誤解が多かった箇所を記録し、次の講座や動画の原稿に反映する。説明を分けて載せた場合は、中心の文章から方法や追加資料へ移れるリンクを確かめ、読み手が根拠にたどり着けるようにする。研究者は、やさしい表現に変えたことで条件や不確実性が消えていないかを最終確認する。広報チームは一度の原稿を完成版とみなさず、専門家の正確さの確認と、初めて読む人の理解度の確認を繰り返すことが必要だと考えている。" for i in range(1, 4)},
}

# Focused question-level repairs after editorial review. These preserve IDs and
# answer bindings while replacing weak or ambiguous distractors. The source
# fingerprint changes with the resulting question text; prior reviews remain
# attached only to their historical versions.
QUESTION_REVISIONS = {
    "N2_11_M10_01": {
        "optionsById": {"A": "修正者ごとに保存先を分けること", "B": "古い版を削除し、最新版だけを残すこと", "C": "ファイルを開いてから新旧を確認すること", "D": "ファイルを開かなくても、新旧を見分けること"},
        "explanationVi": "Ngày tạo và số phiên bản được ghi ngay trên tên tệp, nên người dùng nhận ra bản mới trước khi mở. Bài đọc nói các bản cũ vẫn được giữ; việc lưu riêng theo người sửa hoặc mở tệp để kiểm tra không phải mục tiêu.",
    },
    "N2_11_M10_02": {
        "optionsById": {"A": "見積書の金額は前回と同じ条件だと確認できたから", "B": "条件が同じとは限らず、過去の金額を当てはめられないから", "C": "見積書の総額が変わったと分かったから", "D": "取引を断る判断がすでに済んでいたから"},
        "explanationVi": "Con số trước đây chỉ giống về bề ngoài; điều kiện giao hàng có thể khác. Người phụ trách xác minh trước khi dùng số chưa rõ căn cứ, chứ không xác nhận điều kiện giống nhau hay quyết định hủy giao dịch.",
    },
    "N2_11_M10_03": {
        "optionsById": {"A": "個人が特定される情報を社外に公開しないため", "B": "社外向けの映像を一定の長さに整えるため", "C": "研修の説明を外部向けに全面的に書き換えるため", "D": "社員名の読み方を字幕で補足し、視聴者に正確に伝えるため"},
        "explanationVi": "Vì video được chia sẻ ra ngoài công ty, tên và thông báo có thể nhận diện nhân viên nên cần cắt hoặc làm mờ. Nội dung đào tạo vẫn được giữ lại; độ dài và cách đọc tên không phải lý do.",
    },
    "N2_11_M10_04": {
        "optionsById": {"A": "旧会場の情報で参加者が遅れるのを防ぐこと", "B": "参加希望者が増えたことを知らせ、追加の申込みを受けること", "C": "会場変更に合わせ、開始時刻と議題も更新して伝えること", "D": "新しい会場の定員に合わせ、参加者数を再調整すること"},
        "explanationVi": "Một số người đã lưu thông báo cũ; gửi bản đính chính để họ đến đúng phòng. Giờ và chương trình không đổi, cuộc họp cũng không bị hủy.",
    },
    "N2_11_M10_05": {
        "optionsById": {"A": "次月の業務量や必要な人員を現実に近く見積もるため", "B": "予定外の対応にかかった時間を、担当者ごとの人事評価に反映するため", "C": "翌月にも起きる急な仕事をなくす手順を決めるため", "D": "計画した作業と突発的な対応を、別々の報告欄で管理するため"},
        "explanationVi": "Ghi cả thời gian phát sinh giúp dự báo khối lượng và nhân lực tháng sau sát thực tế. Bài đọc loại trừ việc xếp hạng cá nhân; việc ghi chép không thể chứng minh rằng tháng sau sẽ không có việc phát sinh.",
    },
    "N2_11_M11_01": {
        "optionsById": {"A": "未完了の作業・担当者・完了予定日", "B": "未完了の作業・次に確認する日・連絡先", "C": "完了した作業・評価・休暇予定", "D": "取引先との全記録・社員の個人予定"},
        "explanationVi": "Bảng ghi việc chưa hoàn tất, ngày cần kiểm tra tiếp và thông tin liên hệ. Đây là các mục được nêu trực tiếp; nó không phải bảng đánh giá nhân viên hay lưu toàn bộ hồ sơ giao dịch.",
    },
    "N2_11_M11_02": {
        "stem": "作業の状態をその日のうちに更新する手順を設けたのはなぜか。",
        "optionsById": {"A": "更新しないと、表の情報が古くなるため", "B": "例外的な案件も表だけで判断できるようにするため", "C": "顧客情報を全員に共有するため", "D": "次の担当者が朝に確認する必要をなくすため"},
        "explanationVi": "Nếu không cập nhật sau khi xử lý, bảng sẽ không phản ánh tình trạng mới. Việc này giúp người nhận kiểm tra buổi sáng; các vụ ngoại lệ vẫn cần thời gian bàn giao trực tiếp.",
    },
    "N2_11_M11_03": {
        "optionsById": {"A": "表から外し、元の担当者が戻るまで保留する", "B": "表に記録すれば、口頭での引き継ぎは行わない", "C": "判断を別部署にすべて任せる", "D": "表に加えて、引き継ぎの時間を設ける"},
        "explanationVi": "Với vụ cần phán đoán ngoại lệ, bài đọc nói bảng không đủ và cần dành thời gian bàn giao trực tiếp. Nhóm không bỏ vụ việc, chờ người cũ quay lại hay chuyển toàn bộ trách nhiệm đi nơi khác.",
    },
    "N2_11_M11_04": {
        "optionsById": {"A": "参加者が資料を読まずに集まり、前提確認から始めていたこと", "B": "開始時刻を守ることを優先し、質問を後回しにしたこと", "C": "会議前に資料と疑問点を共有していたこと", "D": "資料を二ページ以内に制限していたこと"},
        "explanationVi": "Người tham dự chưa đọc tài liệu nên phải thống nhất lại tiền đề trong cuộc họp. Việc chia sẻ tài liệu và ghi câu hỏi là biện pháp được thử sau đó, không phải nguyên nhân của thời gian xác nhận kéo dài.",
    },
    "N2_11_M11_05": {
        "stem": "会議を質問や選択肢の比較から始めるため、チームが事前に求めたことは何か。",
        "optionsById": {"A": "結論を決めてから会議に参加する", "B": "全員で詳細な別紙を作成する", "C": "資料を読み、疑問点を一つ用意する", "D": "会議後に疑問点をまとめて送る"},
        "explanationVi": "Nhóm gửi tài liệu trước và yêu cầu mỗi người ghi sẵn một câu hỏi để cuộc họp bắt đầu bằng câu hỏi và so sánh lựa chọn. Không yêu cầu người tham gia quyết định trước hoặc viết phụ lục chi tiết.",
    },
    "N2_11_M11_06": {
        "optionsById": {"A": "全員が同じ時間だけ資料を読むようにするため", "B": "判断材料を別紙へ移し、主資料から外すため", "C": "会議で質問を出さないようにするため", "D": "準備の負担を抑え、判断点を見つけやすくするため"},
        "explanationVi": "Một số người mất quá nhiều thời gian chuẩn bị và khó biết cần quyết định gì. Giới hạn hai trang giữ trọng tâm trong tài liệu chính, còn chi tiết đưa vào phụ lục.",
    },
    "N2_11_M11_07": {
        "optionsById": {"A": "報告後に事実や影響範囲を確かめる職場", "B": "報告した人が責められると感じる職場", "C": "対策の実行状況を月ごとに確かめる職場", "D": "意図的な違反と手順上の失敗を区別する職場"},
        "explanationVi": "Khi người báo cáo nghĩ rằng mình sẽ bị trách, họ dễ giấu lỗi nhỏ. Việc xác minh sự việc, theo dõi biện pháp và phân biệt lỗi cố ý với lỗi quy trình là các cách ứng xử được công ty áp dụng.",
    },
    "N2_11_M11_08": {
        "optionsById": {"A": "報告者の評価を先に見直す", "B": "処分を決めてから影響範囲を調べる", "C": "再発防止策を決めてから事実を確認する", "D": "まず事実と影響の範囲を確かめる"},
        "explanationVi": "Sau khi nhận báo cáo, cấp quản lý trước hết xác minh sự việc và phạm vi ảnh hưởng. Việc phân tích nguyên nhân, trách nhiệm và phòng ngừa tái diễn đến sau bước xác minh này.",
    },
    "N2_11_M11_09": {
        "optionsById": {"A": "失敗を報告した人の責任をすべて免除する", "B": "報告件数を増やすことだけを目標にする", "C": "原因を区別し、組織で改善できる点を直す", "D": "意図の有無にかかわらず、すべて処分する"},
        "explanationVi": "Cơ chế không xóa bỏ trách nhiệm hay chỉ đếm báo cáo. Nó phân biệt vi phạm cố ý với lỗi do quy trình/thông tin để sửa những điểm tổ chức có thể cải thiện.",
    },
    "N2_11_M13_01": {
        "optionsById": {"A": "定型作業でも入力時間はまったく減らなかったため", "B": "時間短縮だけでなく、例外時の確認と利用者への影響も見るため", "C": "利用者への説明は対象を広げた後に行うため", "D": "機械に任せた仕事には記録が必要ないため"},
        "explanationVi": "Thử nghiệm giảm nhập liệu nhưng một số điều kiện lại làm khâu xác nhận lâu hơn. Công ty kiểm tra ngoại lệ, tác động đến người dùng và công việc phát sinh trước khi mở rộng.",
    },
    "N2_11_M13_02": {
        "optionsById": {"A": "回答数が多ければ、全利用者の意見とみなせるため", "B": "聞き取りの結果でアンケートの数値をすべて置き換えるため", "C": "回答の偏りや、数字だけでは分からない理由を確かめるため", "D": "回答しなかった人を制度の対象から外すため"},
        "explanationVi": "Số lượng trả lời không bảo đảm đại diện cho mọi người; khảo sát và phỏng vấn ngắn bổ sung cho nhau để tìm thiên lệch cũng như nguyên nhân cụ thể. Bài đọc không loại bỏ khảo sát hay người không trả lời.",
    },
    "N2_11_M13_03": {
        "optionsById": {"A": "専門用語をすべて削除し、図だけで説明する", "B": "中心を定め、必要な専門語に説明を添え、反応を見て直す", "C": "一人の来館者の反応を優先し、専門家の確認を省く", "D": "読みやすさを優先し、根拠の確認を省く"},
        "explanationVi": "Nhóm xác định ý trung tâm, giải thích thuật ngữ cần giữ và dùng phản hồi của nhiều người để sửa thứ tự. Chuyên gia vẫn kiểm tra độ chính xác; không xóa hết thuật ngữ hay dựa vào một người đọc duy nhất.",
    },
    "N2_12_M11_01": {
        "optionsById": {"A": "値下げ前後の販売数だけで事業の効果を決めるため", "B": "店ごとに異なる表示を残し、選び方を店員に任せるため", "C": "利用者が値引きの程度を比べやすくするため", "D": "すべての商品を同じ価格で販売するため"},
        "explanationVi": "Người mua nói khó chọn vì không biết mức giảm của từng cửa hàng. Ba mức hiển thị thống nhất giúp so sánh dễ hơn; nó không cố định giá hoặc thay thế việc đánh giá lượng rác thực phẩm.",
    },
    "N2_12_M11_02": {
        "stem": "表示をそろえた後、店員側に起きた変化はどれか。",
        "optionsById": {"A": "購入者が値引きの程度を比べる機会がなくなった", "B": "店ごとに割引率を独自に決めるようになった", "C": "売れ残りや廃棄がなくなった", "D": "値引きについての説明が短くなった"},
        "explanationVi": "Câu hỏi giới hạn vào thay đổi phía nhân viên: cách trình bày thống nhất giúp họ giải thích ngắn hơn. Người mua cũng so sánh dễ hơn, nhưng đó là thay đổi ở phía khách hàng.",
    },
    "N2_12_M11_03": {
        "stem": "市が販売数だけでなく廃棄量や利用者の意見も見るのはなぜか。",
        "optionsById": {"A": "参加店の売上順位で、協力の程度を決めるため", "B": "表示が分かりやすければ、廃棄量も必ず減ると示すため", "C": "表示の分かりやすさと食品ロス削減の効果を分けて評価するため", "D": "利用者全員の希望を一つの商品に反映するため"},
        "explanationVi": "Hiển thị dễ hiểu chưa chứng minh rằng lượng thực phẩm bị bỏ đi đã giảm. Thành phố dự định kết hợp lượng bán, lượng bỏ đi và ý kiến người dùng để đánh giá riêng hiệu quả của chương trình.",
    },
    "N2_12_M11_04": {
        "optionsById": {"A": "病院が町外へ移転し、旧路線を使えなくなったため", "B": "利用が少ない日も、決まった路線を運行する費用がかかっていたため", "C": "運転手を増やし、全停留所を同時に回るため", "D": "すべての停留所をなくす方針になったため"},
        "explanationVi": "Xe buýt chạy cố định vẫn phát sinh chi phí vào những ngày ít người đi. Xe đặt trước là cách thay thế một phần tuyến để phù hợp nhu cầu; văn bản không nói bệnh viện chuyển đi hay toàn bộ điểm dừng bị bỏ.",
    },
    "N2_12_M11_05": {
        "optionsById": {"A": "朝の遅れをなくすため、運転手を増やす", "B": "予約を不要にして、当日乗車へ切り替える", "C": "運行範囲を縮め、予約できる地区を減らす", "D": "予約方法が分かりにくいという声に対応する"},
        "explanationVi": "町 kéo dài giờ nhận đặt qua điện thoại sau khi người dân nói cách đặt khó hiểu. Đây là điều chỉnh hướng dẫn/tiếp nhận, không phải bỏ đặt chỗ hay sửa lịch xe buổi sáng.",
    },
    "N2_12_M11_06": {
        "optionsById": {"A": "全ての地区を同じ時刻に運行すること", "B": "以前の路線を費用に関係なく完全に再現すること", "C": "費用を最小にすることだけ", "D": "通院や通学に必要な時間帯を保ちつつ、運行範囲を考えること"},
        "explanationVi": "Thành phố cân nhắc nhu cầu đi khám và đi học cùng chi phí, nhân lực và ý kiến người dùng/đơn vị vận hành. Bài đọc bác bỏ việc tối thiểu hóa chi phí như tiêu chí duy nhất.",
    },
    "N2_12_M11_07": {
        "optionsById": {"A": "各館の書棚に同じ本をすべてそろえること", "B": "予約取消しを防ぐため貸出期間を一律に延ばすこと", "C": "配送をなくし、中央館での受け取りに戻すこと", "D": "予約した本を受け取るまでの待ち時間を短くすること"},
        "explanationVi": "Việc đặt sách về nhiều chi nhánh và dùng hệ thống chung nhằm rút ngắn thời gian chờ nhận sách. Đoạn văn vẫn nói chi phí giao nhận và nhu cầu từng chi nhánh cần được cân nhắc.",
    },
    "N2_12_M11_08": {
        "optionsById": {"A": "需要が本や館によって偏り、購入冊数を決めにくい", "B": "導入後、平均待ち日数が必ず長くなった", "C": "共通システムで各館の所蔵状況を確認できない", "D": "利用者の希望を聞けず、配送費だけで決める"},
        "explanationVi": "平均日 chờ đã giảm nhưng nhu cầu của một số sách tập trung ở vài chi nhánh nên quyết định mua thêm khó hơn. Hệ thống chung và việc lấy ý kiến người dùng vẫn hoạt động.",
    },
    "N2_12_M11_09": {
        "stem": "貸出件数だけでは分からないため、図書館が所蔵数の調整に使う情報は何か。",
        "optionsById": {"A": "本の大きさと棚の空きだけ", "B": "貸出数・予約取消し・待ち時間・希望する受取館など", "C": "貸出件数だけ", "D": "配送費だけ"},
        "explanationVi": "Số lượt mượn không cho biết vì sao người đọc hủy đặt hoặc muốn nhận sách ở chi nhánh nào. Vì vậy thư viện kết hợp số liệu mượn, hủy đặt, thời gian chờ và ý kiến người dùng.",
    },
    "N2_12_M13_01": {
        "optionsById": {"A": "護岸工事の結果、避難範囲が広がり、住民から水位を保つよう求められた", "B": "市が住民の要望を受け、環境団体に工事中止の判断を任せた", "C": "草刈り費用が予想より下がり、植物を残す必要がなくなった", "D": "下流の流れが速まり、魚の産卵場所が減っていた"},
        "explanationVi": "Khảo sát cho thấy dòng chảy phía hạ lưu nhanh hơn và bãi cạn nơi cá đẻ trứng bị thu hẹp; đó là kết quả khiến thành phố xem lại kế hoạch. Ý kiến cư dân và nhóm môi trường là phần tranh luận sau đó.",
    },
    "N2_12_M13_02": {
        "optionsById": {"A": "草刈りや水位に関する懸念を、小さな区間で確かめるため", "B": "本工事の効果を早く確認するため、試験結果を待たずに全区間へ広げる", "C": "草刈りの費用だけを比べ、生態系や安全性は試験対象にしない", "D": "市民の観察会を開かず、専門家の測定だけで案を決める"},
        "explanationVi": "Thử nghiệm quy mô nhỏ giúp kiểm tra thực tế lo ngại về cỏ, tầm nhìn và mực nước trước khi quyết định phạm vi công trình. Thành phố vẫn đánh giá cả an toàn, chi phí và hệ sinh thái.",
    },
    "N2_12_M13_03": {
        "optionsById": {"A": "住民の記録を設計に取り入れるが、安全性や維持費の評価とは切り離す", "B": "住民の記録も用いるが、複数の基準を合わせて評価する", "C": "参加人数の多さを基準に、案の安全性を判断する", "D": "専門家の測定と住民の観察のうち、人数の多い側の意見を採用する"},
        "explanationVi": "Quan sát của cư dân được đưa vào thiết kế, nhưng số người tham gia không tự chứng minh phương án an toàn. Thành phố đặt ý kiến tại chỗ cạnh số liệu chuyên gia và đánh giá nhiều tiêu chí.",
    },
    "N2_13_M10_03": {
        "optionsById": {"A": "誤りの位置だけを示し、正しい表現は担当部署に調べてもらう", "B": "誤りの箇所と正しい表現の両方を書く", "C": "正しい表現だけを書き、字幕の位置は示さない", "D": "訂正予定日が表示されるまで報告を待つ"},
        "explanationVi": "Báo cáo cần nêu cả vị trí sai lẫn cách viết đúng để bộ phận phụ trách xác minh và sửa. Chỉ gửi một trong hai thông tin sẽ khó tìm hoặc kiểm tra đúng chỗ.",
    },
    "N2_13_M11_03": {
        "stem": "読者が情報の確かさを判断できるよう、編集部が記事で明らかにしていることは何か。",
        "optionsById": {"A": "確認できた事実と、まだ確認できていない情報の違い", "B": "投稿が広く共有されているかどうかを、事実確認の代わりに示すこと", "C": "確認できなかった点を記事から外し、確定した内容だけに整理した経緯", "D": "投稿の表現を編集部が要約し、発信者に代わって見解を示した内容"},
        "explanationVi": "Ban biên tập tách điều đã xác minh khỏi điều còn chưa rõ để độc giả tự đánh giá mức đáng tin. Họ giữ dấu vết về nguồn và sai khác, không xóa đi hay tự viết lại phát biểu.",
    },
    "N2_13_M11_07": {
        "stem": "確認の機会を設けながら操作を増やし過ぎないため、大学が行った工夫はどれか。",
        "optionsById": {"A": "提出後に窓口が全ての申請を修正する", "B": "添付ファイルの種類を一つに限定する", "C": "送信のたびに同じ警告を何度も表示する", "D": "提出先と添付名を示し、必要な場面に確認を絞る"},
        "explanationVi": "Đại học hiển thị cụ thể nơi nộp và tên tệp ở các điểm quan trọng, đồng thời không lặp cảnh báo không cần thiết. Cách này vừa giúp ngăn gửi nhầm vừa tránh tạo quá nhiều thao tác.",
    },
    "N2_13_M11_08": {
        "optionsById": {"A": "コメント数より、根拠を考えて論文を読み直す過程を重視する", "B": "コメントの長さや資料の数をそろえ、形式面の統一を評価する", "C": "指摘を受けた学生が、理由を問わず修正を採用したかを見る", "D": "教員が論文を先に修正し、学生同士のコメントを省く"},
        "explanationVi": "Nhóm chuyển từ đếm bình luận sang xem người viết có nêu căn cứ và đọc lại để cân nhắc hay không. Người nhận không buộc phải làm theo mọi góp ý; điều quan trọng là quá trình đánh giá có lý do.",
    },
    "N2_13_M11_09": {
        "optionsById": {"A": "履歴が残る心配がある人には、相談窓口を案内しない", "B": "オンラインの利用が増えたら、電話と対面を縮小する", "C": "相談方法ごとの利用件数だけで配置を決め、匿名の意見は使わない", "D": "異なる事情に合わせて複数の相談方法を残し、使いにくさも調べる"},
        "explanationVi": "Sinh viên gặp những trở ngại khác nhau với viết trực tuyến hoặc chia sẻ thiết bị. Đại học giữ cả điện thoại và gặp trực tiếp, đồng thời hỏi ẩn danh về điểm hữu ích và khó dùng.",
    },
    "N2_13_M13_03": {
        "optionsById": {"A": "方法と限界を中心の文章にすべて集め、追加資料のページは設けない", "B": "専門用語を言い換えれば、対象や条件の制約は説明しなくてよい", "C": "中心となる知見と適用範囲を示し、詳しい根拠へ進めるようにする", "D": "専門家以外の読み手には見せず、正確性を研究者だけで確認する"},
        "explanationVi": "Mục tiêu là giúp người đọc nắm ý chính và phạm vi áp dụng, rồi có thể mở phần phương pháp/tài liệu chi tiết. Bài đọc không yêu cầu đưa mọi chi tiết vào phần chính hay xóa giới hạn nghiên cứu.",
    },
}


def apply_phase_71_reading_repairs(items):
    by_id = {item.get("id"): item for item in items}
    mock_numbers = {item_id.split("_")[1] for item_id in by_id if item_id.startswith("N2_")}
    if not mock_numbers:
        raise ValueError("Phase 7.1 reading patch requires N2 mock item IDs")
    applicable = {
        qid: patch for qid, patch in PATCHES.items()
        if any(qid.startswith(f"N2_{mock_number}_") for mock_number in mock_numbers)
    }
    applicable.update({
        qid: {"passage": passage}
        for qid, passage in MEDIUM_READING_OVERRIDES.items()
        if any(qid.startswith(f"N2_{mock_number}_") for mock_number in mock_numbers)
    })
    applicable.update({
        qid: {**applicable.get(qid, {}), "appendPassage": continuation}
        for qid, continuation in MEDIUM_READING_CONTINUATIONS.items()
        if any(qid.startswith(f"N2_{mock_number}_") for mock_number in mock_numbers)
    })
    applicable.update({
        qid: {**applicable.get(qid, {}), "appendPassage": continuation}
        for qid, continuation in SHORT_READING_CONTINUATIONS.items()
        if any(qid.startswith(f"N2_{mock_number}_") for mock_number in mock_numbers)
    })
    applicable.update({
        qid: {**applicable.get(qid, {}), "appendPassage": continuation}
        for qid, continuation in LONG_READING_CONTINUATIONS.items()
        if any(qid.startswith(f"N2_{mock_number}_") for mock_number in mock_numbers)
    })
    missing = sorted(set(applicable) - set(by_id))
    if missing:
        raise ValueError("Phase 7.1 reading patch IDs missing from candidate: " + ", ".join(missing))

    for qid, patch in applicable.items():
        item = by_id[qid]
        if not item.get("typeId", "").startswith("N2-RD-"):
            raise ValueError(f"{qid}: refusing to apply a reading patch to a non-reading item")
        passage = patch.get("passage", item.get("passage") or item.get("contextPassage", ""))
        passage += patch.get("appendPassage", "")
        item["passage"] = passage
        item["contextPassage"] = passage
        if "stem" in patch:
            item["stem"] = patch["stem"]
        if "correctText" in patch:
            correct_id = item.get("correctAnswer")
            options_by_id = {option["id"]: option for option in item.get("options", [])}
            if correct_id not in options_by_id or len(patch["distractors"]) != 3:
                raise ValueError(f"{qid}: keyed option or distractor count is invalid")
            options_by_id[correct_id]["text"] = patch["correctText"]
            distractor_ids = sorted(option_id for option_id in options_by_id if option_id != correct_id)
            for option_id, text in zip(distractor_ids, patch["distractors"], strict=True):
                options_by_id[option_id]["text"] = text
            if len({option["text"] for option in item["options"]}) != 4:
                raise ValueError(f"{qid}: updated options are not distinct")
            item["distractorExplanations"] = {
                option_id: rationale
                for option_id, rationale in zip(distractor_ids, patch["distractorRationales"], strict=True)
            }
        if "explanationVi" in patch:
            item["explanation"] = patch["explanationVi"]
            item["explanationVi"] = patch["explanationVi"]

    revisions = {
        qid: revision for qid, revision in QUESTION_REVISIONS.items()
        if any(qid.startswith(f"N2_{mock_number}_") for mock_number in mock_numbers)
    }
    missing_revisions = sorted(set(revisions) - set(by_id))
    if missing_revisions:
        raise ValueError("Phase 7.1 question revision IDs missing: " + ", ".join(missing_revisions))
    for qid, revision in revisions.items():
        item = by_id[qid]
        if "stem" in revision:
            item["stem"] = revision["stem"]
        if "optionsById" in revision:
            options_by_id = {option.get("id"): option for option in item.get("options", [])}
            replacement = revision["optionsById"]
            if set(replacement) != set(options_by_id) or len(options_by_id) != 4:
                raise ValueError(f"{qid}: question revision must cover exactly four existing options")
            if item.get("correctAnswer") not in replacement:
                raise ValueError(f"{qid}: question revision would unbind the answer key")
            for option_id, text in replacement.items():
                options_by_id[option_id]["text"] = text
            if len({option["text"] for option in item["options"]}) != 4:
                raise ValueError(f"{qid}: revised options must be distinct")
        if "explanationVi" in revision:
            item["explanation"] = revision["explanationVi"]
            item["explanationVi"] = revision["explanationVi"]
    applicable_revisions = {
        qid: revision for qid, revision in revisions.items()
        if qid in DISTRACTOR_RATIONALES
    }
    for qid in applicable_revisions:
        item = by_id[qid]
        item["distractorExplanations"] = {
            option_id: record[1]
            for option_id, record in DISTRACTOR_RATIONALES[qid].items()
        }
    rationale_errors = validate_distractor_rationales(
        [by_id[qid] for qid in applicable_revisions], applicable_revisions
    )
    if rationale_errors:
        raise ValueError("Phase 7.1 distractor rationale validation failed: " + "; ".join(rationale_errors))
    return items
