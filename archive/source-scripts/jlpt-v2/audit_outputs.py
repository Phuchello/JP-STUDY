from pathlib import Path
import hashlib,json,re,zipfile,posixpath
from lxml import etree as ET
from pypdf import PdfReader
import pdfplumber

root=Path(__file__).resolve().parents[2];out=root/'FINAL';tmp=root/'tmp/jlpt-v2'
original=json.loads((tmp/'original_hashes.json').read_text())
for name,h in original.items():assert hashlib.sha256((root/'outputs/jlpt-2026'/name).read_bytes()).hexdigest()==h
tests=json.loads((tmp/'v2_tracker_tests.json').read_text(encoding='utf-8'));assert all(t['ok'] for t in tests)
pdfmeta={}
for name,n in [('JLPT_START_HERE.pdf',2),('JLPT_DIAGNOSTIC_GUIDE.pdf',4)]:
    reader=PdfReader(out/name);assert len(reader.pages)==n
    page_bounds=[];links=[]
    with pdfplumber.open(out/name) as doc:
        for page in doc.pages:
            assert abs(page.width-595.276)<1 and abs(page.height-841.89)<1
            words=page.extract_words();assert words
            assert all(w['x0']>=35 and w['x1']<=page.width-25 for w in words)
            body=[w for w in words if w['top']<790]
            assert max(w['bottom'] for w in body)<795
            page_bounds.append(round(max(w['bottom'] for w in body),1))
    for p in reader.pages:
        assert '\ufffd' not in p.extract_text()
        for a in p.get('/Annots',[]):
            action=a.get_object().get('/A',{})
            if action.get('/S')=='/URI':links.append(str(action['/URI']))
    assert all(x.startswith('https://') and '<' not in x for x in links)
    pdfmeta[name]={'pages':n,'links':len(links),'body_bottom_points':page_bounds}
master=(out/'GEMINI_MASTER_TUTOR.md').read_text(encoding='utf-8');assert master.count('```text')==1 and master.count('```')==2
plan=(out/'JLPT_RESEARCH_PLAN_v2.md').read_text(encoding='utf-8')
assert re.findall(r'^\| (S\d\d) \|',plan,re.M)==[f'S{i:02}' for i in range(1,22)]
S='http://schemas.openxmlformats.org/spreadsheetml/2006/main';R='http://schemas.openxmlformats.org/officeDocument/2006/relationships';P='http://schemas.openxmlformats.org/package/2006/relationships';ns={'s':S,'r':R,'p':P}
with zipfile.ZipFile(out/'JLPT_PROGRESS_TRACKER_v2.xlsx') as z:
    book=ET.fromstring(z.read('xl/workbook.xml'));rr=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    targets={x.get('Id'):x.get('Target') for x in rr}
    paths={x.get('name'):posixpath.normpath(posixpath.join('xl',targets[x.get('{'+R+'}id')])).lstrip('/') for x in book.find('s:sheets',ns)}
    paths={k:v[3:] if v.startswith('xl/xl/') else v for k,v in paths.items()}
    assert set(paths)=={'Nhật ký','Đo năng lực','Tổng hợp tuần','Chẩn đoán'}
    sheets={name:ET.fromstring(z.read(p)) for name,p in paths.items()}
    formula_count=sum(len(s.findall('.//s:f',ns)) for s in sheets.values())
    all_formulas=[c.text for s in sheets.values() for c in s.findall('.//s:f',ns)]
    assert not any('HYPERLINK' in f for f in all_formulas)
    hyperlinks=0;internal=0;validation_count=0
    for name,s in sheets.items():
        for dv in s.findall('.//s:dataValidation',ns):
            assert dv.get('showErrorMessage')=='1' and dv.get('errorStyle')=='stop' and dv.get('allowBlank')=='1';validation_count+=1
        for h in s.findall('.//s:hyperlink',ns):
            hyperlinks+=1
            if h.get('location'):
                internal+=1;sheet,cell=h.get('location').rsplit('!',1);sheet=sheet.strip("'")
                assert sheet in sheets and re.fullmatch('[A-Z]+[1-9][0-9]*',cell)
    assert hyperlinks==79 and internal==13 and validation_count==20
    # No real measurements were fabricated by the development fixtures.
    for sheet,cols,start,end in [('Nhật ký','BCEFGI',8,59),('Đo năng lực','FGH',8,71),('Chẩn đoán','FGH',8,73),('Chẩn đoán','HIJ',78,88)]:
        for r in range(start,end+1):
            for col in cols:
                c=sheets[sheet].find(f'.//s:c[@r="{col}{r}"]',ns)
                if c is None:continue
                assert c.find('s:f',ns) is None
                v=c.find('s:v',ns);inline=c.find('s:is',ns)
                assert v is None or v.text in (None,'')
                assert inline is None or ''.join(inline.itertext())==''
    # Every original formula and native validation rule remains in its original sheet/cell.
    with zipfile.ZipFile(root/'outputs/jlpt-2026/Theo_doi_tien_bo_JLPT.xlsx') as old:
        original_formulas=0
        for name,p in [('Nhật ký','xl/worksheets/sheet1.xml'),('Đo năng lực','xl/worksheets/sheet2.xml')]:
            source=ET.fromstring(old.read(p));target=sheets[name]
            for c in source.findall('.//s:c',ns):
                f=c.find('s:f',ns)
                if f is not None:
                    assert target.find(f'.//s:c[@r="{c.get("r")}"]/s:f',ns).text==f.text;original_formulas+=1
            for v in source.findall('.//s:dataValidation',ns):
                signatures=lambda x:(x.get('type'),x.get('operator'),x.get('sqref'),tuple((ET.QName(c).localname,c.text) for c in x))
                assert signatures(v) in [signatures(n) for n in target.findall('.//s:dataValidation',ns)]
        assert original_formulas==68
    for s in sheets.values():
        assert not s.findall('.//s:c[@t="e"]',ns)
    assert not any('externalLinks/' in p for p in z.namelist())
meta={'original_hashes_unchanged':3,'original_formulas_preserved':68,'flow_tests':len(tests),'flow_tests_passed':True,'pdfs':pdfmeta,'native_hyperlinks':hyperlinks,'internal_links':internal,'validation_rules':validation_count,'formula_cells':formula_count,'questions':66,'diagnostic_blocks':11,'source_entries':21}
(tmp/'final_audit.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(meta,ensure_ascii=False))
