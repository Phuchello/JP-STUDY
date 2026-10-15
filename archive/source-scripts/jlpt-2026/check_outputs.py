from pathlib import Path
import json, re, zipfile, xml.etree.ElementTree as ET
from pypdf import PdfReader
import pdfplumber

root=Path(__file__).resolve().parents[2]
out=root/'outputs'/'jlpt-2026'
md=(out/'Ke_hoach_JLPT_tam_thoi.md').read_text(encoding='utf-8')
reader=PdfReader(out/'Ke_hoach_JLPT_tam_thoi.pdf')
assert len(reader.pages)==10
assert md.count('```text')==7
refs=re.findall(r'^\| (S\d\d) \|',md,re.M)
assert refs==[f'S{i:02}' for i in range(1,21)]
uris=[]
for p in reader.pages:
    assert '\ufffd' not in p.extract_text()
    for ann in p.get('/Annots',[]):
        a=ann.get_object().get('/A',{})
        if a.get('/S')=='/URI':uris.append(str(a['/URI']))
assert len(uris)>60
assert all(u.startswith('https://') and '<' not in u and 'href=' not in u for u in uris)
assert 'https://ask-books.com/book-details/?slug=9784866397214' in uris
bounds=[]
with pdfplumber.open(out/'Ke_hoach_JLPT_tam_thoi.pdf') as p:
    for i,page in enumerate(p.pages,1):
        words=page.extract_words()
        body=[w for w in words if w['top']<790]
        bounds.append({'page':i,'body_bottom':round(max(w['bottom'] for w in body),1)})
        assert all(w['x0']>=35 and w['x1']<=page.width-25 for w in words)
        assert max(w['bottom'] for w in body)<790

ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(out/'Theo_doi_tien_bo_JLPT.xlsx') as z:
    daily=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
    scores=ET.fromstring(z.read('xl/worksheets/sheet2.xml'))
    assert len(daily.findall('.//s:dataValidation',ns))==3
    assert len(scores.findall('.//s:dataValidation',ns))==4
    for row in [8,39,71]:
        c=scores.find(f'.//s:c[@r="I{row}"]',ns)
        f=c.find('s:f',ns).text
        assert f'F{row}' in f and f'G{row}' in f and 'ISBLANK' in f
    # Authoring checks must not leave measured results behind.
    for s,columns,start,end in [(daily,'BCEFG',8,59),(scores,'FGH',8,71)]:
        for row in range(start,end+1):
            for col in columns:
                c=s.find(f'.//s:c[@r="{col}{row}"]',ns)
                if c is not None:
                    v=c.find('s:v',ns)
                    assert v is None or v.text in (None,'')
    assert not any(n.startswith('xl/externalLinks/') for n in z.namelist())
    summary={'pdf_pages':10,'prompts':7,'source_entries':len(refs),'pdf_links':len(uris),'unique_pdf_links':len(set(uris)),
             'tracker_checks':len(json.loads((root/'tmp/jlpt-2026/tracker_validation.json').read_text(encoding='utf-8'))),
             'page_bounds':bounds,'files':{p.name:p.stat().st_size for p in out.iterdir() if p.suffix in ('.md','.pdf','.xlsx')}}
(root/'tmp/jlpt-2026/final_validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False))
