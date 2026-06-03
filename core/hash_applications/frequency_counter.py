"""
core/hash_applications/frequency_counter.py
Frequency counter pattern using hash tables
"""

from collections import Counter
from typing import List, Dict, Any


def frequency_counter_basic(items: List[Any]) -> Dict[Any, int]:
    """
    Count frequency of each item in a list.
    Time: O(n), Space: O(k) where k = unique items
    """
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq


def most_frequent(items: List[Any]) -> tuple:
    """
    Find the most frequent item and its count.
    Time: O(n), Space: O(k)
    """
    freq = frequency_counter_basic(items)
    max_item = None
    max_count = 0
    
    for item, count in freq.items():
        if count > max_count:
            max_count = count
            max_item = item
    
    return max_item, max_count


def are_anagrams(word1: str, word2: str) -> bool:
    """
    Check if two words are anagrams (same letters, different order).
    Time: O(n), Space: O(k)
    """
    if len(word1) != len(word2):
        return False
    
    freq = {}
    
    # Count characters in word1
    for char in word1:
        freq[char] = freq.get(char, 0) + 1
    
    # Subtract characters in word2
    for char in word2:
        if char not in freq:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False
    
    return True


def find_unique_elements(items: List[Any]) -> List[Any]:
    """
    Find elements that appear exactly once.
    Time: O(n), Space: O(k)
    """
    freq = frequency_counter_basic(items)
    return [item for item, count in freq.items() if count == 1]


def find_duplicates(items: List[Any]) -> List[Any]:
    """
    Find elements that appear more than once.
    Time: O(n), Space: O(k)
    """
    freq = frequency_counter_basic(items)
    return [item for item, count in freq.items() if count > 1]


if __name__ == "__main__":
    print("=" * 60)
    print("FREQUENCY COUNTER PATTERN")
    print("=" * 60)
    
    # Example 1: Basic frequency
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    freq = frequency_counter_basic(words)
    print(f"\nWords: {words}")
    print(f"Frequency: {freq}")
    
    # Example 2: Most frequent
    most, count = most_frequent(words)
    print(f"\nMost frequent: '{most}' ({count} times)")
    
    # Example 3: Anagrams
    print("\n--- Anagram Check ---")
    pairs = [("listen", "silent"), ("hello", "world"), ("race", "care")]
    for w1, w2 in pairs:
        result = are_anagrams(w1, w2)
        print(f"  '{w1}' and '{w2}': {result}")
    
    # Example 4: Unique elements
    numbers = [1, 2, 3, 2, 4, 3, 5, 1, 6]
    unique = find_unique_elements(numbers)
    duplicates = find_duplicates(numbers)
    print(f"\nNumbers: {numbers}")
    print(f"Unique (appear once): {unique}")
    print(f"Duplicates (appear > once): {duplicates}")
    
    # Example 5: Using Python's Counter
    from collections import Counter
    counter = Counter(words)
    print(f"\nPython's Counter: {counter}")
    print(f"Most common: {counter.most_common(2)}")
    
    print("\n✅ Frequency counter pattern complete!")
