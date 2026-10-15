from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
T=Path(__file__).resolve().parent;R=T.parents[1];S='http://schemas.openxmlformats.org/spreadsheetml/2006/main';ns={'s':S}
with ZipFile(T/'authoring_export.xlsx') as z:base={n:z.read(n) for n in z.namelist()}
with ZipFile(R/'FINAL_V3/JLPT_PROGRESS_TRACKER_FINAL.xlsx') as z:full={n:z.read(n) for n in z.namelist()}
for kind in ['nobook','nocols','noviews','links_only']:
 f=dict(full)
 if kind in ['nobook','links_only']:f['xl/workbook.xml']=base['xl/workbook.xml']
 for p in ['xl/worksheets/sheet4.xml','xl/worksheets/sheet5.xml']:
  a=E.fromstring(f[p]);b=E.fromstring(base[p]);changed=False
  for tag in (['cols'] if kind=='nocols' else ['sheetViews'] if kind=='noviews' else ['cols','sheetViews'] if kind=='links_only' else []):
   old=a.find('s:'+tag,ns);new=b.find('s:'+tag,ns)
   if old is not None:
    idx=list(a).index(old);a.remove(old)
    if new is not None:a.insert(idx,new)
   changed=True
  if changed:f[p]=E.tostring(a,xml_declaration=True,encoding='UTF-8',standalone=True)
 with ZipFile(T/(kind+'.xlsx'),'w',ZIP_DEFLATED) as z:
  for n,v in f.items():z.writestr(n,v)
print('Four metadata isolation copies ready')
