"""
LeetCode 349 - Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/

Given two arrays, return their intersection (unique values).

Time: O(m + n)
Space: O(min(m, n))
"""

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Hash set approach"""
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)  # Intersection using &
    
    def intersectionTwoPointer(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Two pointers approach (requires sorted arrays)"""
        nums1.sort()
        nums2.sort()
        
        result = []
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not result or result[-1] != nums1[i]:
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
        ([1, 2, 2, 1], [2, 2], [2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
        ([1, 2, 3], [4, 5, 6], []),
    ]
    
    print("=" * 50)
    print("LeetCode 349 - Intersection of Arrays")
    print("=" * 50)
    
    for nums1, nums2, expected in test_cases:
        result = s.intersection(nums1, nums2)
        result.sort()
        status = "✅" if result == expected else "❌"
        print(f"{status} {nums1} ∩ {nums2} = {result}")
    
    print("\n✅ Intersection complete!")
