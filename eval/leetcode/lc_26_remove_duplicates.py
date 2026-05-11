"""
LeetCode 26 - Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Time: O(n) - single pass
Space: O(1) - in-place modification
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Pointer for position of next unique element
        write_pos = 1
        
        for read_pos in range(1, len(nums)):
            if nums[read_pos] != nums[read_pos - 1]:
                nums[write_pos] = nums[read_pos]
                write_pos += 1
        
        return write_pos

if __name__ == "__main__":
    s = Solution()
    
    # Test 1
    nums1 = [1,1,2]
    k1 = s.removeDuplicates(nums1)
    assert k1 == 2
    assert nums1[:k1] == [1,2]
    
    # Test 2
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = s.removeDuplicates(nums2)
    assert k2 == 5
    assert nums2[:k2] == [0,1,2,3,4]
    
    print("✅ All tests passed for LeetCode 26!")
