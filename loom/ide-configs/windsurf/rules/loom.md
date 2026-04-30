# Windsurf Rules — loom

> Leggi sempre `AGENT.md` all'inizio di ogni sessione.
> Questo file contiene solo istruzioni specifiche per Windsurf (Cascade).
> Per l'architettura DOE, task management, commit protocol e handoff: vedi `AGENT.md`.
> Windsurf legge anche `AGENTS.md` nativamente (cross-tool).

---

## 🚀 Setup Automatico

**Trigger:** "setup loom" / "configura il framework"

**Comando:**
```bash
python loom/scripts/setup.py
```

---

## 💬 Comandi Naturali

| Utente dice | Tu esegui |
|-------------|----------|
| "start task TASK-001 'feature X'" | `python loom/scripts/task.py start TASK-001 "feature X"` |
| "list tasks" | `python loom/scripts/task.py list` |
| "complete task TASK-001" | `python loom/scripts/task.py complete TASK-001 "done"` |
| "start TDD task TASK-001 'feature X'" | `python loom/scripts/task-tdd.py start TASK-001 "feature X"` |
| "run tests" | `python loom/scripts/task-tdd.py test` |
| "sync configs" | `bash loom/scripts/sync-configs.sh` |

---

## Best Practices Windsurf (Cascade)

- Usa Cascade per task multi-step: pianifica prima di eseguire
- Usa rollback (freccia accanto al prompt) se qualcosa va storto
  **⚠️ ATTENZIONE:** i rollback in Windsurf sono irreversibili
- Reset Session da Command Palette se Cascade perde il contesto
- Chiedi conferma prima di operazioni irreversibili
