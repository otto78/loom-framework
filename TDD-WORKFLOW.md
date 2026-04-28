# TDD Workflow — Test-Driven Development

> Workflow completo Test-Driven Development integrato nel framework.

---

## 🎯 Cos'è TDD

**Test-Driven Development** è una metodologia di sviluppo dove:
1. **Scrivi i test PRIMA** del codice
2. **Esegui i test** (devono fallire - Red phase)
3. **Scrivi il codice minimo** per far passare i test (Green phase)
4. **Refactoring** del codice mantenendo i test verdi (Refactor phase)

### Perché TDD

- ✅ **Codice testato al 100%** — Ogni riga ha un test
- ✅ **Design migliore** — Pensare ai test prima migliora l'architettura
- ✅ **Meno bug** — I test catturano errori subito
- ✅ **Refactoring sicuro** — I test garantiscono che nulla si rompa
- ✅ **Documentazione viva** — I test mostrano come usare il codice

---

## 🔄 Ciclo TDD (Red-Green-Refactor)

```
┌─────────────────────────────────────────┐
│ 🔴 RED: Write failing test             │
│ - Scrivi test per feature non esistente│
│ - Test deve fallire                     │
│ - Commit: "test: add tests for X"      │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ 🟢 GREEN: Make test pass                │
│ - Scrivi codice minimo per passare test│
│ - Test deve passare                     │
│ - Non ottimizzare ancora                │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ 🔵 REFACTOR: Clean up code              │
│ - Migliora codice senza cambiare test  │
│ - Test devono rimanere verdi            │
│ - Commit: "feat: implement X"           │
└─────────────────────────────────────────┘
              ↓
         Ripeti per prossima feature
```

---

## 🚀 Workflow con Antigravity

### Comando Principale

```bash
# Start TDD task (Red phase)
python scripts/task-tdd.py start TASK-001 "Implement user authentication"

# Run tests
python scripts/task-tdd.py test

# Complete task (after tests pass)
python scripts/task-tdd.py complete TASK-001
```

### Workflow Completo

#### 1. Start TDD Task (Red Phase)

```bash
python scripts/task-tdd.py start TASK-001 "Add email validation"
```

**Cosa fa:**
1. Chiede dove creare il test file
2. Crea test file vuoto se non esiste
3. Esegue i test (devono fallire - Red phase)
4. Aggiorna `TASKS.md` con checklist TDD
5. Commit: `test: add tests for TASK-001 (TDD Red phase)`
6. Push

**Output:**
```
🧪 Starting TDD workflow for TASK-001: Add email validation

📝 Test file for TASK-001:
   Suggested: tests/test_task_001.py
   Test file path (or press Enter for suggestion): 

⚠️  Test file not found: tests/test_task_001.py

🔴 TDD Red Phase: Write tests first!

Create tests/test_task_001.py with:
  1. Test cases for the feature
  2. Expected behavior
  3. Edge cases

Tests should FAIL initially (Red phase)

Create empty test file tests/test_task_001.py? (y/n): y
✅ Created tests/test_task_001.py
⚠️  Edit the file to add real tests!

🔴 Running tests (Red phase - should fail)...
✅ Tests failed as expected (Red phase)

✅ Updated docs/TASKS.md

🎯 Next steps:
   1. Implement feature to make tests pass (Green phase)
   2. Run: python scripts/task-tdd.py test
   3. If tests pass: python scripts/task-tdd.py complete TASK-001
   4. If tests fail: fix code and repeat step 2
```

#### 2. Write Tests (Red Phase)

Modifica il test file creato:

```python
# tests/test_task_001.py
"""
Tests for TASK-001: Add email validation
"""

def test_valid_email():
    """Test that valid emails are accepted."""
    from myapp import validate_email
    
    assert validate_email("user@example.com") == True
    assert validate_email("test.user@domain.co.uk") == True

def test_invalid_email():
    """Test that invalid emails are rejected."""
    from myapp import validate_email
    
    assert validate_email("invalid") == False
    assert validate_email("@example.com") == False
    assert validate_email("user@") == False

def test_empty_email():
    """Test that empty email is rejected."""
    from myapp import validate_email
    
    assert validate_email("") == False
    assert validate_email(None) == False
```

#### 3. Run Tests (Should Fail)

```bash
python scripts/task-tdd.py test
```

**Output:**
```
🧪 Running test suite...

============================= test session starts ==============================
collected 3 items

tests/test_task_001.py FFF                                              [100%]

=================================== FAILURES ===================================
________________________________ test_valid_email ______________________________
ImportError: cannot import name 'validate_email' from 'myapp'
...

❌ Tests failed! (Still in Red/Green phase)

🎯 Next steps:
   1. Fix the failing tests
   2. Run tests again: python scripts/task-tdd.py test
   3. Repeat until all tests pass
```

#### 4. Implement Feature (Green Phase)

Scrivi il codice minimo per far passare i test:

```python
# myapp/validation.py
import re

def validate_email(email: str) -> bool:
    """Validate email address."""
    if not email:
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

#### 5. Run Tests Again

```bash
python scripts/task-tdd.py test
```

**Output:**
```
🧪 Running test suite...

============================= test session starts ==============================
collected 3 items

tests/test_task_001.py ...                                              [100%]

============================== 3 passed in 0.12s ===============================

✅ All tests passed! (Green phase)

🎯 Next steps:
   1. Refactor code if needed (Refactor phase)
   2. Run tests again to ensure refactoring didn't break anything
   3. Complete task: python scripts/task-tdd.py complete TASK-001
```

#### 6. Refactor (Optional)

Migliora il codice mantenendo i test verdi:

```python
# myapp/validation.py
import re
from typing import Optional

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email: Optional[str]) -> bool:
    """
    Validate email address.
    
    Args:
        email: Email address to validate
    
    Returns:
        True if valid, False otherwise
    
    Examples:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid")
        False
    """
    if not email:
        return False
    
    return bool(EMAIL_PATTERN.match(email))
```

Esegui test di nuovo per verificare:

```bash
python scripts/task-tdd.py test
```

#### 7. Complete Task

```bash
python scripts/task-tdd.py complete TASK-001
```

**Output:**
```
🧪 Completing TDD task TASK-001

🧪 Running final test suite...

============================= test session starts ==============================
collected 3 items

tests/test_task_001.py ...                                              [100%]

============================== 3 passed in 0.12s ===============================

✅ All tests passed!

✅ Updated docs/TASKS.md

🎉 Task TASK-001 completed with TDD workflow!
   All tests passing ✅
```

**Cosa fa:**
1. Esegue test finale
2. Se passano: aggiorna `TASKS.md` (status Done, checklist completa)
3. Commit: `feat: complete TASK-001 (TDD Green - all tests passing)`
4. Push

---

## 📋 TASKS.md con TDD

Quando usi TDD, `TASKS.md` include una checklist:

```markdown
### TASK-001 — Add email validation

**Status:** In Progress (TDD Red Phase)  
**Test file:** `tests/test_task_001.py`  
**Started:** 2025-01-15

**TDD Workflow:**
- [x] 🔴 Red: Tests created and failing
- [ ] 🟢 Green: Implement feature to pass tests
- [ ] 🔵 Refactor: Clean up code
- [ ] ✅ Complete: All tests passing
```

Dopo il completamento:

```markdown
### TASK-001 — Add email validation

**Status:** Done ✅  
**Completed:** 2025-01-15  
**Test file:** `tests/test_task_001.py`  

**TDD Workflow:**
- [x] 🔴 Red: Tests created and failing
- [x] 🟢 Green: Implement feature to pass tests
- [x] 🔵 Refactor: Clean up code
- [x] ✅ Complete: All tests passing
```

---

## 📊 TDD Log

Il framework mantiene un log TDD in `docs/TDD_LOG.md`:

```markdown
# TDD Log

## TASK-001 — RED (Start)

**Time:** 2025-01-15 10:30:00  
**Status:** Tests Failing  
**Details:**
```
============================= test session starts ==============================
collected 3 items

tests/test_task_001.py FFF                                              [100%]
...
```

## TASK-001 — GREEN (Complete)

**Time:** 2025-01-15 11:45:00  
**Status:** All Tests Passing  
**Details:**
```
============================= test session starts ==============================
collected 3 items

tests/test_task_001.py ...                                              [100%]

============================== 3 passed in 0.12s ===============================
```
```

---

## 🎓 Best Practices TDD

### 1. Test Piccoli e Focalizzati

```python
# ✅ Buono - un test, un comportamento
def test_valid_email_with_subdomain():
    assert validate_email("user@mail.example.com") == True

# ❌ Male - troppi comportamenti in un test
def test_email_validation():
    assert validate_email("user@example.com") == True
    assert validate_email("invalid") == False
    assert validate_email("") == False
    # ... 20 altri assert
```

### 2. Test Leggibili

```python
# ✅ Buono - nome descrittivo
def test_empty_email_returns_false():
    result = validate_email("")
    assert result == False

# ❌ Male - nome generico
def test_1():
    assert validate_email("") == False
```

### 3. Arrange-Act-Assert Pattern

```python
def test_user_registration():
    # Arrange - setup
    user_data = {"email": "test@example.com", "password": "secret"}
    
    # Act - esegui azione
    result = register_user(user_data)
    
    # Assert - verifica risultato
    assert result.success == True
    assert result.user_id is not None
```

### 4. Test Indipendenti

```python
# ✅ Buono - ogni test è indipendente
def test_create_user():
    user = create_user("test@example.com")
    assert user.email == "test@example.com"

def test_delete_user():
    user = create_user("test2@example.com")  # Crea proprio user
    delete_user(user.id)
    assert get_user(user.id) is None

# ❌ Male - test dipendenti
def test_create_user():
    global user_id
    user = create_user("test@example.com")
    user_id = user.id  # Dipendenza globale

def test_delete_user():
    delete_user(user_id)  # Dipende da test precedente
```

### 5. Test Edge Cases

```python
def test_email_validation_edge_cases():
    # Empty
    assert validate_email("") == False
    
    # None
    assert validate_email(None) == False
    
    # Very long
    long_email = "a" * 100 + "@example.com"
    assert validate_email(long_email) == False
    
    # Special characters
    assert validate_email("user+tag@example.com") == True
    
    # Multiple @
    assert validate_email("user@@example.com") == False
```

---

## 🔧 Configurazione Test Framework

### Python (pytest)

```bash
# Installa pytest
pip install pytest pytest-cov

# Crea pytest.ini
cat > pytest.ini << EOF
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
EOF
```

### JavaScript (Jest)

```bash
# Installa Jest
npm install --save-dev jest

# Configura package.json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  },
  "jest": {
    "testEnvironment": "node",
    "coverageDirectory": "coverage",
    "collectCoverageFrom": ["src/**/*.js"]
  }
}
```

---

## 📚 Comandi Utili

```bash
# Start TDD task
python scripts/task-tdd.py start TASK-001 "Feature description"

# Run tests
python scripts/task-tdd.py test

# Run tests verbose
python scripts/task-tdd.py test -v

# Complete task
python scripts/task-tdd.py complete TASK-001

# Dry-run (simulate)
python scripts/task-tdd.py start TASK-001 "..." --dry-run

# Complete without push
python scripts/task-tdd.py complete TASK-001 --no-push
```

---

## 🆚 TDD vs Non-TDD Workflow

### Workflow Normale

```bash
python scripts/task.py start TASK-001 "Feature"
# Scrivi codice
# Scrivi test (forse)
python scripts/task.py complete TASK-001 "Done"
```

### Workflow TDD

```bash
python scripts/task-tdd.py start TASK-001 "Feature"
# Scrivi test PRIMA
# Test falliscono (Red)
# Scrivi codice
python scripts/task-tdd.py test
# Test passano (Green)
# Refactor
python scripts/task-tdd.py test
# Test ancora verdi
python scripts/task-tdd.py complete TASK-001
```

**Differenza chiave:** TDD garantisce che ogni feature abbia test PRIMA di essere implementata.

---

## ✅ Checklist TDD

Prima di completare un task TDD:

- [ ] Test scritti PRIMA del codice
- [ ] Test inizialmente falliti (Red phase)
- [ ] Codice implementato per far passare test (Green phase)
- [ ] Codice refactorato mantenendo test verdi (Refactor phase)
- [ ] Tutti i test passano
- [ ] Test coprono edge cases
- [ ] Test sono leggibili e manutenibili
- [ ] Nessun test skippato o commentato

---

**Versione:** 1.0.0  
**Framework:** Antigravity v1.0  
**Metodologia:** Test-Driven Development
