import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';

const dir=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(dir,'../..'), final=path.join(root,'FINAL');
const manifest=JSON.parse(await fs.readFile(path.join(dir,'manifest.json'),'utf8'));
const baseline=JSON.parse(await fs.readFile(path.join(dir,'baseline_workbook.json'),'utf8'));
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(path.join(root,'outputs/jlpt-2026/Theo_doi_tien_bo_JLPT.xlsx')));
const daily=wb.worksheets.getItem('Nhật ký'), scores=wb.worksheets.getItem('Đo năng lực');
const dash=wb.worksheets.add('Tổng hợp tuần'), diag=wb.worksheets.add('Chẩn đoán');
const navy='#314C62', amber='#FFF7DE', pale='#F1F5F8', red='#FCE8E6';
const serial=(y,m,d)=>(Date.UTC(y,m-1,d)-Date.UTC(1899,11,30))/86400000;
const set=(sh,a,v)=>sh.getRange(a).values=[[v]];
const fx=(sh,a,f)=>sh.getRange(a).formulas=[[f]];
const val=(sh,a)=>sh.getRange(a).values[0][0];
const errors=['V','G','R','A','M','T','F'];
function head(sh,a){sh.getRange(a).format={fill:navy,font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},horizontalAlignment:'center',verticalAlignment:'center',wrapText:true,rowHeight:34};sh.getRange(a).format.borders={preset:'inside',style:'thin',color:'#FFFFFF'};}
function newSheet(sh,range){sh.showGridLines=false;sh.getRange(range).format={font:{name:'Arial',size:10,color:'#20282E'},verticalAlignment:'center',rowHeight:25};sh.getRange('A2').format.font={name:'Arial',size:14,bold:true,color:'#000000'};sh.tabColor=navy;}
function input(sh,a){sh.getRange(a).format.fill=amber;}
function calc(sh,a){sh.getRange(a).format.fill=pale;}
function hint(sh,a,text){set(sh,a,text);sh.getRange(a).format.font={name:'Arial',size:10,italic:true,color:'#5D6972'};}
function positiveWarn(sh,a,condition){sh.getRange(a).conditionalFormats.addCustom(condition,{fill:red,font:{color:'#9C2F2F'}});}
const links=[];
function link(sh,address,url,label){set(sh,address,label);sh.getRange(address).format.font={name:'Arial',size:10,color:'#234E72'};links.push({sheet:sh.name,address,url,label});}

// Extend the original two sheets without changing their data or existing formulas.
set(daily,'A5','Ô vàng để nhập. Chưa biết để trống; nghỉ thật nhập 0 phút. Ngủ là tổng 24 giờ, gồm ngủ bù.');
set(daily,'A6','Nhập chế độ và tổng phút; thêm nghe/nói nếu biết. Mã lỗi ở I. Cột J trở đi tự kiểm tra.');
daily.getRange('I7:O7').values=[['Mã lỗi chính','Kiểm tra dòng','Có giờ ngủ','Có mức mệt','Có phút nghe','Có phút nói','Đã ghi phút học']];
head(daily,'I7:O7');
daily.getRange('I8:O59').format={font:{name:'Arial',size:10,color:'#20282E'},rowHeight:25,verticalAlignment:'center'};
input(daily,'I8:I59');calc(daily,'J8:O59');
daily.getRange('I1:I59').format.columnWidth=13;
daily.getRange('J1:J59').format.columnWidth=24;
daily.getRange('K1:O59').format.columnWidth=13;
daily.getRange('I8:I59').dataValidation={rule:{type:'list',values:errors}};
daily.dataValidations.add({range:'B8:B59',rule:{type:'decimal',operator:'between',formula1:0,formula2:24}});
for(let r=8;r<=59;r++){
  const noInput=`AND(COUNTA(B${r}:I${r})=0)`;
  const badSleep=`AND(NOT(ISBLANK(B${r})),OR(NOT(ISNUMBER(B${r})),B${r}<0,B${r}>24))`;
  const badFatigue=`AND(NOT(ISBLANK(C${r})),IF(ISNUMBER(C${r}),OR(C${r}<1,C${r}>5,MOD(C${r},1)<>0),TRUE))`;
  const badPart=`OR(AND(NOT(ISBLANK(F${r})),OR(NOT(ISNUMBER(F${r})),F${r}<0)),AND(NOT(ISBLANK(G${r})),OR(NOT(ISNUMBER(G${r})),G${r}<0)))`;
  fx(daily,`J${r}`,`=IF(${noInput},"",IF(OR(${badSleep},${badFatigue}),"Lỗi ngủ/mệt",IF(NOT(ISNUMBER(E${r})),"Thiếu tổng phút",IF(OR(E${r}<0,${badPart}),"Lỗi phút",IF(SUM(F${r}:G${r})>E${r},"Nghe+nói vượt tổng",IF(AND(D${r}<>"Nghỉ",D${r}<>"Kiệt sức",D${r}<>"Bình thường",D${r}<>"Đủ sức"),"Thiếu chế độ",IF(AND(LEN(I${r})>0,COUNTIF($I$63:$I$69,I${r})=0),"Lỗi mã","Hợp lệ")))))))`);
  fx(daily,`K${r}`,`=IF(AND(ISNUMBER(B${r}),B${r}>=0,B${r}<=24),1,0)`);
  fx(daily,`L${r}`,`=IF(ISNUMBER(C${r}),IF(AND(C${r}>=1,C${r}<=5,MOD(C${r},1)=0),1,0),0)`);
  fx(daily,`M${r}`,`=IF(AND(J${r}="Hợp lệ",ISNUMBER(F${r})),1,0)`);
  fx(daily,`N${r}`,`=IF(AND(J${r}="Hợp lệ",ISNUMBER(G${r})),1,0)`);
  fx(daily,`O${r}`,`=IF(J${r}="Hợp lệ",1,0)`);
}
daily.getRange('I63:J69').values=errors.map((e,i)=>[e,['Từ và kanji','Ngữ pháp','Nối ý đọc','Nhận diện âm','Giữ thông tin','Thời gian','Mệt/gián đoạn'][i]]);
daily.getRange('I62:J62').values=[['Mã','Ý nghĩa']];head(daily,'I62:J62');
positiveWarn(daily,'J8:J59','AND(J8<>"",J8<>"Hợp lệ")');

// A question list with identifiers only; no exam text, answer keys or audio is redistributed.
newSheet(diag,'A1:K90');
set(diag,'A2','Phiếu đáp án chẩn đoán N4 và N3');
hint(diag,'A4','Bắt đầu N4-G1: điền F8:F13. Không tra cứu khi đo. Hết giờ chưa trả lời nhập 0; chưa làm để trống.');
hint(diag,'A5','Sau lượt đo mở khóa trong hướng dẫn PDF; chọn G Đúng/Sai/Bỏ trống, H mã lỗi nếu biết.');
hint(diag,'A6','Cuối khối bấm Ghi ngày/phút rồi nhập H ngày thật, I phút làm, J Mới/Ôn lại. Ô xanh tự tính.');
diag.getRange('A7:K7').values=[['Khối','Cấp','Kỹ năng','Câu','Nguồn','Bạn chọn','Tự chấm','Mã lỗi','Kết thúc khối','Kiểm tra câu','Số lựa chọn']];head(diag,'A7:K7');
const qrows=[];
for(const b of manifest.blocks) for(const q of b.questions){
  const group=typeof q==='string'?Number(q[1]):null;
  const max=b.part==='L'&&((b.level==='N4'&&group>=3)||(b.level==='N3'&&group>=4))?3:4;
  qrows.push([b.code,b.level,b.skill,String(q),null,null,null,null,null,null,max]);
}
diag.getRange('A8:K73').values=qrows;
input(diag,'F8:H73');calc(diag,'J8:K73');
diag.getRange('G8:G73').dataValidation={rule:{type:'list',values:['Đúng','Sai','Bỏ trống']}};
diag.getRange('H8:H73').dataValidation={rule:{type:'list',values:errors}};
for(const [range,max] of [['F8:F39',4],['F40:F43',3],['F44:F69',4],['F70:F73',3]])diag.dataValidations.add({range,rule:{type:'whole',operator:'between',formula1:0,formula2:max}});
for(const b of manifest.blocks){
  for(let r=b.start_row;r<=b.end_row;r++){
    link(diag,`E${r}`,b.url,'Mở đề');
    fx(diag,`J${r}`,`=IF(AND(ISBLANK(F${r}),ISBLANK(G${r}),ISBLANK(H${r})),"",IF(NOT(ISNUMBER(F${r})),"Lỗi đáp án",IF(OR(F${r}<0,F${r}>K${r},MOD(F${r},1)<>0),"Lỗi đáp án",IF(AND(LEN(H${r})>0,COUNTIF('Nhật ký'!$I$63:$I$69,H${r})=0),"Lỗi mã",IF(AND(F${r}=0,G${r}="Bỏ trống"),"Đã chấm",IF(AND(F${r}>0,OR(G${r}="Đúng",G${r}="Sai")),"Đã chấm",IF(ISBLANK(G${r}),"Chưa chấm","Kiểm tra bỏ trống")))))))`);
  }
  link(diag,`I${b.end_row}`,`#'Chẩn đoán'!H${b.summary_row}`,'Ghi ngày/phút');
}
set(diag,'A75','Bảng chấm từng khối');diag.getRange('A75').format.font={name:'Arial',size:12,bold:true};
hint(diag,'A76','H/I/J là ô nhập sau khi chấm. Mới chỉ khi chưa xem câu, chưa xem khóa/bản chép, không được gợi ý.');
diag.getRange('A77:K77').values=[['Khối','Cấp','Kỹ năng','Tổng câu','Đã chấm','Đúng','Độ đúng','Ngày thật','Phút làm','Loại câu','Trạng thái']];head(diag,'A77:K77');
for(const b of manifest.blocks){
  const r=b.summary_row,s=b.start_row,e=b.end_row;
  diag.getRange(`A${r}:D${r}`).values=[[b.code,b.level,b.skill,b.questions.length]];
  fx(diag,`E${r}`,`=COUNTIF(J${s}:J${e},"Đã chấm")`);
  fx(diag,`F${r}`,`=IF(E${r}=D${r},COUNTIFS(G${s}:G${e},"Đúng",J${s}:J${e},"Đã chấm"),"")`);
  fx(diag,`K${r}`,`=IF(E${r}<D${r},"Còn "&(D${r}-E${r})&" câu chưa chấm",IF(OR(NOT(ISNUMBER(H${r})),H${r}<1),"Thiếu ngày",IF(OR(NOT(ISNUMBER(I${r})),I${r}<=0),"Thiếu phút",IF(AND(J${r}<>"Mới",J${r}<>"Ôn lại"),"Chọn loại câu","Đã chấm"))))`);
  fx(diag,`G${r}`,`=IF(K${r}="Đã chấm",F${r}/D${r},"")`);
}
input(diag,'H78:J88');calc(diag,'D78:G88');calc(diag,'K78:K88');
diag.getRange('H78:H88').setNumberFormat('dd/mm/yyyy');
diag.getRange('G78:G88').setNumberFormat('0%');
diag.getRange('J78:J88').dataValidation={rule:{type:'list',values:['Mới','Ôn lại']}};
diag.dataValidations.add({range:'H78:H88',rule:{type:'whole',operator:'between',formula1:1,formula2:2958465}});
diag.dataValidations.add({range:'I78:I88',rule:{type:'decimal',operator:'between',formula1:0.01,formula2:180}});
positiveWarn(diag,'J8:J73','AND(J8<>"",J8<>"Đã chấm",J8<>"Chưa chấm")');
const qw=[12,8,15,11,13,12,15,13,17,24,19];qw.forEach((v,i)=>diag.getRangeByIndexes(0,i,90,1).format.columnWidth=v);
diag.freezePanes.freezeRows(7);diag.freezePanes.freezeColumns(1);

// Append diagnostic summaries. The 64 historical/manual rows remain where they were.
set(scores,'A5','Ô vàng tự nhập; sửa ngày dự kiến theo ngày thật. START18 cuối bảng tự tổng hợp, không nhập lặp.');
set(scores,'A6','Chỉ hàng Mới, hợp lệ đi vào tổng hợp tuần. K là mã lỗi; L nêu dữ liệu cần sửa. Không đổi sang điểm JLPT.');
scores.getRange('K7:L7').values=[['Mã lỗi chính','Kiểm tra dòng']];head(scores,'K7:L7');
scores.getRange('K1:K79').format.columnWidth=13;scores.getRange('L1:L79').format.columnWidth=27;
scores.getRange('K8:L79').format={font:{name:'Arial',size:10,color:'#20282E'},rowHeight:25,verticalAlignment:'center'};input(scores,'K8:K79');calc(scores,'L8:L79');
scores.getRange('K8:K79').dataValidation={rule:{type:'list',values:errors}};
const summaries=[
 ['N4','Từ và kanji',[80]],['N4','Ngữ pháp',[78,79]],['N4','Đọc',[81]],['N4','Nghe',[82,83]],
 ['N3','Từ và kanji',[85]],['N3','Ngữ pháp',[84]],['N3','Đọc',[86]],['N3','Nghe',[87,88]]
];
scores.getRange('A72:J79').copyFrom(scores.getRange('A8:J15'),'all');
scores.getRange('A72:J79').clear({applyTo:'contents'});calc(scores,'A72:J79');
for(let i=0;i<summaries.length;i++){
  const [level,skill,rs]=summaries[i],r=72+i;
  const ready=`AND(${rs.map(s=>`'Chẩn đoán'!K${s}="Đã chấm"`).join(',')})`;
  const sum=(col)=>rs.map(s=>`'Chẩn đoán'!${col}${s}`).join(',');
  const isnew=`AND(${rs.map(s=>`'Chẩn đoán'!J${s}="Mới"`).join(',')})`;
  set(scores,`B${r}`,level);set(scores,`C${r}`,skill);set(scores,`D${r}`,`START18-${level}-${skill==='Từ và kanji'?'V':skill==='Ngữ pháp'?'G':skill==='Đọc'?'R':'L'}`);
  fx(scores,`A${r}`,`=IF(${ready},MAX(${sum('H')}),"")`);
  fx(scores,`E${r}`,`=IF(${ready},IF(${isnew},"Mới","Ôn lại"),"")`);
  for(const [col,source] of [['F','F'],['G','D'],['H','I']])fx(scores,`${col}${r}`,`=IF(${ready},SUM(${sum(source)}),"")`);
  fx(scores,`I${r}`,`=IF(COUNT(F${r}:G${r})<2,"",IF(OR(G${r}<=0,F${r}<0,F${r}>G${r}),"Lỗi nhập",F${r}/G${r}))`);
}
scores.getRange('A72:A79').setNumberFormat('dd/mm/yyyy');scores.getRange('I72:I79').setNumberFormat('0%');scores.getRange('F72:H79').setNumberFormat('0');
for(let r=8;r<=79;r++){
  const active=`OR(COUNT(F${r}:H${r})>0,LEN(F${r}&G${r}&H${r})>0)`;
  const duplicate=`COUNTIFS($B$8:$B$79,B${r},$C$8:$C$79,C${r},$D$8:$D$79,D${r},$E$8:$E$79,"Mới",$G$8:$G$79,">0")>1`;
  const badCategory=`OR(AND(B${r}<>"N4",B${r}<>"N3",B${r}<>"N2"),AND(C${r}<>"Từ và kanji",C${r}<>"Ngữ pháp",C${r}<>"Đọc",C${r}<>"Nghe"))`;
  fx(scores,`L${r}`,`=IF(NOT(${active}),"",IF(NOT(ISNUMBER(I${r})),"Lỗi/thiếu số đúng-tổng",IF(OR(MOD(F${r},1)<>0,MOD(G${r},1)<>0),"Lỗi/thiếu số đúng-tổng",IF(${badCategory},"Sai cấp/kỹ năng",IF(OR(NOT(ISNUMBER(A${r})),A${r}<1),"Thiếu ngày đo",IF(D${r}="","Thiếu mã bài",IF(AND(E${r}<>"Mới",E${r}<>"Ôn lại"),"Thiếu loại câu",IF(OR(NOT(ISNUMBER(H${r})),H${r}<=0),"Thiếu phút",IF(AND(E${r}="Mới",${duplicate}),"Trùng câu mới","Hợp lệ")))))))))`);
}
positiveWarn(scores,'L8:L79','AND(L8<>"",L8<>"Hợp lệ")');

// Weekly dashboard with separate denominators by level and skill; no pass-probability model.
newSheet(dash,'A1:G36');set(dash,'A2','Tổng hợp học tiếng Nhật trong tuần');
set(dash,'A4','Tuần từ');set(dash,'B4',serial(2026,10,15));set(dash,'C4','đến');fx(dash,'D4','=B4+6');
dash.getRange('B4').setNumberFormat('dd/mm/yyyy');dash.getRange('D4').setNumberFormat('dd/mm/yyyy');input(dash,'B4');
hint(dash,'E4','Đổi ngày ở B4 khi cần.');
dash.dataValidations.add({range:'B4',rule:{type:'whole',operator:'between',formula1:1,formula2:2958465}});
dash.getRange('A6:C6').values=[['Chỉ số','Kết quả','Cỡ mẫu']];head(dash,'A6:C6');
dash.getRange('E6:G6').values=[['Mã lỗi','Bản ghi','Ý nghĩa']];head(dash,'E6:G6');
const dateCrit=(tab,col='A')=>`'${tab}'!$${col}$8:$${col}$${tab==='Nhật ký'?59:79},">="&$B$4,'${tab}'!$${col}$8:$${col}$${tab==='Nhật ký'?59:79},"<"&($B$4+7)`;
const dcrit=dateCrit('Nhật ký');
const dailyMetrics=[['Phút học','E','O'],['Phút nghe','F','M'],['Phút nói','G','N'],['Ngủ TB (giờ/24h)','B','K'],['Mệt TB (1–5)','C','L']];
for(let i=0;i<dailyMetrics.length;i++){
  const [label,col,flag]=dailyMetrics[i],r=7+i;
  set(dash,`A${r}`,label);
  fx(dash,`C${r}`,`=SUMIFS('Nhật ký'!$${flag}$8:$${flag}$59,${dcrit})`);
  fx(dash,`B${r}`,`=IF(C${r}=0,"",SUMIFS('Nhật ký'!$${col}$8:$${col}$59,${dcrit},'Nhật ký'!$${flag}$8:$${flag}$59,1)${i>=3?`/C${r}`:''})`);
}
dash.getRange('B10:B11').setNumberFormat('0.0');
set(dash,'A12','Nhật ký cần sửa');fx(dash,'B12',`=SUM(${['Lỗi ngủ/mệt','Thiếu tổng phút','Lỗi phút','Nghe+nói vượt tổng','Thiếu chế độ','Lỗi mã'].map(s=>`COUNTIFS(${dcrit},'Nhật ký'!$J$8:$J$59,"${s}")`).join(',')})`);
set(dash,'A13','Bản đo cần sửa');fx(dash,'B13',`=SUM(${['Lỗi/thiếu số đúng-tổng','Sai cấp/kỹ năng','Thiếu ngày đo','Thiếu mã bài','Thiếu loại câu','Thiếu phút','Trùng câu mới'].map(s=>`COUNTIF('Đo năng lực'!$L$8:$L$79,"${s}")`).join(',')})`);set(dash,'C13','toàn sổ');
for(let i=0;i<errors.length;i++){
  set(dash,`E${7+i}`,errors[i]);fx(dash,`F${7+i}`,`=COUNTIFS(${dcrit},'Nhật ký'!$I$8:$I$59,E${7+i})`);set(dash,`G${7+i}`,['Từ/kanji','Ngữ pháp','Nối ý đọc','Nhận diện âm','Giữ thông tin','Thời gian','Mệt/gián đoạn'][i]);
}
hint(dash,'A15','Câu Mới trong tuần, có ngày/phút/mã bài hợp lệ. Mỗi cấp và kỹ năng giữ riêng.');
dash.getRange('A17:G17').values=[['Cấp','Kỹ năng','Đúng','Tổng câu','Độ đúng thô','Phút làm','Cỡ mẫu']];head(dash,'A17:G17');
let rr=18;
for(const level of ['N4','N3','N2'])for(const skill of ['Từ và kanji','Ngữ pháp','Đọc','Nghe']){
  const r=rr++;set(dash,`A${r}`,level);set(dash,`B${r}`,skill);
  const crit=`${dateCrit('Đo năng lực')},'Đo năng lực'!$B$8:$B$79,A${r},'Đo năng lực'!$C$8:$C$79,B${r},'Đo năng lực'!$E$8:$E$79,"Mới",'Đo năng lực'!$L$8:$L$79,"Hợp lệ"`;
  const count=`COUNTIFS(${crit})`;
  for(const [col,source] of [['C','F'],['D','G'],['F','H']])fx(dash,`${col}${r}`,`=IF(${count}=0,"",SUMIFS('Đo năng lực'!$${source}$8:$${source}$79,${crit}))`);
  fx(dash,`E${r}`,`=IF(COUNT(C${r}:D${r})<2,"",IF(D${r}>0,C${r}/D${r},""))`);
  fx(dash,`G${r}`,`=IF(COUNT(D${r})=0,"Chưa đo",IF(D${r}<10,"Mẫu nhỏ","Có "&D${r}&" câu"))`);
}
dash.getRange('E18:E29').setNumberFormat('0%');
dash.getRange('E18:E29').conditionalFormats.addCustom('AND(ISNUMBER(E18),E18<0.6)',{fill:'#FCE8E6'});
dash.getRange('E18:E29').conditionalFormats.addCustom('AND(ISNUMBER(E18),E18>=0.6,E18<0.8)',{fill:'#FFF0C2'});
dash.getRange('E18:E29').conditionalFormats.addCustom('AND(ISNUMBER(E18),E18>=0.8)',{fill:'#E5EFF7'});
set(dash,'A31','Khối N4 đã chấm');fx(dash,'B31','=COUNTIF(\'Chẩn đoán\'!$K$78:$K$83,"Đã chấm")&"/6 khối"');
set(dash,'D31','N3 tùy chọn');fx(dash,'E31','=COUNTIF(\'Chẩn đoán\'!$K$84:$K$88,"Đã chấm")&"/5 khối"');
link(dash,'A33',`#'Chẩn đoán'!F8`,'Mở phiếu đáp án');link(dash,'D33',`#'Nhật ký'!B8`,'Ghi nhật ký ngày');
hint(dash,'A35','Màu 60% và 80% là mốc quan sát, không phải ngưỡng đỗ. Không đổi độ đúng thô sang điểm JLPT.');
hint(dash,'A36','Trống là chưa có dữ liệu. Cỡ mẫu nhỏ cần đo thêm câu chưa thấy; không kết luận cấp độ từ vài câu.');
const widths=[24,20,14,15,18,15,27];widths.forEach((v,i)=>dash.getRangeByIndexes(0,i,36,1).format.columnWidth=v);
dash.getRange('A17:A29').format.columnWidth=24;
dash.getRange('B4').format.horizontalAlignment='center';dash.getRange('D4').format.horizontalAlignment='center';
dash.getRange('B7:C13').format.horizontalAlignment='center';dash.getRange('F7:F13').format.horizontalAlignment='center';
for(const r of [1,3,5,14,16,30,32,34])dash.getRange(`A${r}:G${r}`).format.rowHeight=9;
positiveWarn(dash,'B12:B13','B12>0');

// Validate calculations using a temporary fixture, then restore every user input.
const checks=[];
function check(name,actual,expected){const ok=typeof expected==='number'?typeof actual==='number'&&Math.abs(actual-expected)<1e-9:JSON.stringify(actual)===JSON.stringify(expected);checks.push({name,actual,expected,ok});if(!ok)throw new Error(JSON.stringify(checks.at(-1)));}
function cellSnapshot(sh,addresses){return addresses.map(a=>({a,values:sh.getRange(a).values,formulas:sh.getRange(a).formulas}));}
function restore(sh,snap){for(const s of snap){if(s.formulas.some(row=>row.some(f=>f)))sh.getRange(s.a).formulas=s.formulas;else sh.getRange(s.a).values=s.values;}}
const dsnap=cellSnapshot(daily,['B8:I10']), ssnap=cellSnapshot(scores,['A8:H13']), qsnap=cellSnapshot(diag,['F8:H13','H78:J78']);
check('Initial unknown accuracy',val(dash,'E18'),'');
check('No initial measured outcomes',val(scores,'F73'),'');
check('N4 diagnostic starts with six optional windows',val(dash,'B31'),'0/6 khối');check('N3 remains a separate optional probe',val(dash,'E31'),'0/5 khối');
daily.getRange('B8:I8').values=[[7.5,4,'Bình thường',25,10,3,'Lỗi trợ từ','G']];
wb.recalculate();check('Diary valid',val(daily,'J8'),'Hợp lệ');check('Week study minutes',val(dash,'B7'),25);check('Sleep mean preserves fractions',val(dash,'B10'),7.5);check('Speaking minutes',val(dash,'B9'),3);
check('Weekly error category',val(dash,'F8'),1);
set(daily,'C8','abc');wb.recalculate();check('Text fatigue is actionable without formula error',val(daily,'J8'),'Lỗi ngủ/mệt');set(daily,'C8',4);
set(daily,'I8',0);wb.recalculate();check('Zero is not a blank error code',val(daily,'J8'),'Lỗi mã');set(daily,'I8','G');
daily.getRange('B9:I9').values=[[0,5,'Nghỉ',0,0,0,'Ngày nghỉ','F']];wb.recalculate();check('Real zero sleep counted',val(dash,'C10'),2);check('Sleep mean with real zero',val(dash,'B10'),3.75);check('Zero-minute rest counted',val(dash,'C7'),2);
daily.getRange('B10:I10').values=[[null,null,'Bình thường',20,null,null,null,null]];wb.recalculate();check('Blank listening is not zero observation',val(dash,'C8'),2);check('Study includes row with unknown listening',val(dash,'B7'),45);
set(daily,'F10',30);wb.recalculate();check('Overlapping minutes flagged',val(daily,'J10'),'Nghe+nói vượt tổng');check('Invalid activity excluded',val(dash,'B7'),25);
set(daily,'B8',25);wb.recalculate();check('Impossible sleep flagged',val(daily,'J8'),'Lỗi ngủ/mệt');set(daily,'B8',7.5);
const fixture=[
 [serial(2026,10,15),'N4','Ngữ pháp','TEST-N4-G','Mới',0,10,6],
 [serial(2026,10,15),'N3','Ngữ pháp','TEST-N3-G','Mới',8,10,7],
 [serial(2026,10,15),'N2','Ngữ pháp','TEST-N2-G','Mới',5,10,8],
 [serial(2026,10,15),'N4','Ngữ pháp','TEST-OLD','Ôn lại',10,10,5],
 [serial(2026,10,22),'N4','Ngữ pháp','TEST-NEXT','Mới',10,10,5],
 [serial(2026,10,14),'N4','Ngữ pháp','TEST-PREV','Mới',10,10,5]
];
scores.getRange('A8:H13').values=fixture;wb.recalculate();
check('Zero correct preserved',val(scores,'I8'),0);check('N4 separate',val(dash,'E19'),0);check('N3 separate',val(dash,'E23'),.8);check('N2 separate',val(dash,'E27'),.5);check('Old and outside-week excluded',val(dash,'D19'),10);
set(dash,'B4',serial(2026,10,22));wb.recalculate();check('Week selector changes included records',val(dash,'E19'),1);check('Other levels do not carry to next week',val(dash,'E23'),'');set(dash,'B4',serial(2026,10,15));
set(scores,'A13',serial(2026,10,21));wb.recalculate();check('Last day of week included',val(dash,'D19'),20);set(scores,'A13',serial(2026,10,14));
set(scores,'B8','N5');wb.recalculate();check('Unsupported level flagged',val(scores,'L8'),'Sai cấp/kỹ năng');set(scores,'B8','N4');
set(scores,'F8',1.5);wb.recalculate();check('Fractional correct-answer count rejected',val(scores,'L8'),'Lỗi/thiếu số đúng-tổng');set(scores,'F8',0);
set(scores,'F8','abc');wb.recalculate();check('Text answer count is flagged without arithmetic error',val(scores,'L8'),'Lỗi/thiếu số đúng-tổng');set(scores,'F8',0);
set(scores,'G8',0);wb.recalculate();check('Zero denominator error',val(scores,'I8'),'Lỗi nhập');check('Invalid measure excluded',val(dash,'E19'),'');set(scores,'G8',10);
set(scores,'F8',11);wb.recalculate();check('Correct above denominator error',val(scores,'I8'),'Lỗi nhập');set(scores,'F8',0);
set(scores,'H8',null);wb.recalculate();check('Missing timing remains visible',val(scores,'L8'),'Thiếu phút');set(scores,'H8',6);
set(scores,'A8',null);wb.recalculate();check('Missing date remains actionable',val(scores,'L8'),'Thiếu ngày đo');check('Missing-date warning does not disappear',val(dash,'B13'),1);set(scores,'A8',serial(2026,10,15));
set(scores,'D9','TEST-N4-G');set(scores,'B9','N4');wb.recalculate();check('Duplicate new set flagged',val(scores,'L8'),'Trùng câu mới');check('Duplicate does not inflate dashboard',val(dash,'D19'),'');
restore(scores,ssnap);
diag.getRange('F8:G13').values=[[1,'Đúng'],[2,'Sai'],[0,'Bỏ trống'],[1,'Đúng'],[2,'Đúng'],[1,'Sai']];
diag.getRange('H78:J78').values=[[serial(2026,10,15),6,'Mới']];wb.recalculate();
check('Six selected, omitted counted in denominator',val(diag,'G78'),.5);check('One grammar block cannot complete combined result',val(scores,'F73'),'');
check('Diagnostic task counter reacts to completed N4 block',val(dash,'B31'),'1/6 khối');
set(diag,'G10','Đúng');wb.recalculate();check('Cannot mark omitted answer correct',val(diag,'J10'),'Kiểm tra bỏ trống');check('Contradictory grading blocks completion',val(diag,'G78'),'');set(diag,'G10','Bỏ trống');
set(diag,'F8',5);wb.recalculate();check('Out-of-range answer caught',val(diag,'J8'),'Lỗi đáp án');set(diag,'F8',1);
set(diag,'F8','abc');wb.recalculate();check('Text answer is flagged without arithmetic error',val(diag,'J8'),'Lỗi đáp án');set(diag,'F8',1);
set(diag,'J78',null);wb.recalculate();check('Freshness cannot be assumed',val(diag,'K78'),'Chọn loại câu');set(diag,'J78','Mới');
set(diag,'H78',0);wb.recalculate();check('Date zero does not complete a block',val(diag,'K78'),'Thiếu ngày');set(diag,'H78',serial(2026,10,15));
set(diag,'F40',4);set(diag,'G40','Đúng');wb.recalculate();check('Three-choice listening rejects answer four',val(diag,'J40'),'Lỗi đáp án');diag.getRange('F40:H40').values=[[null,null,null]];
// Render a fixture view to verify visual progress; it is not saved to the final workbook.
scores.getRange('A8:H13').values=fixture;wb.recalculate();
const sample=await wb.render({sheetName:dash.name,range:'A1:G36',scale:1.2,format:'png'});await fs.writeFile(path.join(dir,'dashboard_test_fixture.png'),new Uint8Array(await sample.arrayBuffer()));
restore(daily,dsnap);restore(scores,ssnap);restore(diag,qsnap);

// Test the complete automatic link, including mixed fresh/review blocks, on disposable inputs.
const q2snap=cellSnapshot(diag,['F8:H20','H78:J79']);
for(let r=8;r<=20;r++){set(diag,`F${r}`,1);set(diag,`G${r}`,'Đúng');}
diag.getRange('H78:J79').values=[[serial(2026,10,15),6,'Mới'],[serial(2026,10,16),6,'Ôn lại']];wb.recalculate();
check('Complete grammar automatic score',val(scores,'F73'),13);check('Mixed freshness becomes review',val(scores,'E73'),'Ôn lại');check('Review diagnostic excluded from fresh dashboard',val(dash,'E19'),'');
set(diag,'J79','Mới');wb.recalculate();check('Fresh diagnostic enters dashboard',val(dash,'E19'),1);check('Completion date is last block date',val(scores,'A73'),serial(2026,10,16));
restore(diag,q2snap);
const listeningSnap=cellSnapshot(diag,['F36:H43','H82:J83']);
for(let r=36;r<=43;r++){set(diag,`F${r}`,0);set(diag,`G${r}`,'Bỏ trống');}
diag.getRange('H82:J83').values=[[serial(2026,10,15),10,'Mới'],[serial(2026,10,15),8,'Mới']];wb.recalculate();
check('All omitted listening is measured zero',val(scores,'I75'),0);check('Listening denominator is all selected items',val(scores,'G75'),8);check('Measured zero listening reaches weekly dashboard',val(dash,'E21'),0);
restore(diag,listeningSnap);
wb.recalculate();
check('No diagnostic answers left from tests',val(diag,'F8'),null);check('No fabricated N2 results',val(dash,'E27'),'');check('No fabricated diagnostic results',val(scores,'F73'),'');

// Check preservation of every baseline input and formula except authorized instruction text.
const authorized={'Nhật ký':new Set(['A5','A6']),'Đo năng lực':new Set(['A5','A6'])};
for(const [name,snap] of Object.entries(baseline)){
  const sh=wb.worksheets.getItem(name),values=sh.getRange(snap.range).values,formulas=sh.getRange(snap.range).formulas;
  for(let r=0;r<snap.values.length;r++)for(let c=0;c<snap.values[r].length;c++){
    const addr=String.fromCharCode(65+c)+(r+1);if(authorized[name].has(addr))continue;
    const oldf=snap.formulas[r]?.[c]||'',newf=formulas[r]?.[c]||'';
    if(oldf!==newf)throw new Error(`Changed original formula ${name}!${addr}`);
    if(!oldf&&JSON.stringify(snap.values[r][c]??null)!==JSON.stringify(values[r][c]??null))throw new Error(`Changed original data ${name}!${addr}`);
  }
}
checks.push({name:'Original data and formulas preserved',ok:true});
const errscan=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},summary:'Final formula scan'});
await fs.writeFile(path.join(dir,'formula_scan.ndjson'),errscan.ndjson);
console.log(errscan.ndjson);
for(const [sh,range,file] of [[dash,'A1:G36','dashboard_final.png'],[daily,'A1:J17','daily_final.png'],[scores,'A1:L15','scores_final.png'],[diag,'A1:I20','diagnostic_final.png'],[diag,'A75:K88','diagnostic_summary_final.png']]){
 const img=await wb.render({sheetName:sh.name,range,scale:1.2,format:'png'});await fs.writeFile(path.join(dir,file),new Uint8Array(await img.arrayBuffer()));
}
await fs.writeFile(path.join(dir,'v2_tracker_tests.json'),JSON.stringify(checks,null,2));
await fs.writeFile(path.join(dir,'native_links.json'),JSON.stringify(links,null,2));
await (await SpreadsheetFile.exportXlsx(wb)).save(path.join(final,'JLPT_PROGRESS_TRACKER_v2.xlsx'));
console.log(JSON.stringify({tests:checks.length,passed:checks.every(c=>c.ok),output:path.join(final,'JLPT_PROGRESS_TRACKER_v2.xlsx')}));
