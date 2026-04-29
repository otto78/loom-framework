# AGENT.md — TaskFlow API
# Source of Truth / Fonte di Verità

> This file is read by all AI agents (Claude, Cursor, Windsurf, loom, VS Code Insider, Cline).
> Do not duplicate these instructions in other files — they all reference here.

---

## What is TaskFlow API

A REST API for managing personal tasks and projects. Allows users to create, update, and track tasks with deadlines and priorities.

**Stack**: Python 3.11 / FastAPI / PostgreSQL / JWT  
**Hosting**: Render.com  
**Principle**: Business logic in services, not routes. Always async. Every endpoint has a test.

---

## Tech Stack

### Backend
- **Language**: Python 3.11
- **Framework**: FastAPI (async)
- **Database**: PostgreSQL via SQLAlchemy + asyncpg
- **Auth**: JWT (python-jose)
- **Validation**: Pydantic v2

### Testing
- **Framework**: pytest + httpx (async client)
- **Coverage**: Aim for >80%

### Infrastructure
- **Hosting**: Render.com
- **CI/CD**: GitHub Actions
- **Secrets**: `.env` (never commit)

---

## Project Structure

```
taskflow-api/
├── AGENT.md                    ← this file (source of truth)
├── PROJECT.md                  ← project description
├── docs/
│   ├── TASKS.md                ← task tracking
│   ├── BACKLOG.md              ← future ideas
│   ├── STORY.md                ← project history
│   ├── CHANGELOG.md            ← version changelog
│   └── HANDOFF.md              ← agent handoff notes
│
├── src/
│   ├── main.py                 ← FastAPI app entry point
│   ├── routes/                 ← API endpoints (thin layer)
│   ├── services/               ← business logic (fat layer)
│   ├── models/                 ← SQLAlchemy models
│   └── schemas/                ← Pydantic schemas
│
├── tests/
│   ├── conftest.py             ← shared fixtures
│   └── test_*.py               ← one file per route/service
│
├── loom/                       ← loom
└── .env                        ← secrets (never commit)
```

---

## DOE Architecture

### Level 1 — Directives (`loom/directives/`)
SOPs for each domain: how to add an endpoint, how to write tests, coding standards.

### Level 2 — Orchestration (this agent)
Read directives → choose right approach → call execution scripts → handle errors → update TASKS.md.

### Level 3 — Execution (`loom/execution/`)
Deterministic scripts: `git_commit.py`, `task_status.py`.

---

## Agent Operating Principles

### 1. Routes are thin, Services are fat
```python
# ✅ Correct
@router.post("/tasks")
async def create_task(data: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await task_service.create(db, data)

# ❌ Wrong — business logic in route
@router.post("/tasks")
async def create_task(data: TaskCreate, db: AsyncSession = Depends(get_db)):
    task = Task(**data.dict())
    db.add(task)
    await db.commit()
    return task
```

### 2. Always write the test first (TDD for critical features)
```
"start TDD task TASK-001 'add task creation endpoint'"
```

### 3. Use loom scripts for task management
```bash
python loom/scripts/task.py start TASK-001 "Add task creation endpoint"
python loom/scripts/task.py complete TASK-001 "Endpoint implemented and tested" --bump minor
python loom/scripts/task.py list
```

### 4. Commit only worked files (no git add -A)
```bash
python loom/execution/git_commit.py --files "src/routes/tasks.py,tests/test_tasks.py" --message "feat: add task creation endpoint [TASK-001]"
```

### 5. Always update TASKS.md before ending a session

### 6. Ask before irreversible DB operations

---

## Project-Specific Rules

### API Design
- Use plural nouns for resources: `/tasks`, `/projects`
- Version prefix: `/api/v1/`
- Always return structured JSON errors: `{"detail": "message", "code": "ERROR_CODE"}`

### Database
- Never use sync SQLAlchemy — always `async with AsyncSession`
- All migrations via Alembic, never manual schema changes

### Testing
- Use `pytest.mark.asyncio` for all async tests
- Shared fixtures in `tests/conftest.py`
- Test both success and error cases

---

## Current Status

Read `docs/TASKS.md` for active tasks.  
Read `docs/STORY.md` for project history.  
Read `docs/HANDOFF.md` for last session notes.

---

**Version**: 1.0.0  
**Last updated**: 2026-04-28  
**Framework**: loom v1.0
