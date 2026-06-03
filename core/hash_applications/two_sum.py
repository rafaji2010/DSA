"""
core/hash_applications/two_sum.py
LeetCode 1 - Two Sum (Hash Table Solution)

Problem: Given array nums and target, return indices of two numbers that add to target.
Time: O(n), Space: O(n)
"""

from typing import List, Tuple, Optional


def two_sum_brute_force(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    O(n²) solution - check every pair.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_hash(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    O(n) solution using hash table.
    
    Key insight: For each number, check if complement (target - num) exists.
    """
    seen = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return (seen[complement], i)
        
        seen[num] = i
    
    return None


def two_sum_with_duplicates(nums: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Find ALL pairs that sum to target (handles duplicates).
    """
    seen = {}
    pairs = []
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            # Add all indices where complement appears
            for j in seen[complement]:
                pairs.append((j, i))
        
        # Store index in list (handle duplicates)
        if num not in seen:
            seen[num] = []
        seen[num].append(i)
    
    return pairs


if __name__ == "__main__":
    print("=" * 60)
    print("TWO SUM - HASH TABLE SOLUTION")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9, (0, 1)),
        ([3, 2, 4], 6, (1, 2)),
        ([3, 3], 6, (0, 1)),
        ([1, 2, 3, 4, 5], 9, (3, 4)),
    ]
    
    print("\n--- Finding single pair ---")
    for nums, target, expected in test_cases:
        result = two_sum_hash(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"{status} {nums} target={target} → {result}")
    
    print("\n--- Finding ALL pairs (with duplicates) ---")
    nums = [1, 3, 2, 2, 4, 1, 5]
    target = 5
    pairs = two_sum_with_duplicates(nums, target)
    print(f"nums={nums}, target={target}")
    print(f"All pairs: {pairs}")
    
    print("\n--- Performance comparison ---")
    import time
    large_nums = list(range(10000))
    target = 19997
    
    start = time.perf_counter()
    two_sum_brute_force(large_nums, target)
    brute_time = time.perf_counter() - start
    
    start = time.perf_counter()
    two_sum_hash(large_nums, target)
    hash_time = time.perf_counter() - start
    
    print(f"Brute force O(n²): {brute_time:.4f}s")
    print(f"Hash table O(n):   {hash_time:.4f}s")
    print(f"Hash table is {brute_time/hash_time:.0f}x faster!")
    
    print("\n✅ Two Sum complete!")
