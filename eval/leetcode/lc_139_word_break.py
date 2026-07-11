
from typing import List

def word_break(s: str, word_dict: List[str]) -> bool:
    """
    LeetCode 139: Word Break
    1D Boolean DP approach.
    Time: O(N^3) worst case (due to substring slicing), O(N^2) with optimized set lookups | Space: O(N)
    """
    word_set = set(word_dict) # O(1) lookups
    n = len(s)
    
    # dp[i] means s[0:i] (first i characters) can be segmented
    dp = [False] * (n + 1)
    dp[0] = True # Empty string is always valid

    for i in range(1, n + 1):
        for j in range(i):
            # If the prefix s[0:j] is valid AND the suffix s[j:i] is in dict
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break # No need to check other j's for this i

    return dp[n]

if __name__ == "__main__":
    s1 = "leetcode"
    w1 = ["leet", "code"]
    print(f"String: '{s1}', Dict: {w1} -> {word_break(s1, w1)}") # Expected: True

    s2 = "applepenapple"
    w2 = ["apple", "pen"]
    print(f"String: '{s2}', Dict: {w2} -> {word_break(s2, w2)}") # Expected: True

    s3 = "catsandog"
    w3 = ["cats", "dog", "sand", "and", "cat"]
    print(f"String: '{s3}', Dict: {w3} -> {word_break(s3, w3)}") # Expected: False