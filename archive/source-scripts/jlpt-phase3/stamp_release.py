from pathlib import Path
import json,hashlib,copy
R=Path(__file__).resolve().parents[2];O=R/'FINAL_PHASE3';P=O/'JLPT_PRACTICE';T=R/'tmp/jlpt-phase3'
def projection(bank):
 b=copy.deepcopy(bank);b.pop('status',None);b.pop('validationNote',None)
 for q in b['questions']+b['roleplays']:q.pop('validation',None)
 return hashlib.sha256(json.dumps(b,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
bp=P/'question_bank.json';b=json.loads(bp.read_text(encoding='utf-8'));before=projection(b);rawbefore=hashlib.sha256(bp.read_bytes()).hexdigest()
b['status']='reviewed-pilot-release';b['validationNote']='Independent AI content QA: blind 80/80 then full keys/distractors; repairs and targeted reaudits passed 15/10/2026, 4 roles and 80 mappings checked. No native-human calibration or acoustic TTS audit. Expansion deferred.'
for q in b['questions']+b['roleplays']:q['validation']['independentReaudit']=True;q['validation']['finalReviewDate']='2026-10-15'
bp.write_text(json.dumps(b,ensure_ascii=False,indent=2),encoding='utf-8');(P/'bank.js').write_text('window.PracticeBank='+json.dumps(b,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8');assert before==projection(b)
kp=O/'ANSWER_KEY_AND_EXPLANATIONS/validated_keys.json';k=json.loads(kp.read_text(encoding='utf-8'));k['validationNote']=b['validationNote'];kp.write_text(json.dumps(k,ensure_ascii=False,indent=2),encoding='utf-8')
lp=O/'JAPANESE_PATTERN_LIBRARY/patterns.json';lib=json.loads(lp.read_text(encoding='utf-8'));beforelib=copy.deepcopy(lib)
for p in lib['patterns']:p['reviewStatus']='AI soạn gốc; đã qua rà nội dung độc lập và sửa theo nguồn 15/10/2026; chưa thẩm định bản ngữ/hiệu chuẩn người học.'
lib['reviewLimit']='31 cards and 37 instructional examples independently AI-reviewed; separate from 80 objective bank items. No human-native or acoustic calibration.'
lp.write_text(json.dumps(lib,ensure_ascii=False,indent=2),encoding='utf-8');(P/'patterns.js').write_text('window.PatternLibrary='+json.dumps(lib,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
for old,new in zip(beforelib['patterns'],lib['patterns']):
 old.pop('reviewStatus');new=copy.deepcopy(new);new.pop('reviewStatus');assert old==new
(T/'release_stamp.json').write_text(json.dumps({'reviewedBankShaBeforeMetadataStamp':rawbefore,'linguisticProjectionUnchanged':True,'linguisticProjectionSha':before,'patternTeachingFieldsUnchanged':True,'note':'Only validation/reviewStatus annotations changed after independent final content approval.'},indent=2),encoding='utf-8')
p=T/'build_pdfs.py';s=p.read_text(encoding='utf-8').replace('Lượt kiểm lại độc lập chưa hoàn tất vì giới hạn sử dụng. Phụ lục 31 thẻ chỉ tác giả rà nguồn, chưa được QA ngôn ngữ độc lập.','Lượt kiểm sau sửa đã đạt; 31 thẻ và 37 câu học cũng đã được rà độc lập. Chưa có thẩm định bản ngữ, hiệu chuẩn người học hay kiểm âm TTS.');p.write_text(s,encoding='utf-8')
p=O/'JAPANESE_PATTERN_LIBRARY/README.md';s=p.read_text(encoding='utf-8').replace('QA: tác giả rà 31 thẻ và đáp án; chưa có lượt QA ngôn ngữ độc lập cho phụ lục.','QA: tác giả soạn, tác tử khác rà độc lập 31 thẻ và 37 khóa; đã sửa và kiểm lại các thay đổi. Chưa có thẩm định bản ngữ hay thử người học.');p.write_text(s,encoding='utf-8')
p=O/'RESEARCH_EVIDENCE_LEDGER.md';s=p.read_text(encoding='utf-8').replace('thêm 3 truy vấn đích TUFS/JF (10+5+5 kết quả)','thêm 4 truy vấn đích TUFS/JF (10+5+5+5 kết quả)').replace('không phải 190 nghiên cứu đã đọc','không phải 195 nghiên cứu đã đọc')
idx=s.index('## Hạn chế kiểm định nội dung');s=s[:idx]+'''## Kiểm định nội dung và giới hạn

80 MCQ +4 vai được một tác tử AI khác giải mù/đọc đầy đủ lượt đầu. Tác giả sửa F01–F16, rồi tác tử kiểm các ID thay đổi, 80 mapping và toàn bộ thư viện qua các lượt. Kết luận cuối PASS; 31 thẻ và37 câu học cũng được rà (không gọi các câu thư viện là giải mù). 58 câu không thay ngôn ngữ không được giải mù lại lần hai; xáo nhãn lựa chọn được kiểm bằng80 mapping nội dung và bộ chấm. Metadata xác nhận QA được đóng sau phê duyệt, không thay trường dạy học/khóa.

Nguồn bổ sung G09: [TUFS cho phép](https://www.coelang.tufs.ac.jp/mt/ja/gmod/contents/explanation/058.html), [TUFS cấm](https://www.coelang.tufs.ac.jp/mt/ja/gmod/contents/explanation/059.html), [JF文-53](https://www.jpf.go.jp/j/urawa/j_rsorcs/textbook/setsumei_pdf/setsumei14_2.pdf), [JF Bangkok Akiko5](https://ba.jpf.go.jp/wp-content/uploads/2022/03/Akiko5_bunpoo382002.pdf), đã đọc trực tiếp 15/10/2026; không đoán ngày xuất bản từ đường dẫn. Một thẻ bổ sung giúp chữa đúng mục tiêu phép/cấm/nghĩa vụ, tổng31 gần mức khoảng20–30 ban đầu. Không mở rộng ngân hàng câu chỉ để tăng số lượng.

Đây chưa phải thẩm định bản ngữ, thử nghiệm người học hay hiệu chuẩn độ khó. Kịch bản/khóa nghe đã kiểm qua chữ; âm TTS chưa kiểm thực. Dừng ở thí điểm80, chưa có300–500/N3/N2. Xem QA_REPORT.md cho kiểm thử ứng dụng và sổ Excel.
''';p.write_text(s,encoding='utf-8')
template=(T/'index_template.html').read_text(encoding='utf-8').replace('<link rel="stylesheet" href="styles.css">','<style>'+(P/'styles.css').read_text(encoding='utf-8')+'</style>')
for name in ['bank.js','patterns.js','engine.js','app.js']:template=template.replace('<script src="'+name+'"></script>','<script>'+(P/name).read_text(encoding='utf-8').replace('</script','<\\/script')+'</script>')
(P/'index.html').write_text(template,encoding='utf-8')
print('Stamped independent QA; language fields and keys unchanged')
