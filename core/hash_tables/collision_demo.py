"""
Demonstrate hash collisions and chaining
"""

from hash_table import HashTable


def demonstrate_collisions():
    """Show how collisions are handled with chaining"""
    
    # Create a small hash table to force collisions
    ht = HashTable[str, str](initial_capacity=4)
    
    print("=" * 60)
    print("COLLISION DEMONSTRATION")
    print("=" * 60)
    
    # These keys are chosen to cause collisions
    test_keys = [
        ("apple", "fruit"),
        ("banana", "fruit"),
        ("cherry", "fruit"),
        ("date", "fruit"),
        ("elderberry", "fruit"),
    ]
    
    print("\n--- Inserting keys one by one ---")
    
    for key, value in test_keys:
        print(f"\nInserting: {key}")
        ht.put(key, value)
        
        # Show bucket distribution
        print(f"  Bucket index: {ht._hash(key)}")
        print(f"  Bucket contents: {ht._buckets[ht._hash(key)]}")
        print(f"  Size: {ht.size()}, Capacity: {ht.capacity()}")
        print(f"  Load factor: {ht.load_factor():.3f}")
    
    print("\n" + "=" * 60)
    print("FINAL HASH TABLE STATE")
    print("=" * 60)
    print(ht)
    
    print("\n--- Searching for keys ---")
    for key in ["apple", "cherry", "grape"]:
        value = ht.get(key)
        print(f"  get('{key}') = {value}")


def analyze_chains():
    """Analyze chain lengths in hash table"""
    
    ht = HashTable[str, str](initial_capacity=8)
    
    # Insert many keys
    words = [
        "apple", "banana", "cherry", "date", "elderberry",
        "fig", "grape", "honeydew", "kiwi", "lemon",
        "mango", "nectarine", "orange", "papaya", "quince"
    ]
    
    print("\n" + "=" * 60)
    print("CHAIN LENGTH ANALYSIS")
    print("=" * 60)
    
    for word in words:
        ht.put(word, f"value_{word}")
    
    print(ht)
    
    print("\n--- Chain Length Distribution ---")
    chain_lengths = [len(bucket) for bucket in ht._buckets]
    
    for i, length in enumerate(chain_lengths):
        if length > 0:
            bar = "█" * length
            print(f"  Bucket {i:2d}: {length} item(s) {bar}")
    
    max_chain = max(chain_lengths)
    avg_chain = sum(chain_lengths) / ht.capacity()
    
    print(f"\n  Max chain length: {max_chain}")
    print(f"  Average chain length: {avg_chain:.2f}")
    print(f"  Empty buckets: {chain_lengths.count(0)}/{ht.capacity()}")
    
    if max_chain > 3:
        print("  ⚠️ Long chains detected! Poor hash distribution.")
    else:
        print("  ✅ Good hash distribution!")


def compare_collision_rates():
    """Compare different hash functions' collision rates"""
    
    from hash_table import hash_sum_ascii, hash_polynomial
    
    words = ["cat", "act", "tac", "bat", "tab", "at", "ta", "ant", "tan", "nat"]
    
    print("\n" + "=" * 60)
    print("HASH FUNCTION COLLISION COMPARISON")
    print("=" * 60)
    
    for name, hash_func in [
        ("Sum ASCII (poor)", hash_sum_ascii),
        ("Polynomial (good)", hash_polynomial),
    ]:
        # Create custom hash table
        class CustomHashTable(HashTable):
            def _hash(self, key):
                return hash_func(key, self._capacity)
        
        ht = CustomHashTable(initial_capacity=8)
        
        for word in words:
            ht.put(word, f"value_{word}")
        
        print(f"\n{name}:")
        print(f"  Collisions: {ht.size() - len([b for b in ht._buckets if b])}")
        
        # Show distribution
        for i, bucket in enumerate(ht._buckets):
            if len(bucket) > 1:
                print(f"  Bucket {i}: {[k for k, v in bucket]} ← COLLISION!")
            elif len(bucket) == 1:
                print(f"  Bucket {i}: {bucket[0][0]}")
        
        # Calculate collision metric
        collisions = sum(1 for b in ht._buckets if len(b) > 1)
        print(f"  Total collision buckets: {collisions}")


if __name__ == "__main__":
    demonstrate_collisions()
    analyze_chains()
    compare_collision_rates()
