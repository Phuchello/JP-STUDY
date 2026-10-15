"""Regenerate the public file index and SHA-256 manifest (no runtime dependencies)."""
from pathlib import Path
import json,hashlib,os
from urllib.parse import quote
ROOT=Path(__file__).resolve().parents[1]
SKIP={'.git','node_modules','tmp','__pycache__'}
def files():
    out=[]
    for base,dirs,names in os.walk(ROOT,followlinks=False):
        dirs[:]=[d for d in dirs if d not in SKIP and not (Path(base)/d).is_symlink() and not (hasattr(Path(base)/d,'is_junction') and (Path(base)/d).is_junction())]
        out.extend(Path(base)/n for n in names if not n.endswith('.pyc'))
    return sorted(out)
def status(path):
    if path.startswith('archive/source-scripts/') or path.endswith('INSTRUCTIONAL_DESIGN.md'):return 'DRAFT'
    # New/unreviewed files must never silently inherit VERIFIED.
    registry=ROOT/'qa/file_status.json'
    known=json.loads(registry.read_text(encoding='utf-8')) if registry.exists() else {}
    return known.get(path,'QA_PENDING')
def main():
    paths={p.relative_to(ROOT).as_posix() for p in files()}|{'FILE_INDEX.md','MANIFEST.json'}
    lines=['# File index','', 'Snapshot 2026-10-15. VERIFIED is scoped verification, not JLPT certification. Historical QA describes its original checkpoint; DRAFT source scripts are not supported release commands. New files default to QA_PENDING until reviewed in qa/file_status.json.','', '| File | Status |','|---|---|']
    lines += ['| ['+x+']('+quote(x,safe='/')+') | '+status(x)+' |' for x in sorted(paths)]
    (ROOT/'FILE_INDEX.md').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
    rows=[]
    for p in files():
        name=p.relative_to(ROOT).as_posix()
        if name=='MANIFEST.json':continue
        data=p.read_bytes();rows.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'status':status(name)})
    doc={'snapshotDate':'2026-10-15','scope':'Public repository files, excluding this manifest itself; no .git/dependencies/tmp','fileCountExcludingManifest':len(rows),'totalBytesExcludingManifest':sum(x['bytes'] for x in rows),'files':rows}
    (ROOT/'MANIFEST.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'filesIncludingManifest':len(rows)+1,'bytesIncludingManifest':sum(x['bytes'] for x in rows)+(ROOT/'MANIFEST.json').stat().st_size}))
if __name__=='__main__':main()
