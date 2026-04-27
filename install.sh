#!/bin/bash
# Loom Framework - One-liner installer
# Usage: curl -fsSL https://raw.githubusercontent.com/otto78/loom-framework/main/install.sh | bash

set -e

LOOM_REPO="https://github.com/otto78/loom-framework.git"
LOOM_DIR="$HOME/.loom-framework"
PYTHON_MIN_VERSION="3.8"

echo "🧵 Loom Framework Installer"
echo "============================"
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python $PYTHON_MIN_VERSION or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Python $PYTHON_VERSION detected"

# Check git
if ! command -v git &> /dev/null; then
    echo "❌ Git not found. Please install git first."
    exit 1
fi

echo "✅ Git detected"

# Clone or update Loom
if [ -d "$LOOM_DIR" ]; then
    echo "📦 Updating existing Loom installation..."
    cd "$LOOM_DIR"
    git pull --quiet
else
    echo "📦 Cloning Loom Framework..."
    git clone --quiet "$LOOM_REPO" "$LOOM_DIR"
fi

echo "✅ Loom Framework installed to $LOOM_DIR"
echo ""

# Detect project directory
if [ -f "pyproject.toml" ] || [ -f "package.json" ] || [ -f "pom.xml" ]; then
    echo "🔍 Project detected in current directory: $(pwd)"
    echo ""
    read -p "Setup Loom in this project? (y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        python3 "$LOOM_DIR/loom/scripts/setup.py"
    else
        echo "ℹ️  To setup Loom later, run:"
        echo "   python3 $LOOM_DIR/loom/scripts/setup.py"
    fi
else
    echo "ℹ️  No project detected in current directory."
    echo "   Navigate to your project and run:"
    echo "   python3 $LOOM_DIR/loom/scripts/setup.py"
fi

echo ""
echo "✨ Installation complete!"
echo ""
echo "📚 Documentation: https://otto78.github.io/loom-framework/docs.html"
echo "🐙 GitHub: https://github.com/otto78/loom-framework"
