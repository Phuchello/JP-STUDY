"""Build and validate the expanded 120-question JLPT bank across N4, N3, and N2.
Executes the comprehensive, audited 5-stage validation pipeline with balanced answer distribution,
genuine independent blind solving, and negative regression test verification.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.rebuild_and_repair_bank import run_full_rebuild_and_validation

if __name__ == '__main__':
    run_full_rebuild_and_validation()
