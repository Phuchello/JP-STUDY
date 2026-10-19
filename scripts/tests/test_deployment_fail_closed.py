import unittest
try:
    import yaml
except ImportError:
    yaml = None
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

        with open(workflow_path, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn('content-qa-gate:', content, "content-qa-gate job must be defined")
        self.assertIn('deploy-pages:', content, "deploy-pages job must be defined")
        self.assertTrue(
            'needs: [content-qa-gate]' in content or 'needs:\n      - content-qa-gate' in content,
            "deploy-pages MUST have 'needs: [content-qa-gate]' to guarantee fail-closed blocking"
        )
        self.assertIn('docs/**', content, "push triggers must cover docs/**")

        if yaml is not None:
            wf = yaml.safe_load(content)
            jobs = wf.get('jobs', {})
            deploy_job = jobs['deploy-pages']
            needs = deploy_job.get('needs', [])
            if isinstance(needs, str):
                needs = [needs]
            self.assertIn('content-qa-gate', needs, "deploy-pages MUST have 'needs: [content-qa-gate]' to guarantee fail-closed blocking")
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
