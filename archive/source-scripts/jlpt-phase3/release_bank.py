from pathlib import Path
import json,hashlib,collections
R=Path(__file__).resolve().parents[2];T=R/'tmp/jlpt-phase3';O=R/'FINAL_PHASE3';P=O/'JLPT_PRACTICE';K=O/'ANSWER_KEY_AND_EXPLANATIONS'
b=json.loads((T/'pilot_draft.json').read_text(encoding='utf-8'));qs={q['id']:q for q in b['questions']}
q=qs['N4-MED-003'];q['passage']=q['passage'].replace('水曜日に店へ届きます','月曜日に店へ届きます')
q=qs['N4-SHORT-003'];q['passage']=q['passage'].replace('金曜日に変更できますか','金曜日に変更しました');q['evidence']='金曜日に変更しました。時間は同じです。'
q=qs['N4-SHORT-007'];q['options'][0]['text']='駅に財布を置いたかもしれないからです。';q['explanationVi']='Ví không có; có thể đã để ở ga nên quay lại hỏi tìm. かもしれない là phỏng đoán, chưa xác nhận đã bỏ quên.'
q['distractorExplanations']={k:v.replace('đã bỏ quên','có thể đã để quên') for k,v in q['distractorExplanations'].items()}
q=qs['N4-SHORT-001'];q['distractorExplanations']={k:v.replace('số phòng mới','số phòng') for k,v in q['distractorExplanations'].items()}
qs['N4-MED-004']['explanationVi']='いちばんはゆっくり食べたいからです cho biết lý do chính là muốn ăn thong thả; tiết kiệm chỉ là lợi ích thêm.'
qs['N4-MED-006']['explanationVi']='Lối vào còn có người dùng xe lăn và người mang hàng đi qua; xe đạp gây cản trở.'
qs['N4-LISTEN-008']['explanationVi']='Kịch bản yêu cầu 必ず店に電話してください trước giờ làm; メールだけではなく nhấn mạnh cần gọi điện, nên chọn B. Chỉ từ đáp án chưa biết lỗi do âm, từ, cấu trúc hay giữ thông tin; sau chấm mới đọc bản chữ để kiểm tra.'
def ref(qid,title,url):qs[qid]['references']=[{'id':'TARGET','title':title,'url':url}]
base='https://www.coelang.tufs.ac.jp/mt/ja/gmod/contents/explanation/'
for i in range(1,5):ref('N4-ORDER-%03d'%i,'TUFS V＋N',base+'079.html')
ref('N4-INTERP-001','Japan Foundation Irodori từ vựng: 〜以外','https://www.irodori.jpf.go.jp/assets/data/wordlist_Z.pdf')
ref('N4-INTERP-002','TUFS 副助詞: しか',base+'095.html')
ref('N4-INTERP-003','JF Irodori Sơ cấp 1: miễn nghĩa vụ / なくてもいい','https://jf.xcms.online/wp-content/uploads/2021/12/v1Grammar_SC1_VN.pdf')
ref('N4-INTERP-005','JF Irodori Sơ cấp 1 L15-22: 前に','https://jf.xcms.online/wp-content/uploads/2021/12/v1Grammar_SC1_VN.pdf#page=48')
ref('N4-GRAM-011','TUFS Vておきます',base+'088.html')
qs['N4-INTERP-006']['prerequisites'].append('V từ điển + と: thao tác và kết quả thường lệ')
for qid,word in [('N4-GRAM-006','会員証: thẻ hội viên'),('N4-GRAM-007','原本: bản gốc'),('N4-SHORT-005','絵の具: màu vẽ'),('N4-MED-002','市民センター: trung tâm sinh hoạt cộng đồng'),('N4-MED-006','車いす: xe lăn; ご協力: sự hợp tác')]:
 qs[qid]['prerequisites'].append(word);qs[qid]['hintVi']=word+'; dùng gợi ý sẽ ghi trợ giúp.'
partners=[(['何時からにしたいですか。','どうしてですか。','明日は午後5時からで大丈夫です。'],'Xác nhận ngày mai bắt đầu 17 giờ; chấp nhận lời nhờ lịch sự đơn giản.'),(['金曜日の午後5時までに出してください。','メールで送ってください。'],'Hạn thứ sáu 17 giờ, gửi email; người học tự nói lại dữ kiện.'),(['どちらまでですか。','この電車でB駅まで行って、そこでC駅行きに乗り換えてください。'],'Ga hư cấu A→B→C: đổi tàu ở B, không phải hướng dẫn tuyến thật.'),(['何時ごろ着きそうですか。','駅に着いたら、もう一度電話してください。'],'Chấp nhận chưa biết giờ đến; việc tiếp theo: tới ga thì gọi lại.')]
for role,(turns,info) in zip(b['roleplays'],partners):role.update(partnerTurns=turns,expectedInformation=info);role['validation']={'status':'reviewed','independentInitialReview':True,'authorCorrectionReview':True,'independentReaudit':False}
b['roleplays'][2]['taskVi']='Tình huống hư cấu: bạn ở ga A, muốn đến ga C. Hỏi người hỗ trợ rồi xác nhận phải đổi tàu ở đâu.'
mapping={'word-reading':'G02','word-meaning':'R01','particle-place':'G02','particle-time':'G04','particle-relation':'G02','form-te':'G06','form-nai':'G07','form-ta':'G05','permission':'T07','obligation':'T08','experience':'T09','noun-modifier':'R04','pattern-order':'G05','meaning-polarity':'R03','meaning-condition':'G07','short-time':'L01','short-reason':'R02','medium-purpose':'R01','medium-condition':'R03','listen-time':'L01','listen-action':'L02','practical-request':'T03'}
mapping.update({'medium-plan':'L01','medium-reason':'R02'})
for q in b['questions']:
 q['patternId']=mapping[q['conceptId']];q['relatedTemplate']='T03' if q['categoryCode'] in ['COMM','LISTEN'] else None
 q['typicalMisunderstanding']=q['commonMistakes'][0];q['reviewStrategy']=q['reviewRecommendation']
 q['validation']={'status':'reviewed','independentBlindSolved':True,'independentInitialReview':True,'authorCorrectionReview':True,'independentReaudit':False,'humanNativeCalibration':False,'date':'2026-10-15'}
 if q.get('audio'):q['audio']['scriptValidated']=True;q['audio']['acousticValidation']='unverified-device-dependent'
 q['commonMistakes']=list(q['distractorExplanations'].values())
b['status']='bounded-pilot-reviewed-with-disclosed-reaudit-limit';b['validationNote']='Independent first-pass review 80/80 +4 roles; author resolved findings. Independent second pass unavailable (usage limit). Not native-human calibrated. No expansion.'
b['answerKeyDigest']=hashlib.sha256(json.dumps([(q['id'],q['correctAnswer']) for q in b['questions']],ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
recipes=[]
for i,(c,v) in enumerate(b['concepts'].items(),1):recipes.append({'id':'P%02d'%i,'mode':'quick' if v['category']!='MED' else 'standard','objective':v['title'],'questionIds':[q['id'] for q in b['questions'] if q['conceptId']==c],'note':'Bộ ghép dùng lại câu; không phải đề độc lập mới.'})
for i in range(8):recipes.append({'id':'M%02d'%(i+1),'mode':'deep' if i>=6 else 'standard','objective':'Phối hợp nền N4 '+str(i+1),'questionIds':[q['id'] for j,q in enumerate(b['questions']) if j%8 in {i,(i+1)%8}],'note':'Bộ ghép từ cùng 80 câu. Hệ thống lọc theo sức, audio và lịch sử.'})
b['recipes']=recipes
(T/'pilot_corrected.json').write_text(json.dumps(b,ensure_ascii=False,indent=2),encoding='utf-8')
(P/'question_bank.json').write_text(json.dumps(b,ensure_ascii=False,indent=2),encoding='utf-8');(P/'bank.js').write_text('window.PracticeBank='+json.dumps(b,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
keys={'bankVersion':b['bankVersion'],'answerKeyDigest':b['answerKeyDigest'],'validationNote':b['validationNote'],'questions':[{k:q.get(k) for k in ['id','correctAnswer','explanationVi','distractorExplanations','evidence','references','patternId']} for q in b['questions']]}
(K/'validated_keys.json').write_text(json.dumps(keys,ensure_ascii=False,indent=2),encoding='utf-8');(K/'index.html').write_text('<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Khóa sau bài</title><p><a href="../JLPT_PRACTICE/index.html#keys">Mở khóa và giải thích trong ứng dụng</a></p><p>Mở chi tiết sẽ đánh dấu câu đã thấy. Không mở trong lượt đo.</p></html>',encoding='utf-8')
assert '月曜日に店へ届きます' in qs['N4-MED-003']['passage']
assert '変更できますか' not in qs['N4-SHORT-003']['passage']
print(len(b['questions']),len(recipes),b['answerKeyDigest'])
