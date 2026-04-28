# Loom Framework — Quick Start 🚀
# Avvio Rapido 🚀

> **EN** — Get started in 2 minutes with zero commands to remember!  
> **IT** — Inizia in 2 minuti senza comandi da ricordare!

---

## ⚡ The Easiest Way / Il Modo Più Semplice

### EN — Zero-Friction Setup

**For new projects (4 steps):**

1. Create your project folder
2. Create `PROJECT.md` with your project description
3. Add `loom/` folder to your project:
   ```bash
   git clone https://github.com/otto78/loom-framework.git loom
   ```
4. Open any IDE and say: **"read loom"**

That's it! Loom reads all its files, finds your `PROJECT.md`, and auto-configures everything.

**For existing projects (2 steps):**

1. Add Loom to your project:
   ```bash
   cd /path/to/your-existing-project
   git clone https://github.com/otto78/loom-framework.git loom
   ```
2. Open any IDE and say: **"read loom"**

---

### IT — Setup Zero-Friction

**Per nuovi progetti (4 step):**

1. Crea la cartella del progetto
2. Crea `PROJECT.md` con la descrizione del tuo progetto
3. Aggiungi la cartella `loom/` al tuo progetto:
   ```bash
   git clone https://github.com/otto78/loom-framework.git loom
   ```
4. Apri qualsiasi IDE e di': **"leggi loom"**

Fatto! Loom legge tutti i suoi file, trova il tuo `PROJECT.md` e configura tutto automaticamente.

**Per progetti esistenti (2 step):**

1. Aggiungi Loom al tuo progetto:
   ```bash
   cd /path/to/your-existing-project
   git clone https://github.com/otto78/loom-framework.git loom
   ```
2. Apri qualsiasi IDE e di': **"leggi loom"**

---

## 🎯 What Happens When You Say "read loom" / Cosa Succede Quando Dici "leggi loom"

### EN

The AI agent automatically:

1. ✅ Reads all Loom framework files
2. ✅ Finds or creates `PROJECT.md` (your project description)
3. ✅ Detects your programming languages and frameworks
4. ✅ Detects your IDE (Cursor, Windsurf, VS Code, etc.)
5. ✅ Creates `AGENT.md` (source of truth for every session)
6. ✅ Creates `docs/TASKS.md`, `STORY.md`, `CHANGELOG.md`
7. ✅ Creates IDE config files (`.cursorrules`, `.windsurfrules`, etc.)
8. ✅ Initializes the 3-level framework structure

**Result**: Your project is ready for AI-assisted development!

### IT

L'agente AI automaticamente:

1. ✅ Legge tutti i file del framework Loom
2. ✅ Trova o crea `PROJECT.md` (la descrizione del tuo progetto)
3. ✅ Rileva i linguaggi di programmazione e i framework in uso
4. ✅ Rileva il tuo IDE (Cursor, Windsurf, VS Code, ecc.)
5. ✅ Crea `AGENT.md` (fonte di verità per ogni sessione)
6. ✅ Crea `docs/TASKS.md`, `STORY.md`, `CHANGELOG.md`
7. ✅ Crea i file di configurazione IDE (`.cursorrules`, `.windsurfrules`, ecc.)
8. ✅ Inizializza la struttura del framework a 3 livelli

**Risultato**: Il tuo progetto è pronto per lo sviluppo assistito dall'AI!

---

## 📋 Your First Task / Il Tuo Primo Task

### EN

Just talk to your AI agent:

```
"start task TASK-001 'implement user login'"
```

The agent will:
- Create the task in `docs/TASKS.md`
- Track progress automatically
- Update `docs/STORY.md` as you work
- Maintain context across sessions

### IT

Parla semplicemente con il tuo agente AI:

```
"avvia task TASK-001 'implementa il login utente'"
```

L'agente:
- Creerà il task in `docs/TASKS.md`
- Traccerà i progressi automaticamente
- Aggiornerà `docs/STORY.md` mentre lavori
- Manterrà il contesto tra le sessioni

---

## 🔄 Daily Workflow / Workflow Quotidiano

### EN

**Morning:**
```
"show me the tasks"
"what's the status of TASK-042?"
```

**During work:**
```
"start task TASK-042 'fix login bug'"
[work on it]
"complete task TASK-042"
```

**Evening:**
```
"update the story with today's progress"
"create handoff notes for tomorrow"
```

**No commands to remember. Just natural language.**

### IT

**Mattina:**
```
"mostra i task"
"qual è lo stato di TASK-042?"
```

**Durante il lavoro:**
```
"avvia task TASK-042 'fix bug login'"
[lavori su di esso]
"completa task TASK-042"
```

**Sera:**
```
"aggiorna la storia con i progressi di oggi"
"crea le note di handoff per domani"
```

**Nessun comando da ricordare. Solo linguaggio naturale.**

---

## 🧪 TDD Workflow (Optional / Opzionale)

### EN

For critical features:

```
"start TDD task TASK-001 'add email validation'"
[agent creates test file]

"run tests"
[tests fail — Red phase]

[implement the feature]

"run tests"
[tests pass — Green phase]

"complete task TASK-001"
```

### IT

Per feature critiche:

```
"avvia task TDD TASK-001 'aggiungi validazione email'"
[l'agente crea il file di test]

"esegui i test"
[test falliscono — fase Red]

[implementi la feature]

"esegui i test"
[test passano — fase Green]

"completa task TASK-001"
```

---

## 📚 Key Files Created / File Chiave Creati

### EN

After "read loom", you'll have:

```
your-project/
├── PROJECT.md          ⭐ Your project description (you create this)
├── AGENT.md            ⭐ Source of truth (auto-generated from PROJECT.md)
├── .cursorrules        IDE config (auto-generated)
├── .windsurfrules      IDE config (auto-generated)
├── CLAUDE.md           IDE config (auto-generated)
├── ANTIGRAVITY.md      IDE config (auto-generated)
├── loom/               Framework files
└── docs/
    ├── TASKS.md        Active tasks (auto-updated)
    ├── BACKLOG.md      Future ideas
    ├── STORY.md        Project history (auto-updated)
    ├── CHANGELOG.md    Version history (auto-updated)
    └── HANDOFF.md      Agent handoff notes
```

### IT

Dopo "leggi loom", avrai:

```
your-project/
├── PROJECT.md          ⭐ Descrizione del tuo progetto (la crei tu)
├── AGENT.md            ⭐ Fonte di verità (auto-generato da PROJECT.md)
├── .cursorrules        Configurazione IDE (auto-generata)
├── .windsurfrules      Configurazione IDE (auto-generata)
├── CLAUDE.md           Configurazione IDE (auto-generata)
├── ANTIGRAVITY.md      Configurazione IDE (auto-generata)
├── loom/               File del framework
└── docs/
    ├── TASKS.md        Task attivi (auto-aggiornato)
    ├── BACKLOG.md      Idee future
    ├── STORY.md        Storia del progetto (auto-aggiornato)
    ├── CHANGELOG.md    Cronologia versioni (auto-aggiornata)
    └── HANDOFF.md      Note di handoff per l'agente
```

---

## 🎨 Supported IDEs / IDE Supportati

### EN

Loom auto-configures for 7 IDEs:

| IDE/Tool | Config File |
|----------|-------------|
| 🌊 Windsurf | `.windsurfrules` |
| 🤖 Claude Code | `CLAUDE.md` |
| ↗️ Cursor | `.cursorrules` |
| ✨ Antigravity | `ANTIGRAVITY.md` |
| 💻 VS Code (Cline) | `.clinerules` |
| 💡 IntelliJ IDEA | `agentic-framework.md` |
| 🐙 GitHub Copilot | `copilot-instructions.md` |

**Switch between IDEs without losing context!**

### IT

Loom si auto-configura per 7 IDE:

| IDE/Tool | File di Configurazione |
|----------|----------------------|
| 🌊 Windsurf | `.windsurfrules` |
| 🤖 Claude Code | `CLAUDE.md` |
| ↗️ Cursor | `.cursorrules` |
| ✨ Antigravity | `ANTIGRAVITY.md` |
| 💻 VS Code (Cline) | `.clinerules` |
| 💡 IntelliJ IDEA | `agentic-framework.md` |
| 🐙 GitHub Copilot | `copilot-instructions.md` |

**Passa da un IDE all'altro senza perdere il contesto!**

---

## 💡 Pro Tips / Suggerimenti Pro

### EN

**1. Make PROJECT.md Detailed**  
The more detail you add, the better the agent understands your project:
- Project goals and vision
- Tech stack and why you chose it
- Architecture decisions
- Coding standards
- Known issues or constraints

**2. Use BACKLOG.md for Ideas**  
Don't create tasks immediately. Add ideas to BACKLOG.md first:
```
"add to backlog: implement dark mode"
```
Convert when ready:
```
"convert backlog item 'dark mode' to task TASK-010"
```

**3. Use Handoffs Between Sessions**  
```
"create handoff: working on TASK-042, login bug partially fixed, need to test edge cases tomorrow"
```
Next session:
```
"read handoff"
```

### IT

**1. Rendi PROJECT.md Dettagliato**  
Più dettagli aggiungi, meglio l'agente capisce il tuo progetto:
- Obiettivi e visione del progetto
- Stack tecnologico e motivazioni
- Decisioni architetturali
- Standard di codice
- Problemi noti o vincoli

**2. Usa BACKLOG.md per le Idee**  
Non creare subito i task. Aggiungi prima le idee al BACKLOG.md:
```
"aggiungi al backlog: implementa dark mode"
```
Converti quando sei pronto:
```
"converti backlog 'dark mode' in task TASK-010"
```

**3. Usa gli Handoff tra le Sessioni**  
```
"crea handoff: lavorando su TASK-042, bug login parzialmente fixato, bisogna testare i casi limite domani"
```
Sessione successiva:
```
"leggi handoff"
```

---

## 🔗 Alternative Methods / Metodi Alternativi

### EN — Method 2: Interactive Wizard

```bash
cd /path/to/your-project
python /path/to/loom-framework/loom/scripts/setup.py
```

### Method 3: Fully Automated

```bash
python loom/scripts/setup.py --auto --project-name "MyProject" --ide windsurf,cursor
```

**But honestly, just saying "read loom" is easier!**

### IT — Metodo 2: Wizard Interattivo

```bash
cd /path/to/your-project
python /path/to/loom-framework/loom/scripts/setup.py
```

### Metodo 3: Completamente Automatizzato

```bash
python loom/scripts/setup.py --auto --project-name "MyProject" --ide windsurf,cursor
```

**Ma onestamente, dire "leggi loom" è molto più semplice!**

---

## 📖 Next Steps / Prossimi Passi

### EN
- **[ABSTRACT.md](./ABSTRACT.md)** — Understand the core concepts
- **[NATURAL-LANGUAGE-GUIDE.md](./NATURAL-LANGUAGE-GUIDE.md)** — All commands you can use
- **[TDD-WORKFLOW.md](./TDD-WORKFLOW.md)** — Test-Driven Development
- **[MONOREPO-GUIDE.md](./MONOREPO-GUIDE.md)** — Using Loom in monorepos
- **[docs/framework-guide.md](./docs/framework-guide.md)** — 3-level architecture

### IT
- **[ABSTRACT.md](./ABSTRACT.md)** — Comprendi i concetti fondamentali
- **[NATURAL-LANGUAGE-GUIDE.md](./NATURAL-LANGUAGE-GUIDE.md)** — Tutti i comandi disponibili
- **[TDD-WORKFLOW.md](./TDD-WORKFLOW.md)** — Sviluppo guidato dai test
- **[MONOREPO-GUIDE.md](./MONOREPO-GUIDE.md)** — Uso di Loom nei monorepo
- **[docs/framework-guide.md](./docs/framework-guide.md)** — Architettura a 3 livelli

---

## 🆘 Need Help? / Hai Bisogno di Aiuto?

- **Issues / Problemi**: [GitHub Issues](https://github.com/otto78/loom-framework/issues)
- **Discussions / Discussioni**: [GitHub Discussions](https://github.com/otto78/loom-framework/discussions)
- **Website / Sito**: [otto78.github.io/loom-framework](https://otto78.github.io/loom-framework)

---

**EN** — That's it! You're ready to weave intelligent agents into your workflow. 🧵  
**IT** — Fatto! Sei pronto per integrare agenti intelligenti nel tuo workflow. 🧵

**Version / Versione**: 1.0.0  
**Setup time / Tempo di setup**: ~2 minutes / ~2 minuti  
**Time to first task / Tempo al primo task**: ~30 seconds / ~30 secondi
