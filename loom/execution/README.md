# Execution — Script Deterministici

Questa cartella contiene gli script deterministici che fanno il lavoro concreto (Livello 3).

---

## 🎯 Cos'è uno Script di Esecuzione

Uno script deterministico che:
- Riceve input ben definiti
- Esegue operazioni concrete (API calls, DB queries, file operations)
- Ritorna output strutturato (JSON)
- È testabile e affidabile (stesso input = stesso output)

**Non fa decisioni** — Esegue solo ciò che gli viene chiesto.

---

## 📝 Struttura di uno Script

### 1. Docstring Completo

```python
#!/usr/bin/env python3
"""
Breve descrizione dello script (1 frase).

Descrizione dettagliata di cosa fa lo script.

Input (CLI args):
  --param1: Descrizione parametro 1
  --param2: Descrizione parametro 2

Output (JSON):
  Success: {"status": "success", "data": {...}}
  Error: {"status": "error", "reason": "..."}

Env vars:
  ENV_VAR_1: Descrizione variabile 1
  ENV_VAR_2: Descrizione variabile 2

Examples:
  python script.py --param1="value" --param2=123
"""
```

### 2. Import e Setup

```python
import argparse
import json
import os
import sys
from typing import Dict, Any

# Configurazione
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
```

### 3. Funzione Principale

```python
def main_function(param1: str, param2: int) -> Dict[str, Any]:
    """
    Funzione principale che fa il lavoro.
    
    Args:
        param1: Descrizione parametro 1
        param2: Descrizione parametro 2
    
    Returns:
        Dict con status e data/reason
    """
    try:
        # Validazione input
        if not param1:
            return {"status": "error", "reason": "param1 is required"}
        
        # Lavoro concreto
        result = do_work(param1, param2)
        
        # Ritorna successo
        return {"status": "success", "data": result}
    
    except Exception as e:
        # Gestione errori
        return {"status": "error", "reason": str(e)}
```

### 4. CLI Entry Point

```python
def main():
    """Entry point CLI."""
    parser = argparse.ArgumentParser(description="Descrizione script")
    parser.add_argument("--param1", required=True, help="Descrizione param1")
    parser.add_argument("--param2", type=int, required=True, help="Descrizione param2")
    args = parser.parse_args()
    
    # Esegui funzione principale
    result = main_function(args.param1, args.param2)
    
    # Output JSON
    print(json.dumps(result, indent=2))
    
    # Exit code
    sys.exit(0 if result["status"] == "success" else 1)

if __name__ == "__main__":
    main()
```

---

## ✅ Esempio Completo

Vedi `_template.py` per un template completo.

---

## 🎓 Best Practices

### 1. Deterministico

Stesso input = stesso output (sempre).

❌ **Male:**
```python
# Usa timestamp corrente (non deterministico)
timestamp = time.time()
```

✅ **Bene:**
```python
# Ricevi timestamp come parametro
def process(timestamp: float):
    ...
```

### 2. JSON Output

Sempre output JSON strutturato.

❌ **Male:**
```python
print("Success!")
print(f"Result: {result}")
```

✅ **Bene:**
```python
print(json.dumps({
    "status": "success",
    "data": result
}))
```

### 3. Exit Code

0 = successo, 1+ = errore.

```python
sys.exit(0 if result["status"] == "success" else 1)
```

### 4. Env Vars per Credenziali

Mai hardcodare credenziali.

❌ **Male:**
```python
API_KEY = "sk-1234567890"
```

✅ **Bene:**
```python
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    return {"status": "error", "reason": "API_KEY not set"}
```

### 5. Gestione Errori Completa

Cattura tutte le eccezioni.

```python
try:
    result = risky_operation()
except SpecificError as e:
    return {"status": "error", "reason": f"Specific error: {e}"}
except Exception as e:
    return {"status": "error", "reason": f"Unexpected error: {e}"}
```

### 6. Validazione Input

Valida sempre gli input.

```python
if not email or "@" not in email:
    return {"status": "error", "reason": "Invalid email"}

if age < 0 or age > 150:
    return {"status": "error", "reason": "Invalid age"}
```

### 7. Logging (Opzionale)

Per debugging, usa logging (non print).

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"Processing {param1}")
logger.error(f"Failed: {error}")
```

### 8. Type Hints

Usa type hints per chiarezza.

```python
def process_data(data: Dict[str, Any], timeout: int = 30) -> Dict[str, Any]:
    ...
```

---

## 📊 Checklist Qualità Script

- [ ] Docstring completo (input, output, env vars, examples)
- [ ] Type hints su tutte le funzioni
- [ ] Validazione input completa
- [ ] Gestione errori completa (try/except)
- [ ] JSON output strutturato
- [ ] Exit code corretto (0 = success, 1 = error)
- [ ] Env vars per credenziali (no hardcode)
- [ ] Testabile (funzione principale separata da CLI)
- [ ] Deterministico (stesso input = stesso output)
- [ ] Documentato (commenti dove necessario)

---

## 🧪 Testing

### Unit Test

```python
# tests/test_script.py
import pytest
from execution.script import main_function

def test_success_case():
    result = main_function("valid_input", 123)
    assert result["status"] == "success"
    assert "data" in result

def test_error_case():
    result = main_function("", 123)
    assert result["status"] == "error"
    assert "reason" in result
```

### Integration Test

```bash
# Test CLI
python execution/script.py --param1="test" --param2=123
echo $?  # Should be 0

python execution/script.py --param1="" --param2=123
echo $?  # Should be 1
```

---

## 🔄 Workflow

### Creare un nuovo script

1. Copia `_template.py` → `nome_script.py`
2. Compila docstring completo
3. Implementa funzione principale
4. Aggiungi validazione input
5. Aggiungi gestione errori
6. Testa manualmente
7. Scrivi unit test
8. Documenta in direttiva corrispondente

### Aggiornare uno script esistente

1. Leggi lo script corrente
2. Identifica cosa modificare
3. Aggiorna funzione principale
4. Aggiorna docstring se necessario
5. Aggiorna test
6. Testa manualmente
7. Aggiorna direttiva se necessario

---

## 🎯 Quando Creare un Nuovo Script

### ✅ Crea quando

- Hai operazione ripetibile
- Serve affidabilità (API call, DB query)
- Logica complessa (algoritmi)
- Serve testabilità

### ❌ Non creare quando

- Operazione una-tantum
- Troppo semplice (1 comando shell)
- Già coperto da script esistente

---

## 📚 Convenzioni di Nome

- **snake_case** — `send_email.py`, `get_user.py`
- **Verbo + Sostantivo** — `create_user.py`, `delete_file.py`
- **Descrittivo** — `generate_weekly_report.py` (non `report.py`)

---

## 🔗 Dipendenze

### Gestione Dipendenze

```bash
# Aggiungi dipendenza
pip install requests
pip freeze > requirements.txt

# Installa dipendenze
pip install -r requirements.txt
```

### Virtual Environment

```bash
# Crea venv
python -m venv venv

# Attiva (Unix/Linux/macOS)
source venv/bin/activate

# Attiva (Windows)
venv\Scripts\activate

# Installa dipendenze
pip install -r requirements.txt
```

---

**Versione:** 1.0.0  
**Ultima modifica:** 2025-01-XX
