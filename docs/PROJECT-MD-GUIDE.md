# 📋 PROJECT.md — The Foundation of LOOM

## What is PROJECT.md?

**PROJECT.md** is the **single source of truth** for your project. It tells LOOM:
- What your project does (Goal)
- Your tech stack (technologies)
- Your architectural decisions (design rules)
- Rules agents MUST follow (code standards)
- Project-specific constraints (gotchas, limits)

When you tell an agent **"read loom"**, it will:
1. Find the `loom/` framework folder
2. Read your `PROJECT.md`
3. Auto-configure based on YOUR project's needs
4. Create `TASKS.md`, `STORY.md`, `HANDOFF.md` with your context
5. Follow YOUR rules for all subsequent work

---

## Why PROJECT.md Matters

**Without PROJECT.md**:
- Agent has generic context
- Agent makes assumptions about your project
- Agent might violate your architecture
- Agent doesn't know your rules or constraints
- Context resets between sessions

**With PROJECT.md**:
- ✅ Agent understands your project immediately
- ✅ Agent respects your architectural decisions
- ✅ Agent follows your specific rules
- ✅ Rules persist across context resets
- ✅ Deterministic behavior (90% accuracy over 10+ steps)

---

## Real-World Examples

### Example 1: FastAPI REST API

```markdown
# TaskFlow API

## Goal
REST API for personal task management. Users create, update, and track tasks with deadlines, priorities, and team collaboration.

## Stack
- Backend: Python 3.11 + FastAPI
- Database: PostgreSQL 15 (asyncpg + SQLAlchemy v2)
- Auth: JWT (python-jose)
- Testing: pytest + httpx
- Hosting: Render.com
- CI/CD: GitHub Actions

## Architecture
- Stateless REST API (no frontend)
- Business logic ONLY in service layer
- Async/await throughout (FastAPI + asyncpg)
- Pydantic v2 for validation
- Models → Services → Routes pattern

## Rules
- Every endpoint MUST have a test
- NO direct DB queries in routes (use services)
- ALL functions MUST have docstrings
- Commit format: feat/fix/docs: description [TASK-XXX]
- NEVER use git add -A (use selective commits)
- NEVER commit .env or secrets
- Type hints required on all functions

## Notes
- DB has 2M user records: avoid unindexed queries
- Stripe webhooks require stripe-cli for local testing
- Rate limit: 100 req/min per user token
- API versioning: all endpoints start with /api/v1/
```

### Example 2: React + Next.js Frontend

```markdown
# EcoTracker Dashboard

## Goal
Web dashboard for environmental impact tracking. Real-time data visualization, report generation, team collaboration features.

## Stack
- Frontend: React 18 + Next.js 14 (App Router)
- UI: Tailwind CSS + shadcn/ui
- State: Zustand
- API: TanStack Query (React Query)
- Testing: Vitest + @testing-library/react
- Hosting: Vercel
- Analytics: Vercel Web Analytics

## Architecture
- Next.js App Router (Server Components by default)
- Client Components only where interaction needed
- API routes as proxy only (business logic in backend)
- Zustand stores in lib/stores/
- Custom hooks in lib/hooks/
- SPA with real-time data via WebSockets

## Rules
- Component names: PascalCase
- Utility functions: camelCase
- Use Server Components by default
- Props interface: interface ComponentProps { ... }
- ALL components MUST have tests
- NO CSS files — Tailwind only
- Color palette: 6 semantic colors (tailwind.config.js)
- Mobile-first responsive design

## Notes
- Dark mode: Next.js theme detection
- Breakpoints: sm/md/lg/xl
- Rate limit: 100 requests/minute per session
- Stripe integration on checkout page
```

### Example 3: Python Package Library

```markdown
# TextProcessor

## Goal
Open-source Python library for NLP text processing: tokenization, sentiment analysis, entity extraction. 50k+ monthly downloads.

## Stack
- Language: Python 3.8+
- Testing: pytest + pytest-cov
- Documentation: Sphinx + ReadTheDocs
- Packaging: setuptools + build
- Versioning: Semantic versioning (MAJOR.MINOR.PATCH)

## Architecture
- Single-responsibility principle: each module does ONE thing
- NO external dependencies (optional: numpy, torch)
- Pluggable backends: swap NLP engines
- Pure Python implementation (no Cython yet)
- Performance-critical paths documented

## Rules
- Type hints on ALL public functions
- 100% test coverage on core modules
- NO breaking changes in minor versions
- Documentation updated with every feature
- Conventional commits
- Wheels built for: Python 3.8, 3.9, 3.10, 3.11, 3.12

## Notes
- API frozen at v1.0: breaking changes only in major
- Performance critical: all O(n) algorithms documented
- Thread-safe: uses RLock for state
- Wheels built automatically by CI
```

---

## How to Write PROJECT.md

### Step 1: Goal (2-3 sentences)
❌ "A web application"
✅ "REST API for real-time task management with JWT auth, team collaboration, and email notifications"

### Step 2: Stack (Be specific with versions)
❌ "Python, JavaScript, Postgres"
✅ 
```
- Backend: Python 3.11 + FastAPI
- Database: PostgreSQL 15 (asyncpg + SQLAlchemy v2)
- Frontend: React 18 + Next.js 14
```

### Step 3: Architecture (3-5 key decisions)
❌ "Modular"
✅
```
- Stateless REST API
- Business logic only in services
- Models → Services → Routes pattern
- Async throughout
```

### Step 4: Rules (MUST-FOLLOW, be specific)
❌ "Follow best practices"
✅
```
- Every endpoint MUST have a test
- NO direct DB queries in routes
- Commit format: feat/fix: description [TASK-XXX]
- NEVER use git add -A
```

### Step 5: Notes (Constraints, gotchas, past decisions)
❌ "Some stuff is complex"
✅
```
- DB has 5M records: avoid unindexed queries
- Stripe webhooks require stripe-cli locally
- API rate limit: 100 req/min per token
```

---

## AI Agent Prompts for PROJECT.md

### Prompt 1: Getting Help Writing It
```
"Help me write PROJECT.md for my project.
I'll answer questions about:
1. What does this project do?
2. What stack are you using?
3. What are 3-5 key architectural decisions?
4. What rules MUST be followed?
5. What constraints exist?"
```

### Prompt 2: Auto-Generate from Codebase
```
"Analyze my codebase and create a draft PROJECT.md.
Look at:
- package.json / pyproject.toml (detect stack)
- README.md (extract goal)
- Code structure (infer architecture)
- Tests and CI config (detect rules)

Then show me the draft so I can edit it."
```

### Prompt 3: Refine Existing PROJECT.md
```
"Review my PROJECT.md for:
- Is the Goal clear and specific?
- Are Stack versions complete?
- Are architectural rules actionable?
- Did I miss important constraints?
- Would an agent understand this?"
```

---

## Common Sections to Add

### Performance / Prestazioni
```markdown
## Performance
- API p95 response: < 200ms
- DB query max: < 1 second
- Cache TTL: 5 minutes
- Max page size: 100 items
```

### Security / Sicurezza
```markdown
## Security
- Password: min 12 chars, 3 types
- Rate limit: 100 req/min per IP
- HTTPS only in production
- CORS: specific domains only
```

### Dependencies / Dipendenze
```markdown
## Dependencies
- Lock ALL versions (requirements.txt / package-lock.json)
- NO major version bumps without approval
- Monthly security audits required
```

### Development Setup / Setup Sviluppo
```markdown
## Development Setup
- Python venv required
- Run: `make setup` to initialize
- DB: `alembic upgrade head`
- Tests: `pytest tests/`
- Local server: `make dev`
```

---

## ✅ Quality Checklist

Your PROJECT.md is good if:
- ✅ Goal is 2-3 sentences, crystal clear
- ✅ Stack has specific versions
- ✅ Architecture lists actual decisions (not buzzwords)
- ✅ Rules are MUST-FOLLOW (not suggestions)
- ✅ Constraints are documented (DB size, rate limits, gotchas)
- ✅ Bilingual if needed (EN/IT)
- ✅ 50-80 lines total (concise, not rambling)

---

## Next Steps

1. **Copy template**: `loom/templates/PROJECT.md.template`
2. **Fill in your details**: Goal, Stack, Architecture, Rules, Notes
3. **Save** as `PROJECT.md` in your project root
4. **Commit** to git
5. **Tell agent**: "read loom" or "leggi loom"
6. **Agent auto-configures** based on YOUR PROJECT.md! 🎯

---

## Related Files (Auto-Created by LOOM)

| File | Purpose |
|------|---------|
| **LOOM.md** | Framework configuration (auto-created) |
| **AGENT.md** | Project context for agents (auto-created) |
| **TASKS.md** | Task tracking system (auto-created) |
| **STORY.md** | Operational history (auto-created) |
| **HANDOFF.md** | Multi-IDE handoff protocol (auto-created) |

---

**Remember**: PROJECT.md is YOUR voice telling the agent what to care about.  
Make it clear, make it specific, and the agent will deliver amazing work! 🧵
