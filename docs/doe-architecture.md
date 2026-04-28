# Antigravity — DOE Architecture Guide
# Guida all'Architettura DOE

> **EN** — The technical foundation that makes AI-assisted development reliable.  
> **IT** — La base tecnica che rende affidabile lo sviluppo assistito dall'AI.

---

## Why Architecture Matters / Perché l'Architettura è Importante

**EN**  
LLMs are probabilistic. Every decision they make has a probability of being wrong. When you chain decisions together, errors compound:
- 1 step: 90% success
- 5 steps: 59% (0.9 × 0.9 × 0.9 × 0.9 × 0.9)
- 10 steps: 35% success rate

**IT**  
Gli LLM sono probabilistici. Ogni decisione che prendono ha una probabilità di essere sbagliata. Quando si concatenano le decisioni, gli errori si accumulano:
- 1 step: 90% successo
- 5 step: 59% (0.9 × 0.9 × 0.9 × 0.9 × 0.9)
- 10 step: 35% tasso di successo

Antigravity solves this by pushing complexity into deterministic code through the **DOE Architecture**.

---

## The DOE Architecture / L'Architettura DOE

```
┌─────────────────────────────────────────┐
│ D — DIRECTIVES (What to do / Cosa fare) │
│ antigravity/directives/*.md                    │
│ Natural language SOPs / SOP in naturale │
├─────────────────────────────────────────┤
│ O — ORCHESTRATION (How / Come decidere) │
│ The AI agent itself / L'agente AI       │
│ Reads directives, calls scripts         │
├─────────────────────────────────────────┤
│ E — EXECUTION (Do it / Esecuzione)      │
│ antigravity/execution/*.py                     │
│ Deterministic scripts / Script det.     │
└─────────────────────────────────────────┘
```

---

## D — Directives (What to do / Cosa fare)

**EN**  
SOPs written in Markdown that define **what** to do. They live in `Antigravity/directives/*.md`.  
Each directive describes **one domain or process**.

**IT**  
SOP scritte in Markdown che definiscono **cosa** fare. Si trovano in `Antigravity/directives/*.md`.  
Ogni direttiva descrive **un dominio o un processo**.

---

## O — Orchestration (How to decide / Come decidere)

**EN**  
Your AI agent (Claude, Cursor, Antigravity, etc.). Role: Intelligent routing between directives and scripts.  
The agent's job: read the relevant directive, verify prerequisites, call the execution script.

**IT**  
Il tuo agente AI (Claude, Cursor, Antigravity, ecc.). Ruolo: Routing intelligente tra direttive e script.  
Il compito dell'agente: leggere la direttiva pertinente, verificare i prerequisiti, chiamare lo script di esecuzione.

---

## E — Execution (Do the work / Eseguire il lavoro)

**EN**  
Deterministic Python scripts in `Antigravity/execution/`. They perform the actual work (API calls, file manipulation, etc.) and return structured JSON results.

**IT**  
Script Python deterministici in `Antigravity/execution/`. Eseguono il lavoro effettivo (chiamate API, manipolazione file, ecc.) e restituiscono risultati JSON strutturati.

---

## How they work together / Come lavorano insieme

```
User: "process payment for customer cus_123 for $49.99"
        ↓
Agent reads: antigravity/directives/payments.md (D)
        ↓
Agent verifies prerequisites ✅ (O)
        ↓
Agent calls: python antigravity/execution/process_payment.py (E)
        ↓
Agent updates: docs/TASKS.md, docs/STORY.md (O)
```

---

**Version**: 1.0.0  
**Framework**: Antigravity (Antigravity)
