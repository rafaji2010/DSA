"""
LeetCode 1143 - Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/

Given two strings, return the length of their longest common subsequence.
Time: O(m × n), Space: O(m × n)
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """2D DP table - O(m × n) time, O(m × n) space"""
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]
    
    def lcsOptimized(self, text1: str, text2: str) -> int:
        """Space optimized - O(m × n) time, O(n) space"""
        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)
        
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        
        return prev[n]


if __name__ == "__main__":
    s = Solution()
    
    test_cases = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("bl", "yby", 1),
        ("pmjghexybyrgzczy", "hafcdqbgncrcbihkd", 6),
    ]
    
    print("=" * 60)
    print("Longest Common Subsequence")
    print("=" * 60)
    
    for text1, text2, expected in test_cases:
        result = s.longestCommonSubsequence(text1, text2)
        result_opt = s.lcsOptimized(text1, text2)
        status = "✅" if result == expected else "❌"
        print(f"\n'{text1}' vs '{text2}'")
        print(f"  LCS: {result} (expected {expected}) {status}")
        print(f"  Optimized: {result_opt}")
    
    print("\n✅ LC 1143 complete!")