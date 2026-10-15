$ErrorActionPreference='Stop'
$taskRoot='<user>\Music\JP'
$r=[ordered]@{version=$null; controls=@(); error=$null}
$e=$null
try {
 $e=New-Object -ComObject Excel.Application;$e.Visible=$false;$e.DisplayAlerts=$false;$e.AutomationSecurity=3;$r.version=$e.Version
 foreach($p in @('tmp\jlpt-v3\nobook.xlsx','tmp\jlpt-v3\nocols.xlsx','tmp\jlpt-v3\noviews.xlsx','tmp\jlpt-v3\links_only.xlsx')) {
  $w=$null
  try {$w=$e.Workbooks.Open((Join-Path $taskRoot $p),0,$true);$r.controls+=@{file=$p;open=$true;sheets=$w.Worksheets.Count};$w.Close($false);$w=$null}
  catch {$r.controls+=@{file=$p;open=$false;error=$_.Exception.Message;hresult=$_.Exception.HResult}}
 }
 try {$w=$e.Workbooks.Add();$r.controls+=@{file='Excel blank workbook control';open=$true};$w.Close($false)}
 catch {$r.controls+=@{file='Excel blank workbook control';open=$false;error=$_.Exception.Message}}
}catch{$r.error=$_.Exception.Message}finally{if($null-ne $e){$e.Quit();[void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($e)}}
$r|ConvertTo-Json -Depth 5|Set-Content -LiteralPath (Join-Path $taskRoot 'tmp\jlpt-v3\excel_environment_probe.json') -Encoding UTF8
$r|ConvertTo-Json -Depth 5 -Compress
