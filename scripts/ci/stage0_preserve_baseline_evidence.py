# -*- coding: utf-8 -*-
"""
STAGE 0: Baseline Verification & Forensic Evidence Preservation
Records the immutable cryptographic state of Phuchello/JP-STUDY at audited baseline commit:
ccecb81e39f0ab6a87db3ba609eff010600da222
"""
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def execute_stage_0():
    print("=== EXECUTING STAGE 0: BASELINE VERIFICATION & EVIDENCE PRESERVATION ===")
    snapshot = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "baselineCommit": "ccecb81e39f0ab6a87db3ba609eff010600da222",
        "mockExams": {},
        "audioAssets": {},
        "historicalReviewFiles": {},
        "invalidatedM06Reviews": {},
        "m06BaselineAnswerKeys": {},
        "scriptsInspected": []
    }

    # 1. Inspect Mock Exams (1 to 6)
    exam_files = sorted(list((ROOT / "data/mock_exams").glob("n2_mock_*.json")))
    exam_files = [f for f in exam_files if not f.name.endswith('_manifest.json')]
    print(f"Found {len(exam_files)} mock exam files:")
    for ef in exam_files:
        mid = ef.stem.upper().replace('_', '-')
        data = json.loads(ef.read_text(encoding='utf-8'))
        sec1_cnt = len(data['sections'][0]['items'])
        sec2_cnt = len(data['sections'][1]['items'])
        file_sha = sha256_file(ef)
        snapshot["mockExams"][mid] = {
            "file": ef.name,
            "sha256": file_sha,
            "sec1Items": sec1_cnt,
            "sec2Items": sec2_cnt,
            "totalItems": sec1_cnt + sec2_cnt
        }
        print(f"  - {mid}: {sec1_cnt} + {sec2_cnt} = {sec1_cnt + sec2_cnt} items (SHA-256: {file_sha[:12]}...)")

    # 2. Inspect Audio Assets across all 6 exams
    audio_dirs = sorted(list((ROOT / "docs/audio").glob("n2_mock_*")))
    total_audio = 0
    for ad in audio_dirs:
        mp3s = sorted(list(ad.glob("*.mp3")))
        total_audio += len(mp3s)
        snapshot["audioAssets"][ad.name] = {
            "count": len(mp3s),
            "files": {m.name: sha256_file(m) for m in mp3s}
        }
        print(f"  - Audio dir {ad.name}: {len(mp3s)} tracks")
    snapshot["totalAudioTracks"] = total_audio
    print(f"Total verified audio tracks across 6 mocks: {total_audio}")

    # 3. Preserve and Hash N2 #06 review files
    m06_review_files = [
        "qa/blind_items_m06_s1_p1.json",
        "qa/blind_items_m06_s1_p2.json",
        "qa/blind_items_m06_s2.json",
        "qa/raw_blind_m06_s1_p1.json",
        "qa/raw_blind_m06_s1_p2.json",
        "qa/raw_blind_m06_s2.json"
    ]
    backup_dir = ROOT / "qa/historical_baseline/m06_pre_repair"
    backup_dir.mkdir(parents=True, exist_ok=True)

    for rf in m06_review_files:
        p = ROOT / rf
        if p.exists():
            f_sha = sha256_file(p)
            snapshot["historicalReviewFiles"][rf] = f_sha
            # Copy to backup directory
            dest = backup_dir / p.name
            shutil.copy2(p, dest)
            print(f"Preserved {rf} -> {dest} (SHA-256: {f_sha})")

    # 4. Extract and preserve N2-MOCK-06 baseline answer key & question versions
    m06_json = json.loads((ROOT / "data/mock_exams/n2_mock_06.json").read_text(encoding='utf-8'))
    m06_keys = {}
    for sec_idx, sec in enumerate(m06_json['sections']):
        for it in sec['items']:
            m06_keys[it['id']] = {
                "section": sec_idx + 1,
                "typeId": it.get('typeId'),
                "stem": it.get('stem'),
                "correctAnswer": it.get('correctAnswer'),
                "options": {o['id']: o['text'] for o in it.get('options', [])},
                "explanationVi": it.get('explanationVi')
            }
    snapshot["m06BaselineAnswerKeys"] = m06_keys
    (ROOT / "qa/historical_baseline/m06_baseline_answer_keys.json").write_text(
        json.dumps(m06_keys, ensure_ascii=False, indent=2), encoding='utf-8'
    )
    print(f"Preserved {len(m06_keys)} baseline answer keys for N2-MOCK-06")

    # 5. Record invalidated review files metadata
    for fn in ["raw_blind_m06_s1_p1.json", "raw_blind_m06_s1_p2.json", "raw_blind_m06_s2.json"]:
        p = ROOT / "qa" / fn
        if p.exists():
            items = json.loads(p.read_text(encoding='utf-8'))
            snapshot["invalidatedM06Reviews"][fn] = {
                "count": len(items),
                "sha256": sha256_file(p),
                "status": "INVALID_FOR_INDEPENDENT_AGREEMENT",
                "invalidationReason": "Review output contaminated with authored correctAnswer"
            }

    # 6. List scripts identified with review file operations
    scripts_to_review = [
        "scripts/curriculum/generate_m06_blind_reviews.py",
        "scripts/curriculum/apply_stage_a_qa_reconciliation.py",
        "scripts/curriculum/export_blind_dataset_m06.py",
        "scripts/curriculum/reconcile_mock_blind_review.py",
        "scripts/curriculum/audit_blind_remapping_integrity.py",
        ".github/workflows/content-qa.yml",
        "scripts/ci/generate_ci_qa_summary.py"
    ]
    snapshot["scriptsInspected"] = scripts_to_review

    # Write snapshot file
    out_snapshot = ROOT / "qa/STAGE_0_BASELINE_SNAPSHOT.json"
    out_snapshot.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Saved complete baseline snapshot to {out_snapshot}")
    print("=== STAGE 0 COMPLETE ===")

if __name__ == '__main__':
    execute_stage_0()
