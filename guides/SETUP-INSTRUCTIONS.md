# Setup Instructions — For AI Agents
# Istruzioni di Setup — Per Agenti AI

> **EN — IMPORTANT:** This file is read by AI agents to understand how to set up the framework.  
> When a user says "read loom", "leggi loom", "setup loom" or similar, follow these instructions.

> **IT — IMPORTANTE:** Questo file è letto dagli agenti AI per capire come configurare il framework.  
> Quando l'utente dice "leggi loom", "read loom", "configura loom" o simili, segui queste istruzioni.

---

## 🤖 EN — For AI Agents: How to setup loom

### User Trigger Phrases

When the user says any of these:
- `"read loom"` / `"leggi loom"`
- `"setup loom"` / `"configure loom"`
- `"inizializza loom"` / `"usa loom"`
- `"configura loom"` / `"installa loom"`
- `"setup agentic framework"` / `"setup loom"`

**→ Execute the Zero-Friction Setup procedure automatically**

---

### Step 1: Detect Project Context & loom Files

Before running setup, gather information:

1. **Read all files in `loom/`** — understand the available directives, templates, and scripts.
2. **Search for Project Meta-File** — look for `PROJECT.md` or `PROGETTO.md` in the root.
3. **Analyze Tech Stack** — detect languages, frameworks, and existing IDE configs.

### Step 2: Auto-Configuration

**If `PROJECT.md` (or `PROGETTO.md`) is found:**
1. Use the content as the primary source of truth.
2. Run setup script:
   ```bash
   python loom/scripts/setup.py --auto --project-name "[detected_name]" --from-project-file PROJECT.md
   ```

**If NOT found:**
1. Ask user: *"I detected the `loom/` folder but no `PROJECT.md`. Would you like me to create one, or can you point me to a project description?"*
2. Offer to create `PROJECT.md` from template: `loom/templates/PROJECT.md.template`

### Step 3: Report Results

After setup completes, tell the user:

```
✅ loom configured!

Project: [project_name]
Source of Truth: AGENT.md
Task Tracking: docs/TASKS.md

Ready! Try: "start task TASK-001 'description'"
```

---

## 🤖 IT — Per Agenti AI: Come Configurare loom

### Frasi Trigger dell'Utente

Quando l'utente dice uno di questi:
- `"leggi loom"` / `"read loom"`
- `"configura loom"` / `"setup loom"`
- `"inizializza loom"` / `"usa loom"`
- `"installa loom"` / `"configure loom"`

**→ Esegui automaticamente la procedura di Setup Zero-Friction**

---

### Step 1: Rileva il Contesto e i File loom

Prima di eseguire il setup, raccogli informazioni:

1. **Leggi tutti i file in `loom/`** — comprendi le direttive, i template e gli script disponibili.
2. **Cerca il File Meta del Progetto** — cerca `PROJECT.md` o `PROGETTO.md` nella root.
3. **Analizza lo Stack Tecnologico** — rileva linguaggi, framework e configurazioni IDE esistenti.

### Step 2: Auto-Configurazione

**Se `PROJECT.md` (o `PROGETTO.md`) è trovato:**
1. Usa il contenuto come fonte di verità primaria.
2. Esegui lo script di setup:
   ```bash
   python loom/scripts/setup.py --auto --project-name "[nome_rilevato]" --from-project-file PROJECT.md
   ```

**Se NON trovato:**
1. Chiedi all'utente: *"Ho rilevato la cartella `loom/` ma nessun `PROJECT.md`. Vuoi che ne crei uno, o puoi indicarmi una descrizione del progetto?"*
2. Offri di creare `PROJECT.md` dal template: `loom/templates/PROJECT.md.template`

### Step 3: Riporta i Risultati

Dopo che il setup è completato, di' all'utente:

```
✅ loom configurato!

Progetto: [nome_progetto]
Fonte di verità: AGENT.md
Tracciamento task: docs/TASKS.md

Pronto! Prova: "avvia task TASK-001 'descrizione'"
```

---

## 🎯 Task Management Commands / Comandi di Gestione Task

| User Says / L'Utente Dice | Execute / Esegui |
|---------------------------|-----------------|
| `"read loom"` / `"leggi loom"` | `python loom/scripts/read_loom.py` |
| `"setup loom"` / `"configura loom"` | `python loom/scripts/setup.py` |
| `"start task TASK-XXX 'desc'"` | `python loom/scripts/task.py start TASK-XXX "desc"` |
| `"avvia task TASK-XXX 'desc'"` | `python loom/scripts/task.py start TASK-XXX "desc"` |
| `"start TDD task TASK-XXX 'desc'"` | `python loom/scripts/task-tdd.py start TASK-XXX "desc"` |
| `"avvia task TDD TASK-XXX 'desc'"` | `python loom/scripts/task-tdd.py start TASK-XXX "desc"` |
| `"list tasks"` / `"mostra i task"` | `python loom/scripts/task.py list` |
| `"run tests"` / `"esegui i test"` | `python loom/scripts/task-tdd.py test` |
| `"complete task TASK-XXX"` | `python loom/scripts/task.py complete TASK-XXX "done"` |
| `"completa task TASK-XXX"` | `python loom/scripts/task.py complete TASK-XXX "fatto"` |
| `"sync configs"` / `"sincronizza configurazioni"` | `bash loom/scripts/sync-configs.sh` |
| `"loom version"` / `"versione loom"` | `python loom/scripts/update.py --status` |
| `"check for loom updates"` / `"ci sono aggiornamenti?"` | `python loom/scripts/update.py --check` |
| `"update loom"` / `"aggiorna loom"` | `python loom/scripts/update.py --apply` |
| `"rollback loom"` / `"ripristina loom"` | `python loom/scripts/update.py --rollback` |

---

## 🔄 EN — Updating loom

### If `update.py` is already present (v1.0.16+)

```bash
python loom/scripts/update.py --check    # check if updates are available
python loom/scripts/update.py --apply    # download and apply the update
python loom/scripts/update.py --rollback # restore previous version if needed
```

After `--apply`, run `python loom/scripts/setup.py` to configure any new IDE/Agent support.

### If `update.py` is NOT present (older version — bootstrap)

Download `update.py` first, then use it to update everything:

**Windows (PowerShell):**
```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/otto78/loom-framework/main/loom/scripts/update.py" -OutFile "loom/scripts/update.py"
python loom/scripts/update.py --apply
```

**Linux / macOS:**
```bash
curl -fsSL https://raw.githubusercontent.com/otto78/loom-framework/main/loom/scripts/update.py -o loom/scripts/update.py
python loom/scripts/update.py --apply
```

> 🔒 **Safe to run at any time** — your project files (AGENT.md, IDE configs, TASKS.md, STORY.md, etc.) are **never touched**. Only the `loom/` directory is updated.

---

## 🔄 IT — Aggiornare loom

### Se `update.py` è già presente (v1.0.16+)

```bash
python loom/scripts/update.py --check    # verifica se ci sono aggiornamenti
python loom/scripts/update.py --apply    # scarica e applica l'aggiornamento
python loom/scripts/update.py --rollback # ripristina la versione precedente
```

Dopo `--apply`, esegui `python loom/scripts/setup.py` per configurare eventuali nuovi tool.

### Se `update.py` NON è presente (versione precedente — bootstrap)

Scarica prima `update.py`, poi usalo per aggiornare tutto:

**Windows (PowerShell):**
```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/otto78/loom-framework/main/loom/scripts/update.py" -OutFile "loom/scripts/update.py"
python loom/scripts/update.py --apply
```

**Linux / macOS:**
```bash
curl -fsSL https://raw.githubusercontent.com/otto78/loom-framework/main/loom/scripts/update.py -o loom/scripts/update.py
python loom/scripts/update.py --apply
```

> 🔒 **Sicuro da eseguire in qualsiasi momento** — i file del progetto (AGENT.md, config IDE, TASKS.md, STORY.md, ecc.) non vengono **mai toccati**. Viene aggiornata solo la cartella `loom/`.

---

## ⚠️ EN — Important Notes for Agents

1. **Always read `AGENT.md` first** — before any work, read it to understand the current project state, rules, and constraints.
2. **Respect persistent memory** — `TASKS.md` and `STORY.md` are the source of truth. Always update them after completing a task.
3. **Multi-agent handoff** — if finishing a session, update `docs/HANDOFF.md` so the next agent can resume seamlessly.
4. **Suggest TDD for critical features** — for security, auth, or core logic tasks, always suggest TDD workflow.
5. **Commit selectively** — never use `git add -A`. Use `loom/execution/git_commit.py` or specify files explicitly.

## ⚠️ IT — Note Importanti per gli Agenti

1. **Leggi sempre prima `AGENT.md`** — prima di qualsiasi lavoro, leggilo per capire lo stato attuale del progetto, le regole e i vincoli.
2. **Rispetta la memoria persistente** — `TASKS.md` e `STORY.md` sono la fonte di verità. Aggiornali sempre dopo aver completato un task.
3. **Handoff multi-agente** — se stai terminando una sessione, aggiorna `docs/HANDOFF.md` in modo che il prossimo agente possa riprendere senza interruzioni.
4. **Suggerisci TDD per feature critiche** — per task relativi a sicurezza, auth o logica core, suggerisci sempre il workflow TDD.
5. **Commit selettivo** — non usare mai `git add -A`. Usa `loom/execution/git_commit.py` o specifica i file esplicitamente.

---

**Version / Versione**: 1.0.16  
**For / Per**: AI Agents — Windsurf, Cursor, Trae, Antigravity, VS Code, IntelliJ + Agents: Claude Code, Cline  
**Purpose / Scopo**: Enable zero-friction setup and persistent task management / Setup senza attrito e gestione task persistente

