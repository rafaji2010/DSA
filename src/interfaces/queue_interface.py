"""Queue interface defining the contract for all queue implementations."""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class QueueInterface(ABC, Generic[T]):
    """Abstract base class for Queue data structure."""
    
    @abstractmethod
    def enqueue(self, item: T) -> None:
        """Add an item to the rear of the queue.
        
        Args:
            item: The item to add to the queue
        """
        pass
    
    @abstractmethod
    def dequeue(self) -> Optional[T]:
        """Remove and return the item from the front of the queue.
        
        Returns:
            The item from the front of the queue, or None if queue is empty
        """
        pass
    
    @abstractmethod
    def peek(self) -> Optional[T]:
        """Return the item from the front of the queue without removing it.
        
        Returns:
            The item from the front of the queue, or None if queue is empty
        """
        pass
    
    @abstractmethod
    def is_empty(self) -> bool:
        """Check if the queue is empty.
        
        Returns:
            True if queue is empty, False otherwise
        """
        pass
    
    @abstractmethod
    def size(self) -> int:
        """Return the number of items in the queue.
        
        Returns:
            The number of items in the queue
        """
        pass
    
    @abstractmethod
    def clear(self) -> None:
        """Remove all items from the queue."""
        pass