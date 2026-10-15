from pathlib import Path
import json
R=Path(__file__).resolve().parents[2];O=R/'FINAL_PHASE3';P=O/'JLPT_PRACTICE';T=R/'tmp/jlpt-phase3';lp=O/'JAPANESE_PATTERN_LIBRARY/patterns.json';lib=json.loads(lp.read_text(encoding='utf-8'))
for p in lib['patterns']:
 if p['id'] in ['T03','T04','T05','T08','T10','T11']:p['formula']=p['template']
 if p['id'] in ['G06','T11']:p['typicalMisunderstanding']=p['commonMistake']
lp.write_text(json.dumps(lib,ensure_ascii=False,indent=2),encoding='utf-8');(P/'patterns.js').write_text('window.PatternLibrary='+json.dumps(lib,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
p=P/'app.js';s=p.read_text(encoding='utf-8');s=s.replace('Ôn từ trong câu rồi tự gọi lại từ trước khi nhìn lựa chọn.','Đọc lại giải thích và nguồn của câu, rồi tự đổi một chi tiết.')
s=s.replace('<p>Nền cần: ${esc(q.prerequisites.join(\'; \'))}</p>', '<p>Nền cần: ${esc(q.prerequisites.join(\'; \'))}</p><p><small>Nguồn khái niệm: ${q.references.map(r=>`<a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(r.title)}</a>`).join(\' · \')}</small></p>')
s=s.replace("const ids=B.questions.filter(q=>q.patternId===p.id).map(q=>q.id).slice(0,5);", "const cs=E.summary(state,B).concepts,ids=B.questions.filter(q=>q.patternId===p.id&&(q.categoryCode!=='LISTEN'||voices.length>0)&&(!q.holdout||cs[q.conceptId].firstStudyAt&&Date.now()-Date.parse(cs[q.conceptId].firstStudyAt)>=3*E.DAY&&cs[q.conceptId].answered>=2)).sort((a,b)=>(E.prior(state,a).item?1:0)-(E.prior(state,b).item?1:0)).map(q=>q.id).slice(0,5);")
p.write_text(s,encoding='utf-8')
template=(T/'index_template.html').read_text(encoding='utf-8').replace('<link rel="stylesheet" href="styles.css">','<style>'+(P/'styles.css').read_text(encoding='utf-8')+'</style>')
for name in ['bank.js','patterns.js','engine.js','app.js']:template=template.replace('<script src="'+name+'"></script>','<script>'+(P/name).read_text(encoding='utf-8').replace('</script','<\\/script')+'</script>')
(P/'index.html').write_text(template,encoding='utf-8');print('Formula and metadata synchronized; library practice respects held-out items')
