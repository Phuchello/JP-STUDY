from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/'FINAL_PHASE3/JLPT_PRACTICE';T=R/'tmp/jlpt-phase3'
p=P/'app.js';s=p.read_text(encoding='utf-8');s=s.replace("if(state.active&&v!=='practice')save();", "if(state.active&&view==='practice'&&v!=='practice'){tick();state.active.interrupted=true;save();}if(state.active&&!state.active.training&&['keys','library'].includes(v)){location.hash='practice';setTimeout(()=>notice('Hãy nộp phần đã làm trước khi xem mẫu/khóa; lượt đo không có gợi ý.'),0);return;}if(state.active&&state.active.training&&['keys','library'].includes(v)){const it=state.active.items[state.active.index];if(it?.presentedAt&&!it.locked)E.assist(state,v==='keys'?'answer-key':'worked-example');save();}")
p.write_text(s,encoding='utf-8')
template=(T/'index_template.html').read_text(encoding='utf-8').replace('<link rel="stylesheet" href="styles.css">','<style>'+(P/'styles.css').read_text(encoding='utf-8')+'</style>')
for name in ['bank.js','patterns.js','engine.js','app.js']:template=template.replace('<script src="'+name+'"></script>','<script>'+(P/name).read_text(encoding='utf-8').replace('</script','<\\/script')+'</script>')
(P/'index.html').write_text(template,encoding='utf-8')
