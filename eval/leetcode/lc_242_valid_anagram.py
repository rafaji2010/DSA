"""
LeetCode 242 - Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings, return true if they are anagrams.

Time: O(n) - count characters
Space: O(1) - at most 26 characters
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Character count approach"""
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        for char in t:
            count[ord(char) - ord('a')] -= 1
            if count[ord(char) - ord('a')] < 0:
                return False
        
        return all(c == 0 for c in count)
    
    def isAnagramCounter(self, s: str, t: str) -> bool:
        """Using Python's Counter"""
        return Counter(s) == Counter(t)
    
    def isAnagramSort(self, s: str, t: str) -> bool:
        """Sorting approach - O(n log n)"""
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "ab", False),
    ]
    
    print("=" * 50)
    print("LeetCode 242 - Valid Anagram")
    print("=" * 50)
    
    for s, t, expected in test_cases:
        result = sol.isAnagram(s, t)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{s}' vs '{t}' → {result}")
    
    print("\n✅ Valid Anagram complete!")
