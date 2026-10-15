from pathlib import Path
p=Path(__file__).resolve().parent/'test_edge_flows.cjs';s=p.read_text(encoding='utf-8').replace('const a=await audio.newPage()','let a=await audio.newPage()').replace("await a.goto(url+'#practice');await a.reload();", "a=await audio.newPage();await a.goto(url+'#practice');");p.write_text(s,encoding='utf-8')
R=Path(__file__).resolve().parents[2];P=R/'FINAL_PHASE3/JLPT_PRACTICE';p=P/'engine.js';s=p.read_text(encoding='utf-8').replace("out.attempts.sort((a,b)=>a.answeredAt.localeCompare(b.answeredAt));", "out.sessions.sort((a,b)=>a.startedAt.localeCompare(b.startedAt));out.attempts.sort((a,b)=>a.answeredAt.localeCompare(b.answeredAt));");p.write_text(s,encoding='utf-8')
template=(Path(__file__).resolve().parent/'index_template.html').read_text(encoding='utf-8').replace('<link rel="stylesheet" href="styles.css">','<style>'+(P/'styles.css').read_text(encoding='utf-8')+'</style>')
for name in ['bank.js','patterns.js','engine.js','app.js']:template=template.replace('<script src="'+name+'"></script>','<script>'+(P/name).read_text(encoding='utf-8').replace('</script','<\\/script')+'</script>')
(P/'index.html').write_text(template,encoding='utf-8')
