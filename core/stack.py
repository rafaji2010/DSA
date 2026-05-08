"""Stack data structure implementation with type hints.

A stack is a LIFO (Last-In, First-Out) data structure.
Operations:
- push: Add an item to the top
- pop: Remove and return the top item
- peek: Look at the top item without removing
- is_empty: Check if stack has no items
- size: Return number of items
"""

from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')  # Generic type - works with any data type


class Stack(Generic[T]):
    """A stack implementation using Python list as underlying storage."""
    
    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """Add an item to the top of the stack.
        
        Args:
            item: The item to add (can be any type)
        """
        self._items.append(item)
    
    def pop(self) -> T:
        """Remove and return the top item from the stack.
        
        Returns:
            The item from the top of the stack
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> T:
        """Return the top item without removing it.
        
        Returns:
            The item at the top of the stack
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek at empty stack")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Check if the stack is empty.
        
        Returns:
            True if stack has no items, False otherwise
        """
        return len(self._items) == 0
    
    def size(self) -> int:
        """Return the number of items in the stack.
        
        Returns:
            Number of items in the stack
        """
        return len(self._items)
    
    def __str__(self) -> str:
        """Return string representation of the stack."""
        return f"Stack({self._items})"
    
    def __repr__(self) -> str:
        """Return detailed string representation."""
        return f"Stack({self._items!r})"