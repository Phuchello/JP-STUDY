# -*- coding: utf-8 -*-
"""
JP-STUDY: Shared Dynamic Active Mock Discovery Module
Central source of truth for discovering, indexing, and validating all active JLPT mock exams.
Replaces all duplicated, hardcoded mock-number lists across the entire codebase.
"""
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any, Set
import json
import re

ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class MockExamInfo:
    exam_id: str          # e.g. "N2-MOCK-01"
    mock_num: str         # e.g. "01"
    path: Path            # Path to data/mock_exams/n2_mock_01.json
    manifest_path: Path   # Path to data/mock_exams/n2_mock_01_audio_manifest.json
    receipt_path: Path    # Path to qa/N2_MOCK_01_AUDIO_PLAYBACK_RECEIPT.json
    
    @property
    def raw_blind_review_paths(self) -> List[Path]:
        m = self.mock_num
        return [
            ROOT / f"qa/raw_blind_m{m}_s1_p1.json",
            ROOT / f"qa/raw_blind_m{m}_s1_p2.json",
            ROOT / f"qa/raw_blind_m{m}_s2.json"
        ]

    @property
    def sealed_blind_input_paths(self) -> List[Path]:
        m = self.mock_num
        return [
            ROOT / f"qa/blind_items_m{m}_s1_p1.json",
            ROOT / f"qa/blind_items_m{m}_s1_p2.json",
            ROOT / f"qa/blind_items_m{m}_s2.json"
        ]


def discover_active_n2_mocks(mock_exams_dir: Path = None) -> List[MockExamInfo]:
    """Dynamically discovers all active N2 mock exams in data/mock_exams/.
    
    Excludes manifests and temporary test fixtures.
    Sorts deterministically by mock number.
    """
    if mock_exams_dir is None:
        mock_exams_dir = ROOT / "data/mock_exams"
    
    if not mock_exams_dir.exists():
        return []
        
    pattern = re.compile(r"^n2_mock_(\d{2})\.json$")
    discovered = []
    
    for entry in mock_exams_dir.iterdir():
        if entry.is_file():
            match = pattern.match(entry.name)
            if match:
                num_str = match.group(1)
                exam_id = f"N2-MOCK-{num_str}"
                manifest_path = mock_exams_dir / f"n2_mock_{num_str}_audio_manifest.json"
                receipt_path = ROOT / f"qa/N2_MOCK_{num_str}_AUDIO_PLAYBACK_RECEIPT.json"
                discovered.append(MockExamInfo(
                    exam_id=exam_id,
                    mock_num=num_str,
                    path=entry,
                    manifest_path=manifest_path,
                    receipt_path=receipt_path
                ))
                
    return sorted(discovered, key=lambda m: m.mock_num)


def load_all_active_mock_questions(discovered_mocks: List[MockExamInfo] = None) -> List[Dict[str, Any]]:
    """Loads all question items across all discovered active mock exams."""
    if discovered_mocks is None:
        discovered_mocks = discover_active_n2_mocks()
        
    all_questions = []
    for m in discovered_mocks:
        data = json.loads(m.path.read_text(encoding='utf-8'))
        for s_idx, sec in enumerate(data.get('sections', []), 1):
            for q in sec.get('items', []):
                q_copy = dict(q)
                q_copy['examId'] = m.exam_id
                q_copy['sectionNum'] = s_idx
                all_questions.append(q_copy)
                
    return all_questions


def verify_downstream_id_consistency(
    discovered_mocks: List[MockExamInfo],
    review_records: List[Dict[str, Any]],
    ledger_records: List[Dict[str, Any]],
    catalog_path: Path = None
) -> Dict[str, Any]:
    """Verifies that discovered question IDs, review IDs, ledger IDs, and catalog IDs are 100% consistent.
    
    Does NOT merely check count; compares exact set equality.
    """
    if catalog_path is None:
        catalog_path = ROOT / "docs/widgets/jlpt_exam_catalog.html"
        
    discovered_qids: Set[str] = set()
    for m in discovered_mocks:
        data = json.loads(m.path.read_text(encoding='utf-8'))
        for sec in data.get('sections', []):
            for q in sec.get('items', []):
                discovered_qids.add(q['id'])
                
    review_qids: Set[str] = {r.get('questionId') or r.get('id') for r in review_records if r.get('questionId') or r.get('id')}
    ledger_qids: Set[str] = {r.get('questionId') or r.get('id') for r in ledger_records if r.get('questionId') or r.get('id')}
    
    # Extract advertised mock IDs from catalog HTML
    catalog_mock_ids: Set[str] = set()
    if catalog_path.exists():
        cat_text = catalog_path.read_text(encoding='utf-8')
        matches = re.findall(r'mockId=(N2-MOCK-\d{2})', cat_text)
        catalog_mock_ids = set(matches)
        
    discovered_mock_ids: Set[str] = {m.exam_id for m in discovered_mocks}
    
    missing_in_review = discovered_qids - review_qids
    missing_in_ledger = discovered_qids - ledger_qids
    missing_in_catalog = discovered_mock_ids - catalog_mock_ids
    
    is_consistent = (
        len(missing_in_review) == 0 and
        len(missing_in_ledger) == 0 and
        len(missing_in_catalog) == 0 and
        len(discovered_qids) == len(review_qids) == len(ledger_qids)
    )
    
    return {
        "isConsistent": is_consistent,
        "totalDiscoveredQuestions": len(discovered_qids),
        "totalReviewRecords": len(review_qids),
        "totalLedgerRecords": len(ledger_qids),
        "totalDiscoveredMocks": len(discovered_mock_ids),
        "totalCatalogMocks": len(catalog_mock_ids),
        "missingInReview": sorted(list(missing_in_review)),
        "missingInLedger": sorted(list(missing_in_ledger)),
        "missingInCatalog": sorted(list(missing_in_catalog))
    }
