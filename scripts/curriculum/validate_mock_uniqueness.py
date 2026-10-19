# -*- coding: utf-8 -*-
"""
JP-STUDY: VALIDATE MOCK EXAM UNIQUENESS & INTEGRITY GATE
Validates that ALL mocks (N2-MOCK-01, N2-MOCK-02, N2-MOCK-03) have:
1. Exactly 105 items (75 Section 1 + 30 Section 2).
2. ZERO internal or cross-mock ID collisions, and zero collisions with practice bank.
3. ZERO verbatim duplicate question stems or context passages across mocks.
4. Complete options (3 for Mondai 4, 4 for others), valid keys, Vietnamese explanations, and distractor rationale.
5. Verified audio mappings and existing physical files for all 30 listening items per mock.
"""
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.stdout.reconfigure(encoding='utf-8')

def validate_uniqueness():
    print("=== JLPT N2 Mock Exam Uniqueness & Quality Gate (All Mocks) ===")

    mock_files = {
        'N2-MOCK-01': ROOT / 'data/mock_exams/n2_mock_01.json',
        'N2-MOCK-02': ROOT / 'data/mock_exams/n2_mock_02.json',
        'N2-MOCK-03': ROOT / 'data/mock_exams/n2_mock_03.json',
        'N2-MOCK-04': ROOT / 'data/mock_exams/n2_mock_04.json',
    }
    if (ROOT / 'data/mock_exams/n2_mock_05.json').exists():
        mock_files['N2-MOCK-05'] = ROOT / 'data/mock_exams/n2_mock_05.json'
    if (ROOT / 'data/mock_exams/n2_mock_06.json').exists():
        mock_files['N2-MOCK-06'] = ROOT / 'data/mock_exams/n2_mock_06.json'


    loaded_mocks = {}
    for name, path in mock_files.items():
        if not path.exists():
            print(f"ERROR: {path} does not exist!")
            sys.exit(1)
        with open(path, 'r', encoding='utf-8') as f:
            loaded_mocks[name] = json.load(f)

    errors = []
    all_seen_ids = set()
    mock_stems_map = {}
    mock_passages_map = {}

    # Load practice bank IDs
    bank_ids = set()
    bank_path = ROOT / 'data/practice_bank.json'
    if bank_path.exists():
        with open(bank_path, 'r', encoding='utf-8') as f:
            bank = json.load(f)
        bank_ids = {it['id'] for it in bank.get('items', [])}

    for name, mock in loaded_mocks.items():
        print(f"\n--- Checking {name} ---")
        sections = mock.get('sections', [])
        if len(sections) != 2:
            errors.append(f"[{name}] Has {len(sections)} sections, expected 2.")
            continue

        sec1_items = sections[0].get('items', [])
        sec2_items = sections[1].get('items', [])
        total_items = sec1_items + sec2_items

        print(f"  Sec 1: {len(sec1_items)} | Sec 2: {len(sec2_items)} | Total: {len(total_items)}")

        if len(sec1_items) != 75:
            errors.append(f"[{name}] Section 1 item count is {len(sec1_items)}, expected 75.")
        if len(sec2_items) != 30:
            errors.append(f"[{name}] Section 2 item count is {len(sec2_items)}, expected 30.")

        # Check IDs
        mock_ids = [it['id'] for it in total_items]
        if len(mock_ids) != len(set(mock_ids)):
            dup = [qid for qid in mock_ids if mock_ids.count(qid) > 1]
            errors.append(f"[{name}] Internal duplicate IDs: {set(dup)}")

        cross_collisions = all_seen_ids.intersection(set(mock_ids))
        if cross_collisions:
            errors.append(f"[{name}] Cross-mock ID collision: {cross_collisions}")
        all_seen_ids.update(mock_ids)

        bank_collisions = bank_ids.intersection(set(mock_ids))
        if bank_collisions:
            errors.append(f"[{name}] ID collision with practice bank: {bank_collisions}")

        # Stem & Passage collection
        mock_stems = {}
        mock_passages = {}
        for q in total_items:
            qid = q['id']
            stem = (q.get('stem') or '').strip()
            passage = (q.get('contextPassage') or '').strip()

            # Cross-check stems against previous mocks
            if q.get('skill') != 'Listening' and len(stem) > 5:
                for prev_name, prev_stems in mock_stems_map.items():
                    if stem in prev_stems:
                        errors.append(f"[{name}] Stem collision with {prev_name} [{qid}]: '{stem[:40]}...'")
                mock_stems[stem] = qid

            # Cross-check passages against previous mocks
            if passage:
                for prev_name, prev_passages in mock_passages_map.items():
                    if passage in prev_passages:
                        errors.append(f"[{name}] Context passage collision with {prev_name} [{qid}]")
                mock_passages[passage] = qid

            # Validate question completeness
            opts = q.get('options', [])
            ans = q.get('correctAnswer')
            exp = q.get('explanationVi', '')
            dist = q.get('distractorExplanations', {})
            is_m4 = (q.get('typeId') == 'N2-LIS-RESP')

            expected_opt_count = 3 if is_m4 else 4
            if len(opts) != expected_opt_count:
                errors.append(f"[{name}][{qid}] Expected {expected_opt_count} options, got {len(opts)}")

            opt_ids = [o['id'] for o in opts]
            if ans not in opt_ids:
                errors.append(f"[{name}][{qid}] Correct answer {ans} not in options {opt_ids}")

            if len(exp.strip()) < 15:
                errors.append(f"[{name}][{qid}] Explanation is too brief ({len(exp)} chars)")

            expected_dist = set(opt_ids) - {ans}
            missing_dist = expected_dist - set(dist.keys())
            if missing_dist:
                errors.append(f"[{name}][{qid}] Missing distractor explanations for {missing_dist}")

            # Check audio for Section 2
            if q in sec2_items:
                audio_url = q.get('audioUrl', '')
                if not audio_url:
                    errors.append(f"[{name}][{qid}] Missing audioUrl")
                else:
                    rel_audio_path = ROOT / 'docs' / audio_url
                    if not rel_audio_path.exists():
                        errors.append(f"[{name}][{qid}] Audio file not found at {rel_audio_path}")

        mock_stems_map[name] = mock_stems
        mock_passages_map[name] = mock_passages

    print("\n--------------------------------------------------")
    if errors:
        print(f"❌ VALIDATION FAILED with {len(errors)} error(s):")
        for err in errors[:25]:
            print(f"  - {err}")
        if len(errors) > 25:
            print(f"  ... and {len(errors) - 25} more errors.")
        sys.exit(1)
    else:
        print(f"✅ ALL VALIDATION CHECKS PASSED FOR ALL {len(loaded_mocks)} MOCKS ({len(all_seen_ids)} ITEMS, {len(loaded_mocks)*30} AUDIO TRACKS):")
        print("  - Exactly 105 items per mock (75 Section 1 + 30 Section 2)")
        print(f"  - Zero ID collisions across {', '.join(loaded_mocks.keys())}, and practice bank")
        print("  - Zero duplicate question stems or context passages")
        print("  - 100% options, keys, explanations, and distractor rationale verified")
        print(f"  - 100% audio files exist on disk and mapped for Section 2 ({len(loaded_mocks)*30}/{len(loaded_mocks)*30})")
        print("Quality gate status: PASS")

if __name__ == '__main__':
    validate_uniqueness()
