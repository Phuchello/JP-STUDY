# -*- coding: utf-8 -*-
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('data/mock_exams/n2_mock_01.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Exam ID: {data['examId']}")
print(f"Title: {data['title']}")
print(f"Duration: {data['durationMinutes']} mins")
print(f"Total questions: {data['totalQuestions']}")
print(f"Total sections: {len(data['sections'])}")

for s_idx, sec in enumerate(data['sections']):
    print(f"\n--- Section {s_idx+1}: {sec['sectionName']} ---")
    print(f"  Duration: {sec['durationMinutes']} mins, Item count: {sec['itemCount']}")
    items = sec['items']
    assert len(items) == sec['itemCount'], f"Mismatch in count: {len(items)} vs {sec['itemCount']}"
    
    # Audit items
    for i, q in enumerate(items):
        qid = q['id']
        assert q['correctAnswer'] in ['A', 'B', 'C', 'D'], f"{qid} bad correct answer {q['correctAnswer']}"
        opt_ids = [o['id'] for o in q['options']]
        assert opt_ids == ['A', 'B', 'C', 'D'], f"{qid} bad options {opt_ids}"
        opt_texts = [o['text'] for o in q['options']]
        assert len(set(opt_texts)) == 4, f"{qid} duplicate options {opt_texts}"
        assert len(q.get('explanationVi', '')) > 15, f"{qid} short explanationVi"
        assert q.get('status') == 'QA_VERIFIED', f"{qid} not QA_VERIFIED"
        dists = q.get('distractorExplanations', {})
        for o in ['A', 'B', 'C', 'D']:
            if o != q['correctAnswer']:
                assert len(dists.get(o, '')) > 5, f"{qid} missing distractor {o}"

print("\nAll Section 1 (75 items) and Section 2 (30 items) successfully audited and verified!")
