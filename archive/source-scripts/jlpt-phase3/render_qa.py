from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
import subprocess,json,pdfplumber
R=Path(__file__).resolve().parents[2];T=R/'tmp/jlpt-phase3';O=R/'FINAL_PHASE3';render=T/'pdf_render';render.mkdir(exist_ok=True)
pop='<user>/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe';results=[]
for f in O.glob('*.pdf'):
 pref=render/f.stem;subprocess.run([pop,'-r','100','-png',str(f),str(pref)],check=True,capture_output=True)
 doc=pdfplumber.open(f);pages=[]
 for n,p in enumerate(doc.pages):
  txt=p.extract_text();blocks=p.extract_words();out=[b for b in blocks if b['top']<20 or b['bottom']>p.height-18 or b['x0']<25 or b['x1']>p.width-25]
  pages.append({'page':n+1,'characters':len(txt),'outOfMargins':out,'replacementGlyph': '\ufffd' in txt})
 results.append({'file':f.name,'pages':len(doc.pages),'checks':pages});doc.close()
 imgs=sorted(render.glob(f.stem+'-*.png'));thumbs=[]
 for x in imgs:
  im=Image.open(x).convert('RGB');im.thumbnail((560,790));canvas=Image.new('RGB',(580,830),'#dfe5e5');canvas.paste(im,((580-im.width)//2,28));ImageDraw.Draw(canvas).text((12,7),x.name,fill='black');thumbs.append(canvas)
 cols=2;rows=(len(thumbs)+cols-1)//cols;contact=Image.new('RGB',(580*cols,830*rows),'#c5d1d5')
 for i,im in enumerate(thumbs):contact.paste(im,((i%cols)*580,(i//cols)*830))
 contact.save(T/(f.stem+'_contact.png'))
(T/'pdf_qa.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(results,ensure_ascii=False))
