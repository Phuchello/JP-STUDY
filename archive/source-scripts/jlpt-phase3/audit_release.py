from pathlib import Path
from collections import Counter
from lxml import etree as E
import json,hashlib,zipfile,copy,re,shutil
R=Path(__file__).resolve().parents[2];O=R/'FINAL_PHASE3';P=O/'JLPT_PRACTICE';T=R/'tmp/jlpt-phase3';checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(name,value):checks.append({'name':name,'ok':bool(value)});assert value,name
original=json.loads((T/'source_hashes.json').read_text(encoding='utf-8'));ck('All13 Phase1/2/2.1 sources unchanged',len(original)==13 and all(sha(R/n)==h for n,h in original.items()))
b=json.loads((P/'question_bank.json').read_text(encoding='utf-8'));lib=json.loads((O/'JAPANESE_PATTERN_LIBRARY/patterns.json').read_text(encoding='utf-8'));keys=json.loads((O/'ANSWER_KEY_AND_EXPLANATIONS/validated_keys.json').read_text(encoding='utf-8'));schema=json.loads((P/'question.schema.json').read_text(encoding='utf-8'));pids={p['id'] for p in lib['patterns']}
ck('80+4 pilot count',len(b['questions'])==80 and len(b['roleplays'])==4);ck('31+37 instructional count',len(pids)==31 and sum(len(p.get('practice',[])) for p in lib['patterns'])==37);ck('30 reusable recipes',len(b['recipes'])==30)
ck('Required metadata + estimated difficulty + evidence',all(all(k in q for k in schema['required']) and isinstance(q['difficultyEstimate'],int) and 1<=q['difficultyEstimate']<=5 and (not(q.get('passage') or q.get('audio')) or q.get('evidence')) for q in b['questions']))
ck('Pattern and template references valid or null',all((not q['patternId'] or q['patternId'] in pids) and (not q['relatedTemplate'] or q['relatedTemplate'] in pids) for q in b['questions']))
ck('Key digest matches recomputation',b['answerKeyDigest']==hashlib.sha256(json.dumps([(q['id'],q['correctAnswer']) for q in b['questions']],ensure_ascii=False,separators=(',',':')).encode()).hexdigest()==keys['answerKeyDigest'])
ck('Key view equals all bank keys and rationales',all(k['correctAnswer']==q['correctAnswer'] and k['distractorExplanations']==q['distractorExplanations'] for k,q in zip(keys['questions'],b['questions'])))
for name,prefix,obj in [('bank','window.PracticeBank=',b),('patterns','window.PatternLibrary=',lib)]:ck(name+' JS resource identical to JSON',json.loads((P/(name+'.js')).read_text(encoding='utf-8')[len(prefix):-2])==obj)
entry=(P/'index.html').read_text(encoding='utf-8');ck('Entry includes exact current scripts and CSS',all((P/n).read_text(encoding='utf-8').replace('</script','<\\/script') in entry for n in ['bank.js','patterns.js','engine.js','app.js']) and '<script src=' not in entry and '<link rel="stylesheet"' not in entry)
ck('All library practice keys in range',all(0<=q['correctIndex']<len(q['options']) for p in lib['patterns'] for q in p.get('practice',[])))
ck('All objective questions marked reviewed',all(q['validation'].get('independentReaudit') for q in b['questions']+b['roleplays']))
review=json.loads((T/'content_final_reaudit.json').read_text(encoding='utf-8'));stamp=json.loads((T/'release_stamp.json').read_text(encoding='utf-8'));ck('Independent final content PASS',review['decision']=='PASS_FOR_LIMITED_PILOT');ck('Independent final bank fingerprint matches release',sha(P/'question_bank.json')==review['verifiedFiles'][0]['Hash'].lower())
pr=copy.deepcopy(b);pr.pop('status');pr.pop('validationNote')
for q in pr['questions']+pr['roleplays']:q.pop('validation')
ck('Teaching projection unchanged after independent approval',hashlib.sha256(json.dumps(pr,ensure_ascii=False,sort_keys=True).encode()).hexdigest()==stamp['linguisticProjectionSha'])
ck('Independent final library fingerprint matches release',sha(O/'JAPANESE_PATTERN_LIBRARY/patterns.json')==review['verifiedFiles'][1]['Hash'].lower())
ck('80 option text/key/distractor remaps preserved',all(x['sameCorrectText'] and x['distractorsMapped'] for x in json.loads((T/'option_mapping_tests.json').read_text())))
engine=json.loads((T/'engine_tests.json').read_text());browser=json.loads((T/'browser_tests.json').read_text());edge=json.loads((T/'edge_flow_tests.json').read_text());native=json.loads((T/'excel_native_tests.json').read_text(encoding='utf-8'));author=json.loads((T/'tracker_tests.json').read_text());pdf=json.loads((T/'pdf_qa.json').read_text())
ck('Engine final test run passes',all(x['ok'] for x in engine));ck('Browser final test run passes',all(x['ok'] for x in browser['tests']) and not browser['errors']);ck('Edge flow final test run passes',all(x['ok'] for x in edge['tests']));ck('Excel native checks pass',native['status']=='passed' and all(x['passed'] for x in native['tests']));ck('Spreadsheet author checks pass',all(x['ok'] for x in author))
ck('PDF page limits 3/5/5/6', {p['file']:p['pages'] for p in pdf}=={'START_HERE.pdf':3,'LEARNING_METHODS.pdf':5,'LISTENING_READING_CHEATSHEETS.pdf':5,'JAPANESE_WRITING_SPEAKING_TEMPLATES.pdf':6});ck('PDF text margins and glyph extraction clean',all(not p['outOfMargins'] and not p['replacementGlyph'] for f in pdf for p in f['checks']))
S='http://schemas.openxmlformats.org/spreadsheetml/2006/main';ns={'s':S}
with zipfile.ZipFile(R/'FINAL_V3/JLPT_PROGRESS_TRACKER_FINAL.xlsx') as z:old={n:z.read(n) for n in z.namelist()}
with zipfile.ZipFile(O/'JLPT_PROGRESS_TRACKER.xlsx') as z:new={n:z.read(n) for n in z.namelist()}
parts=[n for n in old if n.startswith('xl/worksheets/')];ck('Original five worksheet XML/relationship parts exact',all(new[n]==old[n] for n in parts));nativefeatures={'hyperlinks':0,'validations':0,'formulasOld':0,'formulasNew':0}
for n in new:
 if n.startswith('xl/worksheets/') and n.endswith('.xml'):
  sh=E.fromstring(new[n]);nativefeatures['hyperlinks']+=len(sh.findall('s:hyperlinks/s:hyperlink',ns));nativefeatures['validations']+=len(sh.findall('s:dataValidations/s:dataValidation',ns));nativefeatures['formulasNew']+=len(sh.findall('.//s:f',ns))
for n in old:
 if n.startswith('xl/worksheets/') and n.endswith('.xml'):nativefeatures['formulasOld']+=len(E.fromstring(old[n]).findall('.//s:f',ns))
sh=E.fromstring(new['xl/worksheets/phase3_practice.xml']);ck('No learner data in import area',not any(c.get('r').startswith(tuple('ABCDEFGHIJKL')) and 8<=int(re.sub(r'\D','',c.get('r')))<=507 and (c.find('s:v',ns) is not None or c.find('s:is',ns) is not None) for c in sh.findall('.//s:c',ns)))
ck('Native links and validation retained',nativefeatures['hyperlinks']==123 and nativefeatures['validations']==142)
for f in ['content_final_reaudit.md','content_final_reaudit.json']:shutil.copyfile(T/f,O/'ANSWER_KEY_AND_EXPLANATIONS'/f)
(T/'release_checks.json').write_text(json.dumps({'checks':checks,'nativeFeatures':nativefeatures,'coverage':b['coverage'],'keys':dict(Counter(q['correctAnswer'] for q in b['questions']))},ensure_ascii=False,indent=2),encoding='utf-8')
report=f'''# QA — phát hành thí điểm Phase 3 + phụ lục

Ngày kiểm: 15/10/2026. **PASS trong phạm vi bản thí điểm đã triển khai**, với các giới hạn nền tảng/ngôn ngữ bên dưới. Chưa có điểm thực mới của người học; các dữ liệu dùng kiểm thử nằm ngoài gói giao và đã xóa khỏi workbook giao.

## Mốc hoàn thành và phần chưa làm

| Checkpoint | Trạng thái |
|---|---|
| 1 — bằng chứng, schema, thiết kế | Hoàn thành: 14 kỹ thuật, ledger nguồn/độ mạnh và giới hạn |
| 2 — pilot + chấm | Hoàn thành: 80 câu gốc nền N4,4 vai; QA độc lập đầy đủ lượt đầu và kiểm thay đổi nối tiếp |
| 3 — chọn bài + Gemini | Hoàn thành trong pilot: ba chế độ, nghỉ, mới/ôn/hỗ trợ, khóa sau nộp, sao chép lỗi/mẫu |
| 4 — mở rộng + Excel | **Một phần:** Excel đã tích hợp; chưa làm300–500 câu/N3/N2. Có30 bộ ghép từ80 câu, không coi là câu độc lập mới |
| 5 — kiểm thử và giao | Đã kiểm bản pilot như bảng dưới; chưa phải nghiệm thu ngân hàng mở rộng |

Mốc liền mạch hoàn thành đầy đủ: **Checkpoint3**. Các kiểm tra giao diện/dữ liệu củaCheckpoint5 đã làm cho pilot; không gắn nhãn toàn Phase3 đã hoàn thành quy mô300–500. Dừng tại giai đoạn thí điểm đã kiểm, ưu tiên thu dữ liệu người học trước khi sinh thêm câu.

## Kiểm nội dung độc lập

- Tác giả soạn; một tác tử AI khác giải mù80/80 trước khóa, sau đó rà80 khóa,240 nhiễu,22 bằng chứng đọc/nghe và4 vai. Khóa chữ cái lúc bản nháp khớp80/80; QA vẫn phát hiện lỗi dữ kiện/lời giải và yêu cầu sửa.
- Lượt đầu có1 block,5 major,10 minor theo **nhóm**. Sửa dữ kiện hàng tới trước ngày nhận, lịch thay đổi đã chốt, lời giải suy đoán, nguồn đích và thẻ người đối thoại. Sau đó kiểm22 câu có thay đổi/nguồn liên quan,4 vai; rà lại80 mapping tới thẻ chữa. Các liên kết sai mục tiêu đã sửa; không có thẻ đúng thì dùngnull.
- Thư viện **31 thẻ /37 câu chỉ để học** được rà lũy kế đầy đủ; ba câuG09 mới cũng được kiểm độc lập. Không gọi37 câu này là giải mù, không cộng vào80 câu ngân hàng.
- Lượt cuối PASS; không còn phát hiện cụ thể đang mở. [Báo cáo của người kiểm](ANSWER_KEY_AND_EXPLANATIONS/content_final_reaudit.md), [JSON kiểm định](ANSWER_KEY_AND_EXPLANATIONS/content_final_reaudit.json).
- Không tuyên bố giải mù lại toàn80 lần hai. Xáo nhãn sau soạn được kiểm bằng80 mapping đúng nội dung/nhiễu; khóa có digest/phiên bản. Chỉ metadata xác nhận QA được đóng sau phê duyệt; trường dạy học và khóa không đổi, đã đối chiếu hash trước/sau.

## Các kiểm tra thực chạy

| Phần | Kết quả cuối | Phạm vi |
|---|---|---|
| Engine | {len(engine)}/{len(engine)} nhóm kiểm đạt | 320 lựa chọn của80 câu; trống/invalid, buổi dở, đã thấy cùngstimulus, trợ giúp/đoán/gián đoạn, holdout/chậm,30 recipe, nhập/xuất/xung đột, hồi phục sau lỗi, dùng đúng kỹ năng chẩn đoán |
| Browser | {len(browser['tests'])} mục ghi nhận, không lỗi JS | {browser['browser']}; ChromeWindows chạy tự động, tệp local; bàn phím, chấm, lưu/tải lại, clipboard/fallback, JSONgộp, tìm mẫu, khóa, phiếu nói |
| Luồng bổ sung | {len(edge['tests'])}/{len(edge['tests'])} đạt | Offline không gửiHTTP ngoài, chặn mẫu/khóa trong đo, đánh dấu dừng, CSVUTF-8, lưu bị chặn→JSON, mô phỏng callbacknghe để kiểm snapshot trước script |
| Excel author | {len(author)}/{len(author)} đạt | Dòng hợp lệ/trùng/sai số, trợ giúp không vào điểm mới, giây→phút, trống không bịa tỉ lệ |
| Excel thật | {len(native['tests'])}/{len(native['tests'])} đạt | Excel{native['version']} COMẩn trên bản sao; chức năng cũ, save/reopen, UTF-8CSV thực tải từ browser→12 cột→copy vào workbook→phân loại Luyện không thành Mới |
| Toàn vẹn | {len(checks)}/{len(checks)} kiểm đạt |13 tài liệu trước không đổiSHA;5 worksheet cũ vàquan hệ bytegiữ nguyên;{nativefeatures['hyperlinks']}link,{nativefeatures['validations']}validation; đối chiếuJSON/JS/HTML/khóa |
| PDF |19 trang, đúng3/5/5/6 | RenderPoppler từng trang; xem ảnh bố cục và trang chữ lớn; kiểm lề/glyph trích xuất không thấy lỗi |

Kiểm phát hiện CSVphút thập phân bị Excelvùng dấu phẩy đọc thành chữ. Đã đổi riêng cộtCSVJ sang **giây nguyên**, workbook tự tính phút; test cuối kiểm đúng dữ liệu thực qua cầu nối. Các worksheet chẩn đoán cũ giữ đơn vị/hành vi cũ.

## Điều kiện đo và tính bền vững

STANDARD/DEEP hiển thị câu mới trước câu ôn, chỉ chữa sau nộp. QUICK vàbộ chọn mục tiêu là luyện. Câu có trợ giúp/đã thấy/cùng đoạn/đoán/gián đoạn/quá giờ không vào nhóm câu mới tự làm. Trống khác sai; câu dự kiến chưa mở chưa bị chấm. Mẫu n<5 không đưa mạnh/yếu chắc chắn. Ôn đúng câu cũ khác chuyển hiểu ở câu mới sau≥3 ngày. Lịch1/3/7/14 và ngưỡng mẫu là heuristic.

Chọn bài dùng lỗi gần đây để không giữ người học mãi ở lỗi cũ đã phục hồi; vẫn giữ lịch sử cũ. STANDARD ban đầu lấy mẫu đọc ngắn/từ cùng nền ngữ pháp; chỉ thêm nghe khi có giọng Nhật. Mệt4–5 không có chẩn đoán mới; buồn ngủ cho nghỉ. Không có cam kết đỗ, điểm chuẩn hay dự báo xác suấtN2.

## Giới hạn đã xác nhận

- **Nội dung:** QA do AI, chưa giáo viên bản ngữ/thử người học; độ khó/thời gian và cấpN4 là ước lượng. Một số nguồnJF vẫn ở cấp khóa, không xác nhận mọi từ đúng trang.
- **Nghe:** chỉ kịch bản/khóa được rà. Probe thực thấy3 giọngEnglish,không cója. Ứng dụng bỏ câu nghe khi thiếu giọng và không lấy giọngEnglish thay thế. TestUIcallback bằngstub **không phải nghe âm thực**; chưa kiểm phát âm/nhịp/tốc độ hay chất lượng âm trên iPad. Có liên kết MP3JF chính thức để luyện ngoài, không giả là điểmJLPT.
- **Nền tảng:** viewport1280×900,768×1024,1024×768,390×844 không tràn ngang; nút chính≥44px. Đây là mô phỏng màn hình, không phải kiểm iPad/Safari thật hoặc người chạm màn hình thật. iPadFiles có thể chỉ previewHTML.
- **Dữ liệu:** localStorage có thể khác theo trình duyệt/địa chỉ/chế độriêngtư. Đã thử tải lại ởChrome vàmô phỏng bị chặn lưu. Phải dùngJSON để sao lưu/chuyển thiết bị; không đồng bộ hay tự ghiExcel. JSONchỉnh tay không phải hồ sơ chống gian lận.
- **AI:** chỉ sao chép để người học tự dán Gemini; chưa kiểm trong tài khoản thật, không đọc lịch sử/nhập phản hồi tự động. NotebookLM tùy chọn, không bảo đảm tính năng theo gói cấp tài khoản.
- **Quy mô:** chưa300–500 câu, chưa ngân hàngN3/N2 hay100+ mini-test độc lập. 30recipe có thể thiếu câu mới/âm Nhật tùy lịch sử; giao diện nói rõ ôn/không đủ câu, không tạo câu chưa rà để bù.

13 tài liệu trước vẫn giữ nguyên trong các thư mục cũ. Tất cả tệp giao ởFINAL_PHASE3; dữ liệu kiểm thử/build/render ngoài gói. Không có điểm người học, tài khoản hayAPIkey được thêm vào gói.
'''
(O/'QA_REPORT.md').write_text(report,encoding='utf-8');print(json.dumps({'checks':len(checks),'all_pass':True,'coverage':b['coverage'],'nativeFeatures':nativefeatures},ensure_ascii=False))
