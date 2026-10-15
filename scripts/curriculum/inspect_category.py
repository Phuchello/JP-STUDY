import json

with open('curriculum/QUESTION_BANK_EXPANDED.json', 'r', encoding='utf-8') as f:
    bank = json.load(f)

with open('tmp/all_questions_detail.txt', 'w', encoding='utf-8') as out:
    for q in bank['questions']:
        out.write(f"ID: {q['id']} | Level: {q['level']} | Type: {q['typeId']} | Key: {q['correctAnswer']}\n")
        out.write(f"Stem: {q['stem']}\n")
        if q.get('contextPassage'):
            out.write(f"Passage: {q['contextPassage']}\n")
        for o in q['options']:
            out.write(f"  {o['id']}: {o['text']}\n")
        out.write(f"Explanation: {q['explanationVi']}\n")
        out.write(f"Distractors: {json.dumps(q['distractorExplanations'], ensure_ascii=False)}\n")
        out.write("-" * 60 + "\n\n")

print("Dumped all questions to tmp/all_questions_detail.txt")
