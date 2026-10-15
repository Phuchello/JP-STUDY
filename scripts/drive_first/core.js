/* Pure data logic, shared by Apps Script and Node QA. No network or credentials. */
var JPStudy = (() => {
  const HEADERS=['report_date','timezone','activity','quiz_id','submission_id','submitted_at','question_id','level','skill','result','attempt_type','learner_answer','correct_label','concept_id','prior_attempt_dates','fatigue','repeated_error_count','review_candidate','evidence_gaps'];
  function option(q,o){return o.id+'. '+o.text;}
  function review(q,row){return 'CHỮA CÂU SAI VỚI GEMINI\nMã: '+q.id+'\nCâu gốc: '+(q.passage?q.passage+'\n':'')+q.stem+'\n'+q.options.map(o=>option(q,o)).join('\n')+'\nTôi chọn: '+(row.answer||'bỏ trống')+'\nKhóa đã QA: '+q.correctAnswer+'\nGiải thích: '+q.explanationVi+'\nMẫu: '+(q.patternId||q.conceptId)+'\nNguồn: '+q.references.map(r=>r.url).join(' ')+'\nGiải thích bằng 3–6 câu Việt ngắn, không đoán nguyên nhân tôi sai. Nêu một đối chiếu Nhật, hỏi MỘT câu mới và CHỜ. Sau đó sửa ngắn, nhờ tôi nói/viết một câu mới. Không tiết lộ câu chẩn đoán tiếp theo; không chấm phát âm từ chữ.';}
  function normalize(data,quiz,submission,itemMap){
    if(!submission.id||!submission.timestamp)throw Error('Missing response identity/time');
    if(submission.synthetic)return [];
    const used=new Set();
    return quiz.questionIds.map(id=>{
      const q=data.questions[id],itemId=Object.keys(itemMap).find(k=>itemMap[k]===id);
      if(!itemId||used.has(itemId))throw Error('Missing/duplicate item map '+id);used.add(itemId);
      const raw=Object.prototype.hasOwnProperty.call(submission.answers,itemId)?submission.answers[itemId]:'';
      const found=q.options.find(o=>option(q,o)===raw);
      if(raw&&!found)throw Error('Answer value no longer matches audited options '+id);
      return {key:submission.id+'|'+id,submissionId:submission.id,quizId:quiz.id,timestamp:submission.timestamp,id,level:q.level,skill:q.category,concept:q.conceptId,stimulus:q.stimulusId,answer:found?found.id:'',correctLabel:q.correctAnswer,result:!found?'unanswered':found.id===q.correctAnswer?'correct':'incorrect',declaredMode:submission.mode||'unknown',fatigue:[1,2,3,4,5].includes(Number(submission.fatigue))?Number(submission.fatigue):null};
    });
  }
  function enrich(input){
    const unique=new Map();for(const r of input){if(unique.has(r.key)&&JSON.stringify(unique.get(r.key))!==JSON.stringify(r))throw Error('Conflicting duplicate '+r.key);unique.set(r.key,r);}
    const rows=[...unique.values()].sort((a,b)=>a.timestamp.localeCompare(b.timestamp)||a.submissionId.localeCompare(b.submissionId)||a.id.localeCompare(b.id)),seenQ=new Map(),seenStimulus=new Map(),errors=new Map(),before=new Map(),out=[];
    // All questions in one submitted set share pre-submission exposure state.
    for(const r of rows){
      if(!before.has(r.submissionId))before.set(r.submissionId,{q:new Map(seenQ),s:new Map(seenStimulus)});
      const pre=before.get(r.submissionId),prior=pre.q.get(r.id)||[],exposed=pre.s.has(r.stimulus),newSelf=r.declaredMode==='Tự làm, chưa xem câu/khóa'&&!prior.length&&!exposed;
      const type=r.declaredMode==='Có tra/gợi ý'?'assisted':newSelf?'new_self_reported':['Tự làm, chưa xem câu/khóa','Đã xem/ôn lại'].includes(r.declaredMode)?'review':'unknown';
      const e=errors.get(r.id)||0;if(r.result==='incorrect')errors.set(r.id,e+1);
      out.push({...r,attemptType:type,priorDates:prior.slice(),repeatedErrors:errors.get(r.id)||0});
      seenQ.set(r.id,[...(seenQ.get(r.id)||[]),r.timestamp]);seenStimulus.set(r.stimulus,r.timestamp);
    }
    return out;
  }
  function summarize(rows){
    const groups=new Map(),latest=new Map(),skills={};
    for(const r of rows){if(!groups.has(r.submissionId))groups.set(r.submissionId,[]);groups.get(r.submissionId).push(r);latest.set(r.id,r);const k=r.skill+' / '+r.attemptType;const s=skills[k]||(skills[k]={correct:0,incorrect:0,unanswered:0});s[r.result]++;}
    const errors=[...latest.values()].filter(r=>r.result!=='correct'),history=[...groups.values()].map(rs=>({id:rs[0].submissionId,quizId:rs[0].quizId,timestamp:rs[0].timestamp,correct:rs.filter(r=>r.result==='correct').length,total:rs.length,unanswered:rs.filter(r=>r.result==='unanswered').length,newCount:rs.filter(r=>r.attemptType==='new_self_reported').length,reviewCount:rs.filter(r=>r.attemptType==='review').length,assistedCount:rs.filter(r=>r.attemptType==='assisted').length,unknownCount:rs.filter(r=>r.attemptType==='unknown').length,mistakeIds:rs.filter(r=>r.result!=='correct').map(r=>r.id),fatigue:rs[0].fatigue,questionIds:rs.map(r=>r.id)}));
    const n=rows.filter(r=>r.attemptType==='new_self_reported'&&r.result!=='unanswered').length;
    return {history,errors,skills,activityCount:history.filter(h=>h.unanswered===0).length,submittedCount:groups.size,lastActivity:history.length?history[history.length-1].timestamp:null,evidenceGaps:['Lần đầu/tự làm dựa trên tự báo; chưa biết lịch sử ngoài hệ thống.','Báo cáo chỉ phản ánh lượt nộp quiz đã thu; nghe/nói hoặc học không nộp chưa được ghi.','Forms không ghi thời gian học thực hoặc các lần mở chưa nộp.','Chưa có kiểm âm/nghe hoặc điểm nói từ các quiz văn bản.',n<5?'Chưa đủ 5 câu mới đã trả lời để mô tả theo nhóm.':'Mẫu mô tả; chưa đủ thiết kế so sánh để kết luận tiến bộ.'],reviewCandidates:errors.slice(-2).map(r=>r.id)};
  }
  function daily(rows,date,tz,dateOf){
    const selected=rows.filter(r=>dateOf(r.timestamp,tz)===date),summary=summarize(rows),latest=new Map();for(const r of rows)latest.set(r.id,r);
    const items=selected.map(r=>({report_date:date,timezone:tz,activity:'Có hoạt động học mới.',quiz_id:r.quizId,submission_id:r.submissionId,submitted_at:r.timestamp,question_id:r.id,level:r.level,skill:r.skill,result:r.result,attempt_type:r.attemptType,learner_answer:r.answer,correct_label:r.correctLabel,concept_id:r.concept,prior_attempt_dates:r.priorDates.join(' | '),fatigue:r.fatigue??'',repeated_error_count:r.repeatedErrors,review_candidate:latest.get(r.id).result!=='correct'?r.id:'',evidence_gaps:summary.evidenceGaps.join(' | ')}));
    if(!items.length)items.push({report_date:date,timezone:tz,activity:'Không có hoạt động học mới.',evidence_gaps:'Chỉ xét lượt nộp đã thu. Nghe/nói hoặc học không nộp chưa được ghi. Không suy ra lý do vắng hoạt động.'});
    const dayHistory=summarize(selected).history;
    return {date,timezone:tz,message:selected.length?'Có hoạt động học mới.':'Không có hoạt động học mới.',submittedQuizIds:[...new Set(selected.map(r=>r.quizId))],completedQuizIds:[...new Set(dayHistory.filter(h=>h.unanswered===0).map(h=>h.quizId))],items,evidenceGaps:summary.evidenceGaps,reviewCandidates:summary.reviewCandidates};
  }
  function csv(report){const safe=v=>{let s=String(v??'');if(/^[=+@-]/.test(s))s="'"+s;return '"'+s.replace(/"/g,'""')+'"';};return '\uFEFF'+[HEADERS,...report.items.map(r=>HEADERS.map(k=>r[k]??''))].map(r=>r.map(safe).join(',')).join('\r\n')+'\r\n';}
  return {HEADERS,option,review,normalize,enrich,summarize,daily,csv};
})();
if(typeof module!=='undefined')module.exports=JPStudy;
