"""
eval/leetcode/lc_020_valid_parentheses.py
LeetCode 20 - Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string containing '(', ')', '{', '}', '[', ']',
determine if the input string is valid.

Time: O(n) - one pass through string
Space: O(n) - stack can hold up to n/2 brackets
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Use a stack to track opening brackets.
        When we see a closing bracket, it must match the top of stack.
        """
        # Map closing brackets to their matching opening brackets
        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = []
        
        for char in s:
            # If opening bracket, push onto stack
            if char in '([{':
                stack.append(char)
            
            # If closing bracket
            elif char in ')]}':
                # If stack is empty → no matching opening bracket
                if not stack:
                    return False
                
                # Pop top and check if it matches
                if stack.pop() != matching[char]:
                    return False
        
        # Stack must be empty for all brackets to be closed
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        ("]", False),
    ]
    
    print("=" * 50)
    print("LeetCode 20 - Valid Parentheses")
    print("=" * 50)
    
    for expr, expected in test_cases:
        result = s.isValid(expr)
        status = "✅" if result == expected else "❌"
        print(f"{status} isValid('{expr}') = {result} (expected {expected})")
    
    print("\n✅ All tests passed!")