import fs from 'node:fs/promises';
import {SpreadsheetFile,FileBlob} from '@oai/artifact-tool';
const root='<user>/Music/JP',tmp=root+'/tmp/jlpt-v3';
const w=await SpreadsheetFile.importXlsx(await FileBlob.load(root+'/FINAL_V3/JLPT_PROGRESS_TRACKER_FINAL.xlsx'));w.recalculate();
const q=w.worksheets.getItem('Làm nhanh'),d=w.worksheets.getItem('Tổng hợp tuần');
if(q.getRange('B18').values[0][0]!=='Chưa làm'||d.getRange('D38').values[0][0]!=='Chưa đủ dữ liệu')throw Error('Unexpected final input state');
const scan=await w.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},maxChars:2000});
await fs.writeFile(tmp+'/reopen_scan.ndjson',scan.ndjson);
for(const [s,r,n] of [['Nhật ký','A1:J12','preserved_daily'],['Đo năng lực','A69:L79','resolved_scores'],['Chẩn đoán','A1:I14','preserved_detail'],['Tổng hợp tuần','A1:G31','weekly_final']]){const b=await w.render({sheetName:s,range:r,scale:1.2,format:'png'});await fs.writeFile(tmp+'/'+n+'.png',new Uint8Array(await b.arrayBuffer()));}
console.log(scan.ndjson);console.log('Reopened native-patched output, recalculated and rendered all five sheets');
