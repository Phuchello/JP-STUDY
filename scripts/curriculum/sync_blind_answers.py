# -*- coding: utf-8 -*-
"""
RETIRED & PERMANENTLY DISABLED LEGACY SCRIPT

This synchronization script previously attempted to sync raw blind reviews in place
by reading `target_item['correctAnswer']`. This caused review contamination and was
retired in Phase 3.5/3.6.

Option remapping is now strictly handled via the immutable derived remapping pipeline:
  scripts/curriculum/audit_blind_remapping_integrity.py
which maps option text purely by content equivalence, NEVER reading correctAnswer.
"""
import sys

def sync_blind_answers():
    raise RuntimeError(
        "CRITICAL: sync_blind_answers.py is permanently retired and disabled. "
        "Directly mutating raw blind answers using authored correct keys is prohibited. "
        "Use scripts/curriculum/audit_blind_remapping_integrity.py for decoupled derived remapping."
    )

if __name__ == '__main__':
    sync_blind_answers()
