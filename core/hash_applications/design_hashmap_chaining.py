"""
core/hash_applications/design_hashmap_chaining.py
LeetCode 706 - Design HashMap (Chaining approach)

Time: O(1) average, O(n) worst case
Space: O(n)
"""


class ListNode:
    """Node for linked list chain"""
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    """
    HashMap implementation using chaining for collision resolution.
    
    Uses array of buckets, each bucket contains a linked list
    of key-value pairs.
    """
    
    def __init__(self):
        self.capacity = 1000  # Number of buckets
        self.buckets = [ListNode() for _ in range(self.capacity)]  # Sentinel nodes
    
    def _hash(self, key: int) -> int:
        """Hash function - maps key to bucket index."""
        return key % self.capacity
    
    def put(self, key: int, value: int) -> None:
        """Insert or update key-value pair."""
        index = self._hash(key)
        prev = self.buckets[index]
        current = prev.next
        
        # Search for key in chain
        while current:
            if current.key == key:
                # Update existing key
                current.val = value
                return
            prev = current
            current = current.next
        
        # Key not found - add at end of chain
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
        """Remove key-value pair."""
        index = self._hash(key)
        prev = self.buckets[index]
        current = prev.next
        
        while current:
            if current.key == key:
                # Remove current node
                prev.next = current.next
                return
            prev = current
            current = current.next


class MyHashMapLog(MyHashMap):
    """Extended version with logging"""
    
    def __init__(self):
        super().__init__()
        self.operations = []
    
    def put(self, key: int, value: int) -> None:
        super().put(key, value)
        self.operations.append(f"put({key}, {value})")
        print(f"  ✓ PUT: key={key}, value={value}")
        self._print_bucket(self._hash(key))
    
    def get(self, key: int) -> int:
        value = super().get(key)
        self.operations.append(f"get({key}) → {value}")
        print(f"  ✓ GET: key={key} → {value}")
        return value
    
    def remove(self, key: int) -> None:
        super().remove(key)
        self.operations.append(f"remove({key})")
        print(f"  ✓ REMOVE: key={key}")
        self._print_bucket(self._hash(key))
    
    def _print_bucket(self, index: int):
        """Print contents of a specific bucket."""
        current = self.buckets[index].next
        if current:
            items = []
            while current:
                items.append(f"({current.key}:{current.val})")
                current = current.next
            print(f"     Bucket {index}: {' → '.join(items)}")
        else:
            print(f"     Bucket {index}: empty")
    
    def print_operations(self):
        print("\n--- Operations Log ---")
        for op in self.operations:
            print(f"  {op}")
    
    def print_stats(self):
        """Print hash table statistics."""
        total_items = 0
        buckets_used = 0
        
        for i, bucket in enumerate(self.buckets):
            count = 0
            current = bucket.next
            while current:
                count += 1
                current = current.next
            if count > 0:
                buckets_used += 1
                total_items += count
        
        print(f"\n--- Hash Table Stats ---")
        print(f"  Capacity: {self.capacity}")
        print(f"  Items: {total_items}")
        print(f"  Buckets used: {buckets_used}")
        print(f"  Load factor: {total_items / self.capacity:.3f}")


if __name__ == "__main__":
    print("=" * 60)
    print("DESIGN HASH MAP - CHAINING APPROACH")
    print("=" * 60)
    
    # Test with logging version
    hashmap = MyHashMapLog()
    
    print("\n--- Executing operations ---")
    hashmap.put(1, 1)
    hashmap.put(2, 2)
    hashmap.get(1)      # Returns 1
    hashmap.get(3)      # Returns -1 (not found)
    hashmap.put(2, 1)   # Update existing key
    hashmap.get(2)      # Returns 1
    hashmap.remove(2)   # Remove key 2
    hashmap.get(2)      # Returns -1
    
    print("\n--- Testing collisions ---")
    # Create hash table with small capacity to force collisions
    small_map = MyHashMapLog()
    small_map.capacity = 4
    small_map.buckets = [ListNode() for _ in range(4)]
    
    small_map.put(10, 100)  # 10 % 4 = 2
    small_map.put(14, 140)  # 14 % 4 = 2 → COLLISION!
    small_map.put(18, 180)  # 18 % 4 = 2 → COLLISION!
    small_map.put(6, 60)    # 6 % 4 = 2 → COLLISION!
    
    small_map.get(14)
    small_map.remove(14)
    small_map.get(14)
    
    small_map.print_stats()
    
    print("\n✅ Chaining-based HashMap complete!")
