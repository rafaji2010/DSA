"""
core/linked_list.py
Singly Linked List implementation with full type hints.
"""

from __future__ import annotations
from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    """A single node in a linked list."""
    
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: Optional[Node[T]] = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class LinkedList(Generic[T]):
    """Singly linked list with basic operations."""
    
    def __init__(self) -> None:
        self._head: Optional[Node[T]] = None
        self._size: int = 0
    
    def is_empty(self) -> bool:
        """Return True if list has no nodes."""
        return self._head is None
    
    def size(self) -> int:
        """Return number of nodes in list. O(1) — maintained as field."""
        return self._size
    
    def display(self) -> None:
        """Print list in readable format."""
        elements: list[str] = []
        current = self._head
        
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        
        print(" → ".join(elements) + " → None")
    
    def to_list(self) -> list[T]:
        """Convert linked list to Python list for testing."""
        result: list[T] = []
        current = self._head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result
    

    def append(self, value: T) -> None:
        """
        Add value to the end of the list.
        Time: O(n) — must traverse to the tail.
        """
        new_node = Node(value)
        
        if self._head is None:
            # List is empty. New node becomes head.
            self._head = new_node
            self._size = 1
            return
        
        # List is non-empty. Traverse to the tail node.
        current = self._head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self._size += 1


    def prepend(self, value: T) -> None:
        """
        Add value to the front of the list.
        Time: O(1) — just update the head pointer.
        """
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def search(self, value: T) -> bool:
        """
        Check if value exists in the list.
        
        Time: O(n) — may need to check every node
        Space: O(1) — only uses a pointer
        
        Returns:
            True if value found, False otherwise
        """
        current = self._head
        
        # Walk through each node
        while current is not None:
            if current.value == value:
                return True  # Found it!
            current = current.next
        
        return False  # Reached end without finding

    def find_index(self, value: T) -> int:
        """
        Return first index where value appears.
        Returns -1 if not found.
        
        Time: O(n) — may need to check every node
        Space: O(1)
        """
        current = self._head
        index = 0
        
        while current is not None:
            if current.value == value:
                return index  # Found at current position
            current = current.next
            index += 1
        
        return -1  # Not found


    def delete(self, value: T) -> bool:
        """
        Delete the first node with matching value.
        Returns True if deleted, False if not found.
        
        Time: O(n) — must find the node
        Space: O(1)
        """
        # Case 1: Empty list
        if self._head is None:
            return False
        
        # Case 2: Value is at HEAD
        if self._head.value == value:
            breakpoint()
            self._head = self._head.next  # Bypass the head
            self._size -= 1
            return True
        
        # Case 3: Value is elsewhere (middle or tail)
        current = self._head
        while current.next is not None:
            if current.next.value == value:
                breakpoint()
                # Bypass the target node
                current.next = current.next.next
                print(f"After bypass: {current.value}.next = {current.next.value if current.next else 'None'}")
                self._size -= 1
                return True
            current = current.next
        
        return False  # Value not found

    
    def delete_at_index(self, index: int) -> T:
        """
        Delete node at specific index.
        Returns the deleted value.
        Raises IndexError if invalid index.
        
        Time: O(n) — must traverse to find node
        Space: O(1)
        """
        # Validate index
        if index < 0 or index >= self._size:
            raise IndexError("delete index out of range")
        
        # Case 1: Delete head (index 0)
        if index == 0:
            assert self._head is not None  # Safe because size > 0
            value = self._head.value
            self._head = self._head.next
            self._size -= 1
            return value
        
        # Case 2: Delete elsewhere
        # Find node BEFORE the target
        prev = self._get_node_at(index - 1)
        assert prev is not None
        assert prev.next is not None
        
        value = prev.next.value       # Save value to return
        prev.next = prev.next.next    # Bypass the target
        self._size -= 1
        
        return value
    
    # Add to your LinkedList class in core/linked_list.py

    def length(self) -> int:
        """
        Return the number of nodes in the list.
        Time: O(1) — we maintain _size field
        Space: O(1)
        """
        return self._size
    
    def _get_node_at(self, index: int) -> Optional[Node[T]]:
        """
        Helper: get node at specific index (0-based).
        Time: O(n) — must traverse.
        """
        if index < 0 or index >= self._size:
            return None
        
        current = self._head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current


    def __getitem__(self, index: int) -> T:
        """Allow list-like indexing: ll[2]"""
        node = self._get_node_at(index)
        if node is None:
            raise IndexError("list index out of range")
        return node.value


    def __setitem__(self, index: int, value: T) -> None:
        """Allow assignment: ll[2] = 99"""
        node = self._get_node_at(index)
        if node is None:
            raise IndexError("list index out of range")
        node.value = value



if __name__ == "__main__":
    # Test basic functionality
    ll = LinkedList[int]()
    ll.append(10)
    ll.append(20)
    print(ll.length())
    ll.append(30)
    ll.display()                    # 10 → 20 → 30 → None

    ll.prepend(5)
    ll.display()                    # 5 → 10 → 20 → 30 → None

    print(f"ll[2] = {ll[2]}")       # ll[2] = 20
    ll[2] = 99

    print(ll.search(30)) 
    print(ll.search(99))

    print(ll.find_index(30))  # 2
    print(ll.find_index(10))  # 0
    print(ll.find_index(99))  #-1

    print(ll.delete(30)) 
    print(ll.delete_at_index(1))
    
    ll.display()