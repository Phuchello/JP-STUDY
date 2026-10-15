from pathlib import Path
import json

root=Path(__file__).resolve().parent
base='https://www.jlpt.jp/samples/sample2018/'
blocks=[]
def add(code,level,skill,part,questions,minutes,description):
    blocks.append(dict(code=code,level=level,skill=skill,part=part,questions=questions,limit=minutes,description=description,
                       url=base+'pdf/'+level+part+'.pdf'))
add('N4-G1','N4','Ngữ pháp','G',[1,2,3,4,5,6],6,'Nhóm 1 câu 1 đến 6')
add('N4-G2','N4','Ngữ pháp','G',[16,17,21,22,23,24,25],6,'Nhóm 2 câu 16–17 và toàn bộ Nhóm 3 câu 21–25')
add('N4-V','N4','Từ và kanji','V',[1,2,10,11,16,17,26,27,31,32],8,'Mỗi nhóm 1–5 lấy 2 câu đầu')
add('N4-R','N4','Đọc','R',[26,30,31,32,33],15,'Bài ngắn đầu Nhóm 4 câu 26 và toàn bộ Nhóm 5 câu 30–33')
add('N4-L1','N4','Nghe','L',['M1-1','M1-2','M2-1','M2-2'],10,'Nhóm nghe 1 và 2, mỗi nhóm câu 1–2')
add('N4-L2','N4','Nghe','L',['M3-1','M3-2','M4-1','M4-2'],8,'Nhóm nghe 3 và 4, mỗi nhóm câu 1–2')
add('N3-G','N3','Ngữ pháp','G',[1,2,3,4,14,15],7,'Nhóm 1 câu 1–4 và Nhóm 2 câu 14–15')
add('N3-V','N3','Từ và kanji','V',[1,2,9,10,15,16,26,27,31,32],8,'Mỗi nhóm 1–5 lấy 2 câu đầu')
add('N3-R','N3','Đọc','R',[24,28,29,30],12,'Bài ngắn đầu Nhóm 4 câu 24 và bài trung bình đầu Nhóm 5 câu 28–30')
add('N3-L1','N3','Nghe','L',['M1-1','M1-2','M2-1','M2-2'],10,'Nhóm nghe 1 và 2, mỗi nhóm câu 1–2')
add('N3-L2','N3','Nghe','L',['M3-1','M3-2','M4-1','M4-2','M5-1','M5-2'],10,'Nhóm nghe 3, 4 và 5, mỗi nhóm câu 1–2')
row=8
for i,b in enumerate(blocks):
    b.update(start_row=row,end_row=row+len(b['questions'])-1,summary_row=78+i)
    row+=len(b['questions'])
manifest={'blocks':blocks,'answer_rows':[8,73],'summary_rows':[78,88],
          'pdfs':{level:{part:base+'pdf/'+level+part+'.pdf' for part in ['V','G','R','L','answer','script']} for level in ['N4','N3']},
          'audio':{level:{str(g):base+'mp3/'+level+'Q'+str(g)+'.mp3' for g in range(1,5 if level=='N4' else 6)} for level in ['N4','N3']}}
(root/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps([dict(code=b['code'],answers=f"F{b['start_row']}:F{b['end_row']}",grade=f"G{b['start_row']}:G{b['end_row']}",summary=b['summary_row']) for b in blocks],ensure_ascii=False))
