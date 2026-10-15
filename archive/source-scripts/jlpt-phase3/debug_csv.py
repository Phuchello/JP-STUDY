from pathlib import Path
p=Path(__file__).resolve().parent/'test_excel.ps1';s=p.read_text(encoding='utf-8').replace("Test-Value 'Browser CSV native valid row'", "$report.csvValues=@();for($col=1;$col -le 12;$col++) {$value=$imp.Cells.Item(8,$col).Value2; $report.csvValues+=@{column=$col;value=$value;type=if($null -eq $value){'null'}else{$value.GetType().FullName}};Test-Value 'Browser CSV native valid row'")
p.write_text(s,encoding='utf-8')
