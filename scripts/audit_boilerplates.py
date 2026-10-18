# -*- coding: utf-8 -*-
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('data/mock_exams/n2_mock_01.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

items = data['sections'][0]['items']
boilerplate_phrases = [
    'Không phù hợp với ngữ cảnh',
    'Cách đọc sai cho chữ Hán',
    'Mẫu ngữ pháp không phù hợp',
    'Không mang nghĩa tương đương',
    'Sử dụng từ',
    'Nội dung sai lệch',
    'Nội dung phương án không đúng',
    'Sai sót trong việc',
    'Sai với diễn giải',
    'Thông tin không khớp'
]

matches = {}
for q in items:
    qid = q['id']
    for opt, exp in q.get('distractorExplanations', {}).items():
        for bp in boilerplate_phrases:
            if bp in exp:
                matches.setdefault(bp, []).append((qid, opt, exp))

for bp, lst in matches.items():
    print(f"{bp}: {len(lst)} occurrences")

total_boilerplate = sum(len(lst) for lst in matches.values())
print(f"Total boilerplate distractors: {total_boilerplate} across {len(items)} questions")
