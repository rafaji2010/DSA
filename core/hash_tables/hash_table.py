"""
core/hash_tables/hash_table.py
Hash Table implementation with chaining

Time Complexity:
- Insert: O(1) average, O(n) worst case
- Search: O(1) average, O(n) worst case
- Delete: O(1) average, O(n) worst case
Space Complexity: O(n)
"""

from typing import TypeVar, Generic, Optional, List, Tuple, Callable, Union

K = TypeVar("K")  # Key type
V = TypeVar("V")  # Value type

# Hash function type: takes (key, capacity) -> index
HashFunction = Callable[[K, int], int]


class HashTable(Generic[K, V]):
    """
    Hash Table with chaining for collision resolution.
    
    Uses list of lists (buckets) where each bucket stores
    key-value pairs as tuples.
    
    Supports custom hash functions for different use cases.
    """
    
    def __init__(self, initial_capacity: int = 16, custom_hash: Optional[HashFunction] = None):
        """
        Initialize hash table with given capacity.
        
        Args:
            initial_capacity: Number of buckets (default 16)
            custom_hash: Optional custom hash function (key, capacity) -> index
        """
        self._capacity = initial_capacity
        self._size = 0
        self._buckets: List[List[Tuple[K, V]]] = [[] for _ in range(initial_capacity)]
        
        # Set hash function (custom or default)
        if custom_hash:
            self._hash_func = custom_hash
        else:
            self._hash_func = self._default_hash
    
    def _default_hash(self, key: K, capacity: int) -> int:
        """
        Default hash function using Python's built-in hash().
        
        Works for:
        - ints, strings, tuples, custom objects with __hash__
        """
        return hash(key) % capacity
    
    def _hash(self, key: K) -> int:
        """
        Hash function - converts key to bucket index.
        
        Uses the configured hash function (default or custom).
        Passes both key AND capacity to the hash function.
        """
        return self._hash_func(key, self._capacity)
    
    def put(self, key: K, value: V) -> None:
        """
        Insert or update a key-value pair.
        
        Time: O(1) average, O(n) worst case
        """
        index = self._hash(key)
        bucket = self._buckets[index]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Update existing key
                bucket[i] = (key, value)
                return
        
        # Key doesn't exist - add new pair
        bucket.append((key, value))
        self._size += 1
        
        # Check if we need to resize
        if self._size / self._capacity > 0.75:  # Load factor threshold
            self._resize()
    
    def get(self, key: K) -> Optional[V]:
        """
        Retrieve value associated with key.
        
        Returns None if key not found.
        Time: O(1) average, O(n) worst case
        """
        index = self._hash(key)
        bucket = self._buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None
    
    def contains(self, key: K) -> bool:
        """Return True if key exists in hash table."""
        return self.get(key) is not None
    
    def remove(self, key: K) -> bool:
        """
        Remove key-value pair from hash table.
        
        Returns True if removed, False if key not found.
        """
        index = self._hash(key)
        bucket = self._buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return True
        
        return False
    
    def _resize(self) -> None:
        """
        Double capacity when load factor exceeds threshold.
        
        Time: O(n) - rehash all existing entries
        """
        # Save old buckets
        old_buckets = self._buckets
        old_capacity = self._capacity
        
        # Double capacity
        self._capacity *= 2
        self._size = 0
        self._buckets = [[] for _ in range(self._capacity)]
        
        # Rehash all existing entries
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
    
    def size(self) -> int:
        """Return number of key-value pairs in hash table."""
        return self._size
    
    def capacity(self) -> int:
        """Return number of buckets."""
        return self._capacity
    
    def load_factor(self) -> float:
        """Return current load factor (size / capacity)."""
        return self._size / self._capacity
    
    def keys(self) -> List[K]:
        """Return all keys in the hash table."""
        result = []
        for bucket in self._buckets:
            for key, _ in bucket:
                result.append(key)
        return result
    
    def values(self) -> List[V]:
        """Return all values in the hash table."""
        result = []
        for bucket in self._buckets:
            for _, value in bucket:
                result.append(value)
        return result
    
    def items(self) -> List[Tuple[K, V]]:
        """Return all key-value pairs in the hash table."""
        result = []
        for bucket in self._buckets:
            result.extend(bucket)
        return result
    
    def clear(self) -> None:
        """Remove all entries from the hash table."""
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
    
    def __len__(self) -> int:
        return self.size()
    
    def __contains__(self, key: K) -> bool:
        return self.contains(key)
    
    def __setitem__(self, key: K, value: V) -> None:
        """Allow dict-like assignment: ht['key'] = value"""
        self.put(key, value)
    
    def __getitem__(self, key: K) -> V:
        """Allow dict-like access: value = ht['key']"""
        value = self.get(key)
        if value is None:
            raise KeyError(f"Key '{key}' not found")
        return value
    
    def __delitem__(self, key: K) -> None:
        """Allow dict-like deletion: del ht['key']"""
        if not self.remove(key):
            raise KeyError(f"Key '{key}' not found")
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        items = []
        for i, bucket in enumerate(self._buckets):
            if bucket:
                items.append(f"  {i}: {bucket}")
        return f"HashTable(size={self._size}, cap={self._capacity})\n" + "\n".join(items)


# Custom hash function examples
def hash_sum_ascii(key: str, capacity: int) -> int:
    """Simple hash function: sum of ASCII values."""
    return sum(ord(c) for c in key) % capacity


def hash_weighted(key: str, capacity: int) -> int:
    """Weighted sum hash function (position matters)."""
    total = 0
    for i, c in enumerate(key):
        total += ord(c) * (i + 1)
    return total % capacity


def hash_polynomial(key: str, capacity: int, base: int = 31) -> int:
    """Polynomial rolling hash."""
    h = 0
    for c in key:
        h = (h * base + ord(c)) % capacity
    return h


def hash_first_char(key: str, capacity: int) -> int:
    """Very simple: use first character's ASCII value."""
    return ord(key[0]) % capacity if key else 0


def hash_length(key: str, capacity: int) -> int:
    """Use string length as hash."""
    return len(key) % capacity


if __name__ == "__main__":
    print("=" * 60)
    print("HASH TABLE DEMONSTRATION")
    print("=" * 60)
    
    # Create hash table with default hash
    ht = HashTable[str, str]()
    
    print("\n--- Inserting key-value pairs ---")
    ht.put("apple", "fruit")
    ht.put("car", "vehicle")
    ht.put("dog", "animal")
    ht.put("banana", "fruit")
    
    print(f"Size: {ht.size()}")
    print(f"Capacity: {ht.capacity()}")
    print(f"Load factor: {ht.load_factor():.3f}")
    print(ht)
    
    print("\n--- Retrieving values ---")
    print(f"ht.get('apple'): {ht.get('apple')}")
    print(f"ht.get('car'): {ht.get('car')}")
    print(f"ht.get('cat'): {ht.get('cat')}")
    
    print("\n--- Using dict-like syntax ---")
    ht["grape"] = "fruit"
    print(f"ht['grape']: {ht['grape']}")
    
    print("\n--- Updating existing key ---")
    ht.put("apple", "red fruit")
    print(f"ht.get('apple'): {ht.get('apple')}")
    
    print("\n--- Checking contains ---")
    print(f"'dog' in ht: {'dog' in ht}")
    print(f"'cat' in ht: {'cat' in ht}")
    
    print("\n--- Removing keys ---")
    ht.remove("dog")
    print(f"After removing 'dog', size: {ht.size()}")
    print(f"'dog' in ht: {'dog' in ht}")
    
    print("\n--- Keys, values, items ---")
    print(f"Keys: {ht.keys()}")
    print(f"Values: {ht.values()}")
    print(f"Items: {ht.items()}")
    
    print("\n--- Demonstrating resizing ---")
    print(f"Before resize - capacity: {ht.capacity()}, size: {ht.size()}")
    
    # Add many items to trigger resize
    for i in range(20):
        ht.put(f"key_{i}", f"value_{i}")
    
    print(f"After adding 20 items - capacity: {ht.capacity()}, size: {ht.size()}")
    print(f"Load factor: {ht.load_factor():.3f}")
    
    print("\n" + "=" * 60)
    print("CUSTOM HASH FUNCTION DEMONSTRATION")
    print("=" * 60)
    
    # Test keys
    test_keys = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    
    hash_functions = [
        ("Default (Python hash)", None),
        ("Sum ASCII", hash_sum_ascii),
        ("Weighted", hash_weighted),
        ("Polynomial", hash_polynomial),
        ("First Character", hash_first_char),
        ("String Length", hash_length),
    ]
    
    for name, hash_func in hash_functions:
        ht_custom = HashTable[str, str](initial_capacity=8, custom_hash=hash_func)
        
        for key in test_keys:
            ht_custom.put(key, f"value_{key}")
        
        print(f"\n{name}:")
        print(f"  Size: {ht_custom.size()}, Capacity: {ht_custom.capacity()}")
        print(f"  Load factor: {ht_custom.load_factor():.3f}")
        # Count non-empty buckets (distribution)
        non_empty = sum(1 for bucket in ht_custom._buckets if bucket)
        print(f"  Non-empty buckets: {non_empty}/{ht_custom.capacity()}")
        print(f"  Collisions: {ht_custom.size() - non_empty}")
    
    print("\n" + "=" * 60)
    print("CLEAR DEMONSTRATION")
    print("=" * 60)
    print(f"Before clear - size: {ht.size()}")
    ht.clear()
    print(f"After clear - size: {ht.size()}")
    print(f"Is empty: {ht.size() == 0}")
    
    print("\n✅ Hash table implementation complete!")