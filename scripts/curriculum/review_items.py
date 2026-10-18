import sys
import json
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

with open('curriculum/PRACTICE_ENGINE_BANK.json', 'r', encoding='utf-8') as f:
    bank = json.load(f)

by_type = defaultdict(list)
for q in bank['questions']:
    if q.get('status') != 'QUARANTINED':
        by_type[(q['level'], q['typeId'])].append(q)

print(f"Sampling 1 item from each of the {len(by_type)} active question types:")
for (lvl, tid), qlist in sorted(by_type.items()):
    sample = qlist[0]
    print(f"\n=== [{lvl}] {tid} (Total: {len(qlist)}) | ID: {sample['id']} ===")
    if sample.get('contextPassage'):
        print(f"Passage ({len(sample['contextPassage'])} chars): {sample['contextPassage'][:80]}...")
    print(f"Stem: {sample['stem']}")
    opts = " | ".join([f"{o['id']}: {o['text']}" for o in sample['options']])
    print(f"Options: {opts}")
    print(f"Key: {sample['correctAnswer']}")
    print(f"Vi: {sample['explanationVi'][:100]}...")
