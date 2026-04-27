# Setup Instructions — For AI Agents

> **IMPORTANT:** This file is read by AI agents to understand how to setup the framework.
> When a user says "setup agentic framework" or similar, follow these instructions.

---

## 🤖 For AI Agents: How to Setup Framework

### User Trigger Phrases

When user says any of these:
- "setup agentic framework"
- "configure agentic framework"
- "initialize agentic framework"
- "avvia il framework"
- "configura il framework"
- "inizializza il framework"

**→ Execute the setup wizard automatically**

---

## 📋 Setup Procedure

### Step 1: Detect Project Context

Before running setup, gather information:

```python
# You should detect:
project_root = current_working_directory
languages = detect_languages()  # Python, JavaScript, etc.
frameworks = detect_frameworks()  # FastAPI, React, etc.
existing_ides = detect_ide_configs()  # .cursorrules, .windsurfrules, etc.
existing_docs = check_existing_docs()  # TASKS.md, README.md, etc.
```

### Step 2: Ask User Confirmation

Present detected information and ask:

```
I detected:
- Project: [project_name]
- Languages: [python, javascript]
- Frameworks: [fastapi, react]
- IDEs in use: [cursor, vscode]
- Existing docs: [TASKS.md, README.md]

Do you want me to setup Agentic Framework for this project? (yes/no)
```

### Step 3: Run Setup Wizard

If user confirms, execute:

```bash
python agentic-framework/scripts/setup.py --auto --project-name "[detected_name]" --ide [detected_ides]
```

**OR** if user wants interactive mode:

```bash
python agentic-framework/scripts/setup.py
```

### Step 4: Report Results

After setup completes, tell user:

```
✅ Agentic Framework setup complete!

Created files:
- AGENT.md (customize this with your project details)
- .windsurfrules (Windsurf configuration)
- .cursorrules (Cursor configuration)
- docs/TASKS.md (task tracking)
- docs/BACKLOG.md (ideas and future work)
- docs/STORY.md (project history)
- docs/CHANGELOG.md (version history)
- docs/HANDOFF.md (handoff protocol)

Next steps:
1. Review and customize AGENT.md
2. Start your first task: "start task TASK-001 'description'"
3. Read agentic-framework/QUICKSTART.md for more info
```

---

## 🎯 Task Management Commands

After setup, user can use natural language for task management:

### Starting a Task

**User says:**
- "start task TASK-001 'implement feature X'"
- "avvia task TASK-001 'implementa feature X'"
- "create new task for feature X"

**You execute:**
```bash
python agentic-framework/scripts/task.py start TASK-001 "implement feature X"
```

### Listing Tasks

**User says:**
- "list tasks"
- "show tasks"
- "what tasks are active"
- "mostra i task"

**You execute:**
```bash
python agentic-framework/scripts/task.py list
```

### Completing a Task

**User says:**
- "complete task TASK-001"
- "finish task TASK-001"
- "completa task TASK-001"

**You execute:**
```bash
python agentic-framework/scripts/task.py complete TASK-001 "task completed" --bump patch
```

### TDD Workflow

**User says:**
- "start TDD task TASK-001 'add email validation'"
- "create task with TDD for email validation"

**You execute:**
```bash
python agentic-framework/scripts/task-tdd.py start TASK-001 "add email validation"
```

**User says:**
- "run tests"
- "esegui i test"

**You execute:**
```bash
python agentic-framework/scripts/task-tdd.py test
```

---

## 📝 Example Conversation

### Setup Phase

```
User: "setup agentic framework"

Agent: "I detected:
- Project: MyProject
- Languages: Python, JavaScript
- Frameworks: FastAPI, React
- IDEs in use: Cursor, VS Code

Do you want me to setup Agentic Framework for this project?"

User: "yes"

Agent: [executes setup.py]

Agent: "✅ Setup complete! I created:
- AGENT.md (customize with your project details)
- .cursorrules (Cursor configuration)
- .clinerules (VS Code configuration)
- docs/TASKS.md, BACKLOG.md, STORY.md, CHANGELOG.md, HANDOFF.md

Would you like me to help you customize AGENT.md now?"
```

### Task Management Phase

```
User: "start task TASK-001 'implement user authentication'"

Agent: [executes task.py start]

Agent: "✅ Task TASK-001 started!
Status: In Progress
File: docs/TASKS.md updated

Would you like to use TDD workflow for this task? (recommended for critical features)"

User: "yes, use TDD"

Agent: [executes task-tdd.py start]

Agent: "🧪 TDD workflow started!
Created test file: tests/test_task_001.py

Next steps:
1. Write tests in tests/test_task_001.py (they should fail - Red phase)
2. Tell me 'run tests' to verify they fail
3. Implement the feature
4. Tell me 'run tests' again to verify they pass
5. Tell me 'complete task TASK-001' when done"
```

---

## 🔧 Command Mapping

Map natural language to commands:

| User Says | Execute |
|-----------|---------|
| "setup framework" | `python agentic-framework/scripts/setup.py` |
| "start task TASK-XXX 'desc'" | `python agentic-framework/scripts/task.py start TASK-XXX "desc"` |
| "start TDD task TASK-XXX 'desc'" | `python agentic-framework/scripts/task-tdd.py start TASK-XXX "desc"` |
| "list tasks" | `python agentic-framework/scripts/task.py list` |
| "run tests" | `python agentic-framework/scripts/task-tdd.py test` |
| "complete task TASK-XXX" | `python agentic-framework/scripts/task.py complete TASK-XXX "done"` |
| "sync configs" | `bash agentic-framework/scripts/sync-configs.sh` |

---

## 🎨 IDE-Specific Instructions

### For Windsurf
Read `.windsurfrules` which includes:
- Always read `AGENT.md` at session start
- Use task management commands
- Follow 3-level framework

### For Cursor
Read `.cursorrules` which includes:
- Use @AGENT.md for context
- Task management via natural language
- Composer for multi-file tasks

### For Claude Code
Read `CLAUDE.md` which includes:
- Add AGENT.md to project context
- Use Artifacts for code generation
- Task management commands

### For VS Code (Cline)
Read `.clinerules` which includes:
- Use workspace for context
- @-mentions for files
- Task management via chat

### For IntelliJ IDEA
Read `.idea/agentic-framework.md` which includes:
- AI Assistant integration
- Run configurations for scripts
- Task management via terminal

---

## ⚠️ Important Notes

### 1. Always Read AGENT.md First
Before any work, read `AGENT.md` to understand:
- Project context
- Tech stack
- Specific rules
- Framework architecture

### 2. Respect Existing Files
If files already exist (TASKS.md, README.md, etc.), don't overwrite them.
The setup wizard will skip existing files automatically.

### 3. Suggest TDD for Critical Features
When user starts a task for:
- Authentication
- Payment processing
- Data validation
- Security features

Suggest using TDD workflow:
```
"This is a critical feature. Would you like to use TDD workflow? 
It ensures 100% test coverage and better design."
```

### 4. Auto-Sync After AGENT.md Changes
If user modifies `AGENT.md`, suggest:
```
"I noticed you modified AGENT.md. Should I sync IDE configurations?
This ensures all IDE configs are up to date."
```

Then execute:
```bash
bash agentic-framework/scripts/sync-configs.sh
```

---

## 🚀 Quick Reference

### Setup (First Time)
```
User: "setup agentic framework"
→ Detect project
→ Ask confirmation
→ Run setup.py
→ Report results
```

### Daily Workflow
```
User: "start task TASK-001 'feature X'"
→ Execute task.py start
→ Update TASKS.md
→ Commit and push

User: "complete task TASK-001"
→ Execute task.py complete
→ Update TASKS.md, STORY.md
→ Commit and push
```

### TDD Workflow
```
User: "start TDD task TASK-001 'feature X'"
→ Execute task-tdd.py start
→ Create test file
→ Run tests (should fail)

User: "run tests"
→ Execute task-tdd.py test
→ Show results

User: "complete task TASK-001"
→ Execute task-tdd.py complete
→ Verify tests pass
→ Update docs
→ Commit and push
```

---

## 📚 Documentation References

When user asks for help:
- **Setup:** Point to `agentic-framework/QUICKSTART.md`
- **TDD:** Point to `agentic-framework/TDD-WORKFLOW.md`
- **Features:** Point to `agentic-framework/FEATURES.md`
- **Architecture:** Point to `agentic-framework/framework/3-level-framework.md`

---

**Version:** 1.0.0  
**For:** AI Agents (Windsurf, Claude, Cursor, Gemini, VS Code, Copilot, IntelliJ)  
**Purpose:** Enable natural language setup and task management
