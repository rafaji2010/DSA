"""
LeetCode 167 - Two Sum II (Input Array Is Sorted)
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Time: O(n) - single pass with two pointers
Space: O(1) - only two pointers
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # 1-indexed as per problem
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []  # Problem guarantees a solution exists

if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2,7,11,15], 9) == [1,2]
    assert s.twoSum([2,3,4], 6) == [1,3]
    assert s.twoSum([-1,0], -1) == [1,2]
    print("✅ All tests passed for LeetCode 167!")
