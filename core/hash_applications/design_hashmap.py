"""
core/hash_applications/design_hashmap.py
LeetCode 706 - Design HashMap

Design your own HashMap without using built-in dict.
"""

class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    """
    HashMap implementation using chaining.
    """
    
    def __init__(self):
        self.capacity = 1000
        self.buckets = [ListNode() for _ in range(self.capacity)]  # Sentinel nodes
    
    def _hash(self, key: int) -> int:
        """Simple hash function for integer keys."""
        return key % self.capacity
    
    def put(self, key: int, value: int) -> None:
        """Insert or update key-value pair."""
        index = self._hash(key)
        prev = self.buckets[index]
        current = prev.next
        
        # Search for key in chain
        while current:
            if current.key == key:
                current.val = value
                return
            prev = current
            current = current.next
        
        # Key not found - add at end
        prev.next = ListNode(key, value)
    
    def get(self, key: int) -> int:
        """Return value for key, or -1 if not found."""
        index = self._hash(key)
        current = self.buckets[index].next
        
        while current:
            if current.key == key:
                return current.val
            current = current.next
        
        return -1
    
    def remove(self, key: int) -> None:
        """Remove key-value pair if it exists."""
        index = self._hash(key)
        prev = self.buckets[index]
        current = prev.next
        
        while current:
            if current.key == key:
                prev.next = current.next
                return
            prev = current
            current = current.next


class MyHashMapArray:
    """
    Alternative: Use large array (key range 0-1,000,000)
    Simpler but uses more memory.
    """
    
    def __init__(self):
        self.size = 1_000_001
        self.map = [-1] * self.size
    
    def put(self, key: int, value: int) -> None:
        self.map[key] = value
    
    def get(self, key: int) -> int:
        return self.map[key]
    
    def remove(self, key: int) -> None:
        self.map[key] = -1


if __name__ == "__main__":
    print("=" * 60)
    print("DESIGN HASH MAP")
    print("=" * 60)
    
    # Test with chaining implementation
    hashmap = MyHashMap()
    
    print("\n--- Operations ---")
    hashmap.put(1, 1)
    hashmap.put(2, 2)
    print(f"get(1): {hashmap.get(1)}")  # 1
    print(f"get(3): {hashmap.get(3)}")  # -1
    
    hashmap.put(2, 1)
    print(f"get(2): {hashmap.get(2)}")  # 1
    
    hashmap.remove(2)
    print(f"get(2): {hashmap.get(2)}")  # -1
    
    # Test with many keys
    print("\n--- Stress test ---")
    hashmap2 = MyHashMap()
    for i in range(1000):
        hashmap2.put(i, i * 10)
    
    for i in range(1000):
        assert hashmap2.get(i) == i * 10
    
    print("✅ All 1000 keys inserted and retrieved correctly!")
    
    print("\n✅ Design HashMap complete!")
