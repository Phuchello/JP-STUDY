"""Canonical question-content fingerprinting and cryptographic review binding.
Provides deterministic, Unicode-normalized SHA-256 content fingerprints for JLPT questions
and cryptographic binding between question bank content and independent blind review artifacts.
"""
import hashlib
import json
import unicodedata
from pathlib import Path


def canonical_question_fingerprint(q):
    """
    Computes a canonical cryptographic SHA-256 fingerprint for a question's content.
    Includes:
    - id: Question ID (string)
    - level: JLPT level (N4, N3, N2)
    - typeId: Question sub-type
    - stem: Exact stem text, Unicode NFC normalized and trimmed
    - contextPassage: Reading context passage (or None), NFC normalized and trimmed
    - options: All 4 choices sorted by ID, each with 'id' and 'text' (NFC normalized and trimmed)

    Serializes deterministically with sort_keys=True and compact separators (',', ':').
    """
    stem_norm = unicodedata.normalize('NFC', q['stem'].strip()) if q.get('stem') else ''
    
    passage_raw = q.get('contextPassage')
    if passage_raw and passage_raw.strip():
        passage_norm = unicodedata.normalize('NFC', passage_raw.strip())
    else:
        passage_norm = None

    options_norm = []
    for opt in sorted(q.get('options', []), key=lambda x: x['id']):
        options_norm.append({
            'id': opt['id'].strip(),
            'text': unicodedata.normalize('NFC', opt['text'].strip())
        })

    canonical_doc = {
        'id': q['id'].strip(),
        'level': q['level'].strip(),
        'typeId': q['typeId'].strip(),
        'stem': stem_norm,
        'contextPassage': passage_norm,
        'options': options_norm
    }

    payload = json.dumps(canonical_doc, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()


def compute_file_sha256(file_path):
    """Computes SHA-256 of file bytes."""
    path = Path(file_path)
    if not path.exists():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()
