# -*- coding: utf-8 -*-
"""
JP-STUDY: Dynamic Mock Exam Discovery & Release Audit Runner
Discovers every active N2 mock exam automatically:
  - Discovers all valid mock exam JSONs: data/mock_exams/n2_mock_[0-9][0-9].json
  - Excludes manifests, backups, and temporary fixtures
  - Enforces 105 questions (75 Sec 1 + 30 Sec 2), Mondai 4 3-choice rule,
    audio manifest & file integrity (100% SHA-256), playback receipts,
    and frontend catalog/bank registration.
Exits 0 on all pass, 1 on any failure.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.audit_n2_mock_105_questions import audit_mock_105
from scripts.curriculum.acoustic_assurance import evaluate_audio_track_assurance
from scripts.curriculum.discovery import discover_active_n2_mocks
from scripts.curriculum.mock_exam_release_checks import (
    CURRENT_VERSION_REVIEW_SCHEMA,
    validate_current_version_reconciliation,
    validate_full_mock_blueprint,
    validate_star_fragment_integrity,
    validate_version_bound_reconciliation,
)

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def discover_active_mocks(mock_exams_dir: Path = None):
    mocks = discover_active_n2_mocks(mock_exams_dir)
    return [(m.mock_num, m.path) for m in mocks]

def audit_single_discovered_mock(mock_num_str: str, exam_file: Path, catalog_html: str, bank_js: str):
    mid = f"N2-MOCK-{mock_num_str}"
    failures = []
    
    # 1. Parse JSON
    try:
        data = json.loads(exam_file.read_text(encoding='utf-8'))
    except Exception as e:
        return [f"{mid}: Failed to parse JSON: {e}"]

    # 2. Check exam ID
    if data.get('examId') != mid:
        failures.append(f"{mid}: Exam ID mismatch: expected '{mid}', got '{data.get('examId')}'")

    failures.extend(f"{mid}: {issue}" for issue in validate_full_mock_blueprint(data))

    # 3. Check Blueprint Completeness (75 + 30 = 105)
    sections = data.get('sections', [])
    if len(sections) < 2:
        failures.append(f"{mid}: Expected 2 sections, got {len(sections)}")
        return failures

    sec1_items = sections[0].get('items', [])
    sec2_items = sections[1].get('items', [])
    total_q = len(sec1_items) + len(sec2_items)

    if len(sec1_items) != 75:
        failures.append(f"{mid}: Section 1 has {len(sec1_items)} items (strictly 75 required)")
    if len(sec2_items) != 30:
        failures.append(f"{mid}: Section 2 has {len(sec2_items)} items (strictly 30 required)")

    # 4. Check Unique Question IDs
    all_qids = [q.get('id') for q in sec1_items + sec2_items]
    if len(set(all_qids)) != len(all_qids):
        duplicates = [qid for qid, count in __import__('collections').Counter(all_qids).items() if count > 1]
        failures.append(f"{mid}: Duplicate question IDs found: {duplicates}")

    # 5. Check Mondai 4 three-choice rule
    for it in sec2_items:
        qid = it.get('id', '')
        cat = str(it.get('category', ''))
        if 'M4' in qid or 'Mondai 4' in cat or '即時応答' in cat:
            opts = it.get('options', [])
            if len(opts) != 3:
                failures.append(f"{mid}: Mondai 4 question {qid} has {len(opts)} options (strictly 3 required)")

    # 5.5 Check Independent Review Evidence
    mock_info = next((m for m in discover_active_n2_mocks() if m.mock_num == mock_num_str), None)
    if mock_info:
        raw_p1, raw_p2, raw_s2 = mock_info.raw_blind_review_paths
    else:
        raw_p1 = ROOT / f"qa/raw_blind_m{mock_num_str}_s1_p1.json"
        raw_p2 = ROOT / f"qa/raw_blind_m{mock_num_str}_s1_p2.json"
        raw_s2 = ROOT / f"qa/raw_blind_m{mock_num_str}_s2.json"
    if raw_p1.exists() and raw_p2.exists() and raw_s2.exists():
        pass
    else:
        # Generic version-bound reconciliation contract for new review workflows.
        # This is evidence discovery by artifact shape, not a mock-number exemption.
        phase71_report = ROOT / f"qa/N2_MOCK_{mock_num_str}_PHASE71_CANDIDATE_RECONCILIATION.json"
        phase71_sealed = ROOT / f"qa/blind_items_m{int(mock_num_str)}_phase71_candidate.json"
        if data.get("releaseGateStatus") == "REVIEW_CONTENT_VERSION_VERIFIED" and phase71_report.is_file() and phase71_sealed.is_file():
            report_file, sealed_file = phase71_report, phase71_sealed
        else:
            report_file = ROOT / f"qa/N2_MOCK_{mock_num_str}_BLIND_RECONCILIATION.json"
            sealed_file = ROOT / f"qa/blind_items_m{int(mock_num_str)}_final.json"
        if report_file.is_file() and sealed_file.is_file():
            try:
                reconciliation = json.loads(report_file.read_text(encoding="utf-8"))
                sealed_input = json.loads(sealed_file.read_text(encoding="utf-8"))
                validator = (
                    validate_current_version_reconciliation
                    if reconciliation.get("schema") == CURRENT_VERSION_REVIEW_SCHEMA
                    else validate_version_bound_reconciliation
                )
                failures.extend(f"{mid}: {issue}" for issue in validator(reconciliation, data, sealed_input))
            except Exception as e:
                failures.append(f"{mid}: Version-bound reviewer reconciliation could not be validated: {e}")
        else:
            missing_revs = [p.name for p in [raw_p1, raw_p2, raw_s2] if not p.exists()]
            failures.append(f"{mid}: Missing independent review evidence and version-bound reconciliation: {', '.join(missing_revs)}")

    stars = [q for q in sec1_items if q.get("typeId") == "N2-GR-STAR"]
    if stars and all(q.get("starValidationSchema") == "DISPLAYED_FRAGMENT_ORDER_V1" for q in stars):
        failures.extend(f"{mid}: {issue}" for issue in validate_star_fragment_integrity(data))

    # 6. Check Audio Manifest and Real MP3 Files
    manifest_file = exam_file.parent / f"n2_mock_{mock_num_str}_audio_manifest.json"
    audio_dir = ROOT / f"docs/audio/n2_mock_{mock_num_str}"
    
    if not manifest_file.exists():
        failures.append(f"{mid}: Missing audio manifest {manifest_file.name}")
    else:
        manifest_raw = json.loads(manifest_file.read_text(encoding='utf-8'))
        if isinstance(manifest_raw, list):
            manifest = {it['id']: it for it in manifest_raw}
        else:
            manifest = manifest_raw

        if len(manifest) != 30:
            failures.append(f"{mid}: Audio manifest has {len(manifest)} entries (expected 30)")
        
        for qid, meta in manifest.items():
            rel_url = meta.get('audioUrl', '')
            mp3_path = ROOT / "docs" / rel_url if rel_url else (audio_dir / f"{qid}.mp3")
            if not mp3_path.exists():
                failures.append(f"{mid}: Missing audio file {mp3_path.name}")
            else:
                live_sha = sha256_file(mp3_path)
                expected_sha = meta.get('audioSha256')
                if live_sha != expected_sha:
                    failures.append(f"{mid}: Audio SHA-256 mismatch for {qid}: manifest={expected_sha[:8]}, live={live_sha[:8]}")

    # 7. Check Playback Receipt
    receipt_file = ROOT / f"qa/N2_MOCK_{mock_num_str}_AUDIO_PLAYBACK_RECEIPT.json"
    if not receipt_file.exists():
        failures.append(f"{mid}: Missing audio playback receipt {receipt_file.name}")
    else:
        receipt = json.loads(receipt_file.read_text(encoding='utf-8'))
        detailed_rows = receipt.get('results', [])
        tracks = {}
        if isinstance(detailed_rows, list) and detailed_rows:
            for row in detailed_rows:
                if not isinstance(row, dict):
                    continue
                qid = row.get('questionId') or row.get('id') or row.get('qid')
                if qid and qid not in tracks:
                    tracks[qid] = row
                elif qid:
                    failures.append(f"{mid}: Duplicate playback receipt row for {qid}")
        else:
            legacy_tracks = receipt.get('tracks', {})
            if isinstance(legacy_tracks, dict):
                for qid, row in legacy_tracks.items():
                    if isinstance(row, dict):
                        bound_row = dict(row)
                        bound_row.setdefault('questionId', qid)
                        tracks[qid] = bound_row
        if len(tracks) != 30:
            failures.append(f"{mid}: Audio playback receipt has {len(tracks)} tracks (expected 30)")

        manifest_tracks = {}
        if manifest_file.exists():
            manifest_raw = json.loads(manifest_file.read_text(encoding='utf-8'))
            if isinstance(manifest_raw, list):
                manifest_tracks = {
                    row.get('id') or row.get('qid') or row.get('questionId'): row
                    for row in manifest_raw if isinstance(row, dict)
                }
            elif isinstance(manifest_raw, dict):
                manifest_tracks = manifest_raw.get('tracks', manifest_raw)
        verified_count = 0
        for qid, row in tracks.items():
            meta = dict(manifest_tracks.get(qid, {}))
            meta.setdefault('questionId', qid)
            rel_url = meta.get('audioUrl', '')
            live_mp3 = ROOT / 'docs' / rel_url if rel_url else audio_dir / f"{qid}.mp3"
            assurance = evaluate_audio_track_assurance(meta, row, live_mp3)
            if assurance['BROWSER_PLAYBACK_VERIFIED']:
                verified_count += 1
        if verified_count != 30:
            failures.append(f"{mid}: Only {verified_count}/30 audio tracks have ID-bound hash, decode, and playback-progression evidence")

    # 8. Check Catalog and Mock Exam Bank
    if mid not in catalog_html:
        failures.append(f"{mid}: Not declared in docs/widgets/jlpt_exam_catalog.html")
    if f"'{mid}':" not in bank_js and f'"{mid}":' not in bank_js:
        failures.append(f"{mid}: Not registered in docs/widgets/mock_exam_bank.js JP_MOCK_DATA")

    # 9. Run audit_mock_105
    try:
        passed = audit_mock_105(int(mock_num_str))
        if not passed:
            failures.append(f"{mid}: audit_mock_105 failed release gate")
    except Exception as e:
        failures.append(f"{mid}: audit_mock_105 raised exception: {e}")

    return failures

def run_dynamic_mock_audit(exit_on_failure: bool = False):
    print("=== JP-STUDY: DYNAMIC ACTIVE MOCK DISCOVERY & RELEASE AUDIT ===")
    catalog_path = ROOT / "docs/widgets/jlpt_exam_catalog.html"
    bank_path = ROOT / "docs/widgets/mock_exam_bank.js"
    catalog_html = catalog_path.read_text(encoding='utf-8') if catalog_path.exists() else ""
    bank_js = bank_path.read_text(encoding='utf-8') if bank_path.exists() else ""

    discovered = discover_active_mocks()
    print(f"Discovered {len(discovered)} active N2 mock exams:")
    for num_str, f in discovered:
        print(f"  - N2-MOCK-{num_str}: {f.name}")

    if len(discovered) == 0:
        print("❌ CRITICAL: No active N2 mock exams discovered!")
        if exit_on_failure:
            sys.exit(1)
        return False, ["No active N2 mock exams discovered"]

    all_failures = {}
    for num_str, f in discovered:
        mid = f"N2-MOCK-{num_str}"
        print(f"\n--- Auditing {mid} ({f.name}) ---")
        failures = audit_single_discovered_mock(num_str, f, catalog_html, bank_js)
        if failures:
            all_failures[mid] = failures
            print(f"❌ {mid} FAILED with {len(failures)} issue(s):")
            for fl in failures:
                print(f"   * {fl}")
        else:
            print(f"✅ {mid} PASSED all release criteria.")

    print("\n==================================================")
    if all_failures:
        total_failed_mocks = len(all_failures)
        print(f"❌ DYNAMIC AUDIT FAILED: {total_failed_mocks}/{len(discovered)} mock(s) have release-blocking defects.")
        if exit_on_failure:
            sys.exit(1)
        return False, all_failures
    else:
        print(f"✅ DYNAMIC AUDIT PASSED: All {len(discovered)} active N2 mock exams satisfy release criteria.")
        if exit_on_failure:
            sys.exit(0)
        return True, {}

if __name__ == '__main__':
    run_dynamic_mock_audit(exit_on_failure=True)
