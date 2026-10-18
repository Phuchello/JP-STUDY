import json
import unicodedata
from collections import defaultdict

with open('curriculum/PRACTICE_ENGINE_BANK.json', 'r', encoding='utf-8') as f:
    bank = json.load(f)

questions = bank['questions']

def normalize_text(t):
    if not t:
        return ''
    return unicodedata.normalize('NFKC', t.strip())

duplicate_options = []
invalid_keys = []
stem_duplicates = defaultdict(list)
blank_fields = []

for q in questions:
    qid = q['id']
    opts = q.get('options', [])
    opt_texts = [normalize_text(o.get('text', '')) for o in opts]
    
    # Check duplicate options
    if len(opt_texts) != len(set(opt_texts)):
        duplicate_options.append({
            'id': qid,
            'level': q.get('level'),
            'typeId': q.get('typeId'),
            'stem': q.get('stem', ''),
            'options': opt_texts,
            'correctAnswer': q.get('correctAnswer')
        })
        
    # Check valid correct answer
    c_ans = q.get('correctAnswer')
    valid_opt_ids = [o.get('id') for o in opts]
    if c_ans not in valid_opt_ids:
        invalid_keys.append((qid, c_ans, valid_opt_ids))
        
    # Check empty stems or options
    if not q.get('stem', '').strip():
        blank_fields.append((qid, 'empty stem'))
    for o in opts:
        if not o.get('text', '').strip():
            blank_fields.append((qid, f"empty option {o.get('id')}"))
            
    # Track stem duplicates
    stem_norm = normalize_text(q.get('stem', ''))
    stem_duplicates[stem_norm].append(qid)

reused_stems = {stem: qids for stem, qids in stem_duplicates.items() if len(qids) > 1}

report = {
    'totalQuestions': len(questions),
    'duplicateOptionsCount': len(duplicate_options),
    'duplicateOptions': duplicate_options,
    'invalidKeysCount': len(invalid_keys),
    'invalidKeys': invalid_keys,
    'reusedStemsCount': len(reused_stems),
    'reusedStems': [{'stem': stem, 'qids': qids} for stem, qids in reused_stems.items()],
    'blankFields': blank_fields
}

with open('curriculum/audit_defects.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print(f"Audit completed: {len(duplicate_options)} questions with duplicate options, {len(reused_stems)} reused stems.")
