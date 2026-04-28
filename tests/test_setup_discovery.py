import os
import unittest
from pathlib import Path
import shutil
import sys

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from Antigravity.scripts.setup import ProjectDetector, FrameworkSetup

class TestSetupAutoDiscovery(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path("tests/temp_project")
        self.test_dir.mkdir(parents=True, exist_ok=True)
        self.Antigravity_dir = Path(__file__).parent.parent / "Antigravity"
        
    def tearDown(self):
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_detect_project_file(self):
        # Test finding PROJECT.md
        project_file = self.test_dir / "PROJECT.md"
        project_file.write_text("# My Awesome Project", encoding="utf-8")
        
        detector = ProjectDetector(self.test_dir)
        found = detector.detect_project_meta_file()
        self.assertEqual(found.name, "PROJECT.md")

    def test_detect_progetto_file(self):
        # Test finding PROGETTO.md
        project_file = self.test_dir / "PROGETTO.md"
        project_file.write_text("# Il Mio Progetto", encoding="utf-8")
        
        detector = ProjectDetector(self.test_dir)
        found = detector.detect_project_meta_file()
        self.assertEqual(found.name, "PROGETTO.md")

    def test_create_agent_md_from_project_file(self):
        project_file = self.test_dir / "PROJECT.md"
        project_content = "# My Awesome Project\n\nStack: Python, React"
        project_file.write_text(project_content, encoding="utf-8")
        
        setup = FrameworkSetup(self.test_dir, Path(__file__).parent.parent / "Antigravity")
        # Simulate the new behavior
        setup.create_agent_md_from_meta(project_file)
        
        agent_md = self.test_dir / "AGENT.md"
        self.assertTrue(agent_md.exists())
        self.assertIn("My Awesome Project", agent_md.read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
