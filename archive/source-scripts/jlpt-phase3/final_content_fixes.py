from pathlib import Path
import json
R=Path(__file__).resolve().parents[2];O=R/'FINAL_PHASE3';T=R/'tmp/jlpt-phase3';P=O/'JLPT_PRACTICE'
p=T/'test_excel.ps1';s=p.read_text(encoding='utf-8');s=s.replace('$imp.Cells.Item(8,$i+1).Value2=$row[$i]',"$imp.Range(([char](65+$i)).ToString()+'8').Value2=$row[$i]").replace('$imp.Cells.Item(9,$i+1).Value2=$row[$i]',"$imp.Range(([char](65+$i)).ToString()+'9').Value2=$row[$i]");p.write_text(s,encoding='utf-8')
deadline={'id':'JF-DEADLINE','title':'JF 日本語教育通信: まで・までに','url':'https://www.jpf.go.jp/j/project/japanese/teach/tsushin/grammar/200911.html'}
waive={'id':'JF-WAIVER','title':'JF Irodori Grammar_all: 初中級L8-23 Vなくてもいい, PDF p209','url':'https://www.irodori.jpf.go.jp/assets/data/Grammar_all.pdf#page=209'}
b=json.loads((P/'question_bank.json').read_text(encoding='utf-8'))
for q in b['questions']:
 if q['id']=='N4-PART-005':q['references']=[deadline]
 if q['id']=='N4-INTERP-003':q['references']=[waive]
 if q['categoryCode']=='CONJ':q['patternId']='G05';q['reviewStrategy']='Ôn quy tắc thể thường ở nguồn TUFS038 trước; thẻ G05 dùng thể từ điển/thể た trong thứ tự thời gian. '+q['reviewStrategy']
(P/'question_bank.json').write_text(json.dumps(b,ensure_ascii=False,indent=2),encoding='utf-8');(P/'bank.js').write_text('window.PracticeBank='+json.dumps(b,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
kp=O/'ANSWER_KEY_AND_EXPLANATIONS/validated_keys.json';keys=json.loads(kp.read_text(encoding='utf-8'))
for q in keys['questions']:
 orig=next(x for x in b['questions'] if x['id']==q['id']);q['references']=orig['references'];q['patternId']=orig['patternId']
kp.write_text(json.dumps(keys,ensure_ascii=False,indent=2),encoding='utf-8')
lp=O/'JAPANESE_PATTERN_LIBRARY/patterns.json';lib=json.loads(lp.read_text(encoding='utf-8'))
for p in lib['patterns']:
 if p['id']=='G04':p['sources']=[deadline]
 if p['id']=='G05':p['sources'].append({'title':'TUFS 普通形 và biến đổi','url':'https://www.coelang.tufs.ac.jp/mt/ja/gmod/contents/explanation/038.html'})
lp.write_text(json.dumps(lib,ensure_ascii=False,indent=2),encoding='utf-8');(P/'patterns.js').write_text('window.PatternLibrary='+json.dumps(lib,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
rp=O/'RESEARCH_EVIDENCE_LEDGER.md';s=rp.read_text(encoding='utf-8');s=s.replace('online 2021-11-25 theo PMC; DOI record hiển thị 2021-11; print 2022, 148(1–2)','2021-11 theo DOI-linked record; issue 148(1–2) năm 2022; chưa chốt ngày online trong các nguồn truy xuất')
s=s.replace('thêm 1 truy vấn TUFS đích (10 kết quả)','thêm 3 truy vấn đích TUFS/JF (10+5+5 kết quả)')
s=s.replace('không phải 180 nghiên cứu đã đọc','không phải 190 nghiên cứu đã đọc')
s=s.replace('TUFS053 không trực tiếp triển khai toàn bộ までに; thẻ deadline là tổng hợp dạy học, giữ hạn chế dẫn nguồn chi tiết.','Đã bổ sung [JF giải thích まで・までに](https://www.jpf.go.jp/j/project/japanese/teach/tsushin/grammar/200911.html) (mục 2009-11, ngày cụ thể không hiển thị) cho PART005/G04; [Irodori Grammar_all p209](https://www.irodori.jpf.go.jp/assets/data/Grammar_all.pdf#page=209), 初中級L8-23 cho INTERP003/なくてもいい. Chỉ dùng khái niệm cần thiết, không giao đọc 245 trang.')
rp.write_text(s,encoding='utf-8');print('Source gaps corrected; native fixture addressing repaired')
