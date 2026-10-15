from pathlib import Path
T=Path(__file__).resolve().parent
p=T/'test_excel.ps1';s=p.read_text(encoding='utf-8').replace("$imp.Range('A8:L8').Value2=$csvSheet.Range('A2:L2').Value2", "$csvSheet.Range('A2:L2').Copy($imp.Range('A8'))");p.write_text(s,encoding='utf-8')
p=T/'build_tracker.mjs';s=p.read_text(encoding='utf-8').replace("s.freezePanes.freezeRows(7);", "s.getRange('A2:M2').format={wrapText:true,rowHeight:56};s.freezePanes.freezeRows(7);");p.write_text(s,encoding='utf-8')
