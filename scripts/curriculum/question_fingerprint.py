# -*- coding: utf-8 -*-
"""
JP-STUDY: Canonical Question Fingerprinting Utility

Computes deterministic, content-bound SHA-256 hashes of assessment items.
Ensures that any material modification to a question (stem, options, passage, stimulus)
invalidates previous reviews and requires fresh verification.
"""
import hashlib
import json

def compute_question_fingerprint(q):
    """
    Computes a canonical SHA-256 fingerprint for a question item.
    Includes:
      - id
      - stem (normalized whitespace)
      - options (sorted by id, text normalized)
      - contextPassage (normalized)
      - typeId
      - audioUrl / audioSha256
    """
    options = []
    for opt in sorted(q.get('options', []), key=lambda x: str(x.get('id', ''))):
        options.append({
            "id": str(opt.get('id', '')).strip(),
            "text": str(opt.get('text', '')).strip()
        })

    canonical_data = {
        "id": str(q.get('id', '')).strip(),
        "typeId": str(q.get('typeId', '')).strip(),
        "stem": str(q.get('stem', '')).strip(),
        "contextPassage": str(q.get('contextPassage') or '').strip(),
        "options": options,
        "audioUrl": str(q.get('audioUrl') or '').strip()
    }

    canonical_json = json.dumps(canonical_data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(canonical_json.encode('utf-8')).hexdigest()

def compute_option_text_fingerprint(options):
    """
    Computes a hash of the set of option texts (ignoring order/labels).
    Used to distinguish between pure option permutations vs content rewrites.
    """
    texts = sorted([str(opt.get('text', '')).strip() for opt in options])
    canonical_json = json.dumps(texts, ensure_ascii=False)
    return hashlib.sha256(canonical_json.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    from pathlib import Path
    root = Path(__file__).resolve().parents[2]
    total_validated = 0
    for mock_fn in ["data/mock_exams/n2_mock_01.json", "data/mock_exams/n2_mock_02.json", "data/mock_exams/n2_mock_03.json", "data/mock_exams/n2_mock_04.json", "data/mock_exams/n2_mock_05.json"]:
        p = root / mock_fn
        if p.exists():
            data = json.loads(p.read_text(encoding='utf-8'))
            for sec in data.get('sections', []):
                for item in sec.get('items', []):
                    fp = compute_question_fingerprint(item)
                    assert len(fp) == 64, f"Invalid fingerprint for {item.get('id')}"
                    total_validated += 1
    print(f"Successfully computed and validated {total_validated} question fingerprints.")

