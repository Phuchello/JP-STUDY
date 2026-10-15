from pathlib import Path
import json,random,hashlib
R=Path(__file__).resolve().parents[2];O=R/'FINAL_PHASE3';P=O/'JLPT_PRACTICE';T=R/'tmp/jlpt-phase3'
lp=O/'JAPANESE_PATTERN_LIBRARY/patterns.json';lib=json.loads(lp.read_text(encoding='utf-8'))
g={'id':'G08','nameVi':'Chia thể trước khi nối mẫu','nameJa':'て形・た形・ない形','level':'N4 nền (ước lượng)','skill':'Ngữ pháp','meaningVi':'Xác định nhóm động từ trước. Thể て nối nhờ vả/tiến trình; thể た đi với kinh nghiệm đã từng; thể ない đi với phủ định. Nghĩa của cả mẫu không chỉ là nghĩa của một đuôi.','formula':'飲む→飲んで／飲んだ／飲まない; 見る→見て／見た／見ない; する→して／した／しない; 行く→行って／行った／行かない','minimalPair':'日本で働いたことがあります。／今、日本で働いています。','contrastVi':'Câu đầu nêu kinh nghiệm từng làm; câu sau nói hiện đang làm việc ở Nhật. ておく (làm trước để chuẩn bị) khác cả hai, xem TUFS088.','commonMistake':'Chỉ nhìn đuôi る rồi đoán nhóm; dùng thể từ điển trước たことがある; nhầm kinh nghiệm với hiện trạng.','correctionRule':'Đọc yêu cầu cần thể gì, gọi dạng trước khi nhìn lựa chọn, rồi kiểm cả nghĩa mẫu. Động từ đuôi る cần biết đúng nhóm, không đoán tuyệt đối.','prerequisites':['Thể từ điển; ba nhóm động từ'],'typicalMisunderstanding':'Nhận ra chữ Hán nhưng chưa tự gọi được thể động từ.','reviewStrategy':'Che các dạng, tự đổi một động từ cùng nhóm; thử câu mới sau chậm khi đủ sức.','reviewStatus':lib['patterns'][0]['reviewStatus'],'origin':'Original instructional card, not official JLPT item','estimatedMinutes':4,'tags':['chia thể','động từ','kinh nghiệm'], 'sources':[{'title':'TUFS 普通形の体系','url':'https://www.coelang.tufs.ac.jp/mt/ja/gmod/contents/explanation/038.html'},{'title':'JF Irodori Sơ cấp 1 L8: kinh nghiệm','url':'https://hn.jpf.go.jp/irodori/so-cap-1'},{'title':'TUFS ておく','url':'https://www.coelang.tufs.ac.jp/mt/ja/gmod/contents/explanation/088.html'}],'practice':[
 {'stem':'「飲む」をて形にしてください。','options':['飲んで','飲って'],'correctIndex':0,'answerVi':'1. 飲む thuộc nhóm đuôi む: む→んで; không phải って.','scored':False},
 {'stem':'「まだ一度も行った経験がない。」同じ意味は？','options':['行っておきます。','行ったことがありません。'],'correctIndex':1,'answerVi':'2. たことがありません nêu chưa từng; ておく là chuẩn bị trước.','scored':False},
 {'stem':'「見る」をない形にしてください。','options':['見ない','見らない'],'correctIndex':0,'answerVi':'1. 見る nhóm 2: bỏ る rồi thêm ない.','scored':False}]}
lib['patterns'].append(g);lib['count']=30;lib['unscoredPracticeCount']=34;lib['reviewLimit']=lib['reviewLimit'].replace('29 cards and 31','30 cards and 34');lp.write_text(json.dumps(lib,ensure_ascii=False,indent=2),encoding='utf-8');(P/'patterns.js').write_text('window.PatternLibrary='+json.dumps(lib,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
bp=P/'question_bank.json';b=json.loads(bp.read_text(encoding='utf-8'));old_keys={q['id']:q['correctAnswer'] for q in b['questions']};equiv=[]
for q in b['questions']:
 if q['categoryCode']=='VOC':q['patternId']=None
 if q['categoryCode']=='CONJ' or q['conceptId']=='experience':q['patternId']='G08'
 old={o['id']:o['text'] for o in q['options']};correct_text=old[q['correctAnswer']];arr=[{'oldId':o['id'],'text':o['text']} for o in q['options']];random.Random(int(hashlib.sha256(('option-order-v1:'+q['id']).encode()).hexdigest(),16)).shuffle(arr)
 newopts=[];newd={}
 for i,o in enumerate(arr):
  label='ABCD'[i];newopts.append({'id':label,'text':o['text']})
  if o['oldId']==old_keys[q['id']]:q['correctAnswer']=label
  else:newd[label]=q['distractorExplanations'][o['oldId']]
 q['options']=newopts;q['distractorExplanations']=newd;q['commonMistakes']=list(newd.values());q['typicalMisunderstanding']=q['commonMistakes'][0]
 if q['id']=='N4-LISTEN-008':q['explanationVi']=q['explanationVi'].replace('nên chọn B','nên chọn '+q['correctAnswer'])
 equiv.append({'id':q['id'],'oldKey':old_keys[q['id']],'newKey':q['correctAnswer'],'sameCorrectText':next(o['text'] for o in newopts if o['id']==q['correctAnswer'])==correct_text,'distractorsMapped':len(newd)==3})
b['answerKeyDigest']=hashlib.sha256(json.dumps([(q['id'],q['correctAnswer']) for q in b['questions']],ensure_ascii=False,separators=(',',':')).encode()).hexdigest();b['optionOrderNote']='Deterministic per-item shuffle after draft review, mapping exact option texts/rationales; no repeated A-D-C-B answer cycle. All 80 mappings tested.'
bp.write_text(json.dumps(b,ensure_ascii=False,indent=2),encoding='utf-8');(P/'bank.js').write_text('window.PracticeBank='+json.dumps(b,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
kp=O/'ANSWER_KEY_AND_EXPLANATIONS/validated_keys.json';keys={'bankVersion':b['bankVersion'],'answerKeyDigest':b['answerKeyDigest'],'validationNote':b['validationNote'],'questions':[{k:q.get(k) for k in ['id','correctAnswer','explanationVi','distractorExplanations','evidence','references','patternId']} for q in b['questions']]};kp.write_text(json.dumps(keys,ensure_ascii=False,indent=2),encoding='utf-8');(T/'option_mapping_tests.json').write_text(json.dumps(equiv,indent=2),encoding='utf-8');assert all(x['sameCorrectText'] and x['distractorsMapped'] for x in equiv)
p=P/'app.js';s=p.read_text(encoding='utf-8').replace('29 thẻ','30 thẻ').replace('${q.patternId)}','${q.patternId)}');s=s.replace('<p><a href="#library/${esc(q.patternId)}">Học mẫu liên quan 3–5 phút</a></p>', '${q.patternId?`<p><a href="#library/${esc(q.patternId)}">Học mẫu liên quan 3–5 phút</a></p>`:`<p>Ôn từ trong câu rồi tự gọi lại từ trước khi nhìn lựa chọn.</p>`}')
# JavaScript-driven error handling for the clipboard promise remains explicit.
p.write_text(s,encoding='utf-8')
rp=O/'RESEARCH_EVIDENCE_LEDGER.md';s=rp.read_text(encoding='utf-8').replace('29 thẻ','30 thẻ').replace('31 ví dụ','34 ví dụ').replace('2021-11 theo DOI-linked record; issue 148(1–2) năm 2022; chưa chốt ngày online trong các nguồn truy xuất','2021-11, Psychological Bulletin 147(11), 1215–1240 theo PubMed35238586; ngày online cụ thể không chốt')
s=s.replace('DOI chính xác minh riêng.','DOI chính xác minh riêng và [PubMed35238586](https://pubmed.ncbi.nlm.nih.gov/35238586/) đối chiếu issue; không dùng năm copyright2022 như năm số báo.');rp.write_text(s,encoding='utf-8')
p=O/'JAPANESE_PATTERN_LIBRARY/README.md';s=p.read_text(encoding='utf-8').replace('29 thẻ (7 ngữ pháp','30 thẻ (8 ngữ pháp').replace('31 câu','34 câu').replace('29 thẻ','30 thẻ').replace('G01–G07','G01–G08');p.write_text(s,encoding='utf-8')
p=T/'build_pdfs.py';s=p.read_text(encoding='utf-8').replace('29 thẻ','30 thẻ').replace("('body',10.8,14.5,8)","('body',12,16.2,9)").replace("('small',9.2,12,6)","('small',10,13.5,7)").replace("('compact',10,13,6)","('compact',11,14.8,7)");p.write_text(s,encoding='utf-8')
# Bundle once more without reapplying engine mutations.
template=(T/'index_template.html').read_text(encoding='utf-8').replace('<link rel="stylesheet" href="styles.css">','<style>'+(P/'styles.css').read_text(encoding='utf-8')+'</style>')
for name in ['bank.js','patterns.js','engine.js','app.js']:template=template.replace('<script src="'+name+'"></script>','<script>'+(P/name).read_text(encoding='utf-8').replace('</script','<\\/script')+'</script>')
(P/'index.html').write_text(template,encoding='utf-8');print('30 cards, 34 instructional examples, all 80 option-label mappings preserve meaning')
