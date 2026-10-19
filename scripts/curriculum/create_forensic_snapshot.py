import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT_DIR = ROOT / "qa/forensic_snapshot_phase3_5"
SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
BLIND_DIR = SNAPSHOT_DIR / "raw_blind_reviews"
BLIND_DIR.mkdir(exist_ok=True)

def sha256_file(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

# 1. Archive raw blind reviews
blind_files = [
    "raw_blind_m01_s1_p1.json",
    "raw_blind_m01_s1_p2.json",
    "raw_blind_m01_s2.json",
    "raw_blind_m02_s1_p1.json",
    "raw_blind_m02_s1_p2.json",
    "raw_blind_m02_s2.json"
]

manifest = {
    "baselineCommit": "27c53aa2d32481e93ce8f0e128982fbc22b33ced",
    "timestamp": "2026-10-19T17:08:00+07:00",
    "files": {}
}

for bf in blind_files:
    src = ROOT / "qa" / bf
    dst = BLIND_DIR / bf
    shutil.copy2(src, dst)
    manifest["files"][bf] = {
        "sha256": sha256_file(src),
        "bytes": src.stat().st_size
    }

# Also archive recovered pre-sync originals
orig_p1 = ROOT / "qa/raw_blind_m02_s1_p1_ORIGINAL.json"
if orig_p1.exists():
    dst_orig_p1 = BLIND_DIR / "raw_blind_m02_s1_p1_PRE_SYNC_ORIGINAL.json"
    shutil.copy2(orig_p1, dst_orig_p1)
    manifest["files"]["raw_blind_m02_s1_p1_PRE_SYNC_ORIGINAL.json"] = {
        "sha256": sha256_file(orig_p1),
        "bytes": orig_p1.stat().st_size
    }

orig_p2 = ROOT / "qa/raw_blind_m02_s1_p2_ORIGINAL.json"
if orig_p2.exists():
    dst_orig_p2 = BLIND_DIR / "raw_blind_m02_s1_p2_PRE_SYNC_ORIGINAL.json"
    shutil.copy2(orig_p2, dst_orig_p2)
    manifest["files"]["raw_blind_m02_s1_p2_PRE_SYNC_ORIGINAL.json"] = {
        "sha256": sha256_file(orig_p2),
        "bytes": orig_p2.stat().st_size
    }

# 2. Record 210 current question IDs and stored answers
q_records = []
for m in ['01', '02']:
    p = ROOT / f"data/mock_exams/n2_mock_{m}.json"
    data = json.loads(p.read_text(encoding='utf-8'))
    for s_idx, sec in enumerate(data['sections'], 1):
        for q in sec['items']:
            q_records.append({
                "examId": f"N2-MOCK-{m}",
                "section": s_idx,
                "id": q['id'],
                "typeId": q.get('typeId'),
                "stem": q.get('stem'),
                "options": q.get('options'),
                "correctAnswer": q.get('correctAnswer'),
                "explanationVi": q.get('explanationVi')
            })

assert len(q_records) == 210, f"Expected 210 questions, got {len(q_records)}"
(SNAPSHOT_DIR / "baseline_questions_210.json").write_text(
    json.dumps(q_records, ensure_ascii=False, indent=2), encoding='utf-8'
)
manifest["files"]["baseline_questions_210.json"] = {
    "sha256": sha256_file(SNAPSHOT_DIR / "baseline_questions_210.json"),
    "bytes": (SNAPSHOT_DIR / "baseline_questions_210.json").stat().st_size,
    "questionCount": len(q_records)
}

# 3. Audio Assets Manifest (60 files)
audio_records = []
for m in ['01', '02']:
    audio_dir = ROOT / f"docs/audio/n2_mock_{m}"
    for f in sorted(audio_dir.glob("*.mp3")):
        audio_records.append({
            "exam": f"N2-MOCK-{m}",
            "filename": f.name,
            "bytes": f.stat().st_size,
            "sha256": sha256_file(f)
        })

assert len(audio_records) == 60, f"Expected 60 audio files, got {len(audio_records)}"
(SNAPSHOT_DIR / "audio_assets_manifest_60.json").write_text(
    json.dumps(audio_records, ensure_ascii=False, indent=2), encoding='utf-8'
)
manifest["files"]["audio_assets_manifest_60.json"] = {
    "sha256": sha256_file(SNAPSHOT_DIR / "audio_assets_manifest_60.json"),
    "bytes": (SNAPSHOT_DIR / "audio_assets_manifest_60.json").stat().st_size,
    "audioTrackCount": len(audio_records)
}

(SNAPSHOT_DIR / "baseline_evidence_manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8'
)

print("Forensic snapshot generated successfully at:", SNAPSHOT_DIR)
