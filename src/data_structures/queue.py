"""Queue implementation using collections.deque as underlying storage."""
from collections import deque
from typing import Optional, TypeVar, Generic, Iterator
from src.interfaces.queue_interface import QueueInterface

T = TypeVar('T')

class Queue(QueueInterface[T], Generic[T]):
    """Queue implementation using collections.deque.
    
    Time Complexity:
        - enqueue: O(1) - append to right
        - dequeue: O(1) - popleft from left
        - peek: O(1)
        - is_empty: O(1)
        - size: O(1)
    
    Space Complexity: O(n) where n = number of elements
        - Each element stored once in deque
        - Deque uses linked blocks (more memory efficient than list for two-ended ops)
        - Blocks allocated as needed, each holding ~64 elements
    """
    
    def __init__(self, max_size: Optional[int] = None) -> None:
        """Initialize an empty queue.
        
        Args:
            max_size: Maximum number of items the queue can hold (optional)
        """
        self._items: deque[T] = deque()
        self._max_size = max_size
    
    def enqueue(self, item: T) -> None:
        """Add an item to the rear of the queue.
        
        Args:
            item: The item to add to the queue
            
        Raises:
            OverflowError: If queue is at maximum capacity
        """
        if self._max_size is not None and len(self._items) >= self._max_size:
            raise OverflowError(f"Queue is full (max size: {self._max_size})")
        self._items.append(item)
    
    def dequeue(self) -> Optional[T]:
        """Remove and return the item from the front of the queue.
        
        Returns:
            The item from the front of the queue, or None if queue is empty
        """
        if self.is_empty():
            return None
        return self._items.popleft()
    
    def peek(self) -> Optional[T]:
        """Return the item from the front of the queue without removing it.
        
        Returns:
            The item from the front of the queue, or None if queue is empty
        """
        if self.is_empty():
            return None
        return self._items[0]
    
    def is_empty(self) -> bool:
        """Check if the queue is empty.
        
        Returns:
            True if queue is empty, False otherwise
        """
        return len(self._items) == 0
    
    def size(self) -> int:
        """Return the number of items in the queue.
        
        Returns:
            The number of items in the queue
        """
        return len(self._items)
    
    def clear(self) -> None:
        """Remove all items from the queue."""
        self._items.clear()
    
    def __len__(self) -> int:
        """Return the number of items in the queue (support len())."""
        return self.size()
    
    def __bool__(self) -> bool:
        """Return False if queue is empty, True otherwise."""
        return not self.is_empty()
    
    def __str__(self) -> str:
        """Return string representation of the queue."""
        return f"Queue(front={list(self._items)})"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the queue."""
        return f"Queue({list(self._items)}, max_size={self._max_size})"
    
    def __iter__(self) -> Iterator[T]:
        """Return iterator over queue items (from front to rear)."""
        return iter(self._items)