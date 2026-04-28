# Loom Framework — Complete Workflow Guide

> From "read loom" to completed task: the full lifecycle.

---

## Overview

The Loom workflow has three phases:

1. **Setup** — Initialize Loom in your project (once)
2. **Daily Work** — Start, work on, and complete tasks
3. **Handoff** — Pass context between sessions or agents

---

## Phase 1: Setup

### Zero-Friction (Recommended)

```
You:   "read loom"
Agent: Finds PROJECT.md → generates AGENT.md → creates docs/ structure
Agent: "✅ Loom configured! Ready. Try: 'start task TASK-001'"
```

### What Gets Created

```
your-project/
├── AGENT.md              ← Source of truth (from PROJECT.md)
├── .cursorrules          ← IDE config
├── .windsurfrules        ← IDE config
├── CLAUDE.md             ← IDE config
├── ANTIGRAVITY.md        ← IDE config
└── docs/
    ├── TASKS.md          ← Active task tracking
    ├── BACKLOG.md        ← Future ideas
    ├── STORY.md          ← Project history
    ├── CHANGELOG.md      ← Version history
    └── HANDOFF.md        ← Agent handoff notes
```

---

## Phase 2: Daily Work

### Starting a Session

Every new session, the agent reads:

```
1. AGENT.md          → Project context, stack, rules
2. docs/TASKS.md     → What's in progress
3. docs/HANDOFF.md   → Notes from previous session (if any)
```

You don't need to re-explain the project. Just say:

```
"read loom"
```

Or if already configured:

```
"what tasks are active?"
```

---

### Task Lifecycle

#### 1. Start a Task

```
You:   "start task TASK-001 'implement user authentication'"
Agent: python loom/scripts/task.py start TASK-001 "implement user authentication"
Agent: "✅ TASK-001 started. docs/TASKS.md updated."
```

`docs/TASKS.md` is updated to:
```markdown
## 🔄 In Progress

### TASK-001 — Implement user authentication
- **Status**: In Progress
- **Started**: 2026-04-28
- **Branch**: feature/TASK-001-user-auth
```

#### 2. Work on the Task

The agent works normally. At any point you can check status:

```
"what's the status of TASK-001?"
"list all tasks"
"show me the backlog"
```

#### 3. Complete a Task

```
You:   "complete task TASK-001"
Agent: python loom/scripts/task.py complete TASK-001 "Authentication implemented with OAuth2" --bump minor
Agent: "✅ TASK-001 completed. Version bumped to v1.1.0. Committed and pushed."
```

What happens automatically:
- `docs/TASKS.md` — task moved to Completed
- `docs/STORY.md` — entry added with what was done
- `docs/CHANGELOG.md` — version bumped and changelog updated
- `git commit` + `git push` executed

---

### TDD Workflow (for Critical Features)

```
You:   "start TDD task TASK-002 'add email validation'"

Agent: python loom/scripts/task-tdd.py start TASK-002 "add email validation"
Agent: "🧪 TDD started. Created tests/test_task_002.py"
       "🔴 Red Phase: Write failing tests first."

You:   [write tests in tests/test_task_002.py]

You:   "run tests"
Agent: python loom/scripts/task-tdd.py test
Agent: "❌ 3 tests failed — Red phase ✅ (expected)"

You:   [implement the feature]

You:   "run tests"
Agent: "✅ 3 tests passed — Green phase ✅"

You:   "complete task TASK-002"
Agent: python loom/scripts/task-tdd.py complete TASK-002
Agent: "🎉 TASK-002 completed with TDD. All tests passing."
```

---

### Managing the Backlog

```
"add to backlog: implement dark mode"
"add to backlog: optimize database queries for 10x performance"
"show backlog"
"convert backlog item 'dark mode' to task TASK-010"
```

---

### Syncing IDE Configurations

If you update `AGENT.md` directly, sync all IDE configs:

```
"sync configs"
Agent: bash loom/scripts/sync-configs.sh
Agent: "✅ All 7 IDE configurations synced."
```

---

## Phase 3: Handoff

### End of Session

Before stopping, create a handoff note:

```
"create handoff: worked on TASK-042 login bug, 
 fixed the token expiry issue, still need to 
 test edge case with expired refresh tokens"
```

`docs/HANDOFF.md` is updated automatically.

### Next Session (Same or Different Agent)

```
"read loom"
"read handoff"
Agent: "Last session: TASK-042, login bug, token expiry fixed.
        Remaining: test expired refresh token edge case.
        Continue?"
```

### Switching IDEs

No action needed. All state is in files:
- `AGENT.md` — works in any IDE
- `docs/TASKS.md` — read by any agent
- `docs/HANDOFF.md` — survives IDE switch

---

## Quick Reference: All Natural Language Commands

### Setup
```
"read loom"          → Initialize/refresh Loom
"configure loom"     → Same as above
"leggi loom"         → Italian equivalent
```

### Tasks
```
"start task TASK-001 'description'"   → Start task
"list tasks"                          → Show active tasks
"show backlog"                        → Show backlog
"complete task TASK-001"              → Complete task
"add to backlog: idea"                → Add to backlog
```

### TDD
```
"start TDD task TASK-001 'desc'"      → TDD task start
"run tests"                           → Run test suite
"complete task TASK-001"              → Complete (checks tests)
```

### Sync & Status
```
"sync configs"        → Sync all IDE configs
"show status"         → Framework status
"read handoff"        → Read last handoff notes
"create handoff: ..." → Create handoff note
```

---

## Script Reference

| Command | Script | When to Use |
|---------|--------|------------|
| `start task` | `loom/scripts/task.py start` | Normal tasks |
| `complete task` | `loom/scripts/task.py complete` | Normal completion |
| `start TDD task` | `loom/scripts/task-tdd.py start` | Critical features |
| `run tests` | `loom/scripts/task-tdd.py test` | During TDD |
| `sync configs` | `loom/scripts/sync-configs.sh` | After AGENT.md changes |
| `read loom` | `loom/scripts/read_loom.py` | Session start |
| `setup` | `loom/scripts/setup.py` | First-time setup |

---

## Related Documentation

- **[QUICKSTART.md](../QUICKSTART.md)** — 2-minute start
- **[framework-guide.md](./framework-guide.md)** — 3-level architecture
- **[TDD-WORKFLOW.md](../TDD-WORKFLOW.md)** — Full TDD guide
- **[NATURAL-LANGUAGE-GUIDE.md](../NATURAL-LANGUAGE-GUIDE.md)** — All commands

---

**Version**: 1.0.0  
**Framework**: Loom Framework v1.0
