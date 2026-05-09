# core/binary_search_variations.py
"""Binary search variations for handling duplicate elements.

This module extends standard binary search to find:
- First occurrence of a target
- Last occurrence of a target  
- Count of occurrences (using first + last)

All implementations maintain O(log n) time complexity.
"""

from typing import List


def find_first_occurrence(arr: List[int], target: int) -> int:
    """
    Find the first (leftmost) index where target appears.
    
    Time: O(log n) — binary search with one extra assignment
    Space: O(1) — only uses a few variables
    
    Args:
        arr: Sorted list of integers
        target: Value to search for
    
    Returns:
        Index of first occurrence, or -1 if not found
    
    Examples:
        >>> find_first_occurrence([1, 2, 2, 2, 3, 4], 2)
        1
        >>> find_first_occurrence([1, 2, 3, 4], 5)
        -1
        >>> find_first_occurrence([], 5)
        -1
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid          # Store this match
            right = mid - 1       # Keep searching LEFT for earlier occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:  # arr[mid] > target
            right = mid - 1
    
    return result


def find_last_occurrence(arr: List[int], target: int) -> int:
    """
    Find the last (rightmost) index where target appears.
    
    Time: O(log n)
    Space: O(1)
    
    Args:
        arr: Sorted list of integers
        target: Value to search for
    
    Returns:
        Index of last occurrence, or -1 if not found
    
    Examples:
        >>> find_last_occurrence([1, 2, 2, 2, 3, 4], 2)
        3
        >>> find_last_occurrence([1, 2, 3, 4], 5)
        -1
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid          # Store this match
            left = mid + 1        # Keep searching RIGHT for later occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:  # arr[mid] > target
            right = mid - 1
    
    return result


def count_occurrences(arr: List[int], target: int) -> int:
    """
    Count how many times target appears in sorted array.
    
    Time: O(log n) — two binary searches
    Space: O(1)
    
    This is more efficient than O(n) linear scan when the array is large.
    
    Args:
        arr: Sorted list of integers
        target: Value to count
    
    Returns:
        Number of occurrences (0 if not found)
    
    Examples:
        >>> count_occurrences([1, 2, 2, 2, 3, 4], 2)
        3
        >>> count_occurrences([1, 2, 3, 4], 5)
        0
        >>> count_occurrences([], 5)
        0
    """
    first = find_first_occurrence(arr, target)
    if first == -1:
        return 0
    last = find_last_occurrence(arr, target)
    return last - first + 1


def find_first_or_last(arr: List[int], target: int, find_first: bool = True) -> int:
    """
    Unified function to find first or last occurrence.
    
    This shows how the two algorithms are identical except for one line.
    
    Time: O(log n)
    Space: O(1)
    
    Args:
        arr: Sorted list of integers
        target: Value to search for
        find_first: True for first occurrence, False for last
    
    Returns:
        Index of first or last occurrence, or -1 if not found
    
    Examples:
        >>> find_first_or_last([1, 2, 2, 2, 3, 4], 2, find_first=True)
        1
        >>> find_first_or_last([1, 2, 2, 2, 3, 4], 2, find_first=False)
        3
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            if find_first:
                right = mid - 1   # Search LEFT for first
            else:
                left = mid + 1    # Search RIGHT for last
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def find_first_greater_than(arr: List[int], target: int) -> int:
    """
    Find first index where value > target.
    Returns len(arr) if all elements <= target.
    
    Time: O(log n)
    Space: O(1)
    
    Example:
    >>> find_first_greater_than([1, 2, 2, 2, 3, 4], 2)
    4  # index of 3
    >>> find_first_greater_than([1, 2, 3, 4, 5], 5)
    5  # all elements <= target
    """
    left, right = 0, len(arr) - 1
    result = len(arr)  # Default: insertion point at end
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] > target:
            result = mid    # Found a candidate
            right = mid - 1  # Search for an even earlier one
        else:
            left = mid + 1   # Need a larger value
    
    return result


def find_last_less_than(arr: List[int], target: int) -> int:
    """
    Find last index where value < target.
    Returns -1 if all elements >= target.
    
    Time: O(log n)
    Space: O(1)
    
    Example:
    >>> find_last_less_than([1, 2, 2, 2, 3, 4], 2)
    0  # index of 1
    """
    left, right = 0, len(arr) - 1
    result = -1  # Default: no element less than target
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] < target:
            result = mid    # Found a candidate
            left = mid + 1   # Search for a later one
        else:
            right = mid - 1  # Need a smaller value
    
    return result

if __name__ == "__main__":
    test_arr = [1, 2, 2, 2, 3, 4, 5, 5, 6]
    
    print("=" * 60)
    print("Binary Search Variations - First & Last Occurrence")
    print("=" * 60)
    
    print(f"\nArray: {test_arr}")
    print(f"Target: 2")
    print(f"  First occurrence: index {find_first_occurrence(test_arr, 2)}")
    print(f"  Last occurrence:  index {find_last_occurrence(test_arr, 2)}")
    print(f"  Count: {count_occurrences(test_arr, 2)}")
    
    print(f"\nTarget: 5")
    print(f"  First occurrence: index {find_first_occurrence(test_arr, 5)}")
    print(f"  Last occurrence:  index {find_last_occurrence(test_arr, 5)}")
    print(f"  Count: {count_occurrences(test_arr, 5)}")
    
    print(f"\nTarget: 10 (not in array)")
    print(f"  First occurrence: {find_first_occurrence(test_arr, 10)}")
    print(f"  Count: {count_occurrences(test_arr, 10)}")
    
    print(f"\nTarget: 1 (at start)")
    print(f"  First occurrence: {find_first_occurrence(test_arr, 1)}")
    print(f"  Last occurrence:  {find_last_occurrence(test_arr, 1)}")
    
    print(f"\nTarget: 6 (at end)")
    print(f"  First occurrence: {find_first_occurrence(test_arr, 6)}")
    print(f"  Last occurrence:  {find_last_occurrence(test_arr, 6)}")
    
    # Demonstrate unified function
    print("\n" + "=" * 60)
    print("Unified Function Demo")
    print("=" * 60)
    print(f"Target: 2")
    print(f"  First (unified): {find_first_or_last(test_arr, 2, find_first=True)}")
    print(f"  Last  (unified): {find_first_or_last(test_arr, 2, find_first=False)}")
    
    # NEW: Demonstrate find_first_greater_than and find_last_less_than
    print("\n" + "=" * 60)
    print("Advanced Binary Search Variations")
    print("=" * 60)
    
    print(f"\nArray: {test_arr}")
    print(f"Target: 2")
    print(f"  First greater than 2: index {find_first_greater_than(test_arr, 2)} (value = {test_arr[find_first_greater_than(test_arr, 2)] if find_first_greater_than(test_arr, 2) < len(test_arr) else 'out of range'})")
    print(f"  Last less than 2: index {find_last_less_than(test_arr, 2)} (value = {test_arr[find_last_less_than(test_arr, 2)] if find_last_less_than(test_arr, 2) != -1 else 'none'})")
    
    print(f"\nTarget: 4")
    print(f"  First greater than 4: index {find_first_greater_than(test_arr, 4)} (value = {test_arr[find_first_greater_than(test_arr, 4)]})")
    print(f"  Last less than 4: index {find_last_less_than(test_arr, 4)} (value = {test_arr[find_last_less_than(test_arr, 4)]})")
    
    print(f"\nTarget: 10 (greater than all)")
    print(f"  First greater than 10: index {find_first_greater_than(test_arr, 10)} (returns len(arr) = {len(test_arr)})")
    print(f"  Last less than 10: index {find_last_less_than(test_arr, 10)} (value = {test_arr[find_last_less_than(test_arr, 10)]})")
    
    print(f"\nTarget: 0 (less than all)")
    print(f"  First greater than 0: index {find_first_greater_than(test_arr, 0)} (value = {test_arr[find_first_greater_than(test_arr, 0)]})")
    print(f"  Last less than 0: index {find_last_less_than(test_arr, 0)} (returns -1)")