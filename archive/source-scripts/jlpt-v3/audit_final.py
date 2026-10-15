from pathlib import Path
import hashlib,json,zipfile,re,posixpath
from lxml import etree as E
from pypdf import PdfReader
import pdfplumber
R=Path(__file__).resolve().parents[2];T=R/'tmp/jlpt-v3';O=R/'FINAL_V3'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
hashes=json.loads((T/'input_hashes.json').read_text(encoding='utf-8'))
assert len(hashes)==6
assert all(sha(R/'FINAL'/n)==h for n,h in hashes.items())
phase1=json.loads((R/'tmp/jlpt-v2/original_hashes.json').read_text(encoding='utf-8'));assert all(sha(R/'outputs/jlpt-2026'/n)==h for n,h in phase1.items())
tests=json.loads((T/'tracker_tests.json').read_text(encoding='utf-8'));assert all(t['ok'] for t in tests)
native=json.loads((T/'excel_native_tests.json').read_text(encoding='utf-8-sig'));assert native['status']=='passed' and all(t['passed'] for t in native['tests'])
key=json.loads((T/'key_verification.json').read_text(encoding='utf-8'));assert key['verified']==66
S='http://schemas.openxmlformats.org/spreadsheetml/2006/main';D='http://schemas.openxmlformats.org/officeDocument/2006/relationships';ns={'s':S}
baseline=json.loads((T/'input_workbook.json').read_text(encoding='utf-8'))
with zipfile.ZipFile(O/'JLPT_PROGRESS_TRACKER_FINAL.xlsx') as z:
 book=E.fromstring(z.read('xl/workbook.xml'));rr={x.get('Id'):x.get('Target') for x in E.fromstring(z.read('xl/_rels/workbook.xml.rels'))};ss=book.find('s:sheets',ns)
 assert ss[0].get('name')=='Làm nhanh'
 paths={s.get('name'):posixpath.normpath(posixpath.join('xl',rr[s.get('{'+D+'}id')])).lstrip('/') for s in ss};paths={k:p[3:] if p.startswith('xl/xl/') else p for k,p in paths.items()}
 strings=[]
 if 'xl/sharedStrings.xml' in z.namelist():strings=[''.join(a.itertext()) for a in E.fromstring(z.read('xl/sharedStrings.xml'))]
 sheets={};formulas={};values={};links=0;internal=0;validations=0
 for name,p in paths.items():
  sh=E.fromstring(z.read(p));sheets[name]=sh;formulas[name]={};values[name]={}
  for c in sh.findall('.//s:sheetData/s:row/s:c',ns):
   a=c.get('r');f=c.find('s:f',ns);v=c.find('s:v',ns);value=v.text if v is not None else None
   if c.get('t')=='s' and value is not None:value=strings[int(value)]
   if c.get('t')=='inlineStr':value=''.join(c.find('s:is',ns).itertext())
   values[name][a]=value
   if f is not None:formulas[name][a]=f.text
   assert c.get('t')!='e',(name,a,value)
  for dv in sh.findall('.//s:dataValidation',ns):assert dv.get('showErrorMessage')=='1' and dv.get('errorStyle')=='stop';validations+=1
  for h in sh.findall('.//s:hyperlink',ns):
   links+=1
   if h.get('location'):
    internal+=1;n,a=h.get('location').rsplit('!',1);assert n.strip("'") in paths and re.fullmatch('[A-Z]+[1-9][0-9]*',a)
  for hs in sh.findall('s:hyperlinks',ns):assert len(hs)>0
 allowed={('Đo năng lực',c+str(r)) for r in range(72,80) for c in ['A','E','F','G','H']}
 allowed|={('Tổng hợp tuần','F'+str(r)) for r in range(7,14)}|{('Tổng hợp tuần','B31'),('Tổng hợp tuần','E31')}
 changed=[];preserved=0
 for name,base in baseline.items():
  for a,c in base['cells'].items():
   if c['f'] is not None:
    if formulas[name].get(a)==c['f']:preserved+=1
    else:assert (name,a) in allowed,(name,a,'unexpected formula change');changed.append((name,a))
   elif (name,a) not in {('Chẩn đoán','A4'),('Tổng hợp tuần','A33')}:
    old=c['v'];new=values[name].get(a)
    if old in [None,''] and new in [None,'']:continue
    assert old==new,(name,a,old,new)
 assert len(changed)==49 and preserved==643
 for a in ['B13','C13','D13','E13','F13','G13','B16','D16','F16','B17','B21']:assert values['Làm nhanh'].get(a) in [None,'']
 assert values['Tổng hợp tuần'].get('B38') in [None,'']
 assert sheets['Chẩn đoán'].find('s:cols/s:col[@hidden="1"]',ns) is not None
 assert not any('HYPERLINK(' in f for fms in formulas.values() for f in fms.values())
 assert not any('externalLinks/' in p for p in z.namelist())
pdf=PdfReader(O/'JLPT_STUDY_SYSTEM_FINAL.pdf');assert len(pdf.pages)==12
uri=[];gotos=0;bounds=[]
with pdfplumber.open(O/'JLPT_STUDY_SYSTEM_FINAL.pdf') as doc:
 for pn,page in enumerate(doc.pages,1):
  assert abs(page.width-595.276)<1 and abs(page.height-841.89)<1
  words=page.extract_words();assert words
  assert all(w['x0']>=35 and w['x1']<=page.width-30 for w in words),(pn,'horizontal overflow')
  body=[w for w in words if w['top']<790];bounds.append(round(max(w['bottom'] for w in body),1));assert bounds[-1]<795
for pn,page in enumerate(pdf.pages,1):
 assert '\ufffd' not in page.extract_text()
 for a in page.get('/Annots',[]):
  a=a.get_object();action=a.get('/A',{})
  if action.get('/S')=='/URI':uri.append(str(action['/URI']))
  elif a.get('/Dest') is not None:gotos+=1
assert 'https://www.jlpt.jp/samples/sample2018/pdf/N4G.pdf' in uri
assert 'JLPT_PROGRESS_TRACKER_FINAL.xlsx' in uri and (O/'JLPT_PROGRESS_TRACKER_FINAL.xlsx').exists()
assert 'GEMINI_MASTER_TUTOR_FINAL.md' in uri and (O/'GEMINI_MASTER_TUTOR_FINAL.md').exists()
mp3={x for x in uri if x.endswith('.mp3')};assert len(mp3)==10
assert len(pdf.outline)==12 and gotos>=22
md=(O/'GEMINI_MASTER_TUTOR_FINAL.md').read_text(encoding='utf-8');prompt=md.split('```text\n',1)[1].split('\n```',1)[0]
assert all(re.search(r'^'+str(n)+r'\. ',prompt,re.M) for n in range(1,14))
lines=prompt.split('13. Xuất CHECKPOINT',1)[1].split('\nNhắc tôi ghi',1)[0].splitlines()[1:];lines=[x for x in lines if x.strip()];assert len(lines)==8
source=(R/'FINAL/GEMINI_MASTER_TUTOR.md').read_text(encoding='utf-8').split('```text\n',1)[1].split('\n```',1)[0]
for n in [2,3,5,6,7,8,9,10,11,12]:
 pat=rf'^{n}\. .*?(?=\n|$)';assert re.search(pat,source,re.M)[0]==re.search(pat,prompt,re.M)[0],n
example=['NGÀY / MỆT / NGỦ 24H: dữ liệu minh họa, chưa có số đo người học','PHÚT THỰC TẾ HỌC / NGHE / NÓI: chưa xác nhận','MỤC TIÊU / NGUỒN / MÃ BÀI: N4-G1, JLPT 2018','ÔN CŨ: chưa đo','CÂU MỚI LẦN ĐẦU: chưa đo','LỖI / MỘT CÂU SỬA: chưa xác định','TIẾP THEO / NGÀY ÔN: chữa 1 lỗi; ngày chưa xác nhận','CHƯA BIẾT / CẦN KIỂM NGUỒN: dữ liệu thiếu']
assert len(example)==8;(T/'checkpoint_roundtrip_fixture.txt').write_text('\n'.join(example),encoding='utf-8');assert (T/'checkpoint_roundtrip_fixture.txt').read_text(encoding='utf-8').splitlines()==example
result={'phase2_inputs_unchanged':6,'phase1_inputs_unchanged':3,'artifact_tests':len(tests),'native_excel_tests':len(native['tests']),'native_excel_version':native['version'],'verified_answer_keys':66,'v2_formulas_unchanged':preserved,'v2_formulas_changed_for_scope':len(changed),'hyperlinks':links,'internal_links':internal,'validation_rules':validations,'pdf_pages':12,'pdf_external_or_local_links':len(uri),'pdf_internal_links':gotos,'mp3_links_unchanged':len(mp3),'pdf_body_bounds':bounds,'checkpoint_lines':8,'prompt_rules_preserved':13}
(T/'final_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False))
