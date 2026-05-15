"""
core/queue_pdb_debug.py
Debug queue operations with pdb
"""

from collections import deque
import pdb


class DebugQueue:
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item):
        self._items.append(item)
        print(f"Enqueued: {item}, Queue: {list(self._items)}")
    
    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty queue")
        
        pdb.set_trace()  # Breakpoint here
        
        value = self._items.popleft()
        print(f"Dequeued: {value}, Queue: {list(self._items)}")
        return value
    
    def peek(self):
        if not self._items:
            return None
        return self._items[0]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)


if __name__ == "__main__":
    q = DebugQueue()
    
    # Add some items
    for i in range(1, 5):
        q.enqueue(i)
    
    # Debug the dequeue operation
    print("\n--- Debugging dequeue ---")
    q.dequeue()