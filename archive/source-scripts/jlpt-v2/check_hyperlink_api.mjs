import {Workbook} from '@oai/artifact-tool';
const w=Workbook.create();w.worksheets.add('Tra cứu');
console.log(w.help('*',{search:'hyperlink',include:'index,notes,examples',maxChars:4500}).ndjson);
