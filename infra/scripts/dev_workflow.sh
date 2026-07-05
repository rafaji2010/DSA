#!/bin/bash
# ============================================
# Development Workflow Automation
# ============================================

set -euo pipefail

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

# Project root (detect automatically)
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}Development Workflow Automation${NC}"
echo -e "${BLUE}========================================${NC}"

# Function: Run tests
run_tests() {
    echo -e "\n📝 Running tests..."
    if [ -d "tests" ]; then
        python -m pytest tests/ -v --tb=short
    else
        echo "No tests directory found"
    fi
}

# Function: Run type checking
run_mypy() {
    echo -e "\n🔍 Running type checking..."
    if command -v mypy &> /dev/null; then
        mypy core/ --ignore-missing-imports
    else
        echo "mypy not installed"
    fi
}

# Function: Run linter
run_linter() {
    echo -e "\n🧹 Running linter..."
    if command -v ruff &> /dev/null; then
        ruff check core/
    else
        echo "ruff not installed"
    fi
}

# Function: Git operations
git_operations() {
    echo -e "\n📦 Git operations..."
    
    # Show status
    git status --short
    
    # Ask what to do
    echo -e "\nOptions:"
    echo "  1) Add all and commit"
    echo "  2) Just show status"
    echo "  3) Skip"
    read -p "Choose (1-3): " choice
    
    case $choice in
        1)
            read -p "Commit message: " msg
            git add .
            git commit -m "$msg"
            git push
            echo "✅ Pushed to remote"
            ;;
        2)
            echo "No changes made"
            ;;
        *)
            echo "Skipping git operations"
            ;;
    esac
}

# Main workflow
main() {
    echo -e "\n${GREEN}Running pre-commit checks...${NC}"
    run_mypy
    run_linter
    run_tests
    
    echo -e "\n${GREEN}All checks passed!${NC}"
    git_operations
}

main "$@"
