# Loom Framework Tests

This directory contains tests for the Loom Framework.

## Running Tests

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run all tests
pytest

# Run with coverage
pytest --cov=loom --cov-report=html
```

## Test Structure

- `test_setup.py` — Tests for setup wizard
- `test_task.py` — Tests for task workflow manager
- `test_task_tdd.py` — Tests for TDD workflow
- `test_templates.py` — Tests for template generation
