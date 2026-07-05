"""
LeetCode 125 - Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if it reads the same forward and backward
after converting to lowercase and removing non-alphanumeric characters.

Time: O(n), Space: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True


if __name__ == "__main__":
    s = Solution()
    
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("ab_a", True),
        (".,", True),
    ]
    
    print("=" * 50)
    print("LeetCode 125 - Valid Palindrome")
    print("=" * 50)
    
    for s_str, expected in test_cases:
        result = s.isPalindrome(s_str)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{s_str}' → {result}")
    
    print("\n✅ Problem 125 complete!")
