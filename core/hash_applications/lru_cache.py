"""
core/hash_applications/lru_cache.py
LeetCode 146 - LRU Cache

Design a data structure that follows the constraints of:
- Least Recently Used (LRU) cache
- O(1) time for get and put operations
"""


class Node:
    """Doubly Linked List node"""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache implementation using:
    - Hash Table: O(1) access to nodes
    - Doubly Linked List: O(1) removal/insertion (maintains order)
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        
        # Initialize dummy head and tail for easier edge handling
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_to_front(self, node: Node) -> None:
        """Add node right after head (most recent position)"""
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node: Node) -> None:
        """Remove node from linked list"""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_front(self, node: Node) -> None:
        """Move existing node to front (mark as recently used)"""
        self._remove_node(node)
        self._add_to_front(node)
    
    def _remove_tail(self) -> Node:
        """Remove and return the least recently used node (before tail)"""
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        return lru_node
    
    def get(self, key: int) -> int:
        """Return value if key exists, else -1. Mark as recently used."""
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_front(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """Insert or update key-value pair. Remove LRU if capacity exceeded."""
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            # Add new key
            if len(self.cache) >= self.capacity:
                # Remove least recently used
                lru_node = self._remove_tail()
                del self.cache[lru_node.key]
            
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
    
    def display(self) -> None:
        """Display cache order (most recent to least recent)"""
        result = []
        current = self.head.next
        while current != self.tail:
            result.append(f"({current.key}:{current.value})")
            current = current.next
        print(f"Cache order (MRU → LRU): {' → '.join(result) if result else 'empty'}")


class LRUCacheLog(LRUCache):
    """Extended version with logging"""
    
    def get(self, key: int) -> int:
        value = super().get(key)
        print(f"  get({key}) → {value}")
        self.display()
        return value
    
    def put(self, key: int, value: int) -> None:
        print(f"  put({key}, {value})", end="")
        if key in self.cache:
            print(" (updating existing)")
        else:
            print(f" (adding new, cache size={len(self.cache)}/{self.capacity})")
        super().put(key, value)
        self.display()


if __name__ == "__main__":
    print("=" * 60)
    print("LRU CACHE DEMONSTRATION")
    print("=" * 60)
    
    # Test with logging version
    cache = LRUCacheLog(2)
    
    print("\n--- Example 1: Basic operations ---")
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)      # Returns 1
    cache.put(3, 3)   # Evicts key 2
    cache.get(2)      # Returns -1 (not found)
    cache.put(4, 4)   # Evicts key 1
    cache.get(1)      # Returns -1
    cache.get(3)      # Returns 3
    cache.get(4)      # Returns 4
    
    print("\n--- Example 2: Update existing key ---")
    cache2 = LRUCacheLog(2)
    cache2.put(1, 1)
    cache2.put(2, 2)
    cache2.get(1)
    cache2.put(2, 20)  # Update key 2
    cache2.put(3, 3)   # Evicts key 1 (least recently used)
    cache2.get(1)      # Returns -1
    cache2.get(2)      # Returns 20
    cache2.get(3)      # Returns 3
    
    print("\n--- Example 3: Capacity 1 ---")
    cache3 = LRUCacheLog(1)
    cache3.put(1, 1)
    cache3.put(2, 2)   # Evicts key 1
    cache3.get(1)      # Returns -1
    cache3.get(2)      # Returns 2
    
    print("\n✅ LRU Cache implementation complete!")
