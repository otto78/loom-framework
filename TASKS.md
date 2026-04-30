# LOOM FRAMEWORK — IDE Config Refactor

> Refactor completo dei file di configurazione IDE per eliminare la duplicazione con AGENT.md
> e adottare l'architettura GEMINI.md + AGENTS.md corretta.

---

## Ordine di esecuzione

| # | Task | Priorità | Stato |
|---|------|----------|-------|
| 1 | TASK-008 — Fix URL broken (`otto78/loom` → `otto78/loom-framework`) | CRITICA | [ ] |
| 2 | TASK-005 — Fix VS Code: sostituire Cline con GitHub Copilot | CRITICA | [ ] |
| 3 | TASK-003 — Creare `GEMINI.md` per Antigravity (mancante) | ALTA | [ ] |
| 4 | TASK-004 — Aggiornare `AGENTS.md` come file cross-tool | ALTA | [ ] |
| 5 | TASK-001 — Ridurre `CLAUDE.md` al modello minimale | ALTA | [ ] |
| 6 | TASK-002 — Ridurre `.cursorrules` + migrare a `.cursor/rules/loom.mdc` | ALTA | [ ] |
| 7 | TASK-006 — Fix Windsurf: ridurre + `.windsurf/rules/loom.md` | ALTA | [ ] |
| 8 | TASK-007 — Fix IntelliJ: percorso `.aiassistant/rules/` | ALTA | [ ] |
| 9 | TASK-009 — Rimuovere sezione duplicata `natural-lang` in docs.html | ALTA | [ ] |
| 10 | TASK-010 — Aggiungere traduzioni IT mancanti | MEDIA | [ ] |
| 11 | TASK-011 — Aggiornare tabella IDE in docs.html e README | MEDIA | [ ] |

---

## TASK-008 — Fix URL broken

**Problema:** I link del curl installer e Contributing puntano a `otto78/loom`
(senza `-framework`), il repo corretto è `otto78/loom-framework`.

**File:** `docs/index.html`, `docs/docs.html`, `README.md`  
**Priorità:** CRITICA

---

## TASK-005 — Fix VS Code: Cline → GitHub Copilot

**Problema:** Il file VS Code attuale usa `.clinerules` (Cline, terza parte).
Il file nativo per VS Code è `.github/copilot-instructions.md` (GitHub Copilot).
VS Code e VS Code Insider usano lo stesso file — nessun file separato necessario.

**Azioni:**
1. Eliminare `loom/ide-configs/vscode/clinerules.template`
2. Creare `loom/ide-configs/vscode/copilot-instructions.md.template` (modello minimale)
3. Aggiornare `setup.py`: target `.github/copilot-instructions.md`

**File:** `loom/ide-configs/vscode/`, `loom/scripts/setup.py`  
**Priorità:** CRITICA

---

## TASK-003 — Creare GEMINI.md per Antigravity

**Problema:** Loom non genera `GEMINI.md` (file primario di Antigravity).
La gerarchia Antigravity è: `GEMINI.md` > `AGENTS.md` > `.agent/rules/`

**Azioni:**
1. Creare `loom/ide-configs/antigravity/GEMINI.md.template` (modello minimale)
2. Aggiornare `setup.py` per generare `GEMINI.md` nel progetto target

**Nota:** `~/.gemini/GEMINI.md` è condiviso con Gemini CLI — conflitto noto (#16058).
Documentare nella doc.

**File:** `loom/ide-configs/antigravity/GEMINI.md.template`, `loom/scripts/setup.py`  
**Priorità:** ALTA

---

## TASK-004 — Aggiornare AGENTS.md come cross-tool primario

**Problema:** `AGENTS.md` esiste ma non riflette il suo ruolo di file cross-tool
condiviso tra Antigravity, Windsurf, VS Code e VS Code Insider.

**Contenuto finale:** intestazione cross-tool, setup automatico, comandi naturali,
sintesi DOE, riferimento a `AGENT.md` come fonte di verità.

**File:** `loom/ide-configs/antigravity/AGENTS.md.template` (era `ANTIGRAVITY.md.template`)  
**Priorità:** ALTA

---

## TASK-001 — Ridurre CLAUDE.md al modello minimale

**Problema:** ~120/150 righe sono copia esatta di `AGENT.md`.

**Contenuto finale:** solo Setup Automatico, Comandi Naturali, Best Practices Claude Code.
Tutto il resto (DOE, commit, handoff, comandi utili) sta in `AGENT.md`.

**File:** `loom/ide-configs/claude/CLAUDE.md.template`  
**Priorità:** ALTA

---

## TASK-002 — Ridurre Cursor + formato moderno

**Problema:** `.cursorrules` è legacy. Il formato moderno è `.cursor/rules/loom.mdc`
con frontmatter YAML. Contenuto duplica `AGENT.md`.

**Azioni:**
1. Ridurre `cursorrules.template` al modello minimale
2. Creare `loom/ide-configs/cursor/rules/loom.mdc` con frontmatter YAML
3. Aggiornare `setup.py` per generare entrambi

**File:** `loom/ide-configs/cursor/cursorrules.template`,
          `loom/ide-configs/cursor/rules/loom.mdc` (nuovo),
          `loom/scripts/setup.py`  
**Priorità:** ALTA

---

## TASK-006 — Fix Windsurf: ridurre + formato moderno

**Problema:** `.windsurfrules` è legacy. Formato moderno: `.windsurf/rules/loom.md`.
Contenuto duplica `AGENT.md`. Windsurf legge `AGENTS.md` nativamente.

**Azioni:**
1. Ridurre `windsurfrules.template` al modello minimale
2. Creare `loom/ide-configs/windsurf/rules/loom.md`
3. Aggiornare `setup.py` per generare `.windsurf/rules/loom.md`

**File:** `loom/ide-configs/windsurf/windsurfrules.template`,
          `loom/ide-configs/windsurf/rules/loom.md` (nuovo),
          `loom/scripts/setup.py`  
**Priorità:** ALTA

---

## TASK-007 — Fix IntelliJ: verificare percorso

**Problema:** JetBrains AI Assistant 2025.1+ legge da `.aiassistant/rules/loom.md`.
Verificare che `setup.py` usi questo percorso.

**File:** `loom/scripts/setup.py`  
**Priorità:** ALTA

---

## TASK-009 — Rimuovere sezione duplicata natural-lang

**Problema:** In `docs.html` esistono due sezioni quasi identiche:
`natural-lang` e `natural-language`. Tenere la più completa, rimuovere l'altra.

**File:** `docs/docs.html`  
**Priorità:** ALTA

---

## TASK-010 — Aggiungere traduzioni IT mancanti

**Problema:** Le sezioni `tdd`, `setup-instructions`, `monorepo` e `contributing`
non hanno `contentIt` — mostrano contenuto inglese in silenzio con lingua IT.

**File:** `docs/docs.html`  
**Priorità:** MEDIA

---

## TASK-011 — Aggiornare tabella IDE completa

**Tabella target:**

| IDE | File primario | Percorso nel progetto |
|-----|---------------|-----------------------|
| Claude Code | CLAUDE.md | root/ |
| Cursor | .cursor/rules/loom.mdc | root/.cursor/rules/ |
| Cursor (legacy) | .cursorrules | root/ (fallback) |
| Antigravity | GEMINI.md | root/ |
| Windsurf | .windsurf/rules/loom.md | root/.windsurf/rules/ |
| Windsurf (legacy) | .windsurfrules | root/ (fallback) |
| VS Code | copilot-instructions.md | root/.github/ |
| VS Code Insider | copilot-instructions.md | root/.github/ (stesso) |
| IntelliJ IDEA | loom.md | root/.aiassistant/rules/ |

Cross-tool (Antigravity + Windsurf + VS Code + Insider): `AGENTS.md` → root/

**File:** `docs/docs.html`, `README.md`  
**Priorità:** MEDIA (dipende da task precedenti)

---

## Architettura target

```
AGENT.md          ← fonte di verità progetto
AGENTS.md         ← cross-tool: Antigravity + Windsurf + VS Code + Insider
GEMINI.md         ← Antigravity specific (priorità max su AGENTS.md)
CLAUDE.md         ← Claude Code specific
.cursor/rules/loom.mdc        ← Cursor (formato moderno)
.cursorrules                  ← Cursor (fallback legacy)
.windsurf/rules/loom.md       ← Windsurf (formato moderno)
.windsurfrules                ← Windsurf (fallback legacy)
.github/copilot-instructions.md  ← VS Code + VS Code Insider
.aiassistant/rules/loom.md    ← IntelliJ AI Assistant
```

## Changelog
- 2026-04-30: Task list creata da refactor IDE config
