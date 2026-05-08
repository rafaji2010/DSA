"""Stack interface defining the contract for all stack implementations."""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class StackInterface(ABC, Generic[T]):
    """Abstract base class for Stack data structure."""
    
    @abstractmethod
    def push(self, item: T) -> None:
        """Add an item to the top of the stack.
        
        Args:
            item: The item to add to the stack
        """
        pass
    
    @abstractmethod
    def pop(self) -> Optional[T]:
        """Remove and return the item from the top of the stack.
        
        Returns:
            The item from the top of the stack, or None if stack is empty
        """
        pass
    
    @abstractmethod
    def peek(self) -> Optional[T]:
        """Return the item from the top of the stack without removing it.
        
        Returns:
            The item from the top of the stack, or None if stack is empty
        """
        pass
    
    @abstractmethod
    def is_empty(self) -> bool:
        """Check if the stack is empty.
        
        Returns:
            True if stack is empty, False otherwise
        """
        pass
    
    @abstractmethod
    def size(self) -> int:
        """Return the number of items in the stack.
        
        Returns:
            The number of items in the stack
        """
        pass
    
    @abstractmethod
    def clear(self) -> None:
        """Remove all items from the stack."""
        pass