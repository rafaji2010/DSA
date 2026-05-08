"""Stack implementation using list as underlying storage."""
from typing import TypeVar, Generic, Optional, Iterator
from src.interfaces.stack_interface import StackInterface

T = TypeVar('T')

class Stack(StackInterface[T], Generic[T]):
    """Stack implementation using Python list.
    
    Time Complexity:
        - push: O(1) amortized - occasional O(n) when list resizes
        - pop: O(1) amortized
        - peek: O(1)
        - is_empty: O(1)
        - size: O(1)
    
    Space Complexity: O(n) where n = number of elements
        - Each element stored once in self._items list
        - Python list may have capacity up to 2n for growth
        - No recursion or auxiliary structures
    """
    
    def __init__(self, max_size: Optional[int] = None) -> None:
        """Initialize an empty stack.
        
        Args:
            max_size: Maximum number of items the stack can hold (optional)
        """
        self._items: list[T] = []
        self._max_size = max_size
    
    def push(self, item: T) -> None:
        """Add an item to the top of the stack.
        
        Args:
            item: The item to add to the stack
            
        Raises:
            OverflowError: If stack is at maximum capacity
        """
        if self._max_size is not None and len(self._items) >= self._max_size:
            raise OverflowError(f"Stack is full (max size: {self._max_size})")
        self._items.append(item)
    
    def pop(self) -> Optional[T]:
        """Remove and return the item from the top of the stack.
        
        Returns:
            The item from the top of the stack, or None if stack is empty
        """
        if self.is_empty():
            return None
        return self._items.pop()
    
    def peek(self) -> Optional[T]:
        """Return the item from the top of the stack without removing it.
        
        Returns:
            The item from the top of the stack, or None if stack is empty
        """
        if self.is_empty():
            return None
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Check if the stack is empty.
        
        Returns:
            True if stack is empty, False otherwise
        """
        return len(self._items) == 0
    
    def size(self) -> int:
        """Return the number of items in the stack.
        
        Returns:
            The number of items in the stack
        """
        return len(self._items)
    
    def clear(self) -> None:
        """Remove all items from the stack."""
        self._items.clear()
    
    def __len__(self) -> int:
        """Return the number of items in the stack (support len())."""
        return self.size()
    
    def __bool__(self) -> bool:
        """Return False if stack is empty, True otherwise."""
        return not self.is_empty()
    
    def __str__(self) -> str:
        """Return string representation of the stack."""
        return f"Stack(top={list(reversed(self._items))})"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the stack."""
        return f"Stack({self._items}, max_size={self._max_size})"
    
    def __iter__(self) -> Iterator[T]:
        """Return iterator from bottom to top of stack."""
        return iter(self._items)