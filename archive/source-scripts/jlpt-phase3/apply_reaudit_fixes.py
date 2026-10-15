from pathlib import Path
import json
R=Path(__file__).resolve().parents[2];O=R/'FINAL_PHASE3';P=O/'JLPT_PRACTICE';T=R/'tmp/jlpt-phase3'
lp=O/'JAPANESE_PATTERN_LIBRARY/patterns.json';lib=json.loads(lp.read_text(encoding='utf-8'));ps={p['id']:p for p in lib['patterns']}
ps['G07']['formula']='Vたら / V・イ形容詞普通形なら、N・ナ形容詞は だ を付けず なら / Vると / Vば'
ps['G07']['correctionRule']+=' 名詞・ナ形容詞: 学生なら／静かなら, không 学生だなら.'
ps['G04']['practice'][2]['answerVi']='1. までに yêu cầu thực hiện việc gọi/liên lạc chậm nhất lúc 5 giờ; không nhất thiết phải kết thúc nói chuyện lúc 5 giờ.'
ps['R03']['dialogueVi']='Thông thường mở 10 giờ; riêng thứ hai mở 12 giờ.'
ps['G06']['minimalPair']='ドアが開いて（あいて）います。／ドアが開けて（あけて）あります。'
ps['G06']['commonMistake']='Với cặp đang luyện: 開く（あく）là tự động từ, dùng 開いて（あいて）いる; 開ける（あける）là tha động từ, dùng 開けてある. Không cho rằng ている luôn chỉ đang làm.'
ps['T03']['template']='【相手】さん、【名前】です。【日付】のシフトを【希望時刻】からに変更していただけませんか。【理由：Nの／V普通形／ナ形容詞な】ためです。'
ps['T04']['template']='【日付】は【理由：Nの／V普通形／ナ形容詞な】ため、お休みをいただけますか。必要な手続きがあれば教えてください。'
ps['T05']['template']='【名前】です。【理由：Nで／Vて・ので】、【到着見込み】。遅れてすみません。【次の確認】。'
ps['T05']['commonMistake']='Thiếu giờ ước hoặc bịa giờ đến. で sau lý do danh từ: 電車の遅れで; lý do là mệnh đề thì dùng 電車が遅れていて／遅れているので, không ghép で vào mọi câu.'
ps['T08']['template']='【時刻：8時など】に、【場所】で【問題】が起きました。今は【状況】です。どうすればいいですか。'
ps['T08']['commonMistake']='Đổ lỗi khi chưa rõ; giấu phần chưa biết. Mốc giờ dùng に, nơi sự việc dùng で; 今日／昨日 thường không thêm に.'
ps['T10']['template']='私は【意見：V・イ形容詞普通形／N・ナ形容詞だ】と思います。【理由】からです。まだ【不確かな点】は分かりません。'
ps['T11']['template']='【意見】。なぜなら、【理由：V・イ形容詞普通形／N・ナ形容詞だ】からです。例えば、【具体例】。'
ps['T11']['commonMistake']='Ví dụ không minh họa lý do. Trong khung bài tập này dùng cặp なぜなら…からです; đây không phải cách kết duy nhất của なぜなら trong mọi văn cảnh tiếng Nhật.'
g={'id':'G09','nameVi':'Được, cấm, phải và không cần','nameJa':'許可・禁止・義務','level':'N4 nền (ước lượng)','skill':'Ngữ pháp','meaningVi':'てもいい: được phép; てはいけない: bị cấm; なければならない: cần/phải làm; なくてもいい: không bắt buộc. Không cần làm không đồng nghĩa bị cấm làm.','formula':'Vて＋もいいです / Vて＋はいけません / Vない（bỏ い）＋ければなりません / Vない（bỏ い）＋くてもいいです','minimalPair':'今日は残らなければなりません。／今日は残らなくてもいいです。','contrastVi':'Hôm nay phải ở lại; hôm nay không cần ở lại. Cả hai có dấu hiệu phủ định trong cấu trúc nhưng nghĩa vụ trái nhau. 残る: ở lại.','commonMistake':'Thấy ない rồi suy cả hai đều cấm; lẫn được phép với bắt buộc.','correctionRule':'Đọc trọn phần sau động từ; tự gọi đúng một ý: được / cấm / phải / không cần, rồi đổi tình huống.','prerequisites':['Thể て và ない; cách đổi nhóm động từ'],'typicalMisunderstanding':'Chỉ bắt dấu phủ định mà bỏ nghĩa cả mẫu.','reviewStrategy':'Che cặp mẫu, tự nói một quy định hư cấu rồi đổi thành không bắt buộc. Sau chậm thử một câu chưa thấy, không dùng lại điểm cũ.','reviewStatus':ps['G01']['reviewStatus'],'origin':'Original instructional card, not official JLPT item','estimatedMinutes':4,'tags':['xin phép','quy định','nghĩa vụ','phủ định'],'sources':[{'title':'TUFS 許可','url':'https://www.coelang.tufs.ac.jp/mt/ja/gmod/contents/explanation/058.html'},{'title':'TUFS 禁止','url':'https://www.coelang.tufs.ac.jp/mt/ja/gmod/contents/explanation/059.html'},{'title':'JF 文-53 Vなければなりません','url':'https://www.jpf.go.jp/j/urawa/j_rsorcs/textbook/setsumei_pdf/setsumei14_2.pdf'},{'title':'JF Bangkok Akiko5: quy định và việc không cần làm','url':'https://ba.jpf.go.jp/wp-content/uploads/2022/03/Akiko5_bunpoo382002.pdf'}],'practice':[
 {'stem':'「この紙は出さなくてもいいです。」同じ意味は？','options':['この紙を出す必要はありません。','この紙を出してはいけません。'],'correctIndex':0,'answerVi':'1. Không cần nộp khác bị cấm nộp; đáp án2 thêm lệnh cấm không có trong câu.','scored':False},
 {'stem':'「ここでは、写真を撮ることは禁止です。」同じ意味は？','options':['写真を撮ってもいいです。','写真を撮ってはいけません。'],'correctIndex':1,'answerVi':'2. 禁止 là bị cấm, dùng てはいけません; てもいい là được phép, trái ý.','scored':False},
 {'stem':'「必ず、名前を書いてください。」必要があることを表す文は？','options':['名前を書かなければなりません。','名前を書かなくてもいいです。'],'correctIndex':0,'answerVi':'1. 必ず yêu cầu phải ghi; なければなりません giữ ý bắt buộc. Đáp án2 bỏ nghĩa vụ.','scored':False}]}
lib['patterns'].append(g);lib['count']=31;lib['unscoredPracticeCount']=37;lib['reviewLimit']='31 cards and 37 instructional examples; separate from independently audited 80-item bank.'
lib['registerGuide']={'casual':'Bạn thân: もう一度言って。 Có thể quá suồng sã với giáo viên/cấp trên.','polite':'Giáo viên/người chưa thân: もう一度言っていただけますか。 Hoặc もう一度お願いします khi ngữ cảnh rõ.','business':'Email doanh nghiệp có thể cần tên/đơn vị, chào mở và kết phù hợp. Các thẻ ở đây là giao tiếp lịch sự trong trường/nơi làm, chưa là bộ mẫu thư thương mại; không thêm kính ngữ dài khi chưa hiểu.'}
lp.write_text(json.dumps(lib,ensure_ascii=False,indent=2),encoding='utf-8');(P/'patterns.js').write_text('window.PatternLibrary='+json.dumps(lib,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
bp=P/'question_bank.json';b=json.loads(bp.read_text(encoding='utf-8'));qs={q['id']:q for q in b['questions']}
for n in range(1,9):qs['N4-GRAM-%03d'%n]['patternId']='G09'
mp={'ORDER005':'G08','ORDER007':None,'ORDER008':'G09','INTERP002':None,'INTERP003':'G09','INTERP005':'G05','PART007':None,'PART008':None,'PART009':None,'PART010':None,'SHORT002':'R03','SHORT004':'G04','SHORT006':'L02','SHORT008':'G09','MED002':'R03','MED003':'R03','MED006':'R01','LISTEN003':'L02','COMM002':'T01','COMM003':None,'COMM004':'G09'}
for short,pid in mp.items():code=re.sub(r'(\D+)(\d+)',r'N4-\1-\2',short) if False else 'N4-'+short[:-3]+'-'+short[-3:];qs[code]['patternId']=pid
for i in range(1,5):qs['N4-LISTEN-%03d'%i]['relatedTemplate']='T06'
for i in range(5,8):qs['N4-LISTEN-%03d'%i]['relatedTemplate']='T07'
qs['N4-LISTEN-008']['relatedTemplate']='T05';qs['N4-COMM-002']['relatedTemplate']='T01';qs['N4-COMM-003']['relatedTemplate']=None;qs['N4-COMM-004']['relatedTemplate']=None
q=qs['N4-SHORT-007'];q['distractorExplanations']={k:('Câu này không cho biết đã xác nhận nơi để ví; người viết quay lại ga vì có thể đã để ví ở đó.' if 'bỏ quên' in v else v) for k,v in q['distractorExplanations'].items()};q['commonMistakes']=list(q['distractorExplanations'].values());q['typicalMisunderstanding']=q['commonMistakes'][0]
bp.write_text(json.dumps(b,ensure_ascii=False,indent=2),encoding='utf-8');(P/'bank.js').write_text('window.PracticeBank='+json.dumps(b,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
kp=O/'ANSWER_KEY_AND_EXPLANATIONS/validated_keys.json';keys=json.loads(kp.read_text(encoding='utf-8'))
for q in keys['questions']:
 orig=qs[q['id']]
 for k in ['patternId','distractorExplanations']:q[k]=orig[k]
kp.write_text(json.dumps(keys,ensure_ascii=False,indent=2),encoding='utf-8')
for p in [P/'app.js',T/'build_pdfs.py',O/'JAPANESE_PATTERN_LIBRARY/README.md']:
 s=p.read_text(encoding='utf-8').replace('30 thẻ','31 thẻ').replace('34 câu','37 câu').replace('8 ngữ pháp','9 ngữ pháp').replace('G01–G08','G01–G09');p.write_text(s,encoding='utf-8')
# Rebuild one HTML entry with identical runtime/data resources.
template=(T/'index_template.html').read_text(encoding='utf-8').replace('<link rel="stylesheet" href="styles.css">','<style>'+(P/'styles.css').read_text(encoding='utf-8')+'</style>')
for name in ['bank.js','patterns.js','engine.js','app.js']:template=template.replace('<script src="'+name+'"></script>','<script>'+(P/name).read_text(encoding='utf-8').replace('</script','<\\/script')+'</script>')
(P/'index.html').write_text(template,encoding='utf-8');print('Reaudit corrections applied; G09 ready for independent review')
