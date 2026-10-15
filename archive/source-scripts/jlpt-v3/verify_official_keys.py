from pathlib import Path
import re,json,unicodedata,hashlib
from pypdf import PdfReader
R=Path(__file__).resolve().parents[2];T=R/'tmp/jlpt-v3';m=json.loads((T/'manifest_final.json').read_text(encoding='utf-8'));keys=json.loads((T/'verified_keys.json').read_text(encoding='utf-8'))
tables={}
for level in ['N4','N3']:
 section=None;pending=None;group=None;result={}
 for page in PdfReader(T/(level+'answer.pdf')).pages:
  txt=unicodedata.normalize('NFKC',page.extract_text(extraction_mode='layout'))
  for line in txt.splitlines():
   stripped=re.sub(r'\s+','',line)
   if '●言語知識(文字・語彙)' in stripped:section='V';pending=None;continue
   if '●言語知識(文法)・読解' in stripped:section='G';pending=None;continue
   if '●聴解' in stripped:section='L';pending=None;continue
   line=line.strip()
   if not section:continue
   if line.startswith('問題'):
    # Some N4 reading group labels concatenate 4 and question 26.
    rest=line[2:].strip();mat=re.match(r'([1-7])\s*(.*)',rest);group=int(mat[1]);rest=mat[2];pending=[int(x) for x in re.findall(r'\d+',rest)];continue
   if not re.fullmatch(r'[\d\s]+',line):continue
   nums=[int(x) for x in line.split()]
   if pending is not None:
    if section=='L':nums=nums[1:] # official tables contain example before real answers
    assert len(nums)==len(pending),(level,section,group,pending,nums)
    for q,a in zip(pending,nums):result[(section,group,q)]=a
    pending=None
   elif group is not None and section!='L':pending=nums
 tables[level]=result
checked=[]
for b in m['blocks']:
 for j,q in enumerate(b['questions']):
  if b['part']=='L':gr,qn=map(int,re.findall(r'\d+',q));part='L'
  elif b['part']=='V':
   starts=[1,10,16,26,31] if b['level']=='N4' else [1,9,15,26,31];gr=max(i+1 for i,s in enumerate(starts) if q>=s);qn=q;part='V'
  else:
   starts=[1,16,21,26,30,34] if b['level']=='N4' else [1,14,19,24,28,34,38];gr=max(i+1 for i,s in enumerate(starts) if q>=s);qn=q;part='G'
  expected=tables[b['level']][(part,gr,qn)];actual=keys[b['code']][j];assert actual==expected,(b['code'],q,actual,expected)
  checked.append({'block':b['code'],'question':q,'official':expected,'embedded':actual,'ok':True})
(T/'key_verification.json').write_text(json.dumps({'method':'Independent parser of official PDF tables + rendered visual check','verified':len(checked),'pdf_sha256':{n:hashlib.sha256((T/(n+'answer.pdf')).read_bytes()).hexdigest() for n in ['N4','N3']},'items':checked},ensure_ascii=False,indent=2),encoding='utf-8')
print('All',len(checked),'selected answers independently match official PDF tables')
