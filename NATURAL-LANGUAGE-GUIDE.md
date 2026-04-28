# Natural Language Guide — Usa il Framework Loom

> Non serve lanciare script Python manualmente. Basta parlare con il tuo agente AI!

---

## 🎯 Idea Principale: Zero Setup Friction

**Ogni IDE moderno ha già un agente AI integrato.**

Invece di fare:
```bash
python loom/scripts/setup.py
```

Basta dire:
```
"read loom"
```

Loom si auto-configura leggendo i suoi file e il tuo `PROJECT.md`. L'agente capisce e esegue tutto automaticamente!

---

## 🚀 Setup Iniziale "Zero-Friction"

### Dici all'agente (Qualsiasi lingua):

**English:**
```
"read loom"
"configure loom"
"use loom"
```

**Italiano:**
```
"leggi loom"
"configura loom"
"usa loom"
"installa loom"
```

### L'agente fa:

1. **Rileva il contesto:** Legge `loom/` e cerca `PROJECT.md` o `PROGETTO.md`.
2. **Si auto-configura:** Inizializza `AGENT.md`, le regole dell'IDE e la struttura task.
3. **Ti dà il via:**
   ```
   ✅ Loom configured!
   
   Project: MyApp
   Source of Truth: AGENT.md
   Active Tasks: docs/TASKS.md
   
   Ready to start! Try: "start task TASK-001 'my first feature'"
   ```

**Tempo totale:** 10 secondi

---

## 📋 Gestione Task con Linguaggio Naturale

### Avviare un Task

**Tu dici:**
```
"start task TASK-001 'implement user authentication'"
```

**L'agente esegue:**
```bash
python loom/scripts/task.py start TASK-001 "implement user authentication"
```

**L'agente risponde:**
```
✅ Task TASK-001 started!
Status: In Progress
Updated: docs/TASKS.md

This is a critical feature. Would you like to use TDD workflow?
```

---

### Vedere Task Attivi

**Tu dici:**
```
"list tasks"
"mostra i task"
```

**L'agente esegue:**
```bash
python loom/scripts/task.py list
```

**L'agente risponde:**
```
📋 Active tasks:

🔄 TASK-001: Implement user authentication
   Status: In Progress
   Started: 2025-01-15

⏸️ TASK-002: Add email validation
   Status: Not Started
```

---

### Completare un Task

**Tu dici:**
```
"complete task TASK-001"
"completa task TASK-001"
```

**L'agente esegue:**
```bash
python loom/scripts/task.py complete TASK-001 "task completed" --bump patch
```

**L'agente risponde:**
```
✅ Task TASK-001 completed!
Updated: docs/TASKS.md, docs/STORY.md
Committed and pushed to git

Version bumped: v1.0.0 → v1.0.1
```

---

## 🧪 TDD Workflow con Linguaggio Naturale

### Avviare Task TDD

**Tu dici:**
```
"start TDD task TASK-001 'add email validation'"
"avvia task TDD TASK-001 'aggiungi validazione email'"
```

**L'agente esegue:**
```bash
python loom/scripts/task-tdd.py start TASK-001 "add email validation"
```

**L'agente risponde:**
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

---

### Eseguire Test

**Tu dici:**
```
"run tests"
"esegui i test"
```

**L'agente esegue:**
```bash
python loom/scripts/task-tdd.py test
```

**L'agente risponde:**
```
🧪 Running tests...

===== test session starts =====
collected 3 items

tests/test_task_001.py FFF

===== FAILURES =====
...

❌ Tests failed! (Red phase - expected)

Next: Implement the feature to make tests pass
```

---

### Completare Task TDD

**Tu dici:**
```
"complete task TASK-001"
```

**L'agente esegue:**
```bash
python loom/scripts/task-tdd.py complete TASK-001
```

**L'agente risponde:**
```
🧪 Running final tests...

===== 3 passed in 0.12s =====

✅ All tests passed!

🎉 Task TASK-001 completed with TDD workflow!
   All tests passing ✅
```

---

## 🔄 Sincronizzazione Configurazioni

### Dopo Modifica AGENT.md

**Tu dici:**
```
"sync configs"
```

**L'agente esegue:**
```bash
bash loom/scripts/sync-configs.sh
```

**L'agente risponde:**
```
Syncing IDE configurations...

✅ .windsurfrules is in sync
⚠️  .cursorrules is out of sync
✅ Updated .cursorrules
✅ All configurations synced!
```

---

## 💬 Esempi di Conversazioni Complete

### Esempio 1: Setup e Primo Task

```
Tu: "read loom"

Agente: "I detected:
- Project: MyApp
- Languages: Python
- Frameworks: FastAPI
Do you want me to setup Loom?"

Tu: "yes"

Agente: "✅ Loom configured! Created AGENT.md, .cursorrules, docs/TASKS.md
Ready to use!"

Tu: "start task TASK-001 'implement login'"

Agente: "✅ Task TASK-001 started!
This is a critical feature. Use TDD workflow?"

Tu: "yes"

Agente: "🧪 TDD workflow started!
Created tests/test_task_001.py
Write tests first (Red phase)"

Tu: [scrivi test]

Tu: "run tests"

Agente: "❌ Tests failed (expected - Red phase)
Now implement the feature"

Tu: [implementi feature]

Tu: "run tests"

Agente: "✅ All tests passed! (Green phase)
Ready to complete?"

Tu: "complete task TASK-001"

Agente: "🎉 Task completed with TDD!
All tests passing ✅"
```

---

### Esempio 2: Workflow Quotidiano

```
Tu: "list tasks"

Agente: "📋 Active tasks:
🔄 TASK-042: Fix login timeout
⏸️ TASK-043: Add password reset"

Tu: "start task TASK-042 'fix login timeout'"

Agente: "✅ Task TASK-042 started!"

Tu: [lavori sul fix]

Tu: "complete task TASK-042"

Agente: "✅ Task completed!
Version bumped: v1.2.3 → v1.2.4"

Tu: "start task TASK-043 'add password reset'"

Agente: "✅ Task TASK-043 started!
Use TDD for this?"

Tu: "yes"

Agente: "🧪 TDD workflow started!"
```

---

## 🌍 Supporto Multilingua

Loom è progettato per essere agnostico rispetto alla lingua. Puoi parlare con l'agente come preferisci:

### Italiano
```
"leggi loom"
"configura il framework"
"avvia task TASK-001 'descrizione'"
"mostra i task"
"completa task TASK-001"
"esegui i test"
"sincronizza configurazioni"
```

### English
```
"read loom"
"setup the framework"
"start task TASK-001 'description'"
"show tasks"
"complete task TASK-001"
"run tests"
"sync configurations"
```

---

## ✅ Vantaggi

### Prima (Manuale)
```bash
# Devi ricordare i comandi
cd /path/to/project
python agentic-framework/scripts/setup.py
python agentic-framework/scripts/task.py start TASK-001 "description"
python agentic-framework/scripts/task.py list
python agentic-framework/scripts/task.py complete TASK-001 "done" --bump patch
```

### Dopo (Naturale)
```
"setup framework"
"start task TASK-001 'description'"
"list tasks"
"complete task TASK-001"
```

**Più veloce, più intuitivo, più naturale!**

---

## 🎓 Best Practices

### 1. Usa Linguaggio Naturale
Non serve ricordare sintassi esatta. L'agente capisce variazioni:
- "start task" = "create task" = "begin task"
- "list tasks" = "show tasks" = "what tasks"
- "complete task" = "finish task" = "done with task"

### 2. Lascia che l'Agente Suggerisca
L'agente suggerirà TDD per feature critiche:
```
Agente: "This is a critical feature. Use TDD workflow?"
```

### 3. Chiedi Aiuto
```
Tu: "how do I use the framework?"
Agente: [spiega comandi disponibili]
```

### 4. Usa Abbreviazioni
```
"start TASK-001 'feature'"  # Funziona
"list"                       # Funziona
"complete TASK-001"          # Funziona
```

---

## 📚 Documentazione

Per dettagli tecnici:
- **[SETUP-INSTRUCTIONS.md](./SETUP-INSTRUCTIONS.md)** — Per agenti AI
- **[README.md](./README.md)** — Documentazione completa
- **[QUICKSTART.md](./QUICKSTART.md)** — Guida rapida
- **[TDD-WORKFLOW.md](./TDD-WORKFLOW.md)** — Guida TDD

---

## 🎉 Conclusione

**Non serve più lanciare script manualmente!**

Basta parlare con il tuo agente AI:
- "setup framework" → Setup automatico
- "start task" → Crea task
- "run tests" → Esegue test
- "complete task" → Completa task

**Più semplice, più veloce, più naturale!** 🚀

---

**Versione:** 1.0.0  
**Framework:** Agentic Framework v1.0  
**Supporto:** Tutti gli IDE con agenti AI integrati
