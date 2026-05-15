"""
core/middle_linked_list.py
LeetCode 876 — Middle of the Linked List

Find the middle node using the tortoise and hare algorithm.
Time: O(n) — single pass
Space: O(1) — only two pointers
"""

from __future__ import annotations
from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    """A single node in a linked list."""
    
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: Optional[Node[T]] = None


def create_linked_list(values: list[T]) -> Optional[Node[T]]:
    """Convert Python list to linked list."""
    if not values:
        return None
    
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


def linked_list_to_string(head: Optional[Node[T]]) -> str:
    """Convert linked list to readable string."""
    values: list[str] = []
    current = head
    while current is not None:
        values.append(str(current.value))
        current = current.next
    return " → ".join(values) + " → None"


def find_middle_tortoise_hare(head: Optional[Node[T]]) -> Optional[Node[T]]:
    """
    Find middle node using tortoise and hare (fast/slow pointers).
    
    Algorithm:
        1. Initialize slow and fast pointers to head
        2. Move slow 1 step, fast 2 steps
        3. When fast reaches end, slow is at middle
    
    Why this works:
        - fast moves twice as fast as slow
        - When fast reaches end (n steps), slow has taken n/2 steps
        - n/2 steps from start = middle position
    
    Returns:
        Middle node (second middle if even length)
    """
    # Empty list → no middle
    if head is None:
        return None
    
    slow = head  # Tortoise 🐢
    fast = head  # Hare 🐇
    
    # While fast can move 2 steps...
    while fast is not None and fast.next is not None:
        slow = slow.next      # Move 1 step
        fast = fast.next.next # Move 2 steps
    
    # slow now points to the middle
    return slow


def find_middle_two_pass(head: Optional[Node[T]]) -> Optional[Node[T]]:
    """
    Alternative: Count nodes first, then go to middle.
    
    Algorithm:
        1. First pass: count total nodes
        2. Second pass: go to middle index
    
    Time: O(n) — two passes
    Space: O(1)
    
    This is simpler to understand but requires two traversals.
    """
    if head is None:
        return None
    
    # Pass 1: Count nodes
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    
    # Pass 2: Go to middle index
    middle_index = count // 2  # Integer division gives second middle for even
    current = head
    for _ in range(middle_index):
        current = current.next
    
    return current


def find_middle_brute_force(head: Optional[Node[T]]) -> Optional[Node[T]]:
    """
    Brute force: convert to array, then index.
    
    Time: O(n) — but uses O(n) extra space
    Space: O(n) — stores all nodes in array
    
    This is the easiest to understand but uses more memory.
    """
    if head is None:
        return None
    
    # Convert to array
    nodes: list[Node[T]] = []
    current = head
    while current is not None:
        nodes.append(current)
        current = current.next
    
    # Return middle element
    middle_index = len(nodes) // 2
    return nodes[middle_index]


def find_middle_with_trace(head: Optional[Node[T]]) -> Optional[Node[T]]:
    """
    Debug version with step-by-step tracing.
    """
    if head is None:
        print("Empty list → No middle")
        return None
    
    slow = head
    fast = head
    
    print(f"Starting: slow={slow.value}, fast={fast.value}")
    print("-" * 40)
    
    step = 0
    while fast is not None and fast.next is not None:
        step += 1
        print(f"Step {step}:")
        print(f"  Before: slow={slow.value}, fast={fast.value}")
        
        slow = slow.next
        fast = fast.next.next
        
        print(f"  After:  slow={slow.value}, fast={fast.value if fast else 'None'}")
        print()
    
    print(f"✅ Middle found: {slow.value}")
    return slow


# ──────────────────────────────────────────────────────────────
# TEST CODE
# ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 70)
    print("MIDDLE OF LINKED LIST - TORTOISE AND HARE")
    print("=" * 70)
    
    test_cases = [
        ([1, 2, 3, 4, 5], "Odd length (5 nodes)"),
        ([1, 2, 3, 4], "Even length (4 nodes)"),
        ([1], "Single node"),
        ([1, 2], "Two nodes"),
        ([], "Empty list"),
    ]
    
    for values, description in test_cases:
        head = create_linked_list(values)
        print(f"\n{description}:")
        print(f"  List: {linked_list_to_string(head)}")
        
        middle = find_middle_tortoise_hare(head)
        
        if middle:
            print(f"  Middle value: {middle.value}")
        else:
            print("  Middle value: None")
    
    # Detailed trace for odd length
    print("\n" + "=" * 70)
    print("DETAILED TRACE - Odd Length [1,2,3,4,5]")
    print("=" * 70 + "\n")
    
    head_odd = create_linked_list([1, 2, 3, 4, 5])
    find_middle_with_trace(head_odd)
    
    # Detailed trace for even length
    print("\n" + "=" * 70)
    print("DETAILED TRACE - Even Length [1,2,3,4]")
    print("=" * 70 + "\n")
    
    head_even = create_linked_list([1, 2, 3, 4])
    find_middle_with_trace(head_even)
    
    # Compare all three approaches
    print("\n" + "=" * 70)
    print("COMPARING ALL THREE APPROACHES")
    print("=" * 70)
    
    test_list = [1, 2, 3, 4, 5, 6, 7]
    head = create_linked_list(test_list)
    print(f"List: {linked_list_to_string(head)}")
    print()
    
    import time
    
    # Approach 1: Tortoise and Hare (most efficient)
    start = time.perf_counter_ns()
    result1 = find_middle_tortoise_hare(head)
    time1 = time.perf_counter_ns() - start
    print(f"🐢🐇 Tortoise & Hare:  middle={result1.value if result1 else 'None'}, time={time1}ns")
    
    # Create fresh list for second approach
    head2 = create_linked_list(test_list)
    start = time.perf_counter_ns()
    result2 = find_middle_two_pass(head2)
    time2 = time.perf_counter_ns() - start
    print(f"📊 Two Pass:          middle={result2.value if result2 else 'None'}, time={time2}ns")
    
    # Create fresh list for third approach
    head3 = create_linked_list(test_list)
    start = time.perf_counter_ns()
    result3 = find_middle_brute_force(head3)
    time3 = time.perf_counter_ns() - start
    print(f"💾 Brute Force:       middle={result3.value if result3 else 'None'}, time={time3}ns")