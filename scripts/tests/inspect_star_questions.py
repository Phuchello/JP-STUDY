import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

def main():
    for m in ['01', '02']:
        with open(f'data/mock_exams/n2_mock_{m}.json', 'r', encoding='utf-8') as f:
            d = json.load(f)
        print(f"=== Mock {m} Star Questions ===")
        for q in d['sections'][0]['items']:
            if q.get('typeId') == 'N2-GR-STAR':
                print(f"ID: {q['id']}")
                print(f"  Stem: {q['stem']}")
                opts = [f"{o['id']}: {o['text']}" for o in q['options']]
                print(f"  Options: {opts}")
                print(f"  Key: {q['correctAnswer']}")
                print(f"  Exp: {q.get('explanationVi', '')[:100]}...")

if __name__ == '__main__':
    main()
