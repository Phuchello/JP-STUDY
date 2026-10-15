from pathlib import Path
import json,hashlib,zipfile
R=Path(__file__).resolve().parents[2];O=R/'FINAL_PHASE3';T=R/'tmp/jlpt-phase3'
p=O/'QA_REPORT.md';s=p.read_text(encoding='utf-8')
for old,new in {'Checkpoint3':'Checkpoint 3','Checkpoint5':'Checkpoint 5','300–500':'300–500','80+4':'80 + 4','80/80':'80/80','31 thẻ /37':'31 thẻ / 37','80 câu,4':'80 câu, 4','lượt đầu và kiểm thay đổi':'lượt đầu và các lượt kiểm thay đổi','80 khóa,240':'80 khóa, 240','22 bằng':'22 bằng','và4 vai':'và 4 vai','sửa F01–F16':'sửa F01–F16','4 vai;':'4 vai;','80 mapping':'80 mapping','3 giọngEnglish,không cója':'3 giọng tiếng Anh, không có giọng Nhật','giọngEnglish':'giọng tiếng Anh','TestUIcallback':'Test UI callback','CSVUTF-8':'CSV UTF-8','callbacknghe':'callback nghe','CSVphút':'CSV phút','Excelvùng':'Excel vùng','HTML/khóa':'HTML/khóa','cũ vàquan hệ bytegiữ':'cũ và quan hệ byte giữ','giọng Nhật. Mệt4–5':'giọng Nhật. Mệt 4–5','N4 là':'N4 là','với nguồnJF':'với nguồn JF','cấpN4':'cấp N4','câu ngân hàng80':'câu ngân hàng 80','ngày/ngườihọc':'ngày/người học','mẫu n<5':'mẫu n < 5','sau≥3':'sau ≥3','lịch1/3/7/14':'lịch 1/3/7/14','ChromeWindows':'Chrome Windows','Excel16.0':'Excel 16.0','RenderPoppler':'Render Poppler','13 tài liệu':'13 tài liệu','điểmJLPT':'điểm JLPT','ngân hàngN3/N2':'ngân hàng N3/N2','30recipe':'30 recipe','trình duyệt/địa chỉ/chế độriêngtư':'trình duyệt/địa chỉ/chế độ riêng tư','JSONchỉnh':'JSON chỉnh','vàAPIkey':'và API key','ởFINAL_PHASE3':'ở FINAL_PHASE3','và37':'và 37','và4':'và 4','cho pilot80':'cho pilot 80'}.items():s=s.replace(old,new)
p.write_text(s,encoding='utf-8')
b=json.loads((O/'JLPT_PRACTICE/question_bank.json').read_text(encoding='utf-8'));manifest={'release':'JLPT adaptive learning pilot 1.0.0','date':'2026-10-15','bankVersion':b['bankVersion'],'answerKeyDigest':b['answerKeyDigest'],'counts':{'objectiveQuestions':80,'speakingRoles':4,'patternCards':31,'instructionalOnlyQuestions':37,'reusableRecipes':30},'checkpoint':'1–3 complete;4 workbook integrated, bank expansion deferred;5 tested for pilot','previous13FilesUnchanged':True,'files':{}}
for f in sorted(O.rglob('*')):
 if f.is_file() and f.name!='MANIFEST.json':manifest['files'][str(f.relative_to(O)).replace('\\','/')]={'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
(O/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
dest=R/'JLPT_PHASE3_PILOT.zip'
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(O.rglob('*')):
  if f.is_file():z.write(f,'FINAL_PHASE3/'+str(f.relative_to(O)).replace('\\','/'))
with zipfile.ZipFile(dest) as z:assert z.testzip() is None;assert len(z.namelist())==len(manifest['files'])+1
print(json.dumps({'package':str(dest),'bytes':dest.stat().st_size,'files':len(manifest['files'])+1,'zip_integrity':'PASS'},ensure_ascii=False))
