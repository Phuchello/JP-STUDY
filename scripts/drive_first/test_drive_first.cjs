const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert/strict');const R=path.resolve(__dirname,'../..'),D=JSON.parse(fs.readFileSync(path.join(R,'tmp/drive-first/data.json'),'utf8')),C=require('./core.js'),bank=JSON.parse(fs.readFileSync(path.join(R,'deliverables/phase3/JLPT_PRACTICE/question_bank.json'),'utf8')),K=JSON.parse(fs.readFileSync(path.join(R,'deliverables/phase3/ANSWER_KEY_AND_EXPLANATIONS/validated_keys.json'),'utf8'));const results=[];function test(n,f){try{f();results.push({name:n,ok:true});}catch(e){results.push({name:n,ok:false,error:e.message});}}
const source=new Map(bank.questions.map(q=>[q.id,q]));test('10 quizzes / 68 distinct reused IDs / 12 reserved',()=>{assert.equal(D.quizzes.length,10);assert.equal(new Set(D.quizzes.flatMap(q=>q.questionIds)).size,68);assert.equal(bank.questions.length-Object.keys(D.questions).length,12);});
for(const quiz of D.quizzes){test(quiz.id+' size and non-listening classification',()=>{assert(quiz.questionIds.length>=5&&quiz.questionIds.length<=10);assert(quiz.questionIds.every(i=>!source.get(i).audio));});for(const id of quiz.questionIds){const q=D.questions[id];test(id+' exactly retained from audited source',()=>assert.deepEqual(q,source.get(id)));for(const o of q.options){test(id+' label '+o.id+' scoring map',()=>{const map={'item-777':id},one={...quiz,questionIds:[id]},r=C.normalize(D,one,{id:'test',timestamp:'2026-10-15T00:00:00.000Z',mode:'Tự làm, chưa xem câu/khóa',answers:{'item-777':C.option(q,o)}},map)[0],key=K.questions.find(k=>k.id===id).correctAnswer;assert.equal(r.result,o.id===key?'correct':'incorrect');assert.equal(r.answer,o.id);});}}}
const quiz=D.quizzes[0],map=Object.fromEntries(quiz.questionIds.map((id,i)=>[String(100+i),id]));function sub(sid,t,mode='Tự làm, chưa xem câu/khóa',fatigue=''){const answers={};for(const [item,id]of Object.entries(map)){const q=D.questions[id];answers[item]=C.option(q,q.options.find(o=>o.id===q.correctAnswer));}return{id:sid,timestamp:t,answers,mode,fatigue};}
const s1=sub('first','2026-10-15T14:59:00.000Z');s1.answers['101']=C.option(D.questions[map['101']],D.questions[map['101']].options.find(o=>o.id!==D.questions[map['101']].correctAnswer));s1.answers['102']=C.option(D.questions[map['102']],D.questions[map['102']].options.find(o=>o.id!==D.questions[map['102']].correctAnswer));delete s1.answers['104'];const raw=C.normalize(D,quiz,s1,map),en=C.enrich(raw);
test('Omitted MCQ item is unanswered, not shifted to next question',()=>{assert.equal(raw[4].result,'unanswered');assert.equal(raw[4].id,quiz.questionIds[4]);assert.equal(raw[3].result,'correct');});test('2 correct / 2 wrong / 1 blank and partial, no fake fatigue',()=>{const a=C.summarize(en),h=a.history[0];assert.equal(h.correct,2);assert.equal(h.total,5);assert.equal(h.unanswered,1);assert.equal(a.activityCount,0);assert.equal(a.submittedCount,1);assert.equal(h.fatigue,null);});test('Duplicate event is idempotent',()=>assert.equal(C.enrich([...raw,...raw]).length,5));test('Conflicting duplicate rejected',()=>assert.throws(()=>C.enrich([...raw,{...raw[0],answer:'conflict'}])));test('Synthetic submissions never become learning rows',()=>assert.deepEqual(C.normalize(D,quiz,{...s1,synthetic:true},map),[]));test('Unknown answer and missing map fail closed',()=>{assert.throws(()=>C.normalize(D,quiz,{...s1,answers:{...s1.answers,'100':'unmapped choice'}},map));assert.throws(()=>C.normalize(D,quiz,s1,{}));});
const r2=C.normalize(D,quiz,sub('second','2026-10-18T15:01:00.000Z'),map);test('Retake self-report cannot reset seen ID to new',()=>assert(C.enrich([...raw,...r2]).slice(5).every(r=>r.attemptType==='review')));test('Latest correction removes stale error candidates',()=>assert.equal(C.summarize(C.enrich([...raw,...r2])).errors.length,0));test('Prior attempt dates retained',()=>assert.deepEqual(C.enrich([...raw,...r2])[5].priorDates,[s1.timestamp]));test('Assistance and unknown are not new',()=>{for(const mode of ['Có tra/gợi ý','unknown']){const a=C.enrich(C.normalize(D,quiz,sub('a','2026-10-20T00:00:00Z',mode),map));assert(!a.some(r=>r.attemptType==='new_self_reported'));}});test('Same stimulus different question is review',()=>{const other={...raw[0],id:'other',key:'later|other',submissionId:'later',timestamp:'2026-10-16T00:00:00Z'};assert.equal(C.enrich([raw[0],other])[1].attemptType,'review');});test('Unanswered submitted item remains exposed after feedback',()=>assert.equal(C.enrich([...raw,...r2])[9].attemptType,'review'));test('Same-submission shared stimulus uses pre-submission snapshot',()=>{const other={...raw[0],id:'other',key:'first|other'};assert(C.enrich([raw[0],other]).every(r=>r.attemptType==='new_self_reported'));});
const dateOf=(iso,tz)=>new Intl.DateTimeFormat('en-CA',{timeZone:tz,year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date(iso));test('Report uses requested timezone / local date boundary',()=>{assert.equal(C.daily(en,'2026-10-15','Asia/Tokyo',dateOf).items.length,5);assert.equal(C.daily(en,'2026-10-16','Asia/Tokyo',dateOf).message,'Không có hoạt động học mới.');});test('No-activity report is neutral and not fabricated failure',()=>{const r=C.daily([],'2026-10-15','Asia/Tokyo',dateOf);assert.equal(r.message,'Không có hoạt động học mới.');assert.equal(r.completedQuizIds.length,0);assert(!r.items[0].result);});test('CSV has BOM, quoted fields, injection guard and no inferred duration',()=>{const r=C.daily(en,'2026-10-15','Asia/Tokyo',dateOf);r.items[0].concept_id='=1+1';const csv=C.csv(r);assert(csv.startsWith('\uFEFF'));assert(csv.includes("'=1+1"));assert(!C.HEADERS.includes('duration'));assert(csv.includes('unanswered'));});test('Gemini package contains exact ID, choice, key and original explanation',()=>{const q=D.questions[raw[1].id],p=C.review(q,raw[1]);assert(p.includes(q.id)&&p.includes(q.stem)&&p.includes(q.explanationVi)&&p.includes(q.correctAnswer));assert(!p.includes('https://gemini.google.com/?'));});
test('Partial submission is submitted, not completed in daily JSON',()=>{const r=C.daily(en,'2026-10-15','Asia/Tokyo',dateOf);assert.deepEqual(r.submittedQuizIds,[quiz.id]);assert.deepEqual(r.completedQuizIds,[]);});
test('Fully answered retake is completed, without becoming new',()=>{const all=C.enrich([...raw,...r2]),r=C.daily(all,dateOf(r2[0].timestamp,'Asia/Tokyo'),'Asia/Tokyo',dateOf);assert.deepEqual(r.completedQuizIds,[quiz.id]);assert(r.items.every(x=>x.attempt_type==='review'));});
test('Unrecognized declared mode remains unknown, never review/new',()=>{const r=C.enrich(C.normalize(D,quiz,sub('bad-mode','2026-10-20T00:00:00Z','obsolete option'),map));assert(r.every(x=>x.attemptType==='unknown'));});
// Deterministic Workspace mocks exercise the adapter, not the actual Google service.
let serial=1000;const sheets=new Map(),forms=new Map(),properties=new Map(),triggers=[],files=new Map(),folderMap=new Map();
function rc(a){const m=a.match(/([A-Z]+)(\d+)/);return[Number(m[2]),[...m[1]].reduce((n,x)=>n*26+x.charCodeAt(0)-64,0)];}
class Range{constructor(sh,args){this.sh=sh;if(typeof args[0]==='string'){const parts=args[0].split(':'),a=rc(parts[0]),b=rc(parts[1]||parts[0]);[this.r,this.c]=a;this.nr=b[0]-a[0]+1;this.nc=b[1]-a[1]+1;}else [this.r,this.c,this.nr=1,this.nc=1]=args;}setValues(rows){assert.equal(rows.length,this.nr);rows.forEach((r,i)=>{assert.equal(r.length,this.nc);r.forEach((v,j)=>this.sh.data.set((this.r+i)+','+(this.c+j),v));});return this;}getValues(){return Array.from({length:this.nr},(_,i)=>Array.from({length:this.nc},(_,j)=>this.sh.data.get((this.r+i)+','+(this.c+j))??''));}setValue(v){assert.equal(this.nr*this.nc,1);return this.setValues([[v]]);}getValue(){return this.getValues()[0][0];}setRichTextValue(v){this.sh.links.set(this.r+','+this.c,v.url);return this.setValue(v.text);}setNumberFormat(){return this;}clearContent(){for(let i=0;i<this.nr;i++)for(let j=0;j<this.nc;j++)this.sh.data.delete((this.r+i)+','+(this.c+j));return this;}}
class Sheet{constructor(name){this.name=name;this.id=++serial;this.data=new Map();this.links=new Map();}setName(n){this.name=n;return this;}getName(){return this.name;}getSheetId(){return this.id;}getLastRow(){return Math.max(0,...[...this.data].filter(([k,v])=>v!=='').map(([k])=>Number(k.split(',')[0])));}getRange(...args){return new Range(this,args);}appendRow(v){this.getRange(this.getLastRow()+1,1,1,v.length).setValues([v]);}}
class SS{constructor(id,names=['Sheet1']){this.id=id;this.tabs=names.map(n=>new Sheet(n));sheets.set(id,this);}getName(){return this.name||'JP_STUDY_HOC_HOM_NAY';}getId(){return this.id;}getUrl(){return'https://example.invalid/sheets/'+this.id;}getSheets(){return this.tabs;}getSheetByName(n){const s=this.tabs.find(s=>s.name===n);if(!s)throw Error('missing tab '+n);return s;}insertSheet(n){const s=new Sheet(n);this.tabs.push(s);return s;}setSpreadsheetTimeZone(z){this.tz=z;}toast(){}}
class Item{constructor(type){this.type=type;this.id=++serial;this.title='';}getId(){return this.id;}getTitle(){return this.title;}setTitle(t){this.title=t;return this;}asListItem(){assert.equal(this.type,'LIST');return this;}asMultipleChoiceItem(){assert.equal(this.type,'MC');return this;}setChoiceValues(a){this.values=a;return this;}setRequired(v){this.required=v;return this;}isRequired(){return this.required??false;}createChoice(value,correct){return{getValue:()=>value,isCorrectAnswer:()=>correct};}setChoices(a){this.choices=a;return this;}getChoices(){return this.choices;}setPoints(n){this.points=n;return this;}getPoints(){return this.points;}setFeedbackForCorrect(v){this.feedbackCorrect=v;return this;}getFeedbackForCorrect(){return this.feedbackCorrect;}setFeedbackForIncorrect(v){this.feedbackIncorrect=v;return this;}getFeedbackForIncorrect(){return this.feedbackIncorrect;}}
class Form{constructor(title,published){this.id='form'+(++serial);this.title=title;this.published=published;this.items=[];this.responses=[];forms.set(this.id,this);}getId(){return this.id;}getItems(t){return this.items.filter(i=>!t||i.type===t);}getItemById(id){return this.items.find(i=>i.id===id);}addListItem(){const i=new Item('LIST');this.items.push(i);return i;}addPageBreakItem(){const i=new Item('PAGE');this.items.push(i);return i;}addMultipleChoiceItem(){const i=new Item('MC');this.items.push(i);return i;}getDestinationId(){if(!this.destination)throw Error('no response destination');return this.destination;}setDestination(t,id){this.destination=id;return this;}getEditUrl(){return'https://example.invalid/forms/'+this.id+'/edit';}getPublishedUrl(){return'https://example.invalid/forms/'+this.id+'/view';}collectsEmail(){return this.setCollectEmailValue;}isPublishingSummary(){return this.setPublishingSummaryValue;}isQuiz(){return this.setIsQuizValue;}supportsAdvancedResponderPermissions(){return true;}isPublished(){return this.published;}getResponses(){return this.responses;}}
for(const n of ['setIsQuiz','setCollectEmail','setPublishingSummary','setAllowResponseEdits','setShowLinkToRespondAgain','setShuffleQuestions','setProgressBar','setLimitOneResponsePerUser','setDescription','setConfirmationMessage'])Form.prototype[n]=function(v){this[n+'Value']=v;return this;};
function iter(a){let i=0;return{hasNext:()=>i<a.length,next:()=>a[i++]};}class Folder{constructor(name){this.id='folder'+(++serial);this.name=name;this.children=[];this.files=[];folderMap.set(this.id,this);}getName(){return this.name;}getId(){return this.id;}getParents(){return iter(this.parents||[]);}getFoldersByName(n){return iter(this.children.filter(x=>x.name===n));}createFolder(n){const f=new Folder(n);this.children.push(f);return f;}getFilesByName(n){return iter(this.files.filter(x=>x.name===n));}createFile(name,content,mime){const f={id:'file'+(++serial),name,content,mime,getUrl(){return'https://example.invalid/files/'+this.id;},setName(v){this.name=v;}};this.files.push(f);return f;}}
const main=new SS('dashboard',['HỌC HÔM NAY','TUẦN NÀY','LỊCH SỬ','LỖI CẦN ÔN','BÁO CÁO QUẢN LÝ']),root=new Folder('JP-STUDY — HỌC TIẾNG NHẬT');const today=new Folder('01_HỌC_HÔM_NAY');today.parents=[root];let active=main,mainParents=[today];main.getSheetByName('BÁO CÁO QUẢN LÝ').getRange('B3').setValue('Asia/Tokyo');const ui={ButtonSet:{YES_NO:'YES_NO'},Button:{YES:'YES'},alert:()=> 'YES'};
const ctx=vm.createContext({console,JP_DATA:D,JPStudy:C,Map,Set,Date,JSON,Object,Number,String,Array,Error,SpreadsheetApp:{getActiveSpreadsheet:()=>active,newRichTextValue:()=>({setText(text){this.text=text;return this;},setLinkUrl(url){this.url=url;return this;},build(){return {text:this.text,url:this.url};}}),openById:id=>sheets.get(id),create:n=>new SS('raw'+(++serial)),getUi:()=>ui},DriveApp:{getFolderById:id=>{assert.equal(id,root.id);return root;},getFileById:id=>({getParents:()=>iter(id===main.id?mainParents:[]),moveTo:f=>{files.set(id,f.id);}})},FormApp:{ItemType:{LIST:'LIST',MULTIPLE_CHOICE:'MC'},DestinationType:{SPREADSHEET:'SHEET'},create:(t,p)=>new Form(t,p),openById:id=>forms.get(id),createFeedback:()=>({setText(t){this.text=t;return this;},build(){return {getText:()=>this.text,text:this.text,url:this.url};}})},PropertiesService:{getScriptProperties:()=>({getProperty:k=>properties.get(k),setProperty:(k,v)=>properties.set(k,v)})},LockService:{getScriptLock:()=>({waitLock(){},releaseLock(){}})},ScriptApp:{getProjectTriggers:()=>triggers,newTrigger:handler=>({forForm(form){this.id=form.id;return this;},onFormSubmit(){return this;},create(){triggers.push({getHandlerFunction:()=>handler,getTriggerSourceId:()=>this.id});}})},Utilities:{formatDate:(date,z,p)=>p==='yyyy-MM-dd'?dateOf(date.toISOString(),z):'20261015_000000_001'},MimeType:{CSV:'CSV',PLAIN_TEXT:'TEXT'}});
const pilotPayload=fs.readFileSync(path.join(R,'DRIVE_SETUP/pilot_payload.js'),'utf8');vm.runInContext(pilotPayload,ctx);
const adapter=fs.readFileSync(path.join(R,'DRIVE_SETUP/workspace_adapter.js'),'utf8');vm.runInContext(adapter,ctx);

test('Bound bootstrap rejects absent active spreadsheet before persistence',()=>{active=null;assert.throws(()=>ctx.jpSheet());assert(!properties.has('JP_DASHBOARD_ID'));active=main;});
test('Bound bootstrap rejects wrong spreadsheet title',()=>{main.name='Other';assert.throws(()=>ctx.jpSheet());assert(!properties.has('JP_DASHBOARD_ID'));main.name='JP_STUDY_HOC_HOM_NAY';});
test('Bound bootstrap detects and persists only its own dashboard',()=>{assert.equal(ctx.jpSheet(),main);assert.equal(properties.get('JP_DASHBOARD_ID'),main.id);});
test('Bound bootstrap rejects ambiguous folder parents',()=>{mainParents=[today,today];assert.throws(()=>ctx.jpRoot());assert(!properties.has('JP_ROOT_FOLDER_ID'));mainParents=[today];});
test('Bound bootstrap rejects wrong project folder',()=>{root.name='Other project';assert.throws(()=>ctx.jpRoot());assert(!properties.has('JP_ROOT_FOLDER_ID'));root.name='JP-STUDY — HỌC TIẾNG NHẬT';});
test('Bound bootstrap detects unique project root without hardcoded IDs',()=>{assert.equal(ctx.jpRoot(),root);assert.equal(properties.get('JP_ROOT_FOLDER_ID'),root.id);});
test('Unlinked native destination exception is handled without masking unrelated errors',()=>{let linked='';ctx.jpEnsureDestination({getDestinationId(){throw Error('Exception: Biểu mẫu hiện không có đích trả lời.');},setDestination(t,id){linked=id;}},'expected');assert.equal(linked,'expected');assert.throws(()=>ctx.jpEnsureDestination({getDestinationId(){throw Error('permission denied');},setDestination(){assert.fail('must not replace');}},'expected'));});
test('Existing unexpected destination is never silently replaced',()=>{assert.throws(()=>ctx.jpEnsureDestination({getDestinationId(){return 'different';},setDestination(){assert.fail('must not replace');}},'expected'));});
test('P0 builds 3 unpublished Forms, 1 raw workbook and 3 triggers',()=>{ctx.setupP0();assert.equal(forms.size,3);assert.equal(sheets.size,2);assert.equal(triggers.length,3);assert([...forms.values()].every(f=>f.published===false&&!f.collectsEmail()&&!f.isPublishingSummary()));});test('P0 repeated setup is idempotent',()=>{ctx.setupP0();assert.equal(forms.size,3);assert.equal(triggers.length,3);});test('P1 builds remaining 7 / keys remain authoritative',()=>{ctx.setupRemaining();assert.equal(forms.size,10);assert.equal(triggers.length,10);assert.equal(ctx.auditForms(),10);});
let state=JSON.parse(properties.get('JP_STATE')),info=state.forms[quiz.id],form=forms.get(info.id);function response(id,mode,answers,fatigue=''){const vals={...answers,[info.modeId]:mode};if(fatigue)vals[info.fatigueId]=fatigue;return{getId:()=>id,getTimestamp:()=>new Date(id==='again'?'2026-10-18T00:00:00Z':'2026-10-15T00:00:00Z'),getItemResponses:()=>Object.entries(vals).map(([i,v])=>({getItem:()=>({getId:()=>Number(i)}),getResponse:()=>v}))};}
const answers={};quiz.questionIds.forEach((id,i)=>{if(i===4)return;const q=D.questions[id];answers[Object.keys(info.items).find(k=>info.items[k]===id)]=C.option(q,q.options.find(o=>i<2?o.id===q.correctAnswer:o.id!==q.correctAnswer));});const resp=response('real','Tự làm, chưa xem câu/khóa',answers,'3');
test('Adapter submission → raw store → history → error package',()=>{ctx.onQuizSubmit({source:form,response:resp});const raw=sheets.get(state.rawId).getSheetByName('CHI_TIET');assert.equal(raw.getLastRow(),6);const hs=main.getSheetByName('LỊCH SỬ').getRange('A4:N4').getValues()[0];assert.equal(hs[4],2);assert.equal(hs[5],5);assert.equal(hs[6],1);assert.equal(hs[12],3);assert(main.getSheetByName('LỖI CẦN ÔN').getRange('B9').getValue().includes('KHÓA')||main.getSheetByName('LỖI CẦN ÔN').getRange('B9').getValue().includes('Khóa'));});test('Adapter duplicate trigger does not append duplicate raw/history',()=>{ctx.onQuizSubmit({source:form,response:resp});assert.equal(sheets.get(state.rawId).getSheetByName('CHI_TIET').getLastRow(),6);assert.equal(main.getSheetByName('LỊCH SỬ').getLastRow(),4);});test('Synthetic live QA quarantined outside learner history',()=>{ctx.onQuizSubmit({source:form,response:response('synthetic','QA - Dữ liệu giả',answers)});assert.equal(sheets.get(state.rawId).getSheetByName('CHI_TIET').getLastRow(),6);assert.equal(sheets.get(state.rawId).getSheetByName('NHAT_KY_QA').getLastRow(),2);});test('Unpublished forms cannot become learner links',()=>assert.throws(()=>ctx.activateReady()));test('Published audited forms become links only after explicit owner acknowledgement',()=>{for(const f of forms.values())f.published=true;ctx.activateReady();assert.equal(main.getSheetByName('HỌC HÔM NAY').getRange('B7').getValue(),'MỞ BÀI NGẮN');assert(main.getSheetByName('HỌC HÔM NAY').links.get('7,2').includes('example.invalid'));assert(!adapter.includes('HYPERLINK('));});test('Export CSV/JSON and archived rerun preserve earlier exports',()=>{ctx.exportDailyReport();ctx.exportDailyReport();const tracking=root.children.find(f=>f.name==='05_THEO_DÕI_TIẾN_BỘ'),exports=tracking.children.find(f=>f.name==='BAO_CAO_XUAT');assert.equal(exports.files.length,4);assert.equal(exports.getFilesByName('DAILY_LEARNING_REPORT.csv').hasNext(),true);});test('Audit catches changed correct-choice mapping',()=>{const it=form.getItemById(Number(Object.keys(info.items)[0])),old=it.choices;it.choices=old.map((c,i)=>({getValue:()=>c.getValue(),isCorrectAnswer:()=>i===0}));if(old[0].isCorrectAnswer())it.choices=old.map((c,i)=>({getValue:()=>c.getValue(),isCorrectAnswer:()=>i===1}));assert.throws(()=>ctx.auditForms());it.choices=old;});
const acls=new Map([...forms.keys()].map(id=>[id,[{id:'owner',type:'user',role:'owner'},{id:'public',type:'anyone',role:'reader',view:'published'}]]));let removed=0;ctx.Drive={Permissions:{list:id=>({permissions:acls.get(id)}),remove:(id,pid)=>{const a=acls.get(id);assert(a.find(p=>p.id===pid&&p.type==='anyone'&&p.view==='published'));acls.set(id,a.filter(p=>p.id!==pid));removed++;}}};vm.runInContext(fs.readFileSync(path.join(R,'DRIVE_SETUP/live_qa.js'),'utf8'),ctx);
test('P0 ACL cleanup removes only public published responders, not P1',()=>{ctx.restrictP0Responders();assert.equal(removed,3);assert(D.quizzes.filter(q=>q.releaseGroup==='P0').every(q=>acls.get(state.forms[q.id].id).length===1));assert.equal(acls.get(state.forms['W01-B04'].id).length,2);});
test('Unexpected named participant prevents owner-only publication',()=>{acls.get(info.id).push({id:'other',type:'user',role:'reader',view:'published'});assert.throws(()=>ctx.jpOwnerOnly_(info.id));assert.equal(acls.get(info.id).length,2);acls.set(info.id,[{id:'owner',type:'user',role:'owner'}]);});
test('QA refresh refuses production target and unlabelled rows',()=>{assert.throws(()=>ctx.jpRefresh(state,{sheet:main,rows:en.map(r=>({...r,synthetic:true}))}));const isolated=new SS('isolated',['HỌC HÔM NAY','TUẦN NÀY','LỊCH SỬ','LỖI CẦN ÔN','BÁO CÁO QUẢN LÝ']);assert.throws(()=>ctx.jpRefresh(state,{sheet:isolated,rows:en}));});
test('QA history/error views are rendered in isolated sheet without learner writes',()=>{const before=JSON.stringify([...main.getSheetByName('LỊCH SỬ').data]),isolated=sheets.get('isolated');ctx.jpRefresh(state,{sheet:isolated,rows:en.map(r=>({...r,synthetic:true}))});assert.equal(isolated.getSheetByName('LỊCH SỬ').getRange('E4').getValue(),2);assert.equal(isolated.getSheetByName('LỊCH SỬ').getRange('G4').getValue(),1);assert.equal(JSON.stringify([...main.getSheetByName('LỊCH SỬ').data]),before);assert(isolated.getSheetByName('LỖI CẦN ÔN').getRange('B9').getValue().includes('Khóa'));});
test('Live QA refuses to copy a dashboard that already has learner rows',()=>assert.throws(()=>ctx.verifySyntheticQa(),/Có dữ liệu học thật/));

// ============================================================================
// PHASE 3.7 PILOT INTEGRATION TESTS (MOCK WORKSPACE ENVIRONMENT)
// Note: Uses deterministic Workspace mocks to verify data flow and control logic;
// not live Google Forms execution.
// ============================================================================

test('Pilot registered in effective runtime quiz registry and questions lookup', () => {
  const ed = ctx.jpEffectiveData();
  assert(ed.quizzes.some(q => q.id === 'MD-N4-VOC-01'));
  const pilotQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  assert.equal(pilotQuiz.questionIds.length, 5);
  for (const qid of pilotQuiz.questionIds) {
    assert(ed.questions[qid], 'Missing question ' + qid);
    assert.equal(ed.questions[qid].id, qid);
    assert.equal(ed.questions[qid].options.length, 4);
    assert(['A', 'B', 'C', 'D'].includes(ed.questions[qid].correctAnswer));
  }
  assert.equal(D.quizzes.length, 10);
  assert.equal(Object.keys(D.questions).length, 68);
});

let pilotDeployResult, pilotForm, pilotInfo;
test('Scenario K: deployPilotMdN4Voc01 creates Form, JP_MODES, trigger, destination and is idempotent', () => {
  const triggerCountBefore = triggers.length;
  const formCountBefore = forms.size;

  pilotDeployResult = ctx.deployPilotMdN4Voc01();
  assert.equal(pilotDeployResult.practiceSetId, 'MD-N4-VOC-01');
  assert.equal(pilotDeployResult.stage, 'FORM_CONFIG_AUDITED');
  assert.equal(pilotDeployResult.triggerInstalled, true);
  assert.equal(pilotDeployResult.modeConfigured, true);
  assert.equal(pilotDeployResult.partialSubmissionAllowed, true);

  assert.equal(forms.size, formCountBefore + 1);
  assert.equal(triggers.length, triggerCountBefore + 1);

  const curState = JSON.parse(properties.get('JP_STATE'));
  pilotInfo = curState.forms['MD-N4-VOC-01'];
  assert(pilotInfo && pilotInfo.built);
  assert(pilotInfo.modeId, 'Missing modeId in pilot form info');
  assert(pilotInfo.fatigueId, 'Missing fatigueId in pilot form info');
  assert.equal(Object.keys(pilotInfo.items).length, 5);

  pilotForm = forms.get(pilotInfo.id);
  assert(pilotForm);
  for (const item of pilotForm.getItems('MC')) {
    assert.equal(item.required, false, 'Question should be optional for partial submissions');
    assert.equal(item.points, 1);
  }

  const redeployResult = ctx.deployPilotMdN4Voc01();
  assert.equal(redeployResult.formId, pilotInfo.id);
  assert.equal(forms.size, formCountBefore + 1);
  assert.equal(triggers.length, triggerCountBefore + 1);
});

test('P0-2 Negative Control: Unverified pilot Form without QA submission remains inactive', () => {
  pilotForm.published = true;
  assert.equal(pilotInfo.active, false);
  assert.throws(() => ctx.activateReady(), /Pilot Form chưa có lượt nộp QA/);
  const curState = JSON.parse(properties.get('JP_STATE'));
  assert.equal(curState.forms['MD-N4-VOC-01'].active, false);
  assert.equal(pilotInfo.active, false);
});

test('P1 Content Audit: Mutated Japanese stem throws error and aborts audit', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const item0 = pilotForm.getItems('MC')[0];
  const origTitle = item0.getTitle();
  item0.setTitle('[N4-MO-READ-001] Mutated stem text');
  assert.throws(() => ctx.jpAuditOne(pQuiz, pilotInfo), /Stem\/passage không khớp canonical/);
  item0.setTitle(origTitle);
});

test('P1 Content Audit: Mutated question order throws error and aborts audit', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const mcItems = pilotForm.getItems('MC');
  const idx0 = pilotForm.items.indexOf(mcItems[0]);
  const idx1 = pilotForm.items.indexOf(mcItems[1]);
  pilotForm.items[idx0] = mcItems[1];
  pilotForm.items[idx1] = mcItems[0];
  assert.throws(() => ctx.jpAuditOne(pQuiz, pilotInfo), /Thứ tự câu hỏi không đúng thứ tự canonical/);
  pilotForm.items[idx0] = mcItems[0];
  pilotForm.items[idx1] = mcItems[1];
});

test('P1 Content Audit: Mutated choice order throws error and aborts audit', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const item0 = pilotForm.getItems('MC')[0];
  const origChoices = item0.getChoices();
  item0.setChoices([...origChoices].reverse());
  assert.throws(() => ctx.jpAuditOne(pQuiz, pilotInfo), /Khóa\/nhiễu lệch/);
  item0.setChoices(origChoices);
});

test('P1 Content Audit: Mutated points throws error and aborts audit', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const item0 = pilotForm.getItems('MC')[0];
  item0.setPoints(2);
  assert.throws(() => ctx.jpAuditOne(pQuiz, pilotInfo), /Khóa\/nhiễu lệch/);
  item0.setPoints(1);
});

test('P1 Content Audit: Mutated correct Vietnamese feedback throws error and aborts audit', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const item0 = pilotForm.getItems('MC')[0];
  const origFbC = item0.getFeedbackForCorrect();
  item0.setFeedbackForCorrect({ getText: () => 'Sai lời giải', text: 'Sai lời giải' });
  assert.throws(() => ctx.jpAuditOne(pQuiz, pilotInfo), /Feedback câu đúng không khớp canonical explanationVi/);
  item0.setFeedbackForCorrect(origFbC);
});

test('P1 Content Audit: Mutated incorrect Vietnamese distractor feedback throws error and aborts audit', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const item0 = pilotForm.getItems('MC')[0];
  const origFbI = item0.getFeedbackForIncorrect();
  item0.setFeedbackForIncorrect({ getText: () => 'Sai distractor', text: 'Sai distractor' });
  assert.throws(() => ctx.jpAuditOne(pQuiz, pilotInfo), /Feedback câu sai không khớp distractor explanations/);
  item0.setFeedbackForIncorrect(origFbI);
});

test('P1 Content Audit: Mutated setRequired(true) throws error and aborts audit', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const item0 = pilotForm.getItems('MC')[0];
  item0.setRequired(true);
  assert.throws(() => ctx.jpAuditOne(pQuiz, pilotInfo), /Câu hỏi phải là optional \(setRequired\(false\)\)/);
  item0.setRequired(false);
});

test('P1 Content Audit: Mutated content digest in pilot info throws error and aborts audit', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const origDigest = pilotInfo.contentDigest;
  pilotInfo.contentDigest = 'corrupted_digest_1234567890abcdef';
  assert.throws(() => ctx.jpAuditOne(pQuiz, pilotInfo), /Content digest không khớp canonical pilot payload/);
  pilotInfo.contentDigest = origDigest;
});

function makePilotResponse(respId, mode, answerMap, fatigue = '') {
  const vals = { ...answerMap, [pilotInfo.modeId]: mode };
  if (fatigue) vals[pilotInfo.fatigueId] = fatigue;
  return {
    getId: () => respId,
    getTimestamp: () => new Date('2026-10-17T12:00:00Z'),
    getItemResponses: () => Object.entries(vals).map(([i, v]) => ({
      getItem: () => ({ getId: () => Number(i) }),
      getResponse: () => v
    }))
  };
}

function getHistoryRow(submissionId) {
  const sh = main.getSheetByName('LỊCH SỬ');
  const count = sh.getLastRow() - 3;
  if (count < 1) return null;
  const rows = sh.getRange(4, 1, count, 14).getValues();
  return rows.find(r => String(r[13]).endsWith(submissionId)) || null;
}


test('Scenario A: Pilot 5 correct answers yields 5/5 score in history', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const ansA = {};
  for (const qid of pQuiz.questionIds) {
    const q = ed.questions[qid];
    const itemKey = Object.keys(pilotInfo.items).find(k => pilotInfo.items[k] === qid);
    const correctOpt = q.options.find(o => o.id === q.correctAnswer);
    ansA[itemKey] = C.option(q, correctOpt);
  }
  const curState = JSON.parse(properties.get('JP_STATE'));
  const rawBefore = sheets.get(curState.rawId).getSheetByName('CHI_TIET').getLastRow();
  const respA = makePilotResponse('pilot-resp-A', 'Tự làm, chưa xem câu/khóa', ansA, '2');
  ctx.onQuizSubmit({ source: pilotForm, response: respA });

  const rawAfter = sheets.get(curState.rawId).getSheetByName('CHI_TIET').getLastRow();
  assert.equal(rawAfter, rawBefore + 5);

  const histValues = getHistoryRow('pilot-resp-A');
  assert(histValues, 'History row must exist for pilot-resp-A');
  assert.equal(histValues[1], 'MD-N4-VOC-01');
  assert.equal(histValues[4], 5);
  assert.equal(histValues[5], 5);
  assert.equal(histValues[6], 0);
  assert.equal(histValues[10], 'Đã nộp đủ');
});

test('Scenario G: Trigger fires twice idempotently without duplicating raw or history', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const curState = JSON.parse(properties.get('JP_STATE'));
  const rawBefore = sheets.get(curState.rawId).getSheetByName('CHI_TIET').getLastRow();
  const histRowsBefore = main.getSheetByName('LỊCH SỬ').getLastRow();

  const ansA = {};
  for (const qid of pQuiz.questionIds) {
    const q = ed.questions[qid];
    const itemKey = Object.keys(pilotInfo.items).find(k => pilotInfo.items[k] === qid);
    ansA[itemKey] = C.option(q, q.options.find(o => o.id === q.correctAnswer));
  }
  const respA = makePilotResponse('pilot-resp-A', 'Tự làm, chưa xem câu/khóa', ansA, '2');
  ctx.onQuizSubmit({ source: pilotForm, response: respA });

  const rawAfter = sheets.get(curState.rawId).getSheetByName('CHI_TIET').getLastRow();
  const histRowsAfter = main.getSheetByName('LỊCH SỬ').getLastRow();
  assert.equal(rawAfter, rawBefore);
  assert.equal(histRowsAfter, histRowsBefore);
});

test('Scenario B: Pilot 5 wrong answers yields 0/5 score and records mistakes', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const ansB = {};
  for (const qid of pQuiz.questionIds) {
    const q = ed.questions[qid];
    const itemKey = Object.keys(pilotInfo.items).find(k => pilotInfo.items[k] === qid);
    const wrongOpt = q.options.find(o => o.id !== q.correctAnswer);
    ansB[itemKey] = C.option(q, wrongOpt);
  }
  const respB = makePilotResponse('pilot-resp-B', 'Tự làm, chưa xem câu/khóa', ansB, '4');
  ctx.onQuizSubmit({ source: pilotForm, response: respB });

  const histValues = getHistoryRow('pilot-resp-B');
  assert(histValues, 'History row must exist for pilot-resp-B');
  assert.equal(histValues[1], 'MD-N4-VOC-01');
  assert.equal(histValues[4], 0);
  assert.equal(histValues[5], 5);
  assert.equal(histValues[6], 0);
  assert.equal(histValues[11], pQuiz.questionIds.join(', '));
});

test('Scenario C: Pilot mix of 3 correct and 2 wrong yields 3/5', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const ansC = {};
  pQuiz.questionIds.forEach((qid, idx) => {
    const q = ed.questions[qid];
    const itemKey = Object.keys(pilotInfo.items).find(k => pilotInfo.items[k] === qid);
    const opt = (idx < 3) ? q.options.find(o => o.id === q.correctAnswer) : q.options.find(o => o.id !== q.correctAnswer);
    ansC[itemKey] = C.option(q, opt);
  });
  const respC = makePilotResponse('pilot-resp-C', 'Tự làm, chưa xem câu/khóa', ansC, '1');
  ctx.onQuizSubmit({ source: pilotForm, response: respC });

  const histValues = getHistoryRow('pilot-resp-C');
  assert(histValues, 'History row must exist for pilot-resp-C');
  assert.equal(histValues[1], 'MD-N4-VOC-01');
  assert.equal(histValues[4], 3);
  assert.equal(histValues[5], 5);
  assert.equal(histValues[6], 0);
});

test('Scenario D: Pilot partial submission (3 answered, 2 blank) recorded with unanswered=2', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const ansD = {};
  pQuiz.questionIds.forEach((qid, idx) => {
    if (idx >= 3) return;
    const q = ed.questions[qid];
    const itemKey = Object.keys(pilotInfo.items).find(k => pilotInfo.items[k] === qid);
    const opt = (idx < 2) ? q.options.find(o => o.id === q.correctAnswer) : q.options.find(o => o.id !== q.correctAnswer);
    ansD[itemKey] = C.option(q, opt);
  });
  const respD = makePilotResponse('pilot-resp-D', 'Tự làm, chưa xem câu/khóa', ansD);
  ctx.onQuizSubmit({ source: pilotForm, response: respD });

  const histValues = getHistoryRow('pilot-resp-D');
  assert(histValues, 'History row must exist for pilot-resp-D');
  assert.equal(histValues[1], 'MD-N4-VOC-01');
  assert.equal(histValues[4], 2);
  assert.equal(histValues[5], 5);
  assert.equal(histValues[6], 2);
  assert.equal(histValues[10], 'Đã nộp một phần');
});

test('Scenario E: Synthetic QA mode is quarantined to NHAT_KY_QA, absent from CHI_TIET and history', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const curState = JSON.parse(properties.get('JP_STATE'));
  const rawBefore = sheets.get(curState.rawId).getSheetByName('CHI_TIET').getLastRow();
  const qaBefore = sheets.get(curState.rawId).getSheetByName('NHAT_KY_QA').getLastRow();

  const ansE = {};
  for (const qid of pQuiz.questionIds) {
    const q = ed.questions[qid];
    const itemKey = Object.keys(pilotInfo.items).find(k => pilotInfo.items[k] === qid);
    ansE[itemKey] = C.option(q, q.options.find(o => o.id === q.correctAnswer));
  }
  const respE = makePilotResponse('pilot-synthetic-001', 'QA - Dữ liệu giả', ansE);
  ctx.onQuizSubmit({ source: pilotForm, response: respE });

  const rawAfter = sheets.get(curState.rawId).getSheetByName('CHI_TIET').getLastRow();
  const qaAfter = sheets.get(curState.rawId).getSheetByName('NHAT_KY_QA').getLastRow();
  assert.equal(rawAfter, rawBefore, 'CHI_TIET must not receive synthetic rows');
  assert.equal(qaAfter, qaBefore + 1, 'NHAT_KY_QA must receive the quarantined record');
});

test('Scenario F: Learner mode records responses in CHI_TIET and updates summary/history', () => {
  const curState = JSON.parse(properties.get('JP_STATE'));
  const rows = sheets.get(curState.rawId).getSheetByName('CHI_TIET').getRange(2, 2, sheets.get(curState.rawId).getSheetByName('CHI_TIET').getLastRow() - 1, 1).getValues().map(r => JSON.parse(r[0]));
  const pilotRows = rows.filter(r => r.quizId === 'MD-N4-VOC-01');
  assert(pilotRows.length > 0, 'Pilot learner rows exist in CHI_TIET');
  assert(pilotRows.every(r => r.quizId === 'MD-N4-VOC-01'));
  assert(pilotRows.some(r => r.result === 'correct'));
  assert(pilotRows.some(r => r.result === 'incorrect'));
  assert(pilotRows.some(r => r.result === 'unanswered'));
});

test('Scenario H: syncResponses recovers missed Form responses', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const ansH = {};
  for (const qid of pQuiz.questionIds) {
    const q = ed.questions[qid];
    const itemKey = Object.keys(pilotInfo.items).find(k => pilotInfo.items[k] === qid);
    ansH[itemKey] = C.option(q, q.options.find(o => o.id === q.correctAnswer));
  }
  const missedResp = makePilotResponse('pilot-missed-001', 'Tự làm, chưa xem câu/khóa', ansH, '1');
  pilotForm.responses.push(missedResp);

  const curState = JSON.parse(properties.get('JP_STATE'));
  const rawBefore = sheets.get(curState.rawId).getSheetByName('CHI_TIET').getLastRow();
  ctx.syncResponses();
  const rawAfter = sheets.get(curState.rawId).getSheetByName('CHI_TIET').getLastRow();
  assert.equal(rawAfter, rawBefore + 5, 'syncResponses must recover the 5 items from missed submission');
});

test('Scenario I: Submission from unknown form ID throws Error("Không biết form")', () => {
  const fakeForm = { getId: () => 'form-totally-unknown' };
  assert.throws(() => ctx.onQuizSubmit({ source: fakeForm, response: { getId: () => 'fake' } }), /Không biết form/);
});

test('Scenario J: Old P0 Form W01-B01 continues to process correctly after pilot deployment', () => {
  const p0State = JSON.parse(properties.get('JP_STATE'));
  const p0Info = p0State.forms['W01-B01'];
  const p0Form = forms.get(p0Info.id);
  const p0Quiz = D.quizzes.find(q => q.id === 'W01-B01');

  const p0Ans = {};
  p0Quiz.questionIds.forEach((qid, idx) => {
    const q = D.questions[qid];
    const itemKey = Object.keys(p0Info.items).find(k => p0Info.items[k] === qid);
    p0Ans[itemKey] = C.option(q, q.options.find(o => o.id === q.correctAnswer));
  });
  const p0Resp = response('p0-preservation-test', 'Tự làm, chưa xem câu/khóa', p0Ans, '2');
  const rawBefore = sheets.get(p0State.rawId).getSheetByName('CHI_TIET').getLastRow();
  ctx.onQuizSubmit({ source: p0Form, response: p0Resp });
  const rawAfter = sheets.get(p0State.rawId).getSheetByName('CHI_TIET').getLastRow();
  assert.equal(rawAfter, rawBefore + p0Quiz.questionIds.length);
});

test('Scenario L: Pilot questions in jpEffectiveData match canonical QUESTION_BANK_EXPANDED', () => {
  const ed = ctx.jpEffectiveData();
  const pQuiz = ed.quizzes.find(q => q.id === 'MD-N4-VOC-01');
  const bankData = JSON.parse(fs.readFileSync(path.join(R, 'curriculum/QUESTION_BANK_EXPANDED.json'), 'utf8'));
  const bankMap = Object.fromEntries(bankData.questions.map(q => [q.id, q]));
  for (const qid of pQuiz.questionIds) {
    const bankQ = bankMap[qid];
    const pilotQ = ed.questions[qid];
    assert.equal(pilotQ.stem, bankQ.stem, 'Stem mismatch for ' + qid);
    assert.equal(pilotQ.correctAnswer, bankQ.correctAnswer, 'Answer mismatch for ' + qid);
    assert.equal(pilotQ.explanationVi, bankQ.explanationVi, 'Explanation mismatch for ' + qid);
    assert.equal(JSON.stringify(pilotQ.options.map(o => o.text)), JSON.stringify(bankQ.options.map(o => o.text)), 'Options mismatch for ' + qid);
  }
});

test('P0-2 Positive Control: Verified pilot Form with synthetic QA in NHAT_KY_QA activates successfully', () => {
  pilotForm.published = true;
  ctx.activateReady();
  const curState = JSON.parse(properties.get('JP_STATE'));
  assert.equal(curState.forms['MD-N4-VOC-01'].active, true);
  pilotInfo = curState.forms['MD-N4-VOC-01'];
  assert.equal(pilotInfo.active, true);
});

test('P0-2 Gate: Missing trigger onQuizSubmit prevents activation', () => {
  const trigIdx = triggers.findIndex(t => t.getHandlerFunction() === 'onQuizSubmit' && t.getTriggerSourceId() === pilotInfo.id);
  assert(trigIdx >= 0);
  const removedTrigger = triggers.splice(trigIdx, 1)[0];
  assert.throws(() => ctx.activateReady(), /Thiếu trigger onQuizSubmit/);
  triggers.push(removedTrigger);
});

test('P0-2 Gate: Mismatched destination Sheet prevents activation', () => {
  const origDest = pilotForm.destination;
  pilotForm.destination = 'other_raw_sheet_id';
  assert.throws(() => ctx.activateReady(), /Đích phản hồi của pilot Form không khớp/);
  pilotForm.destination = origDest;
});

test('P0-2 Gate: Mismatched content digest prevents activation', () => {
  const s = JSON.parse(properties.get('JP_STATE'));
  const origDigest = s.forms['MD-N4-VOC-01'].contentDigest;
  s.forms['MD-N4-VOC-01'].contentDigest = 'corrupted_digest_xyz';
  properties.set('JP_STATE', JSON.stringify(s));
  assert.throws(() => ctx.activateReady(), /Content digest.*không khớp/);
  s.forms['MD-N4-VOC-01'].contentDigest = origDigest;
  properties.set('JP_STATE', JSON.stringify(s));
});

test('P1 Silent Modification Guard: Rebuilding Form with existing learner rows in CHI_TIET throws error', () => {
  const s = JSON.parse(properties.get('JP_STATE'));
  s.forms['MD-N4-VOC-01'].built = false;
  properties.set('JP_STATE', JSON.stringify(s));
  assert.throws(() => ctx.deployPilotMdN4Voc01(), /Form đã có dữ liệu người học/);
  s.forms['MD-N4-VOC-01'].built = true;
  properties.set('JP_STATE', JSON.stringify(s));
});

const report={scope:'Node pure logic + Workspace mocks; NOT real Google Forms grading, triggers or mobile UI verification',tests:results,passed:results.filter(x=>x.ok).length,failed:results.filter(x=>!x.ok).length};fs.writeFileSync(path.join(R,'tmp/drive-first/tests.json'),JSON.stringify(report,null,2));console.log(JSON.stringify({tests:results.length,passed:report.passed,failed:results.filter(x=>!x.ok)}));if(report.failed)process.exitCode=1;
