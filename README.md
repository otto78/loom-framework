# Loom Framework 🧵

> **Weave intelligent agents into your development workflow**

A complete operational framework for AI-powered development across multiple IDEs. Loom provides structure, automation, and best practices for teams working with AI agents.

---

## 🎯 What is Loom?

Loom is an operational framework that brings structure to AI-assisted development. It provides:

- ⚡ **Quick Setup** — Interactive wizard + automated scripts
- 🤖 **Multi-IDE Support** — 7 IDEs (Windsurf, Claude, Cursor, Gemini, VS Code, Copilot, IntelliJ)
- 📋 **Task Management** — Complete system with TASKS.md + BACKLOG.md
- 🧪 **TDD Workflow** — Test-Driven Development integrated
- 📝 **Integrated Versioning** — Automatic STORY.md + CHANGELOG.md
- 🔄 **Automated Workflow** — Python scripts for complete task lifecycle
- 📚 **3-Level Framework** — Directives / Orchestration / Execution
- 🔀 **Handoff Protocol** — Seamless agent-to-agent transitions
- 🧩 **Adaptable** — Works with new and existing projects

---

## 🚀 Quick Start

### Method 1: Interactive Wizard (Recommended)

```bash
# 1. Clone Loom
git clone https://github.com/yourusername/loom-framework.git

# 2. Run setup wizard in your project
cd /path/to/your-project
python /path/to/loom-framework/loom/scripts/setup.py

# The wizard will automatically detect:
# - Programming languages
# - Frameworks in use
# - IDEs configured
# And create all necessary files
```

### Method 2: Natural Language (with AI Agent)

Simply tell your AI agent:

```
"setup loom framework"
```

The agent will automatically execute the setup wizard!

See **[NATURAL-LANGUAGE-GUIDE.md](./NATURAL-LANGUAGE-GUIDE.md)** for complete guide.

### Method 3: Automated Setup

```bash
# Auto-setup without interaction
python loom/scripts/setup.py --auto

# With specific options
python loom/scripts/setup.py --auto --project-name "MyProject" --ide windsurf,cursor,intellij
```

---

## 📋 Natural Language Commands

After setup, use natural language with your AI agent:

```
"start task TASK-001 'implement feature X'"
"list tasks"
"run tests"
"complete task TASK-001"
"sync configs"
```

No need to remember Python script paths or command syntax!

---

## 🏗️ The 3-Level Framework

```
┌─────────────────────────────────────────┐
│ Level 1: DIRECTIVES (What to do)       │
│ directives/*.md — SOPs in natural      │
│ language, objectives, inputs, outputs   │
├─────────────────────────────────────────┤
│ Level 2: ORCHESTRATION (How to decide) │
│ Intelligent routing between directives │
│ and execution scripts                   │
├─────────────────────────────────────────┤
│ Level 3: EXECUTION (Do the work)       │
│ execution/*.py — Deterministic scripts │
│ Environment variables in .env           │
└─────────────────────────────────────────┘
```

**Why it works**: LLMs are probabilistic (90% accuracy = 59% over 5 steps).
Pushing complexity into deterministic code reduces errors.

---

## 📁 Structure

```
loom-framework/
├── README.md                          # This guide
├── docs/
│   ├── setup-guide.md                 # Complete setup guide
│   ├── workflow-guide.md              # Task workflow guide
│   ├── framework-guide.md             # 3-level framework
│   └── templates/                     # Documentation templates
│       ├── TASKS.md                   # Task tracking
│       ├── BACKLOG.md                 # Future ideas
│       ├── STORY.md                   # Operational history
│       ├── CHANGELOG.md               # Detailed changelog
│       └── HANDOFF.md                 # Handoff protocol
│
├── loom/
│   ├── scripts/                       # Automation scripts
│   │   ├── task.py                    # Task workflow manager ⭐
│   │   ├── task-tdd.py                # TDD workflow ⭐
│   │   ├── setup.py                   # Interactive wizard ⭐
│   │   ├── init-project.sh            # Init Unix/Linux/macOS
│   │   ├── init-project.ps1           # Init Windows
│   │   └── sync-configs.sh            # Sync IDE configs
│   │
│   ├── templates/                     # Core templates
│   │   ├── AGENT.md.template          # Project source of truth
│   │   ├── 3-level-framework.md       # Architecture details
│   │   └── coding-standards.md        # Code standards
│   │
│   ├── ide-configs/                   # IDE configurations
│   │   ├── windsurf/                  # .windsurfrules
│   │   ├── claude/                    # CLAUDE.md
│   │   ├── cursor/                    # .cursorrules
│   │   ├── gemini/                    # GEMINI.md
│   │   ├── vscode/                    # .clinerules
│   │   ├── copilot/                   # copilot-instructions.md
│   │   └── intellij/                  # agentic-framework.md
│   │
│   ├── directives/                    # SOPs (Standard Operating Procedures)
│   │   ├── README.md                  # How to write directives
│   │   ├── _template.md               # Template for new directives
│   │   └── coding-standards.md        # Shared standards
│   │
│   └── execution/                     # Deterministic scripts
│       ├── README.md                  # Execution conventions
│       └── _template.py               # Template for new scripts
│
├── examples/                          # Example projects
└── tests/                             # Framework tests
```

---

## 🔄 Task Workflow

### Normal Workflow

```bash
# Initialize system (first time)
python loom/scripts/task.py init

# Start new task
python loom/scripts/task.py start TASK-001 "Implement feature X"

# List active tasks
python loom/scripts/task.py list

# Complete task
python loom/scripts/task.py complete TASK-001 "Feature X implemented" --bump minor
```

### TDD Workflow

```bash
# Start TDD task (create tests first)
python loom/scripts/task-tdd.py start TASK-001 "Add email validation"

# Write tests (should fail - Red phase)
# Implement feature (tests pass - Green phase)

# Run tests
python loom/scripts/task-tdd.py test

# Complete task (only if tests pass)
python loom/scripts/task-tdd.py complete TASK-001
```

---

## 🎨 Supported IDEs

| IDE/Tool | Config File | Location |
|----------|-------------|----------|
| Windsurf | `.windsurfrules` | Root |
| Claude Code | `CLAUDE.md` | Root |
| Cursor | `.cursorrules` | Root |
| Gemini CLI | `GEMINI.md` | Root |
| GitHub Copilot | `copilot-instructions.md` | `.github/` |
| Cline (VS Code) | `.clinerules` | Root |
| IntelliJ IDEA | `agentic-framework.md` | `.idea/` |

---

## 📚 Documentation

- **[QUICKSTART.md](./QUICKSTART.md)** — 5-minute quick start
- **[NATURAL-LANGUAGE-GUIDE.md](./NATURAL-LANGUAGE-GUIDE.md)** — Use framework by talking
- **[TDD-WORKFLOW.md](./TDD-WORKFLOW.md)** — Test-Driven Development guide
- **[SETUP-INSTRUCTIONS.md](./SETUP-INSTRUCTIONS.md)** — For AI agents
- **[docs/framework-guide.md](./docs/framework-guide.md)** — 3-level architecture
- **[docs/workflow-guide.md](./docs/workflow-guide.md)** — Complete workflow guide

---

## 🌟 Why Loom?

### Before Loom
- ❌ Inconsistent AI agent behavior
- ❌ No task tracking
- ❌ Manual documentation updates
- ❌ Lost context between sessions
- ❌ No testing workflow

### After Loom
- ✅ Structured agent workflows
- ✅ Automatic task management
- ✅ Auto-updated documentation
- ✅ Seamless handoffs
- ✅ Integrated TDD workflow

---

## 🤝 Contributing

Loom is a living system. Improve it continuously:
- Add new IDEs when you use them
- Refine standards when you discover better patterns
- Extend the framework when you need more structure
- Share improvements with the community

**Guiding principle**: Every project using Loom should improve it for future projects.

---

## 📝 License

MIT — Use, modify, share freely.

---

## 🔗 Links

- **Website**: [loom-framework.dev](https://loom-framework.dev)
- **Documentation**: [docs.loom-framework.dev](https://docs.loom-framework.dev)
- **GitHub**: [github.com/yourusername/loom-framework](https://github.com/yourusername/loom-framework)
- **Issues**: [github.com/yourusername/loom-framework/issues](https://github.com/yourusername/loom-framework/issues)

---

**Version**: 1.0.0  
**Author**: Andrea Mazzarotto  
**Tagline**: Weave intelligent agents into your development workflow 🧵
