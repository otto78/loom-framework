# Loom Framework — Quick Start 🚀

Get started with Loom in 5 minutes!

---

## 📦 Installation

### Option 1: Clone Repository

```bash
git clone https://github.com/yourusername/loom-framework.git
cd loom-framework
```

### Option 2: Download ZIP

Download from [GitHub Releases](https://github.com/yourusername/loom-framework/releases) and extract.

---

## ⚡ Setup Your Project

### Method 1: Interactive Wizard (Recommended)

```bash
cd /path/to/your-project
python /path/to/loom-framework/loom/scripts/setup.py
```

The wizard will:
1. Detect your programming languages
2. Detect your frameworks
3. Detect your IDEs
4. Create all necessary files

### Method 2: Natural Language

Tell your AI agent:

```
"setup loom framework"
```

Done! The agent executes everything automatically.

### Method 3: Automated

```bash
python loom/scripts/setup.py --auto --project-name "MyProject" --ide windsurf,cursor
```

---

## 📋 Your First Task

### Start a Task

```bash
python loom/scripts/task.py start TASK-001 "Implement user login"
```

Or tell your AI agent:

```
"start task TASK-001 'implement user login'"
```

### Work on the Task

1. Read `AGENT.md` for project context
2. Follow the 3-level framework:
   - Check `loom/directives/` for SOPs
   - Use `loom/execution/` for scripts
3. Make commits as you work

### Complete the Task

```bash
python loom/scripts/task.py complete TASK-001 "Login implemented" --bump patch
```

Or tell your AI agent:

```
"complete task TASK-001"
```

---

## 🧪 TDD Workflow (Optional)

For critical features, use Test-Driven Development:

```bash
# Start TDD task
python loom/scripts/task-tdd.py start TASK-001 "Add email validation"

# Write tests (they should fail - Red phase)
# Implement feature (tests pass - Green phase)

# Run tests
python loom/scripts/task-tdd.py test

# Complete when tests pass
python loom/scripts/task-tdd.py complete TASK-001
```

Or with natural language:

```
"start TDD task TASK-001 'add email validation'"
"run tests"
"complete task TASK-001"
```

---

## 📚 Key Files

After setup, you'll have:

- **`AGENT.md`** — Source of truth for your project (customize this!)
- **`docs/TASKS.md`** — Active tasks
- **`docs/BACKLOG.md`** — Future ideas
- **`docs/STORY.md`** — Project history
- **`docs/CHANGELOG.md`** — Version history
- **IDE config files** — `.windsurfrules`, `.cursorrules`, etc.

---

## 🎯 Daily Workflow

```bash
# Morning: Check tasks
python loom/scripts/task.py list

# Start working
python loom/scripts/task.py start TASK-042 "Fix login bug"

# Work on it...

# Complete
python loom/scripts/task.py complete TASK-042 "Bug fixed" --bump patch

# Evening: Update handoff
# Edit docs/HANDOFF.md with current status
```

Or with natural language:

```
"list tasks"
"start task TASK-042 'fix login bug'"
[work on it]
"complete task TASK-042"
```

---

## 🎨 IDE Support

Loom works with:
- **Windsurf** — `.windsurfrules`
- **Claude Code** — `CLAUDE.md`
- **Cursor** — `.cursorrules`
- **Gemini CLI** — `GEMINI.md`
- **VS Code (Cline)** — `.clinerules`
- **GitHub Copilot** — `.github/copilot-instructions.md`
- **IntelliJ IDEA** — `.idea/agentic-framework.md`

All configured automatically by the setup wizard!

---

## 💡 Tips

### 1. Customize AGENT.md
This is your project's source of truth. Add:
- Project goals
- Tech stack details
- Specific rules
- Architecture decisions

### 2. Use BACKLOG.md
Don't create tasks immediately. Add ideas to BACKLOG.md first, then convert to tasks when ready.

### 3. Follow the 3-Level Framework
- **Directives** (what to do) → `loom/directives/`
- **Orchestration** (how to decide) → AI agent
- **Execution** (do the work) → `loom/execution/`

### 4. Use Natural Language
Don't memorize commands. Just talk to your AI agent:
- "setup loom"
- "start task"
- "run tests"
- "complete task"

---

## 📖 Next Steps

- **[README.md](./README.md)** — Full documentation
- **[NATURAL-LANGUAGE-GUIDE.md](./NATURAL-LANGUAGE-GUIDE.md)** — Use framework by talking
- **[TDD-WORKFLOW.md](./TDD-WORKFLOW.md)** — Test-Driven Development guide
- **[docs/framework-guide.md](./docs/framework-guide.md)** — 3-level architecture

---

## 🆘 Need Help?

- **Issues**: [GitHub Issues](https://github.com/yourusername/loom-framework/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/loom-framework/discussions)
- **Documentation**: [loom-framework.dev](https://loom-framework.dev)

---

**That's it! You're ready to weave intelligent agents into your workflow.** 🧵

**Version**: 1.0.0  
**Time to setup**: ~5 minutes  
**Time to first task**: ~2 minutes
