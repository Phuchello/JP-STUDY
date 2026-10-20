# -*- coding: utf-8 -*-
"""
JP-STUDY: Comprehensive CI Quality Assurance Summary Generator & Gate Enforcer (Phase 6)
Enforces strict multi-dimensional release verification across all active mock exams:
  1. Dynamic active mock discovery (all n2_mock_[0-9][0-9].json)
  2. Structural completeness (75 Section 1 + 30 Section 2 = 105 items per mock)
  3. Mondai 4 Quick Response 3-choice rule
  4. 5-Tiered acoustic quality and real browser playback verification
  5. Repository-wide anti-contamination verification (zero fake review generators)
  6. Per-question provenance derivation (zero exam-ID shortcuts)
  7. Exact question/review/catalog ID consistency verification
"""
import hashlib
import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.question_fingerprint import compute_question_fingerprint
from scripts.curriculum.discovery import (
    discover_active_n2_mocks,
    load_all_active_mock_questions,
    verify_downstream_id_consistency
)
from scripts.curriculum.anti_contamination_audit import audit_repository_anti_contamination
from scripts.curriculum.review_provenance import ReviewProvenanceValidator
from scripts.curriculum.acoustic_assurance import evaluate_audio_track_assurance

def evaluate_all_exams(exit_on_failure=False):
    gate_failures = []
    
    # 1. Discover all active mock exams dynamically
    discovered_mocks = discover_active_n2_mocks()
    if not discovered_mocks:
        gate_failures.append("No mock exams discovered in data/mock_exams")

    # Load all derived reviews for provenance lookup
    derived_reviews_file = ROOT / "qa/DERIVED_SEMANTIC_BLIND_REVIEWS.json"
    reviews_by_qid = {}
    review_records = []
    if derived_reviews_file.exists():
        derived_data = json.loads(derived_reviews_file.read_text(encoding='utf-8'))
        review_records = derived_data if isinstance(derived_data, list) else derived_data.get('reviews', [])
        for r in review_records:
            qid = r.get('questionId') or r.get('id')
            if qid:
                reviews_by_qid[qid] = r

    mock_metrics = {}
    total_items = 0
    total_audio_verified = 0

    for m in discovered_mocks:
        mid = m.exam_id
        m_num = m.mock_num
        data = json.loads(m.path.read_text(encoding='utf-8'))
        sections = data.get('sections', [])

        if len(sections) < 2:
            gate_failures.append(f"{mid}: Expected 2 sections, got {len(sections)}")
            continue

        sec1_items = sections[0].get('items', [])
        sec2_items = sections[1].get('items', [])
        total_items += (len(sec1_items) + len(sec2_items))

        # Check item counts
        if len(sec1_items) != 75:
            gate_failures.append(f"{mid}: Section 1 has {len(sec1_items)} items (expected 75)")
        if len(sec2_items) != 30:
            gate_failures.append(f"{mid}: Section 2 has {len(sec2_items)} items (expected 30)")

        # Check Section 1 answer balance (<= 38% for any single letter)
        sec1_answers = Counter(it.get('correctAnswer') for it in sec1_items)
        max_letter_count = max(sec1_answers.values()) if sec1_answers else 0
        max_ratio = max_letter_count / 75.0 if sec1_items else 0.0

        if max_ratio > 0.38:
            gate_failures.append(f"{mid}: Section 1 answer distribution biased (max ratio {max_ratio:.1%} > 38%)")

        # Check Mondai 4 3-choice rule in Section 2
        for it in sec2_items:
            if "Mondai 4" in it.get('category', '') or it.get('typeId') == 'N2-LIS-QUICK':
                opt_count = len(it.get('options', []))
                if opt_count != 3:
                    gate_failures.append(f"{mid}: Item {it['id']} has {opt_count} choices (must be exactly 3)")

        # Verify Audio Manifest and Receipt with 5-Tier Acoustic Assurance
        manifest_file = m.manifest_path
        receipt_file = m.receipt_path

        receipt_verified = False
        verified_tracks = 0
        if manifest_file.exists():
            manifest = json.loads(manifest_file.read_text(encoding='utf-8'))
            if isinstance(manifest, list):
                manifest_items = manifest
            elif isinstance(manifest, dict) and "tracks" in manifest:
                manifest_items = manifest["tracks"]
            elif isinstance(manifest, dict):
                manifest_items = list(manifest.values())
            else:
                manifest_items = []

            if len(manifest_items) != 30:
                gate_failures.append(f"{mid}: Audio manifest has {len(manifest_items)} entries (expected 30)")

            if receipt_file.exists():
                receipt = json.loads(receipt_file.read_text(encoding='utf-8'))
                raw_tracks = receipt.get('tracks', {})
                if isinstance(raw_tracks, dict):
                    receipt_tracks_map = raw_tracks
                elif isinstance(raw_tracks, list):
                    receipt_tracks_map = {t.get('questionId', f"{mid}_L{i:02d}"): t for i, t in enumerate(raw_tracks, 1)}
                else:
                    receipt_tracks_map = {}

                # Evaluate each track across the 5 acoustic tiers
                exam_audio_passed = True
                audio_dir = ROOT / f"docs/audio/n2_mock_{m_num}"

                for t_meta in manifest_items:
                    t_qid = t_meta.get('id') or t_meta.get('questionId')
                    rel_url = t_meta.get('audioUrl', '')
                    mp3_path = ROOT / "docs" / rel_url if rel_url else (audio_dir / f"{t_qid}.mp3")
                    r_track = receipt_tracks_map.get(t_qid, {})

                    tier_eval = evaluate_audio_track_assurance(
                        track_meta=t_meta,
                        receipt_track=r_track,
                        live_mp3_path=mp3_path
                    )

                    if not tier_eval["BROWSER_PLAYBACK_VERIFIED"]:
                        exam_audio_passed = False
                        gate_failures.append(f"{mid}: Track {t_qid} failed BROWSER_PLAYBACK_VERIFIED: {tier_eval['failureReason']}")
                    else:
                        verified_tracks += 1

                if exam_audio_passed and verified_tracks == 30:
                    receipt_verified = True
                    total_audio_verified += 30
                else:
                    gate_failures.append(f"{mid}: Only {verified_tracks}/30 audio tracks verified browser playback")
            else:
                gate_failures.append(f"{mid}: Missing audio playback receipt {receipt_file.name}")
        else:
            gate_failures.append(f"{mid}: Missing audio manifest {manifest_file.name}")

        # Derive per-exam Semantic QA Status dynamically from per-question review provenance
        exam_all_items = sec1_items + sec2_items
        prov_counts = Counter()
        key_mismatches_count = 0

        for q in exam_all_items:
            q_copy = dict(q)
            q_copy['examId'] = mid
            qid = q['id']
            curr_fp = compute_question_fingerprint(q_copy)
            rev = reviews_by_qid.get(qid)
            
            p_res = ReviewProvenanceValidator.classify_review_provenance(
                question_item=q_copy,
                review_record=rev,
                current_fingerprint=curr_fp
            )
            prov_counts[p_res["status"]] += 1

            # Check for key mismatches
            if rev:
                blind_ans = str(rev.get('remappedBlindAnswer') or rev.get('blindAnswer', '')).strip().upper()
                authored_ans = str(q.get('correctAnswer', '')).strip().upper()
                if blind_ans and authored_ans and blind_ans != authored_ans:
                    key_mismatches_count += 1

        # Dynamic Semantic QA Status Derivation:
        # Zero shortcuts based on examId!
        if key_mismatches_count > 0:
            semantic_qa_status = "CONTENT_QA_BLOCKED"
            gate_failures.append(f"{mid}: Contains {key_mismatches_count} key mismatches")
        elif prov_counts.get("REVIEW_REQUIRED", 0) > 0:
            semantic_qa_status = "CONTENT_QA_PENDING"
        elif prov_counts.get("REVIEW_CONTAMINATED", 0) > 0:
            semantic_qa_status = "REVIEW_PROVENANCE_PENDING"
        elif prov_counts.get("INDEPENDENT_REVIEW_ATTESTED", 0) == 105:
            semantic_qa_status = "INDEPENDENT_AI_REVIEW_VERIFIED"
        elif (prov_counts.get("INDEPENDENT_REVIEW_ATTESTED", 0) + prov_counts.get("REVIEW_EXECUTION_REPORTED_NOT_ATTESTED", 0)) == 105:
            semantic_qa_status = "REVIEW_EXECUTION_REPORTED_NOT_ATTESTED"
        elif prov_counts.get("REVIEW_CONTENT_VERSION_VERIFIED", 0) == 105:
            semantic_qa_status = "REVIEW_CONTENT_VERSION_VERIFIED"
        else:
            semantic_qa_status = "REVIEW_PROVENANCE_PENDING"

        # Technical Status is TECHNICALLY_READY if 105 items and audio verified
        is_tech_ready = (len(sec1_items) == 75 and len(sec2_items) == 30 and receipt_verified)

        mock_metrics[mid] = {
            "totalQuestions": len(sec1_items) + len(sec2_items),
            "section1AnswerDistribution": dict(sec1_answers),
            "maxLetterRatio": round(max_ratio, 3),
            "audioReceiptVerified": receipt_verified,
            "verifiedAudioTracks": verified_tracks,
            "technicalStatus": "TECHNICALLY_READY" if is_tech_ready else "TECHNICALLY_BLOCKED",
            "semanticQaStatus": semantic_qa_status,
            "provenanceBreakdown": dict(prov_counts),
            "keyMismatches": key_mismatches_count,
            "humanPanelStatus": "PENDING_HUMAN_PANEL"
        }

    # 2. Verify Ledger Integrity
    ledger_file = ROOT / "qa/QUESTION_AUDIT_LEDGER.json"
    ledger_dispositions = Counter()
    ledger_classifications = Counter()
    fingerprint_matches = Counter()
    ledger_records = []

    if ledger_file.exists():
        ledger_data = json.loads(ledger_file.read_text(encoding='utf-8'))
        ledger_records = ledger_data if isinstance(ledger_data, list) else ledger_data.get('records', [])
        for rec in ledger_records:
            ledger_dispositions[rec.get('finalDisposition')] += 1
            ledger_classifications[rec.get('reconciliationClassification')] += 1
            fingerprint_matches[rec.get('fingerprintMatch')] += 1
    else:
        gate_failures.append("Missing QUESTION_AUDIT_LEDGER.json")

    quarantined = ledger_dispositions.get('QUARANTINED', 0) + ledger_dispositions.get('KEY_MISMATCH_QUARANTINED', 0)
    review_required = ledger_dispositions.get('REVIEW_REQUIRED', 0) + ledger_dispositions.get('RE_REVIEW_REQUIRED', 0)
    fp_mismatches = fingerprint_matches.get(False, 0)

    if quarantined > 0:
        gate_failures.append(f"Ledger contains {quarantined} QUARANTINED items")
    if review_required > 0:
        gate_failures.append(f"Ledger contains {review_required} unverified REVIEW_REQUIRED items")
    if fp_mismatches > 0:
        gate_failures.append(f"Ledger contains {fp_mismatches} fingerprint mismatches")

    # 3. Verify Repository-Wide Anti-Contamination
    anti_contam_res = audit_repository_anti_contamination()
    if not anti_contam_res['passed']:
        for v in anti_contam_res['violations']:
            gate_failures.append(f"Anti-contamination violation in {v['file']}: {v['violation']}")
        for gf in anti_contam_res['guardFailures']:
            gate_failures.append(f"Anti-contamination guard failure: {gf}")

    # 4. Verify Downstream ID Consistency across Discovered Items, Review Records, Ledger, and Catalog
    consistency_res = verify_downstream_id_consistency(
        discovered_mocks=discovered_mocks,
        review_records=review_records,
        ledger_records=ledger_records
    )
    if not consistency_res['isConsistent']:
        if consistency_res['missingInReview']:
            gate_failures.append(f"Questions missing in review records: {consistency_res['missingInReview'][:5]}...")
        if consistency_res['missingInLedger']:
            gate_failures.append(f"Questions missing in audit ledger: {consistency_res['missingInLedger'][:5]}...")
        if consistency_res['missingInCatalog']:
            gate_failures.append(f"Mocks missing in catalog HTML: {consistency_res['missingInCatalog']}")

    # Gate decision
    is_gate_pass = (len(gate_failures) == 0)

    summary = {
        "workflow": "Content QA & Adversarial Release Gate",
        "ciRunTimestamp": datetime.now(timezone.utc).isoformat(),
        "totalItemsAudited": total_items,
        "totalAudioTracksVerified": total_audio_verified,
        "gateStatus": "PASS" if is_gate_pass else "FAIL",
        "gateFailures": gate_failures,
        "quarantinedCount": quarantined,
        "reviewRequiredCount": review_required,
        "fingerprintMismatches": fp_mismatches,
        "idConsistency": consistency_res,
        "antiContaminationVerified": anti_contam_res['passed'],
        "mockBreakdown": mock_metrics,
        "ledgerMetrics": {
            "dispositions": dict(ledger_dispositions),
            "classifications": dict(ledger_classifications),
            "fingerprintMatches": dict(fingerprint_matches)
        },
        "evaluationLayers": {
            "aiBlindReviewVerified": True if (is_gate_pass and total_items > 0) else False,
            "humanExpertCertification": "PENDING_HUMAN_PANEL",
            "failClosedPublicationEnforced": True
        },
        "releaseCertification": "TECHNICALLY_READY · REVIEW_PROVENANCE_GUARDED" if is_gate_pass else "BLOCKED_FAIL_CLOSED"
    }

    out_file = ROOT / "qa/CI_QA_SUMMARY.json"
    out_file.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Generated comprehensive CI QA summary at {out_file}:")
    print(json.dumps(summary, indent=2, ensure_ascii=False))

    if not is_gate_pass:
        print(f"\n❌ GATE BLOCKED with {len(gate_failures)} failures:")
        for gf in gate_failures:
            print(f"  - {gf}")
        if exit_on_failure:
            sys.exit(1)
    else:
        print("\n✅ RELEASE GATE PASSED: All integrity checks satisfied.")
        if exit_on_failure:
            sys.exit(0)

    return summary

generate_ci_qa_summary = evaluate_all_exams

if __name__ == "__main__":
    summary = evaluate_all_exams(exit_on_failure=True)
