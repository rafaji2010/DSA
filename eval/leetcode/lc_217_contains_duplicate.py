"""
LeetCode 217 - Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array, return true if any value appears at least twice.

Time: O(n) - single pass with hash set
Space: O(n) - hash set stores up to n elements
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Hash set approach - O(n) time, O(n) space"""
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    def containsDuplicateSort(self, nums: List[int]) -> bool:
        """Sorting approach - O(n log n) time, O(1) space"""
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
    ]
    
    print("=" * 50)
    print("LeetCode 217 - Contains Duplicate")
    print("=" * 50)
    
    for nums, expected in test_cases:
        result = s.containsDuplicate(nums)
        status = "✅" if result == expected else "❌"
        print(f"{status} {nums} → {result}")
    
    print("\n✅ Contains Duplicate complete!")
