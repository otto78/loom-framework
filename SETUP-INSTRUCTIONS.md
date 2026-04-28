# Setup Instructions — For AI Agents

> **IMPORTANT:** This file is read by AI agents to understand how to setup the framework.
> When a user says "read loom", "leggi loom", "setup loom" or similar, follow these instructions.

---

## 🤖 For AI Agents: How to Setup Loom

### User Trigger Phrases

When user says any of these:
- "read loom" / "leggi loom"
- "setup loom" / "configure loom"
- "inizializza loom" / "usa loom"
- "configura loom" / "installa loom"

**→ Execute the Zero-Friction Setup procedure automatically**

---

## 📋 Setup Procedure (Zero-Friction)

### Step 1: Detect Project Context & Loom Files

Before running setup, gather information:

1. **Read all files in `loom/`**: Understand the available directives, templates, and scripts.
2. **Search for Project Meta-File**: Look for `PROJECT.md` or `PROGETTO.md` in the root.
3. **Analyze Tech Stack**: Detect languages, frameworks, and existing IDE configs.

### Step 2: Auto-Configuration

If `PROJECT.md` (or `PROGETTO.md`) is found:
1. **Initialize AGENT.md**: Use the content of `PROJECT.md` as the primary source of truth.
2. **Run setup script**:
   ```bash
   python loom/scripts/setup.py --auto --project-name "[detected_name]" --from-project-file PROJECT.md
   ```

If NOT found:
1. **Ask User**: "I detected the `loom/` folder but no `PROJECT.md`. Would you like me to create one or can you point me to a project description?"
2. **Create Template**: Offer to create `PROJECT.md` from the template `loom/templates/PROJECT.md.template`.

### Step 3: Report Results

After setup completes, tell user:

```
✅ Loom configured!

Project: [project_name]
Source of Truth: AGENT.md
Task Tracking: docs/TASKS.md

Ready to start! Try: "start task TASK-001 'description'"
```

---

## 🎯 Task Management Commands

After setup, map natural language to commands:

| User Says | Execute |
|-----------|---------|
| "read loom" | `python loom/scripts/read_loom.py` |
| "setup loom" | `python loom/scripts/setup.py` |
| "start task TASK-XXX 'desc'" | `python loom/scripts/task.py start TASK-XXX "desc"` |
| "start TDD task TASK-XXX 'desc'" | `python loom/scripts/task-tdd.py start TASK-XXX "desc"` |
| "list tasks" | `python loom/scripts/task.py list` |
| "run tests" | `python loom/scripts/task-tdd.py test` |
| "complete task TASK-XXX" | `python loom/scripts/task.py complete TASK-XXX "done"` |
| "sync configs" | `bash loom/scripts/sync-configs.sh` |

---

## ⚠️ Important Notes for Agents

### 1. Always Read AGENT.md First
Before any work, read `AGENT.md` to understand the current project state and rules.

### 2. Respect Persistent Memory
`TASKS.md` and `STORY.md` are the source of truth for the project's progress and history. Always update them after completing a task.

### 3. Multi-Agent Handoff
If you are finishing a session, update `docs/HANDOFF.md` so the next agent can resume seamlessly.

### 4. Suggest TDD for Critical Features
When starting tasks related to security, auth, or core logic, always suggest using TDD.

---

**Version:** 1.0.0  
**For:** AI Agents (Windsurf, Claude, Cursor, Gemini, VS Code, Copilot, IntelliJ)  
**Purpose:** Enable zero-friction setup and persistent task management.
