# TODO — Manual Actions Required

These tasks require manual action and cannot be automated:

## 🔴 HIGH PRIORITY

### Add GitHub Topics
**Where**: https://github.com/otto78/antigravity/settings

**Topics to add** (see `.github/GITHUB-TOPICS.md` for full list):
- `ai-agents`
- `developer-tools`
- `llm`
- `cursor`
- `claude-code`
- `windsurf`
- `tdd`
- `workflow-automation`
- `python`
- `ide-integration`

**Why**: Improves discoverability on GitHub search and explore.

---

### Test docs.html Rendering
**Issue**: Content might not render in browser due to CORS or JS issues.

**How to test**:
1. Open https://otto78.github.io/antigravity/docs.html in browser
2. Check if all sections render correctly
3. Test language switcher (EN/IT)
4. Test dark mode toggle

**If broken**: Check browser console for errors, verify marked.js and highlight.js CDN links.

---

## 🟡 MEDIUM PRIORITY

### Create Good First Issues
**Where**: https://github.com/otto78/antigravity/issues

**Suggested issues**:
1. "Add support for Zed IDE" (use `.github/ISSUE_TEMPLATE/ide-support.md`)
2. "Add example Python project to examples/" (use `.github/ISSUE_TEMPLATE/good-first-issue.md`)
3. "Write unit tests for task.py" (use `.github/ISSUE_TEMPLATE/good-first-issue.md`)
4. "Translate MONOREPO-GUIDE.md to Italian"

**Why**: Invites community contributions and builds engagement.

---

### Add Demo GIF/Video
**Where**: README.md hero section (after badges, before "What Gets Created")

**What to record**:
- Terminal showing: `python antigravity/scripts/setup.py`
- Wizard detecting project
- Files being created
- Natural language command: "start task TASK-001 'implement login'"
- TASKS.md being updated

**Tools**: 
- Windows: ScreenToGif, OBS Studio
- macOS: QuickTime, Kap
- Linux: Peek, SimpleScreenRecorder

**Upload to**: GitHub repo or Imgur, then embed in README

---

## 🟢 NICE TO HAVE

### Register Domain (Optional)
**Domain**: `antigravity.dev`

**Check availability**: https://www.namecheap.com or https://domains.google

**If registered**:
1. Point to GitHub Pages: `otto78.github.io/antigravity`
2. Update all links in README, pyproject.toml, docs
3. Add CNAME file to `/docs` directory

**Cost**: ~$10-15/year

**Note**: Not critical — GitHub Pages URL works fine.

---

### Launch Posts
**Platforms**:
- dev.to — Write article "Introducing Antigravity"
- HackerNews — Submit as "Show HN: Antigravity"
- Reddit r/ClaudeAI — "I built a framework for AI-assisted development"
- Reddit r/cursor — "Antigravity: Multi-IDE AI workflow system"
- Twitter/X — Thread with screenshots

**When**: After adding demo GIF and opening good first issues.

---

## ✅ COMPLETED (Automated)

- [x] Fix placeholder URLs (yourusername → otto78)
- [x] Align IDE count to 7 everywhere
- [x] Add VS Code Insider to IDE tables
- [x] Fix domain links (antigravity.dev → GitHub Pages)
- [x] Add badges to README
- [x] Add "Why Not X?" section
- [x] Add DOE Architecture to landing page
- [x] Add Italian translations to docs.html
- [x] Create issue templates
- [x] Add installer one-liners
- [x] Create MONOREPO-GUIDE.md
- [x] Add `Antigravity status` command
- [x] Populate CHANGELOG.md template
- [x] Move NAME-PROPOSALS.md to .github/
- [x] Add README to tests/ and examples/

---

**Last updated**: 2025-01-XX
