"""
core/hash_applications/design_hashmap_array.py
LeetCode 706 - Design HashMap (Array approach)

Time: O(1) for all operations
Space: O(10^6)
"""


class MyHashMap:
    """
    HashMap implementation using a large array.
    Keys are between 0 and 1,000,000.
    """
    
    def __init__(self):
        # Create array of size 1,000,001 filled with -1
        # -1 means the key doesn't exist
        self.map = [-1] * 1_000_001
    
    def put(self, key: int, value: int) -> None:
        """Insert or update key-value pair."""
        self.map[key] = value
    
    def get(self, key: int) -> int:
        """Return value for key, or -1 if not found."""
        return self.map[key]
    
    def remove(self, key: int) -> None:
        """Remove key-value pair."""
        self.map[key] = -1


class MyHashMapLog:
    """
    Same but with logging to see operations.
    """
    
    def __init__(self):
        self.map = [-1] * 1_000_001
        self.operations = []
    
    def put(self, key: int, value: int) -> None:
        self.map[key] = value
        self.operations.append(f"put({key}, {value})")
        print(f"  ✓ PUT: key={key}, value={value}")
    
    def get(self, key: int) -> int:
        value = self.map[key]
        self.operations.append(f"get({key}) → {value}")
        print(f"  ✓ GET: key={key} → {value}")
        return value
    
    def remove(self, key: int) -> None:
        self.map[key] = -1
        self.operations.append(f"remove({key})")
        print(f"  ✓ REMOVE: key={key}")
    
    def print_operations(self):
        print("\n--- Operations Log ---")
        for op in self.operations:
            print(f"  {op}")


if __name__ == "__main__":
    print("=" * 60)
    print("DESIGN HASH MAP - ARRAY APPROACH")
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
    
    hashmap.print_operations()
    
    print("\n✅ Array-based HashMap complete!")
