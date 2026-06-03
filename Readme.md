# DSA Learning Repository

**Stage 2 of AJ's 24-month Agentic AI Engineering Roadmap**
*Data Structures, Algorithms, Linux/CLI, and AI Dev Tools*

---

## 📚 What's Inside

This repository contains my implementation of core data structures and algorithms from scratch, along with LeetCode solutions and Linux command-line practice.

---

## 🏗️ Project Structure
DSA/
├── core/ # Core DSA implementations
│ ├── stack.py # Stack (list-based)
│ ├── stack_linked.py # Stack (LinkedList-based)
│ ├── queue.py # Queue (deque-based)
│ ├── linked_list.py # Complete LinkedList implementation
│ ├── circular_buffer.py # Ring buffer
│ ├── binary_search.py # Binary search (iterative + recursive)
│ ├── two_pointers.py # Two pointers pattern
│ ├── pydantic_models.py # Pydantic validation examples
│ └── pdb_debug_examples/ # pdb debugging practice
├── eval/ # Evaluation & LeetCode
│ ├── leetcode/ # LeetCode solutions
│ │ ├── lc_001_two_sum.py
│ │ ├── lc_020_valid_parentheses.py
│ │ ├── lc_021_merge_sorted_lists.py
│ │ ├── lc_026_remove_duplicates.py
│ │ ├── lc_141_linked_list_cycle.py
│ │ ├── lc_155_min_stack.py
│ │ ├── lc_167_two_sum_ii.py
│ │ ├── lc_206_reverse_linked_list.py
│ │ ├── lc_225_stack_using_queues.py
│ │ ├── lc_232_queue_using_stacks.py
│ │ ├── lc_704_binary_search.py
│ │ ├── lc_876_middle_linked_list.py
│ │ └── lc_977_squares_sorted.py
│ └── test_*.py # pytest test files
├── benchmarks/ # Performance benchmarks
│ ├── binary_search_scale.py
│ ├── deque_vs_list.py
│ └── array_operations_timing.py
└── pyproject.toml # Project configuration

text

---

## ✅ What I've Built (Week 1-2)

### Week 1: Foundations
- ✅ Big O analysis (O(1), O(n), O(n²), O(log n))
- ✅ Binary search (iterative + recursive)
- ✅ pdb debugging with breakpoints
- ✅ Two Pointers pattern (LeetCode 167, 26, 977)
- ✅ Type hints with mypy --strict

### Week 2: Core Data Structures
- ✅ **Linked List** - Complete implementation
  - `append()`, `prepend()`, `delete()`, `search()`
  - `reverse()` (iterative + recursive)
  - `find_middle()` (tortoise and hare)
- ✅ **Stack** - Two implementations
  - List-based (built-in)
  - LinkedList-based (composition)
- ✅ **Queue** - deque-based with O(1) operations
- ✅ **Circular Buffer** - Fixed-size ring buffer with modulo wrap
- ✅ **Min Stack** - O(1) getMin with auxiliary stack

### Linux Commands Mastered
- `grep` (recursive, line numbers, count, invert)
- `find` (name, type, size, mtime)
- `sed` (stream editing, find/replace)
- `awk` (column extraction)
- `uniq` (duplicate counting with `-c`)
- `less` (pagination, search, follow mode)
- Pipe `|` composition

### LeetCode Solved (Week 2)
| # | Problem | Key Insight |
|---|---------|--------------|
| 1 | Two Sum | Hash map for O(n) |
| 20 | Valid Parentheses | Stack for matching |
| 21 | Merge Two Sorted Lists | Two pointers |
| 141 | Linked List Cycle | Floyd's algorithm |
| 155 | Min Stack | Auxiliary stack |
| 206 | Reverse Linked List | Three pointers |
| 225 | Stack using Queues | Two queues + rotate |
| 232 | Queue using Stacks | Two stacks + transfer |
| 876 | Middle of Linked List | Tortoise and hare |

**Total LeetCode: 13 problems**

---

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.11+
- `uv` package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/DSA.git
cd DSA

# Install uv (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
uv venv

# Activate it
source .venv/bin/activate

# Install dependencies
uv pip install -e ".[dev]"
Type Checking
bash
mypy --strict core/
Running Tests
bash
pytest tests/ -v
📊 Performance Benchmarks
bash
# Compare linear vs binary search
python benchmarks/binary_search_scale.py

# Compare list.pop(0) vs deque.popleft()
python benchmarks/deque_vs_list.py

# Time array operations (O(1) vs O(n))
python benchmarks/array_operations_timing.py
🐛 Debugging with pdb
bash
# Run with debugger
python -m pdb core/stack.py

# Common pdb commands:
# n - next line
# s - step into function
# p var - print variable
# c - continue
# w - show call stack
📈 Progress Tracker
Metric	Week 1	Week 2	Target
LeetCode	4	13	20
Data Structures	2	5	10
Linux Commands	8	15+	20
pdb usage	Learning	Every session	Every session
🎯 Next Up (Week 3)
Hash tables (implement from scratch)

Trees and Binary Search Trees

BFS and DFS on graphs

Sorting algorithms (merge, quick)

More LeetCode (target: 20 total)

📝 License
MIT - Learning purposes only

Made with ☕ and ⌨️ during Stage 2 of the Agentic AI Engineering Roadmap
#SSH test
