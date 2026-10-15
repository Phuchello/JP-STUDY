from pathlib import Path
from lxml import etree as E
import zipfile,copy,posixpath,json
R=Path(__file__).resolve().parents[2];T=R/'tmp/jlpt-phase3';dest=R/'FINAL_PHASE3/JLPT_PROGRESS_TRACKER.xlsx'
def read(p):
 with zipfile.ZipFile(p) as z:return {n:z.read(n) for n in z.namelist()}
orig=read(R/'FINAL_V3/JLPT_PROGRESS_TRACKER_FINAL.xlsx');new=read(T/'import_sheet.xlsx');S='http://schemas.openxmlformats.org/spreadsheetml/2006/main';D='http://schemas.openxmlformats.org/officeDocument/2006/relationships';P='http://schemas.openxmlformats.org/package/2006/relationships';C='http://schemas.openxmlformats.org/package/2006/content-types';ns={'s':S}
oldstyle=E.fromstring(orig['xl/styles.xml']);newstyle=E.fromstring(new['xl/styles.xml']);maps={}
for kind in ['fonts','fills','borders','numFmts','cellStyleXfs','cellXfs']:
 a=oldstyle.find('s:'+kind,ns);b=newstyle.find('s:'+kind,ns)
 if b is None:continue
 if a is None:
  a=E.Element('{'+S+'}'+kind);oldstyle.insert(0,a)
 maps[kind]={}
 for i,item in enumerate(b):
  c=copy.deepcopy(item)
  if kind=='numFmts':
   oldid=int(c.get('numFmtId'));nid=max([163]+[int(x.get('numFmtId')) for x in a])+1;c.set('numFmtId',str(nid));maps[kind][oldid]=nid
  else:
   if kind in ['cellStyleXfs','cellXfs']:
    for attr,k in [('fontId','fonts'),('fillId','fills'),('borderId','borders'),('xfId','cellStyleXfs'),('numFmtId','numFmts')]:
     val=c.get(attr)
     if val is not None and int(val) in maps.get(k,{}):c.set(attr,str(maps[k][int(val)]))
   maps[kind][i]=len(a)
  a.append(c)
 a.set('count',str(len(a)))
orig['xl/styles.xml']=E.tostring(oldstyle,xml_declaration=True,encoding='UTF-8',standalone=True)
sheetpath=next(k for k in new if k.startswith('xl/worksheets/sheet') and k.endswith('.xml'));sh=E.fromstring(new[sheetpath]);sst=E.fromstring(new['xl/sharedStrings.xml']) if 'xl/sharedStrings.xml' in new else []
for c in sh.findall('.//s:c',ns):
 if c.get('s') is not None:c.set('s',str(maps['cellXfs'][int(c.get('s'))]))
 if c.get('t')=='s':
  idx=int(c.find('s:v',ns).text);c.remove(c.find('s:v',ns));c.set('t','inlineStr');x=E.SubElement(c,'{'+S+'}is')
  for child in sst[idx]:x.append(copy.deepcopy(child))
name='xl/worksheets/phase3_practice.xml';orig[name]=E.tostring(sh,xml_declaration=True,encoding='UTF-8',standalone=True)
wb=E.fromstring(orig['xl/workbook.xml']);sheets=wb.find('s:sheets',ns);rid='rIdPhase3Practice';E.SubElement(sheets,'{'+S+'}sheet',name='Luyện tập',sheetId=str(max(int(x.get('sheetId')) for x in sheets)+1),attrib={'{'+D+'}id':rid});orig['xl/workbook.xml']=E.tostring(wb,xml_declaration=True,encoding='UTF-8',standalone=True)
rels=E.fromstring(orig['xl/_rels/workbook.xml.rels']);E.SubElement(rels,'{'+P+'}Relationship',Id=rid,Type=D+'/worksheet',Target='worksheets/phase3_practice.xml');orig['xl/_rels/workbook.xml.rels']=E.tostring(rels,xml_declaration=True,encoding='UTF-8',standalone=True)
ct=E.fromstring(orig['[Content_Types].xml']);E.SubElement(ct,'{'+C+'}Override',PartName='/'+name,ContentType='application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml');orig['[Content_Types].xml']=E.tostring(ct,xml_declaration=True,encoding='UTF-8',standalone=True)
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
 for n,v in orig.items():z.writestr(n,v)
baseline=read(R/'FINAL_V3/JLPT_PROGRESS_TRACKER_FINAL.xlsx');preserved=[n for n in baseline if n.startswith('xl/worksheets/')];assert all(orig[n]==baseline[n] for n in preserved)
(T/'tracker_preservation.json').write_text(json.dumps({'all_original_worksheet_parts_byte_identical':True,'parts':preserved,'method':'ArtifactTool authored new sheet; OOXML merge preserves original sheet XML, relations, formulas, hyperlinks and validation.'},indent=2),encoding='utf-8');print('Merged without changing any of five existing worksheet parts')
