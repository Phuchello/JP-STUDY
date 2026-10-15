/* Owner-only technical QA. Drive Advanced Service v3; never add learner access here. */
function jpP0_(){const s=jpState();return JP_DATA.quizzes.filter(q=>q.releaseGroup==='P0').map(q=>{const info=s.forms[q.id];if(!info||!info.built)throw Error('P0 chưa được dựng đủ: '+q.id);return {q,info,form:FormApp.openById(info.id)};});}
function jpAcl_(id){return Drive.Permissions.list(id,{includePermissionsForView:'published',fields:'permissions(id,type,role,view)'}).permissions||[];}
function jpOwnerOnly_(id){const a=jpAcl_(id);if(a.length!==1||a[0].type!=='user'||a[0].role!=='owner')throw Error('Quyền chưa chỉ có owner; chưa publish/kích hoạt.');return true;}
function restrictP0Responders(){for(const x of jpP0_()){for(const p of jpAcl_(x.info.id)){if(p.type==='anyone'&&p.view==='published'&&p.role==='reader')Drive.Permissions.remove(x.info.id,p.id);}jpOwnerOnly_(x.info.id);}console.log('P0 responder ACL: owner only; no learner added.');}
function inspectDeployment(){const s=jpState(),tr=ScriptApp.getProjectTriggers(),out=jpP0_().map(x=>{jpAuditOne(x.q,x.info);if(x.form.getDestinationId()!==s.rawId)throw Error('Sai bảng nhận phản hồi');const count=tr.filter(t=>t.getHandlerFunction()==='onQuizSubmit'&&t.getTriggerSourceId()===x.info.id).length;if(count!==1)throw Error('Số trigger không đúng: '+x.q.id);return {quiz:x.q.id,editUrl:x.form.getEditUrl(),responderUrl:x.form.getPublishedUrl(),published:x.form.isPublished(),questionCount:x.q.questionIds.length,submitTriggers:count,acl:jpAcl_(x.info.id).map(p=>({type:p.type,role:p.role,view:p.view||''}))};});console.log(JSON.stringify({forms:out,rawId:s.rawId,learnerRows:jpGetRows(s).length}));return out;}
function publishP0OwnerQa(){const items=jpP0_();for(const x of items){jpAuditOne(x.q,x.info);jpOwnerOnly_(x.info.id);}for(const x of items){x.form.setPublished(true);try{jpOwnerOnly_(x.info.id);}catch(e){x.form.setPublished(false);throw e;}}console.log('Published P0 only for existing owner QA. Learner links remain gated.');inspectDeployment();}
function verifySyntheticQa(){
 const lock=LockService.getScriptLock();lock.waitLock(15000);
 try{const s=jpState();if(jpGetRows(s).length)throw Error('Có dữ liệu học thật; cần bản QA trống riêng, không tự sao chép lịch sử.');
  const raw=jpRaw(s),log=raw.getSheetByName('NHAT_KY_QA'),logged=log.getLastRow()>1?log.getRange(2,2,log.getLastRow()-1,1).getValues().flat():[],rows=[],grades=[];
  for(const x of jpP0_()){
   jpAuditOne(x.q,x.info);jpOwnerOnly_(x.info.id);
   const samples=x.form.getResponses().filter(r=>r.getItemResponses().some(ir=>String(ir.getItem().getId())===x.info.modeId&&ir.getResponse()==='QA - Dữ liệu giả'));
   const r=samples[samples.length-1];if(!r)throw Error('Chưa có lượt nộp QA thật: '+x.q.id);
   const sid=x.info.id+':'+r.getId();if(!logged.includes(sid))throw Error('Chưa thấy submit trigger cách ly lượt QA: '+x.q.id);
   const answers={};for(const ir of r.getItemResponses())answers[String(ir.getItem().getId())]=ir.getResponse();
   const rr=JPStudy.normalize(JP_DATA,x.q,{id:sid,timestamp:r.getTimestamp().toISOString(),answers,mode:'unknown',fatigue:answers[x.info.fatigueId]},x.info.items);
   const actual=new Map(r.getGradableItemResponses().map(ir=>[String(ir.getItem().getId()),ir.getScore()]));let points=0;
   for(const row of rr){const item=Object.keys(x.info.items).find(k=>x.info.items[k]===row.id),score=actual.get(item),expected=row.result==='correct'?1:0;if(row.result!=='unanswered'&&score!==expected)throw Error('Điểm Google chưa khớp khóa '+row.id);if(row.result==='unanswered'&&score!=null&&score!==0)throw Error('Điểm câu trống không bằng 0');points+=Number(score||0);}
   const summary=JPStudy.summarize(JPStudy.enrich(rr)).history[0];if(!summary.correct||!summary.unanswered||summary.correct+summary.unanswered===summary.total)throw Error('QA cần có đúng, sai và trống cho mỗi Form.');
   grades.push({quiz:x.q.id,googlePoints:points,total:rr.length,correct:summary.correct,incorrect:rr.length-summary.correct-summary.unanswered,unanswered:summary.unanswered,triggerRecorded:true});rows.push(...rr.map(z=>({...z,synthetic:true})));
  }
  const all=JPStudy.enrich(rows),props=PropertiesService.getScriptProperties(),folder=jpFolder(jpFolder(jpRoot(),'05_THEO_DÕI_TIẾN_BỘ'),'QA_TECHNICAL_ONLY');let id=props.getProperty('JP_QA_SHEET_ID');
  if(!id){const copy=DriveApp.getFileById(jpSheet().getId()).makeCopy('JP_STUDY_QA_SYNTHETIC',folder);id=copy.getId();props.setProperty('JP_QA_SHEET_ID',id);}jpOwnerOnly_(id);
  const ss=SpreadsheetApp.openById(id);jpRefresh(s,{sheet:ss,rows:all});for(const tab of ['HỌC HÔM NAY','LỊCH SỬ','LỖI CẦN ÔN','BÁO CÁO QUẢN LÝ'])ss.getSheetByName(tab).getRange('A1').setValue('QA · DỮ LIỆU GIẢ · '+tab);
  const tz=JP_DATA.timezone,date=Utilities.formatDate(new Date(),tz,'yyyy-MM-dd'),report=JPStudy.daily(all,date,tz,(iso,z)=>Utilities.formatDate(new Date(iso),z,'yyyy-MM-dd'));report.synthetic=true;report.scope='TECHNICAL QA ONLY — actual Google submissions; no learner progress';report.googleGrades=grades;report.items.forEach(z=>{z.activity='QA - Dữ liệu giả';z.evidence_gaps='SYNTHETIC_QA_ONLY | '+z.evidence_gaps;});
  const stamp=Utilities.formatDate(new Date(),tz,'yyyyMMdd_HHmmss_SSS'),csv=folder.createFile('QA_LEARNING_REPORT_'+stamp+'.csv',JPStudy.csv(report),MimeType.CSV),json=folder.createFile('QA_LEARNING_REPORT_'+stamp+'.json',JSON.stringify(report,null,2),MimeType.PLAIN_TEXT);
  const proof={scope:report.scope,grades,qaDashboard:ss.getUrl(),csv:csv.getUrl(),json:json.getUrl(),learnerRows:jpGetRows(s).length,qaRows:all.length,qaHistory:JPStudy.summarize(all).history.length};props.setProperty('JP_QA_PROOF',JSON.stringify(proof));console.log(JSON.stringify(proof));return proof;
 }finally{lock.releaseLock();}
}
function activateP0Verified(){
 const s=jpState();
 for(const q of JP_DATA.quizzes){
  const inf=s.forms[q.id];
  if(!inf||!inf.built)continue;
  jpAuditOne(q,inf);
  const f=FormApp.openById(inf.id);
  if(!f.supportsAdvancedResponderPermissions()||!f.isPublished())throw Error('Chưa publish với đối tượng giới hạn: '+q.id);
  inf.active=true;
 }
 jpSave(s);
 jpRefresh(s);
 const active=Object.keys(s.forms).filter(k=>s.forms[k].active);
 console.log(JSON.stringify({activated:active,dashboard:jpSheet().getUrl()}));
 return active;
}
function verifyLearnerDashboard(){
 const s=jpState(),ss=jpSheet();
 const home=ss.getSheetByName('HỌC HÔM NAY');
 const b6=home.getRange('B6').getValue();
 const b7rt=home.getRange('B7').getRichTextValue();
 const b7text=b7rt?b7rt.getText():'';
 const b7url=b7rt?b7rt.getLinkUrl():'';
 const week=ss.getSheetByName('TUẦN NÀY');
 const weekRows=[];
 for(let i=4;i<=6;i++){
  const rt=week.getRange(i,4).getRichTextValue();
  weekRows.push({
   title:week.getRange(i,1).getValue(),
   linkText:rt?rt.getText():week.getRange(i,4).getValue(),
   url:rt?rt.getLinkUrl():''
  });
 }
 const exp=exportDailyReport();
 const result={
  dashboardStatus:b6,
  quizButtonText:b7text,
  quizButtonUrl:b7url,
  weekLinks:weekRows,
  learnerRows:jpGetRows(s).length,
  activeQuizzes:Object.keys(s.forms).filter(k=>s.forms[k].active),
  exportedCsv:exp.csv,
  exportedJson:exp.json
 };
 console.log(JSON.stringify(result));
 return result;
}

