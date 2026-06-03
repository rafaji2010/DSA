"""
core/hash_applications/subarray_sum.py
LeetCode 560 - Subarray Sum Equals K

Problem: Count number of subarrays that sum to k.
Time: O(n), Space: O(n)
"""

from typing import List
from collections import defaultdict


def subarray_sum_brute_force(nums: List[int], k: int) -> int:
    """
    O(n²) solution - check all subarrays.
    """
    count = 0
    n = len(nums)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == k:
                count += 1
    
    return count


def subarray_sum_hash(nums: List[int], k: int) -> int:
    """
    O(n) solution using hash table.
    
    Key insight: If prefix_sum[j] - prefix_sum[i-1] = k,
    then prefix_sum[i-1] = prefix_sum[j] - k.
    
    So we store all prefix sums seen so far.
    """
    count = 0
    prefix_sum = 0
    sum_count = defaultdict(int)
    sum_count[0] = 1  # Empty prefix sum
    
    for num in nums:
        prefix_sum += num
        
        # Check if there's a previous prefix sum that would make current sum = k
        # If prefix_sum - previous_sum = k, then previous_sum = prefix_sum - k
        count += sum_count[prefix_sum - k]
        
        # Record current prefix sum for future
        sum_count[prefix_sum] += 1
    
    return count


def subarray_sum_with_indices(nums: List[int], k: int) -> List[tuple]:
    """
    Find all subarrays that sum to k with their indices.
    """
    result = []
    prefix_sum = 0
    sum_indices = defaultdict(list)
    sum_indices[0].append(-1)  # Empty prefix sum before start
    
    for i, num in enumerate(nums):
        prefix_sum += num
        
        # Check for subarrays ending at i
        target = prefix_sum - k
        if target in sum_indices:
            for start_idx in sum_indices[target]:
                result.append((start_idx + 1, i))
        
        sum_indices[prefix_sum].append(i)
    
    return result


if __name__ == "__main__":
    print("=" * 60)
    print("SUBARRAY SUM EQUALS K")
    print("=" * 60)
    
    test_cases = [
        ([1, 1, 1], 2, 2),      # [1,1] at indices 0-1 and 1-2
        ([1, 2, 3], 3, 2),      # [1,2] and [3]
        ([1, -1, 0], 0, 3),     # [1,-1], [0], [1,-1,0]
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
    ]
    
    print("\n--- Counting subarrays ---")
    for nums, k, expected in test_cases:
        result = subarray_sum_hash(nums, k)
        status = "✅" if result == expected else "❌"
        print(f"{status} {nums}, k={k} → {result} subarrays (expected {expected})")
    
    print("\n--- Finding subarray indices ---")
    nums = [1, 2, 3, 4, 5]
    k = 9
    indices = subarray_sum_with_indices(nums, k)
    print(f"nums={nums}, k={k}")
    print(f"Subarrays: {indices}")
    for start, end in indices:
        print(f"  [{start}:{end}] = {nums[start:end+1]}")
    
    print("\n--- Performance comparison ---")
    import time
    large_nums = [1] * 1000
    k = 500
    
    start = time.perf_counter()
    subarray_sum_brute_force(large_nums, k)
    brute_time = time.perf_counter() - start
    
    start = time.perf_counter()
    subarray_sum_hash(large_nums, k)
    hash_time = time.perf_counter() - start
    
    print(f"Brute force O(n²): {brute_time:.4f}s")
    print(f"Hash table O(n):   {hash_time:.4f}s")
    print(f"Hash table is {brute_time/hash_time:.0f}x faster!")
    
    print("\n✅ Subarray Sum Equals K complete!")
