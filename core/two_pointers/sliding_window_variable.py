"""
core/two_pointers/sliding_window_variable.py
Variable Size Sliding Window Pattern
"""

from typing import List


def length_of_longest_substring(s: str) -> int:
    """
    LeetCode 3 - Longest Substring Without Repeating Characters
    Time: O(n), Space: O(min(n, alphabet_size))
    """
    char_index = {}
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length


def min_size_subarray_sum(nums: List[int], target: int) -> int:
    """
    LeetCode 209 - Minimum Size Subarray Sum
    Find minimal length subarray with sum >= target.
    
    Time: O(n), Space: O(1)
    """
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0


def max_consecutive_ones(nums: List[int], k: int) -> int:
    """
    LeetCode 1004 - Max Consecutive Ones III
    Max consecutive ones after flipping at most k zeros.
    
    Time: O(n), Space: O(1)
    """
    left = 0
    zeros_count = 0
    max_length = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros_count += 1
        
        while zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


if __name__ == "__main__":
    print("=" * 60)
    print("VARIABLE SIZE SLIDING WINDOW")
    print("=" * 60)
    
    # Longest substring without repeating characters
    print("\n--- Longest Substring Without Repeating ---")
    test_strings = ["abcabcbb", "bbbbb", "pwwkew", " "]
    for s in test_strings:
        result = length_of_longest_substring(s)
        print(f"'{s}' → {result}")
    
    # Minimum size subarray sum
    print("\n--- Minimum Size Subarray Sum ---")
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    result = min_size_subarray_sum(nums, target)
    print(f"nums={nums}, target={target} → min length={result}")
    
    # Max consecutive ones
    print("\n--- Max Consecutive Ones ---")
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    result = max_consecutive_ones(nums, k)
    print(f"nums={nums}, k={k} → max length={result}")
    
    print("\n✅ Variable size sliding window complete!")
