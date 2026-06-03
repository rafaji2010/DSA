"""
core/hash_applications/group_anagrams.py
LeetCode 49 - Group Anagrams

Problem: Group strings that are anagrams of each other.
Time: O(n * k * log k) where n = number of strings, k = max length
Space: O(n * k)
"""

from typing import List, Dict
from collections import defaultdict


def group_anagrams_sorted(strs: List[str]) -> List[List[str]]:
    """
    Solution 1: Use sorted string as key.
    
    Anagrams have the same sorted string.
    "eat" and "tea" both sort to "aet"
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Sort characters to create key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())


def group_anagrams_count(strs: List[str]) -> List[List[str]]:
    """
    Solution 2: Use character count tuple as key (O(k) instead of O(k log k))
    
    "eat" → (1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0)
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Count frequency of each letter (a-z)
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # Use tuple as key (list is not hashable)
        key = tuple(count)
        groups[key].append(s)
    
    return list(groups.values())


def find_anagram_pairs(strs: List[str]) -> List[tuple]:
    """Find all pairs of anagrams."""
    from itertools import combinations
    pairs = []
    
    for i, j in combinations(range(len(strs)), 2):
        if sorted(strs[i]) == sorted(strs[j]):
            pairs.append((strs[i], strs[j]))
    
    return pairs


if __name__ == "__main__":
    print("=" * 60)
    print("GROUP ANAGRAMS")
    print("=" * 60)
    
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["abc", "cba", "bca", "def", "fed", "edf"],
    ]
    
    for strs in test_cases:
        result = group_anagrams_sorted(strs)
        print(f"\nInput: {strs}")
        print(f"Groups: {result}")
    
    # Compare methods
    print("\n--- Method Comparison ---")
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Sorted key method: {group_anagrams_sorted(words)}")
    print(f"Count key method:   {group_anagrams_count(words)}")
    
    # Find anagram pairs
    print("\n--- Anagram Pairs ---")
    pairs = find_anagram_pairs(words)
    print(f"Anagram pairs: {pairs}")
    
    print("\n✅ Group Anagrams complete!")
