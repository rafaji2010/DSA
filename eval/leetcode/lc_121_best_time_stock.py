#!/usr/bin/env python3
"""
eval/lc_121_best_time_stock.py
LeetCode #121: Best Time to Buy and Sell Stock

Pattern: Sliding Window / Greedy — track running minimum
Time: O(n), Space: O(1)
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Single pass optimal solution.
    Time: O(n), Space: O(1)
    """
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    
    return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Prices: {prices}")
    print(f"Max profit: {max_profit(prices)}")  # 5
