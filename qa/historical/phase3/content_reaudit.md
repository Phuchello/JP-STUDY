# Kiểm lại nội dung sau sửa — 15/10/2026

Nguồn kiểm: `FINAL_PHASE3/JLPT_PRACTICE/question_bank.json` và `FINAL_PHASE3/JAPANESE_PATTERN_LIBRARY/patterns.json`.

**Kết luận snapshot này:** các lỗi block/major cũ trong nội dung câu hỏi và bốn vai đã được sửa. **Chưa pass toàn gói** vì còn một lỗi minor của F03 và lỗi major mới ở liên kết ôn (RA02). Tác giả đã thông báo sẽ sửa mapping theo từng ID và bổ sung G09; G09 chưa nằm trong 30 thẻ đã kiểm ở snapshot này.

Đã kiểm lại bằng suy luận ngôn ngữ **21 ID từng có phát hiện + N4-PART-005 =22 câu**, đủ lựa chọn sau xáo, khóa, giải thích, từng nhiễu, passage/audio.script, evidence, prerequisite và nguồn liên quan. **22/22 khóa** khớp nội dung giải lại. Không so chữ cái cũ với khóa mới. Đã đọc các trường commonMistakes, typicalMisunderstanding và liên kết ôn phụ thuộc. Đã kiểm **4/4 vai**, nay có lượt người đối thoại và dữ kiện để xác nhận.

Đã rà nội dung **30/30 thẻ**:8 grammar,6 listen,4 read,12 templates. Đã giải lại đủ **34/34 câu chỉ để học**, đối chiếu lựa chọn và lời giải; khóa đều hợp lệ và không thấy khóa đôi. Các câu này không cộng vào ngân hàng80. Đã đọc mapping của **80/80 ID**, nhưng không tuyên bố giải mù hoặc rà lại toàn bộ80 câu Nhật lần hai sau xáo; rà ngôn ngữ đầy đủ80 đã thực hiện ở lượt đầu.

Đã xác nhận đích [JF まで・までに](https://www.jpf.go.jp/j/project/japanese/teach/tsushin/grammar/200911.html) hỗ trợ hạn nộp. [Grammar_all.pdf trang209](https://www.irodori.jpf.go.jp/assets/data/Grammar_all.pdf#page=209) đúng mục なくてもいい/だいじょうぶ, 初中級L8-23. Chương nguồn không phải chứng nhận mức JLPT của câu.

| Phát hiện cũ | Kết quả | Ghi chú |
|---|---|---|
| F01 | PASS | N4-MED-003 |
| F02 | PASS | N4-SHORT-003 |
| F03 | CHƯA HẾT — minor | N4-SHORT-007 |
| F04 | PASS | N4-SHORT-001 |
| F05 | PASS | N4-MED-004 |
| F06 | PASS | N4-MED-006 |
| F07 | PASS | N4-LISTEN-008 |
| F08 | PASS | N4-INTERP-001, N4-INTERP-002, N4-INTERP-003, N4-INTERP-005 |
| F09 | PASS | N4-ORDER-001, N4-ORDER-002, N4-ORDER-003, N4-ORDER-004 |
| F10 | PASS | N4-GRAM-011 |
| F11 | PASS | N4-INTERP-006 |
| F12 | PASS | N4-GRAM-006, N4-GRAM-007, N4-SHORT-005, N4-MED-002, N4-MED-006 |
| F13 | PASS | N4-SPK-001 |
| F14 | PASS | N4-SPK-002 |
| F15 | PASS | N4-SPK-003 |
| F16 | PASS | N4-SPK-004 |

F01 nay hàng tới thứ Hai nên nhận sớm thứ Ba không mâu thuẫn. F02 đã đổi thành 変更しました, có lịch chốt. F08/F09/F10 đã trỏ đích thích hợp. F12 đã bổ sung nghĩa từ hỗ trợ ở prerequisite. F13–F16 có dữ kiện đối thoại, đủ để học viên tự xác nhận. Chưa kiểm giao diện có che thẻ người đối thoại trước khi học viên trả lời hay không.

**RA01 — minor — N4-SHORT-007**

Đã sửa đáp án và explanationVi; distractorExplanations C và commonMistakes vẫn khẳng định 'bỏ quên ví'.

Sửa cụ thể: Sửa thành 'Đoạn nói có thể để ví ở ga nên quay lại tìm, không phải muốn mua vé.' và đồng bộ commonMistakes.

**RA02 — major — liên kết từng ID ở bảng dưới**

Nhiều liên kết ôn gán theo concept rộng nên đưa người học sang thẻ không dạy mục tiêu của câu. Khóa câu hỏi vẫn đúng.

Sửa cụ thể: Đổi từng ID theo mappingRecommendations; khi chưa có thẻ đúng, để null thay vì gán ép. G09 chờ tác giả bổ sung và QA riêng.

**RA03 — minor — T03, T04, T05, T08, T10, T11**

Các ví dụ Nhật đang đúng nhưng loại từ trong ô thay chưa rõ; việc điền lý do/mốc giờ theo đúng khung có thể tạo câu sai.

Sửa cụ thể: T03: V thường+ため/Nのため; T04: Nのため hoặc V thường+ため; T05: Nで/Vて・ので (ví dụ hiện dùng 遅れていて); T08: tách 時刻に/場所で; T10: V・イA thườngと思う, N・ナAだと思う; T11: N・ナAだからです.

**RA04 — minor — G07**

Công thức 普通形なら thiếu ngoại lệ danh từ/ナ形容詞, dễ sinh 学生だなら.

Sửa cụ thể: Ghi V/イA普通形なら; N/ナAなら (学生なら、静かなら; bỏ だ phi quá khứ khẳng định).

**RA05 — minor — G04**

Lời giải practice thứ ba nói 'hạn hoàn tất cuộc gọi' có thể bị hiểu phải kết thúc cuộc nói chuyện trước 5 giờ. 電話してください thường yêu cầu thực hiện cuộc gọi/liên lạc trước hạn.

Sửa cụ thể: Đổi thành '5 giờ là hạn thực hiện việc gọi/liên lạc; không phải thời gian phải gọi liên tục.'

**RA06 — minor — R03**

dialogueVi dùng 'Ngày thường10 giờ' cho 毎日10時; dễ lẫn với 平日 và không bao gồm thứ Bảy/Chủ nhật.

Sửa cụ thể: Đổi thành 'Thông thường mở lúc10 giờ; riêng thứ Hai từ12 giờ.'

**RA07 — minor — T11**

commonMistake/typicalMisunderstanding trình bày không kết からです sau なぜなら như lỗi tuyệt đối, dù đây là cặp được chọn trong bài tập.

Sửa cụ thể: Giới hạn: 'Trong mẫu bài tập này, dùng cặp なぜなら…からです và nói đủ lý do'; không dạy rằng mọi cách kết khác đều sai.

**RA08 — minor — G06**

Đang dạy cặp 開く（あく）/開ける nhưng không ghi cách đọc khi nêu ghép 開いてある là lỗi; phạm vi có thể bị hiểu thành cấm mọi chuỗi chữ 開いてある.

Sửa cụ thể: Ghi rõ 'Trong cặp 開く（あく）/開ける đang học: あいている vs あけてある' trong commonMistake/typicalMisunderstanding, giữ ví dụ cửa hiện tại.

**Mapping đề nghị để tác giả sửa**

Các dòng major là liên kết lệch hẳn mục tiêu; các dòng minor giúp ôn đúng trọng tâm hơn. `null` là chưa có thẻ phù hợp, không cần tạo thêm thẻ chỉ để điền chỗ trống. G09 là thẻ tác giả đang chuẩn bị, phải QA riêng trước khi chấp thuận.

| ID | patternId đề nghị | relatedTemplate đề nghị | Mức | Lý do |
|---|---|---|---|---|
| N4-PART-007 | null | null | minor | G04 dạy まで/までに, chưa dạy mốc に. |
| N4-PART-008 | null | null | minor | G02 không dạy đối tượng を. |
| N4-PART-009 | null | null | minor | G02 không dạy người cùng làm と. |
| N4-PART-010 | null | null | minor | G02 không dạy xuất phát から. |
| N4-GRAM-001 | G09 | null | major | T07/T08 không phải thẻ đối chiếu phép/cấm/nghĩa vụ/miễn nghĩa vụ; G09 đang được tác giả bổ sung. |
| N4-GRAM-002 | G09 | null | major | T07/T08 không phải thẻ đối chiếu phép/cấm/nghĩa vụ/miễn nghĩa vụ; G09 đang được tác giả bổ sung. |
| N4-GRAM-003 | G09 | null | major | T07/T08 không phải thẻ đối chiếu phép/cấm/nghĩa vụ/miễn nghĩa vụ; G09 đang được tác giả bổ sung. |
| N4-GRAM-004 | G09 | null | major | T07/T08 không phải thẻ đối chiếu phép/cấm/nghĩa vụ/miễn nghĩa vụ; G09 đang được tác giả bổ sung. |
| N4-GRAM-005 | G09 | null | major | T07/T08 không phải thẻ đối chiếu phép/cấm/nghĩa vụ/miễn nghĩa vụ; G09 đang được tác giả bổ sung. |
| N4-GRAM-006 | G09 | null | major | T07/T08 không phải thẻ đối chiếu phép/cấm/nghĩa vụ/miễn nghĩa vụ; G09 đang được tác giả bổ sung. |
| N4-GRAM-007 | G09 | null | major | T07/T08 không phải thẻ đối chiếu phép/cấm/nghĩa vụ/miễn nghĩa vụ; G09 đang được tác giả bổ sung. |
| N4-GRAM-008 | G09 | null | major | T07/T08 không phải thẻ đối chiếu phép/cấm/nghĩa vụ/miễn nghĩa vụ; G09 đang được tác giả bổ sung. |
| N4-ORDER-005 | G08 | null | major | Mẫu kinh nghiệm たことがない, không phải trước/sau. |
| N4-ORDER-007 | null | null | minor | Lời khuyên たほうがいい chưa có thẻ đúng; G05 trước/sau không dạy mẫu này. |
| N4-ORDER-008 | G09 | null | minor | Trật tự của mẫu bắt buộc, không phải trật tự sự việc trước/sau. |
| N4-INTERP-002 | null | null | minor | R03 là tìm điều kiện/ngoại lệ theo tình huống, chưa dạy しか. |
| N4-INTERP-003 | G09 | null | minor | Đích chính là なくてもいい. |
| N4-INTERP-005 | G05 | null | major | Đích là Vる前に; G07 là các mẫu điều kiện. |
| N4-SHORT-002 | R03 | null | minor | Tra giờ theo ngoại lệ thứ Bảy. |
| N4-SHORT-004 | G04 | null | minor | Hạn trả までに. |
| N4-SHORT-006 | L02 | null | minor | Việc phải làm khi sắp trễ, không hỏi lý do. |
| N4-SHORT-008 | G09 | null | minor | Không cần mua sữa. |
| N4-MED-002 | R03 | null | minor | Nhánh nếu mưa và nơi đi thẳng. |
| N4-MED-003 | R03 | null | minor | Điều kiện nhận hàng sớm và hạn liên lạc. |
| N4-MED-006 | R01 | null | minor | Ý chính của thông báo. |
| N4-LISTEN-001 | L01 | T06 | minor | Xác nhận lịch, không xin đổi ca. |
| N4-LISTEN-002 | L01 | T06 | minor | Xác nhận địa điểm đã đổi. |
| N4-LISTEN-003 | L02 | T06 | minor | Chỉ dẫn đến trước hạn, không có đổi giờ. |
| N4-LISTEN-004 | L01 | T06 | minor | Xác nhận lịch giao đã đổi. |
| N4-LISTEN-005 | L02 | T07 | minor | Làm rõ chỉ dẫn cửa sổ/điện. |
| N4-LISTEN-006 | L02 | T07 | minor | Chỉ dẫn có điều kiện. |
| N4-LISTEN-007 | L02 | T07 | minor | Chỉ dẫn sao giấy trùng T07. |
| N4-LISTEN-008 | L02 | T05 | major | Báo trễ, không xin đổi ca. |
| N4-COMM-002 | T01 | T01 | major | Xin nhắc lại lời giáo viên, không xin đổi ca. |
| N4-COMM-003 | null | null | minor | Chưa có thẻ hỏi tuyến tàu đúng mục tiêu. |
| N4-COMM-004 | G09 | null | minor | Xin phép trả sách, không đổi ca. |

Những mapping không có trong bảng giữ được trong phạm vi kiểm này. Không yêu cầu mapping phải cùng kỹ năng nếu nội dung ôn phù hợp; ví dụ đọc thông báo đổi giờ có thể liên hệ L01. Vấn đề là gán mẫu khác ý cần học, như xin nhắc lại lại dẫn sang xin đổi ca.

**Khóa và sổ kiểm22 câu sau xáo**

| ID | Chọn lại | Khóa | Nội dung đáp án |
|---|---|---|---|
| N4-GRAM-006 | D | D | 見せなければなりません |
| N4-GRAM-007 | A | A | 原本を出さなくてもいいです。 |
| N4-GRAM-011 | A | A | しておきます |
| N4-ORDER-001 | B | B | 先週買ったくつです。 |
| N4-ORDER-002 | C | C | 駅で会った人です。 |
| N4-ORDER-003 | A | A | 友だちが作ったお菓子です。 |
| N4-ORDER-004 | C | C | 日本語を教えている先生を知っています。 |
| N4-INTERP-001 | A | A | 日曜日は休みです。 |
| N4-INTERP-002 | D | D | 財布にあるお金は千円だけです。 |
| N4-INTERP-003 | B | B | 今日は全部する必要はありません。 |
| N4-INTERP-005 | A | A | 先生にメールを送ります。 |
| N4-INTERP-006 | C | C | このボタンを押します。 |
| N4-SHORT-001 | C | C | 午前10時からです。 |
| N4-SHORT-003 | A | A | 金曜日の午後2時です。 |
| N4-SHORT-005 | A | A | 雨が降っているからです。 |
| N4-SHORT-007 | D | D | 駅に財布を置いたかもしれないからです。 |
| N4-MED-002 | D | D | 市民センターの入口です。 |
| N4-MED-003 | B | B | 月曜日の午後6時までに連絡します。 |
| N4-MED-004 | D | D | 昼休みにゆっくり食べたいからです。 |
| N4-MED-006 | B | B | 入口の近くに自転車を置かないでほしいということです。 |
| N4-LISTEN-008 | C | C | 店に電話します。 |
| N4-PART-005 | A | A | までに |

**Giới hạn**

- QA do mô hình thực hiện, không phải giáo viên bản ngữ; chưa có thử nghiệm người học thực hoặc hiệu chuẩn khó/thời gian.
- Tám câu nghe ở lượt đầu và câu nghe được kiểm lại ở lượt này chỉ rà kịch bản chữ/khóa; chưa nghe hay xác nhận phát âm/tốc độ/ngữ điệu TTS.
- Nhiều nguồn J04 vẫn ở cấp khóa; không khẳng định mọi câu đã có nguồn đúng trang. Đích mới までに và なくてもいい đã được mở kiểm.
- 34 câu phụ lục không phải câu ngân hàng được giải mù ở lượt đầu. Đã đọc khóa khi kiểm phụ lục, nên không gọi đây là một lượt giải mù.
- Không sửa ngân hàng hoặc nguồn trong nhiệm vụ QA. Bản máy đọc: [content_reaudit_findings.json](./content_reaudit_findings.json).

Chờ tác giả gửi bản sửa G09/mapping và các góp ý trên; kiểm lại phần thay đổi trước khi cập nhật kết luận cuối.

