# core/dp/coin_change_tabulation.py
from typing import List
import sys

def coin_change(coins: List[int], amount: int) -> int:
    """
    LeetCode 322: Coin Change (Bottom-Up Tabulation)
    Time: O(amount * len(coins)) | Space: O(amount)
    """
    # Initialize DP array with a large number (infinity)
    dp: List[int] = [sys.maxsize] * (amount + 1)
    
    # Base case: 0 coins needed to make amount 0
    dp[0] = 0
    
    # Build the table for each amount from 1 to target amount
    for i in range(1, amount + 1):
        for coin in coins:
            # If this coin can be used (it doesn't overshoot the amount)
            if i - coin >= 0:
                # Take the minimum of:
                # 1. What we already have in dp[i]
                # 2. 1 (this coin) + the optimal way to make the remainder (dp[i - coin])
                dp[i] = min(dp[i], 1 + dp[i - coin])
                
    # If dp[amount] is still maxsize, it was impossible. Return -1.
    return dp[amount] if dp[amount] != sys.maxsize else -1

if __name__ == "__main__":
    print(f"Coins [1,2,5], Amount 11: {coin_change([1, 2, 5], 11)}")  # Expected: 3 (5+5+1)
    print(f"Coins [2], Amount 3: {coin_change([2], 3)}")              # Expected: -1