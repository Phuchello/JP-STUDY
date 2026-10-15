import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const tmp=path.dirname(fileURLToPath(import.meta.url)),root=path.resolve(tmp,'../..'),out=path.join(root,'FINAL_V3');
const manifest=JSON.parse(await fs.readFile(path.join(root,'tmp/jlpt-v2/manifest.json'),'utf8'));
// Transcribed from official tables, checked against both rendered pages and extracted tables.
const verified={
 'N4-G1':[3,4,2,1,4,1],'N4-G2':[1,2,3,1,4,2,3],
 'N4-V':[3,4,2,3,1,2,2,2,3,1],'N4-R':[4,3,1,2,3],
 'N4-L1':[1,3,1,2],'N4-L2':[2,2,1,3],
 'N3-G':[2,4,3,1,2,4],'N3-V':[4,2,4,3,2,4,4,1,3,2],
 'N3-R':[3,2,3,4],'N3-L1':[2,3,2,4],'N3-L2':[3,4,1,2,1,3]
};
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(path.join(root,'FINAL/JLPT_PROGRESS_TRACKER_v2.xlsx')));
const quick=wb.worksheets.add('Làm nhanh'),diag=wb.worksheets.getItem('Chẩn đoán'),dash=wb.worksheets.getItem('Tổng hợp tuần'),scores=wb.worksheets.getItem('Đo năng lực');
const set=(s,a,v)=>s.getRange(a).values=[[v]],fx=(s,a,f)=>s.getRange(a).formulas=[[f]],val=(s,a)=>s.getRange(a).values[0][0];
const errors=['V','G','R','A','M','T','F'],links=[];
const navy='#314C62',amber='#FFF7DE',pale='#F1F5F8';
function input(s,a){s.getRange(a).format.fill=amber;}
function link(s,a,url,label){set(s,a,label);s.getRange(a).format.font={name:'Arial',size:11,color:'#234E72',underline:'single'};links.push({sheet:s.name,address:a,url,label});}
quick.showGridLines=false;quick.tabColor=navy;
quick.getRange('A1:Y185').format={font:{name:'Arial',size:11,color:'#20282E'},rowHeight:28,verticalAlignment:'center'};
[17,15,14,14,14,16,15].forEach((v,i)=>quick.getRangeByIndexes(0,i,185,1).format.columnWidth=v);
set(quick,'A2','Làm một khối rồi dừng');quick.getRange('A2').format.font={name:'Arial',size:16,bold:true};
set(quick,'A4','1. Mở đề. 2. Ghi lựa chọn. 3. Chọn Xong. 4. Ghi ngày/phút/loại câu.');
set(quick,'A5','Vàng để nhập. 0 = bỏ câu; trống = chưa làm. Không mở khóa khi đang đo.');
set(quick,'A6','Mỗi khối chọn một chế độ. Đã có lịch sử thì giữ nguyên, không ghi đè lần đầu.');
manifest.blocks.forEach((b,i)=>{
 const c=String.fromCharCode(65+i%6),r=7+Math.floor(i/6),a=10+14*i,s=172+i,n=b.questions.length;
 b.quick={top:a,answers:b.questions.map((q,j)=>`${String.fromCharCode(66+j%6)}${a+(j<6?3:5)}`),date:`B${a+6}`,minutes:`D${a+6}`,type:`F${a+6}`,finish:`B${a+7}`,error:`B${a+11}`,status:`B${a+8}`,result:`B${a+9}`,review:`B${a+10}`,summary:s};
 link(quick,`${c}${r}`,`#'Làm nhanh'!A${a}`,b.code);
 set(quick,`A${a}`,`${b.code} · ${b.skill} · ${b.limit} phút làm`);
 quick.getRange(`A${a}:G${a}`).format={fill:navy,font:{name:'Arial',size:12,bold:true,color:'#FFFFFF'},rowHeight:30};
 set(quick,`A${a+1}`,'Nguồn JLPT');link(quick,`B${a+1}`,b.url,'Mở đề');link(quick,`E${a+1}`,`https://www.jlpt.jp/samples/sample2018/pdf/${b.level}answer.pdf`,'Khóa sau khi làm');
 set(quick,`A${a+2}`,'Câu');set(quick,`A${a+3}`,'Bạn chọn');
 if(n>6){set(quick,`A${a+4}`,'Câu tiếp');set(quick,`A${a+5}`,'Bạn chọn');}
 for(let j=0;j<n;j++){
  const addr=b.quick.answers[j],max=b.part==='L'&&((b.level==='N4'&&Number(String(b.questions[j])[1])>=3)||(b.level==='N3'&&Number(String(b.questions[j])[1])>=4))?3:4;
  set(quick,addr.replace(/\d+/,x=>String(Number(x)-1)),String(b.questions[j]));input(quick,addr);quick.getRange(addr).format.horizontalAlignment='center';quick.getRange(addr).format.borders={preset:'all',style:'thin',color:'#D9D9D9'};
  quick.dataValidations.add({range:addr,rule:{type:'whole',operator:'between',formula1:0,formula2:max}});
  const qr=b.start_row+j;set(diag,`M${qr}`,b.code+':'+b.questions[j]);set(diag,`N${qr}`,verified[b.code][j]);set(diag,`O${qr}`,`${b.level}answer.pdf p${b.part==='L'||b.part==='R'?2:1}`);
  fx(quick,`I${qr+8}`,`=IF(ISBLANK(${addr}),0,IF(ISNUMBER(${addr}),IF(AND(${addr}>=0,${addr}<=${max},MOD(${addr},1)=0),1,-1),-1))`);
  fx(quick,`J${qr+8}`,`=IF(I${qr+8}=1,IF(${addr}='Chẩn đoán'!N${qr},1,0),0)`);
 }
 const q=b.quick;
 for(const [c,label] of [['A','Ngày thật'],['C','Phút làm'],['E','Loại câu']])set(quick,`${c}${a+6}`,label);
 input(quick,q.date);input(quick,q.minutes);input(quick,q.type);quick.getRange(q.date).setNumberFormat('dd/mm/yyyy');
 quick.dataValidations.add({range:q.date,rule:{type:'whole',operator:'between',formula1:1,formula2:2958465}});
 quick.dataValidations.add({range:q.minutes,rule:{type:'decimal',operator:'between',formula1:.01,formula2:180}});
 quick.getRange(q.type).dataValidation={rule:{type:'list',values:['Mới','Ôn lại']}};
 set(quick,`A${a+7}`,'Chấm sau giờ');input(quick,q.finish);quick.getRange(q.finish).dataValidation={rule:{type:'list',values:['Xong']}};
 set(quick,`D${a+7}`,'Dở dang: để nguyên; chưa chọn Xong.');
 set(quick,`A${a+8}`,'Trạng thái');set(quick,`A${a+9}`,'Kết quả');set(quick,`A${a+10}`,'Câu cần sửa');set(quick,`A${a+11}`,'Lỗi chính');input(quick,q.error);quick.getRange(q.error).dataValidation={rule:{type:'list',values:errors}};
 link(quick,`E${a+11}`,`#'Tổng hợp tuần'!A2`,'Xem tuần');set(quick,`A${a+12}`,'Tiếp theo');
 const sr=b.summary_row,st=b.start_row+8,en=b.end_row+8;
 set(quick,`I${s}`,b.code);set(quick,`K${s}`,n);set(quick,`Y${s}`,n);
 fx(quick,`R${s}`,`=SUM(${q.answers.map(x=>`IF(ISBLANK(${x}),0,1)`).join(',')})`);
 fx(quick,`S${s}`,`=COUNTIF(I${st}:I${en},-1)`);fx(quick,`T${s}`,`=SUM(J${st}:J${en})`);
 fx(quick,`U${s}`,`=COUNTA('Chẩn đoán'!F${b.start_row}:H${b.end_row},'Chẩn đoán'!H${sr}:J${sr})`);
 fx(quick,`V${s}`,`=COUNTA(${[...q.answers,q.date,q.minutes,q.type,q.finish,q.error].join(',')})`);
 const dateok=`IF(ISNUMBER(${q.date}),AND(${q.date}>=1,${q.date}<=2958465,MOD(${q.date},1)=0),FALSE)`;
 const timeok=`IF(ISNUMBER(${q.minutes}),AND(${q.minutes}>0,${q.minutes}<=180),FALSE)`;
 fx(quick,`W${s}`,`=IF(V${s}=0,"Chưa làm",IF(S${s}>0,"Sửa đáp án",IF(R${s}<K${s},"Còn "&(K${s}-R${s})&" câu",IF(${q.finish}<>"Xong","Chọn Xong để chấm",IF(NOT(${dateok}),"Thiếu/sai ngày",IF(NOT(${timeok}),"Thiếu/sai phút",IF(AND(${q.type}<>"Mới",${q.type}<>"Ôn lại"),"Chọn Mới/Ôn lại",IF(AND(LEN(${q.error})>0,COUNTIF('Nhật ký'!$I$63:$I$69,${q.error})=0),"Sửa mã lỗi","Đã chấm"))))))))`);
 fx(quick,`J${s}`,`=IF(AND(U${s}>0,V${s}>0),"Trùng hai chế độ",IF(U${s}>0,"Chi tiết",IF(V${s}>0,"Nhanh","")))`);
 fx(quick,`P${s}`,`=IF(J${s}="Trùng hai chế độ",J${s},IF(J${s}="Chi tiết",'Chẩn đoán'!K${sr},W${s}))`);
 for(const [col,qa,da] of [['L',`T${s}`,`F${sr}`],['M',q.date,`H${sr}`],['N',q.minutes,`I${sr}`],['O',q.type,`J${sr}`]])fx(quick,`${col}${s}`,`=IF(P${s}="Đã chấm",IF(J${s}="Chi tiết",'Chẩn đoán'!${da},${qa}),"")`);
 fx(quick,`Q${s}`,`=IF(AND(P${s}="Đã chấm",J${s}="Nhanh",LEN(${q.error})>0),${q.error},"")`);
 const reveal=`AND(${q.finish}="Xong",R${s}=K${s},S${s}=0)`;
 const list=q.answers.map((ad,j)=>`IF(${ad}='Chẩn đoán'!N${b.start_row+j},"","${b.questions[j]}, ")`).join('&');
 fx(quick,`X${s}`,`=IF(${reveal},${list},"")`);
 fx(quick,q.status,`=P${s}`);fx(quick,q.result,`=IF(${reveal},T${s}&"/"&K${s}&" đúng; 0 vẫn tính bỏ câu","Đã ghi "&R${s}&"/"&K${s}&"; chưa hiện điểm")`);
 fx(quick,q.review,`=IF(${reveal},IF(X${s}="","Không có câu sai/bỏ",X${s}),"Chỉ hiện sau khi làm xong")`);
 fx(quick,`B${a+12}`,`=IF(P${s}="Đã chấm","Chọn 1 lỗi để chữa 5-10 phút rồi dừng.",IF(P${s}="Trùng hai chế độ","Giữ lịch sử ở Chẩn đoán; xóa bản nhập trùng ở đây.","Hoàn tất khi đủ sức; không ép làm khối tiếp."))`);
 for(const line of [a+8,a+9,a+10,a+12]){quick.getRange(`B${line}:G${line}`).merge();quick.getRange(`B${line}:G${line}`).format={fill:pale,font:{name:'Arial',size:11},wrapText:true,rowHeight:32};}
 quick.getRange(`A${a}:G${a}`).merge();quick.getRange(`E${a+1}:G${a+1}`).merge();quick.getRange(`D${a+7}:G${a+7}`).merge();
 quick.getRange(q.status).conditionalFormats.addCustom(`AND(${q.status}<>"Đã chấm",${q.status}<>"Chưa làm")`,{font:{color:'#9C2F2F'}});
});
for(const r of [4,5,6])quick.getRange(`A${r}:G${r}`).merge();
set(diag,'M6','Khóa chính thức 2018, chỉ dùng tự học cá nhân; phần phụ trợ ẩn để tránh xem trước.');
set(diag,'M7','Mã câu');set(diag,'N7','Khóa đã đối chiếu');set(diag,'O7','Vị trí nguồn');
set(diag,'M75','Source: Official Worldwide Japanese-Language Proficiency Test Website (https://www.jlpt.jp/)');
set(diag,'M76','N4answer.pdf và N3answer.pdf; JLPT Site Policy mục 1(1), kiểm 15/10/2026. Không tái bản nội dung đề/âm thanh.');
set(diag,'A4','Chế độ chi tiết được giữ nguyên. Mỗi khối chọn một chế độ: trang này hoặc Làm nhanh.');
const groups=[[0],[0,1],[3],[4,5],[7],[6],[8],[9,10]]; // vocab group corrected below
groups[0]=[2];
for(let i=0;i<groups.length;i++){
 const rs=groups[i].map(j=>172+j),r=72+i,ready=`AND(${rs.map(x=>`'Làm nhanh'!P${x}="Đã chấm"`).join(',')})`,sum=col=>rs.map(x=>`'Làm nhanh'!${col}${x}`).join(',');
 fx(scores,`A${r}`,`=IF(${ready},MAX(${sum('M')}),"")`);
 fx(scores,`E${r}`,`=IF(${ready},IF(AND(${rs.map(x=>`'Làm nhanh'!O${x}="Mới"`).join(',')}),"Mới","Ôn lại"),"")`);
 for(const [c,s] of [['F','L'],['G','K'],['H','N']])fx(scores,`${c}${r}`,`=IF(${ready},SUM(${sum(s)}),"")`);
}
fx(dash,'B31',`=COUNTIF('Làm nhanh'!$P$172:$P$177,"Đã chấm")&"/6 khối"`);fx(dash,'E31',`=COUNTIF('Làm nhanh'!$P$178:$P$182,"Đã chấm")&"/5 khối"`);
link(dash,'A33',`#'Làm nhanh'!B13`,'Mở Làm nhanh');
set(dash,'A38','Ngày bắt đầu thật');input(dash,'B38');dash.getRange('B38').setNumberFormat('dd/mm/yyyy');
set(dash,'C38','D7 (+7 ngày)');set(dash,'E38','D14 (+14 ngày)');
const startValid='IF(ISNUMBER($B$38),AND($B$38>=1,$B$38<=2958451,MOD($B$38,1)=0),FALSE)';
for(const [c,n] of [['D',7],['F',14]])fx(dash,`${c}38`,`=IF(${startValid},B38+${n},"Chưa đủ dữ liệu")`);
dash.getRange('D38').setNumberFormat('dd/mm/yyyy');dash.getRange('F38').setNumberFormat('dd/mm/yyyy');
dash.dataValidations.add({range:'B38',rule:{type:'whole',operator:'between',formula1:1,formula2:2958451}});
set(dash,'A40','D7: dữ liệu để xem');set(dash,'A41','D14: dữ liệu để so');
set(dash,'A43','B38 không đổi ngày lịch sử. Đổi B4 để xem tuần chứa ngày hoàn tất.');
set(dash,'A44','Chưa đủ dữ liệu là trạng thái hợp lệ; không tính khả năng đỗ N2.');
for(const [r,days] of [[40,7],[41,14]]){
 const crit=`'Đo năng lực'!$A$8:$A$79,">="&$B$38,'Đo năng lực'!$A$8:$A$79,"<="&($B$38+${days}),'Đo năng lực'!$B$8:$B$79,"N4",'Đo năng lực'!$E$8:$E$79,"Mới",'Đo năng lực'!$L$8:$L$79,"Hợp lệ"`;
 const count=(skill)=>`SUMIFS('Đo năng lực'!$G$8:$G$79,${crit},'Đo năng lực'!$C$8:$C$79,"${skill}")`;
 const criteria=[`COUNTIFS('Nhật ký'!$A$8:$A$59,">="&$B$38,'Nhật ký'!$A$8:$A$59,"<="&($B$38+${days}),'Nhật ký'!$J$8:$J$59,"Hợp lệ")>=3`,`${count('Ngữ pháp')}>=10`,`${count('Đọc')}>=5`,`${count('Nghe')}>=5`];
 if(days===14)criteria.push(`COUNTIFS(${crit},'Đo năng lực'!$C$8:$C$79,"Ngữ pháp")>=2`);
 fx(dash,`B${r}`,`=IF(NOT(${startValid}),"Chưa đủ dữ liệu",IF(AND(${criteria.join(',')}),"Có dữ liệu; tự đối chiếu trang 11","Chưa đủ dữ liệu"))`);
}
dash.getRange('A38:G44').format.font={name:'Arial',size:10};dash.getRange('A38:G44').format.rowHeight=29;
for(const r of [40,41])dash.getRange(`B${r}:G${r}`).merge();
for(let i=0;i<7;i++){
 const f=dash.getRange(`F${7+i}`).formulas[0][0];fx(dash,`F${7+i}`,f+`+COUNTIFS('Làm nhanh'!$M$172:$M$182,">="&$B$4,'Làm nhanh'!$M$172:$M$182,"<"&($B$4+7),'Làm nhanh'!$Q$172:$Q$182,E${7+i},'Làm nhanh'!$P$172:$P$182,"Đã chấm")`);
}
// Behavioral checks, then restore the input snapshot. No test scores remain in output.
const checks=[];function check(name,a,e){const ok=typeof e==='number'?typeof a==='number'&&Math.abs(a-e)<1e-9:JSON.stringify(a)===JSON.stringify(e);checks.push({name,actual:a,expected:e,ok});if(!ok)throw Error(JSON.stringify(checks.at(-1)));}
const q0=manifest.blocks[0].quick,q1=manifest.blocks[1].quick;
const serial=(y,m,d)=>(Date.UTC(y,m-1,d)-Date.UTC(1899,11,30))/86400000;
check('Blank quick answers remain unknown',val(quick,q0.status),'Chưa làm');check('Missing start date gives insufficient D7',val(dash,'D38'),'Chưa đủ dữ liệu');
function fill(b,arr){b.quick.answers.forEach((a,i)=>set(quick,a,arr[i]??null));}
function metadata(b){set(quick,b.quick.date,serial(2026,10,20));set(quick,b.quick.minutes,b.limit);set(quick,b.quick.type,'Mới');set(quick,b.quick.finish,'Xong');}
fill(manifest.blocks[0],[3,4]);check('Partial first block retained',val(quick,q0.status),'Còn 4 câu');check('Partial result not leaked',val(quick,q0.review),'Chỉ hiện sau khi làm xong');
fill(manifest.blocks[0],[3,4,2,1,4,1]);check('Completed unsubmitted block has no feedback',val(quick,q0.status),'Chọn Xong để chấm');
set(quick,q0.finish,'Xong');check('Grading before date still shows correct total',val(quick,q0.result),'6/6 đúng; 0 vẫn tính bỏ câu');check('Missing date blocked',val(quick,q0.status),'Thiếu/sai ngày');
metadata(manifest.blocks[0]);check('Completed block',val(quick,q0.status),'Đã chấm');check('First grammar block alone cannot create aggregate',val(scores,'F73'),'');
set(quick,q0.minutes,null);check('Missing minutes blocked',val(quick,q0.status),'Thiếu/sai phút');set(quick,q0.minutes,6);set(quick,q0.type,null);check('Missing new/review type blocked',val(quick,q0.status),'Chọn Mới/Ôn lại');set(quick,q0.type,'Mới');
for(const x of [5,-1,1.5,'abc']){set(quick,'B13',x);check('Invalid answer '+x,val(quick,q0.status),'Sửa đáp án');}set(quick,'B13',3);
set(quick,q0.date,'2026-10-20');check('Text date is not coerced silently',val(quick,q0.status),'Thiếu/sai ngày');set(quick,q0.date,serial(2026,10,20));
fill(manifest.blocks[0],[0,0,0,0,0,0]);check('Explicit skips are real zero',val(quick,q0.result),'0/6 đúng; 0 vẫn tính bỏ câu');check('Skipped question in review list',val(quick,q0.review),'1, 2, 3, 4, 5, 6, ');
set(quick,'B13',null);check('Blank differs from explicit skip',val(quick,q0.status),'Còn 1 câu');
fill(manifest.blocks[0],verified['N4-G1']);set(quick,'G13',2);check('Wrong item list',val(quick,q0.review),'6, ');check('Five of six arithmetic',val(quick,q0.result),'5/6 đúng; 0 vẫn tính bỏ câu');
set(diag,'F8',3);check('Two modes cannot double count',val(quick,q0.status),'Trùng hai chế độ');set(diag,'F8',null);
fill(manifest.blocks[1],verified['N4-G2']);metadata(manifest.blocks[1]);check('Two complete grammar blocks aggregate',val(scores,'F73'),12);check('Grammar denominator',val(scores,'G73'),13);
set(dash,'B4',serial(2026,10,20));check('Weekly quick data used',val(dash,'D19'),13);check('Weekly quick accuracy',val(dash,'E19'),12/13);
set(quick,q1.type,'Ôn lại');check('Mixed review/new becomes review',val(scores,'E73'),'Ôn lại');check('Review excluded from new weekly score',val(dash,'E19'),'');set(quick,q1.type,'Mới');
set(dash,'B38',serial(2026,10,20));check('D7 dynamic',val(dash,'D38'),serial(2026,10,27));check('D14 dynamic',val(dash,'F38'),serial(2026,11,3));check('Not enough learning evidence still insufficient',val(dash,'B40'),'Chưa đủ dữ liệu');
for(const bad of [0,-1,1.5,'abc',2958465]){set(dash,'B38',bad);check('Invalid actual start '+bad,val(dash,'D38'),'Chưa đủ dữ liệu');check('Invalid start does not enable checkpoint '+bad,val(dash,'B40'),'Chưa đủ dữ liệu');}set(dash,'B38',serial(2026,10,20));
// Mixed entry modes resolve per block while preserving detailed-mode original inputs.
for(const a of [...q1.answers,q1.date,q1.minutes,q1.type,q1.finish,q1.error])set(quick,a,null);
for(let j=0;j<7;j++){set(diag,'F'+(14+j),verified['N4-G2'][j]);set(diag,'G'+(14+j),'Đúng');}
diag.getRange('H79:J79').values=[[serial(2026,10,20),6,'Mới']];
check('Quick G1 and detailed G2 combine without duplicate',val(scores,'F73'),12);
diag.getRange('F14:H20').clear({applyTo:'contents'});diag.getRange('H79:J79').clear({applyTo:'contents'});
// Verify every official answer individually, plus one wrong and all omissions per block.
for(const b of manifest.blocks){
 fill(b,verified[b.code]);metadata(b);check(b.code+' all verified keys correct',val(quick,`T${b.quick.summary}`),b.questions.length);check(b.code+' submitted',val(quick,b.quick.status),'Đã chấm');
 const first=b.quick.answers[0];set(quick,first,verified[b.code][0]===1?2:1);check(b.code+' one incorrect',val(quick,`T${b.quick.summary}`),b.questions.length-1);
 fill(b,b.questions.map(()=>0));check(b.code+' all skips valid',val(quick,b.quick.status),'Đã chấm');check(b.code+' all skips zero',val(quick,`T${b.quick.summary}`),0);
}
const l=manifest.blocks.find(b=>b.code==='N4-L2');set(quick,l.quick.answers[0],4);check('Three-choice audio rejects 4',val(quick,l.quick.status),'Sửa đáp án');
for(const b of manifest.blocks)for(const a of [...b.quick.answers,b.quick.date,b.quick.minutes,b.quick.type,b.quick.finish,b.quick.error])set(quick,a,null);
set(dash,'B4',45945); // original reporting-week selector restored below from source.
const baseline=JSON.parse(await fs.readFile(path.join(tmp,'input_workbook.json'),'utf8'));set(dash,'B4',Number(baseline['Tổng hợp tuần'].cells.B4.v));set(dash,'B38',null);
check('Fixtures cleared',val(quick,q0.status),'Chưa làm');check('No fabricated final grammar score',val(scores,'F73'),'');
wb.recalculate();
const scan=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},maxChars:3000});
await fs.writeFile(path.join(tmp,'formula_scan.ndjson'),scan.ndjson);
for(const [sheet,range,name] of [['Làm nhanh','A1:G23','quick_blank'],['Tổng hợp tuần','A31:G44','dynamic_dates']]){const b=await wb.render({sheetName:sheet,range,scale:1.5,format:'png'});await fs.writeFile(path.join(tmp,name+'.png'),new Uint8Array(await b.arrayBuffer()));}
fill(manifest.blocks[0],[3,4,2,1,4,2]);metadata(manifest.blocks[0]);set(quick,q0.error,'G');
const preview=await wb.render({sheetName:'Làm nhanh',range:'A10:G23',scale:1.5,format:'png'});await fs.writeFile(path.join(tmp,'quick_complete_fixture.png'),new Uint8Array(await preview.arrayBuffer()));
for(const a of [...q0.answers,q0.date,q0.minutes,q0.type,q0.finish,q0.error])set(quick,a,null);wb.recalculate();
await fs.mkdir(out,{recursive:true});await(await SpreadsheetFile.exportXlsx(wb)).save(path.join(out,'JLPT_PROGRESS_TRACKER_FINAL.xlsx'));
await fs.copyFile(path.join(out,'JLPT_PROGRESS_TRACKER_FINAL.xlsx'),path.join(tmp,'authoring_export.xlsx'));
await fs.writeFile(path.join(tmp,'tracker_tests.json'),JSON.stringify(checks,null,2));await fs.writeFile(path.join(tmp,'manifest_final.json'),JSON.stringify(manifest,null,2));await fs.writeFile(path.join(tmp,'new_links.json'),JSON.stringify(links,null,2));await fs.writeFile(path.join(tmp,'verified_keys.json'),JSON.stringify(verified,null,2));
console.log(JSON.stringify({tests:checks.length,passed:checks.every(x=>x.ok),blocks:manifest.blocks.length}));
