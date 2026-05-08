"""Verify all dependencies are installed correctly."""

import sys

def test_imports():
    """Test all required packages can be imported."""
    packages = [
        ("pydantic", "Data validation"),
        ("mypy", "Type checking"),
        ("pytest", "Testing framework"),
        ("black", "Code formatting"),
        ("ruff", "Linting"),
    ]
    
    print("Testing package imports...")
    all_ok = True
    
    for package, description in packages:
        try:
            exec(f"import {package}")
            print(f"  ✅ {package:12} - {description}")
        except ImportError:
            print(f"  ❌ {package:12} - MISSING!")
            all_ok = False
    
    # Test your project modules
    try:
        import core
        print(f"  ✅ {'core':12} - Your DSA module")
    except ImportError:
        print(f"  ❌ {'core':12} - NOT FOUND!")
        all_ok = False
        
    try:
        import app
        print(f"  ✅ {'app':12} - Entry points module")
    except ImportError:
        print(f"  ❌ {'app':12} - NOT FOUND!")
        all_ok = False
    
    return all_ok

if __name__ == "__main__":
    print("=" * 50)
    print("DSA Project Setup Verification")
    print("=" * 50)
    print(f"Python version: {sys.version}")
    print("-" * 50)
    
    if test_imports():
        print("-" * 50)
        print("✅ All dependencies are correctly installed!")
        print("✅ You're ready for Day 2!")
    else:
        print("-" * 50)
        print("❌ Some dependencies are missing")
        print("Run: uv pip install -e '.[dev]'")