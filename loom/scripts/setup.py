#!/usr/bin/env python3
"""
setup.py - Interactive Setup Wizard for Loom Framework

This script automatically detects your project and sets up the framework:
- Detects programming languages and frameworks
- Detects IDEs in use
- Auto-discovers PROJECT.md or PROGETTO.md for context
- Creates all necessary files from templates
- Configures IDE-specific files
- Initializes task management system

Usage:
    python scripts/setup.py                    # Interactive mode
    python scripts/setup.py --auto             # Auto-detect everything
    python scripts/setup.py --project-name "MyProject" --ide windsurf,cursor
    python scripts/setup.py --from-project-file PROJECT.md
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set

# Handle encoding for Windows terminals
if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text: str):
    """Print colored header."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text.center(60)}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.END}\n")

def print_success(text: str):
    """Print success message."""
    try:
        print(f"{Colors.GREEN}✅ {text}{Colors.END}")
    except UnicodeEncodeError:
        print(f"{Colors.GREEN}[OK] {text}{Colors.END}")

def print_info(text: str):
    """Print info message."""
    try:
        print(f"{Colors.CYAN}ℹ️  {text}{Colors.END}")
    except UnicodeEncodeError:
        print(f"{Colors.CYAN}[INFO] {text}{Colors.END}")

def print_warning(text: str):
    """Print warning message."""
    try:
        print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")
    except UnicodeEncodeError:
        print(f"{Colors.YELLOW}[WARN] {text}{Colors.END}")

def print_error(text: str):
    """Print error message."""
    try:
        print(f"{Colors.RED}❌ {text}{Colors.END}")
    except UnicodeEncodeError:
        print(f"{Colors.RED}[ERR] {text}{Colors.END}")


class ProjectDetector:
    """Detects project characteristics."""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
    
    def detect_languages(self) -> Set[str]:
        """Detect programming languages used in project."""
        languages = set()
        
        # Check for common files
        if (self.project_root / "package.json").exists():
            languages.add("javascript")
        if (self.project_root / "requirements.txt").exists() or (self.project_root / "setup.py").exists():
            languages.add("python")
        if (self.project_root / "Cargo.toml").exists():
            languages.add("rust")
        if (self.project_root / "go.mod").exists():
            languages.add("go")
        if (self.project_root / "pom.xml").exists() or (self.project_root / "build.gradle").exists():
            languages.add("java")
        if (self.project_root / "Gemfile").exists():
            languages.add("ruby")
        
        # Scan for file extensions
        for ext_map in [
            (".py", "python"),
            (".js", "javascript"),
            (".ts", "typescript"),
            (".rs", "rust"),
            (".go", "go"),
            (".java", "java"),
            (".rb", "ruby"),
            (".php", "php"),
            (".cs", "csharp"),
        ]:
            ext, lang = ext_map
            if any(self.project_root.rglob(f"*{ext}")):
                languages.add(lang)
        
        return languages
    
    def detect_frameworks(self) -> Set[str]:
        """Detect frameworks used in project."""
        frameworks = set()
        
        # Check package.json
        package_json = self.project_root / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                    deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                    
                    if "react" in deps:
                        frameworks.add("react")
                    if "vue" in deps:
                        frameworks.add("vue")
                    if "@angular/core" in deps:
                        frameworks.add("angular")
                    if "next" in deps:
                        frameworks.add("nextjs")
                    if "express" in deps:
                        frameworks.add("express")
                    if "@nestjs/core" in deps:
                        frameworks.add("nestjs")
            except:
                pass
        
        # Check requirements.txt
        requirements = self.project_root / "requirements.txt"
        if requirements.exists():
            try:
                content = requirements.read_text().lower()
                if "fastapi" in content:
                    frameworks.add("fastapi")
                if "flask" in content:
                    frameworks.add("flask")
                if "django" in content:
                    frameworks.add("django")
            except:
                pass
        
        return frameworks
    
    def detect_ides(self) -> Set[str]:
        """Detect IDEs in use based on config files."""
        ides = set()
        
        if (self.project_root / ".idea").exists():
            ides.add("intellij")
        if (self.project_root / ".vscode").exists():
            ides.add("vscode")
        if (self.project_root / ".cursorrules").exists():
            ides.add("cursor")
        if (self.project_root / ".windsurfrules").exists():
            ides.add("windsurf")
        if (self.project_root / "CLAUDE.md").exists():
            ides.add("claude")
        if (self.project_root / "GEMINI.md").exists():
            ides.add("gemini")
        if (self.project_root / ".github" / "copilot-instructions.md").exists():
            ides.add("copilot")
        
        return ides
    
    def detect_existing_docs(self) -> Set[str]:
        """Detect existing documentation files."""
        docs = set()
        
        docs_dir = self.project_root / "docs"
        if docs_dir.exists():
            if (docs_dir / "TASKS.md").exists():
                docs.add("TASKS.md")
            if (docs_dir / "BACKLOG.md").exists():
                docs.add("BACKLOG.md")
            if (docs_dir / "STORY.md").exists():
                docs.add("STORY.md")
            if (docs_dir / "CHANGELOG.md").exists():
                docs.add("CHANGELOG.md")
            if (docs_dir / "HANDOFF.md").exists():
                docs.add("HANDOFF.md")
        
        return docs

    def detect_project_meta_file(self) -> Optional[Path]:
        """Search for PROJECT.md or PROGETTO.md in root."""
        for name in ["PROJECT.md", "PROGETTO.md"]:
            path = self.project_root / name
            if path.exists():
                return path
        return None


class FrameworkSetup:
    """Sets up the agentic framework."""
    
    def __init__(self, project_root: Path, framework_root: Path):
        self.project_root = project_root
        self.framework_root = framework_root
    
    def create_agent_md(self, project_name: str, languages: Set[str], frameworks: Set[str]):
        """Create AGENT.md from template."""
        template_path = self.framework_root / "framework" / "AGENT.md.template"
        target_path = self.project_root / "AGENT.md"
        
        if target_path.exists():
            print_warning(f"AGENT.md already exists, skipping")
            return
        
        # Read template
        if not template_path.exists():
             # Fallback if template missing
             content = f"# {project_name}\n\nStack: {', '.join(languages | frameworks)}\n"
        else:
             content = template_path.read_text(encoding="utf-8")
        
        # Replace placeholders
        content = content.replace("[NOME_PROGETTO]", project_name)
        content = content.replace("[STACK]", ", ".join(languages | frameworks))
        
        # Write file
        target_path.write_text(content, encoding="utf-8")
        print_success(f"Created AGENT.md")

    def create_agent_md_from_meta(self, meta_path: Path):
        """Create AGENT.md using a project meta-file as content."""
        target_path = self.project_root / "AGENT.md"
        
        if target_path.exists():
            print_warning(f"AGENT.md already exists, skipping")
            return
            
        content = meta_path.read_text(encoding="utf-8")
        target_path.write_text(content, encoding="utf-8")
        print_success(f"Created AGENT.md from {meta_path.name}")
    
    def setup_ide_config(self, ide: str):
        """Setup IDE-specific configuration."""
        ide_map = {
            "windsurf": (".windsurfrules", "ide-configs/windsurf/windsurfrules.template"),
            "claude": ("CLAUDE.md", "ide-configs/claude/CLAUDE.md.template"),
            "cursor": (".cursorrules", "ide-configs/cursor/cursorrules.template"),
            "gemini": ("GEMINI.md", "ide-configs/gemini/GEMINI.md.template"),
            "vscode": (".clinerules", "ide-configs/vscode/clinerules.template"),
            "copilot": (".github/copilot-instructions.md", "ide-configs/copilot/copilot-instructions.md.template"),
            "intellij": (".idea/agentic-framework.md", "ide-configs/intellij/agentic-framework.md.template"),
        }
        
        if ide not in ide_map:
            print_warning(f"Unknown IDE: {ide}")
            return
        
        target_file, template_file = ide_map[ide]
        target_path = self.project_root / target_file
        template_path = self.framework_root / template_file
        
        if not template_path.exists():
            print_warning(f"Template not found: {template_path}")
            return
        
        if target_path.exists():
            print_warning(f"{target_file} already exists, skipping")
            return
        
        # Create parent directory if needed
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy template
        shutil.copy2(template_path, target_path)
        print_success(f"Created {target_file}")
    
    def init_docs(self):
        """Initialize documentation files."""
        docs_dir = self.project_root / "docs"
        docs_dir.mkdir(exist_ok=True)
        
        templates = [
            "TASKS.md",
            "BACKLOG.md",
            "STORY.md",
            "CHANGELOG.md",
            "HANDOFF.md",
        ]
        
        for template_name in templates:
            target_path = docs_dir / template_name
            template_path = self.framework_root / "docs" / "templates" / template_name
            
            if target_path.exists():
                print_warning(f"docs/{template_name} already exists, skipping")
                continue
            
            if not template_path.exists():
                print_warning(f"Template not found: {template_path}")
                continue
            
            shutil.copy2(template_path, target_path)
            print_success(f"Created docs/{template_name}")


def interactive_setup():
    """Run interactive setup wizard."""
    print_header("Loom Framework Setup Wizard")
    
    # Detect project root
    project_root = Path.cwd()
    framework_root = Path(__file__).parent.parent
    
    print_info(f"Project root: {project_root}")
    print_info(f"Framework root: {framework_root}")
    
    # Detect project characteristics
    print_header("Detecting Project")
    detector = ProjectDetector(project_root)
    
    languages = detector.detect_languages()
    frameworks = detector.detect_frameworks()
    ides = detector.detect_ides()
    existing_docs = detector.detect_existing_docs()
    
    print_info(f"Languages detected: {', '.join(languages) if languages else 'None'}")
    print_info(f"Frameworks detected: {', '.join(frameworks) if frameworks else 'None'}")
    print_info(f"IDEs detected: {', '.join(ides) if ides else 'None'}")
    print_info(f"Existing docs: {', '.join(existing_docs) if existing_docs else 'None'}")
    
    # Ask for project name
    print_header("Project Configuration")
    project_name = input(f"{Colors.CYAN}Project name: {Colors.END}").strip()
    if not project_name:
        project_name = project_root.name
        print_info(f"Using directory name: {project_name}")
    
    # Ask for IDEs to configure
    print(f"\n{Colors.CYAN}Which IDEs do you want to configure?{Colors.END}")
    print("1. Windsurf")
    print("2. Claude Code")
    print("3. Cursor")
    print("4. Gemini CLI")
    print("5. VS Code (Cline)")
    print("6. GitHub Copilot")
    print("7. IntelliJ IDEA")
    print("8. All")
    
    ide_choice = input(f"{Colors.CYAN}Enter numbers (comma-separated, e.g., 1,3,7): {Colors.END}").strip()
    
    ide_map = {
        "1": "windsurf",
        "2": "claude",
        "3": "cursor",
        "4": "gemini",
        "5": "vscode",
        "6": "copilot",
        "7": "intellij",
        "8": "all",
    }
    
    selected_ides = set()
    if "8" in ide_choice:
        selected_ides = {"windsurf", "claude", "cursor", "gemini", "vscode", "copilot", "intellij"}
    else:
        for num in ide_choice.split(","):
            num = num.strip()
            if num in ide_map:
                selected_ides.add(ide_map[num])
    
    # Setup
    print_header("Setting Up Framework")
    setup = FrameworkSetup(project_root, framework_root)
    
    # Create AGENT.md
    setup.create_agent_md(project_name, languages, frameworks)
    
    # Setup IDE configs
    for ide in selected_ides:
        setup.setup_ide_config(ide)
    
    # Initialize docs
    setup.init_docs()
    
    # Success
    print_header("Setup Complete!")
    print_success("Loom Framework configured successfully!")
    print_info("\nNext steps:")
    print(f"  1. Review and customize {Colors.BOLD}AGENT.md{Colors.END}")
    print(f"  2. Start your first task: {Colors.BOLD}python scripts/task.py start TASK-001 'Setup complete'{Colors.END}")
    print(f"  3. Read {Colors.BOLD}QUICKSTART.md{Colors.END} for more info")


def auto_setup(project_name: Optional[str] = None, ides: Optional[List[str]] = None, project_file: Optional[str] = None):
    """Run automatic setup without interaction."""
    print_header("Loom Framework Auto Setup")
    
    # Detect project root
    project_root = Path.cwd()
    framework_root = Path(__file__).parent.parent
    
    # Detect project characteristics
    detector = ProjectDetector(project_root)
    languages = detector.detect_languages()
    frameworks = detector.detect_frameworks()
    detected_ides = detector.detect_ides()
    
    # Use detected or provided values
    if not project_name:
        project_name = project_root.name
    
    if not ides:
        ides = list(detected_ides) if detected_ides else ["windsurf", "cursor"]
    
    print_info(f"Project: {project_name}")
    print_info(f"Languages: {', '.join(languages)}")
    print_info(f"Frameworks: {', '.join(frameworks)}")
    print_info(f"IDEs: {', '.join(ides)}")
    
    # Setup
    setup = FrameworkSetup(project_root, framework_root)
    
    if project_file:
        setup.create_agent_md_from_meta(Path(project_file))
    else:
        meta_file = detector.detect_project_meta_file()
        if meta_file:
            setup.create_agent_md_from_meta(meta_file)
        else:
            setup.create_agent_md(project_name, languages, frameworks)
    
    for ide in ides:
        setup.setup_ide_config(ide)
    
    setup.init_docs()
    
    print_success("Auto setup complete!")


def main():
    parser = argparse.ArgumentParser(description="Agentic Framework Setup Wizard")
    parser.add_argument("--auto", action="store_true", help="Auto-detect and setup without interaction")
    parser.add_argument("--project-name", help="Project name")
    parser.add_argument("--ide", help="IDEs to configure (comma-separated)")
    parser.add_argument("--from-project-file", help="Path to PROJECT.md or PROGETTO.md")
    
    args = parser.parse_args()
    
    try:
        if args.auto:
            ides = args.ide.split(",") if args.ide else None
            auto_setup(args.project_name, ides, args.from_project_file)
        else:
            interactive_setup()
    except KeyboardInterrupt:
        print_error("\n\nSetup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print_error(f"\n\nSetup failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
