"""
LeetCode 977 - Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

Time: O(n) - two pointers from both ends
Space: O(n) - for result array
"""

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        
        for i in range(n - 1, -1, -1):
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                result[i] = left_square
                left += 1
            else:
                result[i] = right_square
                right -= 1
        
        return result

if __name__ == "__main__":
    s = Solution()
    
    # Test 1
    assert s.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
    
    # Test 2
    assert s.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
    
    print("✅ All tests passed for LeetCode 977!")
