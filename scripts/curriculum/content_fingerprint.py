"""Canonical question-content fingerprinting and cryptographic review binding.
Provides deterministic, Unicode-normalized SHA-256 fingerprints across 4 distinct release dimensions:
  1. BLIND_INPUT_SHA256: fields visible to blind independent reviewers (backward-compatible with canonical_question_fingerprint)
  2. SCORING_SHA256: answer key and scoring-relevant option bindings
  3. PEDAGOGICAL_CONTENT_SHA256: Vietnamese explanations, distractor analyses, remediation, and STAR assembly
  4. FULL_ITEM_SHA256: canonical digest of all release-critical question fields
"""
import hashlib
import json
import unicodedata
from pathlib import Path


def _norm_str(s):
    if s is None:
        return None
    val = str(s).strip()
    return unicodedata.normalize('NFC', val) if val else None


def canonical_blind_input_fingerprint(q):
    """
    Computes canonical SHA-256 fingerprint for BLIND REVIEW INPUT.
    Contains ONLY fields visible to an independent reviewer (no answer keys or explanations):
    - id: Question ID (string)
    - level: JLPT level (N4, N3, N2)
    - typeId: Question sub-type
    - stem: Exact stem text, Unicode NFC normalized and trimmed
    - contextPassage: Reading context passage (or None), NFC normalized and trimmed
    - options: All choices sorted by ID, each with 'id' and 'text' (NFC normalized and trimmed)

    Serializes deterministically with sort_keys=True and compact separators (',', ':').
    """
    stem_norm = _norm_str(q.get('stem')) or ''
    passage_norm = _norm_str(q.get('contextPassage'))

    options_norm = []
    for opt in sorted(q.get('options', []), key=lambda x: str(x.get('id', ''))):
        options_norm.append({
            'id': str(opt.get('id', '')).strip(),
            'text': _norm_str(opt.get('text', '')) or ''
        })

    canonical_doc = {
        'id': str(q.get('id', '')).strip(),
        'level': str(q.get('level', '')).strip(),
        'typeId': str(q.get('typeId', '')).strip(),
        'stem': stem_norm,
        'contextPassage': passage_norm,
        'options': options_norm
    }

    payload = json.dumps(canonical_doc, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()


# Backward-compatible alias
canonical_question_fingerprint = canonical_blind_input_fingerprint


def canonical_scoring_fingerprint(q):
    """
    Computes canonical SHA-256 digest for SCORING & GRADING integrity.
    Includes question ID, level, typeId, correctAnswer, and option ID-to-text bindings.
    """
    options_norm = []
    for opt in sorted(q.get('options', []), key=lambda x: str(x.get('id', ''))):
        options_norm.append({
            'id': str(opt.get('id', '')).strip(),
            'text': _norm_str(opt.get('text', '')) or ''
        })

    scoring_doc = {
        'id': str(q.get('id', '')).strip(),
        'level': str(q.get('level', '')).strip(),
        'typeId': str(q.get('typeId', '')).strip(),
        'correctAnswer': str(q.get('correctAnswer', '')).strip().upper(),
        'options': options_norm
    }

    payload = json.dumps(scoring_doc, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()


def canonical_pedagogical_fingerprint(q):
    """
    Computes canonical SHA-256 digest for PEDAGOGICAL CONTENT.
    Includes explanationVi, distractorExplanations, remediation, and assembledSentence (for STAR questions).
    """
    dist_raw = q.get('distractorExplanations') or {}
    dist_norm = {
        _norm_str(k): _norm_str(v)
        for k, v in sorted(dist_raw.items())
        if k is not None
    }

    ped_doc = {
        'id': str(q.get('id', '')).strip(),
        'explanationVi': _norm_str(q.get('explanationVi')),
        'distractorExplanations': dist_norm,
        'remediation': _norm_str(q.get('remediation')),
        'assembledSentence': _norm_str(q.get('assembledSentence'))
    }

    payload = json.dumps(ped_doc, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()


def canonical_full_item_fingerprint(q):
    """
    Computes canonical SHA-256 digest of ALL release-critical question fields.
    Guarantees full educational item immutability (stems, options, answers, explanations, remediation).
    """
    stem_norm = _norm_str(q.get('stem')) or ''
    passage_norm = _norm_str(q.get('contextPassage'))

    options_norm = []
    for opt in sorted(q.get('options', []), key=lambda x: str(x.get('id', ''))):
        options_norm.append({
            'id': str(opt.get('id', '')).strip(),
            'text': _norm_str(opt.get('text', '')) or ''
        })

    dist_raw = q.get('distractorExplanations') or {}
    dist_norm = {
        _norm_str(k): _norm_str(v)
        for k, v in sorted(dist_raw.items())
        if k is not None
    }

    full_doc = {
        'id': str(q.get('id', '')).strip(),
        'level': str(q.get('level', '')).strip(),
        'skill': str(q.get('skill', '')).strip(),
        'typeId': str(q.get('typeId', '')).strip(),
        'stem': stem_norm,
        'contextPassage': passage_norm,
        'options': options_norm,
        'correctAnswer': str(q.get('correctAnswer', '')).strip().upper(),
        'assembledSentence': _norm_str(q.get('assembledSentence')),
        'explanationVi': _norm_str(q.get('explanationVi')),
        'distractorExplanations': dist_norm,
        'remediation': _norm_str(q.get('remediation'))
    }

    payload = json.dumps(full_doc, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()


def compute_all_question_fingerprints(q):
    """Returns a dict of all 4 cryptographic fingerprints for an item."""
    return {
        'blindInputSha256': canonical_blind_input_fingerprint(q),
        'scoringSha256': canonical_scoring_fingerprint(q),
        'pedagogicalSha256': canonical_pedagogical_fingerprint(q),
        'fullItemSha256': canonical_full_item_fingerprint(q)
    }


def compute_file_sha256(file_path):
    """Computes SHA-256 of file bytes with newline normalization for cross-platform Git checkout consistency."""
    path = Path(file_path)
    if not path.exists():
        return None
    data = path.read_bytes()
    # Normalize \r\n to \n to ensure Windows CRLF checkouts match Git object blobs
    data = data.replace(b'\r\n', b'\n')
    return hashlib.sha256(data).hexdigest()
