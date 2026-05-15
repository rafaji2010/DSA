# LeetCode Solutions - Stage 2

Collection of LeetCode problems solved during DSA practice.

---

## 📊 Problem Tracker

### Week 1
| # | Problem | Solution | Difficulty | Key Insight |
|---|---------|----------|------------|--------------|
| 167 | Two Sum II | [lc_167_two_sum_ii.py](lc_167_two_sum_ii.py) | Easy | Two pointers (opposite ends) |
| 26 | Remove Duplicates | [lc_26_remove_duplicates.py](lc_26_remove_duplicates.py) | Easy | Two pointers (same direction) |
| 977 | Squares of Sorted Array | [lc_977_squares_sorted.py](lc_977_squares_sorted.py) | Easy | Two pointers from ends |
| 704 | Binary Search | [lc_704_binary_search.py](lc_704_binary_search.py) | Easy | Divide and conquer, O(log n) |

### Week 2
| # | Problem | Solution | Difficulty | Key Insight |
|---|---------|----------|------------|--------------|
| 1 | Two Sum | [lc_001_two_sum.py](lc_001_two_sum.py) | Easy | Hash map for O(n) lookup |
| 20 | Valid Parentheses | [lc_020_valid_parentheses.py](lc_020_valid_parentheses.py) | Easy | Stack for bracket matching |
| 21 | Merge Two Sorted Lists | [lc_021_merge_sorted_lists.py](lc_021_merge_sorted_lists.py) | Easy | Two pointers (merge step) |
| 141 | Linked List Cycle | [lc_141_linked_list_cycle.py](lc_141_linked_list_cycle.py) | Easy | Floyd's cycle detection |
| 155 | Min Stack | [lc_155_min_stack.py](lc_155_min_stack.py) | Medium | Auxiliary stack for O(1) getMin |
| 206 | Reverse Linked List | [lc_206_reverse_linked_list.py](lc_206_reverse_linked_list.py) | Easy | Three pointers (prev, curr, next) |
| 225 | Stack using Queues | [lc_225_stack_using_queues.py](lc_225_stack_using_queues.py) | Easy | Two queues, rotate for LIFO |
| 232 | Queue using Stacks | [lc_232_queue_using_stacks.py](lc_232_queue_using_stacks.py) | Easy | Two stacks, transfer for FIFO |
| 876 | Middle of Linked List | [lc_876_middle_linked_list.py](lc_876_middle_linked_list.py) | Easy | Tortoise and hare (fast/slow) |

**Total: 13 problems solved** (9 Easy, 4 Medium)

---

## 🧠 Patterns Learned

| Pattern | Problems | Key Insight |
|---------|----------|--------------|
| **Two Pointers** | 26, 167, 977, 21 | Move pointers based on condition, O(n) instead of O(n²) |
| **Hash Map** | 1, 167 | "Have I seen this before?" becomes O(1) |
| **Stack** | 20, 155, 225 | LIFO for matching, history, and reversal |
| **Queue** | 225, 232 | FIFO for order preservation |
| **Fast/Slow Pointers** | 141, 876 | 2x speed for cycle detection and middle |
| **Recursion** | 206 | Call stack unwinding for reversal |

---

## 🚀 How to Run

