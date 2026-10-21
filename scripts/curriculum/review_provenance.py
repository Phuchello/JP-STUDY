# -*- coding: utf-8 -*-
"""
JP-STUDY: Review Provenance & Execution Integrity Engine (Phase 6 Hotfix)
Evaluates and enforces cryptographic, operational, and linguistic review provenance.

Eliminates all shortcuts based on examId, questionId, self-declared flags, or content fingerprints alone.
Requires positive, verifiable evidence lookup keyed by exact sealed input and execution attestation.

Explicit Provenance Classifications:
  - INDEPENDENT_REVIEW_ATTESTED: Traceable, isolated execution record verified against sealed input.
  - REVIEW_EXECUTION_REPORTED_NOT_ATTESTED: Execution reference reported, but host log unverified in current runner.
  - REVIEW_CONTENT_VERSION_VERIFIED: Review matches current content version, but execution isolation unproven.
  - REVIEW_PROVENANCE_PENDING: Historical review exists, but execution provenance is pending fresh panel.
  - REVIEW_CONTAMINATED: Concrete evidence that review was derived from authored key.
  - STALE_REVIEW: Review exists for previous question version, but current content changed.
  - REVIEW_REQUIRED: Question lacks review evidence entirely.
  - REVIEW_TAMPERED: Review output was altered after cryptographic hash was recorded.
"""
import hashlib
import json
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple, Set

ROOT = Path(__file__).resolve().parents[2]

from scripts.curriculum.blind_review_exporter import FORBIDDEN_KEYS, validate_sealed_item_purity

def compute_object_hash(obj: Any) -> str:
    """Computes deterministic SHA-256 hash of a JSON-serializable object."""
    serialized = json.dumps(obj, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(serialized.encode('utf-8')).hexdigest()

def compute_file_sha256(file_path: Path) -> str:
    """Computes SHA-256 hash of a file on disk."""
    if not file_path.exists():
        return ""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

KNOWN_CONTAMINATED_MOCKS = {"N2-MOCK-04", "N2-MOCK-05"}

# Reported Sealed Review Batches
# These references identify the sealed input and reviewer response. They do not
# attest isolated execution; a local host log is not portable CI evidence.
REPORTED_REVIEW_BATCHES: Dict[str, Dict[str, Any]] = {
    "N2-MOCK-06_s1_p1": {
        "batchId": "batch-20261020-m06-p1",
        "sealedInputFile": "qa/blind_items_m06_s1_p1.json",
        "reviewOutputFile": "qa/raw_blind_m06_s1_p1.json",
        "conversationId": "1080af9c-3d6d-45eb-8357-7db7a47c9508",
        "itemCount": 38,
        "executionEvidence": "reported-not-attested"
    },
    "N2-MOCK-06_s1_p2": {
        "batchId": "batch-20261020-m06-p2",
        "sealedInputFile": "qa/blind_items_m06_s1_p2.json",
        "reviewOutputFile": "qa/raw_blind_m06_s1_p2.json",
        "conversationId": "df59f05f-d971-4a7c-bf7b-4079ad1e41ac",
        "itemCount": 37,
        "executionEvidence": "reported-not-attested"
    },
    "N2-MOCK-06_s2": {
        "batchId": "batch-20261020-m06-s2",
        "sealedInputFile": "qa/blind_items_m06_s2.json",
        "reviewOutputFile": "qa/raw_blind_m06_s2.json",
        "conversationId": "5f93c328-840c-4a5d-8ce2-a0449d53f057",
        "itemCount": 30,
        "executionEvidence": "reported-not-attested"
    },
    "REPAIRED_6": {
        "batchId": "batch-20261016-repaired-6",
        "sealedInputFile": "qa/blind_review_repaired_6.json",
        "reviewOutputFile": "qa/raw_blind_review_repaired_6.json",
        "conversationId": "cbfb8289-5e9d-4efa-84e7-d2710a0d4843",
        "itemCount": 6,
        "executionEvidence": "reported-not-attested"
    }
}


class ReviewProvenanceValidator:
    """Production validator for review evidence and positive provenance attestation."""

    @classmethod
    def register_review_batch(cls, batch_key: str, batch_meta: Dict[str, Any]):
        """Dynamically registers a reported review batch reference."""
        REPORTED_REVIEW_BATCHES[batch_key] = batch_meta

    @staticmethod
    def inspect_execution_host_log(conversation_id: str) -> Dict[str, Any]:
        """Inspects whether an isolated execution host log exists and is intact."""
        if not conversation_id:
            return {"exists": False, "sha256": None, "stepCount": 0}
        
        user_home = Path.home()
        log_path = user_home / f".gemini/antigravity/brain/{conversation_id}/.system_generated/logs/transcript.jsonl"
        if log_path.exists():
            sha = compute_file_sha256(log_path)
            try:
                with log_path.open(encoding="utf-8", errors="ignore") as f:
                    line_count = sum(1 for _ in f)
            except Exception:
                line_count = 0
            return {
                "exists": True,
                "logPath": str(log_path),
                "sha256": sha,
                "stepCount": line_count
            }
        return {"exists": False, "logPath": None, "sha256": None, "stepCount": 0}

    @classmethod
    def classify_review_provenance(
        cls,
        question_item: Dict[str, Any],
        review_record: Optional[Dict[str, Any]],
        current_fingerprint: str,
        execution_attestation: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Classifies the evidence status of a question review strictly based on positive evidence.
        
        Eliminates all shortcuts based on examId or self-declared labels.
        """
        qid = question_item.get('id', 'UNKNOWN')
        exam_id = question_item.get('examId', '')

        # 1. Missing review evidence entirely
        if review_record is None:
            return {
                "qid": qid,
                "status": "REVIEW_REQUIRED",
                "isCertified": False,
                "reason": "Missing review evidence in repository records."
            }

        # 2. Check content fingerprint match
        review_fp = review_record.get('contentFingerprint')
        if not review_fp or review_fp != current_fingerprint:
            return {
                "qid": qid,
                "status": "STALE_REVIEW",
                "isCertified": False,
                "reason": f"Content fingerprint mismatch: question={current_fingerprint[:8]}..., review={str(review_fp)[:8]}..."
            }

        # 3. Check for response hash tampering
        recorded_response_hash = review_record.get('responseHash')
        if recorded_response_hash:
            calculated_hash = compute_object_hash({
                "id": review_record.get('id'),
                "blindAnswer": review_record.get('blindAnswer'),
                "linguisticJustification": review_record.get('linguisticJustification')
            })
            if calculated_hash != recorded_response_hash:
                return {
                    "qid": qid,
                    "status": "REVIEW_TAMPERED",
                    "isCertified": False,
                    "reason": f"Review response hash mismatch: calculated {calculated_hash[:8]} vs recorded {recorded_response_hash[:8]}"
                }

        # 4. Check for contaminated generation origin
        # N2-MOCK-04 and N2-MOCK-05 have confirmed contaminated generation history
        if exam_id in KNOWN_CONTAMINATED_MOCKS and not review_record.get('isFreshIndependentSolve'):
            return {
                "qid": qid,
                "status": "REVIEW_CONTAMINATED",
                "isCertified": False,
                "reason": f"Question review belongs to {exam_id} whose review generator was confirmed contaminated with authored keys."
            }

        # 5. Look up positive batch execution evidence
        # An independent certification CANNOT be granted simply because of exam_id or self-declared strings
        matching_batch: Optional[Dict[str, Any]] = None
        
        # Check provided execution_attestation first
        if execution_attestation:
            cid = execution_attestation.get('conversationId')
            sealed_file = execution_attestation.get('sealedInputFile')
            if cid and sealed_file:
                matching_batch = execution_attestation

        # Otherwise look up in verified review batches registry
        if not matching_batch:
            for b_key, b_meta in REPORTED_REVIEW_BATCHES.items():
                sealed_path = ROOT / b_meta["sealedInputFile"]
                if sealed_path.exists():
                    try:
                        items = json.loads(sealed_path.read_text(encoding='utf-8'))
                        if any(it.get('id') == qid for it in items):
                            matching_batch = b_meta
                            break
                    except Exception:
                        pass

        if matching_batch:
            # Positive verification: verify sealed input file purity and existence
            sealed_path = ROOT / matching_batch["sealedInputFile"]
            if not sealed_path.exists():
                return {
                    "qid": qid,
                    "status": "REVIEW_PROVENANCE_PENDING",
                    "isCertified": False,
                    "reason": f"Attested sealed input file {matching_batch['sealedInputFile']} missing on disk."
                }
            
            # Verify purity: must NOT contain correctAnswer or explanations
            try:
                sealed_items = json.loads(sealed_path.read_text(encoding='utf-8'))
                target_sealed_item = next((it for it in sealed_items if it.get('id') == qid), None)
                if target_sealed_item:
                    validate_sealed_item_purity(target_sealed_item)
            except Exception as e:
                return {
                    "qid": qid,
                    "status": "REVIEW_CONTAMINATED",
                    "isCertified": False,
                    "reason": f"Sealed input purity violation: {e}"
                }

            # A host-local log is not portable evidence: a CI runner cannot
            # verify that user's machine state. Keep this at reported status
            # unless a future repository-verifiable attestation is implemented.
            cid = matching_batch.get("conversationId", "")
            return {
                "qid": qid,
                "status": "REVIEW_EXECUTION_REPORTED_NOT_ATTESTED",
                "isCertified": False,
                "reason": f"Execution reference {cid[:8]}... is reported, but no portable execution attestation is available."
            }

        # 6. Content version verified but execution unproven
        return {
            "qid": qid,
            "status": "REVIEW_CONTENT_VERSION_VERIFIED",
            "isCertified": False,
            "reason": "Matches current question content version, but isolated execution trace is unproven."
        }

    @staticmethod
    def reconcile_question(
        question_item: Dict[str, Any],
        review_record: Dict[str, Any],
        current_fingerprint: str,
        is_repaired_item: bool = False
    ) -> Dict[str, Any]:
        """Reconciles independent reviewer answer against authored key."""
        qid = question_item.get('id')
        authored_key = str(question_item.get('correctAnswer', '')).strip().upper()
        blind_answer = str(review_record.get('blindAnswer', '')).strip().upper()

        if not blind_answer:
            return {
                "qid": qid,
                "disposition": "REVIEW_REQUIRED",
                "classification": "UNVERIFIED",
                "match": False,
                "gatePassed": False
            }

        # Verify fingerprint
        review_fp = review_record.get('contentFingerprint')
        if review_fp != current_fingerprint:
            return {
                "qid": qid,
                "disposition": "FINGERPRINT_MISMATCH",
                "classification": "STALE_REVIEW",
                "match": False,
                "gatePassed": False
            }

        if blind_answer == authored_key:
            if is_repaired_item:
                return {
                    "qid": qid,
                    "disposition": "REPAIRED_AND_VERIFIED",
                    "classification": "GRAMMATICAL_DEFECT_RESOLVED",
                    "match": True,
                    "gatePassed": True
                }
            return {
                "qid": qid,
                "disposition": "AI_SEMANTIC_VERIFIED",
                "classification": "AGREEMENT",
                "match": True,
                "gatePassed": True
            }
        else:
            return {
                "qid": qid,
                "disposition": "KEY_MISMATCH_QUARANTINED",
                "classification": "KEY_MISMATCH",
                "match": False,
                "gatePassed": False,
                "details": f"Authored key '{authored_key}' conflicts with reviewer choice '{blind_answer}'"
            }
