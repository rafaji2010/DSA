"""
LeetCode 350 - Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, return their intersection (including duplicates).

Time: O(m + n)
Space: O(min(m, n))
"""

from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Hash map count approach"""
        count = Counter(nums1)
        result = []
        
        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1
        
        return result
    
    def intersectTwoPointer(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Two pointers approach (requires sorted arrays)"""
        nums1.sort()
        nums2.sort()
        
        result = []
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return result


if __name__ == "__main__":
    s = Solution()
    
    test_cases = [
        ([1, 2, 2, 1], [2, 2], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
        ([1, 2, 3], [4, 5, 6], []),
    ]
    
    print("=" * 50)
    print("LeetCode 350 - Intersection II")
    print("=" * 50)
    
    for nums1, nums2, expected in test_cases:
        result = s.intersect(nums1, nums2)
        result.sort()
        expected.sort()
        status = "✅" if result == expected else "❌"
        print(f"{status} {nums1} ∩ {nums2} = {result}")
    
    print("\n✅ Intersection II complete!")
