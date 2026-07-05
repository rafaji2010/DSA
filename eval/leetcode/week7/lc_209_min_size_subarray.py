"""
LeetCode 209 - Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers and a target sum, return the minimal length
of a contiguous subarray whose sum is >= target.

Time: O(n), Space: O(1)
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
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


if __name__ == "__main__":
    s = Solution()
    
    test_cases = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        (15, [1, 2, 3, 4, 5], 5),
    ]
    
    print("=" * 50)
    print("LeetCode 209 - Minimum Size Subarray Sum")
    print("=" * 50)
    
    for target, nums, expected in test_cases:
        result = s.minSubArrayLen(target, nums)
        status = "✅" if result == expected else "❌"
        print(f"{status} target={target}, nums={nums} → {result} (expected {expected})")
    
    print("\n✅ Problem 209 complete!")
