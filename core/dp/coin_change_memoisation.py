# core/dynamic_programming/coin_change.py
from typing import List, Dict
import sys

def coin_change(coins: List[int], amount: int) -> int:
    """
    LeetCode 322: Coin Change
    Top-Down DP (Memoization).
    Time: O(amount * len(coins)) | Space: O(amount)
    """
    memo: Dict[int, int] = {}

    def dfs(remaining: int) -> int:
        # Base Case 1: Exact amount reached
        if remaining == 0:
            return 0
        # Base Case 2: Overshot the amount
        if remaining < 0:
            return -1
        # Base Case 3: Already computed this subproblem
        if remaining in memo:
            return memo[remaining]

        min_coins = sys.maxsize
        for coin in coins:
            res = dfs(remaining - coin)
            if res != -1:
                min_coins = min(min_coins, 1 + res)

        # Cache the result (or -1 if impossible)
        memo[remaining] = min_coins if min_coins != sys.maxsize else -1
        return memo[remaining]

    return dfs(amount)

if __name__ == "__main__":
    print(f"Coins [1,2,5], Amount 11: {coin_change([1, 2, 5], 11)}")  # Expected: 3 (5+5+1)
    print(f"Coins [2], Amount 3: {coin_change([2], 3)}")              # Expected: -1