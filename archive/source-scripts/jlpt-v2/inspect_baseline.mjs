import fs from 'node:fs/promises';
import {SpreadsheetFile,FileBlob} from '@oai/artifact-tool';
const root='<user>/Music/JP';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(root+'/outputs/jlpt-2026/Theo_doi_tien_bo_JLPT.xlsx'));
const snapshot={};
for(const [name,range,img] of [['Nhật ký','A1:H59','baseline_daily.png'],['Đo năng lực','A1:J71','baseline_scores.png']]){
  const sh=wb.worksheets.getItem(name);
  const r=sh.getRange(range);
  snapshot[name]={values:r.values,formulas:r.formulas,range};
  const b=await wb.render({sheetName:name,range:name==='Nhật ký'?'A1:H17':'A1:J19',scale:1.2,format:'png'});
  await fs.writeFile(root+'/tmp/jlpt-v2/'+img,new Uint8Array(await b.arrayBuffer()));
}
await fs.writeFile(root+'/tmp/jlpt-v2/baseline_workbook.json',JSON.stringify(snapshot));
console.log((await wb.inspect({kind:'workbook,sheet',maxChars:2000})).ndjson);
console.log((await wb.inspect({kind:'table',range:"'Nhật ký'!A4:H9",include:'values,formulas',tableMaxRows:6,tableMaxCols:8,maxChars:1800})).ndjson);
console.log((await wb.inspect({kind:'table',range:"'Đo năng lực'!A7:J10",include:'values,formulas',tableMaxRows:4,tableMaxCols:10,maxChars:1800})).ndjson);
