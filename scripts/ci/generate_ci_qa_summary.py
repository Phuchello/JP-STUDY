# -*- coding: utf-8 -*-
"""
JP-STUDY: Machine-Readable CI/CD Content QA Summary Generator
Derives honest, comprehensive QA metrics from actual source ledgers,
audit reports, acoustic receipts, and provenance metadata across all active mock exams.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path(__file__).resolve().parents[2]

def generate_ci_qa_summary():
    ledger_file = ROOT / 'qa/QUESTION_AUDIT_LEDGER.json'
    if not ledger_file.exists():
        ledger_file = ROOT / 'qa/QUESTION_AUDIT_LEDGER_210.json'
    
    if not ledger_file.exists():
        raise FileNotFoundError(f"Missing question audit ledger: {ledger_file}")

    with open(ledger_file, 'r', encoding='utf-8') as f:
        ledger = json.load(f)

    total_items = len(ledger)
    quarantined = [it for it in ledger if it.get('finalDisposition') == 'QUARANTINED']
    review_required = [it for it in ledger if it.get('finalDisposition') == 'REVIEW_REQUIRED']
    re_review_required = [it for it in ledger if it.get('finalDisposition') == 'RE_REVIEW_REQUIRED']

    # Exam breakdowns
    by_mock = defaultdict(lambda: {"total": 0, "verified": 0, "quarantined": 0})
    for it in ledger:
        m = it.get('examId', 'UNKNOWN')
        by_mock[m]["total"] += 1
        disp = it.get('finalDisposition', '')
        if disp in ['AI_SEMANTIC_VERIFIED', 'REPAIRED_AND_VERIFIED', 'PASS']:
            by_mock[m]["verified"] += 1
        elif disp == 'QUARANTINED':
            by_mock[m]["quarantined"] += 1

    # Check audit reports
    reports_status = {}
    mocks_list = ['01', '02', '03', '04']
    if (ROOT / 'data/mock_exams/n2_mock_05.json').exists():
        mocks_list.append('05')

    for m in mocks_list:
        rep = ROOT / f'qa/N2_MOCK_{m}_INDEPENDENT_AUDIT_REPORT.md'
        reports_status[f"n2Mock{m}Audited"] = rep.exists()

    # Provenance summary from BLIND_REVIEW_INTEGRITY_AUDIT.json
    integrity_file = ROOT / 'qa/BLIND_REVIEW_INTEGRITY_AUDIT.json'
    provenance_data = {}
    if integrity_file.exists():
        with open(integrity_file, 'r', encoding='utf-8') as f:
            integrity_report = json.load(f)
            provenance_data = integrity_report.get('provenanceBreakdown', {})

    # Audio verification receipts
    audio_receipts_status = {}
    for m in mocks_list:
        rec = ROOT / f'qa/N2_MOCK_{m}_AUDIO_PLAYBACK_RECEIPT.json'
        if rec.exists():
            with open(rec, 'r', encoding='utf-8') as f:
                r_data = json.load(f)
                tracks = r_data.get('tracks', {})
                all_verified = all(t.get('browserPlaybackVerified') for t in tracks.values()) if tracks else False
                audio_receipts_status[f"N2-MOCK-{m}"] = {
                    "receiptExists": True,
                    "tracksCount": len(tracks),
                    "allPlaybackVerified": all_verified
                }
        else:
            audio_receipts_status[f"N2-MOCK-{m}"] = {
                "receiptExists": False,
                "tracksCount": 0,
                "allPlaybackVerified": False
            }


    gate_status = "PASS" if (len(quarantined) == 0 and len(review_required) == 0 and len(re_review_required) == 0) else "FAIL"

    summary = {
        "workflow": "Content QA & Adversarial Release Gate",
        "ciRunTimestamp": datetime.now(timezone.utc).isoformat(),
        "totalItemsAudited": total_items,
        "quarantinedCount": len(quarantined),
        "reviewRequiredCount": len(review_required) + len(re_review_required),
        "gateStatus": gate_status,
        "auditReports": reports_status,
        "mockBreakdown": dict(by_mock),
        "provenanceBreakdown": provenance_data,
        "audioAcousticStatus": audio_receipts_status,
        "releaseCertification": "TECHNICALLY_READY · AI_AUDITED" if gate_status == "PASS" else "BLOCKED_QUARANTINED"
    }

    out_file = ROOT / 'qa/CI_QA_SUMMARY.json'
    out_file.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Generated comprehensive CI QA summary at {out_file}:")
    print(json.dumps(summary, indent=2, ensure_ascii=False))

    if gate_status != "PASS":
        print(f"ERROR: Release gate failed with {len(quarantined)} quarantined items and {len(review_required)} pending reviews!")
        sys.exit(1)

    return summary

if __name__ == '__main__':
    generate_ci_qa_summary()
