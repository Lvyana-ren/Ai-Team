"""Xen-AI-Team integration checks for the vendored UI/UX Pro Max package."""

import json
import subprocess
import sys
import unittest
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = SKILL_DIR / "scripts"
SEARCH = SCRIPTS_DIR / "search.py"
SKILL_MD = SKILL_DIR / "SKILL.md"


class XenVendorLayoutTests(unittest.TestCase):
    def test_runtime_and_catalog_assets_are_present(self):
        required = (
            SEARCH,
            SCRIPTS_DIR / "core.py",
            SCRIPTS_DIR / "design_system.py",
            SCRIPTS_DIR / "reasoning_contract.py",
            SCRIPTS_DIR / "validate_data.py",
            SKILL_DIR / "data" / "styles.csv",
            SKILL_DIR / "data" / "ux-guidelines.csv",
            SKILL_DIR / "data" / "ui-reasoning.csv",
            SKILL_DIR / "data" / "stacks" / "jetpack-compose.csv",
            SKILL_DIR / "references" / "quick-reference.md",
            SKILL_DIR / "references" / "pro-rules.md",
            SKILL_DIR / "LICENSE.txt",
            SKILL_DIR / "UPSTREAM.md",
        )
        missing = [str(path.relative_to(SKILL_DIR)) for path in required if not path.is_file()]
        self.assertEqual([], missing, f"missing vendored assets: {missing}")

    def test_skill_uses_xen_repository_root_not_claude_plugin_root(self):
        content = SKILL_MD.read_text(encoding="utf-8")
        self.assertNotIn("CLAUDE_PLUGIN_ROOT", content)
        self.assertIn("$XEN_AI_TEAM_ROOT/agents/designer/skills/upstream/ui-ux-pro-max/scripts/search.py", content)

    def test_style_search_runs_from_vendored_path(self):
        result = subprocess.run(
            [sys.executable, str(SEARCH), "dark dashboard", "--domain", "style", "--json"],
            cwd=SKILL_DIR.parents[4],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        payload = json.loads(result.stdout)
        self.assertGreater(payload.get("count", 0), 0, result.stdout)

    def test_jetpack_compose_stack_search_runs(self):
        result = subprocess.run(
            [sys.executable, str(SEARCH), "compose state", "--stack", "jetpack-compose", "--json"],
            cwd=SKILL_DIR.parents[4],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(payload.get("results"), result.stdout)


if __name__ == "__main__":
    unittest.main()
