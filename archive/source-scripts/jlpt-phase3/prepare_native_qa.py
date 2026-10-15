from pathlib import Path
import re
R=Path(__file__).resolve().parents[2];T=R/'tmp/jlpt-phase3'
s=(R/'tmp/jlpt-v3/test_excel.ps1').read_text(encoding='utf-8').replace('tmp\\jlpt-v3\\excel_native_tests.json','tmp\\jlpt-phase3\\excel_native_tests.json').replace('FINAL_V3\\JLPT_PROGRESS_TRACKER_FINAL.xlsx','FINAL_PHASE3\\JLPT_PROGRESS_TRACKER.xlsx').replace('tmp\\jlpt-v3\\excel_native_fixture.xlsx','tmp\\jlpt-phase3\\excel_native_fixture.xlsx')
new=''' $imp=$book.Worksheets.Item('Luyện tập')
 Test-Value 'Six worksheets preserve five old' $book.Worksheets.Count 6
 Test-Value 'Import blank score unknown' $imp.Range('G2').Value2 'Chưa có dữ liệu'
 $row=@('native-test','2026-10-15','N4','Ngữ pháp','ORIG-test','Mới',3.0,4.0,5.0,2.0,'','test fixture')
 for($i=0;$i -lt 12;$i++) {$imp.Cells.Item(8,$i+1).Value2=$row[$i]}
 $excel.CalculateFullRebuild()
 Test-Value 'Native import valid row' $imp.Range('M8').Value2 'Hợp lệ'
 Test-Value 'Native import numerator' $imp.Range('C2').Value2 3
 Test-Value 'Native answered denominator' $imp.Range('E2').Value2 4
 Test-Value 'Native import independent accuracy' $imp.Range('G2').Value2 0.75
 for($i=0;$i -lt 12;$i++) {$imp.Cells.Item(9,$i+1).Value2=$row[$i]}
 $excel.CalculateFullRebuild()
 Test-Value 'Native duplicate prevented' $imp.Range('M9').Value2 'Kiểm tra/trùng'
 Test-Value 'Native duplicate no inflation' $imp.Range('C2').Value2 3
 $imp.Range('F9').Value2='Hỗ trợ';$excel.CalculateFullRebuild()
 Test-Value 'Native assisted distinct data row' $imp.Range('M9').Value2 'Hợp lệ'
 Test-Value 'Native assisted excluded from new accuracy' $imp.Range('C2').Value2 3
 $imp.Range('G9').Value2=8.0;$excel.CalculateFullRebuild()
 Test-Value 'Native invalid counts caught' $imp.Range('M9').Value2 'Kiểm tra/trùng'
 $imp.Range('A8:L9').ClearContents();$excel.CalculateFullRebuild()
 Test-Value 'Native cleared no invented data' $imp.Range('G2').Value2 'Chưa có dữ liệu'
'''
s=s.replace(' $book.Save();$book.Close($false);$book=$null',new+' $book.Save();$book.Close($false);$book=$null')
(T/'test_excel.ps1').write_text(s,encoding='utf-8')
