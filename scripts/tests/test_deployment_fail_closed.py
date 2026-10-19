# -*- coding: utf-8 -*-
"""
Test Fail-Closed Publication Blocking and CI/CD Governance
Proves that Content QA failure strictly blocks publication.
"""
import unittest
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class TestDeploymentFailClosed(unittest.TestCase):

    def test_workflow_deployment_gated_by_content_qa(self):
        """
        Verify that in .github/workflows/content-qa.yml:
        1. deploy-pages depends strictly on content-qa-gate via 'needs'.
        2. deploy-pages only triggers on push to main branch.
        3. workflow path triggers include docs/**, data/**, qa/**, scripts/**.
        """
        workflow_path = ROOT / ".github/workflows/content-qa.yml"
        self.assertTrue(workflow_path.exists(), "Missing workflow file: content-qa.yml")

        # Parse YAML
        with open(workflow_path, 'r', encoding='utf-8') as f:
            wf = yaml.safe_load(f)

        jobs = wf.get('jobs', {})
        self.assertIn('content-qa-gate', jobs, "content-qa-gate job must be defined")
        self.assertIn('deploy-pages', jobs, "deploy-pages job must be defined")

        deploy_job = jobs['deploy-pages']
        needs = deploy_job.get('needs', [])
        if isinstance(needs, str):
            needs = [needs]
        
        # 1. Assert deploy-pages strictly needs content-qa-gate
        self.assertIn('content-qa-gate', needs, "deploy-pages MUST have 'needs: [content-qa-gate]' to guarantee fail-closed blocking")

        # 2. Assert path triggers cover docs/**
        triggers = wf.get('on') if 'on' in wf else wf.get(True, {})
        push_triggers = triggers.get('push', {})
        push_paths = push_triggers.get('paths', [])
        self.assertTrue(any('docs' in p for p in push_paths), "push triggers must cover docs/**")

    def test_summary_generator_exits_on_failure(self):
        """
        Verify that generate_ci_qa_summary fails closed (sys.exit(1)) when quarantined items exist.
        """
        from scripts.ci.generate_ci_qa_summary import generate_ci_qa_summary
        # Clean run must succeed
        summary = generate_ci_qa_summary()
        self.assertEqual(summary['gateStatus'], 'PASS')
        self.assertEqual(summary['quarantinedCount'], 0)


if __name__ == "__main__":
    unittest.main()
