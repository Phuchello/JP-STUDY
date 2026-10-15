import json

with open('curriculum/QUESTION_BANK_EXPANDED.json', 'r', encoding='utf-8') as f:
    bank = json.load(f)

with open('tmp/all_stars.txt', 'w', encoding='utf-8') as out:
    for q in bank['questions']:
        if 'STAR' in q['typeId']:
            out.write(f"[{q['id']}] Key: {q['correctAnswer']}\nStem: {q['stem']}\n")
            for o in q['options']:
                out.write(f"  {o['id']}: {o['text']}\n")
            out.write(f"Expl: {q['explanationVi']}\n\n")
