# -*- coding: utf-8 -*-
"""Option-bound Vietnamese distractor rationales for the Phase 7.1 candidate.

Each record stores the exact wrong-option text alongside its explanation so a
later option edit cannot silently inherit stale feedback.
"""
from __future__ import annotations


DISTRACTOR_RATIONALES = {
    "N2_11_M10_01": {
        "A": ("修正者ごとに保存先を分けること", "Bài đọc nói mọi người vẫn dùng chung một thư mục. Quy tắc mới thay đổi tên tệp, không chia nơi lưu theo người sửa."),
        "B": ("古い版を削除し、最新版だけを残すこと", "Đoạn sau nói rõ bản cũ vẫn được giữ làm hồ sơ. Mục tiêu là nhận ra bản mới qua tên tệp, không xóa các phiên bản cũ."),
        "C": ("ファイルを開いてから新旧を確認すること", "Vấn đề ban đầu là phải mở từng tệp mới biết bản nào mới. Cách ghi ngày và số phiên bản giúp phân biệt trước khi mở."),
    },
    "N2_11_M10_02": {
        "A": ("見積書の金額は前回と同じ条件だと確認できたから", "Người phụ trách chưa xác nhận điều kiện giống nhau; bài đọc nói điều kiện giao hàng thay đổi thì số tiền cũng có thể đổi."),
        "C": ("見積書の総額が変わったと分かったから", "Chỉ có một khoản thiếu giải thích cần hỏi lại. Không có thông tin cho biết tổng tiền đã thay đổi."),
        "D": ("取引を断る判断がすでに済んでいたから", "Người phụ trách vẫn hỏi căn cứ của khoản tiền và tạm không dùng nó để tính giá thành; bài không nói đã quyết định từ chối giao dịch."),
    },
    "N2_11_M10_03": {
        "B": ("社外向けの映像を一定の長さに整えるため", "Các cảnh cần xử lý là cảnh có tên nhân viên hoặc thông báo. Thời lượng video không được nêu là mục tiêu chỉnh sửa."),
        "C": ("研修の説明を外部向けに全面的に書き換えるため", "Giảng viên yêu cầu giữ phần giải thích đào tạo và chỉ kiểm tra thông tin nhận diện cá nhân; không yêu cầu viết lại nội dung."),
        "D": ("社員名の読み方を字幕で補足し、視聴者に正確に伝えるため", "Tên nhân viên được che hoặc cắt để tránh nhận diện, không được bổ sung cách đọc vào phụ đề."),
    },
    "N2_11_M10_04": {
        "B": ("参加希望者が増えたことを知らせ、追加の申込みを受けること", "Bài chỉ nói gửi lại thông tin đã sửa sau khi đổi phòng. Không mở thêm lượt đăng ký; mục tiêu trực tiếp là tránh người dựa vào địa điểm cũ."),
        "C": ("会場変更に合わせ、開始時刻と議題も更新して伝えること", "Giờ và chủ đề họp được giữ nguyên; bản sửa chỉ đổi địa điểm."),
        "D": ("新しい会場の定員に合わせ、参加者数を再調整すること", "Phòng mới được chọn để tất cả người muốn dự đều có chỗ. Không có thủ tục giảm hoặc xếp lại người tham gia."),
    },
    "N2_11_M10_05": {
        "B": ("予定外の対応にかかった時間を、担当者ごとの人事評価に反映するため", "Bài loại trừ việc dùng số liệu để đánh giá tốc độ xử lý từng người. Dữ liệu phục vụ dự báo công việc và nhân lực tháng sau."),
        "C": ("翌月にも起きる急な仕事をなくす手順を決めるため", "Việc phát sinh thay đổi theo từng tháng; ghi thời gian không đồng nghĩa có thể loại bỏ các sự việc đó."),
        "D": ("計画した作業と突発的な対応を、別々の報告欄で管理するため", "Bài nói ghi cả giờ làm theo kế hoạch lẫn giờ phát sinh để dự báo khối lượng. Việc chia chúng thành các ô báo cáo riêng không được nêu là mục tiêu."),
    },
    "N2_11_M11_01": {
        "A": ("未完了の作業・担当者・完了予定日", "Bài nêu ngày cần kiểm tra tiếp, không phải ngày dự kiến hoàn tất; bảng cũng không liệt kê riêng người phụ trách theo lựa chọn này."),
        "C": ("完了した作業・評価・休暇予定", "Bảng tập trung vào việc chưa xong để bàn giao. Đánh giá nhân viên và lịch nghỉ không phải các mục được nêu."),
        "D": ("取引先との全記録・社員の個人予定", "Đoạn cuối còn giới hạn người được xem để tránh chia sẻ quá mức thông tin khách hàng; bảng không chứa toàn bộ hồ sơ và lịch cá nhân."),
    },
    "N2_11_M11_02": {
        "B": ("例外的な案件も表だけで判断できるようにするため", "Bài nói các vụ cần phán đoán ngoại lệ không thể xử lý chỉ bằng bảng; họ vẫn dành thời gian bàn giao."),
        "C": ("顧客情報を全員に共有するため", "Quyền xem bị giới hạn để không chia sẻ quá mức thông tin khách hàng; cập nhật trạng thái không nhằm mở quyền cho mọi người."),
        "D": ("次の担当者が朝に確認する必要をなくすため", "Quy trình mới yêu cầu người nhận kiểm tra bảng vào buổi sáng. Cập nhật trong ngày giúp thông tin lúc đó không bị cũ."),
    },
    "N2_11_M11_03": {
        "A": ("表から外し、元の担当者が戻るまで保留する", "Bài yêu cầu xử lý ngoại lệ bằng buổi bàn giao bổ sung, không giữ nguyên vụ việc chờ người nghỉ quay lại."),
        "B": ("表に記録すれば、口頭での引き継ぎは行わない", "Tác giả nói rõ các vụ cần quyết định ngoại lệ không thể chỉ dựa vào bảng; phải dành thời gian bàn giao."),
        "C": ("判断を別部署にすべて任せる", "Trách nhiệm xử lý vẫn ở bộ phận đang bàn giao. Bài không nói chuyển toàn bộ quyết định sang phòng ban khác."),
    },
    "N2_11_M11_04": {
        "B": ("開始時刻を守ることを優先し、質問を後回しにしたこと", "Nguyên nhân được nêu là người dự đến mà chưa đọc tài liệu nên phải xác nhận tiền đề. Việc trì hoãn câu hỏi không được nói đến."),
        "C": ("会議前に資料と疑問点を共有していたこと", "Chia sẻ trước và chuẩn bị câu hỏi là cách nhóm thử sau khi nhận ra vấn đề, không phải nguyên nhân ban đầu."),
        "D": ("資料を二ページ以内に制限していたこと", "Giới hạn hai trang được áp dụng về sau để giảm gánh nặng chuẩn bị; nguyên nhân ban đầu là tài liệu chưa được đọc."),
    },
    "N2_11_M11_05": {
        "A": ("結論を決めてから会議に参加する", "Nhóm muốn mọi người chuẩn bị một câu hỏi, không yêu cầu họ quyết định trước khi nghe thảo luận."),
        "B": ("全員で詳細な別紙を作成する", "Tài liệu chi tiết được tách thành phụ lục cho người cần xem; người dự không được yêu cầu cùng viết phụ lục."),
        "D": ("会議後に疑問点をまとめて送る", "Câu hỏi cần được chuẩn bị trước để cuộc họp bắt đầu bằng trao đổi; gửi sau cuộc họp không phục vụ mục tiêu đó."),
    },
    "N2_11_M11_06": {
        "A": ("全員が同じ時間だけ資料を読むようにするため", "Giới hạn độ dài không đảm bảo mọi người đọc cùng thời lượng; lý do là giảm thời gian chuẩn bị quá mức."),
        "B": ("判断材料を別紙へ移し、主資料から外すため", "Chỉ chi tiết dành cho người cần mới đưa sang phụ lục. Kết luận và căn cứ cần quyết định vẫn ở tài liệu chính."),
        "C": ("会議で質問を出さないようにするため", "Câu hỏi là một phần của cách họp mới; tài liệu ngắn giúp tìm điểm cần quyết định, không nhằm ngăn đặt câu hỏi."),
    },
    "N2_11_M11_07": {
        "A": ("報告後に事実や影響範囲を確かめる職場", "Việc xác minh là quy trình công ty dùng để xử lý báo cáo; thái độ khiến lỗi nhỏ bị giấu là người báo cáo sợ bị trách."),
        "C": ("対策の実行状況を月ごとに確かめる職場", "Theo dõi biện pháp hàng tháng là hoạt động sau báo cáo, nhằm cải thiện hệ thống chứ không tạo tâm lý sợ báo lỗi."),
        "D": ("意図的な違反と手順上の失敗を区別する職場", "Công ty phân biệt vi phạm cố ý với lỗi quy trình để sửa nguyên nhân tổ chức; đây là cách ứng xử hỗ trợ báo cáo, không phải điều làm người ta giấu lỗi."),
    },
    "N2_11_M11_08": {
        "A": ("報告者の評価を先に見直す", "Bài nói cấp trên trước hết xác minh sự việc và phạm vi ảnh hưởng; đánh giá cá nhân được tách khỏi bước này."),
        "B": ("処分を決めてから影響範囲を調べる", "Thứ tự bị đảo: phải xác định sự việc và người bị ảnh hưởng trước rồi mới xử lý nguyên nhân hoặc vi phạm."),
        "C": ("再発防止策を決めてから事実を確認する", "Đây cũng là đảo trình tự. Không thể chọn biện pháp phòng ngừa trước khi biết chính xác điều gì đã xảy ra."),
    },
    "N2_11_M11_09": {
        "A": ("失敗を報告した人の責任をすべて免除する", "Bài nói rõ cơ chế không xóa trách nhiệm; vi phạm cố ý vẫn được xử lý theo nội quy."),
        "B": ("報告件数を増やすことだけを目標にする", "Công ty không chỉ đếm số báo cáo mà còn kiểm tra hàng tháng xem biện pháp đã thực hiện chưa."),
        "D": ("意図の有無にかかわらず、すべて処分する", "Cơ chế phân biệt hành vi cố ý với lỗi do thủ tục hoặc thiếu thông tin; không xử phạt mọi trường hợp như nhau."),
    },
    "N2_11_M13_01": {
        "A": ("定型作業でも入力時間はまったく減らなかったため", "Thử nghiệm cho thấy thời gian nhập liệu giảm. Vấn đề khiến công ty chưa mở rộng là một số điều kiện làm khâu xác nhận lâu hơn."),
        "C": ("利用者への説明は対象を広げた後に行うため", "Người dùng được giải thích thay đổi và nơi hỏi trước khi mở rộng. Công ty kiểm tra tác động này từ giai đoạn thử."),
        "D": ("機械に任せた仕事には記録が必要ないため", "Công ty yêu cầu ghi loại việc, điều kiện, quyết định và việc mới phát sinh sau tự động hóa để đánh giá toàn bộ quy trình."),
    },
    "N2_11_M13_02": {
        "A": ("回答数が多ければ、全利用者の意見とみなせるため", "Bài cảnh báo số phản hồi nhiều vẫn có thể thiên lệch vì nhóm quan tâm hoặc có kinh nghiệm thường trả lời nhiều hơn."),
        "B": ("聞き取りの結果でアンケートの数値をすべて置き換えるため", "Thành phố giữ số liệu khảo sát để nắm xu hướng rồi dùng phỏng vấn bổ sung bối cảnh; không bỏ toàn bộ số liệu."),
        "D": ("回答しなかった人を制度の対象から外すため", "Người không trả lời cũng được mời phỏng vấn ngắn. Họ không bị loại khỏi đối tượng của chính sách."),
    },
    "N2_11_M13_03": {
        "A": ("専門用語をすべて削除し、図だけで説明する", "Bài cảnh báo thay hết thuật ngữ có thể làm mất phân biệt chuyên môn; nhóm giữ thuật ngữ cần thiết và thêm giải thích."),
        "C": ("一人の来館者の反応を優先し、専門家の確認を省く", "Nhóm so sánh phản hồi của nhiều người và chuyên gia vẫn kiểm tra nội dung để giữ độ chính xác."),
        "D": ("読みやすさを優先し、根拠の確認を省く", "Mục tiêu là cân bằng dễ hiểu với chính xác; phản hồi độc giả giúp sửa cách trình bày chứ không thay thế kiểm chứng."),
    },
    "N2_12_M11_01": {
        "A": ("値下げ前後の販売数だけで事業の効果を決めるため", "Thành phố còn xem lượng bỏ đi và ý kiến người mua; họ không kết luận hiệu quả chỉ từ số bán."),
        "B": ("店ごとに異なる表示を残し、選び方を店員に任せるため", "Khách hàng khó chọn vì cách giảm giá khác nhau giữa cửa hàng. Thành phố thống nhất ba mức hiển thị thay vì giữ cách riêng."),
        "D": ("すべての商品を同じ価格で販売するため", "Thống nhất mức biểu thị giảm giá không có nghĩa bán mọi thực phẩm cùng giá; giá trị và tình trạng mỗi món vẫn khác nhau."),
    },
    "N2_12_M11_02": {
        "A": ("購入者が値引きの程度を比べる機会がなくなった", "Sau khi thống nhất cách hiển thị, người mua so sánh dễ hơn; cơ hội so sánh không biến mất."),
        "B": ("店ごとに割引率を独自に決めるようになった", "Đây là cách làm ban đầu. Sau thay đổi, mức giảm được trình bày theo ba cấp độ chung."),
        "C": ("売れ残りや廃棄がなくなった", "Chương trình đang đo xem lượng bỏ đi có giảm hay không; chưa có kết luận rằng thực phẩm dư hoặc rác đã biến mất."),
    },
    "N2_12_M11_03": {
        "A": ("参加店の売上順位で、協力の程度を決めるため", "Bài không xếp hạng cửa hàng; họ kiểm tra đồng thời lượng bán, lượng bỏ đi và ý kiến người mua."),
        "B": ("表示が分かりやすければ、廃棄量も必ず減ると示すため", "Đoạn cuối yêu cầu tách độ dễ hiểu của nhãn khỏi hiệu quả giảm lãng phí; nhãn rõ không bảo đảm lượng bỏ đi giảm."),
        "D": ("利用者全員の希望を一つの商品に反映するため", "Ý kiến người mua là một nguồn đánh giá, không phải yêu cầu làm một sản phẩm đáp ứng tất cả mọi người."),
    },
    "N2_12_M11_04": {
        "A": ("病院が町外へ移転し、旧路線を使えなくなったため", "Bệnh viện vẫn được nêu là điểm gần đó để lên xuống; lý do chuyển xe là xe buýt chạy tuyến cố định tốn chi phí cả ngày ít khách."),
        "C": ("運転手を増やし、全停留所を同時に回るため", "Mô hình mới đi qua các khu có đặt chỗ. Bài nêu thiếu nhân lực và chi phí là hạn chế của phương án tăng chuyến."),
        "D": ("すべての停留所をなくす方針になったため", "Chỉ một phần xe buýt được đổi sang xe đặt trước; không có thông báo xóa toàn bộ điểm dừng."),
    },
    "N2_12_M11_05": {
        "A": ("朝の遅れをなくすため、運転手を増やす", "Việc kéo dài giờ điện thoại xử lý phản hồi rằng cách đặt xe khó hiểu; tăng tài xế là phương án khác được cân nhắc cho giờ cao điểm."),
        "B": ("予約を不要にして、当日乗車へ切り替える", "Dịch vụ vẫn là xe ghép có đặt trước; bài không nói bỏ đặt chỗ."),
        "C": ("運行範囲を縮め、予約できる地区を減らす", "Thị trấn đăng hướng dẫn ở điểm dừng và kéo dài giờ nhận điện thoại để người dân hiểu cách đặt, không giảm khu vực phục vụ."),
    },
    "N2_12_M11_06": {
        "A": ("全ての地区を同じ時刻に運行すること", "Mục tiêu là giữ các khung giờ cần cho khám bệnh và đi học; không yêu cầu mọi khu có cùng giờ chạy."),
        "B": ("以前の路線を費用に関係なく完全に再現すること", "Thị trấn so sánh chi phí, nhân lực và nhu cầu; họ không định khôi phục toàn bộ tuyến cũ bất kể ngân sách."),
        "C": ("費用を最小にすることだけ", "Đoạn cuối nói rõ không chỉ lấy chi phí làm tiêu chí; thời gian cần thiết và ý kiến người dùng cũng được xem xét."),
    },
    "N2_12_M11_07": {
        "A": ("各館の書棚に同じ本をすべてそろえること", "Thư viện chỉ đặt thêm các sách được đặt nhiều ở nhiều chi nhánh; không mua toàn bộ danh mục giống nhau cho mọi nơi."),
        "B": ("予約取消しを防ぐため貸出期間を一律に延ばすこと", "Thay đổi tập trung vào vị trí sách và hệ thống kiểm tra tình trạng mượn; không sửa thời hạn mượn."),
        "C": ("配送をなくし、中央館での受け取りに戻すこと", "Việc chuyển sách giữa các thư viện vẫn là một phần dịch vụ. Hệ thống mới giúp giảm thời gian chờ nhận sách."),
    },
    "N2_12_M11_08": {
        "B": ("導入後、平均待ち日数が必ず長くなった", "Bài nói số ngày chờ trung bình đã ngắn hơn. Vấn đề còn lại là nhu cầu của một số sách tập trung ở vài chi nhánh."),
        "C": ("共通システムで各館の所蔵状況を確認できない", "Hệ thống chung được giới thiệu chính để xem tình trạng sách ở từng thư viện; trở ngại là quyết định số lượng mua thêm."),
        "D": ("利用者の希望を聞けず、配送費だけで決める", "Thư viện dự định lấy ý kiến người dùng và cân nhắc nhiều chỉ số, gồm nhu cầu và phí giao nhận."),
    },
    "N2_12_M11_09": {
        "A": ("本の大きさと棚の空きだけ", "Kích thước sách và chỗ trống trên kệ không cho biết sách nào bị hủy đặt, thời gian chờ hay chi nhánh người đọc muốn nhận."),
        "C": ("貸出件数だけ", "Câu hỏi nhấn mạnh dữ liệu ngoài lượt mượn; bài bổ sung hủy đặt, thời gian chờ, nơi nhận mong muốn và ý kiến người dùng."),
        "D": ("配送費だけ", "Phí giao nhận là một yếu tố vận hành nhưng không giải thích được nhu cầu ở từng chi nhánh hay lý do hủy đặt."),
    },
    "N2_12_M13_01": {
        "A": ("護岸工事の結果、避難範囲が広がり、住民から水位を保つよう求められた", "Kết quả khảo sát được nêu là dòng chảy hạ lưu nhanh hơn và bãi nông nơi cá đẻ trứng giảm. Yêu cầu về phạm vi sơ tán không xuất hiện trong đoạn này."),
        "B": ("市が住民の要望を受け、環境団体に工事中止の判断を任せた", "Thành phố không trao quyền quyết định cho một nhóm. Họ tự thử nghiệm quy mô nhỏ để cân nhắc ý kiến cư dân, nhóm môi trường và số liệu."),
        "C": ("草刈り費用が予想より下がり、植物を残す必要がなくなった", "Người dân lo chi phí cắt cỏ có thể tăng; không có kết quả cho thấy chi phí giảm hay cây cối không cần giữ."),
    },
    "N2_12_M13_02": {
        "B": ("本工事の効果を早く確認するため、試験結果を待たずに全区間へ広げる", "Thành phố muốn kiểm tra trước trong một đoạn nhỏ và dự định hai năm sau mới quyết định phạm vi công trình chính."),
        "C": ("草刈りの費用だけを比べ、生態系や安全性は試験対象にしない", "Thử nghiệm xem cả tần suất cắt cỏ và biến động mực nước; quyết định cuối cùng cân nhắc an toàn, chi phí và hệ sinh thái."),
        "D": ("市民の観察会を開かず、専門家の測定だけで案を決める", "Người dân tham gia quan sát hàng tháng và chia sẻ ghi chép. Thành phố đối chiếu ý kiến này với đo đạc chuyên môn."),
    },
    "N2_12_M13_03": {
        "A": ("住民の記録を設計に取り入れるが、安全性や維持費の評価とは切り離す", "Ghi chép của người dân được đưa vào thiết kế, nhưng đánh giá cuối cùng vẫn kết hợp an toàn, chi phí bảo trì và thay đổi hệ sinh thái."),
        "C": ("参加人数の多さを基準に、案の安全性を判断する", "Bài nói rõ số người tham gia đông không tự chứng minh phương án an toàn; đây chỉ là một nguồn quan sát."),
        "D": ("専門家の測定と住民の観察のうち、人数の多い側の意見を採用する", "Thành phố đặt quan sát cư dân cạnh kết quả đo của chuyên gia và giữ cả điều kiện, lợi ích lẫn rủi ro trong hồ sơ; không chọn theo số người."),
    },
    "N2_13_M10_03": {
        "A": ("誤りの位置だけを示し、正しい表現は担当部署に調べてもらう", "Mẫu báo lỗi yêu cầu cả vị trí sai lẫn cách diễn đạt đúng để bộ phận phụ trách có thể đối chiếu."),
        "C": ("正しい表現だけを書き、字幕の位置は示さない", "Chỉ có cách viết đúng sẽ không cho biết câu phụ đề nào cần kiểm tra; biểu mẫu yêu cầu cả vị trí."),
        "D": ("訂正予定日が表示されるまで報告を待つ", "Sinh viên có thể báo lỗi ngay. Ngày dự kiến chỉ được hiển thị nếu việc xác minh và sửa cần thêm thời gian."),
    },
    "N2_13_M11_01": {
        "A": ("再生回数と視聴時間", "Bài đọc nêu nguy cơ chạy theo lượt xem khiến phần trình diễn nổi bật hơn nội dung. Vì vậy số lượt xem và thời lượng xem không phải tiêu chí đánh giá được chọn."),
        "C": ("編集技術の新しさ", "Bài đọc không đánh giá video theo kỹ thuật dựng mới hay cũ. Tiêu chí được nêu là người mới theo được ý chính và lời giải thích có căn cứ."),
        "D": ("教員の説明をどれだけ短くできたか", "Video được dùng để hỗ trợ người mới đặt câu hỏi, không thay thế phần giảng của giáo viên. Độ ngắn của bài giảng không phải tiêu chí đánh giá video."),
    },
    "N2_13_M11_03": {
        "B": ("投稿が広く共有されているかどうかを、事実確認の代わりに示すこと", "Độ lan truyền không chứng minh tính đúng. Biên tập viên kiểm tra người đăng, thời gian, địa điểm, ảnh và nguồn độc lập."),
        "C": ("確認できなかった点を記事から外し、確定した内容だけに整理した経緯", "Bài yêu cầu giữ cả điểm chưa xác nhận và chênh lệch giữa tài liệu để độc giả tự đánh giá; không xóa chúng khỏi dấu vết bài viết."),
        "D": ("投稿の表現を編集部が要約し、発信者に代わって見解を示した内容", "Biên tập viên ghi nguồn và lịch sử đính chính, không viết lại lời người đăng thay họ."),
    },
    "N2_13_M11_07": {
        "A": ("提出後に窓口が全ての申請を修正する", "Nhiều thủ tục không sửa được sau khi gửi. Vì vậy giao diện nhắc kiểm tra trước và ngay trước lúc nộp."),
        "B": ("添付ファイルの種類を一つに限定する", "Đại học không giới hạn loại tệp; họ hiện rõ nơi nộp và tên tệp để người dùng kiểm tra đúng hồ sơ."),
        "C": ("送信のたびに同じ警告を何度も表示する", "Bài nói lặp cảnh báo khiến người dùng đọc lướt; xác nhận chỉ xuất hiện ở các bước cần kiểm tra."),
    },
    "N2_13_M11_08": {
        "B": ("コメントの長さや資料の数をそろえ、形式面の統一を評価する", "Yêu cầu mới tập trung vào đoạn được nhận xét, lý do và căn cứ kiểm chứng, không đặt độ dài hoặc số tài liệu làm thước đo."),
        "C": ("指摘を受けた学生が、理由を問わず修正を採用したかを見る", "Người nhận không buộc phải làm theo góp ý; giáo viên đánh giá việc đọc lại và cân nhắc có căn cứ."),
        "D": ("教員が論文を先に修正し、学生同士のコメントを省く", "Hoạt động sinh viên nhận xét lẫn nhau vẫn được duy trì. Giáo viên xem quá trình đọc lại chứ không thay thế các bình luận."),
    },
    "N2_13_M11_09": {
        "A": ("履歴が残る心配がある人には、相談窓口を案内しない", "Trường tiếp tục lựa chọn gặp trực tiếp và điện thoại cho người lo lịch sử trên thiết bị dùng chung; họ không từ chối người cần riêng tư."),
        "B": ("オンラインの利用が増えたら、電話と対面を縮小する", "Số lượt trực tuyến tăng không làm trường bỏ các kênh khác; bài nói rõ họ duy trì điện thoại và đặt lịch gặp trực tiếp."),
        "C": ("相談方法ごとの利用件数だけで配置を決め、匿名の意見は使わない", "Lượt dùng chỉ là một nguồn. Trường còn hỏi ẩn danh về điểm hữu ích, khó dùng và lý do bỏ dở để tránh suy ra hiệu quả từ số lượng."),
    },
    "N2_13_M13_03": {
        "A": ("方法と限界を中心の文章にすべて集め、追加資料のページは設けない", "Nhóm giữ ý chính và phạm vi trong phần trung tâm, còn phương pháp chi tiết được đưa sang trang bổ sung có liên kết."),
        "B": ("専門用語を言い換えれば、対象や条件の制約は説明しなくてよい", "Đoạn yêu cầu nêu đối tượng, điều kiện và phần chưa chắc chắn; chỉ đổi thuật ngữ không đủ để giữ đúng phạm vi nghiên cứu."),
        "D": ("専門家以外の読み手には見せず、正確性を研究者だけで確認する", "Sinh viên ngoài chuyên môn đọc bản thảo để phát hiện chỗ khó hiểu, trong khi nhà nghiên cứu vẫn kiểm tra tính chính xác."),
    },
}


def validate_distractor_rationales(items, question_revisions):
    """Return option-binding, coverage, and duplication errors for this set."""
    by_id = {item.get("id"): item for item in items}
    errors = []
    expected_ids = set(question_revisions)
    missing_rationales = expected_ids - set(DISTRACTOR_RATIONALES)
    if missing_rationales:
        errors.append(
            "rationale coverage missing revision IDs: "
            f"{sorted(missing_rationales)}"
        )

    rationale_texts = []
    for qid in sorted(expected_ids):
        item = by_id.get(qid)
        records = DISTRACTOR_RATIONALES.get(qid)
        if item is None:
            errors.append(f"{qid}: candidate item missing")
            continue
        if not isinstance(records, dict):
            errors.append(f"{qid}: rationale mapping missing")
            continue
        options = {o.get("id"): o.get("text") for o in item.get("options", [])}
        expected_wrong_ids = set(options) - {item.get("correctAnswer")}
        if len(options) != 4 or item.get("correctAnswer") not in options:
            errors.append(f"{qid}: option/key structure invalid")
        if set(records) != expected_wrong_ids:
            errors.append(
                f"{qid}: distractor rationale IDs mismatch; "
                f"expected={sorted(expected_wrong_ids)}, actual={sorted(records)}"
            )
        candidate_feedback = item.get("distractorExplanations")
        expected_feedback = {
            option_id: record[1]
            for option_id, record in records.items()
            if isinstance(record, tuple) and len(record) == 2
        }
        if candidate_feedback != expected_feedback:
            errors.append(f"{qid}: candidate feedback is missing, stale, or bound to the wrong option")
        if isinstance(candidate_feedback, dict):
            for option_id, feedback in candidate_feedback.items():
                if not isinstance(feedback, str):
                    errors.append(f"{qid}/{option_id}: candidate feedback must be text")
                    continue
                if feedback.strip() == (item.get("explanationVi") or "").strip():
                    errors.append(f"{qid}/{option_id}: candidate feedback only repeats the answer explanation")
                if "không phù hợp với bài đọc" in feedback.lower() or "không supported by the passage" in feedback.lower():
                    errors.append(f"{qid}/{option_id}: generic candidate feedback detected")
        revision_options = question_revisions.get(qid, {}).get("optionsById", {})
        for option_id, record in records.items():
            if option_id == item.get("correctAnswer"):
                errors.append(f"{qid}/{option_id}: correct option has distractor rationale")
            if option_id not in options or not isinstance(record, tuple) or len(record) != 2:
                errors.append(f"{qid}/{option_id}: malformed or unbound rationale record")
                continue
            expected_text, rationale = record
            if expected_text != options[option_id]:
                errors.append(f"{qid}/{option_id}: rationale is stale for current option text")
            if revision_options.get(option_id, expected_text) != expected_text:
                errors.append(f"{qid}/{option_id}: rationale binding differs from explicit revision text")
            if not isinstance(rationale, str) or len(rationale.strip()) < 25:
                errors.append(f"{qid}/{option_id}: rationale missing or too short")
                continue
            if rationale.strip() == (item.get("explanationVi") or "").strip():
                errors.append(f"{qid}/{option_id}: distractor rationale only repeats the answer explanation")
            if "không phù hợp với bài đọc" in rationale.lower() or "không supported by the passage" in rationale.lower():
                errors.append(f"{qid}/{option_id}: generic distractor boilerplate detected")
            rationale_texts.append((qid, option_id, rationale.strip()))

    normalized = [text for _, _, text in rationale_texts]
    if len(set(normalized)) != len(normalized):
        errors.append("duplicate distractor-rationale text detected across revised Reading set")
    return errors
