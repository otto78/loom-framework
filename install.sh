#!/bin/bash
# Antigravity - One-liner installer
# Usage: curl -fsSL https://raw.githubusercontent.com/otto78/antigravity/main/install.sh | bash

set -e

Antigravity_REPO="https://github.com/otto78/antigravity.git"
Antigravity_DIR="$HOME/.antigravity"
PYTHON_MIN_VERSION="3.8"

echo "🧵 Antigravity Installer"
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

# Clone or update Antigravity
if [ -d "$Antigravity_DIR" ]; then
    echo "📦 Updating existing Antigravity installation..."
    cd "$Antigravity_DIR"
    git pull --quiet
else
    echo "📦 Cloning Antigravity..."
    git clone --quiet "$Antigravity_REPO" "$Antigravity_DIR"
fi

echo "✅ Antigravity installed to $Antigravity_DIR"
echo ""

# Detect project directory
if [ -f "pyproject.toml" ] || [ -f "package.json" ] || [ -f "pom.xml" ]; then
    echo "🔍 Project detected in current directory: $(pwd)"
    echo ""
    read -p "Setup Antigravity in this project? (y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        python3 "$Antigravity_DIR/antigravity/scripts/setup.py"
    else
        echo "ℹ️  To setup Antigravity later, run:"
        echo "   python3 $Antigravity_DIR/antigravity/scripts/setup.py"
    fi
else
    echo "ℹ️  No project detected in current directory."
    echo "   Navigate to your project and run:"
    echo "   python3 $Antigravity_DIR/antigravity/scripts/setup.py"
fi

echo ""
echo "✨ Installation complete!"
echo ""
echo "📚 Documentation: https://otto78.github.io/antigravity/docs.html"
echo "🐙 GitHub: https://github.com/otto78/antigravity"
