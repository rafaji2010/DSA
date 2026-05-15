# core/search_insert_position.py
"""LeetCode 35 - Search Insert Position.

Given a sorted array and target, return the index where target would be
inserted to maintain sorted order. If target exists, return its index.
"""

from typing import List


def search_insert(nums: List[int], target: int) -> int:
    """
    Return index where target should be inserted to maintain sorted order.
    
    Time: O(log n) - binary search
    Space: O(1) - only uses variables
    
    Args:
        nums: Sorted list of integers
        target: Value to search for or insert
    
    Returns:
        Index where target exists or should be inserted
    
    Examples:
        >>> search_insert([1, 3, 5, 6], 5)
        2
        >>> search_insert([1, 3, 5, 6], 2)
        1
        >>> search_insert([1, 3, 5, 6], 7)
        4
        >>> search_insert([1, 3, 5, 6], 0)
        0
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid           # Found! Return its index
        elif nums[mid] < target:
            left = mid + 1       # Target is in right half
        else:
            right = mid - 1      # Target is in left half
    
    # Not found - insertion point is 'left'
    return left


def search_insert_recursive(nums: List[int], target: int) -> int:
    """Recursive version for comparison."""
    def _search(left: int, right: int) -> int:
        if left > right:
            return left
        
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return _search(mid + 1, right)
        else:
            return _search(left, mid - 1)
    
    return _search(0, len(nums) - 1)


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0),
        ([1], 2, 1),
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 6, 5),
        ([], 5, 0),
    ]
    
    print("=" * 60)
    print("LeetCode 35 - Search Insert Position")
    print("=" * 60)
    
    for nums, target, expected in test_cases:
        result = search_insert(nums, target)
        status = "✅" if result == expected else "❌"
        
        # Show what the result means
        if result < len(nums) and nums[result] == target:
            meaning = f"Found {target} at index {result}"
        elif result < len(nums):
            meaning = f"Insert {target} before {nums[result]} (index {result})"
        else:
            meaning = f"Append {target} at end (index {result})"
        
        print(f"{status} {nums}, target={target} → {result} ({meaning})")