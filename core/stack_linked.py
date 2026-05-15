"""
core/stack_linked.py
Stack implementation using LinkedList from Day 6
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from typing import TypeVar, Generic, Optional
from core.linked_list import LinkedList

T = TypeVar("T")


class StackLinked(Generic[T]):
    """
    LIFO Stack implemented with a Linked List.
    All operations are O(1).
    
    This demonstrates that Stack is an INTERFACE (what operations)
    that can be implemented with different underlying data structures.
    """
    
    def __init__(self) -> None:
        """Initialize empty stack using LinkedList."""
        self._list: LinkedList[T] = LinkedList()
    
    def push(self, item: T) -> None:
        """
        Add item to top of stack.
        Time: O(1) - prepend is constant time.
        """
        self._list.prepend(item)
    
    def pop(self) -> T:
        """
        Remove and return top item.
        Time: O(1) - delete from head is constant time.
        Raises IndexError if stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        
        # Get value from head before deleting
        value = self._list._head.value if self._list._head else None
        if value is None:
            raise IndexError("pop from empty stack")
        
        self._list.delete_at_index(0)
        return value
    
    def peek_head(self) -> Optional[T]:
        """Return head value without removing. O(1)."""
        return self._head.value if self._head else None
    
    
    def peek(self) -> T:
        """
        Return top item without removing.
        Time: O(1) - direct head access.
        Raises IndexError if stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek at empty stack")
        
        value = self._list.peek_head()
        if value is None:
            raise IndexError("peek at empty stack")
        return value
        # Head is the top of stack (since we prepend)
            
    def is_empty(self) -> bool:
        """Return True if stack has no items."""
        return self._list.is_empty()
    
    def size(self) -> int:
        """Return number of items in stack."""
        return self._list.size()
    
    def __repr__(self) -> str:
        """Show stack contents (top to bottom)."""
        if self.is_empty():
            return "StackLinked(empty)"
        
        # Collect values from head (top) to tail (bottom)
        values = []
        current = self._list._head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        
        return f"StackLinked(top → {' → '.join(values)} → bottom)"
    
    def __len__(self) -> int:
        """Allow len(stack) syntax."""
        return self.size()


if __name__ == "__main__":
    print("=" * 50)
    print("Testing StackLinked (LinkedList-based Stack)")
    print("=" * 50)
    
    # Create stack
    stack = StackLinked[int]()
    print(f"Empty stack: {stack}")
    print(f"Is empty? {stack.is_empty()}")
    
    # Push items
    print("\n--- Pushing 10, 20, 30 ---")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Stack after pushes: {stack}")
    print(f"Size: {stack.size()}")
    print(f"Is empty? {stack.is_empty()}")
    
    # Peek
    print(f"\nPeek (top item): {stack.peek()}")
    
    # Pop items
    print("\n--- Popping items ---")
    print(f"Pop: {stack.pop()}")
    print(f"Stack after pop: {stack}")
    print(f"Pop: {stack.pop()}")
    print(f"Stack after pop: {stack}")
    print(f"Pop: {stack.pop()}")
    print(f"Stack after pop: {stack}")
    
    # Test empty stack error
    print("\n--- Testing empty stack error ---")
    try:
        stack.pop()
    except IndexError as e:
        print(f"✅ Caught expected error: {e}")
    
    # Test len() and bool
    stack.push(100)
    print(f"\nAfter push(100): stack={stack}, len={len(stack)}")
    
    print("\n✅ StackLinked implementation complete!")