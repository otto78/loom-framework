# Contributing to Loom Framework

Thank you for your interest in contributing to Loom! 🧵

---

## 🎯 How to Contribute

### 1. Report Issues

Found a bug or have a feature request?

1. Check [existing issues](https://github.com/yourusername/loom-framework/issues)
2. If not found, [create a new issue](https://github.com/yourusername/loom-framework/issues/new)
3. Use the issue templates provided

### 2. Improve Documentation

Documentation improvements are always welcome:

- Fix typos
- Add examples
- Clarify explanations
- Translate to other languages

### 3. Add IDE Support

Using an IDE not yet supported?

1. Create config template in `loom/ide-configs/your-ide/`
2. Update `loom/scripts/setup.py` to detect and configure it
3. Add to README.md IDE support table
4. Submit a pull request

### 4. Enhance Scripts

Improve existing scripts or add new ones:

- Better error handling
- More options
- Performance improvements
- New features

### 5. Share Your Experience

- Write blog posts
- Create video tutorials
- Share on social media
- Present at meetups

---

## 🔧 Development Setup

```bash
# Clone repository
git clone https://github.com/yourusername/loom-framework.git
cd loom-framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Run linter
flake8 loom/
```

---

## 📝 Pull Request Process

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Make** your changes
4. **Test** your changes thoroughly
5. **Commit** with clear messages: `git commit -m "feat: add amazing feature"`
6. **Push** to your fork: `git push origin feature/amazing-feature`
7. **Open** a pull request

### Commit Message Format

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add support for PyCharm IDE
fix: resolve task completion bug
docs: update QUICKSTART guide
test: add tests for setup wizard
refactor: simplify task.py logic
```

---

## ✅ Code Standards

### Python

- Follow [PEP 8](https://pep8.org/)
- Use type hints
- Write docstrings
- Add tests for new features

### Documentation

- Use clear, concise language
- Include code examples
- Add screenshots when helpful
- Keep formatting consistent

### Scripts

- Handle errors gracefully
- Provide helpful error messages
- Support `--dry-run` mode
- Add `--help` documentation

---

## 🧪 Testing

All contributions should include tests:

```bash
# Run all tests
pytest tests/

# Run specific test
pytest tests/test_task.py

# Run with coverage
pytest --cov=loom tests/
```

---

## 📚 Documentation

Update documentation when:

- Adding new features
- Changing existing behavior
- Adding new IDE support
- Fixing bugs

Files to update:
- `README.md` — Main documentation
- `QUICKSTART.md` — Quick start guide
- `docs/` — Detailed guides
- Inline code comments

---

## 🎨 IDE Config Templates

When adding IDE support:

1. Create template in `loom/ide-configs/your-ide/`
2. Include:
   - Reference to `AGENT.md`
   - Natural language command support
   - 3-level framework explanation
   - Task management commands
3. Test with actual IDE
4. Document in README.md

---

## 🌍 Internationalization

Help translate Loom:

1. Create `docs/i18n/[language]/` directory
2. Translate key documents:
   - README.md
   - QUICKSTART.md
   - NATURAL-LANGUAGE-GUIDE.md
3. Update natural language commands in scripts
4. Submit pull request

---

## 💬 Community

- **Discussions**: [GitHub Discussions](https://github.com/yourusername/loom-framework/discussions)
- **Issues**: [GitHub Issues](https://github.com/yourusername/loom-framework/issues)
- **Twitter**: [@loomframework](https://twitter.com/loomframework)

---

## 📜 Code of Conduct

Be respectful, inclusive, and constructive. We're all here to improve Loom together.

---

## 🙏 Recognition

Contributors are recognized in:
- `CONTRIBUTORS.md`
- Release notes
- Project README

---

## ❓ Questions?

Not sure where to start? Open a [discussion](https://github.com/yourusername/loom-framework/discussions) and ask!

---

**Thank you for contributing to Loom!** 🧵

Every contribution, no matter how small, makes Loom better for everyone.
