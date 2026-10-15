from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[2];P=R/'FINAL_PHASE3/JLPT_PRACTICE';T=R/'tmp/jlpt-phase3'
p=P/'engine.js';s=p.read_text(encoding='utf-8')
s=s.replace('locked:false,audioPlays:0','locked:false,audioPlays:0,isListening:q.categoryCode===\'LISTEN\',firstListen:null')
s=s.replace("if(!s.training&&['hint'", "if(it.isListening&&it.audioPlays===1&&['transcript','replayed-audio'].includes(kind)&&!it.firstListen)it.firstListen={answer:it.answer,capturedAt:iso(),assistance:[...it.assistance]};if(!s.training&&['hint'")
s=s.replace("const q=question(bank,it.questionId);if(q.categoryCode==='LISTEN'", "const q=question(bank,it.questionId);if(q.audio&&it.audioPlays>1&&!it.assistance.includes('replayed-audio'))it.assistance.push('replayed-audio');if(q.categoryCode==='LISTEN'")
s=s.replace("correctAnswer:q.correctAnswer,...r,assistance", "correctAnswer:q.correctAnswer,...r,audioPlays:it.audioPlays,firstListen:q.audio?(it.firstListen?{...clone(it.firstListen),...score(q,it.firstListen.answer)}:it.audioPlays===1&&!it.assistance.some(x=>['transcript','replayed-audio','no-audio'].includes(x))?{answer:it.answer,...r,capturedAt:iso(now),assistance:[...it.assistance]}:null):null,assistance")
p.write_text(s,encoding='utf-8')
p=P/'app.js';s=p.read_text(encoding='utf-8');s=s.replace("${q.evidence?`<p>Bằng chứng:","${a.firstListen?`<p>Lượt nghe đầu trước hỗ trợ: ${esc(a.firstListen.answer||'trống')} · ${a.firstListen.attempted?(a.firstListen.correct?'đúng':'sai'):'chưa đáp'}. Điều kiện trợ giúp khi đó: ${esc(a.firstListen.assistance?.join(', ')||'không ghi trợ giúp')}.</p>`:''}${q.evidence?`<p>Bằng chứng:")
# Explicitly display successful role save in the role view; progress JSON retains records.
p.write_text(s,encoding='utf-8')
# Keep the working external-script template out of the learner's package; deliver one self-contained entry file.
template=T/'index_template.html'
if not template.exists():template.write_text((P/'index.html').read_text(encoding='utf-8'),encoding='utf-8')
s=template.read_text(encoding='utf-8');s=s.replace('<link rel="stylesheet" href="styles.css">','<style>'+ (P/'styles.css').read_text(encoding='utf-8')+'</style>')
for name in ['bank.js','patterns.js','engine.js','app.js']:s=s.replace('<script src="'+name+'"></script>','<script>'+ (P/name).read_text(encoding='utf-8').replace('</script','<\\/script')+'</script>')
(P/'index.html').write_text(s,encoding='utf-8')
print('Single-file entry built; no network dependencies for text practice')
