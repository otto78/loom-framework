# Loom Framework — Quick Start 🚀

Get started with Loom in **2 minutes** with zero commands to remember!

---

## ⚡ The Easiest Way (Zero-Friction Setup)

### For New Projects

**4 simple steps:**

1. **Create your project folder**
   ```bash
   mkdir my-awesome-project
   cd my-awesome-project
   ```

2. **Create PROJECT.md** with your project description
   ```bash
   # Create a file called PROJECT.md
   # Add: project name, description, tech stack, goals
   ```

3. **Add Loom to your project**
   ```bash
   git clone https://github.com/otto78/loom-framework.git loom
   # Or download and extract loom/ folder into your project
   ```

4. **Open any IDE and say:**
   ```
   "read loom"
   ```
   
   Or: `"configure loom"`, `"setup loom"`, `"use loom"` — any of these work!

**That's it!** Loom reads all its files, finds your PROJECT.md, and auto-configures everything.

---

### For Existing Projects

**2 simple steps:**

1. **Add Loom to your project**
   ```bash
   cd /path/to/your-existing-project
   git clone https://github.com/otto78/loom-framework.git loom
   ```

2. **Open any IDE and say:**
   ```
   "read loom"
   ```

Loom will ask you where your project description is (or help you create one).

---

## 🎯 What Happens When You Say "Read Loom"?

The AI agent automatically:

1. ✅ Reads all Loom framework files
2. ✅ Finds or creates PROJECT.md (your project description)
3. ✅ Detects your programming languages and frameworks
4. ✅ Detects your IDE (Cursor, Windsurf, VS Code, etc.)
5. ✅ Creates AGENT.md (source of truth)
6. ✅ Creates docs/TASKS.md, STORY.md, CHANGELOG.md
7. ✅ Creates IDE config files (.cursorrules, .windsurfrules, etc.)
8. ✅ Initializes the 3-level framework structure

**Result**: Your project is ready for AI-assisted development!

---

## 📝 Your First Task

Just talk to your AI agent:

```
"start task TASK-001 'implement user login'"
```

The agent will:
- Create the task in TASKS.md
- Track progress automatically
- Update STORY.md as you work
- Maintain context across sessions

---

## 🔄 Daily Workflow

**Morning:**
```
"show me the tasks"
"what's the status of TASK-042?"
```

**During work:**
```
"start task TASK-042 'fix login bug'"
[work on it]
"complete task TASK-042"
```

**Evening:**
```
"update the story with today's progress"
"create handoff notes for tomorrow"
```

**No commands to remember. Just natural language.**

---

## 🧪 TDD Workflow (Optional)

For critical features:

```
"start TDD task TASK-001 'add email validation'"
[agent creates test file]

"run tests"
[tests fail - Red phase]

[you implement the feature]

"run tests"
[tests pass - Green phase]

"complete task TASK-001"
```

---

## 📚 Key Files Created

After "read loom", you'll have:

```
your-project/
├── PROJECT.md          ⭐ Your project description (you create this)
├── AGENT.md            ⭐ Source of truth (auto-generated from PROJECT.md)
├── .cursorrules        IDE config (auto-generated)
├── .windsurfrules      IDE config (auto-generated)
├── CLAUDE.md           IDE config (auto-generated)
├── loom/               Framework files
└── docs/
    ├── TASKS.md        Active tasks (auto-updated)
    ├── BACKLOG.md      Future ideas
    ├── STORY.md        Project history (auto-updated)
    ├── CHANGELOG.md    Version history (auto-updated)
    └── HANDOFF.md      Agent handoff notes
```

---

## 🌍 Multi-Language Support

### English
```
"read loom"
"configure loom"
"start task TASK-001 'description'"
"list tasks"
"run tests"
"complete task TASK-001"
```

### Italiano
```
"leggi loom"
"configura loom"
"avvia task TASK-001 'descrizione'"
"mostra i task"
"esegui i test"
"completa task TASK-001"
```

**Works in any language your AI agent understands!**

---

## 🎨 Supported IDEs

Loom auto-configures for:
- 🌊 **Windsurf** (by Codeium)
- 🤖 **Claude Code**
- ↗️ **Cursor**
- ✨ **Antigravity**
- 💻 **VS Code** (Cline)
- 💡 **IntelliJ IDEA**
- 🐙 **GitHub Copilot**

**Switch between IDEs without losing context!**

---

## 💡 Pro Tips

### 1. Make PROJECT.md Detailed
The more details you add, the better the agent understands your project:
- Project goals and vision
- Tech stack and why you chose it
- Architecture decisions
- Coding standards
- Known issues or constraints

### 2. Use BACKLOG.md for Ideas
Don't create tasks immediately. Add ideas to BACKLOG.md first:
```
"add to backlog: implement dark mode"
"add to backlog: optimize database queries"
```

Convert to tasks when ready:
```
"convert backlog item 'dark mode' to task TASK-010"
```

### 3. Let the Agent Update STORY.md
Don't manually edit STORY.md. Let the agent do it:
```
"update story: completed login feature with OAuth2"
"update story: refactored database layer for better performance"
```

### 4. Use Handoffs Between Sessions
```
"create handoff: working on TASK-042, login bug partially fixed, need to test edge cases tomorrow"
```

Next session:
```
"read handoff"
```

---

## 🔗 Alternative Setup Methods

### Method 2: Interactive Wizard (If You Prefer Commands)

```bash
cd /path/to/your-project
python /path/to/loom-framework/loom/scripts/setup.py
```

### Method 3: Fully Automated

```bash
python loom/scripts/setup.py --auto --project-name "MyProject" --ide windsurf,cursor
```

**But honestly, just saying "read loom" is easier!**

---

## 📖 Next Steps

- **[ABSTRACT.md](./ABSTRACT.md)** — Understand the core concepts
- **[NATURAL-LANGUAGE-GUIDE.md](./NATURAL-LANGUAGE-GUIDE.md)** — All commands you can use
- **[TDD-WORKFLOW.md](./TDD-WORKFLOW.md)** — Test-Driven Development
- **[MONOREPO-GUIDE.md](./MONOREPO-GUIDE.md)** — Using Loom in monorepos
- **[README.md](./README.md)** — Full documentation

---

## 🆘 Need Help?

- **Issues**: [GitHub Issues](https://github.com/otto78/loom-framework/issues)
- **Discussions**: [GitHub Discussions](https://github.com/otto78/loom-framework/discussions)
- **Documentation**: [otto78.github.io/loom-framework](https://otto78.github.io/loom-framework)

---

**That's it! You're ready to weave intelligent agents into your workflow.** 🧵

**Version**: 1.0.0  
**Time to setup**: ~2 minutes  
**Time to first task**: ~30 seconds
