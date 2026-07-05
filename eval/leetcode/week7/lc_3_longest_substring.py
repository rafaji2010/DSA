"""
LeetCode 3 - Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Time: O(n), Space: O(min(n, alphabet_size))
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # If character seen before and within current window
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            
            char_index[char] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length


if __name__ == "__main__":
    s = Solution()
    
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
    ]
    
    print("=" * 50)
    print("LeetCode 3 - Longest Substring Without Repeating Characters")
    print("=" * 50)
    
    for s_str, expected in test_cases:
        result = s.lengthOfLongestSubstring(s_str)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{s_str}' → {result} (expected {expected})")
    
    print("\n✅ Problem 3 complete!")
