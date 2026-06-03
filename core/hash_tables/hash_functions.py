"""
core/hash_tables/hash_functions.py
Demonstrating different hash function implementations
"""

def hash_sum_ascii(key: str, capacity: int) -> int:
    """
    Hash function: Sum of ASCII values.
    
    Pros: Simple, fast
    Cons: Different strings can have same sum ("ab" = 97+98=195, "ba"=98+97=195)
    """
    return sum(ord(c) for c in key) % capacity


def hash_weighted(key: str, capacity: int) -> int:
    """
    Hash function: Weighted sum (position matters).
    
    Uses polynomial: sum(ord(c) * (position + 1))
    "ab" = 97*1 + 98*2 = 97 + 196 = 293
    "ba" = 98*1 + 97*2 = 98 + 194 = 292 (different!)
    """
    total = 0
    for i, c in enumerate(key):
        total += ord(c) * (i + 1)  # Position matters!
    return total % capacity


def hash_polynomial(key: str, capacity: int, base: int = 31) -> int:
    """
    Polynomial rolling hash (used in Java's String.hashCode()).
    
    h = s[0] * 31^(n-1) + s[1] * 31^(n-2) + ... + s[n-1]
    """
    h = 0
    for c in key:
        h = h * base + ord(c)
    return h % capacity


def hash_python_builtin(key: str, capacity: int) -> int:
    """Use Python's built-in hash() - best for real use."""
    return hash(key) % capacity


if __name__ == "__main__":
    capacity = 16
    test_keys = ["apple", "banana", "cherry", "date", "apple", "banana"]
    
    print("=" * 80)
    print("HASH FUNCTION COMPARISON")
    print("=" * 80)
    print(f"{'Key':<12} {'Sum ASCII':<12} {'Weighted':<12} {'Polynomial':<12} {'Python':<12}")
    print("-" * 80)
    
    for key in test_keys:
        sum_idx = hash_sum_ascii(key, capacity)
        weight_idx = hash_weighted(key, capacity)
        poly_idx = hash_polynomial(key, capacity)
        py_idx = hash_python_builtin(key, capacity)
        
        print(f"{key:<12} {sum_idx:<12} {weight_idx:<12} {poly_idx:<12} {py_idx:<12}")
    
    print("\n" + "=" * 80)
    print("COLLISION ANALYSIS")
    print("=" * 80)
    
    # Test collision rates
    words = ["cat", "act", "tac", "bat", "tab", "at", "ta"]
    
    for hash_func_name, hash_func in [
        ("Sum ASCII", hash_sum_ascii),
        ("Weighted", hash_weighted),
        ("Polynomial", hash_polynomial),
        ("Python", hash_python_builtin),
    ]:
        indices = {}
        for word in words:
            idx = hash_func(word, 8)  # Small capacity to see collisions
            if idx not in indices:
                indices[idx] = []
            indices[idx].append(word)
        
        collisions = sum(1 for bucket in indices.values() if len(bucket) > 1)
        print(f"\n{hash_func_name}:")
        print(f"  Buckets: {indices}")
        print(f"  Collisions: {collisions}")
    
    print("\n" + "=" * 80)
    print("WHY HASH FUNCTIONS MATTER")
    print("=" * 80)
    print("""
    Good hash function:                    Poor hash function:
    ┌─────────────────────────┐           ┌─────────────────────────┐
    │ Bucket 0: [A]            │           │ Bucket 0: [A,B,C,D,E,F]  │
    │ Bucket 1: [B]            │           │ Bucket 1: []             │
    │ Bucket 2: [C]            │           │ Bucket 2: []             │
    │ Bucket 3: [D]            │           │ Bucket 3: []             │
    │ Bucket 4: [E]            │           │ Bucket 4: []             │
    │ Bucket 5: [F]            │           │ Bucket 5: []             │
    └─────────────────────────┘           └─────────────────────────┘
    
    Even distribution!                     All items in one bucket!
    O(1) lookup!                           O(n) lookup (linked list!)
    """)
