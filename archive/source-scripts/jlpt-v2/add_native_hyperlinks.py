"""Supply native hyperlinks and validation alerts absent from the authoring surface."""
from pathlib import Path
import json,zipfile,posixpath
from lxml import etree as ET

root=Path(__file__).resolve().parents[2]
target=root/'FINAL/JLPT_PROGRESS_TRACKER_v2.xlsx'
links=json.loads((root/'tmp/jlpt-v2/native_links.json').read_text(encoding='utf-8'))
S='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
P='http://schemas.openxmlformats.org/package/2006/relationships'
ns={'s':S,'r':R,'p':P}
with zipfile.ZipFile(target) as z:files={n:z.read(n) for n in z.namelist()}
book=ET.fromstring(files['xl/workbook.xml'])
rels=ET.fromstring(files['xl/_rels/workbook.xml.rels'])
targets={x.get('Id'):x.get('Target') for x in rels}
byname={x.get('name'):posixpath.normpath(posixpath.join('xl',targets[x.get('{'+R+'}id')])) for x in book.find('s:sheets',ns)}
byname={k:v.lstrip('/') for k,v in byname.items()}
validation_count=0
for fname in [n for n in files if n.startswith('xl/worksheets/sheet') and n.endswith('.xml')]:
    s=ET.fromstring(files[fname])
    for dv in s.findall('.//s:dataValidation',ns):
        dv.set('showErrorMessage','1');dv.set('errorStyle','stop');dv.set('allowBlank','1')
        dv.set('errorTitle','Giá trị chưa hợp lệ')
        dv.set('error','Nhập đúng phạm vi hoặc lựa chọn của ô; để trống khi chưa có dữ liệu.')
        validation_count+=1
    files[fname]=ET.tostring(s,xml_declaration=True,encoding='UTF-8',standalone=True)
for name in sorted({x['sheet'] for x in links}):
    fname=byname[name]
    if fname.startswith('xl/xl/'):fname=fname[3:]
    if fname not in files:raise ValueError(fname)
    sheet=ET.fromstring(files[fname])
    parent=sheet.find('s:hyperlinks',ns)
    if parent is None:
        parent=ET.Element('{'+S+'}hyperlinks')
        after={'printOptions','pageMargins','pageSetup','headerFooter','rowBreaks','colBreaks','customProperties','cellWatches','ignoredErrors','smartTags','drawing','legacyDrawing','legacyDrawingHF','picture','oleObjects','controls','webPublishItems','tableParts','extLst'}
        i=next((i for i,x in enumerate(sheet) if ET.QName(x).localname in after),len(sheet))
        sheet.insert(i,parent)
    relname=posixpath.dirname(fname)+'/_rels/'+posixpath.basename(fname)+'.rels'
    sr=ET.fromstring(files[relname]) if relname in files else ET.Element('{'+P+'}Relationships',nsmap={None:P})
    used={x.get('Id') for x in sr};n=1
    for item in [x for x in links if x['sheet']==name]:
        for old in list(parent):
            if old.get('ref')==item['address']:parent.remove(old)
        h=ET.SubElement(parent,'{'+S+'}hyperlink',ref=item['address'],display=item['label'])
        if item['url'].startswith('#'):h.set('location',item['url'][1:])
        else:
            while 'rIdJLPT'+str(n) in used:n+=1
            rid='rIdJLPT'+str(n);used.add(rid)
            h.set('{'+R+'}id',rid)
            ET.SubElement(sr,'{'+P+'}Relationship',Id=rid,Type=R+'/hyperlink',Target=item['url'],TargetMode='External')
    files[fname]=ET.tostring(sheet,xml_declaration=True,encoding='UTF-8',standalone=True)
    files[relname]=ET.tostring(sr,xml_declaration=True,encoding='UTF-8',standalone=True)
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
    for name,data in files.items():z.writestr(name,data)
print(json.dumps({'native_hyperlinks':len(links),'validation_alerts':validation_count,'sheets':sorted({x['sheet'] for x in links})},ensure_ascii=False))
