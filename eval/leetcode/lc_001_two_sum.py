"""
LeetCode 1 - Two Sum
https://leetcode.com/problems/two-sum/

Time: O(n) - single pass through array
Space: O(n) - hash map stores up to n elements
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        
        return []  # Problem guarantees a solution exists


if __name__ == "__main__":
    s = Solution()
    
    # Test cases
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    
    print("✅ All tests passed!")