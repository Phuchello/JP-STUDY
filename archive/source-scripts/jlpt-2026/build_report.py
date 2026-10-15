from pathlib import Path
import re, html, json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, PageBreak, Spacer, KeepTogether

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'outputs' / 'jlpt-2026'
SRC = OUT / 'Ke_hoach_JLPT_tam_thoi.md'
PDF = OUT / 'Ke_hoach_JLPT_tam_thoi.pdf'
QA = ROOT / 'tmp' / 'jlpt-2026'
pdfmetrics.registerFont(TTFont('VN', r'C:\Windows\Fonts\arial.ttf'))
pdfmetrics.registerFont(TTFont('VNB', r'C:\Windows\Fonts\arialbd.ttf'))
pdfmetrics.registerFont(TTFont('VNI', r'C:\Windows\Fonts\ariali.ttf'))
pdfmetrics.registerFontFamily('VN', normal='VN', bold='VNB', italic='VNI', boldItalic='VNB')
pdfmetrics.registerFont(TTFont('JP', r'C:\Windows\Fonts\msgothic.ttc', subfontIndex=0))

source_urls = {
'S01':'https://www.jlpt.jp/reference/pdf/guide_2026.pdf',
'S02':'https://www.jlpt.jp/e/guideline/testsections.html',
'S03':'https://www.jlpt.jp/e/guideline/results.html',
'S04':'https://www.jlpt.jp/e/samples/sampleindex.html',
'S05':'https://hn.jpf.go.jp/irodori',
'S06':'https://www.irodori.jpf.go.jp/en/faq.html',
'S07':'https://ask-books.com/book-details/?slug=9784866397214',
'S08':'https://tadoku.org/japanese/en/free-books-en/',
'S09':'https://docs.ankiweb.net/syncing.html',
'S10':'https://www.science.org/doi/10.1126/science.1152408',
'S11':'https://wixtedlab.ucsd.edu/publications/wixted/Cepeda_et_al_(2006).pdf',
'S12':'https://pubmed.ncbi.nlm.nih.gov/27530500/',
'S13':'https://www.aasm.org/resources/pdf/adultsleepdurationconsensus.pdf',
'S14':'https://support.google.com/gemini/answer/16448384',
'S15':'https://support.google.com/gemini/answer/14903178?co=GENIE.Platform%3DDesktop&hl=en',
'S16':'https://support.google.com/gemini/answer/15274899?co=GENIE.Platform%3DiOS&hl=en',
'S17':'https://support.google.com/gemini/answer/13575153',
'S18':'https://support.google.com/notebooklm/answer/16164461?hl=en&co=GENIE.Platform%3DiOS',
'S19':'https://support.google.com/notebooklm/answer/16215270?hl=en',
'S20':'https://www.jlpt.jp/e/about/cefr_reference.html',
}

def rich(text):
    text = text.replace('–', '-').replace('—', '-')
    tokens = []
    def keep(m):
        tokens.append('<link href="%s" color="#234E72">%s</link>' % (html.escape(m.group(2), quote=True), html.escape(m.group(1))))
        return f'ZZLINK{len(tokens)-1}ZZ'
    text = re.sub(r'\[([^\]]+)\]\((https?://[^\s]+)\)', keep, text)
    text = html.escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    def refs(m):
        keys = []
        for item in m.group(1).split(','):
            item=item.strip()
            span=re.fullmatch(r'S(\d+)-S(\d+)', item)
            keys.extend([f'S{n:02d}' for n in range(int(span[1]),int(span[2])+1)] if span else [item])
        return '[' + ', '.join(f'<link href="{html.escape(source_urls[k],quote=True)}" color="#234E72">{k}</link>' if k in source_urls else k for k in keys) + ']'
    text = re.sub(r'\[(S\d{2}(?:-S\d{2})?(?:,\s*S\d{2}(?:-S\d{2})?)*)\]', refs, text)
    # Link literal addresses while preserving internal punctuation in query strings.
    text = re.sub(r'(?<!["=])(https?://[^\s<]+)', lambda m: '<link href="%s" color="#234E72">%s</link>'%(m.group(1).rstrip(';'),m.group(1).rstrip(';')), text)
    text = re.sub(r'[\u3040-\u30ff\u3400-\u9fff\uff00-\uffef]+', lambda m: '<font name="JP">'+m.group(0)+'</font>', text)
    for i,t in enumerate(tokens): text=text.replace(f'ZZLINK{i}ZZ',t)
    return text

def style(name, size=10.3, leading=13.8, **kw):
    args=dict(fontName='VN', fontSize=size, leading=leading, textColor=colors.HexColor('#20282E'), spaceAfter=6)
    args.update(kw)
    return ParagraphStyle(name, **args)

body=style('body')
small=style('small',9.0,11.8)
title=style('title',18,22,fontName='VNB',textColor=colors.black,spaceBefore=0,keepWithNext=True)
h2=style('h2',11.5,14.5,fontName='VNB',textColor=colors.black,spaceBefore=7,keepWithNext=True)
cell=style('cell',9.2,12.1,spaceBefore=0)
cell.spaceAfter=0
head=style('head',9.2,12.1,fontName='VNB',textColor=colors.white)
head.spaceAfter=0
prompt=style('prompt',9.7,12.6,spaceBefore=0)
ledger=style('ledger',8.5,11.2)
ledger.spaceAfter=0
ledgerhead=style('ledgerhead',8.8,11.3,fontName='VNB',textColor=colors.white)
ledgerhead.spaceAfter=0

W,H=A4
M=40
AW=W-2*M
AH=H-42-42
page_index=0

def make_table(rows, page_num, index):
    n=len(rows[0])
    if page_num==1: fr=[.53,.47]
    elif page_num==2: fr=[.20,.14,.45,.21]
    elif page_num==3 and index==0: fr=[.14,.60,.26]
    elif page_num==3: fr=[.22,.44,.34]
    elif page_num==4 and index==0: fr=[.11,.42,.47]
    elif page_num==4: fr=[.23,.49,.28]
    elif page_num==7: fr=[.19,.46,.35] if index==0 else [.18,.55,.27]
    elif page_num==8: fr=[.24,.61,.15]
    elif page_num==10: fr=[.07,.43,.50]
    else: fr=[1/n]*n
    if len(fr)!=n: fr=[1/n]*n
    data=[]
    for i,row in enumerate(rows):
        st=(ledgerhead if i==0 else ledger) if page_num==10 else (head if i==0 else cell)
        data.append([Paragraph(rich(x),st) for x in row])
    t=Table(data,colWidths=[AW*f for f in fr],hAlign='LEFT',repeatRows=1)
    pad=4 if page_num==10 else 5
    commands=[('BACKGROUND',(0,0),(-1,0),colors.HexColor('#314C62')),
              ('GRID',(0,0),(-1,-1),.4,colors.HexColor('#D9D9D9')),
              ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
              ('TOPPADDING',(0,0),(-1,-1),pad),('BOTTOMPADDING',(0,0),(-1,-1),pad),
              ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5)]
    for i in range(2,len(rows),2):commands.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#F2F5F7')))
    t.setStyle(TableStyle(commands))
    return [t,Spacer(1,7)]

def parse_page(text,pn):
    lines=text.strip().splitlines()
    result=[]; i=0; table_index=0
    while i<len(lines):
        line=lines[i].strip()
        if not line: i+=1; continue
        if line.startswith('```'):
            items=[];i+=1
            while i<len(lines) and not lines[i].startswith('```'):
                items.append(lines[i].strip());i+=1
            result.append(Paragraph(rich(' '.join(items)),prompt));i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch('[-: ]+',x) for x in cells):rows.append(cells)
                i+=1
            result.extend(make_table(rows,pn,table_index));table_index+=1;continue
        if line.startswith('# '):
            result.append(Paragraph(rich(line[2:]),title));i+=1;continue
        if line.startswith('## '):
            result.append(Paragraph(rich(line[3:]),h2));i+=1;continue
        if line.startswith('- ') or re.match(r'^\d+\. ',line):
            result.append(Paragraph(rich(line),body if pn!=10 else small));i+=1;continue
        words=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','```','- ')) and not re.match(r'^\d+\. ',lines[i]):
            words.append(lines[i].strip());i+=1
        result.append(Paragraph(rich(' '.join(words)),small if pn==10 else body))
    return result

def footer(c,doc):
    c.setFont('VN',8)
    c.setFillColor(colors.HexColor('#59656E'))
    c.drawString(M,25,'Kế hoạch tạm thời  •  15/10/2026')
    c.drawRightString(W-M,25,f'{doc.page} / 10')

pages=SRC.read_text(encoding='utf-8').split('<!-- PAGE -->')
story=[]; sizes=[]
for pn,txt in enumerate(pages,1):
    elements=parse_page(txt,pn)
    ht=0
    for e in elements:
        _,h=e.wrap(AW-12,AH)
        ht+=h+e.getSpaceBefore()+e.getSpaceAfter()
    sizes.append({'page':pn,'estimated_height':round(ht,1),'available':round(AH-12,1),'words':len(txt.split())})
    story.extend(elements)
    if pn<len(pages):story.append(PageBreak())
doc=SimpleDocTemplate(str(PDF),pagesize=A4,leftMargin=M,rightMargin=M,topMargin=42,bottomMargin=42,
                     title='Kế hoạch phục hồi tiếng Nhật và dự thi N2',author='Báo cáo hỗ trợ học tập',
                     subject='Kế hoạch tạm thời N4 N3 N2 cho người vừa học vừa làm tại Nhật')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
(QA/'layout_estimates.json').write_text(json.dumps(sizes,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'pdf':str(PDF),'pages':len(pages),'layout':sizes},ensure_ascii=False))
