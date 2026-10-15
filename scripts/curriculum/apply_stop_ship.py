import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def apply_stop_ship():
    bank_path = ROOT / 'curriculum/QUESTION_BANK_EXPANDED.json'
    with open(bank_path, 'r', encoding='utf-8') as f:
        bank = json.load(f)
    
    # Mark all 120 items CONTENT_QA_PENDING
    for q in bank['questions']:
        q['status'] = 'CONTENT_QA_PENDING'
        q['exposureEligible'] = False
        q['diagnosticEligible'] = False
    
    bank['version'] = 'phase-3.7-stop-ship-audit'
    bank['auditStatus'] = 'STOP_SHIP_CONTENT_QA_IN_PROGRESS'
    
    with open(bank_path, 'w', encoding='utf-8') as f:
        json.dump(bank, f, ensure_ascii=False, indent=2)
    print("Marked all 120 questions as CONTENT_QA_PENDING.")

    # Update practice sets
    ps_path = ROOT / 'curriculum/PRACTICE_SETS.json'
    with open(ps_path, 'r', encoding='utf-8') as f:
        ps = json.load(f)
        
    for s in ps['sets']:
        if s['category'] == 'FULL_MOCK_EXAM':
            s['readinessStatus'] = 'NOT_READY — INSUFFICIENT UNIQUE ITEMS'
            s['implementationType'] = 'SPEC_ONLY'
        else:
            s['readinessStatus'] = 'CONTENT_QA_BLOCKED'
            s['implementationType'] = 'SPEC_ONLY'
            s['blockReason'] = 'Phân hệ phụ thuộc vào 120 câu hỏi đang trong quy trình đại tu và thẩm định chất lượng (Emergency Content Repair).'

    ps['version'] = 'phase-3.7-stop-ship'
    ps['countsByStatus'] = {
        'LIVE_VERIFIED': 0, # Practice sets defined here are spec-only; 3 live P0 forms are tracked in QUIZ_FORMS
        'CONTENT_QA_BLOCKED': sum(1 for s in ps['sets'] if s['readinessStatus'] == 'CONTENT_QA_BLOCKED'),
        'NOT_READY': sum(1 for s in ps['sets'] if s['readinessStatus'].startswith('NOT_READY'))
    }
    
    with open(ps_path, 'w', encoding='utf-8') as f:
        json.dump(ps, f, ensure_ascii=False, indent=2)
    print("Updated curriculum/PRACTICE_SETS.json with CONTENT_QA_BLOCKED status.")

if __name__ == '__main__':
    apply_stop_ship()
