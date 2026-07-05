#!/usr/bin/env python3
"""
tests/practice/buggy_merge_sort.py
INTENTIONALLY BUGGY merge sort for pdb practice.
DO NOT FIX BY READING — fix by debugging with pdb only!
"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """Sort array using merge sort."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted arrays. BUG INTRODUCED HERE."""
    result = []
    i = j = 0

    # BUG: Using <= instead of < causes IndexError
    while i <= len(left) and j <= len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    test_arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original: {test_arr}")
    breakpoint()
    sorted_arr = merge_sort(test_arr)
    print(f"Sorted:   {sorted_arr}")

