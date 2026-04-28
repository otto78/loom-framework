# Natural Language Guide — Antigravity
# Guida al Linguaggio Naturale — Antigravity

> **EN** — No need to run Python scripts manually. Just talk to your AI agent!  
> **IT** — Non serve lanciare script Python manualmente. Basta parlare con il tuo agente AI!

---

## 🎯 Core Idea / Idea Principale

**EN — Zero Setup Friction**

Every modern IDE already has a built-in AI agent. Instead of typing:
```bash
python antigravity/scripts/setup.py
```
Just say:
```
"read Antigravity"
```
Antigravity self-configures by reading its files and your `PROJECT.md`. The agent understands and executes everything automatically.

---

**IT — Setup Senza Attrito**

Ogni IDE moderno ha già un agente AI integrato. Invece di fare:
```bash
python antigravity/scripts/setup.py
```
Basta dire:
```
"leggi Antigravity"
```
Antigravity si auto-configura leggendo i suoi file e il tuo `PROJECT.md`. L'agente capisce ed esegue tutto automaticamente.

---

## 🚀 Initial Setup / Setup Iniziale

### EN — Zero-Friction Setup

Tell the agent (any language works):

```
"read Antigravity"
"configure Antigravity"
"use Antigravity"
"setup Antigravity"
```

The agent will:
1. **Detect context** — reads `Antigravity/` and looks for `PROJECT.md` or `PROGETTO.md`
2. **Self-configure** — initializes `AGENT.md`, IDE rules, task structure
3. **Report back**:
   ```
   ✅ Antigravity configured!

   Project: MyApp
   Source of Truth: AGENT.md
   Active Tasks: docs/TASKS.md

   Ready! Try: "start task TASK-001 'my first feature'"
   ```

**Total time**: ~10 seconds

---

### IT — Setup Zero-Friction

Di' all'agente (funziona in qualsiasi lingua):

```
"leggi Antigravity"
"configura Antigravity"
"usa Antigravity"
"installa Antigravity"
```

L'agente eseguirà:
1. **Rileva il contesto** — legge `Antigravity/` e cerca `PROJECT.md` o `PROGETTO.md`
2. **Si auto-configura** — inizializza `AGENT.md`, le regole IDE e la struttura task
3. **Ti dà il via**:
   ```
   ✅ Antigravity configurato!

   Progetto: MyApp
   Fonte di verità: AGENT.md
   Task attivi: docs/TASKS.md

   Pronto! Prova: "avvia task TASK-001 'mia prima feature'"
   ```

**Tempo totale**: ~10 secondi

---

## 📋 Task Management / Gestione Task

### EN — Starting a Task

```
"start task TASK-001 'implement user authentication'"
```

Agent runs:
```bash
python antigravity/scripts/task.py start TASK-001 "implement user authentication"
```

Agent responds:
```
✅ Task TASK-001 started!
Status: In Progress
Updated: docs/TASKS.md

This is a critical feature. Would you like to use TDD workflow?
```

### IT — Avviare un Task

```
"avvia task TASK-001 'implementa autenticazione utente'"
```

L'agente esegue:
```bash
python antigravity/scripts/task.py start TASK-001 "implementa autenticazione utente"
```

L'agente risponde:
```
✅ Task TASK-001 avviato!
Stato: In corso
Aggiornato: docs/TASKS.md

È una feature critica. Vuoi usare il workflow TDD?
```

---

### EN — Listing Active Tasks

```
"list tasks"
"show tasks"
"what tasks are active?"
```

Agent runs:
```bash
python antigravity/scripts/task.py list
```

Agent responds:
```
📋 Active tasks:

🔄 TASK-001: Implement user authentication
   Status: In Progress
   Started: 2026-01-15

⏸️ TASK-002: Add email validation
   Status: Not Started
```

### IT — Vedere Task Attivi

```
"mostra i task"
"lista task"
"quali task sono attivi?"
```

L'agente esegue:
```bash
python antigravity/scripts/task.py list
```

L'agente risponde:
```
📋 Task attivi:

🔄 TASK-001: Implementa autenticazione utente
   Stato: In corso
   Avviato: 15/01/2026

⏸️ TASK-002: Aggiungi validazione email
   Stato: Non avviato
```

---

### EN — Completing a Task

```
"complete task TASK-001"
"done with TASK-001"
"finish task TASK-001"
```

Agent runs:
```bash
python antigravity/scripts/task.py complete TASK-001 "task completed" --bump patch
```

Agent responds:
```
✅ Task TASK-001 completed!
Updated: docs/TASKS.md, docs/STORY.md
Committed and pushed to git

Version bumped: v1.0.0 → v1.0.1
```

### IT — Completare un Task

```
"completa task TASK-001"
"chiudi TASK-001"
"finisci task TASK-001"
```

L'agente esegue:
```bash
python antigravity/scripts/task.py complete TASK-001 "task completato" --bump patch
```

L'agente risponde:
```
✅ Task TASK-001 completato!
Aggiornato: docs/TASKS.md, docs/STORY.md
Commit e push eseguiti

Versione aggiornata: v1.0.0 → v1.0.1
```

---

## 🧪 TDD Workflow

### EN — Starting a TDD Task

```
"start TDD task TASK-001 'add email validation'"
"use test-driven development for TASK-001"
```

Agent runs:
```bash
python antigravity/scripts/task-tdd.py start TASK-001 "add email validation"
```

Agent responds:
```
🧪 TDD workflow started!

Created test file: tests/test_task_001.py

🔴 Red Phase: Write tests first!

Next steps:
1. Write tests in tests/test_task_001.py
2. Tell me "run tests" to verify they fail
3. Implement the feature
4. Tell me "run tests" again
5. Tell me "complete task TASK-001"
```

### IT — Avviare Task TDD

```
"avvia task TDD TASK-001 'aggiungi validazione email'"
"usa test-driven development per TASK-001"
```

L'agente esegue:
```bash
python antigravity/scripts/task-tdd.py start TASK-001 "aggiungi validazione email"
```

L'agente risponde:
```
🧪 Workflow TDD avviato!

Creato file test: tests/test_task_001.py

🔴 Fase Red: Scrivi prima i test!

Prossimi step:
1. Scrivi i test in tests/test_task_001.py
2. Di' "esegui i test" per verificare che falliscano
3. Implementa la feature
4. Di' "esegui i test" di nuovo
5. Di' "completa task TASK-001"
```

---

### EN — Running Tests

```
"run tests"
"execute tests"
"check tests"
```

Agent runs:
```bash
python antigravity/scripts/task-tdd.py test
```

**Red phase** (expected failures):
```
❌ Tests failed! (Red phase — expected)
3 tests failed. Implement the feature to make them pass.
```

**Green phase** (after implementation):
```
✅ All 3 tests passed! (Green phase)
Ready to complete task.
```

### IT — Eseguire i Test

```
"esegui i test"
"lancia i test"
"controlla i test"
```

L'agente esegue:
```bash
python antigravity/scripts/task-tdd.py test
```

**Fase Red** (fallimenti attesi):
```
❌ Test falliti! (Fase Red — atteso)
3 test falliti. Implementa la feature per farli passare.
```

**Fase Green** (dopo l'implementazione):
```
✅ 3 test passati! (Fase Green)
Pronto per completare il task.
```

---

## 🔄 Sync & Status / Sincronizzazione e Stato

### EN — Syncing IDE Configurations

After editing `AGENT.md` directly:

```
"sync configs"
"sync IDE configs"
```

Agent runs:
```bash
bash antigravity/scripts/sync-configs.sh
```

```
✅ .windsurfrules — in sync
⚠️  .cursorrules — out of sync
✅ Updated .cursorrules
✅ All 7 configurations synced!
```

### IT — Sincronizzare le Configurazioni IDE

Dopo aver modificato `AGENT.md` direttamente:

```
"sincronizza le configurazioni"
"sync configs"
```

L'agente esegue:
```bash
bash antigravity/scripts/sync-configs.sh
```

```
✅ .windsurfrules — sincronizzato
⚠️  .cursorrules — non sincronizzato
✅ Aggiornato .cursorrules
✅ Tutte le 7 configurazioni sincronizzate!
```

---

## 💬 Full Conversation Examples / Esempi di Conversazioni Complete

### EN — Example 1: Setup and First Task

```
You:   "read Antigravity"
Agent: "Detected: Project MyApp, Python, FastAPI.
        Setup Antigravity? (y/n)"
You:   "yes"
Agent: "✅ Antigravity configured! AGENT.md, .cursorrules, docs/TASKS.md created."

You:   "start task TASK-001 'implement login'"
Agent: "✅ TASK-001 started. Use TDD?"
You:   "yes"
Agent: "🧪 TDD started! Write tests in tests/test_task_001.py"

You:   [write tests]
You:   "run tests"
Agent: "❌ Tests failed (Red phase — expected). Implement the feature."

You:   [implement feature]
You:   "run tests"
Agent: "✅ All tests passed! (Green phase)"

You:   "complete task TASK-001"
Agent: "🎉 TASK-001 completed with TDD! All tests passing ✅"
```

### IT — Esempio 1: Setup e Primo Task

```
Tu:    "leggi Antigravity"
Agente:"Rilevato: Progetto MyApp, Python, FastAPI.
        Configuro Antigravity? (s/n)"
Tu:    "sì"
Agente:"✅ Antigravity configurato! Creati AGENT.md, .cursorrules, docs/TASKS.md."

Tu:    "avvia task TASK-001 'implementa login'"
Agente:"✅ TASK-001 avviato. Uso TDD?"
Tu:    "sì"
Agente:"🧪 TDD avviato! Scrivi i test in tests/test_task_001.py"

Tu:    [scrivi test]
Tu:    "esegui i test"
Agente:"❌ Test falliti (fase Red — atteso). Implementa la feature."

Tu:    [implementi la feature]
Tu:    "esegui i test"
Agente:"✅ Tutti i test passati! (Fase Green)"

Tu:    "completa task TASK-001"
Agente:"🎉 TASK-001 completato con TDD! Tutti i test passano ✅"
```

---

### EN — Example 2: Daily Workflow

```
You:   "list tasks"
Agent: "📋 Active: TASK-042 (fix login timeout), TASK-043 (password reset)"

You:   "start task TASK-042 'fix login timeout'"
Agent: "✅ TASK-042 started!"

You:   [work on fix]

You:   "complete task TASK-042"
Agent: "✅ Completed. Version bumped v1.2.3 → v1.2.4"

You:   "start task TASK-043 'add password reset'"
Agent: "✅ TASK-043 started. Use TDD?"
You:   "yes"
```

### IT — Esempio 2: Workflow Quotidiano

```
Tu:    "mostra i task"
Agente:"📋 Attivi: TASK-042 (fix timeout login), TASK-043 (reset password)"

Tu:    "avvia task TASK-042 'fix timeout login'"
Agente:"✅ TASK-042 avviato!"

Tu:    [lavori sul fix]

Tu:    "completa task TASK-042"
Agente:"✅ Completato. Versione aggiornata v1.2.3 → v1.2.4"

Tu:    "avvia task TASK-043 'aggiungi reset password'"
Agente:"✅ TASK-043 avviato. Uso TDD?"
Tu:    "sì"
```

---

## 🌍 Command Reference / Riferimento Comandi

### EN → IT Translation Table

| English | Italiano |
|---------|---------|
| `"read Antigravity"` | `"leggi Antigravity"` |
| `"configure Antigravity"` | `"configura Antigravity"` |
| `"start task TASK-001 'desc'"` | `"avvia task TASK-001 'descrizione'"` |
| `"list tasks"` | `"mostra i task"` / `"lista task"` |
| `"complete task TASK-001"` | `"completa task TASK-001"` |
| `"run tests"` | `"esegui i test"` |
| `"sync configs"` | `"sincronizza configurazioni"` |
| `"show backlog"` | `"mostra il backlog"` |
| `"add to backlog: idea"` | `"aggiungi al backlog: idea"` |
| `"create handoff: notes"` | `"crea handoff: note"` |
| `"read handoff"` | `"leggi handoff"` |

> **Works in any language** — The agent understands variations: "start task" = "create task" = "begin task"  
> **Funziona in qualsiasi lingua** — L'agente capisce variazioni: "avvia task" = "crea task" = "inizia task"

---

## ✅ Benefits / Vantaggi

### EN — Before vs After

**Before Antigravity (Manual)**:
```bash
cd /path/to/project
python antigravity/scripts/setup.py
python antigravity/scripts/task.py start TASK-001 "description"
python antigravity/scripts/task.py list
python antigravity/scripts/task.py complete TASK-001 "done" --bump patch
```

**After Antigravity (Natural)**:
```
"setup framework"
"start task TASK-001 'description'"
"list tasks"
"complete task TASK-001"
```

### IT — Prima vs Dopo

**Prima di Antigravity (Manuale)**:
```bash
cd /path/to/project
python antigravity/scripts/setup.py
python antigravity/scripts/task.py start TASK-001 "descrizione"
python antigravity/scripts/task.py list
python antigravity/scripts/task.py complete TASK-001 "fatto" --bump patch
```

**Dopo Antigravity (Naturale)**:
```
"configura il framework"
"avvia task TASK-001 'descrizione'"
"mostra i task"
"completa task TASK-001"
```

---

## 📚 Related Documentation / Documentazione Correlata

- **[QUICKSTART.md](./QUICKSTART.md)** — 2-minute quick start / Avvio rapido in 2 minuti
- **[README.md](./README.md)** — Full documentation / Documentazione completa
- **[TDD-WORKFLOW.md](./TDD-WORKFLOW.md)** — TDD guide / Guida TDD
- **[SETUP-INSTRUCTIONS.md](./SETUP-INSTRUCTIONS.md)** — For AI agents / Per agenti AI

---

**Version / Versione**: 1.0.0  
**Framework**: Antigravity v1.0  
**Support / Supporto**: All IDEs with AI agents / Tutti gli IDE con agenti AI
