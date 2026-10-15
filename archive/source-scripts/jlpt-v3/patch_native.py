from pathlib import Path
import json,zipfile,posixpath
from lxml import etree as E
R=Path(__file__).resolve().parents[2];T=R/'tmp/jlpt-v3';target=R/'FINAL_V3/JLPT_PROGRESS_TRACKER_FINAL.xlsx'
S='http://schemas.openxmlformats.org/spreadsheetml/2006/main';D='http://schemas.openxmlformats.org/officeDocument/2006/relationships';P='http://schemas.openxmlformats.org/package/2006/relationships';ns={'s':S}
with zipfile.ZipFile(target) as z:files={n:z.read(n) for n in z.namelist()}
book=E.fromstring(files['xl/workbook.xml']);rels={a.get('Id'):a.get('Target') for a in E.fromstring(files['xl/_rels/workbook.xml.rels'])}
paths={sh.get('name'):posixpath.normpath(posixpath.join('xl',rels[sh.get('{'+D+'}id')])).lstrip('/') for sh in book.find('s:sheets',ns)}
paths={k:p[3:] if p.startswith('xl/xl/') else p for k,p in paths.items()}
ss=book.find('s:sheets',ns);fast=next(s for s in ss if s.get('name')=='Làm nhanh');ss.remove(fast);ss.insert(0,fast)
view=book.find('s:bookViews/s:workbookView',ns)
if view is not None:view.set('activeTab','0');view.set('firstSheet','0')
calc=book.find('s:calcPr',ns)
if calc is None:calc=E.SubElement(book,'{'+S+'}calcPr')
calc.set('calcMode','auto');calc.set('fullCalcOnLoad','1');calc.set('forceFullCalc','1')
files['xl/workbook.xml']=E.tostring(book,xml_declaration=True,encoding='UTF-8',standalone=True)
old=json.loads((R/'tmp/jlpt-v2/native_links.json').read_text(encoding='utf-8'));new=json.loads((T/'new_links.json').read_text(encoding='utf-8'));links={(x['sheet'],x['address']):x for x in old+new}
dvcount=0
for name,p in paths.items():
 sh=E.fromstring(files[p]);sv=sh.find('s:sheetViews/s:sheetView',ns)
 if sv is not None:sv.set('tabSelected','1' if name=='Làm nhanh' else '0')
 if name=='Làm nhanh' and sv is not None:
  sels=sv.findall('s:selection',ns)
  if not sels:sels=[E.SubElement(sv,'{'+S+'}selection')]
  for a in sels:a.set('activeCell','B13');a.set('sqref','B13')
  sv.set('topLeftCell','A1');sv.set('zoomScale','90')
 for d in sh.findall('.//s:dataValidation',ns):
  d.set('allowBlank','1');d.set('showErrorMessage','1');d.set('errorStyle','stop');d.set('errorTitle','Giá trị chưa hợp lệ');d.set('error','Nhập đúng phạm vi; 0 là bỏ câu, trống là chưa làm.');dvcount+=1
 if name in ['Làm nhanh','Chẩn đoán']:
  cols=sh.find('s:cols',ns)
  if cols is None:
   cols=E.Element('{'+S+'}cols');sh.insert(list(sh).index(sh.find('s:sheetData',ns)),cols)
  low,high=(9,25) if name=='Làm nhanh' else (13,16)
  # Clip existing column definitions, so hidden ranges never overlap them.
  for c in list(cols):
   a,b=int(c.get('min')),int(c.get('max'))
   if b<low or a>high:continue
   cols.remove(c)
   if a<low:
    c1=E.fromstring(E.tostring(c));c1.set('max',str(low-1));cols.append(c1)
   if b>high:
    c2=E.fromstring(E.tostring(c));c2.set('min',str(high+1));cols.append(c2)
  E.SubElement(cols,'{'+S+'}col',min=str(low),max=str(high),hidden='1',width='14',customWidth='1')
  cols[:]=sorted(cols,key=lambda a:int(a.get('min')))
 parent=sh.find('s:hyperlinks',ns)
 if parent is None:
  parent=E.Element('{'+S+'}hyperlinks');after={'printOptions','pageMargins','pageSetup','headerFooter','drawing','legacyDrawing','tableParts','extLst'};idx=next((i for i,c in enumerate(sh) if E.QName(c).localname in after),len(sh));sh.insert(idx,parent)
 rp=posixpath.dirname(p)+'/_rels/'+posixpath.basename(p)+'.rels';rr=E.fromstring(files[rp]) if rp in files else E.Element('{'+P+'}Relationships',nsmap={None:P});used={a.get('Id') for a in rr};n=1
 for (s,a),item in links.items():
  if s!=name:continue
  for h in list(parent):
   if h.get('ref')==a:parent.remove(h)
  h=E.SubElement(parent,'{'+S+'}hyperlink',ref=a,display=item['label'])
  if item['url'].startswith('#'):h.set('location',item['url'][1:])
  else:
   while 'rIdV3'+str(n) in used:n+=1
   rid='rIdV3'+str(n);used.add(rid);h.set('{'+D+'}id',rid);E.SubElement(rr,'{'+P+'}Relationship',Id=rid,Type=D+'/hyperlink',Target=item['url'],TargetMode='External')
 if len(parent)==0:sh.remove(parent)
 files[p]=E.tostring(sh,xml_declaration=True,encoding='UTF-8',standalone=True)
 if len(rr)>0:files[rp]=E.tostring(rr,xml_declaration=True,encoding='UTF-8',standalone=True)
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
 for n,v in files.items():z.writestr(n,v)
(T/'native_features.json').write_text(json.dumps({'hyperlinks':len(links),'validation_rules':dvcount,'first_sheet':'Làm nhanh','keys_hidden':True,'calc_mode':'auto'},ensure_ascii=False,indent=2),encoding='utf-8')
print('Native links, validations, opening view and hidden key columns applied')
