# Loom Framework — Monorepo Usage Guide

> How to use Loom in monorepo projects (multiple packages/services in one repository)

---

## What is a Monorepo?

A monorepo contains multiple projects/packages in a single repository:

```
monorepo/
├── packages/
│   ├── frontend/
│   ├── backend/
│   └── shared/
├── services/
│   ├── api/
│   └── worker/
└── tools/
```

---

## Loom in Monorepos — Two Approaches

### Approach 1: Root-Level Loom (Recommended)

Setup Loom at the repository root to manage the entire monorepo as one project.

```bash
cd /path/to/monorepo
python /path/to/loom-framework/loom/scripts/setup.py
```

**Result:**
```
monorepo/
├── AGENT.md              # ⭐ Describes entire monorepo
├── .cursorrules          # IDE config for whole repo
├── docs/
│   ├── TASKS.md          # All tasks across packages
│   ├── BACKLOG.md
│   └── STORY.md
├── packages/
│   ├── frontend/
│   └── backend/
└── services/
```

**When to use:**
- Packages are tightly coupled
- Single team manages everything
- Shared versioning/releases

---

### Approach 2: Per-Package Loom

Setup Loom independently in each package that needs it.

```bash
cd /path/to/monorepo/packages/frontend
python /path/to/loom-framework/loom/scripts/setup.py

cd /path/to/monorepo/packages/backend
python /path/to/loom-framework/loom/scripts/setup.py
```

**Result:**
```
monorepo/
├── packages/
│   ├── frontend/
│   │   ├── AGENT.md      # Frontend-specific context
│   │   ├── .cursorrules
│   │   └── docs/
│   │       └── TASKS.md  # Frontend tasks only
│   └── backend/
│       ├── AGENT.md      # Backend-specific context
│       ├── .cursorrules
│       └── docs/
│           └── TASKS.md  # Backend tasks only
└── services/
```

**When to use:**
- Packages are independent
- Different teams per package
- Independent versioning/releases

---

## Hybrid Approach (Advanced)

Root-level Loom for coordination + per-package Loom for details.

```
monorepo/
├── AGENT.md              # High-level monorepo overview
├── docs/
│   ├── TASKS.md          # Cross-cutting tasks
│   └── BACKLOG.md        # Monorepo-wide ideas
├── packages/
│   ├── frontend/
│   │   ├── AGENT.md      # Frontend details
│   │   └── docs/
│   │       └── TASKS.md  # Frontend-specific tasks
│   └── backend/
│       ├── AGENT.md      # Backend details
│       └── docs/
│           └── TASKS.md  # Backend-specific tasks
```

**Root AGENT.md** references package-level AGENT.md files:

```markdown
# Monorepo — MyCompany Platform

## Architecture

This monorepo contains:
- `packages/frontend/` — React app (see packages/frontend/AGENT.md)
- `packages/backend/` — FastAPI service (see packages/backend/AGENT.md)
- `services/worker/` — Background jobs

## Cross-Package Tasks

See docs/TASKS.md for tasks that span multiple packages.
For package-specific tasks, see each package's docs/TASKS.md.
```

---

## Task Management in Monorepos

### Root-Level Tasks (Approach 1)

Use prefixes to organize tasks by package:

```markdown
# docs/TASKS.md

## 🚀 In Progress

- [ ] **FE-001**: Implement login UI
  - Package: frontend
  - Priority: High

- [ ] **BE-001**: Add authentication API
  - Package: backend
  - Priority: High

- [ ] **INFRA-001**: Setup CI/CD pipeline
  - Package: root
  - Priority: Medium
```

### Per-Package Tasks (Approach 2)

Each package has independent task IDs:

```markdown
# packages/frontend/docs/TASKS.md
- [ ] **TASK-001**: Implement login UI

# packages/backend/docs/TASKS.md
- [ ] **TASK-001**: Add authentication API
```

No conflicts because they're in separate files.

---

## IDE Configs in Monorepos

### Root-Level IDE Config

`.cursorrules` at root applies to entire monorepo:

```markdown
# .cursorrules

This is a monorepo containing:
- Frontend (React) in packages/frontend/
- Backend (FastAPI) in packages/backend/

When working on frontend, focus on packages/frontend/.
When working on backend, focus on packages/backend/.

See AGENT.md for full context.
```

### Per-Package IDE Config

Each package can override with its own config:

```
packages/frontend/.cursorrules  # Frontend-specific rules
packages/backend/.cursorrules   # Backend-specific rules
```

Most IDEs respect nested configs and use the closest one.

---

## Best Practices

### 1. Choose One Approach Early

Don't mix approaches randomly. Decide based on your team structure.

### 2. Document the Structure

In root `AGENT.md`, explain which approach you're using:

```markdown
## Loom Setup

This monorepo uses **root-level Loom** with task prefixes (FE-, BE-, INFRA-).
All tasks are tracked in root docs/TASKS.md.
```

### 3. Use Task Prefixes (Root-Level)

- `FE-XXX` — Frontend tasks
- `BE-XXX` — Backend tasks
- `INFRA-XXX` — Infrastructure/DevOps
- `SHARED-XXX` — Shared library tasks

### 4. Cross-Reference in Hybrid

Root AGENT.md should link to package AGENT.md files:

```markdown
For detailed context on each package:
- Frontend: [packages/frontend/AGENT.md](packages/frontend/AGENT.md)
- Backend: [packages/backend/AGENT.md](packages/backend/AGENT.md)
```

### 5. Shared Directives

If using 3-level framework, directives can be shared:

```
monorepo/
├── loom/
│   ├── directives/       # Shared across packages
│   │   ├── deploy.md
│   │   └── test.md
│   └── execution/        # Shared scripts
│       ├── deploy.py
│       └── test.py
├── packages/
│   ├── frontend/
│   │   └── loom/
│   │       ├── directives/  # Frontend-specific
│   │       └── execution/
│   └── backend/
│       └── loom/
│           ├── directives/  # Backend-specific
│           └── execution/
```

---

## Example: Root-Level Setup

```bash
# 1. Clone Loom
git clone https://github.com/otto78/loom-framework.git

# 2. Setup at monorepo root
cd /path/to/monorepo
python /path/to/loom-framework/loom/scripts/setup.py

# 3. Start cross-package task
python loom/scripts/task.py start INFRA-001 "Setup CI/CD for all packages"

# 4. Start package-specific tasks
python loom/scripts/task.py start FE-001 "Implement login UI"
python loom/scripts/task.py start BE-001 "Add auth API"
```

---

## Example: Per-Package Setup

```bash
# 1. Setup in frontend
cd /path/to/monorepo/packages/frontend
python /path/to/loom-framework/loom/scripts/setup.py

# 2. Setup in backend
cd /path/to/monorepo/packages/backend
python /path/to/loom-framework/loom/scripts/setup.py

# 3. Work on frontend
cd packages/frontend
python loom/scripts/task.py start TASK-001 "Implement login UI"

# 4. Work on backend
cd packages/backend
python loom/scripts/task.py start TASK-001 "Add auth API"
```

---

## Troubleshooting

### "Which AGENT.md should the agent read?"

**Root-level approach:** Always read root `AGENT.md` first.

**Per-package approach:** Agent reads the `AGENT.md` in the package it's working on.

**Hybrid approach:** Agent reads root `AGENT.md`, then follows links to package-specific ones.

### "Task IDs conflict between packages"

Use prefixes (FE-, BE-) or switch to per-package Loom.

### "IDE config not applying to subpackage"

Some IDEs only read root config. Create package-specific config or use root config with conditional rules.

---

## Summary

| Aspect | Root-Level | Per-Package | Hybrid |
|--------|------------|-------------|--------|
| Setup complexity | Low | Medium | High |
| Task tracking | Centralized | Distributed | Both |
| Best for | Tightly coupled | Independent packages | Large teams |
| Task ID strategy | Prefixes (FE-, BE-) | Independent | Both |

**Recommendation:** Start with **root-level** for most monorepos. Switch to per-package only if packages are truly independent.

---

**Version:** 1.0.0  
**Last updated:** 2025-01-XX
