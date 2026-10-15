"""Fill only HYPERLINK display caches unsupported by the artifact calculator.
Native Google Sheets readback independently verified these exact formula labels.
No changes to formulas, inputs, layout, styles or other package parts.
"""
from pathlib import Path
import zipfile,re,xml.etree.ElementTree as E
R=Path(__file__).resolve().parents[2];p=R/'DRIVE_SETUP/JP_STUDY_HOC_HOM_NAY.xlsx';S='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
with zipfile.ZipFile(p) as z: entries={n:z.read(n) for n in z.namelist()}
count=0
for name,data in list(entries.items()):
 if not name.startswith('xl/worksheets/') or not name.endswith('.xml'):continue
 root=E.fromstring(data);changed=False
 for c in root.iter(S+'c'):
  f=c.find(S+'f')
  if f is None or not f.text or not f.text.startswith('HYPERLINK('):continue
  label=re.search(r',"([^"]+)"\)$',f.text).group(1);v=c.find(S+'v')
  if v is None:v=E.SubElement(c,S+'v')
  c.set('t','str');v.text=label;changed=True;count+=1
 if changed:entries[name]=E.tostring(root,encoding='utf-8',xml_declaration=True)
with zipfile.ZipFile(p,'w',zipfile.ZIP_DEFLATED) as z:
 for name,data in entries.items():z.writestr(name,data)
assert count==3,count
print('HYPERLINK labels cached: 3; formulas retained')
