"""
core/dp/coin_change.py
Coin Change - Minimum coins to make amount
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    Minimum number of coins to make amount.
    Returns -1 if impossible.
    
    Time: O(n × amount) where n = len(coins)
    Space: O(amount)
    
    dp[i] = minimum coins needed to make amount i
    dp[0] = 0 (zero coins needed for amount 0)
    dp[i] = min(dp[i - coin] + 1) for each coin ≤ i
    """
    # Initialize with amount + 1 (sentinel value for infinity)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != amount + 1 else -1


def coin_change_trace(coins: List[int], amount: int) -> None:
    """Coin Change with DP table visualization."""
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    print(f"Coins: {coins}, Target: {amount}")
    print("=" * 60)
    
    for coin in coins:
        print(f"\nProcessing coin {coin}:")
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
        print(f"  dp: {dp}")
    
    result = dp[amount] if dp[amount] != amount + 1 else -1
    print(f"\nResult: {result} coins")


def coin_change_with_path(coins: List[int], amount: int) -> tuple:
    """Return minimum coins AND the coin combination."""
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    used_coin = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coin[i] = coin
    
    if dp[amount] == amount + 1:
        return -1, []
    
    # Reconstruct path
    path = []
    remaining = amount
    while remaining > 0:
        coin = used_coin[remaining]
        path.append(coin)
        remaining -= coin
    
    return dp[amount], path

def greedy_coin_change(coins: List[int], amount: int) -> int:
    """Greedy approach - picks largest coin first."""
    coins = sorted(coins, reverse=True)
    count = 0
    remaining = amount
    
    for coin in coins:
        while remaining >= coin:
            remaining -= coin
            count += 1
    
    return count if remaining == 0 else -1


# Test where greedy FAILS
coins = [1, 5, 6, 9]
amount = 11

print(f"Greedy: {greedy_coin_change(coins, amount)} coins")  # 3 (9+1+1)
print(f"DP: {coin_change(coins, amount)} coins")             # 2 (5+6)
print("Greedy FAILS because it picks 9 first!")


if __name__ == "__main__":
    print("=" * 60)
    print("COIN CHANGE PROBLEM")
    print("=" * 60)
    
    test_cases = [
        ([1, 5, 6, 9], 11, 2),  # 5 + 6
        ([1, 2, 5], 11, 3),     # 5 + 5 + 1
        ([2], 3, -1),           # Impossible
        ([1, 3, 4], 6, 2),      # 3 + 3
        ([186, 419, 83, 408], 6249, 20),  # Larger case
    ]
    
    for coins, amount, expected in test_cases:
        result = coin_change(coins, amount)
        status = "✅" if result == expected else "❌"
        print(f"\nCoins: {coins}, Amount: {amount}")
        print(f"Minimum coins: {result} (expected {expected}) {status}")
        
        if result != -1:
            count, path = coin_change_with_path(coins, amount)
            print(f"  Coin combination: {path}")
    
    print("\n" + "=" * 60)
    print("DETAILED TRACE")
    print("=" * 60)
    coin_change_trace([1, 5, 6, 9], 11)
 
    print("\n✅ Coin Change complete!")

    greedy_coin_change([1, 5, 6, 9], 11)