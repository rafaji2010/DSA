"""
core/two_pointers/sliding_window_fixed.py
Fixed Size Sliding Window Pattern
"""

from typing import List


def max_sum_subarray(nums: List[int], k: int) -> int:
    """Maximum sum of any subarray of size k."""
    if len(nums) < k:
        return -1
    
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


def max_avg_subarray(nums: List[int], k: int) -> float:
    """LeetCode 643 - Maximum Average Subarray I."""
    max_sum = max_sum_subarray(nums, k)
    return max_sum / k


def min_avg_subarray(nums: List[int], k: int) -> float:
    """Minimum average of any subarray of size k."""
    if len(nums) < k:
        return -1
    
    window_sum = sum(nums[:k])
    min_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        min_sum = min(min_sum, window_sum)
    
    return min_sum / k


def max_product_subarray(nums: List[int], k: int) -> int:
    """Maximum product of any subarray of size k."""
    if len(nums) < k:
        return -1
    
    product = 1
    for i in range(k):
        product *= nums[i]
    
    max_product = product
    
    for i in range(k, len(nums)):
        # When dividing, ensure no zero
        if nums[i - k] != 0:
            product = product // nums[i - k] * nums[i]
        else:
            # Recalculate if zero was removed
            product = 1
            for j in range(i - k + 1, i + 1):
                product *= nums[j]
        max_product = max(max_product, product)
    
    return max_product


if __name__ == "__main__":
    print("=" * 60)
    print("FIXED SIZE SLIDING WINDOW")
    print("=" * 60)
    
    nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    
    print(f"\nArray: {nums}")
    print(f"Window size: {k}")
    print(f"Maximum sum: {max_sum_subarray(nums, k)}")
    print(f"Maximum average: {max_avg_subarray(nums, k):.2f}")
    print(f"Minimum average: {min_avg_subarray(nums, k):.2f}")
    
    print("\n✅ Fixed size sliding window complete!")
