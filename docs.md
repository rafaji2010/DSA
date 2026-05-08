Copy and paste this complete markdown content:

markdown
# DSA Project Setup - Complete Documentation

## Table of Contents
1. [Project Structure](#project-structure)
2. [Package Management with uv](#package-management-with-uv)
3. [Virtual Environments](#virtual-environments)
4. [pyproject.toml Explained](#pyprojecttoml-explained)
5. [Common Errors & Solutions](#common-errors--solutions)
6. [Testing & Type Checking](#testing--type-checking)
7. [Important Commands Reference](#important-commands-reference)
8. [Tool Comparison: uv vs pytest vs mypy](#tool-comparison-uv-vs-pytest-vs-mypy)
9. [Workflow Diagram](#workflow-diagram)
10. [Key Concepts Explained](#key-concepts-explained)

---

## Project Structure

### Professional Folder Layout
D:\DSA
├── app/ → Entry points (CLI scripts, API routes, user-facing code)
├── core/ → Domain logic (pure Python DSA implementations)
├── agents/ → Future LangGraph agents & orchestrators
├── tools/ → Future tool wrappers for agents
├── rag/ → Future retrieval & embedding logic
├── eval/ → Tests, benchmarks, LeetCode solutions
├── infra/ → Shell scripts, Docker, configs (operational code)
├── .venv/ → Virtual environment (isolated Python)
├── pyproject.toml → Project metadata and dependencies
├── README.md → Project documentation
└── uv.lock → Locked dependency versions (auto-generated)

text

### Why This Structure?

| Folder | Purpose | What goes here |
|--------|---------|----------------|
| `app/` | Entry points | CLI scripts, FastAPI routes, anything user calls directly |
| `core/` | Business logic | Pure Python algorithms, data structures, no frameworks |
| `eval/` | Testing | pytest files, benchmarks, LeetCode solutions |
| `infra/` | Operations | Dockerfiles, shell scripts, CI/CD configs |

**Key Principle:** Separation of concerns - change your CLI without touching algorithms, or swap algorithms without breaking the interface.

---

## Package Management with uv

### What is uv?

uv is a **Python package manager written in Rust** - 10-100x faster than pip.

### Common uv Commands

```bash
uv venv                      # Create virtual environment
uv pip install package       # Install a package
uv pip install -e .          # Install current project (editable mode)
uv pip install -e ".[dev]"   # Install with dev dependencies
uv pip list                  # List installed packages
uv pip uninstall package     # Remove a package
uv pip cache clean           # Clear download cache
Why uv instead of pip?
Feature	pip	uv
Speed	Slow (2-5 seconds)	Fast (0.2-0.5 seconds)
Language	Python	Rust
Parallel downloads	No	Yes
Smart caching	Limited	Aggressive
Virtual env management	Manual	Built-in
Virtual Environments
What is a Virtual Environment?
An isolated Python installation for your project - keeps dependencies separate from system Python.

Why Use Virtual Environments?
text
Without venv:
System Python (C:\Python311\)
├── Project A's packages
├── Project B's packages  ← CONFLICTS!
└── Project C's packages

With venv:
Project A/.venv/     ← Only Project A's packages
Project B/.venv/     ← Only Project B's packages
Project C/.venv/     ← Only Project C's packages
Virtual Environment Commands
bash
# Create venv
uv venv

# Activate (Windows PowerShell)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate

# Deactivate
deactivate

# Delete venv (just delete the folder)
rm -rf .venv          # Mac/Linux
rmdir /s .venv        # Windows
Note: activate is a script you RUN, not a folder you CD into!

Common Activation Mistake
bash
# WRONG - trying to CD into a file
cd .venv\Scripts\activate

# CORRECT - run the script
.venv\Scripts\activate
pyproject.toml Explained
Complete Working Example
toml
[project]
name = "dsa"
version = "0.1.0"
description = "Stage 2: DSA + Linux + AI Dev Tools"
readme = "README.md"
requires-python = ">=3.11"

dependencies = [
    "pydantic>=2.0",        # Runtime dependencies
]

[project.optional-dependencies]
dev = [
    "mypy>=1.0",            # Type checking
    "pytest>=7.0",          # Testing
    "black>=23.0",          # Formatting
    "ruff>=0.1.0",          # Linting
]

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["."]
include = ["app*", "core*"]
exclude = ["agents*", "tools*", "rag*", "eval*", "infra*"]

[tool.black]
line-length = 88
target-version = ['py311']

[tool.ruff]
line-length = 88
select = ["E", "F", "I", "N", "W"]
Key Sections Explained
Section	Purpose
[project]	Metadata - name, version, description
dependencies	REQUIRED packages (always installed)
[project.optional-dependencies]	OPTIONAL packages (install with ".[dev]")
[build-system]	How to build your package
[tool.setuptools.packages.find]	Which folders are Python packages
[tool.black]	Configuration for Black formatter
[tool.ruff]	Configuration for Ruff linter
Dependencies vs Optional Dependencies
toml
dependencies = [
    "pydantic>=2.0",     # REQUIRED - code won't run without this
]

[project.optional-dependencies]
dev = [
    "pytest",            # OPTIONAL - only needed for development
    "mypy",              # OPTIONAL - only needed for type checking
]
Installation difference:

bash
uv pip install .         # Only installs pydantic
uv pip install ".[dev]"  # Installs pydantic + pytest + mypy
requires-python = ">=3.11"
Means: Python 3.11 OR ANY newer version (3.12, 3.13, etc.)

If someone tries Python 3.9 → installation FAILS immediately

Prevents subtle compatibility bugs

Common Errors & Solutions
Error 1: "No virtual environment found"
bash
error: No virtual environment found; run 'uv venv' to create an environment
Solution:

bash
uv venv
.venv\Scripts\activate
uv pip install -e ".[dev]"
Error 2: "does not appear to be a Python project"
bash
error: D:\DSA does not appear to be a Python project, as neither 'pyproject.toml' nor 'setup.py' are present
Solution: Create pyproject.toml in the current directory.

Error 3: "Multiple top-level packages discovered"
bash
error: Multiple top-level packages discovered in a flat-layout: 
['app', 'rag', 'core', 'eval', 'infra', 'agents']
Solution: Add __init__.py to ALL folders OR add package discovery section:

toml
[tool.setuptools.packages.find]
where = ["."]
include = ["app*", "core*"]
exclude = ["agents*", "tools*", "rag*", "eval*", "infra*"]
Error 4: Mismatched folder names
bash
# Wrong folder
cd D:\DSA\Scripts\activate

# Correct
cd D:\DSA
.venv\Scripts\activate
Error 5: Hardlink warning (harmless)
bash
warning: Failed to hardlink files; falling back to full copy.
Solution: Ignore or suppress with:

bash
$env:UV_LINK_MODE = "copy"
Testing & Type Checking
What is assert?
assert is a testing statement that checks if a condition is TRUE.

python
assert condition, "Optional error message"

# If condition is True → nothing happens (test passes)
# If condition is False → raises AssertionError (test fails)
Why use assert instead of just calling functions?
python
# WITHOUT assert - just runs, no verification
s.push(10)
s.pop()           # Returns 10 but we don't verify

# WITH assert - verifies the result
s.push(10)
assert s.size() == 1    # Verifies size increased
assert s.pop() == 10    # Verifies correct value
Example Stack Test
python
def test_push():
    s = Stack[int]()
    s.push(5)
    assert s.size() == 1      # Test passes if size is 1
    assert s.peek() == 5      # Test passes if top is 5
Pytest Flags
Flag	Meaning	Example
-v	Verbose - shows each test name	pytest -v
--tb=short	Short traceback on error	pytest --tb=short
--tb=long	Full traceback with variables	pytest --tb=long
-k "pattern"	Run tests matching pattern	pytest -k "push"
--cov	Show test coverage	pytest --cov=core
What -v does (verbose):
bash
# Without -v
==========================
9 passed in 0.12s

# With -v
==========================
eval/test_stack.py::TestStack::test_new_stack_is_empty PASSED
eval/test_stack.py::TestStack::test_push_adds_item PASSED
eval/test_stack.py::TestStack::test_multiple_pushes PASSED
...
What --tb=short does:
bash
# Long traceback (default)
test_stack.py:15: in test_something
    assert result == 3
E   assert 5 == 3
E   +  where 5 = calculate()
    ... (full call stack with local variables)

# Short traceback
test_stack.py:15: AssertionError
Important Commands Reference
Navigation & Setup
bash
# Drive navigation
D:                    # Switch to D: drive
cd D:\DSA            # Go to DSA folder (from anywhere)
cd ..                # Go up one level
pwd                  # Show current path
dir                  # List files (Windows)
ls                   # List files (Mac/Linux)

# Virtual environment
uv venv              # Create venv
.venv\Scripts\activate    # Activate (Windows)
deactivate           # Exit venv
Package Management
bash
uv pip install package         # Install single package
uv pip install -e .            # Install current project
uv pip install -e ".[dev]"     # Install with dev dependencies
uv pip list                    # List all packages
uv pip show dsa                # Show package details
uv pip uninstall package       # Remove package
uv pip cache clear             # Clear cache
Testing & Type Checking
bash
# Run all tests
pytest eval/

# Run specific test file
pytest eval/test_stack.py

# Run with verbose output
pytest eval/test_stack.py -v

# Run with short error messages
pytest eval/test_stack.py --tb=short

# Run specific test by name
pytest eval/test_stack.py -k "test_push"

# Type checking
mypy core/stack.py
mypy eval/test_stack.py --ignore-missing-imports

# Format code
black core/stack.py

# Lint code
ruff check core/stack.py
Git Commands
bash
git init                        # Initialize repository
git add .                       # Stage all files
git commit -m "message"         # Commit changes
git status                      # Check status
git log --oneline              # View commit history
Tool Comparison: uv vs pytest vs mypy
Overview
Tool	Type	Purpose	When to use
uv	Package Manager	Install packages, manage dependencies	Once per project setup
pytest	Testing Framework	Run tests, verify code works	Every time you write code
mypy	Type Checker	Verify type correctness	Before committing code
Detailed Comparison
uv (Package Manager)
bash
# What it does: Manages what packages are installed
uv pip install pytest   # Downloads and installs pytest
uv pip list             # Shows what's installed
uv pip uninstall black  # Removes packages
pytest (Test Runner)
bash
# What it does: Runs your test code and reports PASS/FAIL
pytest test_stack.py    # Runs all test functions
pytest -k "push"        # Runs only tests with "push" in name
pytest --cov            # Shows test coverage
mypy (Type Checker)
bash
# What it does: Checks that types match WITHOUT running code
mypy core/stack.py      # Checks type hints
mypy --strict core/     # Strict type checking
How They Work Together
bash
# Complete workflow:
uv pip install -e ".[dev]"  # 1. Install everything
mypy core/stack.py           # 2. Check types (static analysis)
pytest eval/test_stack.py    # 3. Run tests (dynamic verification)
Analogy - Building a House
Tool	Analogy
uv	Hardware store - gets the materials (tools, packages)
mypy	Blueprint check - ensures design is correct (types match)
pytest	Building inspector - verifies everything works (tests pass)
Independence
They are NOT dependent on each other:

bash
# Can use independently:
mypy file.py      # Works without pytest
pytest test.py    # Works without mypy
uv install        # Works without either

# BUT best practice uses ALL:
uv pip install -e ".[dev]"  # Setup
mypy core/*.py              # Type check
pytest eval/                # Run tests
Workflow Diagram
Complete Development Workflow
text
┌─────────────────────────────────────────────────────────────┐
│                     START NEW PROJECT                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  1. CREATE STRUCTURE                                         │
│     mkdir D:\DSA && cd D:\DSA                                │
│     mkdir app core agents tools rag eval infra               │
│     touch README.md pyproject.toml                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  2. SETUP VIRTUAL ENVIRONMENT                                │
│     uv venv                                                  │
│     .venv\Scripts\activate                                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  3. INSTALL DEPENDENCIES                                     │
│     uv pip install -e ".[dev]"                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  4. WRITE CODE                                               │
│     Create: core/stack.py, core/queue.py                    │
│     Add type hints and docstrings                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  5. TYPE CHECK (mypy)                                       │
│     mypy core/stack.py                                       │
│     ✅ No errors? Continue                                   │
│     ❌ Errors? Fix type hints                               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  6. WRITE TESTS                                              │
│     Create: eval/test_stack.py                              │
│     Write pytest test functions with asserts                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  7. RUN TESTS (pytest)                                      │
│     pytest eval/ -v                                          │
│     ✅ All pass? Continue                                    │
│     ❌ Failures? Fix code or tests                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  8. FORMAT & LINT (black + ruff)                            │
│     black core/ eval/                                        │
│     ruff check core/ eval/                                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  9. COMMIT TO GIT                                            │
│     git add .                                                │
│     git commit -m "description"                             │
│     git push                                                 │
└─────────────────────────────────────────────────────────────┘
Tool Interaction Flow
text
┌──────────┐     ┌──────────┐     ┌──────────┐
│    uv    │────▶│   mypy   │────▶│  pytest  │
│ Install  │     │  Check   │     │   Run    │
│ Packages │     │  Types   │     │  Tests   │
└──────────┘     └──────────┘     └──────────┘
      │                │                 │
      ▼                ▼                 ▼
   Packages         Type              Test
   Available        Safety            Results
      │                │                 │
      └────────────────┼─────────────────┘
                       ▼
              ┌──────────────┐
              │   Working    │
              │   Project    │
              └──────────────┘
Key Concepts Explained
1. What is -c in python -c?
-c stands for "command" - tells Python to execute the next string as code.

bash
python -c "print('Hello World')"   # Runs the string as Python code
Use cases:

Quick testing without creating files

One-liners in terminal

Scripting and automation

Limitation: Cannot handle multi-line class definitions or complex structures.

2. What does Stack[int]() mean?
python
s = Stack[int]()    # Create a Stack that holds integers
s = Stack[str]()    # Create a Stack that holds strings
s = Stack()         # Untyped stack (any type allowed)
The [int] is a type parameter (generics) - tells the type checker what data type this stack will hold.

3. Generic Types with TypeVar
python
from typing import TypeVar, Generic

T = TypeVar('T')  # T can be any type

class Stack(Generic[T]):
    def push(self, item: T) -> None: ...
    def pop(self) -> T: ...
4. Private Attributes (underscore convention)
python
self._items = []  # Underscore means "internal use - don't touch"
self.items = []   # Public attribute (can be accessed directly)
The underscore is a convention (not enforced by Python) that tells other developers: "This is private, don't use it directly."

5. Raising Exceptions
python
if self.is_empty():
    raise IndexError("Cannot pop from empty stack")
raise - keyword to trigger an exception

IndexError - type of exception (built-in)

Message - description of what went wrong

6. LIFO vs FIFO
Structure	Order	Analogy
Stack	LIFO (Last-In-First-Out)	Stack of plates
Queue	FIFO (First-In-First-Out)	Line at a store
7. Editable Install (-e flag)
bash
uv pip install -e .  # Editable mode
Creates a symlink from your virtual environment to your code

Changes to your .py files are immediately available

No need to reinstall after every change

8. Why __init__.py?
Marks a folder as a Python package so you can import from it:

python
# Without __init__.py in core/ folder:
import core.stack  # ❌ ImportError

# With __init__.py in core/ folder:
import core.stack  # ✅ Works
Python -c Command Reference
Valid Examples
bash
# Simple print
python -c "print('hello')"

# Import and use
python -c "import math; print(math.pi)"

# Simple function
python -c "def add(a,b): return a+b; print(add(5,3))"

# Multiple statements with semicolons
python -c "x=10; y=20; print(x+y)"
Invalid Examples
bash
# Class definition (too complex)
python -c "class Test: pass"           # ❌ SyntaxError

# Multi-line structures
python -c "if True:\n    print('hi')"  # ❌ SyntaxError

# Complex imports with from/import
python -c "from math import *; print(pi)"  # ⚠️ Might work but not recommended
Quick Troubleshooting Guide
Problem	Likely Cause	Solution
uv: command not found	uv not installed	pip install uv
Activation doesn't change prompt	Wrong activation command	Use .venv\Scripts\activate (Windows)
ModuleNotFoundError	Package not installed	uv pip install -e ".[dev]"
Tests not found	Wrong directory	cd D:\DSA first
mypy errors everywhere	Missing type hints	Add type annotations to functions
Import works in IDE but not terminal	Wrong Python selected	Activate virtual environment first
Memory Aids
Tool Purposes
uv = Universal package manager (U gets packages)

pytest = Python test runner (P runs tests)

mypy = My type checker (M checks types)

Folder Purposes
app = Application entry points

core = Core business logic

eval = Evaluation & tests

infra = Infrastructure & ops

Command Flags
-v = Verbose (more detail)

-e = Editable (symlink install)

-c = Command (run string as code)

Summary Checklist
Day 1 Completion
Created folder structure (app/, core/, eval/, etc.)

Created pyproject.toml with dependencies

Created README.md

Set up virtual environment with uv

Installed packages with uv pip install -e ".[dev]"

Verified installation with uv pip list

Initialized git repository

Day 2 Progress
Understood type hints and generics

Implemented Stack class with full methods

Wrote pytest tests for Stack

All 9 tests passing

mypy type checking passes

Understood difference between uv, pytest, mypy

Additional Resources
uv Documentation

pytest Documentation

mypy Documentation

Python Type Hints

setuptools Documentation

*Documentation created: 2026-05-05*
*Project: Stage 2 - DSA + Linux + AI Dev Tools*

text

Now save the file and verify it was created:

```powershell
# Check the file exists
dir docs.md

# Open it in your editor to review
code docs.md
This markdown file contains everything we discussed:

✅ All your questions with detailed answers

✅ Flowcharts and workflow diagrams

✅ Command references

✅ Error solutions

✅ Tool comparisons

✅ Quick memory aids

The file is saved as docs.md in your D:\DSA folder. You can reference it anytime you need to remember a concept or command.

Ready to continue with the Queue implementation when you are! 🚀

