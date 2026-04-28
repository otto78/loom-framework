# Loom Framework — 3-Level Architecture Guide

> The technical foundation that makes AI-assisted development reliable.

---

## Why Architecture Matters for AI Agents

LLMs are probabilistic. Every decision they make has a probability of being wrong. When you chain decisions together, errors compound:

```
90% accuracy per step
× 5 chained steps = 59% success rate
× 10 chained steps = 35% success rate
```

Without structure, a 10-step AI workflow has a **65% chance of failure**. Loom solves this by pushing complexity into deterministic code.

---

## The DOE Architecture

```
┌─────────────────────────────────────────┐
│ Level 1: DIRECTIVES (What to do)        │
│ loom/directives/*.md                    │
│ Natural language SOPs for the agent     │
├─────────────────────────────────────────┤
│ Level 2: ORCHESTRATION (How to decide)  │
│ The AI agent itself                     │
│ Reads directives, calls scripts         │
├─────────────────────────────────────────┤
│ Level 3: EXECUTION (Do the work)        │
│ loom/execution/*.py                     │
│ Deterministic Python scripts            │
└─────────────────────────────────────────┘
```

---

## Level 1 — Directives

**Location**: `loom/directives/`  
**Format**: Markdown files  
**Purpose**: Standard Operating Procedures in natural language

### What a Directive Contains

Each directive describes **one domain or process**:

```markdown
# Process Payment — Directive

## Goal
Accept and process a customer payment securely.

## Prerequisites
- Stripe API key in .env
- Customer ID available
- Amount validated

## Steps
1. Validate amount is positive and within limits
2. Call execution/process_payment.py with customer_id and amount
3. Handle success: update docs/TASKS.md, notify user
4. Handle failure: log error, retry once, escalate if still failing

## Output
- Success: payment_id returned, TASKS.md updated
- Failure: error logged in docs/STORY.md

## Scripts Used
- `loom/execution/process_payment.py`
```

### Writing Good Directives

- Write as if explaining to a competent junior developer
- Be explicit about inputs, outputs, and edge cases
- Reference execution scripts by name — don't embed logic
- Update directives when you discover new constraints

---

## Level 2 — Orchestration (The AI Agent)

**Who**: Your AI agent (Claude, Cursor, Antigravity, etc.)  
**Role**: Intelligent routing between directives and scripts

The agent's job at this level is **not** to write code or do complex work. It is to:

1. Read the relevant directive
2. Verify prerequisites are met
3. Call the correct execution script with the right parameters
4. Handle errors and retry logic
5. Update `docs/TASKS.md` and `docs/STORY.md`

### What the Agent Should NOT Do at This Level

- ❌ Write complex business logic inline
- ❌ Make multiple chained API calls without a script
- ❌ Handle data transformation without a script
- ✅ Read directive → call script → report result

---

## Level 3 — Execution

**Location**: `loom/execution/`  
**Format**: Python scripts (or Node.js, Rust, etc.)  
**Purpose**: Deterministic, tested, reusable tools

### What an Execution Script Looks Like

```python
#!/usr/bin/env python3
"""
process_payment.py - Process a customer payment via Stripe.

Usage:
    python loom/execution/process_payment.py --customer-id cus_123 --amount 4999

Returns:
    JSON with payment_id on success, error message on failure.
"""
import argparse
import json
import sys

def process_payment(customer_id: str, amount: int) -> dict:
    """Process payment. Returns dict with success/error."""
    # ... deterministic logic here ...
    return {"success": True, "payment_id": "pi_abc123"}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--customer-id", required=True)
    parser.add_argument("--amount", type=int, required=True)
    args = parser.parse_args()
    
    result = process_payment(args.customer_id, args.amount)
    print(json.dumps(result))
    sys.exit(0 if result.get("success") else 1)
```

### Rules for Execution Scripts

1. **Single responsibility** — one script, one job
2. **Always testable** — can be run with `pytest` or standalone
3. **Return structured output** — JSON preferred
4. **Document thoroughly** — docstring, args, return values
5. **Never interactive** — no `input()` calls, always CLI args

---

## How the 3 Levels Work Together

```
User: "process payment for customer cus_123 for $49.99"
        ↓
Agent reads: loom/directives/payments.md
        ↓
Agent verifies: STRIPE_KEY in .env ✅, amount valid ✅
        ↓
Agent calls: python loom/execution/process_payment.py --customer-id cus_123 --amount 4999
        ↓
Script returns: {"success": true, "payment_id": "pi_abc123"}
        ↓
Agent updates: docs/TASKS.md, docs/STORY.md
        ↓
Agent reports: "Payment processed. ID: pi_abc123"
```

**Result**: The LLM only made 3 decisions (read directive, verify, call script). The complex, error-prone logic lived in deterministic Python. Accuracy stays at 90%.

---

## Adding Your Own Directives and Scripts

### New Directive

```bash
# Copy the template
cp loom/directives/_template.md loom/directives/my-feature.md
# Edit with your SOP
```

### New Execution Script

```bash
# Copy the template
cp loom/execution/_template.py loom/execution/my_feature.py
# Implement the logic
# Write tests in tests/
```

---

## Related Documentation

- **[AGENT.md.template](../loom/templates/AGENT.md.template)** — Full agent configuration
- **[workflow-guide.md](./workflow-guide.md)** — Task lifecycle workflow
- **[TDD-WORKFLOW.md](../TDD-WORKFLOW.md)** — Test-driven development
- **[QUICKSTART.md](../QUICKSTART.md)** — Getting started

---

**Version**: 1.0.0  
**Framework**: Loom Framework v1.0
