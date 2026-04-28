# TASKS — TaskFlow API

> **How to use**: Tell your agent "list tasks", "start task TASK-XXX", "complete task TASK-XXX"

---

## 🔄 In Progress

### TASK-001 — Set up FastAPI project structure
- **Status**: In Progress
- **Started**: 2026-04-28
- **Branch**: `feat/TASK-001-project-setup`
- **Description**: Initialize FastAPI app, SQLAlchemy async setup, Pydantic v2 schemas, basic health endpoint.
- **Tests**: `tests/test_health.py`

---

## 📋 Not Started

### TASK-002 — Implement task CRUD endpoints
- **Status**: Not Started
- **Description**: POST /api/v1/tasks, GET /api/v1/tasks, GET /api/v1/tasks/{id}, PUT /api/v1/tasks/{id}, DELETE /api/v1/tasks/{id}
- **Approach**: TDD — write tests first

### TASK-003 — Add JWT authentication
- **Status**: Not Started
- **Description**: POST /api/v1/auth/register, POST /api/v1/auth/login, JWT middleware on protected routes
- **Approach**: TDD

### TASK-004 — Deploy to Render.com
- **Status**: Not Started
- **Description**: Create render.yaml, configure PostgreSQL instance, set environment variables, verify health endpoint

---

## ✅ Completed

*(no completed tasks yet — project just started)*

---

## 📝 Notes

- All tasks use TDD where possible (tests before implementation)
- Commit format: `feat/fix/docs/test/refactor: description [TASK-XXX]`
- Update this file at the start and end of every session

---

**Last updated**: 2026-04-28  
**Active**: 1 | **Not started**: 3 | **Completed**: 0
