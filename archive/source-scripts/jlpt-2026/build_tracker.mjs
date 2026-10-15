import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook, SpreadsheetFile} from '@oai/artifact-tool';

const here=path.dirname(fileURLToPath(import.meta.url));
const out=path.resolve(here,'../../outputs/jlpt-2026');
await fs.mkdir(out,{recursive:true});
const wb=Workbook.create();
const daily=wb.worksheets.add('Nhật ký');
const scores=wb.worksheets.add('Đo năng lực');
const navy='#314C62', amber='#FFF7DE', pale='#F1F5F8';
const serial=(y,m,d)=>(Date.UTC(y,m-1,d)-Date.UTC(1899,11,30))/86400000;

function base(sh,last,cols){
  sh.showGridLines=false;
  sh.getRange(`A1:${cols}${last}`).format.font={name:'Arial',size:10,color:'#20282E'};
  sh.getRange(`A1:${cols}${last}`).format.verticalAlignment='center';
  sh.getRange(`A8:${cols}${last}`).format.rowHeight=25;
  sh.getRange(`A7:${cols}7`).format={fill:navy,font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},wrapText:true,horizontalAlignment:'center',verticalAlignment:'center',rowHeight:34};
  sh.getRange(`A7:${cols}7`).format.borders={preset:'inside',style:'thin',color:'#FFFFFF'};
  sh.getRange(`A2:${cols}2`).format.font={name:'Arial',size:14,bold:true,color:'#000000'};
  sh.getRange(`A3:${cols}3`).format.borders={bottom:{style:'thin',color:'#D9D9D9'}};
  sh.getRange(`A5:${cols}6`).format.font={name:'Arial',size:10,italic:true,color:'#5D6972'};
  sh.getRange(`A5:${cols}6`).format.rowHeight=22;
  sh.freezePanes.freezeRows(7);
  sh.freezePanes.freezeColumns(1);
  sh.tabColor=navy;
}

base(daily,59,'H');
daily.getRange('A2').values=[['Nhật ký tiếng Nhật từ 15 tháng 10 đến 5 tháng 12 năm 2026']];
daily.getRange('A4:H4').values=[['Ngày có ghi',null,'Phút học',null,'Phút nghe',null,'Phút nói',null]];
daily.getRange('B4').formulas=[['=COUNT(E8:E59)']];
daily.getRange('D4').formulas=[['=IF(COUNT(E8:E59)=0,"",SUM(E8:E59))']];
daily.getRange('F4').formulas=[['=IF(COUNT(F8:F59)=0,"",SUM(F8:F59))']];
daily.getRange('H4').formulas=[['=IF(COUNT(G8:G59)=0,"",SUM(G8:G59))']];
daily.getRange('A4:H4').format.rowHeight=28;
for(const address of ['B4','D4','F4','H4']){
  daily.getRange(address).format.horizontalAlignment='center';
  daily.getRange(address).format.font={name:'Arial',size:11,bold:true,color:navy};
}
daily.getRange('A5').values=[['Ô vàng để nhập. Để trống khi chưa ghi; nhập 0 khi thực sự không học. Ngủ là tổng trong 24 giờ.']];
daily.getRange('A6').values=[['Nghe và nói nằm trong tổng phút học, không cộng trùng. Đỏ nhạt nếu nghe + nói vượt tổng đã nhập.']];
daily.getRange('A7:H7').values=[['Ngày','Ngủ 24h\n(giờ)','Mệt\n1 đến 5','Chế độ','Học\n(phút)','Nghe\n(phút)','Nói\n(phút)','Một lỗi hoặc việc tiếp theo']];
const drows=[];
for(let i=0;i<52;i++) drows.push([serial(2026,10,15)+i,null,null,null,null,null,null,null]);
daily.getRange('A8:H59').values=drows;
daily.getRange('A8:A59').setNumberFormat('dd/mm/yyyy');
daily.getRange('B8:B59').setNumberFormat('0.0');
daily.getRange('C8:C59').setNumberFormat('0');
daily.getRange('E8:G59').setNumberFormat('0');
daily.getRange('B8:H59').format.fill=amber;
daily.getRange('H8:H59').format.wrapText=true;
daily.getRange('D8:D59').dataValidation={rule:{type:'list',values:['Nghỉ','Kiệt sức','Bình thường','Đủ sức']}};
daily.dataValidations.add({range:'C8:C59',rule:{type:'whole',operator:'between',formula1:1,formula2:5}});
daily.dataValidations.add({range:'E8:G59',rule:{type:'whole',operator:'between',formula1:0,formula2:1440}});
daily.getRange('E8:G59').conditionalFormats.addCustom('AND(ISNUMBER($E8),SUM($F8:$G8)>$E8)',{fill:'#FCE8E6',font:{color:'#9C2F2F'}});
const dw=[14,12,9,16,12,11,11,32];
dw.forEach((v,i)=>daily.getRangeByIndexes(0,i,59,1).format.columnWidth=v);
daily.getRange('A8:G59').format.horizontalAlignment='right';
daily.getRange('D8:D59').format.horizontalAlignment='left';

base(scores,71,'J');
scores.getRange('A2').values=[['Đo năng lực bằng câu mới và ôn lại lỗi']];
scores.getRange('A4').values=[['Tỷ lệ đúng thô không đổi thành điểm JLPT. Chỉ dùng các hàng Mới để quyết định tăng độ khó.']];
scores.getRange('A5').values=[['Ngày là mốc dự kiến, sửa theo ngày làm thật. Ô vàng để nhập; ô xanh nhạt là công thức.']];
scores.getRange('A6').values=[['Nguồn đề: https://www.jlpt.jp/e/samples/sampleindex.html . Màu 60% và 80% là mốc thực hành.']];
scores.getRange('A7:J7').values=[['Ngày đo','Cấp','Kỹ năng','Mã cuốn / phần / câu','Loại câu','Số đúng','Tổng câu','Phút làm','Tỷ lệ đúng','Lỗi chính hoặc quyết định']];
const checkpoints=[[2026,10,15],[2026,10,22],[2026,10,29],[2026,11,5],[2026,11,12],[2026,11,19],[2026,11,26],[2026,12,3]];
const srows=[];
for(const dt of checkpoints) for(const level of ['N4','N3']) for(const skill of ['Từ và kanji','Ngữ pháp','Đọc','Nghe']) srows.push([serial(...dt),level,skill,null,null,null,null,null,null,null]);
scores.getRange('A8:J71').values=srows;
scores.getRange('A8:A71').setNumberFormat('dd/mm/yyyy');
scores.getRange('F8:H71').setNumberFormat('0');
scores.getRange('I8:I71').setNumberFormat('0%');
scores.getRange('A8:H71').format.fill=amber;
scores.getRange('J8:J71').format.fill=amber;
scores.getRange('I8:I71').format.fill=pale;
scores.getRange('B8:B71').dataValidation={rule:{type:'list',values:['N4','N3','N2']}};
scores.getRange('C8:C71').dataValidation={rule:{type:'list',values:['Từ và kanji','Ngữ pháp','Đọc','Nghe']}};
scores.getRange('E8:E71').dataValidation={rule:{type:'list',values:['Mới','Ôn lại']}};
scores.dataValidations.add({range:'F8:H71',rule:{type:'whole',operator:'between',formula1:0,formula2:1000}});
scores.getRange('I8').formulas=[['=IF(OR(ISBLANK(F8),ISBLANK(G8)),"",IF(OR(NOT(ISNUMBER(F8)),NOT(ISNUMBER(G8))),"Lỗi nhập",IF(OR(G8<=0,F8<0,F8>G8),"Lỗi nhập",F8/G8)))']];
scores.getRange('I8:I71').fillDown();
scores.getRange('I8:I71').conditionalFormats.addCustom('AND(ISNUMBER(I8),I8<0.6)',{fill:'#FCE8E6',font:{color:'#9C2F2F'}});
scores.getRange('I8:I71').conditionalFormats.addCustom('AND(ISNUMBER(I8),I8>=0.6,I8<0.8)',{fill:'#FFF0C2'});
scores.getRange('I8:I71').conditionalFormats.addCustom('AND(ISNUMBER(I8),I8>=0.8)',{fill:'#E5EFF7'});
scores.getRange('I8:I71').conditionalFormats.add('containsText',{text:'Lỗi nhập',format:{fill:'#FCE8E6',font:{bold:true,color:'#9C2F2F'}}});
const sw=[14,8,15,24,12,9,10,10,12,30];
sw.forEach((v,i)=>scores.getRangeByIndexes(0,i,71,1).format.columnWidth=v);
scores.getRange('D8:D71').format.wrapText=true;
scores.getRange('J8:J71').format.wrapText=true;
scores.getRange('F8:I71').format.horizontalAlignment='right';

// Verify editable inputs, blank versus zero, copied formulas, and invalid numerator.
const checks=[];
function val(sh,r){return sh.getRange(r).values[0][0];}
const blank=val(scores,'I8');
checks.push({case:'Chưa đo giữ trống',actual:blank,ok:blank===''||blank===null});
for(const row of [8,39,71]){
  scores.getRange(`F${row}:G${row}`).values=[[8,10]];
  wb.recalculate();
  const v=val(scores,`I${row}`);
  checks.push({case:`8/10 ở dòng ${row}`,actual:v,ok:Math.abs(v-.8)<1e-9});
  scores.getRange(`F${row}:G${row}`).values=[[null,null]];
}
scores.getRange('F8:G8').values=[[0,10]];
wb.recalculate();
checks.push({case:'0 đúng là 0 phần trăm',actual:val(scores,'I8'),ok:val(scores,'I8')===0});
scores.getRange('F8:G8').values=[[11,10]];
wb.recalculate();
checks.push({case:'Số đúng vượt tổng hiện lỗi',actual:val(scores,'I8'),ok:val(scores,'I8')==='Lỗi nhập'});
scores.getRange('F8:G8').values=[[0,0]];
wb.recalculate();
checks.push({case:'Tổng câu bằng 0 hiện lỗi',actual:val(scores,'I8'),ok:val(scores,'I8')==='Lỗi nhập'});
scores.getRange('F8:G8').values=[[-1,10]];
wb.recalculate();
checks.push({case:'Số đúng âm hiện lỗi',actual:val(scores,'I8'),ok:val(scores,'I8')==='Lỗi nhập'});
scores.getRange('F8:G8').values=[['abc',10]];
wb.recalculate();
checks.push({case:'Chữ trong ô số hiện lỗi',actual:val(scores,'I8'),ok:val(scores,'I8')==='Lỗi nhập'});
scores.getRange('F8:G8').values=[[null,null]];
daily.getRange('E8:G8').values=[[25,10,3]];
wb.recalculate();
checks.push({case:'Tổng phút từ nhật ký',actual:[val(daily,'B4'),val(daily,'D4'),val(daily,'F4'),val(daily,'H4')],ok:val(daily,'B4')===1&&val(daily,'D4')===25&&val(daily,'F4')===10&&val(daily,'H4')===3});
daily.getRange('E8:G8').values=[[0,0,0]];
wb.recalculate();
checks.push({case:'Ngày nghỉ nhập 0 vẫn là một ngày ghi',actual:[val(daily,'B4'),val(daily,'D4')],ok:val(daily,'B4')===1&&val(daily,'D4')===0});
daily.getRange('E8:G8').values=[[null,null,null]];
wb.recalculate();
checks.push({case:'Khôi phục bảng trống',actual:[val(daily,'B4'),val(daily,'D4')],ok:val(daily,'B4')===0&&(val(daily,'D4')===''||val(daily,'D4')===null)});
if(checks.some(x=>!x.ok))throw new Error(JSON.stringify(checks));
console.log(JSON.stringify(checks));
console.log((await wb.inspect({kind:'table',range:"'Đo năng lực'!A7:J10",include:'values,formulas',tableMaxRows:4,tableMaxCols:10,maxChars:1600})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:40},summary:'Kiểm tra lỗi công thức cuối'})).ndjson);
for(const [sh,range,file] of [[daily,'A1:H17','nhat_ky.png'],[scores,'A1:J19','do_nang_luc.png']]){
  const img=await wb.render({sheetName:sh.name,range,scale:1.5,format:'png'});
  await fs.writeFile(path.join(here,file),new Uint8Array(await img.arrayBuffer()));
}
await fs.writeFile(path.join(here,'tracker_validation.json'),JSON.stringify(checks,null,2));
await (await SpreadsheetFile.exportXlsx(wb)).save(path.join(out,'Theo_doi_tien_bo_JLPT.xlsx'));
console.log('EXPORTED '+path.join(out,'Theo_doi_tien_bo_JLPT.xlsx'));
