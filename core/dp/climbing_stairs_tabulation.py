# core/dp/climbing_stairs_tabulation.py
from typing import List

def climb_stairs(n: int) -> int:
    """
    LeetCode 70: Climbing Stairs (Bottom-Up Tabulation)
    Time: O(n) | Space: O(n) -> Can be optimized to O(1) but using array for clarity
    """
    if n <= 1:
        return 1
        
    # Create a DP array of size n+1
    dp: List[int] = [0] * (n + 1)
    
    # Base cases
    dp[0] = 1
    dp[1] = 1
    
    # Build the table from bottom up
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]

if __name__ == "__main__":
    print(f"Ways to climb 2 stairs: {climb_stairs(2)}")  # Expected: 2 (1+1, 2)
    print(f"Ways to climb 3 stairs: {climb_stairs(3)}")  # Expected: 3 (1+1+1, 1+2, 2+1)
    print(f"Ways to climb 5 stairs: {climb_stairs(5)}")  # Expected: 8