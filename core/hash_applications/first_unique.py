"""
core/hash_applications/first_unique.py
Find first non-repeating character in a string
"""

from collections import Counter


def first_unique_char_brute_force(s: str) -> int:
    """
    O(n²) solution - check each character against all others.
    """
    n = len(s)
    for i in range(n):
        is_unique = True
        for j in range(n):
            if i != j and s[i] == s[j]:
                is_unique = False
                break
        if is_unique:
            return i
    return -1


def first_unique_char_hash(s: str) -> int:
    """
    O(n) solution using hash table.
    
    Algorithm:
    1. Count frequency of each character
    2. Find first character with frequency 1
    """
    # Count frequencies
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Find first unique
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    
    return -1


def first_unique_char_counter(s: str) -> int:
    """Using Python's Counter (cleaner)"""
    from collections import Counter
    freq = Counter(s)
    
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1


def all_unique_chars(s: str) -> List[str]:
    """Return all characters that appear exactly once."""
    freq = Counter(s)
    return [char for char, count in freq.items() if count == 1]


def first_repeating_char(s: str) -> int:
    """Find first character that repeats."""
    seen = set()
    for i, char in enumerate(s):
        if char in seen:
            return i
        seen.add(char)
    return -1


if __name__ == "__main__":
    print("=" * 60)
    print("FIRST NON-REPEATING CHARACTER")
    print("=" * 60)
    
    test_strings = [
        "leetcode",      # 'l' at index 0
        "loveleetcode",  # 'v' at index 2
        "aabb",          # no unique → -1
        "abcabc",        # no unique → -1
        "hello",         # 'h' at index 0
        "aabcc",         # 'b' at index 2
    ]
    
    print("\n--- Finding first unique character ---")
    for s in test_strings:
        idx = first_unique_char_hash(s)
        char = s[idx] if idx != -1 else "None"
        print(f"  '{s}' → index {idx} (character '{char}')")
    
    print("\n--- Performance comparison ---")
    import time
    long_string = "a" * 10000 + "b" + "c" * 10000
    
    start = time.perf_counter()
    first_unique_char_brute_force(long_string)
    brute_time = time.perf_counter() - start
    
    start = time.perf_counter()
    first_unique_char_hash(long_string)
    hash_time = time.perf_counter() - start
    
    print(f"Brute force O(n²): {brute_time:.4f}s")
    print(f"Hash table O(n):   {hash_time:.4f}s")
    print(f"Hash table is {brute_time/hash_time:.0f}x faster!")
    
    print("\n✅ First Unique Character complete!")
