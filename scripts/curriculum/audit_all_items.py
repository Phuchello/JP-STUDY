import json
import sys

def audit():
    with open('curriculum/QUESTION_BANK_EXPANDED.json', 'r', encoding='utf-8') as f:
        bank = json.load(f)
    
    questions = bank['questions']
    print(f"Total questions loaded: {len(questions)}")
    
    # Check answer distribution
    from collections import Counter
    ans_dist = Counter(q['correctAnswer'] for q in questions)
    print("Answer distribution:", dict(ans_dist))
    
    # Audit each type
    by_type = {}
    for q in questions:
        by_type.setdefault(q['typeId'], []).append(q)
        
    for tid, qlist in sorted(by_type.items()):
        print(f"\n==========================================")
        print(f"TYPE: {tid} ({len(qlist)} questions)")
        print(f"==========================================")
        for q in qlist:
            sys.stdout.buffer.write(f"\n[{q['id']}] (Level: {q['level']}, Key: {q['correctAnswer']})\n".encode('utf-8'))
            sys.stdout.buffer.write(f"Stem: {q['stem']}\n".encode('utf-8'))
            for opt in q['options']:
                sys.stdout.buffer.write(f"  {opt['id']}. {opt['text']}\n".encode('utf-8'))
            sys.stdout.buffer.write(f"Explanation: {q['explanationVi']}\n".encode('utf-8'))
            dist_keys = sorted(q['distractorExplanations'].keys())
            sys.stdout.buffer.write(f"Distractors: {dist_keys}\n".encode('utf-8'))

if __name__ == '__main__':
    audit()
