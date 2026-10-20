# -*- coding: utf-8 -*-
"""
ANTI-CONTAMINATION GUARD & RETIRED SCRIPT:
apply_stage_a_qa_reconciliation.py is permanently retired and protected.

Phase 5.2 Audit Finding:
Section 3 of this script previously attempted to re-assign `r['blindAnswer'] = new_key`
from authored question keys during the N2-MOCK-04 answer-key rebalancing.
Overwriting independent reviewer answers with authored correct answers violates
the core blind-review integrity policy.

Option remapping must strictly be derived by semantic option-text equivalence via:
  scripts/curriculum/audit_blind_remapping_integrity.py
which NEVER reads or substitutes `correctAnswer`.
"""

def apply_reconciliation():
    raise PermissionError(
        "CRITICAL CONTAMINATION GUARD: Direct modification of blind reviewer answers "
        "using authored correct answers is strictly prohibited by the Phase 5.2 integrity policy. "
        "Use scripts/curriculum/audit_blind_remapping_integrity.py for decoupled derived remapping."
    )

if __name__ == '__main__':
    apply_reconciliation()
