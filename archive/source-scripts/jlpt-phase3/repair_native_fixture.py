from pathlib import Path
p=Path(__file__).resolve().parent/'test_excel.ps1';s=p.read_text(encoding='utf-8')
values=["'native-test'","'2026-10-15'","'N4'","'Ngữ pháp'","'ORIG-test'","'Mới'",'3.0','4.0','5.0','2.0',"''","'test fixture'"]
for row in [8,9]:
 old="for($i=0;$i -lt 12;$i++) {$imp.Range(([char](65+$i)).ToString()+'"+str(row)+"').Value2=$row[$i]}"
 s=s.replace(old,'\n'.join(" $imp.Range('"+chr(65+i)+str(row)+"').Value2="+v for i,v in enumerate(values)))
s=s.replace("$report.error=$_.Exception.Message", "$report.error=$_.Exception.Message; $report.stack=$_.ScriptStackTrace")
p.write_text(s,encoding='utf-8')
