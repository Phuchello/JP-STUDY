from pathlib import Path
import json,subprocess,os,shutil
import pdfplumber
from PIL import Image,ImageOps,ImageDraw
R=Path(__file__).resolve().parents[2];T=R/'tmp/drive-first';PDF=R/'deliverables/phase3.5';poppler=os.environ.get('PDFTOPPM') or shutil.which('pdftoppm');assert poppler,'Set PDFTOPPM to installed Poppler executable'
paths=sorted(PDF.glob('*.pdf'));rows=[];thumb=[]
for f in paths:
 if not f.exists():continue
 name=f.stem.replace('.private','-private');subprocess.run([poppler,'-scale-to','1200','-png',str(f),str(T/name)],check=True,capture_output=True)
 with pdfplumber.open(f) as doc:
  pages=[]
  for i,pg in enumerate(doc.pages,1):
   text=pg.extract_text() or '';bad=[c['text'] for c in pg.chars if c['x0']<36 or c['x1']>pg.width-36 or c['top']<30 or c['bottom']>pg.height-20];assert not bad,(f.name,i,bad[:10]);assert '\ufffd' not in text and '(cid:' not in text
   pages.append({'page':i,'characters':len(text),'marginOrGlyphErrors':0,'links':len(pg.hyperlinks)})
   img=Image.open(T/(name+'-'+str(i)+'.png')).convert('RGB');img.thumbnail((400,570));tile=Image.new('RGB',(420,610),'white');tile.paste(img,((420-img.width)//2,25));ImageDraw.Draw(tile).text((10,5),name+' p'+str(i),fill='black');thumb.append(tile)
  assert 1<=len(pages)<=3,(f.name,len(pages))
  if f.name.startswith('00_'):assert len(pages)<=2
  rows.append({'file':f.name,'pages':len(pages),'checks':pages})
for batch in range(0,len(thumb),6):
 tiles=thumb[batch:batch+6];sheet=Image.new('RGB',(1260,1220),'#cccccc')
 for j,t in enumerate(tiles):sheet.paste(t,((j%3)*420,(j//3)*610))
 sheet.save(T/('pdf-contact-'+str(batch//6)+'.png'))
(T/'pdf_qa.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'files':len(rows),'pages':sum(x['pages'] for x in rows),'layoutChecksPassed':True,'visualContactSheets':(len(thumb)+5)//6}))
