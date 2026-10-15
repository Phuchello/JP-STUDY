(function(root,factory){const api=factory();if(typeof module==='object'&&module.exports)module.exports=api;else root.JLPT=api;})(typeof globalThis!=='undefined'?globalThis:this,function(){
 'use strict';
 const VERSION='1.0.0',SCHEMA=1,DAY=86400000;
 const ASSIST=['hint','transcript','replayed-audio','no-audio','gemini','answer-key','worked-example'];
 const MODES={quick:{label:'QUICK',minutes:5,min:3,max:5,training:true},standard:{label:'STANDARD',minutes:15,min:8,max:12,training:false},deep:{label:'DEEP',minutes:30,min:12,max:20,training:false},review:{label:'Ôn lỗi',minutes:5,min:3,max:5,training:true}};
 function id(){return typeof crypto!=='undefined'&&crypto.randomUUID?crypto.randomUUID():'s-'+Date.now().toString(36)+'-'+Math.random().toString(36).slice(2);}
 function iso(now){return new Date(now===undefined?Date.now():now).toISOString();}
 function localDate(now){const d=new Date(now===undefined?Date.now():now);return [d.getFullYear(),String(d.getMonth()+1).padStart(2,'0'),String(d.getDate()).padStart(2,'0')].join('-');}
 function fresh(bank){return {schemaVersion:SCHEMA,appVersion:VERSION,bankVersion:bank.bankVersion,answerKeyDigest:bank.answerKeyDigest,attempts:[],exposures:[],sessions:[],diagnostics:[],reflections:{},speaking:[],active:null,createdAt:iso(),updatedAt:iso()};}
 function clone(v){return JSON.parse(JSON.stringify(v));}
 function question(bank,qid){const q=bank.questions.find(q=>q.id===qid);if(!q)throw Error('Mã câu không có trong ngân hàng: '+qid);return q;}
 function score(q,a){
  if(a===null||a===undefined||a==='')return {status:'unanswered',attempted:false,correct:null};
  if(typeof a!=='string'||!q.options.some(o=>o.id===a))return {status:'invalid',attempted:false,correct:null};
  return {status:a===q.correctAnswer?'correct':'incorrect',attempted:true,correct:a===q.correctAnswer};
 }
 function checkBank(bank){
  if(!bank||!Array.isArray(bank.questions)||!bank.questions.length)throw Error('Ngân hàng trống.');
  const ids=new Set(),stems=new Set();
  for(const q of bank.questions){
   for(const k of ['id','level','categoryCode','conceptId','learningObjective','stem','correctAnswer','explanationVi','errorCategory','reviewRecommendation','origin'])if(typeof q[k]!=='string'||!q[k].trim())throw Error(q.id+': thiếu '+k);
   if(ids.has(q.id))throw Error('Trùng mã câu');ids.add(q.id);
   if(stems.has(q.stem+(q.passage||q.audio?.script||'')))throw Error('Trùng nội dung câu');stems.add(q.stem+(q.passage||q.audio?.script||''));
   if(!Array.isArray(q.options)||q.options.length<2||new Set(q.options.map(x=>x.id)).size!==q.options.length||new Set(q.options.map(x=>x.text)).size!==q.options.length)throw Error(q.id+': lựa chọn lỗi');
   if(!q.options.some(x=>x.id===q.correctAnswer))throw Error(q.id+': khóa không có trong lựa chọn');
   if(!q.prerequisites?.length||!q.references?.length||!q.estimatedSeconds)throw Error(q.id+': thiếu dữ liệu dạy học');
   for(const o of q.options)if(o.id!==q.correctAnswer&&!q.distractorExplanations?.[o.id])throw Error(q.id+': thiếu giải thích nhiễu');
   if(q.passage&&!q.evidence)throw Error(q.id+': thiếu bằng chứng đọc');
   if(q.categoryCode==='LISTEN'&&(!q.audio?.script||!q.evidence))throw Error(q.id+': thiếu kịch bản/khóa nghe');
  }return {questions:ids.size,roles:bank.roleplays?.length||0};
 }
 function prior(state,q){return {item:state.exposures.some(e=>e.questionId===q.id),stimulus:state.exposures.some(e=>e.stimulusId===q.stimulusId)};}
 function history(state,qid){return state.attempts.filter(a=>a.questionId===qid);}
 function due(state,qid,now){const h=history(state,qid),a=h[h.length-1];return !!a&&a.nextReviewAt&&Date.parse(a.nextReviewAt)<=(now===undefined?Date.now():now);}
 function status(state,q,now){
  const h=history(state,q.id),a=h[h.length-1];let label='Chưa làm';
  if(!a&&prior(state,q).item)label='Đã xem, chưa trả lời';
  if(a){if(!a.attempted)label='Đã xem, chưa trả lời';else if(!a.correct)label='Sai';else if(a.assistance.length)label='Đúng có trợ giúp';else if(!a.isItemNew||!a.isStimulusNew)label='Đúng khi ôn';else if(a.guessed)label='Đúng nhưng đã đoán';else label='Đúng tự làm';}
  return {label,due:due(state,q.id,now),last:a||null,seen:prior(state,q).item};
 }
 function conceptStats(state,bank){
  const out={};for(const [c,v]of Object.entries(bank.concepts))out[c]={id:c,title:v.title,answered:0,correct:0,assisted:0,guessed:0,wrong:0,eligible:0,eligibleCorrect:0,seconds:[],firstStudyAt:null};
  for(const a of state.attempts){const q=bank.questions.find(q=>q.id===a.questionId);if(!q)continue;const v=out[q.conceptId];if(a.attempted){v.answered++;v.correct+=a.correct?1:0;v.wrong+=a.correct?0:1;v.assisted+=a.assistance.length?1:0;v.guessed+=a.guessed?1:0;if(!v.firstStudyAt||a.answeredAt<v.firstStudyAt)v.firstStudyAt=a.answeredAt;if(a.activeSeconds>0&&!a.interrupted)v.seconds.push(a.activeSeconds);if(a.evidenceType==='independent-new'){v.eligible++;v.eligibleCorrect+=a.correct?1:0;}}}
  return out;
 }
 function select(state,bank,{mode='standard',fatigue=3,sleepy=false,audioAvailable=false,now=Date.now(),recipeId=null}={}){
  if(!MODES[mode])throw Error('Chế độ không hợp lệ.');
  if(!Number.isInteger(fatigue)||fatigue<1||fatigue>5)throw Error('Chọn mức mệt 1–5.');
  if(sleepy)return {rest:true,reason:'Đang buồn ngủ: nghỉ trước, không làm bài đo.',ids:[]};
  if(mode==='deep'&&fatigue>=3)return {rest:false,blocked:true,reason:'Hôm nay nên chọn 5–15 phút; buổi dài chỉ khi đủ sức.',ids:[]};
  const tired=fatigue>=4,training=MODES[mode].training||tired;
  let pool=bank.questions.filter(q=>q.level==='N4'&&q.validation.status==='reviewed'&&(q.categoryCode!=='LISTEN'||audioAvailable));
  const recipe=recipeId&&bank.recipes?.find(r=>r.id===recipeId);if(recipe)pool=pool.filter(q=>recipe.questionIds.includes(q.id));
  if(tired||mode==='review')pool=pool.filter(q=>prior(state,q).item);
  if(!pool.length)return {rest:tired,workedExample:tired,reason:tired?'Chưa có câu cũ để ôn. Hãy nghỉ, hoặc xem một mẫu có hướng dẫn.':'Chưa có câu phù hợp để ôn; có thể bắt đầu QUICK khi đủ sức.',ids:[]};
  const cs=conceptStats(state,bank),order=Object.keys(bank.concepts),recent={};for(const a of state.attempts)if(a.attempted){const q=bank.questions.find(q=>q.id===a.questionId);if(q)(recent[q.conceptId]||=[]).push(a);} 
  const priority=c=>{
   const s=cs[c],qs=pool.filter(q=>q.conceptId===c);let p=0;
   if(qs.some(q=>due(state,q.id,now)))p+=30;
   if(s.eligible>=3&&s.eligibleCorrect/s.eligible<.6)p+=8;
   if(s.answered>=3){const tail=(recent[c]||[]).slice(-4);p+=Math.min(20,tail.filter(a=>!a.correct).length*4)+Math.min(12,tail.filter(a=>a.assistance.length).length*3)+Math.min(8,tail.filter(a=>a.guessed).length*2);}
   if(!s.answered&&['particle-place','form-te','permission'].includes(c))p+=15;
   const ds=state.diagnostics.filter(d=>d.level==='N4'&&d.total>=5&&d.correct/d.total<.6&&d.assistance==='none');
   const code=bank.concepts[c].category,diagSkill=['PART','CONJ','GRAM','ORDER'].includes(code)?'Ngữ pháp':['INTERP','SHORT','MED'].includes(code)?'Đọc':code==='LISTEN'?'Nghe':code==='VOC'?'Từ và kanji':'Giao tiếp';if(ds.some(d=>d.skill===diagSkill))p+=20;
   if(s.seconds.length>=3){const med=[...s.seconds].sort((a,b)=>a-b)[Math.floor(s.seconds.length/2)],expected=qs.reduce((n,q)=>n+q.estimatedSeconds,0)/(qs.length||1);if(med>expected*1.5)p+=4;}
   return p-order.indexOf(c)/100;
  };
  const ranked=order.filter(c=>pool.some(q=>q.conceptId===c)).sort((a,b)=>priority(b)-priority(a));
  let reason='Chưa có đủ dữ liệu: bắt đầu từ cấu trúc nền N4.',chosen=[];
  const eligibleHoldout=q=>{const c=cs[q.conceptId];return !q.holdout||c.firstStudyAt&&now-Date.parse(c.firstStudyAt)>=3*DAY&&c.answered>=2;};
  const newItems=pool.filter(q=>!prior(state,q).item&&!prior(state,q).stimulus&&eligibleHoldout(q));
  const oldItems=pool.filter(q=>prior(state,q).item).sort((a,b)=>(due(state,b.id,now)?1:0)-(due(state,a.id,now)?1:0));
  if(recipe)reason='Bộ ghép từ ngân hàng; câu đã thấy vẫn tính ôn.';
  const add=q=>{if(q&&!chosen.some(x=>x.id===q.id)&&(!recipe||recipe.questionIds.includes(q.id)))chosen.push(q);};
  if(mode==='quick'||mode==='review'||tired){
   const c=ranked.find(c=>pool.filter(q=>q.conceptId===c&&q.estimatedSeconds<=75).length>=3)||ranked.find(c=>pool.some(q=>q.conceptId===c&&q.estimatedSeconds<=75));
   const candidates=(tired||mode==='review'?oldItems:[...oldItems.filter(q=>due(state,q.id,now)),...newItems,...oldItems]).filter(q=>q.conceptId===c&&q.estimatedSeconds<=75);
   [...new Map(candidates.map(q=>[q.id,q])).values()].slice(0,tired?3:4).forEach(add);
   reason=tired?'Mệt 4–5: chỉ ôn câu cũ tối đa 5 phút; nghỉ vẫn là lựa chọn phù hợp.':cs[c]?.wrong?'Mục tiêu có lỗi hoặc cần ôn: '+bank.concepts[c]?.title:'Một mục tiêu nền: '+bank.concepts[c]?.title;
   if(!chosen.length)return {blocked:true,ids:[],reason:'Không còn câu ngắn phù hợp; hãy chọn STANDARD khi đủ sức hoặc nghỉ.'};
  }else{
   const max=mode==='deep'?20:10;
   const sorted=[...newItems].sort((a,b)=>priority(b.conceptId)-priority(a.conceptId));
   const skillUse={};
   for(const code of (mode==='deep'?['MED','SHORT','VOC','LISTEN']:['SHORT','VOC','LISTEN'])){const q=sorted.find(q=>q.categoryCode===code);if(q){add(q);skillUse[code]=1;}}
   for(const q of sorted){if(chosen.length>=max-(oldItems.length?2:0))break;const skill=q.categoryCode;if((skillUse[skill]||0)>=3)continue;add(q);skillUse[skill]=(skillUse[skill]||0)+1;}
   oldItems.slice(0,2).forEach(add);
   if(chosen.length<Math.min(max,8))for(const q of [...sorted,...oldItems]){if(chosen.length>=max)break;add(q);}
   reason=newItems.length?'Ưu tiên câu chưa thấy ở nền N4, làm câu mới trước rồi ôn; chưa có điểm chuẩn hóa.':'Đã dùng hết câu mới phù hợp: phiên này là ôn, không chứng minh tiến bộ độc lập.';
  }
  if(recipe&&!chosen.length)recipe.questionIds.map(qid=>pool.find(q=>q.id===qid)).filter(Boolean).forEach(add);
  const budget=(mode==='deep'?30:mode==='standard'?15:5)*60;
  while(chosen.length>MODES[mode].min&&chosen.reduce((s,q)=>s+q.estimatedSeconds,0)>budget*.85)chosen.pop();
  if(!chosen.length)return {rest:false,blocked:true,ids:[],reason:'Không còn câu vừa thời gian trong mục tiêu này. Chọn ôn hoặc nghỉ.'};
  const sorted=training?chosen:chosen.sort((a,b)=>(prior(state,a).item?1:0)-(prior(state,b).item?1:0));
  return {rest:false,ids:sorted.map(q=>q.id),reason,training,mode:tired?'review':mode,fatigue,now,audioAvailable,estimatedSeconds:sorted.reduce((s,q)=>s+q.estimatedSeconds,0)};
 }
 function start(state,bank,selection,now){
  if(state.active)throw Error('Có buổi đang dở; tiếp tục hoặc nộp phần đã làm.');
  if(!selection.ids?.length)throw Error(selection.reason||'Chưa có câu để làm.');
  const at=iso(now),s={id:id(),mode:selection.mode,training:!!selection.training,reason:selection.reason,fatigue:selection.fatigue,startedAt:at,localDate:localDate(now),timezone:typeof Intl!=='undefined'?Intl.DateTimeFormat().resolvedOptions().timeZone:'unknown',index:0,interrupted:false,overTime:false,submitted:false,items:selection.ids.map(qid=>{const q=question(bank,qid),p=prior(state,q);return {questionId:qid,isItemNew:!p.item,isStimulusNew:!p.stimulus,presentedAt:null,answer:null,answerChanges:[],assistance:[],guessed:false,activeSeconds:0,locked:false,audioPlays:0,isListening:q.categoryCode==='LISTEN',firstListen:null};})};state.active=s;state.updatedAt=at;return s;
 }
 function present(state,bank,index,now){const s=state.active;if(!s||!s.items[index])throw Error('Không có câu đang làm.');s.index=index;const it=s.items[index],q=question(bank,it.questionId);if(!it.presentedAt){it.presentedAt=iso(now);state.exposures.push({id:s.id+':'+q.id,sessionId:s.id,questionId:q.id,stimulusId:q.stimulusId,at:it.presentedAt,kind:'practice'});}return it;}
 function answer(state,a,now){const s=state.active,it=s?.items[s.index];if(!it||it.locked)throw Error('Câu đã chấm hoặc không còn hoạt động.');it.answerChanges.push({answer:a,at:iso(now)});it.answer=a;}
 function assist(state,kind){const s=state.active,it=s?.items[s.index];if(!it||!ASSIST.includes(kind))throw Error('Loại trợ giúp không hợp lệ.');if(it.isListening&&it.audioPlays===1&&['transcript','replayed-audio'].includes(kind)&&!it.firstListen)it.firstListen={answer:it.answer,capturedAt:iso(),assistance:[...it.assistance]};if(!s.training&&['hint','transcript','gemini','answer-key','worked-example'].includes(kind))throw Error('Lượt đo không có gợi ý hay đáp án trước.');if(!it.assistance.includes(kind))it.assistance.push(kind);}
 function evidence(s,it){if(it.assistance.length)return 'assisted';if(!it.isItemNew||!it.isStimulusNew)return 'review';if(s.training)return 'training-new';if(s.interrupted||s.overTime)return 'new-conditions';if(it.guessed)return 'new-guessed';return 'independent-new';}
 function makeAttempt(state,bank,s,it,now){
  const q=question(bank,it.questionId);if(q.audio&&it.audioPlays>1&&!it.assistance.includes('replayed-audio'))it.assistance.push('replayed-audio');if(q.categoryCode==='LISTEN'&&it.audioPlays<1&&!it.assistance.includes('no-audio'))it.assistance.push('no-audio');const r=score(q,it.answer);if(r.status==='invalid')throw Error(q.id+': đáp án không hợp lệ.');
  const h=history(state,q.id),last=h[h.length-1],n=r.correct&&!it.assistance.length&&!it.guessed?(last?.reviewIntervalDays>=3?last.reviewIntervalDays>=7?14:7:3):1;
  const ev=evidence(s,it),oldConcept=state.attempts.filter(a=>bank.questions.find(x=>x.id===a.questionId)?.conceptId===q.conceptId&&a.attempted).sort((a,b)=>a.answeredAt.localeCompare(b.answeredAt))[0];
  return {id:s.id+':'+q.id,sessionId:s.id,questionId:q.id,stimulusId:q.stimulusId,answer:it.answer,answerChanges:clone(it.answerChanges),correctAnswer:q.correctAnswer,...r,audioPlays:it.audioPlays,firstListen:q.audio?(it.firstListen?{...clone(it.firstListen),...score(q,it.firstListen.answer)}:it.audioPlays===1&&!it.assistance.some(x=>['transcript','replayed-audio','no-audio'].includes(x))?{answer:it.answer,...r,capturedAt:iso(now),assistance:[...it.assistance]}:null):null,assistance:[...it.assistance],guessed:!!it.guessed,isItemNew:it.isItemNew,isStimulusNew:it.isStimulusNew,evidenceType:ev,mode:s.mode,activeSeconds:Math.max(0,Math.round(it.activeSeconds*10)/10),interrupted:s.interrupted,overTime:s.overTime,answeredAt:iso(now),localDate:s.localDate,bankVersion:bank.bankVersion,answerKeyDigest:bank.answerKeyDigest,reviewIntervalDays:n,nextReviewAt:iso((now===undefined?Date.now():now)+n*DAY),delayedNewConcept:ev==='independent-new'&&!!oldConcept&&(now===undefined?Date.now():now)-Date.parse(oldConcept.answeredAt)>=3*DAY};
 }
 function checkOne(state,bank,now){const s=state.active,it=s?.items[s.index];if(!s||!s.training)throw Error('Chỉ chấm từng câu trong chế độ luyện.');if(it.locked)return state.attempts.find(a=>a.id===s.id+':'+it.questionId);const a=makeAttempt(state,bank,s,it,now);if(!state.attempts.some(x=>x.id===a.id))state.attempts.push(a);it.locked=true;return a;}
 function submit(state,bank,now){
  const s=state.active;if(!s)throw Error('Không có buổi đang làm.');
  for(const it of s.items.filter(x=>x.presentedAt)){if(!state.attempts.some(a=>a.id===s.id+':'+it.questionId))state.attempts.push(makeAttempt(state,bank,s,it,now));it.locked=true;}
  const rows=state.attempts.filter(a=>a.sessionId===s.id);s.submitted=true;s.finishedAt=iso(now);s.presentedCount=s.items.filter(x=>x.presentedAt).length;s.plannedCount=s.items.length;s.attemptedCount=rows.filter(a=>a.attempted).length;s.correctCount=rows.filter(a=>a.correct).length;s.unansweredCount=rows.filter(a=>!a.attempted).length;s.independentCount=rows.filter(a=>a.attempted&&a.evidenceType==='independent-new').length;s.studySeconds=Math.round(s.items.reduce((n,x)=>n+x.activeSeconds,0));
  state.sessions.push(clone(s));state.active=null;state.updatedAt=iso(now);return clone(s);
 }
 function summary(state,bank){
  const skills={},concepts=conceptStats(state,bank),seen=new Set(state.exposures.map(e=>e.questionId));
  const skill=q=>['PART','CONJ','GRAM','ORDER'].includes(q.categoryCode)?'Ngữ pháp':['INTERP','SHORT','MED'].includes(q.categoryCode)?'Đọc':q.categoryCode==='LISTEN'?'Nghe':q.categoryCode==='VOC'?'Từ và kanji':'Giao tiếp';
  for(const q of bank.questions){const k=skill(q);if(!skills[k])skills[k]={skill:k,total:0,correct:0,review:0,assisted:0,training:0,guessed:0,delayedNew:0,delayedCorrect:0};}
  for(const a of state.attempts){const q=bank.questions.find(q=>q.id===a.questionId);if(!q||!a.attempted)continue;const s=skills[skill(q)];if(a.evidenceType==='independent-new'){s.total++;s.correct+=a.correct?1:0;if(a.delayedNewConcept){s.delayedNew++;s.delayedCorrect+=a.correct?1:0;}}else if(a.evidenceType==='review')s.review++;else if(a.evidenceType==='assisted')s.assisted++;else if(a.evidenceType==='training-new')s.training++;if(a.guessed)s.guessed++;}
  const eligible=Object.values(skills).filter(s=>s.total>=5).sort((a,b)=>a.correct/a.total-b.correct/b.total);
  return {skills:Object.values(skills),weakest:eligible[0]||null,strongest:eligible.length>=2?eligible[eligible.length-1]:null,concepts,seenCount:seen.size,newRemaining:bank.questions.filter(q=>!seen.has(q.id)).length,sessions:state.sessions.length,correct:state.attempts.filter(a=>a.correct).length,attempted:state.attempts.filter(a=>a.attempted).length};
 }
 function errorPackage(state,bank,sessionId){
  const s=state.sessions.find(s=>s.id===sessionId);if(!s)throw Error('Không có kết quả buổi này.');const rows=state.attempts.filter(a=>a.sessionId===sessionId&&(!a.correct||a.assistance.length||a.guessed));
  return 'ĐÂY LÀ PHẦN CHỮA SAU KHI ĐÃ NỘP, KHÔNG PHẢI LƯỢT ĐO.\nChỉ chọn một hiểu nhầm để dạy ngắn; hỏi một câu mới và chờ tôi trả lời. Không tự ghi Excel hay giả vờ nhớ chat khác.\n'+JSON.stringify(rows.slice(0,3).map(a=>{const q=question(bank,a.questionId);return {questionId:q.id,patternId:q.patternId,relatedTemplate:q.relatedTemplate,origin:q.origin,question:q.stem,passage:q.passage||null,practiceAudioScript:q.audio?.script||null,options:q.options,learnerAnswer:a.answer,verifiedAnswer:q.correctAnswer,answerKeyDigest:a.answerKeyDigest,explanation:q.explanationVi,wrongChoiceReason:q.distractorExplanations[a.answer]||null,errorCategory:q.errorCategory,prerequisites:q.prerequisites,source:q.references,assistanceAlreadyReceived:a.assistance,evidenceType:a.evidenceType,guessed:a.guessed};}),null,2)+'\nNếu không đủ dữ liệu phân biệt lỗi âm/từ/ngữ pháp/ghi nhớ, hỏi một câu kiểm tra; không chẩn đoán chắc chắn.';
 }
 function csv(state,bank){
  const headers=['Session ID','Ngày','Cấp','Kỹ năng','Mã bài','Loại dữ liệu','Đúng','Đã trả lời','Tổng đã xem','Giây làm','Trợ giúp','Ghi chú'];const rows=[];
  const groups=new Map();for(const a of state.attempts){const q=question(bank,a.questionId),sk=['PART','CONJ','GRAM','ORDER'].includes(q.categoryCode)?'Ngữ pháp':['INTERP','SHORT','MED'].includes(q.categoryCode)?'Đọc':q.categoryCode==='LISTEN'?'Nghe':q.categoryCode==='VOC'?'Từ và kanji':'Giao tiếp';const tag=a.evidenceType==='independent-new'?'Mới':a.evidenceType==='review'?'Ôn lại':a.evidenceType==='assisted'?'Hỗ trợ':'Luyện';const key=a.sessionId+'|'+sk+'|'+tag;if(!groups.has(key))groups.set(key,{a,sk,tag,correct:0,attempted:0,presented:0,seconds:0,assistance:new Set()});const g=groups.get(key);g.correct+=a.correct?1:0;g.attempted+=a.attempted?1:0;g.presented++;g.seconds+=a.activeSeconds;a.assistance.forEach(x=>g.assistance.add(x));}
  for(const g of groups.values())rows.push([g.a.sessionId,g.a.localDate,'N4',g.sk,'ORIG-'+g.a.sessionId.slice(0,8),g.tag,g.correct,g.attempted,g.presented,Math.round(g.seconds),[...g.assistance].join(';'),'Câu gốc, không phải điểm JLPT; '+g.a.bankVersion]);
  const enc=v=>'"'+String(typeof v==='string'&&/^[=+@-]/.test(v)?"'"+v:v??'').replaceAll('"','""')+'"';return '\ufeff'+[headers,...rows].map(r=>r.map(enc).join(',')).join('\r\n');
 }
 function validateImport(obj,bank){
  if(!obj||typeof obj!=='object'||Array.isArray(obj)||obj.schemaVersion!==SCHEMA)throw Error('Không đúng tệp tiến độ phiên bản 1.');
  if(obj.bankVersion!==bank.bankVersion||obj.answerKeyDigest!==bank.answerKeyDigest)throw Error('Khác phiên bản ngân hàng/khóa. Không tự đổi điểm lịch sử.');
  for(const k of ['attempts','exposures','sessions','diagnostics'])if(!Array.isArray(obj[k])||obj[k].length>20000)throw Error('Danh sách '+k+' không hợp lệ/quá lớn.');
  const validDate=x=>typeof x==='string'&&x.length<50&&Number.isFinite(Date.parse(x));const ids=new Set();
  for(const a of obj.attempts){
   const q=question(bank,a.questionId);if(typeof a.id!=='string'||a.id.length>180||ids.has(a.id))throw Error('ID lượt làm trùng hoặc không hợp lệ.');ids.add(a.id);
   if(a.bankVersion!==bank.bankVersion||a.answerKeyDigest!==bank.answerKeyDigest)throw Error('Khóa trong lượt làm không khớp.');
   const r=score(q,a.answer);if(r.status==='invalid'||r.correct!==a.correct||r.attempted!==a.attempted)throw Error('Đáp án/điểm trong tệp không nhất quán.');
   if(!Array.isArray(a.assistance)||a.assistance.some(x=>!ASSIST.includes(x))||!validDate(a.answeredAt)||!validDate(a.nextReviewAt)||!Number.isFinite(a.activeSeconds)||a.activeSeconds<0||a.activeSeconds>86400)throw Error('Thời gian/trợ giúp không hợp lệ.');
   if(!['independent-new','review','assisted','training-new','new-conditions','new-guessed'].includes(a.evidenceType))throw Error('Loại dữ liệu không hợp lệ.');
   if(a.evidenceType==='independent-new'&&(!a.isItemNew||!a.isStimulusNew||a.assistance.length||a.guessed||a.interrupted||a.overTime||MODES[a.mode]?.training))throw Error('Câu có trợ giúp/đã thấy không được đánh dấu mới độc lập.');
  }
  for(const e of obj.exposures)if(!bank.questions.some(q=>q.id===e.questionId&&q.stimulusId===e.stimulusId)||!validDate(e.at)||typeof e.id!=='string'||e.id.length>180)throw Error('Lịch sử đã xem không hợp lệ.');
  for(const d of obj.diagnostics)if(!['N4','N3','N2'].includes(d.level)||!Number.isInteger(d.correct)||!Number.isInteger(d.total)||d.total<1||d.correct<0||d.correct>d.total||!validDate(d.date))throw Error('Chẩn đoán không hợp lệ.');
  const safeId=x=>typeof x==='string'&&/^[A-Za-z0-9_:-]{1,180}$/.test(x);
  const sessionCheck=s=>{if(!s||!safeId(s.id)||!MODES[s.mode]||typeof s.training!=='boolean'||!validDate(s.startedAt)||!Array.isArray(s.items)||s.items.length>30||!Number.isInteger(s.index)||s.index<0||s.index>=s.items.length)throw Error('Buổi làm không hợp lệ.');for(const it of s.items){question(bank,it.questionId);if(score(question(bank,it.questionId),it.answer).status==='invalid'||!Array.isArray(it.assistance)||it.assistance.some(x=>!ASSIST.includes(x))||!Array.isArray(it.answerChanges)||it.answerChanges.length>1000||!Number.isFinite(it.activeSeconds)||it.activeSeconds<0||it.activeSeconds>86400||typeof it.guessed!=='boolean'||typeof it.isItemNew!=='boolean'||typeof it.isStimulusNew!=='boolean'||!Number.isInteger(it.audioPlays)||it.audioPlays<0||it.audioPlays>1000||it.presentedAt&&!validDate(it.presentedAt))throw Error('Câu trong buổi dở không hợp lệ.');}};
  for(const a of obj.attempts)if(!safeId(a.sessionId)||!safeId(a.id)||!MODES[a.mode]||a.correctAnswer!==question(bank,a.questionId).correctAnswer||['guessed','isItemNew','isStimulusNew','interrupted','overTime'].some(k=>typeof a[k]!=='boolean'))throw Error('Lượt làm thiếu cờ hoặc khóa không đúng.');
  for(const k of ['sessions','exposures','speaking']){const arr=obj[k]||[];if(new Set(arr.map(x=>x.id)).size!==arr.length)throw Error('ID trùng trong '+k);}
  obj.sessions.forEach(sessionCheck);if(obj.active)sessionCheck(obj.active);
  if(obj.speaking!==undefined&&(!Array.isArray(obj.speaking)||obj.speaking.length>20000||obj.speaking.some(r=>!safeId(r.id)||!bank.roleplays.some(x=>x.id===r.roleId)||!validDate(r.at)||!Array.isArray(r.intents)||r.intents.length!==4||r.intents.some(x=>!['0','1','?'].includes(x)))))throw Error('Phiếu nói không hợp lệ.');
  if(obj.reflections!==undefined&&(!obj.reflections||typeof obj.reflections!=='object'||Array.isArray(obj.reflections)||Object.keys(obj.reflections).length>20000))throw Error('Phản hồi không hợp lệ.');
  return true;
 }
 function merge(state,incoming,bank){
  validateImport(incoming,bank);const out=clone(state);
  for(const key of ['attempts','exposures','sessions','speaking']){const map=new Map((out[key]||[]).map(x=>[x.id,x]));for(const x of incoming[key]||[]){if(map.has(x.id)&&JSON.stringify(map.get(x.id))!==JSON.stringify(x))throw Error('Xung đột lịch sử cùng ID; giữ tệp hiện tại, chưa nhập.');map.set(x.id,clone(x));}out[key]=[...map.values()];}
  out.sessions.sort((a,b)=>a.startedAt.localeCompare(b.startedAt));out.attempts.sort((a,b)=>a.answeredAt.localeCompare(b.answeredAt));out.diagnostics=[...out.diagnostics,...incoming.diagnostics.filter(x=>!out.diagnostics.some(y=>JSON.stringify(x)===JSON.stringify(y)))];
  if(incoming.active&&!out.sessions.some(s=>s.id===incoming.active.id)){if(out.active&&JSON.stringify(out.active)!==JSON.stringify(incoming.active))throw Error('Hai buổi dở khác nhau. Nộp phần hiện tại rồi nhập bản sao.');if(!out.active){out.active=clone(incoming.active);out.active.interrupted=true;}}
  if(out.active&&out.sessions.some(s=>s.id===out.active.id))out.active=null;
  out.reflections={...incoming.reflections,...out.reflections};out.updatedAt=iso();return out;
 }
 function reviewedKey(state,bank,qid,now){const q=question(bank,qid);state.exposures.push({id:'key-'+id(),sessionId:null,questionId:q.id,stimulusId:q.stimulusId,at:iso(now),kind:'answer-key'});}
 return Object.freeze({VERSION,SCHEMA,DAY,MODES,ASSIST,fresh,checkBank,question,score,prior,status,due,select,start,present,answer,assist,checkOne,submit,summary,errorPackage,csv,validateImport,merge,reviewedKey,clone,iso,localDate});
});
