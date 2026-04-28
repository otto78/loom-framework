# TaskFlow API

## Goal
A REST API for managing personal tasks and projects.
The API allows users to create, update, and track tasks with deadlines and priorities.

## Stack
- Backend: Python 3.11 / FastAPI
- Database: PostgreSQL (via SQLAlchemy + asyncpg)
- Auth: JWT (python-jose)
- Testing: pytest + httpx
- Hosting: Render.com (free tier → paid when needed)

## Architecture
- Stateless REST API, no frontend
- All business logic in service layer (not in routes)
- Async throughout (FastAPI + asyncpg)
- Pydantic v2 for validation

## Rules
- Every endpoint must have a corresponding test
- No direct DB queries in routes — always go through services
- All functions must have docstrings
- Use conventional commits: feat/fix/docs/refactor/test
- Never commit .env or secrets

## Notes
- The project uses Loom Framework for AI-assisted development
- All tasks tracked in docs/TASKS.md
- Agent context always loaded from AGENT.md via "read loom"
