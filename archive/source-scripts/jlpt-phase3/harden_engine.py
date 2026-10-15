from pathlib import Path
p=Path(__file__).resolve().parents[2]/'FINAL_PHASE3/JLPT_PRACTICE/engine.js'
s=p.read_text(encoding='utf-8')
s=s.replace('reflections:{},active:null','reflections:{},speaking:[],active:null')
s=s.replace("if(tired||mode==='review')pool", "const recipe=recipeId&&bank.recipes?.find(r=>r.id===recipeId);if(recipe)pool=pool.filter(q=>recipe.questionIds.includes(q.id));\n  if(tired||mode==='review')pool")
s=s.replace("const recipe=recipeId&&bank.recipes?.find(r=>r.id===recipeId);if(recipe){pool=pool.filter(q=>recipe.questionIds.includes(q.id));reason='Bộ ghép cố định từ ngân hàng, vẫn tách câu mới và đã thấy.';}", "if(recipe)reason='Bộ ghép từ ngân hàng; câu đã thấy vẫn tính ôn.';")
s=s.replace("return p-order.indexOf(c)/100;", "if(s.seconds.length>=3){const med=[...s.seconds].sort((a,b)=>a-b)[Math.floor(s.seconds.length/2)],expected=qs.reduce((n,q)=>n+q.estimatedSeconds,0)/(qs.length||1);if(med>expected*1.5)p+=4;}\n   return p-order.indexOf(c)/100;")
s=s.replace("ranked.find(c=>pool.filter(q=>q.conceptId===c).length>=3)||ranked[0]", "ranked.find(c=>pool.filter(q=>q.conceptId===c&&q.estimatedSeconds<=75).length>=3)||ranked.find(c=>pool.some(q=>q.conceptId===c&&q.estimatedSeconds<=75))")
s=s.replace("candidates.slice(0,tired?3:4).forEach(add);", "[...new Map(candidates.map(q=>[q.id,q])).values()].slice(0,tired?3:4).forEach(add);")
s=s.replace("if(!chosen.length){pool.filter(q=>q.conceptId===c).slice(0,3).forEach(add);reason+=' Bài đọc dài có thể cần thêm thời gian; được dừng bất cứ lúc nào.';}", "if(!chosen.length)return {blocked:true,ids:[],reason:'Không còn câu ngắn phù hợp; hãy chọn STANDARD khi đủ sức hoặc nghỉ.'};")
s=s.replace("bank.concepts[c].title", "bank.concepts[c]?.title")
s=s.replace("const q=question(bank,it.questionId),r=score(q,it.answer);if(r.status", "const q=question(bank,it.questionId);if(q.categoryCode==='LISTEN'&&it.audioPlays<1&&!it.assistance.includes('no-audio'))it.assistance.push('no-audio');const r=score(q,it.answer);if(r.status")
s=s.replace("Math.min(14,last.reviewIntervalDays*2)", "last.reviewIntervalDays>=7?14:7")
s=s.replace("const a=makeAttempt(state,bank,s,it,now);if(!state.attempts", "if(it.locked)return state.attempts.find(a=>a.id===s.id+':'+it.questionId);const a=makeAttempt(state,bank,s,it,now);if(!state.attempts")
s=s.replace("const enc=v=>'\"'+String(v??'').replaceAll", "const enc=v=>'\"'+String(typeof v==='string'&&/^[=+@-]/.test(v)?\"'\"+v:v??'').replaceAll")
s=s.replace("for(const e of obj.exposures)if(!bank.questions.some(q=>q.id===e.questionId)||!validDate(e.at)||typeof e.id!=='string'||e.id.length>180)", "for(const e of obj.exposures)if(!bank.questions.some(q=>q.id===e.questionId&&q.stimulusId===e.stimulusId)||!validDate(e.at)||typeof e.id!=='string'||e.id.length>180)")
s=s.replace("return true;\n }\n function merge", """const safeId=x=>typeof x==='string'&&/^[A-Za-z0-9_:-]{1,180}$/.test(x);
  const sessionCheck=s=>{if(!s||!safeId(s.id)||!MODES[s.mode]||typeof s.training!=='boolean'||!validDate(s.startedAt)||!Array.isArray(s.items)||s.items.length>30||!Number.isInteger(s.index)||s.index<0||s.index>=s.items.length)throw Error('Buổi làm không hợp lệ.');for(const it of s.items){question(bank,it.questionId);if(score(question(bank,it.questionId),it.answer).status==='invalid'||!Array.isArray(it.assistance)||it.assistance.some(x=>!ASSIST.includes(x))||!Array.isArray(it.answerChanges)||it.answerChanges.length>1000||!Number.isFinite(it.activeSeconds)||it.activeSeconds<0||it.activeSeconds>86400||typeof it.guessed!=='boolean'||typeof it.isItemNew!=='boolean'||typeof it.isStimulusNew!=='boolean'||!Number.isInteger(it.audioPlays)||it.audioPlays<0||it.audioPlays>1000||it.presentedAt&&!validDate(it.presentedAt))throw Error('Câu trong buổi dở không hợp lệ.');}};
  for(const a of obj.attempts)if(!safeId(a.sessionId)||!safeId(a.id)||!MODES[a.mode]||a.correctAnswer!==question(bank,a.questionId).correctAnswer||['guessed','isItemNew','isStimulusNew','interrupted','overTime'].some(k=>typeof a[k]!=='boolean'))throw Error('Lượt làm thiếu cờ hoặc khóa không đúng.');
  obj.sessions.forEach(sessionCheck);if(obj.active)sessionCheck(obj.active);
  if(obj.speaking!==undefined&&(!Array.isArray(obj.speaking)||obj.speaking.length>20000||obj.speaking.some(r=>!safeId(r.id)||!bank.roleplays.some(x=>x.id===r.roleId)||!validDate(r.at)||!Array.isArray(r.intents)||r.intents.length!==4||r.intents.some(x=>!['0','1','?'].includes(x)))))throw Error('Phiếu nói không hợp lệ.');
  if(obj.reflections!==undefined&&(!obj.reflections||typeof obj.reflections!=='object'||Array.isArray(obj.reflections)||Object.keys(obj.reflections).length>20000))throw Error('Phản hồi không hợp lệ.');
  return true;
 }
 function merge""")
s=s.replace("['attempts','exposures','sessions'])", "['attempts','exposures','sessions','speaking'])")
s=s.replace("out[key].map(x=>[x.id,x])", "(out[key]||[]).map(x=>[x.id,x])")
s=s.replace("for(const x of incoming[key])", "for(const x of incoming[key]||[])")
s=s.replace("out.updatedAt=iso();return out;", """if(incoming.active&&!out.sessions.some(s=>s.id===incoming.active.id)){if(out.active&&JSON.stringify(out.active)!==JSON.stringify(incoming.active))throw Error('Hai buổi dở khác nhau. Nộp phần hiện tại rồi nhập bản sao.');if(!out.active){out.active=clone(incoming.active);out.active.interrupted=true;}}
  if(out.active&&out.sessions.some(s=>s.id===out.active.id))out.active=null;
  out.reflections={...incoming.reflections,...out.reflections};out.updatedAt=iso();return out;""")
p.write_text(s,encoding='utf-8')
