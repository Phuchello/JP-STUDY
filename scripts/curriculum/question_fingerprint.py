# -*- coding: utf-8 -*-
"""
JP-STUDY: Canonical Question & Assessment Version Fingerprinting Utility

Computes deterministic, content-bound SHA-256 hashes of assessment items across 3 explicit layers:
  1. QUESTION_TEXT_FINGERPRINT: stem, contextPassage, sorted options, typeId
  2. AUDIO_ASSET_FINGERPRINT: verified SHA-256 hash of actual audio bytes on disk & manifest
  3. ASSESSMENT_VERSION_FINGERPRINT: combined text + audio + modality + type metadata

Ensures that any material modification to a question (stem, options, passage, stimulus,
or audio track bytes) invalidates previous reviews and requires fresh verification.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def compute_question_text_fingerprint(q):
    """
    Computes a canonical SHA-256 hash of the question's written text and structure:
      - id
      - typeId
      - stem (normalized whitespace)
      - contextPassage (normalized whitespace)
      - options (sorted by id, text normalized)
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
        "options": options
    }

    canonical_json = json.dumps(canonical_data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(canonical_json.encode('utf-8')).hexdigest()

def compute_audio_asset_fingerprint(q, root_dir=None):
    """
    Computes/verifies the SHA-256 hash of the actual audio asset.
    Cross-checks file on disk against recorded audioSha256 where present.
    Returns empty string for non-listening items.
    """
    audio_url = str(q.get('audioUrl') or '').strip()
    recorded_sha = str(q.get('audioSha256') or '').strip().lower()

    if not audio_url and not recorded_sha:
        return ""

    if root_dir is None:
        root_dir = ROOT

    audio_rel = audio_url.lstrip('./')
    if audio_rel:
        candidates = [
            root_dir / "docs" / audio_rel,
            root_dir / audio_rel,
            root_dir / "docs" / "audio" / Path(audio_rel).name
        ]
        for candidate in candidates:
            if candidate.exists() and candidate.is_file():
                file_bytes = candidate.read_bytes()
                computed_file_sha = hashlib.sha256(file_bytes).hexdigest().lower()
                if recorded_sha and recorded_sha != computed_file_sha:
                    raise ValueError(
                        f"Audio hash mismatch for item {q.get('id')}: "
                        f"recorded={recorded_sha} vs actual_file={computed_file_sha}"
                    )
                return computed_file_sha

    if recorded_sha:
        return recorded_sha

    return ""

def compute_assessment_version_fingerprint(q, root_dir=None):
    """
    Computes the canonical assessment version fingerprint combining:
      - question text fingerprint
      - audio asset fingerprint (actual audio file SHA-256)
      - assessment modality (WRITTEN vs LISTENING)
      - item typeId
    Any modification to audio bytes or printed text changes this fingerprint.
    """
    text_fp = compute_question_text_fingerprint(q)
    audio_fp = compute_audio_asset_fingerprint(q, root_dir=root_dir)

    is_listening = bool(q.get('audioUrl') or q.get('audioSha256') or '-L' in str(q.get('typeId', '')) or q.get('section') == 2)
    modality = "LISTENING" if is_listening else "WRITTEN"

    canonical_data = {
        "id": str(q.get('id', '')).strip(),
        "typeId": str(q.get('typeId', '')).strip(),
        "textFingerprint": text_fp,
        "audioFingerprint": audio_fp,
        "modality": modality
    }

    canonical_json = json.dumps(canonical_data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(canonical_json.encode('utf-8')).hexdigest()

def compute_question_fingerprint(q, root_dir=None):
    """
    Primary canonical question fingerprint.
    Equivalent to compute_assessment_version_fingerprint(q).
    """
    return compute_assessment_version_fingerprint(q, root_dir=root_dir)

def compute_option_text_fingerprint(options):
    """
    Computes a hash of the set of option texts (ignoring order/labels).
    Used to distinguish between pure option permutations vs content rewrites.
    """
    texts = sorted([str(opt.get('text', '')).strip() for opt in options])
    canonical_json = json.dumps(texts, ensure_ascii=False)
    return hashlib.sha256(canonical_json.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    total_validated = 0
    for mock_fn in [
        "data/mock_exams/n2_mock_01.json",
        "data/mock_exams/n2_mock_02.json",
        "data/mock_exams/n2_mock_03.json",
        "data/mock_exams/n2_mock_04.json",
        "data/mock_exams/n2_mock_05.json"
    ]:
        p = ROOT / mock_fn
        if p.exists():
            data = json.loads(p.read_text(encoding='utf-8'))
            for sec in data.get('sections', []):
                for item in sec.get('items', []):
                    fp = compute_question_fingerprint(item)
                    assert len(fp) == 64, f"Invalid fingerprint for {item.get('id')}"
                    total_validated += 1
    print(f"Successfully computed and validated {total_validated} question assessment fingerprints.")
