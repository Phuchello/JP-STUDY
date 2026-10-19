# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
bank_path = ROOT / "docs/widgets/mock_exam_bank.js"
content = bank_path.read_text(encoding='utf-8')

m4_path = ROOT / "data/mock_exams/n2_mock_04.json"
m4_data = json.loads(m4_path.read_text(encoding='utf-8'))

start_token = "  'N2-MOCK-04': {"
end_token = "  'N2-MOCK-05': {"

start_idx = content.find(start_token)
end_idx = content.find(end_token)
assert start_idx != -1, "Could not find N2-MOCK-04 in bank.js"
assert end_idx != -1, "Could not find N2-MOCK-05 in bank.js"

new_m4_block = "  'N2-MOCK-04': " + json.dumps(m4_data, ensure_ascii=False, indent=2) + ",\n\n"
new_content = content[:start_idx] + new_m4_block + content[end_idx:]
bank_path.write_text(new_content, encoding='utf-8')
print("Successfully updated N2-MOCK-04 in docs/widgets/mock_exam_bank.js")
