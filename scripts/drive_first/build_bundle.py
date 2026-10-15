"""Reuse audited source items; never generate or rewrite Japanese questions."""
from pathlib import Path
import json,hashlib,csv
R=Path(__file__).resolve().parents[2];B=R/'deliverables/phase3/JLPT_PRACTICE/question_bank.json';K=R/'deliverables/phase3/ANSWER_KEY_AND_EXPLANATIONS/validated_keys.json';b=json.loads(B.read_text(encoding='utf-8'));keys=json.loads(K.read_text(encoding='utf-8'));lookup={q['id']:q for q in b['questions']}
def ids(group,a,z):return [f'N4-{group}-{i:03}' for i in range(a,z+1)]
spec=[('W01-B01','Trợ từ trong câu',ids('PART',1,5),5,8),('W01-B02','Từ và kanji',ids('VOC',1,8),5,10),('W01-B03','Chia thể cơ bản',ids('CONJ',1,5),5,8),('W01-B04','Đọc thông báo ngắn',ids('SHORT',1,5),8,12),('W01-B05','Hiểu mẫu câu',ids('GRAM',1,6),5,10),('W02-B01','Trợ từ trong ngữ cảnh',ids('PART',6,10),5,8),('W02-B02','Thể động từ và tính từ',ids('CONJ',6,10)+ids('GRAM',9,12),8,12),('W02-B03','Nối ý và ý câu',ids('GRAM',7,8)+ids('INTERP',1,6),8,12),('W02-B04','Sắp xếp câu',ids('ORDER',1,8),8,12),('W02-B05','Đọc và tìm bằng chứng',ids('SHORT',6,8)+ids('MED',1,6),10,15)]
quizzes=[{'id':i,'title':f'{i} | N4 {n} | {len(q)} câu','objective':n,'questionIds':q,'minutes':[a,z],'releaseGroup':'P0' if j<3 else 'P1','week':1 if i.startswith('W01') else 2,'mode':'self_reported_unaided_or_review','status':'QA_PENDING_LIVE_FORMS'} for j,(i,n,q,a,z) in enumerate(spec)]
allids=[i for q in quizzes for i in q['questionIds']];assert len(allids)==len(set(allids))==68;assert all(5<=len(q['questionIds'])<=10 for q in quizzes);assert all(not lookup[i].get('audio') for i in allids)
for i in allids:
 q=lookup[i];k=next(k for k in keys['questions'] if k['id']==i);assert k['correctAnswer']==q['correctAnswer'];assert len({o['text'] for o in q['options']})==4
data={'version':'drive-first-2026.10.15','sourceBankSha256':hashlib.sha256(B.read_bytes()).hexdigest(),'answerKeyDigest':b['answerKeyDigest'],'timezone':'Asia/Tokyo','quizzes':quizzes,'questions':{i:lookup[i] for i in allids},'roles':b['roleplays'],'patternNames':{p['id']:p['nameVi'] for p in json.loads((R/'deliverables/phase3/JAPANESE_PATTERN_LIBRARY/patterns.json').read_text(encoding='utf-8'))['patterns']}}
role_text=['# Chọn một vai nói, khoảng 3 phút','', 'Bốn tình huống gốc đã QA, dùng lại từ pilot. Đây là luyện có hướng dẫn, không là phép đo nói độc lập hoặc điểm JLPT. Chọn một vai, chép khối vào Gemini; chưa cần làm cả bốn. Dữ kiện là tình huống hư cấu, không phải lịch cá nhân.','']
for role in b['roleplays']:
 role_text += ['## '+role['id']+' — '+role['learningObjective'],'','```text','Đóng vai người đối thoại cho bài luyện tiếng Nhật sau.','MÃ: '+role['id'],'NGỮ CẢNH: '+role['taskVi'],'Ý CẦN TRUYỀN ĐẠT: '+'; '.join(role['requiredIntents']),'THẺ NGƯỜI ĐỐI THOẠI: '+' / '.join(role['partnerTurns']),'Để tôi mở lời trước, rồi hỏi từng lượt và CHỜ. Không đưa câu mẫu cho vai tôi trước khi tôi thử. Sau 3–6 lượt chỉ sửa 1–2 lỗi cản nghĩa, nhờ tôi nói lại với một dữ kiện khác. Không đoán vì sao tôi sai, không gán cấp, không chấm phát âm từ văn bản. Nếu tôi mệt, cho phép dừng.','```','']
(R/'deliverables/phase3.5/VAI_NOI.md').write_text('\n'.join(role_text),encoding='utf-8',newline='\n')
(R/'QUIZ_FORMS/quiz_plan.json').write_text(json.dumps({k:v for k,v in data.items() if k not in ['questions','roles','patternNames']},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
with (R/'QUIZ_FORMS/answer_mapping.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,lineterminator='\n');w.writerow(['quiz_id','position','question_id','correct_label','correct_text','points','stimulus_id','concept_id'])
 for quiz in quizzes:
  for pos,i in enumerate(quiz['questionIds'],1):
   q=lookup[i];w.writerow([quiz['id'],pos,i,q['correctAnswer'],next(o['text'] for o in q['options'] if o['id']==q['correctAnswer']),1,q['stimulusId'],q['conceptId']])
(R/'tmp/drive-first/data.json').write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
core=(R/'scripts/drive_first/core.js').read_text(encoding='utf-8');adapter=(R/'DRIVE_SETUP/workspace_adapter.js').read_text(encoding='utf-8')
(R/'DRIVE_SETUP/JP_STUDY_SETUP.gs').write_text('// Generated from audited payload + core.js + workspace_adapter.js. No credentials.\nconst JP_DATA='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n'+core+'\n'+adapter,encoding='utf-8',newline='\n')
print(json.dumps({'quizzes':len(quizzes),'uniqueReusedQuestions':len(allids),'unassignedOriginalQuestions':len(b['questions'])-len(allids),'regeneratedQuestions':0}))
