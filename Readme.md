\# Stage 2: DSA + Linux + AI Dev Tools



\## What This Project Is

A structured learning environment for mastering Data Structures \& Algorithms, Linux fundamentals, and AI development tools. This repo follows production-grade architecture patterns used in agentic AI systems.



\## Project Structure

stage-2-dsa/

├── app/ → Entry points (CLI, API routes)

├── core/ → Domain logic (pure Python DSA implementations)

├── agents/ → Future LangGraph agents \& orchestrators

├── tools/ → Future tool wrappers for agents

├── rag/ → Future retrieval \& embedding logic

├── eval/ → Tests, benchmarks, LeetCode solutions

└── infra/ → Shell scripts, Docker, configs



text



\## Installation



```bash

\# Install uv (if not already installed)

pip install uv



\# Install project dependencies

uv pip install -e .



Development Setup

\# Install with dev dependencies

uv pip install -e ".\[dev]"

Project Goal

By the end of Stage 2, this repo will contain a complete DSA library with 50+ LeetCode solutions, all type-checked, tested, and organised in a professional project structure ready for LangGraph integration.



text



\## Step 5: Write the pyproject.toml File



```powershell

\# Open pyproject.toml in Notepad

notepad pyproject.toml

Copy and paste this exact content:



toml

\[project]

name = "stage-2-dsa"

version = "0.1.0"

description = "Stage 2: DSA + Linux + AI Dev Tools — AJ's Coding Journey"

readme = "README.md"

requires-python = ">=3.11"

license = { text = "MIT" }

authors = \[

&#x20;   { name = "Your Name", email = "your.email@example.com" }

]



dependencies = \[

&#x20;   "pydantic>=2.0",

]



\[project.optional-dependencies]

dev = \[

&#x20;   "mypy>=1.0",

&#x20;   "pytest>=7.0",

&#x20;   "black>=23.0",

&#x20;   "ruff>=0.1.0",

]



\[build-system]

requires = \["setuptools>=61.0"]

build-backend = "setuptools.build\_meta"



\[tool.black]

line-length = 88

target-version = \['py311']



\[tool.ruff]

line-length = 88

select = \["E", "F", "I", "N", "W"]


# Day 2 (using WSL command lines)

# DSA Implementations in Python

Type-safe data structure implementations with 100% test coverage and performance benchmarks.

## 🚀 Quick Start

```bash
# Clone/cd into project
cd /mnt/d/DSA

# Install with uv
uv pip install -e ".[dev]"

# Run tests
pytest

# Type check
mypy src/
📁 Project Structure
text
src/
├── interfaces/      # Abstract base classes (what each DS must implement)
├── data_structures/ # Concrete implementations (Stack, Queue, etc.)
tests/               # pytest test suite with 100% coverage
📊 Implemented Data Structures
Structure	Time Complexity	Space Complexity	Tests
Stack (list-based)	Push/Pop O(1)	O(n)	12 ✅
Queue (deque-based)	Enqueue/Dequeue O(1)	O(n)	15 ✅
🔧 Development Commands
bash
pytest -v --cov=src          # Run tests with coverage
mypy src/                    # Type check all code
black src/ tests/            # Format code
ruff check src/              # Lint code
📈 Performance
Run benchmarks to see O(1) vs O(n²) differences:

bash
python benchmarks/speed.py
text

## 6. Your Action Items RIGHT NOW:

**Task 1:** Run the editable install:
```bash
cd /mnt/d/DSA
uv pip install -e ".[dev]"
Paste output here 👇

Task 2: While waiting, add space complexity comments to your Stack and Queue.

Example for Stack:

python
class Stack(StackInterface[T]):
    """Stack implementation using Python list.
    
    Space Complexity: O(n) where n = number of elements
    - Each element stored once in the underlying list
    - No auxiliary structures used
    """
    def __init__(self) -> None:
        self._items: list[T] = []  # O(n) space



