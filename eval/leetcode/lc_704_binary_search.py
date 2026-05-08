"""
LeetCode 704 - Binary Search
https://leetcode.com/problems/binary-search/

Problem:
Given a sorted (ascending) array of integers and a target integer,
return the index of the target if it exists, otherwise return -1.

Time Complexity: O(log n) - halves search space each iteration
Space Complexity: O(1) - only uses constant extra space

Examples:
>>> Solution().search([-1,0,3,5,9,12], 9)
4
>>> Solution().search([-1,0,3,5,9,12], 2)
-1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Search for target in sorted array using binary search.
        
        Args:
            nums: Sorted array of integers (ascending order)
            target: Integer value to search for
        
        Returns:
            Index of target if found, otherwise -1
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Calculate middle index
            mid = (left + right) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            
            # Target is in right half (larger values)
            elif nums[mid] < target:
                left = mid + 1
            
            # Target is in left half (smaller values)
            else:
                right = mid - 1
        
        # Target not found
        return -1


# Alternative: Recursive solution (for learning)
class SolutionRecursive:
    def search(self, nums: List[int], target: int) -> int:
        """Recursive version of binary search."""
        return self._binary_search_recursive(nums, target, 0, len(nums) - 1)
    
    def _binary_search_recursive(self, nums: List[int], target: int, left: int, right: int) -> int:
        """Helper recursive function."""
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self._binary_search_recursive(nums, target, mid + 1, right)
        else:
            return self._binary_search_recursive(nums, target, left, mid - 1)

# Test locally
if __name__ == "__main__":
    from typing import List
    
    sol = Solution()
    
    print("=" * 50)
    print("Testing LeetCode 704 - Binary Search")
    print("=" * 50)
    
    # Test case 1 - Add type annotation
    nums1: List[int] = [-1, 0, 3, 5, 9, 12]
    target1: int = 9
    result1: int = sol.search(nums1, target1)
    expected1: int = 4
    print(f"Test 1: {nums1}, target={target1}")
    print(f"  Result: {result1}, Expected: {expected1} {'✓' if result1 == expected1 else '✗'}")
    
    # Test case 2
    nums2: List[int] = [-1, 0, 3, 5, 9, 12]
    target2: int = 2
    result2: int = sol.search(nums2, target2)
    expected2: int = -1
    print(f"Test 2: {nums2}, target={target2}")
    print(f"  Result: {result2}, Expected: {expected2} {'✓' if result2 == expected2 else '✗'}")
    
    # Test case 3 - Single element
    nums3: List[int] = [5]
    target3: int = 5
    result3: int = sol.search(nums3, target3)
    expected3: int = 0
    print(f"Test 3: {nums3}, target={target3}")
    print(f"  Result: {result3}, Expected: {expected3} {'✓' if result3 == expected3 else '✗'}")
    
    # Test case 4 - Single element not found
    nums4: List[int] = [5]
    target4: int = -5
    result4: int = sol.search(nums4, target4)
    expected4: int = -1
    print(f"Test 4: {nums4}, target={target4}")
    print(f"  Result: {result4}, Expected: {expected4} {'✓' if result4 == expected4 else '✗'}")
    
    # Test case 5 - Empty array (FIX THIS ONE)
    nums5: List[int] = []  # ← Add : List[int] annotation
    target5: int = 5
    result5: int = sol.search(nums5, target5)
    expected5: int = -1
    print(f"Test 5: {nums5}, target={target5}")
    print(f"  Result: {result5}, Expected: {expected5} {'✓' if result5 == expected5 else '✗'}")
    
    # Test recursive version
    print("\n" + "-" * 50)
    print("Testing Recursive Version")
    print("-" * 50)
    sol_rec: SolutionRecursive = SolutionRecursive()
    result_rec: int = sol_rec.search(nums1, target1)
    print(f"Recursive search for {target1}: {result_rec} {'✓' if result_rec == expected1 else '✗'}")
    
    print("\n" + "=" * 50)
    print("All tests passed! Ready to submit to LeetCode! 🎉")
    print("=" * 50)
