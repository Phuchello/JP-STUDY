"""Validate the public snapshot. Writes results only under ignored tmp/."""
from pathlib import Path
from xml.etree import ElementTree as ET
from urllib.parse import unquote,urlsplit
import json,hashlib,re,zipfile,os
from update_manifest import files
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'tmp';OUT.mkdir(exist_ok=True);checks=[]
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(name,ok,detail=None):
    checks.append({'name':name,'ok':bool(ok),**({'detail':detail} if detail else {})})
def main():
    D=ROOT/'deliverables/phase3';A=D/'JLPT_PRACTICE';b=load('deliverables/phase3/JLPT_PRACTICE/question_bank.json');lib=load('deliverables/phase3/JAPANESE_PATTERN_LIBRARY/patterns.json');keys=load('deliverables/phase3/ANSWER_KEY_AND_EXPLANATIONS/validated_keys.json');schema=load('deliverables/phase3/JLPT_PRACTICE/question.schema.json');review=load('deliverables/phase3/ANSWER_KEY_AND_EXPLANATIONS/content_final_reaudit.json')
    ck('80 questions + 4 roles + 30 reuse recipes',len(b['questions'])==80 and len(b['roleplays'])==4 and len(b['recipes'])==30)
    pids={p['id'] for p in lib['patterns']};ck('31 patterns and 37 instructional examples',len(pids)==31 and sum(len(p.get('practice',[])) for p in lib['patterns'])==37)
    ck('Stable unique question IDs',len({q['id'] for q in b['questions']+b['roleplays']})==84)
    ck('Required schema fields and pattern mappings',all(all(k in q for k in schema['required']) and (not q['patternId'] or q['patternId'] in pids) and (not q['relatedTemplate'] or q['relatedTemplate'] in pids) for q in b['questions']))
    digest=hashlib.sha256(json.dumps([(q['id'],q['correctAnswer']) for q in b['questions']],ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
    ck('Digest and all 80 key/explanation mappings',digest==b['answerKeyDigest']==keys['answerKeyDigest'] and len(keys['questions'])==80 and all(k['id']==q['id'] and k['correctAnswer']==q['correctAnswer'] and k['distractorExplanations']==q['distractorExplanations'] for k,q in zip(keys['questions'],b['questions'])))
    ck('Independent final QA fingerprints retained',review['decision']=='PASS_FOR_LIMITED_PILOT' and all(sha(ROOT/x['Path'])==x['Hash'].lower() for x in review['verifiedFiles']))
    ck('JSON equals browser JS resources',json.loads((A/'bank.js').read_text(encoding='utf-8')[len('window.PracticeBank='):-2])==b and json.loads((A/'patterns.js').read_text(encoding='utf-8')[len('window.PatternLibrary='):-2])==lib)
    entry=(A/'index.html').read_text(encoding='utf-8');ck('Offline HTML embeds current resources',all((A/n).read_text(encoding='utf-8').replace('</script','<\\/script') in entry for n in ['bank.js','patterns.js','engine.js','app.js']) and '<script src=' not in entry)
    current=load('MANIFEST.json');actual={p.relative_to(ROOT).as_posix():p for p in files() if p.name!='MANIFEST.json'}
    ck('Manifest covers every public file',set(actual)=={r['path'] for r in current['files']})
    ck('All manifest sizes and SHA-256 match',all(actual.get(r['path']) and actual[r['path']].stat().st_size==r['bytes'] and sha(actual[r['path']])==r['sha256'] for r in current['files']))
    ck('All statuses explicit',all(r['status'] in ['DRAFT','QA_PENDING','VERIFIED'] for r in current['files']))
    ck('No file >= 50 MiB',all(p.stat().st_size<50*1024**2 for p in actual.values()))
    binaries=[p for p in actual.values() if p.suffix in ['.pdf','.xlsx']];ck('No duplicate PDF/XLSX payloads',len(binaries)==len({sha(p) for p in binaries}))
    forbidden=[n for n in actual if n.endswith(('.zip','.exe','.pem','.key','.p12','.pfx')) or Path(n).name.startswith('.env') or 'node_modules/' in n or n.startswith(('private/','personal/','learner-data/'))];ck('No forbidden artifacts',not forbidden,forbidden)
    # Heuristic only: supplements manual review, does not prove arbitrary PII absence.
    bad=[];patterns=[r'gh[pousr]_[A-Za-z0-9]{25,}',r'github_pat_[A-Za-z0-9_]{30,}',r'sk-[A-Za-z0-9]{25,}',r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY',r'C:[/\\]+Users[/\\]+',r'sinh năm 2003',r'柏木実業専門学校',r'60 mấy điểm',r'6:30',r'18 tháng']
    for n,p in actual.items():
        if p.suffix in ['.pdf','.xlsx','.mp3']:continue
        text=p.read_text(encoding='utf-8-sig')
        # The scanner source itself contains banned examples, not user data.
        if n=='scripts/validate_release.py':continue
        if any(re.search(x,text) for x in patterns):bad.append(n)
    ck('Secret/private-profile heuristic scan',not bad,bad)
    broken=[]
    for n,p in actual.items():
        if p.suffix!='.md':continue
        text=p.read_text(encoding='utf-8')
        for target in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^\n)]+)\)',text):
            target=target.strip().strip('<>');parts=urlsplit(target)
            if parts.scheme or target.startswith('#'):continue
            if not (p.parent/unquote(parts.path)).exists():broken.append({'file':n,'target':target})
    ck('All relative Markdown link targets exist',not broken,broken)
    ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'};wb_stats=[]
    for p in [p for p in binaries if p.suffix=='.xlsx']:
        with zipfile.ZipFile(p) as z:
            wb=ET.fromstring(z.read('xl/workbook.xml'));raw='\n'.join(z.read(n).decode('utf-8') for n in z.namelist() if n.endswith('.xml'))
            wb_stats.append({'path':p.relative_to(ROOT).as_posix(),'sheets':len(wb.findall('s:sheets/s:sheet',ns)),'bytes':p.stat().st_size})
            ck('Workbook package privacy '+p.name,not any(re.search(x,raw) for x in patterns))
    ck('Original four tracker checkpoints retained',len([x for x in wb_stats if x['path'].startswith('archive/') or x['path'].startswith('deliverables/phase3/')])==4)
    if (ROOT/'DRIVE_SETUP/JP_STUDY_HOC_HOM_NAY.xlsx').exists():ck('Drive-first template has five tabs',any(x['path']=='DRIVE_SETUP/JP_STUDY_HOC_HOM_NAY.xlsx' and x['sheets']==5 for x in wb_stats))
    with zipfile.ZipFile(D/'JLPT_PROGRESS_TRACKER.xlsx') as z:
        sh=ET.fromstring(z.read('xl/worksheets/phase3_practice.xml'));cells=[c for c in sh.findall('.//s:c',ns) if re.match(r'^[A-L](?:[8-9]|[1-9]\d|[1-4]\d\d|50[0-7])$',c.get('r',''))]
        ck('Current tracker import area has no learner rows',all(c.find('s:v',ns) is None and c.find('s:is',ns) is None for c in cells))
    inv=load('qa/source_inventory.json');ck('All 299 source files classified',len(inv['files'])==299 and all(x.get('disposition') and x.get('sha256') and x.get('status') in ['DRAFT','QA_PENDING','VERIFIED'] for x in inv['files']))
    for n in ['engine_tests.json','browser_tests.json','edge_flow_tests.json']:
        result=load('qa/current/'+n);tests=result if isinstance(result,list) else result['tests'];ck('Current rerun passes '+n,all(x['ok'] for x in tests))
    report={'snapshotDate':'2026-10-15','checks':checks,'passed':sum(x['ok'] for x in checks),'failed':sum(not x['ok'] for x in checks),'workbooks':wb_stats,'publicFileCount':len(actual)+1,'publicBytesIncludingManifest':sum(p.stat().st_size for p in actual.values())+(ROOT/'MANIFEST.json').stat().st_size}
    (OUT/'publication_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'checks':len(checks),'passed':report['passed'],'failures':[x for x in checks if not x['ok']],'files':report['publicFileCount'],'bytes':report['publicBytesIncludingManifest']},ensure_ascii=False))
    return 1 if report['failed'] else 0
if __name__=='__main__':raise SystemExit(main())
