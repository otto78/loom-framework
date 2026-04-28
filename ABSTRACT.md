# Loom Framework — Abstract

> **The operational framework that makes AI agents reliable, persistent, and token-efficient**

---

## 🇬🇧 English

### The Problem

AI-assisted development faces three critical challenges:

1. **Context Window Limitations**
   - Agents lose memory when context resets
   - Long conversations hit token limits
   - Critical project knowledge gets forgotten

2. **Multi-Agent Chaos**
   - Switching between IDEs loses context
   - Different agents can't share state
   - Handoffs between sessions fail
   - Team collaboration becomes fragmented

3. **Token Waste & Probabilistic Failures**
   - Agents repeat the same prompts over and over
   - 90% accuracy per step = 35% success over 10 steps
   - Complex tasks chain failures exponentially
   - No learning between sessions

### The Solution: Loom Framework

Loom solves these problems through **persistent file-based memory** and a **deterministic 3-level architecture**:

#### 1. Persistent Memory (Beats Context Limits)
- **TASKS.md** — Active work tracking that survives context resets
- **STORY.md** — Operational history across all sessions
- **AGENT.md** — Single source of truth for project context
- **CHANGELOG.md** — Automatic versioning and change tracking

These files create a **shared memory layer** that:
- Survives context window resets
- Works across different IDEs and agents
- Enables seamless handoffs between sessions
- Maintains project continuity indefinitely

#### 2. Multi-IDE & Multi-Agent Support
- **7 IDE configs** kept in sync automatically
- Same workflow in Cursor, Windsurf, Claude Code, VS Code, IntelliJ, Gemini, Copilot
- Agents read the same files regardless of IDE
- Switch tools without losing context

#### 3. Token-Efficient Deterministic Framework
- **Directives** (Level 1): SOPs in natural language — what to do
- **Orchestration** (Level 2): Agent makes decisions — how to decide
- **Execution** (Level 3): Python scripts do the work — deterministic

**Token savings**: Instead of prompting "how to send email" every time, the agent:
1. Reads `directives/send-email.md` once (cached)
2. Calls `execution/send_email.py` (deterministic, no tokens)
3. Gets JSON result (structured, minimal tokens)

**Result**: 90% accuracy maintained over 10+ steps instead of degrading to 35%.

#### 4. Self-Improving Agents
- Agents write new directives as they learn
- Scripts get reused across sessions
- Framework improves with every project
- Knowledge compounds instead of resetting

### Zero-Friction Setup

No commands to remember. Just:

```
1. Create your project folder
2. Add PROJECT.md with project description
3. Put loom/ folder in your project
4. Open any IDE and say: "read loom"
```

That's it. Loom auto-configures everything.

### Key Benefits

- ✅ **Persistent**: Survives context resets and session changes
- ✅ **Multi-Agent**: Works across IDEs and AI tools
- ✅ **Token-Efficient**: Reuses knowledge, minimizes repetition
- ✅ **Deterministic**: Scripts replace probabilistic prompts
- ✅ **Self-Improving**: Agents learn and compound knowledge
- ✅ **Zero-Friction**: Natural language setup, no commands

---

## 🇮🇹 Italiano

### Il Problema

Lo sviluppo assistito da AI affronta tre sfide critiche:

1. **Limiti della Finestra di Contesto**
   - Gli agenti perdono la memoria quando il contesto si resetta
   - Le conversazioni lunghe raggiungono i limiti di token
   - La conoscenza critica del progetto viene dimenticata

2. **Caos Multi-Agente**
   - Cambiare IDE perde il contesto
   - Agenti diversi non possono condividere lo stato
   - I passaggi tra sessioni falliscono
   - La collaborazione di team diventa frammentata

3. **Spreco di Token & Fallimenti Probabilistici**
   - Gli agenti ripetono gli stessi prompt continuamente
   - 90% di accuratezza per step = 35% di successo su 10 step
   - Task complessi accumulano fallimenti esponenzialmente
   - Nessun apprendimento tra sessioni

### La Soluzione: Loom Framework

Loom risolve questi problemi attraverso **memoria persistente basata su file** e un'**architettura deterministica a 3 livelli**:

#### 1. Memoria Persistente (Supera i Limiti di Contesto)
- **TASKS.md** — Tracciamento lavoro che sopravvive ai reset
- **STORY.md** — Storia operativa attraverso tutte le sessioni
- **AGENT.md** — Unica fonte di verità per il contesto del progetto
- **CHANGELOG.md** — Versioning e tracking automatico delle modifiche

Questi file creano un **layer di memoria condivisa** che:
- Sopravvive ai reset della finestra di contesto
- Funziona tra IDE e agenti diversi
- Abilita passaggi fluidi tra sessioni
- Mantiene la continuità del progetto indefinitamente

#### 2. Supporto Multi-IDE & Multi-Agente
- **7 config IDE** mantenute sincronizzate automaticamente
- Stesso workflow in Cursor, Windsurf, Claude Code, VS Code, IntelliJ, Gemini, Copilot
- Gli agenti leggono gli stessi file indipendentemente dall'IDE
- Cambia strumenti senza perdere contesto

#### 3. Framework Deterministico Token-Efficient
- **Direttive** (Livello 1): SOP in linguaggio naturale — cosa fare
- **Orchestrazione** (Livello 2): L'agente decide — come decidere
- **Esecuzione** (Livello 3): Script Python fanno il lavoro — deterministico

**Risparmio token**: Invece di chiedere "come inviare email" ogni volta, l'agente:
1. Legge `directives/send-email.md` una volta (cached)
2. Chiama `execution/send_email.py` (deterministico, zero token)
3. Ottiene risultato JSON (strutturato, token minimi)

**Risultato**: 90% di accuratezza mantenuta su 10+ step invece di degradare al 35%.

#### 4. Agenti Auto-Miglioranti
- Gli agenti scrivono nuove direttive mentre imparano
- Gli script vengono riutilizzati tra sessioni
- Il framework migliora con ogni progetto
- La conoscenza si accumula invece di resettarsi

### Setup Zero-Friction

Nessun comando da ricordare. Semplicemente:

```
1. Crea la cartella del tuo progetto
2. Aggiungi PROJECT.md con la descrizione del progetto
3. Metti la cartella loom/ nel tuo progetto
4. Apri qualsiasi IDE e di': "leggi loom"
```

Tutto qui. Loom auto-configura tutto.

### Benefici Chiave

- ✅ **Persistente**: Sopravvive a reset di contesto e cambi di sessione
- ✅ **Multi-Agente**: Funziona tra IDE e strumenti AI
- ✅ **Token-Efficient**: Riusa conoscenza, minimizza ripetizioni
- ✅ **Deterministico**: Script sostituiscono prompt probabilistici
- ✅ **Auto-Migliorante**: Gli agenti imparano e accumulano conoscenza
- ✅ **Zero-Friction**: Setup in linguaggio naturale, nessun comando

---

**Version**: 1.0.0  
**Author**: Andrea Mazzarotto  
**License**: MIT
