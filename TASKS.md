# LOOM Framework — Task Plan

---

## TASK-042 — Documentation & Project Organization

### Goal
Migliorare documentazione, organizzare file root, ottimizzare download ZIP, correggere logo e flusso task nel Quick Start.

### Acceptance Criteria
- [ ] Quick Start include logica task/epiche con comandi "lista task" 
- [ ] Logo loom visibile correttamente nella home
- [ ] README titolo corretto "Loom Framework", aggiunta sezione Monorepo tradotta
- [ ] File root organizzati in cartelle (docs/, guides/, etc.)
- [ ] ZIP include solo file necessari (no CONTRIBUTING, ABSTRACT)
- [ ] ABSTRACT.md posizionato correttamente o rimosso dalla root

### Epic
Documentation & UX Improvements

### Priority
high

---

## Sub-Tasks

#### TASK-042.1 — Migliorare Quick Start con flusso task/epiche
**Scope:** Modificare sezione Quick Start in `docs/index.html` e `docs/docs.html` per includere:
- Comando "lista task" o "fammi vedere i task" prima di "avvia task"
- Logica: se non ci sono task, l'agente deve proporre di crearli da PROJECT.md
- Riferimento alle epiche se presenti in PROJECT.md
**File:** docs/index.html, docs/docs.html
**Estimated:** 30 min

#### TASK-042.2 — Correggere logo nella home
**Scope:** Verificare e correggere il logo loom in index.html (🧵 → logo immagine se necessario)
**File:** docs/index.html
**Estimated:** 15 min

#### TASK-042.3 — Fix README titolo e aggiungere Monorepo
**Scope:** 
- Correggere eventuali refusi nel titolo README ("lomm" → "Loom Framework")
- Aggiungere sezione Monorepo alla lista documentazione
- Tradurre sezione Monorepo completamente in italiano in docs.html
**File:** README.md, docs/docs.html
**Estimated:** 45 min

#### TASK-042.4 — Organizzare file root in cartelle
**Scope:** Spostare file markdown non essenziali dalla root in sottocartelle:
- Proposta: `guides/` per CONTRIBUTING, MONOREPO-GUIDE, TDD-WORKFLOW, SETUP-INSTRUCTIONS
- `docs/` per ABSTRACT, PUBLISH, NATURAL-LANGUAGE-GUIDE
- Aggiornare tutti i riferimenti interni
**File:** struttura cartelle, README.md, docs/docs.html
**Estimated:** 60 min

#### TASK-042.5 — Ottimizzare ZIP download
**Scope:** Modificare `loom/scripts/build-zip.py` per escludere file non necessari:
- Rimuovere: CONTRIBUTING.md, ABSTRACT.md, PUBLISH.md
- Includere solo: loom/, README.md, QUICKSTART.md, LICENSE, pyproject.toml, install scripts
**File:** loom/scripts/build-zip.py
**Estimated:** 20 min

#### TASK-042.6 — Aggiornare riferimenti dopo riorganizzazione
**Scope:** Verificare e aggiornare tutti i link interni dopo lo spostamento file
**File:** tutti i file .md e .html
**Estimated:** 30 min

---

## Notes
- Utente ha richiesto specificamente: Quick Start deve considerare che i task possono venire da PROJECT.md
- ABSTRACT.md è visibile nella home come descrizione principale
- Logo attuale è 🧵 (emoji), forse si vuole un'immagine
- Titolo README sembra corretto, verificare se c'è "lomm" da qualche parte

## Dependencies
- TASK-042.4 dipende da TASK-042.3 (README aggiornato prima di spostare)
- TASK-042.6 dipende da TASK-042.4

## Changelog
- 2026-04-30: Task creato
