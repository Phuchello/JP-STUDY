from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[2];P=R/'FINAL_PHASE3/JLPT_PRACTICE';T=R/'tmp/jlpt-phase3'
p=P/'app.js';s=p.read_text(encoding='utf-8');s=s.replace("function role(rid){view='role';", "function role(rid){if(location.hash!=='#role/'+rid){location.hash='role/'+rid;return;}view='role';")
s=s.replace("else if(v==='keys')keys();", "else if(v==='keys')keys();else if(v==='role')role(id);")
# The tutor package carries the newly added pattern/template tags.
p.write_text(s,encoding='utf-8');p=P/'engine.js';s=p.read_text(encoding='utf-8');s=s.replace("questionId:q.id,origin:q.origin,question:q.stem", "questionId:q.id,patternId:q.patternId,relatedTemplate:q.relatedTemplate,origin:q.origin,question:q.stem")
s=s.replace("const max=mode==='deep'?18:10", "const max=mode==='deep'?20:10")
s=s.replace("if(s.answered>=3){p+=", "if(s.eligible>=3&&s.eligibleCorrect/s.eligible<.6)p+=8;\n   if(s.answered>=3){p+=")
s=s.replace("obj.sessions.forEach(sessionCheck);if(obj.active)", "for(const k of ['sessions','exposures','speaking']){const arr=obj[k]||[];if(new Set(arr.map(x=>x.id)).size!==arr.length)throw Error('ID trùng trong '+k);}\n  obj.sessions.forEach(sessionCheck);if(obj.active)")
p.write_text(s,encoding='utf-8')
for f in ['research_fetch2.json','research_addendum_fetch.json']:
 x=(T/f).read_text(encoding='utf-8');print(f,[(x[max(0,m.start()-60):m.start()+100]) for m in list(re.finditer(r'2021 Nov|2022 Jan|2021-11|2022-01|Published online',x))[:8]])
