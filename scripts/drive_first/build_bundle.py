"""
Reuse audited source items; never generate or rewrite Japanese questions.
Enforces canonical pilot build against QUESTION_BANK_EXPANDED.json and PRACTICE_SETS.json.
Regenerates pilot_payload.js deterministically, builds JP_STUDY_SETUP.gs,
re-extracts bundled payload, and verifies against canonical source.
"""
from pathlib import Path
import json
import hashlib
import csv
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.export_pilot_payload import (
    PILOT_PRACTICE_SET_ID,
    PILOT_QUESTION_IDS,
    export_pilot_payload,
    validate_pilot_payload_against_bank,
    build_pilot_payload
)

BANK_P3 = ROOT / 'deliverables/phase3/JLPT_PRACTICE/question_bank.json'
KEYS_P3 = ROOT / 'deliverables/phase3/ANSWER_KEY_AND_EXPLANATIONS/validated_keys.json'
PATTERNS_P3 = ROOT / 'deliverables/phase3/JAPANESE_PATTERN_LIBRARY/patterns.json'
BANK_EXPANDED = ROOT / 'curriculum/QUESTION_BANK_EXPANDED.json'
PRACTICE_SETS = ROOT / 'curriculum/PRACTICE_SETS.json'
PILOT_PAYLOAD_JS = ROOT / 'DRIVE_SETUP/pilot_payload.js'
SETUP_GS = ROOT / 'DRIVE_SETUP/JP_STUDY_SETUP.gs'
CORE_JS = ROOT / 'scripts/drive_first/core.js'
ADAPTER_JS = ROOT / 'DRIVE_SETUP/workspace_adapter.js'
LIVE_QA_JS = ROOT / 'DRIVE_SETUP/live_qa.js'


def validate_practice_set_eligibility(sets_path=PRACTICE_SETS, bank_path=BANK_EXPANDED):
    """
    Validates MD-N4-VOC-01 release eligibility in PRACTICE_SETS.json and QUESTION_BANK_EXPANDED.json.
    Fails fast if any discrepancy is found.
    """
    with open(sets_path, 'r', encoding='utf-8') as f:
        sets_data = json.load(f)

    pilot_set = next((s for s in sets_data.get('sets', []) if s.get('id') == PILOT_PRACTICE_SET_ID), None)
    if not pilot_set:
        raise ValueError(f"CANONICAL_BUILD_FAILED: Pilot set {PILOT_PRACTICE_SET_ID} not found in {sets_path}")

    status = pilot_set.get('readinessStatus') or pilot_set.get('status')
    if status not in ['QA_PASSED_NOT_DEPLOYED', 'QA_PASSED_READY_FOR_DEPLOYMENT']:
        raise ValueError(f"CANONICAL_BUILD_FAILED: Pilot set {PILOT_PRACTICE_SET_ID} has status '{status}', must be QA_PASSED_NOT_DEPLOYED")

    qids = pilot_set.get('questionIds', [])
    if qids != PILOT_QUESTION_IDS:
        raise ValueError(f"CANONICAL_BUILD_FAILED: Pilot set {PILOT_PRACTICE_SET_ID} question IDs mismatch: {qids} != {PILOT_QUESTION_IDS}")

    # Validate against canonical expanded bank
    with open(bank_path, 'r', encoding='utf-8') as f:
        bank_data = json.load(f)
    bank_map = {q['id']: q for q in bank_data.get('questions', [])}

    for qid in PILOT_QUESTION_IDS:
        if qid not in bank_map:
            raise ValueError(f"CANONICAL_BUILD_FAILED: Question {qid} not found in canonical bank {bank_path}")
        q = bank_map[qid]
        if q.get('status') != 'QA_VERIFIED':
            raise ValueError(f"CANONICAL_BUILD_FAILED: Question {qid} has status {q.get('status')}, expected QA_VERIFIED")
        if not (q.get('stem') or '').strip():
            raise ValueError(f"CANONICAL_BUILD_FAILED: Question {qid} has empty stem")
        opts = q.get('options', [])
        if len(opts) != 4 or [o.get('id') for o in opts] != ['A', 'B', 'C', 'D']:
            raise ValueError(f"CANONICAL_BUILD_FAILED: Question {qid} has invalid options: {opts}")
        if q.get('correctAnswer') not in ['A', 'B', 'C', 'D']:
            raise ValueError(f"CANONICAL_BUILD_FAILED: Question {qid} has invalid correctAnswer: {q.get('correctAnswer')}")
        if not (q.get('explanationVi') or '').strip():
            raise ValueError(f"CANONICAL_BUILD_FAILED: Question {qid} has empty explanationVi")
        if not q.get('distractorExplanations'):
            raise ValueError(f"CANONICAL_BUILD_FAILED: Question {qid} missing distractorExplanations")

    return True


def verify_bundled_pilot_payload(setup_gs_path=SETUP_GS, expected_payload=None, bank_path=BANK_EXPANDED):
    """
    Re-extracts JP_PILOT_DATA from bundled JP_STUDY_SETUP.gs and verifies against canonical source.
    Fails fast if any stale artifact, mutation, or hash drift is detected.
    """
    content = setup_gs_path.read_text(encoding='utf-8')
    m = re.search(r'var\s+JP_PILOT_DATA\s*=\s*(\{.*?\});\n', content, re.DOTALL)
    if not m:
        raise ValueError("CANONICAL_BUILD_FAILED: var JP_PILOT_DATA definition not found in bundled JP_STUDY_SETUP.gs")

    bundled_payload = json.loads(m.group(1))

    if expected_payload:
        if bundled_payload.get('contentDigest') != expected_payload.get('contentDigest'):
            raise ValueError(
                f"CANONICAL_BUILD_FAILED: Bundled content digest {bundled_payload.get('contentDigest')} "
                f"!= expected {expected_payload.get('contentDigest')}"
            )
        if bundled_payload.get('questions') != expected_payload.get('questions'):
            raise ValueError("CANONICAL_BUILD_FAILED: Bundled questions do not match expected payload")

    # Validate against canonical bank
    validate_pilot_payload_against_bank(bundled_payload, bank_path=bank_path)
    return bundled_payload


def build_bundle():
    """
    Orchestrates canonical pilot validation, payload regeneration, bundle construction, and verification.
    """
    # 1. Validate practice set eligibility and canonical bank
    validate_practice_set_eligibility(PRACTICE_SETS, BANK_EXPANDED)

    # 2. Regenerate pilot_payload.js deterministically
    canonical_payload = export_pilot_payload(bank_path=BANK_EXPANDED)

    # 3. Build legacy P0/P1 quizzes and structures
    b = json.loads(BANK_P3.read_text(encoding='utf-8'))
    keys = json.loads(KEYS_P3.read_text(encoding='utf-8'))
    lookup = {q['id']: q for q in b['questions']}

    def ids(group, a, z):
        return [f'N4-{group}-{i:03}' for i in range(a, z + 1)]

    spec = [
        ('W01-B01', 'Trợ từ trong câu', ids('PART', 1, 5), 5, 8),
        ('W01-B02', 'Từ và kanji', ids('VOC', 1, 8), 5, 10),
        ('W01-B03', 'Chia thể cơ bản', ids('CONJ', 1, 5), 5, 8),
        ('W01-B04', 'Đọc thông báo ngắn', ids('SHORT', 1, 5), 8, 12),
        ('W01-B05', 'Hiểu mẫu câu', ids('GRAM', 1, 6), 5, 10),
        ('W02-B01', 'Trợ từ trong ngữ cảnh', ids('PART', 6, 10), 5, 8),
        ('W02-B02', 'Thể động từ và tính từ', ids('CONJ', 6, 10) + ids('GRAM', 9, 12), 8, 12),
        ('W02-B03', 'Nối ý và ý câu', ids('GRAM', 7, 8) + ids('INTERP', 1, 6), 8, 12),
        ('W02-B04', 'Sắp xếp câu', ids('ORDER', 1, 8), 8, 12),
        ('W02-B05', 'Đọc và tìm bằng chứng', ids('SHORT', 6, 8) + ids('MED', 1, 6), 10, 15)
    ]
    quizzes = [
        {
            'id': i,
            'title': f'{i} | N4 {n} | {len(q)} câu',
            'objective': n,
            'questionIds': q,
            'minutes': [a, z],
            'releaseGroup': 'P0' if j < 3 else 'P1',
            'week': 1 if i.startswith('W01') else 2,
            'mode': 'self_reported_unaided_or_review',
            'status': 'QA_PENDING_LIVE_FORMS'
        }
        for j, (i, n, q, a, z) in enumerate(spec)
    ]
    allids = [i for q in quizzes for i in q['questionIds']]
    assert len(allids) == len(set(allids)) == 68
    assert all(5 <= len(q['questionIds']) <= 10 for q in quizzes)
    assert all(not lookup[i].get('audio') for i in allids)
    for i in allids:
        q = lookup[i]
        k = next(k for k in keys['questions'] if k['id'] == i)
        assert k['correctAnswer'] == q['correctAnswer']
        assert len({o['text'] for o in q['options']}) == 4

    data = {
        'version': 'drive-first-2026.10.15',
        'sourceBankSha256': hashlib.sha256(BANK_P3.read_bytes()).hexdigest(),
        'answerKeyDigest': b['answerKeyDigest'],
        'timezone': 'Asia/Tokyo',
        'quizzes': quizzes,
        'questions': {i: lookup[i] for i in allids},
        'roles': b['roleplays'],
        'patternNames': {p['id']: p['nameVi'] for p in json.loads(PATTERNS_P3.read_text(encoding='utf-8'))['patterns']}
    }

    role_text = [
        '# Chọn một vai nói, khoảng 3 phút', '',
        'Bốn tình huống gốc đã QA, dùng lại từ pilot. Đây là luyện có hướng dẫn, không là phép đo nói độc lập hoặc điểm JLPT. Chọn một vai, chép khối vào Gemini; chưa cần làm cả bốn. Dữ kiện là tình huống hư cấu, không phải lịch cá nhân.', ''
    ]
    for role in b['roleplays']:
        role_text += [
            '## ' + role['id'] + ' — ' + role['learningObjective'], '',
            '```text',
            'Đóng vai người đối thoại cho bài luyện tiếng Nhật sau.',
            'MÃ: ' + role['id'],
            'NGỮ CẢNH: ' + role['taskVi'],
            'Ý CẦN TRUYỀN ĐẠT: ' + '; '.join(role['requiredIntents']),
            'THẺ NGƯỜI ĐỐI THOẠI: ' + ' / '.join(role['partnerTurns']),
            'Để tôi mở lời trước, rồi hỏi từng lượt và CHỜ. Không đưa câu mẫu cho vai tôi trước khi tôi thử. Sau 3–6 lượt chỉ sửa 1–2 lỗi cản nghĩa, nhờ tôi nói lại với một dữ kiện khác. Không đoán vì sao tôi sai, không gán cấp, không chấm phát âm từ văn bản. Nếu tôi mệt, cho phép dừng.',
            '```', ''
        ]
    (ROOT / 'deliverables/phase3.5/VAI_NOI.md').write_text('\n'.join(role_text), encoding='utf-8', newline='\n')
    (ROOT / 'QUIZ_FORMS/quiz_plan.json').write_text(json.dumps({k: v for k, v in data.items() if k not in ['questions', 'roles', 'patternNames']}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')

    with (ROOT / 'QUIZ_FORMS/answer_mapping.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(['quiz_id', 'position', 'question_id', 'correct_label', 'correct_text', 'points', 'stimulus_id', 'concept_id'])
        for quiz in quizzes:
            for pos, i in enumerate(quiz['questionIds'], 1):
                q = lookup[i]
                w.writerow([quiz['id'], pos, i, q['correctAnswer'], next(o['text'] for o in q['options'] if o['id'] == q['correctAnswer']), 1, q['stimulusId'], q['conceptId']])

    (ROOT / 'tmp/drive-first/data.json').write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')

    core = CORE_JS.read_text(encoding='utf-8')
    adapter = ADAPTER_JS.read_text(encoding='utf-8')
    liveqa = LIVE_QA_JS.read_text(encoding='utf-8')
    pilot = PILOT_PAYLOAD_JS.read_text(encoding='utf-8')

    SETUP_GS.write_text(
        '// Generated from audited payload + pilot_payload.js + core.js + workspace_adapter.js. No credentials.\n'
        + 'const JP_DATA=' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n'
        + pilot + '\n'
        + core + '\n'
        + adapter + liveqa,
        encoding='utf-8',
        newline='\n'
    )

    # 4. Re-extract and verify bundled pilot data against canonical source
    verify_bundled_pilot_payload(SETUP_GS, expected_payload=canonical_payload, bank_path=BANK_EXPANDED)

    result = {
        'quizzes': len(quizzes),
        'uniqueReusedQuestions': len(allids),
        'unassignedOriginalQuestions': len(b['questions']) - len(allids),
        'regeneratedQuestions': 0,
        'pilotValidated': True,
        'pilotDigest': canonical_payload['contentDigest']
    }
    print(json.dumps(result))
    return result


if __name__ == '__main__':
    build_bundle()
