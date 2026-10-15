from pathlib import Path
import re,html,json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle,Spacer,PageBreak

ROOT=Path(__file__).resolve().parents[2];TMP=ROOT/'tmp/jlpt-v2';OUT=ROOT/'FINAL'
for name,file in [('VN','arial.ttf'),('VNB','arialbd.ttf'),('VNI','ariali.ttf')]:pdfmetrics.registerFont(TTFont(name,str(Path('C:/Windows/Fonts')/file)))
pdfmetrics.registerFontFamily('VN',normal='VN',bold='VNB',italic='VNI',boldItalic='VNB')
pdfmetrics.registerFont(TTFont('JP','C:/Windows/Fonts/msgothic.ttc',subfontIndex=0))
def st(name,size,leading,**kw):
    d=dict(fontName='VN',fontSize=size,leading=leading,textColor=colors.HexColor('#20282E'),spaceAfter=6);d.update(kw);return ParagraphStyle(name,**d)
body=st('Body',10.4,13.8)
title=st('Title',18,22,fontName='VNB',textColor=colors.black,keepWithNext=True)
h2=st('Heading',11.4,14.5,fontName='VNB',textColor=colors.black,spaceBefore=7,keepWithNext=True)
cell=st('Cell',9.4,12.4,spaceAfter=0)
th=st('Header',9.4,12.4,spaceAfter=0,fontName='VNB',textColor=colors.white)
W,H=A4;M=40;AW=W-2*M;AH=H-84

def rich(t):
    t=t.replace('–','-').replace('—','-')
    tokens=[]
    def keep(m):
        tokens.append('<link href="%s" color="#234E72">%s</link>'%(html.escape(m.group(2),quote=True),html.escape(m.group(1))))
        return f'ZZLINK{len(tokens)-1}ZZ'
    t=re.sub(r'\[([^\]]+)\]\((https?://[^\s]+)\)',keep,t)
    t=html.escape(t)
    t=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',t)
    t=re.sub(r'`([^`]+)`',r'<b>\1</b>',t)
    t=re.sub(r'[\u3040-\u30ff\u3400-\u9fff\uff00-\uffef]+',lambda m:'<font name="JP">'+m.group(0)+'</font>',t)
    for i,v in enumerate(tokens):t=t.replace(f'ZZLINK{i}ZZ',v)
    return t

def make_table(rows,kind,pn,idx):
    n=len(rows[0])
    if kind=='start':widths=[.23,.42,.35] if pn==1 else [.15,.48,.10,.27]
    elif pn==1:widths=[.42,.58] if idx==0 else [.16,.52,.12,.20]
    elif pn==2:widths=[.15,.52,.14,.19]
    elif pn==3:widths=[.37,.63] if idx==0 else [.15,.52,.12,.21]
    else:widths=[.08,.43,.49]
    if len(widths)!=n:widths=[1/n]*n
    t=Table([[Paragraph(rich(c),th if i==0 else cell) for c in row] for i,row in enumerate(rows)],colWidths=[AW*v for v in widths],repeatRows=1,hAlign='LEFT')
    rules=[('BACKGROUND',(0,0),(-1,0),colors.HexColor('#314C62')),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#D9D9D9')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5)]
    for r in range(2,len(rows),2):rules.append(('BACKGROUND',(0,r),(-1,r),colors.HexColor('#F2F5F7')))
    t.setStyle(TableStyle(rules));return [t,Spacer(1,7)]

def parse(txt,kind,pn):
    lines=txt.strip().splitlines();i=0;out=[];idx=0
    while i<len(lines):
        l=lines[i].strip()
        if not l:i+=1;continue
        if l.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch('[-: ]+',c) for c in cells):rows.append(cells)
                i+=1
            out+=make_table(rows,kind,pn,idx);idx+=1;continue
        if l.startswith('# '):out.append(Paragraph(rich(l[2:]),title));i+=1;continue
        if l.startswith('## '):out.append(Paragraph(rich(l[3:]),h2));i+=1;continue
        words=[l];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','- ')) and not re.match(r'^\d+\. ',lines[i]):words.append(lines[i].strip());i+=1
        out.append(Paragraph(rich(' '.join(words)),body))
    return out

est=[]
for file,kind,source in [('JLPT_START_HERE.pdf','start','start_content.md'),('JLPT_DIAGNOSTIC_GUIDE.pdf','diagnostic','diagnostic_content.md')]:
    pages=(TMP/source).read_text(encoding='utf-8').split('<!-- PAGE -->');story=[]
    for pn,text in enumerate(pages,1):
        items=parse(text,kind,pn);ht=0
        for item in items:
            _,h=item.wrap(AW-12,AH);ht+=h+item.getSpaceAfter()+item.getSpaceBefore()
        est.append(dict(file=file,page=pn,estimated_height=round(ht,1),available=round(AH-12,1)))
        story+=items
        if pn<len(pages):story.append(PageBreak())
    def footer(c,d,total=len(pages)):
        c.setFont('VN',8);c.setFillColor(colors.HexColor('#59656E'));c.drawString(M,25,'Hệ thống JLPT tạm thời - 15/10/2026');c.drawRightString(W-M,25,f'{d.page} / {total}')
    doc=SimpleDocTemplate(str(OUT/file),pagesize=A4,leftMargin=M,rightMargin=M,topMargin=42,bottomMargin=42,title='Bắt đầu học tiếng Nhật' if kind=='start' else 'Hướng dẫn chẩn đoán N4 và N3',author='Hỗ trợ học tập tiếng Nhật')
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
(TMP/'pdf_layout_estimates.json').write_text(json.dumps(est,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(est,ensure_ascii=False))
