# -*- coding: utf-8 -*-
"""
ANTI-CONTAMINATION GUARD:
generate_m05_blind_reviews.py is permanently disabled and retired.
Direct generation of blind reviews from authored answer keys was identified
as a critical integrity defect (Phase 5.2).

Use scripts/curriculum/blind_review_exporter.py to export sealed candidate items
without answer keys or explanations, and evaluate them independently.
"""

def generate_reviews():
    raise PermissionError(
        "Direct generation of blind reviews from authored answer keys is strictly prohibited "
        "by the blind-review integrity policy. Use scripts/curriculum/blind_review_exporter.py "
        "to export sealed candidate items without answer keys or explanations."
    )

if __name__ == '__main__':
    generate_reviews()
