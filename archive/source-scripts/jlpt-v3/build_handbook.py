from pathlib import Path
import re,html,json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle,Spacer,PageBreak
R=Path(__file__).resolve().parents[2];T=R/'tmp/jlpt-v3';O=R/'FINAL_V3'
for n,f in [('VN','arial.ttf'),('VNB','arialbd.ttf'),('VNI','ariali.ttf')]:pdfmetrics.registerFont(TTFont(n,str(Path('C:/Windows/Fonts')/f)))
pdfmetrics.registerFontFamily('VN',normal='VN',bold='VNB',italic='VNI',boldItalic='VNB')
pdfmetrics.registerFont(TTFont('JP','C:/Windows/Fonts/msgothic.ttc',subfontIndex=0))
def style(n,sz,lead,**k):
 d=dict(fontName='VN',fontSize=sz,leading=lead,textColor=colors.HexColor('#20282E'),spaceAfter=7);d.update(k);return ParagraphStyle(n,**d)
body=style('Body',11,14.7);title=style('Title',20,24,fontName='VNB',spaceAfter=12);head=style('Head',12.5,16,fontName='VNB',spaceBefore=7,keepWithNext=True)
cell=style('Cell',10.5,13.6,spaceAfter=0);th=style('TH',10.5,13.6,fontName='VNB',textColor=colors.white,spaceAfter=0)
promptstyle=style('Prompt',10.4,13.6,spaceAfter=8)
W,H=A4;M=40;AW=W-M*2
def rich(s):
 s=s.replace('–','-').replace('—','-').replace('→',' > ');tokens=[]
 def link(m):
  tokens.append('<link href="'+html.escape(m.group(2),quote=True)+'" color="#234E72"><u>'+html.escape(m.group(1))+'</u></link>');return 'ZZLINK'+str(len(tokens)-1)+'ZZ'
 s=re.sub(r'\[([^\]]+)\]\(([^\s]+)\)',link,s);s=html.escape(s);s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'[\u3000-\u30ff\u3400-\u9fff\uff00-\uffef]+',lambda m:'<font name="JP">'+m.group(0)+'</font>',s)
 for i,t in enumerate(tokens):s=s.replace('ZZLINK'+str(i)+'ZZ',t)
 return s
txt=(T/'handbook_content.md').read_text(encoding='utf-8');prompt=(T/'tutor_prompt.txt').read_text(encoding='utf-8')
split=prompt.index('8. Luyện nghe:');txt=txt.replace('{{PROMPT1}}',prompt[:split].strip()).replace('{{PROMPT2}}',prompt[split:].strip())
pages=txt.split('<!-- PAGE -->');assert len(pages)==12
titles=[];story=[];est=[]
for pn,p in enumerate(pages,1):
 lines=p.strip().splitlines();titles.append(lines[0][2:]);i=0;items=[]
 while i<len(lines):
  l=lines[i].strip();i+=1
  if not l:continue
  if l.startswith('# '):items.append(Paragraph(rich(l[2:]),title));continue
  if l.startswith('## '):items.append(Paragraph(rich(l[3:]),head));continue
  if l.startswith('|'):
   rows=[]
   while True:
    cells=[x.strip() for x in l.strip('|').split('|')]
    if not all(re.fullmatch('[-: ]+',x) for x in cells):rows.append(cells)
    if i>=len(lines) or not lines[i].strip().startswith('|'):break
    l=lines[i].strip();i+=1
   n=len(rows[0]);widths=[.23,.77] if n==2 else [.21,.43,.36]
   if pn==12:widths=[.48,.52]
   table=Table([[Paragraph(rich(c),th if ri==0 else cell) for c in row] for ri,row in enumerate(rows)],colWidths=[AW*x for x in widths],repeatRows=1,hAlign='LEFT')
   rules=[('BACKGROUND',(0,0),(-1,0),colors.HexColor('#314C62')),('LINEBELOW',(0,0),(-1,0),.6,colors.HexColor('#314C62')),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,1),(-1,-1),.35,colors.HexColor('#D9D9D9'))]
   for r in range(2,len(rows),2):rules.append(('BACKGROUND',(0,r),(-1,r),colors.HexColor('#F1F5F8')))
   table.setStyle(TableStyle(rules));items += [table,Spacer(1,8)];continue
  # Prompt lines kept as separate paragraphs, checkpoint stays eight visible lines.
  use=promptstyle if pn in [9,10] else body
  items.append(Paragraph(rich(l),use))
 ht=sum(x.wrap(AW-12,H-92)[1]+x.getSpaceAfter()+x.getSpaceBefore() for x in items)
 est.append({'page':pn,'height':round(ht,1),'available':round(H-92-12,1)})
 story+=items
 if pn<12:story.append(PageBreak())
def footer(c,d):
 c.bookmarkPage('p'+str(d.page));c.addOutlineEntry(titles[d.page-1],'p'+str(d.page),level=0)
 c.setFont('VN',8);c.setFillColor(colors.HexColor('#59656E'));c.drawString(M,25,'Bắt đầu');c.linkRect('Về trang đầu','p1',(M,21,M+45,34),relative=0,thickness=0);c.drawCentredString(W/2,25,'Hệ thống học JLPT · cập nhật 15/10/2026');c.drawRightString(W-M,25,str(d.page)+' / 12')
doc=SimpleDocTemplate(str(O/'JLPT_STUDY_SYSTEM_FINAL.pdf'),pagesize=A4,leftMargin=M,rightMargin=M,topMargin=40,bottomMargin=43,title='Hệ thống học JLPT - mở và học một việc',author='Hỗ trợ học tập tiếng Nhật')
(T/'handbook_layout.json').write_text(json.dumps(est,indent=2),encoding='utf-8')
print(json.dumps(est));doc.build(story,onFirstPage=footer,onLaterPages=footer)
print('Handbook written')
