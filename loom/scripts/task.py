#!/usr/bin/env python3
"""
Task Workflow Manager - Agentic Framework v1.0

Gestisce il ciclo completo di un task: start → develop → complete → handoff
con aggiornamento automatico di TASKS.md, STORY.md, CHANGELOG.md e versioning.
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple
import subprocess
import shutil

# Configurazione paths (rilevamento automatico)
PROJECT_ROOT = Path.cwd()
DOCS_DIR = PROJECT_ROOT / "docs"
TASKS_FILE = DOCS_DIR / "TASKS.md"
STORY_FILE = DOCS_DIR / "STORY.md"
CHANGELOG_FILE = DOCS_DIR / "CHANGELOG.md"
HANDOFF_FILE = DOCS_DIR / "HANDOFF.md"
BACKUP_DIR = PROJECT_ROOT / ".task-backups"


class TaskWorkflowError(Exception):
    """Errore nel workflow task."""
    pass


def backup_file(filepath: Path) -> Path:
    """Crea backup di un file prima di modificarlo."""
    if not filepath.exists():
        return None
    
    BACKUP_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"{filepath.name}.{timestamp}.bak"
    shutil.copy2(filepath, backup_path)
    return backup_path


def run_git_command(cmd: list, dry_run: bool = False) -> Tuple[bool, str]:
    """Esegue comando git con gestione errori."""
    if dry_run:
        print(f"[DRY-RUN] git {' '.join(cmd)}")
        return True, ""
    
    try:
        result = subprocess.run(
            ["git"] + cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr


def find_task_in_file(task_id: str, content: str) -> Optional[Tuple[int, int]]:
    """Trova un task in TASKS.md e ritorna (start_pos, end_pos)."""
    # Pattern più robusto che gestisce variazioni di formato
    pattern = rf'###\s*{re.escape(task_id)}[^\n]*\n'
    match = re.search(pattern, content)
    
    if not match:
        return None
    
    start = match.start()
    
    # Trova la fine del task (prossimo ### o fine file)
    next_task = re.search(r'\n###\s+', content[match.end():])
    if next_task:
        end = match.end() + next_task.start()
    else:
        end = len(content)
    
    return (start, end)


def detect_change_type(description: str, commit_type: str) -> str:
    """Rileva tipo di change per CHANGELOG basato su commit type e descrizione."""
    desc_lower = description.lower()
    
    if commit_type == "feat" or any(word in desc_lower for word in ["aggiunto", "implementato", "added", "nuovo"]):
        return "Added"
    elif commit_type == "fix" or any(word in desc_lower for word in ["corretto", "risolto", "fixed", "bug"]):
        return "Fixed"
    elif "security" in desc_lower or "vulnerabilità" in desc_lower or "sicurezza" in desc_lower:
        return "Security"
    elif "deprecat" in desc_lower:
        return "Deprecated"
    elif "rimosso" in desc_lower or "removed" in desc_lower or "eliminato" in desc_lower:
        return "Removed"
    else:
        return "Changed"


def init_task_system(dry_run: bool = False):
    """Inizializza il sistema di task management."""
    print("🚀 Inizializzazione sistema task management...")
    
    # Crea directory docs se non esiste
    if not DOCS_DIR.exists():
        if not dry_run:
            DOCS_DIR.mkdir(parents=True)
        print(f"✅ Creata directory: {DOCS_DIR}")
    
    # Crea file da template se non esistono
    templates_dir = Path(__file__).parent.parent / "docs" / "templates"
    
    files_to_create = [
        (TASKS_FILE, templates_dir / "TASKS.md"),
        (STORY_FILE, templates_dir / "STORY.md"),
        (CHANGELOG_FILE, templates_dir / "CHANGELOG.md"),
        (HANDOFF_FILE, templates_dir / "HANDOFF.md"),
    ]
    
    for target, template in files_to_create:
        if not target.exists():
            if template.exists():
                if not dry_run:
                    shutil.copy2(template, target)
                print(f"✅ Creato: {target.name}")
            else:
                print(f"⚠️  Template non trovato: {template}")
        else:
            print(f"⏭️  Già esistente: {target.name}")
    
    print("\n✨ Sistema task management inizializzato!")


def start_task(task_id: str, description: str, dry_run: bool = False, no_push: bool = False):
    """Avvia un nuovo task."""
    print(f"🚀 Avvio task {task_id}: {description}")
    
    if not TASKS_FILE.exists():
        raise TaskWorkflowError(f"File {TASKS_FILE} non trovato. Esegui 'task.py init' prima.")
    
    # Backup
    backup_path = backup_file(TASKS_FILE)
    if backup_path:
        print(f"💾 Backup creato: {backup_path}")
    
    # Leggi TASKS.md
    content = TASKS_FILE.read_text(encoding="utf-8")
    
    # Verifica che il task non esista già
    if find_task_in_file(task_id, content) is not None:
        raise TaskWorkflowError(f"Task {task_id} già esistente in TASKS.md")
    
    # Aggiorna status a "In Progress"
    new_task_entry = f"\n### {task_id} — {description}\n\n**Status:** In Progress  \n**Priorità:** Media  \n**Avviato:** {datetime.now().strftime('%Y-%m-%d')}\n\n"
    
    # Inserisci nella sezione "Lavoro in Corso"
    updated_content = re.sub(
        r'(## 🚀 Lavoro in Corso\n)',
        rf'\1{new_task_entry}',
        content
    )
    
    if not dry_run:
        TASKS_FILE.write_text(updated_content, encoding="utf-8")
    
    print(f"✅ Task {task_id} aggiunto a TASKS.md")
    
    # Git commit
    success, output = run_git_command(["add", str(TASKS_FILE)], dry_run)
    if not success:
        raise TaskWorkflowError(f"Git add fallito: {output}")
    
    success, output = run_git_command(["commit", "-m", f"chore: start task {task_id}"], dry_run)
    if not success:
        raise TaskWorkflowError(f"Git commit fallito: {output}")
    
    # Git push
    if not no_push:
        success, output = run_git_command(["push"], dry_run)
        if not success:
            print(f"⚠️  Git push fallito: {output}")
            print("💡 Commit locale completato. Esegui 'git push' manualmente.")
        else:
            print("✅ Push completato")
    
    print(f"\n✨ Task {task_id} avviato con successo!")


def complete_task(task_id: str, description: str, version_bump: Optional[str] = None, 
                  dry_run: bool = False, no_push: bool = False):
    """Completa un task esistente."""
    print(f"🎯 Completamento task {task_id}")
    
    if not TASKS_FILE.exists():
        raise TaskWorkflowError(f"File {TASKS_FILE} non trovato.")
    
    # Backup files
    for f in [TASKS_FILE, STORY_FILE, CHANGELOG_FILE]:
        if f.exists():
            backup_path = backup_file(f)
            print(f"💾 Backup: {backup_path}")
    
    # Aggiorna TASKS.md
    content = TASKS_FILE.read_text(encoding="utf-8")
    task_pos = find_task_in_file(task_id, content)
    
    if task_pos is None:
        raise TaskWorkflowError(f"Task {task_id} non trovato in TASKS.md")
    
    start, end = task_pos
    task_section = content[start:end]
    
    # Aggiorna status
    updated_task = re.sub(
        r'\*\*Status:\*\*[^\n]*',
        f'**Status:** Done ✅  \n**Completato:** {datetime.now().strftime("%Y-%m-%d")}',
        task_section
    )
    
    updated_content = content[:start] + updated_task + content[end:]
    
    if not dry_run:
        TASKS_FILE.write_text(updated_content, encoding="utf-8")
    
    print(f"✅ TASKS.md aggiornato")
    
    # Aggiorna STORY.md e CHANGELOG.md se esistono
    if STORY_FILE.exists() and version_bump:
        # TODO: Implementare version bump
        print(f"⏭️  Version bump ({version_bump}) - da implementare")
    
    # Git commit
    commit_type = "feat" if "feat" in description.lower() else "fix"
    commit_msg = f"{commit_type}: {description} [{task_id}]"
    
    success, output = run_git_command(["add", str(TASKS_FILE)], dry_run)
    if not success:
        raise TaskWorkflowError(f"Git add fallito: {output}")
    
    success, output = run_git_command(["commit", "-m", commit_msg], dry_run)
    if not success:
        raise TaskWorkflowError(f"Git commit fallito: {output}")
    
    # Git push
    if not no_push:
        success, output = run_git_command(["push"], dry_run)
        if not success:
            print(f"⚠️  Git push fallito: {output}")
            print("💡 Commit locale completato. Esegui 'git push' manualmente.")
        else:
            print("✅ Push completato")
    
    print(f"\n✨ Task {task_id} completato con successo!")


def list_tasks():
    """Lista tutti i task in TASKS.md."""
    if not TASKS_FILE.exists():
        print("❌ File TASKS.md non trovato. Esegui 'task.py init' prima.")
        return
    
    content = TASKS_FILE.read_text(encoding="utf-8")
    
    # Trova tutti i task
    tasks = re.findall(r'###\s+([A-Z]+-\d+)\s+—\s+([^\n]+)\n.*?\*\*Status:\*\*\s+([^\n]+)', content, re.DOTALL)
    
    if not tasks:
        print("📋 Nessun task trovato in TASKS.md")
        return
    
    print("\n📋 Task attivi:\n")
    for task_id, desc, status in tasks:
        status_icon = "✅" if "Done" in status else "🔄" if "In Progress" in status else "⏸️"
        print(f"{status_icon} {task_id}: {desc}")
        print(f"   Status: {status.strip()}\n")


def main():
    parser = argparse.ArgumentParser(description="Task Workflow Manager")
    parser.add_argument("--dry-run", action="store_true", help="Simula operazioni senza eseguirle")
    
    subparsers = parser.add_subparsers(dest="command", help="Comando da eseguire")
    
    # Init
    subparsers.add_parser("init", help="Inizializza sistema task management")
    
    # Start
    start_parser = subparsers.add_parser("start", help="Avvia nuovo task")
    start_parser.add_argument("task_id", help="ID del task (es: TASK-001)")
    start_parser.add_argument("description", help="Descrizione del task")
    start_parser.add_argument("--no-push", action="store_true", help="Non fare push automatico")
    
    # Complete
    complete_parser = subparsers.add_parser("complete", help="Completa task esistente")
    complete_parser.add_argument("task_id", help="ID del task")
    complete_parser.add_argument("description", help="Descrizione del completamento")
    complete_parser.add_argument("--bump", choices=["major", "minor", "patch"], help="Incrementa versione")
    complete_parser.add_argument("--no-push", action="store_true", help="Non fare push automatico")
    
    # List
    subparsers.add_parser("list", help="Lista tutti i task")
    
    args = parser.parse_args()
    
    try:
        if args.command == "init":
            init_task_system(dry_run=args.dry_run)
        
        elif args.command == "start":
            start_task(args.task_id, args.description, dry_run=args.dry_run, no_push=args.no_push)
        
        elif args.command == "complete":
            complete_task(args.task_id, args.description, version_bump=args.bump, 
                         dry_run=args.dry_run, no_push=args.no_push)
        
        elif args.command == "list":
            list_tasks()
        
        else:
            parser.print_help()
    
    except TaskWorkflowError as e:
        print(f"\n❌ Errore: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Errore inaspettato: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
