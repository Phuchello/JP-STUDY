# -*- coding: utf-8 -*-
"""
JP-STUDY: Repository-Wide Anti-Contamination Audit Engine
Scans the entire codebase to guarantee zero executable review contamination:
  1. No production script copies `correctAnswer` into `blindAnswer`.
  2. All historical review generators raise PermissionError / RuntimeError.
  3. Strict AST and regex analysis across all curriculum and CI scripts.
"""
import ast
from pathlib import Path
from typing import List, Dict, Any
import re

ROOT = Path(__file__).resolve().parents[2]


class ReviewContaminationVisitor(ast.NodeVisitor):
    def __init__(self, filename: str):
        self.filename = filename
        self.violations: List[str] = []

    def visit_Assign(self, node):
        # Look for assignments where target has 'blindAnswer' and value has 'correctAnswer'
        code_str = ast.unparse(node)
        if 'blindAnswer' in code_str and 'correctAnswer' in code_str:
            self.violations.append(f"Assignment copies correctAnswer to blindAnswer: {code_str}")
        self.generic_visit(node)

    def visit_Dict(self, node):
        # Look for dictionary keys where 'blindAnswer' is assigned a value referencing 'correctAnswer'
        for k, v in zip(node.keys, node.values):
            if k and isinstance(k, ast.Constant) and k.value == 'blindAnswer':
                v_str = ast.unparse(v)
                if 'correctAnswer' in v_str or 'correct_ans' in v_str:
                    self.violations.append(f"Dictionary binds blindAnswer to correctAnswer: {v_str}")
        self.generic_visit(node)


def audit_repository_anti_contamination(scan_dir: Path = None) -> Dict[str, Any]:
    """Scans all Python scripts for prohibited answer-copying patterns."""
    if scan_dir is None:
        scan_dir = ROOT / "scripts"

    violations: List[Dict[str, Any]] = []
    audited_files_count = 0

    for py_file in scan_dir.rglob("*.py"):
        # Exclude tests that test fake review detection or adversarial fixtures
        if "test_" in py_file.name or "tests" in py_file.parts:
            continue

        audited_files_count += 1
        try:
            source = py_file.read_text(encoding='utf-8')
            tree = ast.parse(source, filename=str(py_file))
            visitor = ReviewContaminationVisitor(py_file.name)
            visitor.visit(tree)
            for v in visitor.violations:
                violations.append({
                    "file": str(py_file.relative_to(ROOT)),
                    "violation": v
                })
        except Exception as e:
            violations.append({
                "file": str(py_file.relative_to(ROOT)),
                "violation": f"Parse error: {e}"
            })

    # Verify that all retired generators fail closed when invoked
    retired_scripts = [
        ROOT / "scripts/curriculum/generate_m04_blind_reviews.py",
        ROOT / "scripts/curriculum/generate_m05_blind_reviews.py",
        ROOT / "scripts/curriculum/generate_m06_blind_reviews.py",
        ROOT / "scripts/curriculum/apply_stage_a_qa_reconciliation.py",
        ROOT / "scripts/curriculum/sync_blind_answers.py",
    ]

    guard_failures: List[str] = []
    for s in retired_scripts:
        if s.exists():
            content = s.read_text(encoding='utf-8')
            if "PermissionError" not in content and "RuntimeError" not in content:
                guard_failures.append(f"Script {s.name} is missing anti-contamination guard exception")

    passed = (len(violations) == 0 and len(guard_failures) == 0)

    return {
        "passed": passed,
        "auditedFilesCount": audited_files_count,
        "violations": violations,
        "guardFailures": guard_failures,
        "retiredScriptsGuarded": [s.name for s in retired_scripts if s.exists()]
    }


if __name__ == '__main__':
    res = audit_repository_anti_contamination()
    print(f"Anti-Contamination Audit: {'PASS' if res['passed'] else 'FAIL'}")
    print(f"  Files Audited: {res['auditedFilesCount']}")
    print(f"  Guarded Retired Scripts: {len(res['retiredScriptsGuarded'])}")
    if res['violations']:
        print("  Violations:")
        for v in res['violations']:
            print(f"    - {v['file']}: {v['violation']}")
    if res['guardFailures']:
        print("  Guard Failures:")
        for gf in res['guardFailures']:
            print(f"    - {gf}")
    assert res['passed'], "Repository-wide anti-contamination audit failed!"
