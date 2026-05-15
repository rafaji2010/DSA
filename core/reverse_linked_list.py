"""
core/reverse_linked_list.py
LeetCode 206 — Reverse Linked List

Reverse a singly linked list.
Time: O(n) — visit each node once
Space: O(1) — only 3 pointers
"""

from __future__ import annotations
from typing import Optional, TypeVar, Generic
from core.linked_list import LinkedList, Node

T = TypeVar("T")


def reverse_linked_list_iterative(head: Optional[Node[T]]) -> Optional[Node[T]]:
    """
    Reverse linked list using three pointers.
    
    The trick: We need to reverse the direction of each 'next' pointer.
    To do this without losing the rest of the list, we track:
        - prev: the node we've already reversed (starts as None)
        - current: the node we're currently processing (starts as head)
        - next_temp: the next node to process (current.next before we change it)
    
    Algorithm:
        1. Save current.next in next_temp
        2. Reverse the pointer: current.next = prev
        3. Move prev forward: prev = current
        4. Move current forward: current = next_temp
        5. Repeat until current is None
    
    At the end, prev is pointing to the new head (old tail)
    """
    prev: Optional[Node[T]] = None
    current = head
    
    # Debug: Add breakpoint here to watch pointer manipulation
    # breakpoint()
    
    while current is not None:
        # Step 1: Save the next node BEFORE we overwrite current.next
        next_temp = current.next
        
        # Step 2: Reverse the pointer (make current point backward)
        current.next = prev
        
        # Step 3: Move prev forward to current
        prev = current
        
        # Step 4: Move current forward to next_temp
        current = next_temp
    
    # After loop, prev is the new head (original tail)
    return prev


def reverse_linked_list_recursive(head: Optional[Node[T]]) -> Optional[Node[T]]:
    """
    Reverse linked list recursively.
    
    Base case: empty list or single node → return itself
    
    Recursive case: 
        1. Reverse the rest of the list (from head.next onward)
        2. The rest's tail is now head.next (after reversal)
        3. Point head.next.next to head (this reverses the last link)
        4. Point head.next to None (old head becomes new tail)
    
    Time: O(n) — visit each node once
    Space: O(n) — call stack depth equals list length
    """
    # Base case: empty list or single node
    if head is None or head.next is None:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverse_linked_list_recursive(head.next)
    
    # At this point:
    # - new_head is the tail of original list (now head of reversed)
    # - head.next is the node that was after head (now the tail of reversed rest)
    # - head.next.next is None (since that node was the tail)
    #
    # We need to reverse the connection:
    # Original: head → head.next → (reversed rest)
    # After recursion: head → head.next ← ... (head.next is now tail of reversed)
    # We want: head ← head.next ← ... (head becomes new tail)
    
    # Make the node that was after head point back to head
    head.next.next = head
    
    # Break the original forward link (head now becomes tail)
    head.next = None
    
    return new_head


def reverse_print_demo(head: Optional[Node[T]], step: int = 0) -> Optional[Node[T]]:
    """
    Debug version with visualization.
    Use this to watch the reversal process!
    """
    prev: Optional[Node[T]] = None
    current = head
    
    print("\n=== Starting Reverse ===")
    print(f"Initial: {_list_to_string(current)}")
    print()
    
    step_num = 0
    while current is not None:
        print(f"Step {step_num}:")
        print(f"  prev    → {_node_str(prev)}")
        print(f"  current → {_node_str(current)}")
        
        # Save next
        next_temp = current.next
        print(f"  Saved next_temp = Node({current.value if current else 'None'}).next = {_node_str(next_temp)}")
        
        # Reverse pointer
        current.next = prev
        print(f"  AFTER REVERSE: current.next now points to {_node_str(prev)}")
        
        # Move pointers
        prev = current
        current = next_temp
        print(f"  Moved: prev = Node({prev.value if prev else 'None'}), current = {_node_str(current)}")
        
        step_num += 1
        print()
    
    print(f"Final: prev = {_node_str(prev)} (NEW HEAD!)")
    print(f"Reversed list: {_list_to_string(prev)}")
    
    return prev


def _node_str(node: Optional[Node[T]]) -> str:
    """Helper for debugging output"""
    if node is None:
        return "None"
    return f"Node({node.value})"


def _list_to_string(head: Optional[Node[T]]) -> str:
    """Convert linked list to string for visualization"""
    values: list[str] = []
    current = head
    while current is not None:
        values.append(str(current.value))
        current = current.next
    return " → ".join(values) + " → None"


def create_test_list(values: list[T]) -> Optional[Node[T]]:
    """Create linked list from Python list"""
    if not values:
        return None
    
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


def list_to_array(head: Optional[Node[T]]) -> list[T]:
    """Convert linked list back to Python list"""
    result: list[T] = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result


if __name__ == "__main__":
    # Test 1: Normal list
    print("=" * 50)
    print("TEST 1: Normal list [1, 2, 3, 4, 5]")
    print("=" * 50)
    
    head1 = create_test_list([1, 2, 3, 4, 5])
    print(f"Original: {_list_to_string(head1)}")
    
    reversed1 = reverse_linked_list_iterative(head1)
    print(f"Reversed: {_list_to_string(reversed1)}")
    print()
    
    # Test 2: Single node
    print("=" * 50)
    print("TEST 2: Single node [42]")
    print("=" * 50)
    
    head2 = create_test_list([42])
    print(f"Original: {_list_to_string(head2)}")
    
    reversed2 = reverse_linked_list_iterative(head2)
    print(f"Reversed: {_list_to_string(reversed2)}")
    print()
    
    # Test 3: Two nodes
    print("=" * 50)
    print("TEST 3: Two nodes [1, 2]")
    print("=" * 50)
    
    head3 = create_test_list([1, 2])
    print(f"Original: {_list_to_string(head3)}")
    
    reversed3 = reverse_linked_list_iterative(head3)
    print(f"Reversed: {_list_to_string(reversed3)}")
    print()
    
    # Test 4: Recursive version
    print("=" * 50)
    print("TEST 4: Recursive reverse [1, 2, 3, 4, 5]")
    print("=" * 50)
    
    head4 = create_test_list([1, 2, 3, 4, 5])
    print(f"Original: {_list_to_string(head4)}")
    
    reversed4 = reverse_linked_list_recursive(head4)
    print(f"Reversed (recursive): {_list_to_string(reversed4)}")
    print()
    
    # Test 5: Debug visualization
    print("=" * 50)
    print("TEST 5: Debug visualization (watch the pointers!)")
    print("=" * 50)
    
    head5 = create_test_list([1, 2, 3, 4])
    reverse_print_demo(head5)