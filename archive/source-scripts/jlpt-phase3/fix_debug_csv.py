from pathlib import Path
p=Path(__file__).resolve().parent/'test_excel.ps1';s=p.read_text(encoding='utf-8').replace("$value.GetType().FullName}};Test-Value 'Browser CSV", "$value.GetType().FullName}}};Test-Value 'Browser CSV");p.write_text(s,encoding='utf-8')
