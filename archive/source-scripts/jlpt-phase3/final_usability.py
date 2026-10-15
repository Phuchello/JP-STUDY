from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/'FINAL_PHASE3/JLPT_PRACTICE';T=R/'tmp/jlpt-phase3'
p=P/'app.js';s=p.read_text(encoding='utf-8')
s=s.replace('<p id="voice-status" class="muted"></p>','<p id="voice-status" class="muted"></p><p><a href="https://www.irodori.jpf.go.jp/elementary01/audio/lesson14.html" target="_blank" rel="noopener">Nghe Irodori: liên lạc xin nghỉ · MP3 chính thức</a> (cần mạng, không phải điểm JLPT).</p>')
s=s.replace('<div class="card"><h2>Nghe và nói để dùng ngay</h2>', '<details class="card"><summary>Tùy chọn: luyện một bộ theo mục tiêu</summary><label>Bộ ngắn <select id="recipe">${B.recipes.map(r=>`<option value="${r.id}">${esc(r.id+\' · \'+r.objective)}</option>`).join(\'\')}</select></label>${btn(\'Luyện bộ đã chọn\',\'recipe-start\',true)}<small>Dùng lại cùng 80 câu, vẫn ghi mới/ôn. Đây là luyện có hướng dẫn; không cộng vào điểm mới độc lập.</small></details><div class="card"><h2>Nghe và nói để dùng ngay</h2>')
s=s.replace("on('rest',()=>notice", "on('recipe-start',()=>{if(state.active)throw Error('Hãy nộp hoặc tiếp tục buổi dở trước.');const v=document.querySelector('#fatigue').value;if(!v)throw Error('Chọn mức mệt hôm nay trước.');const r=B.recipes.find(x=>x.id===document.querySelector('#recipe').value),sel=E.select(state,B,{mode:r.mode,recipeId:r.id,fatigue:Number(v),sleepy:document.querySelector('#sleepy').checked,audioAvailable:voices.length>0});if(!sel.ids.length){notice(sel.reason);return;}sel.training=true;E.start(state,B,sel);save();location.hash='practice';});on('rest',()=>notice")
s=s.replace('<div class="card"><h2>Việc tiếp được đề nghị</h2>', '<div class="card"><h2>Nói đời sống · ghi riêng</h2><p>${(state.speaking||[]).length} phiếu nói. 0 = chưa truyền đạt, 1 = truyền đạt được, ? = chưa rõ. Phát âm chưa đánh giá bằng chữ.</p>${(state.speaking||[]).slice(-3).reverse().map(r=>`<p>${esc(B.roleplays.find(x=>x.id===r.roleId)?.learningObjective)} · ${esc(r.at.slice(0,10))}: ${esc(r.intents.join(\' / \'))}</p>`).join(\'\')}</div><div class="card"><h2>Việc tiếp được đề nghị</h2>')
p.write_text(s,encoding='utf-8')
template=(T/'index_template.html').read_text(encoding='utf-8').replace('<link rel="stylesheet" href="styles.css">','<style>'+(P/'styles.css').read_text(encoding='utf-8')+'</style>')
for name in ['bank.js','patterns.js','engine.js','app.js']:template=template.replace('<script src="'+name+'"></script>','<script>'+(P/name).read_text(encoding='utf-8').replace('</script','<\\/script')+'</script>')
(P/'index.html').write_text(template,encoding='utf-8')
# Reuse actual downloaded CSV from the browser for a native Excel handoff check.
p=T/'test_excel.ps1';s=p.read_text(encoding='utf-8');anchor=" $book.Save();$book.Close($false);$book=$null"
csvqa=''' $csvPath=Join-Path $taskRoot 'tmp\\jlpt-phase3\\browser_export.csv'
 $excel.Workbooks.OpenText($csvPath,65001,1,1,1,$false,$false,$false,$true,$false,$false)
 $csvBook=$excel.ActiveWorkbook;$csvSheet=$csvBook.Worksheets.Item(1)
 Test-Value 'Downloaded CSV twelve columns' $csvSheet.UsedRange.Columns.Count 12
 Test-Value 'Downloaded CSV Vietnamese UTF8 header' $csvSheet.Range('H1').Value2 'Đã trả lời'
 $imp.Range('A8:L8').Value2=$csvSheet.Range('A2:L2').Value2
 $csvBook.Close($false);$excel.CalculateFullRebuild()
 Test-Value 'Browser CSV native valid row' $imp.Range('M8').Value2 'Hợp lệ'
 Test-Value 'Browser interrupted practice remains training' $imp.Range('F8').Value2 'Luyện'
 Test-Value 'Browser training excluded from independent score' $imp.Range('G2').Value2 'Chưa có dữ liệu'
 $imp.Range('A8:L8').ClearContents();$excel.CalculateFullRebuild()
'''
s=s.replace(anchor,csvqa+anchor);p.write_text(s,encoding='utf-8')
