from pathlib import Path
import hashlib,json,re,importlib.util
R=Path(__file__).resolve().parents[2];T=R/'tmp/jlpt-phase3';O=R/'FINAL_PHASE3'
for p in [O,O/'JLPT_PRACTICE',O/'ANSWER_KEY_AND_EXPLANATIONS']:p.mkdir(exist_ok=True,parents=True)
files=[p for d in [R/'outputs/jlpt-2026',R/'FINAL',R/'FINAL_V3'] for p in d.iterdir() if p.is_file()]
hashes={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(T/'source_hashes.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2),encoding='utf-8')
rows=[]
for p in sorted(T.glob('research_pass*.json')):
 for q in json.loads(p.read_text(encoding='utf-8')):
  s='\n'.join(c['text'] for c in q['result']['content'] if c['type']=='text');urls=re.findall(r'^URL: (\S+)',s,re.M)
  rows.append({'workstream':q['id'],'requested':q['requested'],'returned_urls':len(urls),'urls':urls})
allurls=[u for r in rows for u in r['urls']]
stats={'queries':len(rows),'requested_results':sum(r['requested'] for r in rows),'returned_results':len(allurls),'unique_urls':len(set(allurls)),'rows':rows}
(T/'search_coverage.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in stats.items() if k!='rows'}));print('Preserved input snapshots:',len(hashes))
