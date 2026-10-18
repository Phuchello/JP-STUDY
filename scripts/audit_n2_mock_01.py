# -*- coding: utf-8 -*-
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    with open('data/mock_exams/n2_mock_01.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    items = data['sections'][0]['items']
    print(f"Total items in Section 1: {len(items)}")

    issues = []
    generic_distractor_count = 0

    for i, q in enumerate(items):
        qid = q.get('id', f'idx_{i}')
        # Check options
        opt_ids = [o.get('id') for o in q.get('options', [])]
        if opt_ids != ['A', 'B', 'C', 'D']:
            issues.append(f"{qid}: Invalid option IDs {opt_ids}")
        ans = q.get('correctAnswer')
        if ans not in ['A', 'B', 'C', 'D']:
            issues.append(f"{qid}: Invalid correct answer {ans}")

        opt_texts = [o.get('text') for o in q.get('options', [])]
        if len(set(opt_texts)) != len(opt_texts):
            issues.append(f"{qid}: Duplicate option texts {opt_texts}")

        exp = q.get('explanationVi', '')
        if not exp or len(exp.strip()) < 10:
            issues.append(f"{qid}: Weak or missing explanationVi ({exp})")

        dists = q.get('distractorExplanations', {})
        for o in ['A', 'B', 'C', 'D']:
            if o != ans:
                d_text = dists.get(o, '')
                if not d_text:
                    issues.append(f"{qid}: Missing distractor {o}")
                elif "Chú ý phân biệt âm ngắt, âm đục và trường âm" in d_text or "Lựa chọn này không phù hợp" in d_text:
                    generic_distractor_count += 1

    print(f"Found {len(issues)} structural issues.")
    for issue in issues[:10]:
        print(f"  - {issue}")
    print(f"Generic distractor explanations found: {generic_distractor_count}")
    for i, q in enumerate(items):
        qid = q.get('id', f'idx_{i}')
        dists = q.get('distractorExplanations', {})
        for o, text in dists.items():
            if "Chú ý phân biệt âm ngắt" in text or "Lựa chọn này không phù hợp" in text:
                print(f"  {qid} [{o}]: {text}")

if __name__ == '__main__':
    main()
