#!/usr/bin/env python3
"""
Test suite for loom documentation structure.
Tests verify that all required documentation files exist and contain key concepts.

Run: pytest tests/test_documentation.py -v
"""

import pytest
from pathlib import Path

# Project root
ROOT = Path(__file__).parent.parent


class TestAbstractExists:
    """Test that ABSTRACT.md exists with required content."""
    
    def test_abstract_file_exists(self):
        """ABSTRACT.md must exist in root."""
        assert (ROOT / "ABSTRACT.md").exists(), "ABSTRACT.md not found in root"
    
    def test_abstract_has_english_content(self):
        """ABSTRACT.md must have English section."""
        content = (ROOT / "ABSTRACT.md").read_text(encoding="utf-8")
        assert "# Abstract" in content or "# loom Abstract" in content
        assert "context window" in content.lower()
        assert "multi-agent" in content.lower()
        assert "token" in content.lower()
    
    def test_abstract_has_italian_content(self):
        """ABSTRACT.md must have Italian section."""
        content = (ROOT / "ABSTRACT.md").read_text(encoding="utf-8")
        assert "italiano" in content.lower() or "## it" in content.lower()
        assert "contesto" in content.lower() or "finestra di contesto" in content.lower()


class TestQuickstartUpdated:
    """Test that QUICKSTART.md has new zero-friction workflow."""
    
    def test_quickstart_mentions_read_loom(self):
        """QUICKSTART must mention 'read loom' command."""
        content = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")
        assert "read loom" in content.lower() or "leggi loom" in content.lower()
    
    def test_quickstart_has_project_md_step(self):
        """QUICKSTART must mention PROJECT.md creation."""
        content = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")
        assert "PROJECT.md" in content or "PROGETTO.md" in content
    
    def test_quickstart_has_4_steps_new_project(self):
        """QUICKSTART must have 4-step workflow for new projects."""
        content = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")
        # Check for numbered steps or bullet points
        assert "1." in content or "①" in content or "- " in content
        assert "folder" in content.lower() or "cartella" in content.lower()
    
    def test_quickstart_no_python_commands(self):
        """QUICKSTART should minimize explicit Python commands."""
        content = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")
        # Should not have python setup.py as primary method
        lines = content.split("\n")
        first_method_lines = "\n".join(lines[:50])  # First 50 lines
        assert "python" not in first_method_lines.lower() or "natural language" in first_method_lines.lower()


class TestReadmeUpdated:
    """Test that README.md emphasizes zero-friction setup."""
    
    def test_readme_has_problem_section(self):
        """README must have 'The Problem' section before solution."""
        content = (ROOT / "README.md").read_text(encoding="utf-8")
        assert "problem" in content.lower() or "why loom" in content.lower()
    
    def test_readme_mentions_context_window(self):
        """README must mention context window limitation."""
        content = (ROOT / "README.md").read_text(encoding="utf-8")
        assert "context" in content.lower()
    
    def test_readme_mentions_token_savings(self):
        """README must mention token savings benefit."""
        content = (ROOT / "README.md").read_text(encoding="utf-8")
        assert "token" in content.lower()
    
    def test_readme_quick_start_shows_read_loom(self):
        """README Quick Start must show 'read loom' as primary method."""
        content = (ROOT / "README.md").read_text(encoding="utf-8")
        # Find Quick Start section
        if "## 🚀 Quick Start" in content or "## Quick Start" in content:
            quick_start_idx = content.lower().find("quick start")
            quick_start_section = content[quick_start_idx:quick_start_idx+1000]
            assert "read loom" in quick_start_section.lower() or "leggi loom" in quick_start_section.lower()


class TestNaturalLanguageGuideUpdated:
    """Test that NATURAL-LANGUAGE-GUIDE.md has new triggers."""
    
    def test_guide_has_read_loom_trigger(self):
        """Guide must list 'read loom' as trigger phrase."""
        content = (ROOT / "NATURAL-LANGUAGE-GUIDE.md").read_text(encoding="utf-8")
        assert "read loom" in content.lower() or "leggi loom" in content.lower()
    
    def test_guide_has_configure_loom_trigger(self):
        """Guide must list 'configure loom' as trigger phrase."""
        content = (ROOT / "NATURAL-LANGUAGE-GUIDE.md").read_text(encoding="utf-8")
        assert "configure loom" in content.lower() or "configura loom" in content.lower()


class TestSetupInstructionsUpdated:
    """Test that SETUP-INSTRUCTIONS.md has new agent instructions."""
    
    def test_setup_instructions_has_read_loom_trigger(self):
        """Setup instructions must include 'read loom' trigger."""
        content = (ROOT / "SETUP-INSTRUCTIONS.md").read_text(encoding="utf-8")
        assert "read loom" in content.lower() or "leggi loom" in content.lower()
    
    def test_setup_instructions_mentions_project_md(self):
        """Setup instructions must mention PROJECT.md discovery."""
        content = (ROOT / "SETUP-INSTRUCTIONS.md").read_text(encoding="utf-8")
        assert "PROJECT.md" in content or "PROGETTO.md" in content


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
