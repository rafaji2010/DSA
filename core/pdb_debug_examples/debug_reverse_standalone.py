"""
core/pdb_debug_examples/debug_reverse_standalone.py
Self-contained version for pdb debugging - no import issues!
"""

from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    """A single node in a linked list."""
    
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: Optional[Node[T]] = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


def reverse_linked_list_iterative(head: Optional[Node[T]]) -> Optional[Node[T]]:
    """
    Reverse linked list using three pointers.
    """
    prev: Optional[Node[T]] = None
    current = head
    
    # We'll put breakpoint here later
    # breakpoint()
    
    while current is not None:
        # Save the next node BEFORE we overwrite current.next
        next_temp = current.next
        
        # Reverse the pointer
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_temp
    
    return prev


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


def list_to_string(head: Optional[Node[T]]) -> str:
    """Convert linked list to string for visualization"""
    values: list[str] = []
    current = head
    while current is not None:
        values.append(str(current.value))
        current = current.next
    return " → ".join(values) + " → None"


def visualize_reversal(head: Optional[Node[T]]) -> Optional[Node[T]]:
    """
    Debug version with step-by-step visualization.
    """
    prev: Optional[Node[T]] = None
    current = head
    
    print("\n" + "="*60)
    print("STARTING REVERSE")
    print(f"Original: {list_to_string(current)}")
    print("="*60)
    
    step = 0
    while current is not None:
        print(f"\n--- STEP {step} ---")
        print(f"  Before: prev={prev}, current={current}")
        
        next_temp = current.next
        print(f"  next_temp = {next_temp}")
        
        current.next = prev
        print(f"  After reverse: current.next = {prev}")
        
        prev = current
        current = next_temp
        print(f"  After move: prev={prev}, current={current}")
        
        step += 1
    
    print("\n" + "="*60)
    print(f"REVERSED: {list_to_string(prev)}")
    print("="*60)
    
    return prev


if __name__ == "__main__":
    # Create a test list
    head = create_test_list([1, 2, 3, 4, 5])
    
    # UNCOMMENT ONE OF THESE APPROACHES:
    
    # APPROACH 1: Just run normally
    # reversed_head = reverse_linked_list_iterative(head)
    # print(f"Reversed: {list_to_string(reversed_head)}")
    
    # APPROACH 2: Visualize the reversal
    # visualize_reversal(head)
    
    # APPROACH 3: Use pdb with breakpoint() - BEST FOR LEARNING
    breakpoint()  # ← This will pause execution here
    reversed_head = reverse_linked_list_iterative(head)
    print(f"Reversed: {list_to_string(reversed_head)}")