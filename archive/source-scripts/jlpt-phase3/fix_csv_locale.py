from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/'FINAL_PHASE3/JLPT_PRACTICE';T=R/'tmp/jlpt-phase3'
p=P/'engine.js';s=p.read_text(encoding='utf-8').replace("'Phút làm','Trợ giúp'","'Giây làm','Trợ giúp'").replace('Math.round(g.seconds/60*100)/100','Math.round(g.seconds)');p.write_text(s,encoding='utf-8')
p=T/'build_tracker.mjs';s=p.read_text(encoding='utf-8').replace("'Phút làm','Trợ giúp'","'Giây làm','Trợ giúp'").replace('=SUMIF(M8:M507,"Hợp lệ",J8:J507)','=SUMIF(M8:M507,"Hợp lệ",J8:J507)/60').replace("3,4,5,2,'','fixture'","3,4,5,120,'','fixture'");s=s.replace("check('Numerator','C2',3);","check('Numerator','C2',3);check('Seconds converted to minutes','K2',2);");p.write_text(s,encoding='utf-8')
template=(T/'index_template.html').read_text(encoding='utf-8').replace('<link rel="stylesheet" href="styles.css">','<style>'+(P/'styles.css').read_text(encoding='utf-8')+'</style>')
for name in ['bank.js','patterns.js','engine.js','app.js']:template=template.replace('<script src="'+name+'"></script>','<script>'+(P/name).read_text(encoding='utf-8').replace('</script','<\\/script')+'</script>')
(P/'index.html').write_text(template,encoding='utf-8')
