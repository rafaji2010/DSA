"""
core/sorting/counting_sort.py
Counting Sort - O(n + k) time, O(k) space
Where k = range of input values
"""

from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting Sort implementation.
    
    Time: O(n + k) where k = max - min + 1
    Space: O(k)
    
    Works best when:
    - Range of values (k) is small
    - Values are integers
    """
    if not arr:
        return []
    
    # Find range
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1
    
    # Count occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    
    # Reconstruct sorted array
    result = []
    for i, cnt in enumerate(count):
        value = i + min_val
        result.extend([value] * cnt)
    
    return result


def counting_sort_stable(arr: List[int]) -> List[int]:
    """
    Stable Counting Sort (preserves relative order of equal elements).
    
    Uses cumulative counts to determine positions.
    """
    if not arr:
        return []
    
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1
    
    # Count occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    
    # Calculate cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output from right to left (for stability)
    output = [0] * len(arr)
    for num in reversed(arr):
        idx = num - min_val
        count[idx] -= 1
        output[count[idx]] = num
    
    return output


def counting_sort_with_trace(arr: List[int]) -> List[int]:
    """Counting Sort with detailed tracing."""
    if not arr:
        return []
    
    print(f"Original: {arr}")
    
    min_val = min(arr)
    max_val = max(arr)
    print(f"Range: min={min_val}, max={max_val}")
    
    range_size = max_val - min_val + 1
    count = [0] * range_size
    
    print("\nCounting occurrences:")
    for num in arr:
        idx = num - min_val
        count[idx] += 1
        print(f"  {num} → count[{idx}] = {count[idx]}")
    
    print(f"\nCount array: {count}")
    print("(index: value → frequency)")
    
    # Reconstruct
    result = []
    for i, cnt in enumerate(count):
        value = i + min_val
        if cnt > 0:
            print(f"  Value {value} appears {cnt} time(s)")
            result.extend([value] * cnt)
    
    print(f"\nSorted: {result}")
    return result


if __name__ == "__main__":
    print("=" * 60)
    print("COUNTING SORT DEMONSTRATION")
    print("=" * 60)
    
    test_arrays = [
        [4, 2, 2, 8, 3, 3, 1, 4],
        [5, 3, 1, 2, 4],
        [10, 5, 3, 8, 2],
        [1, 1, 1, 1, 1],
    ]
    
    for arr in test_arrays:
        print(f"\nOriginal: {arr}")
        sorted_arr = counting_sort(arr)
        print(f"Sorted:   {sorted_arr}")
    
    print("\n" + "-" * 40)
    print("DETAILED TRACE")
    print("-" * 40)
    counting_sort_with_trace([4, 2, 2, 8, 3, 3, 1, 4])
    
    print("\n" + "=" * 60)
    print("WHEN COUNTING SORT BREAKS")
    print("=" * 60)
    
    # Large range example
    arr_large_range = [1, 1000000, 2, 999999]
    print(f"\nLarge range array: {arr_large_range}")
    print(f"Range size: {max(arr_large_range) - min(arr_large_range) + 1}")
    print(f"This would require a count array of ~1,000,000 elements!")
    print(f"Time: O(n + k) = O(1,000,000) - still works but memory heavy")
    
    # Non-integer example
    arr_float = [3.2, 1.5, 4.8, 2.1]
    print(f"\nFloat array: {arr_float}")
    print("Counting Sort only works for integers!")
    print("(Would need to convert or use different algorithm)")
    
    print("\n✅ Counting Sort complete!")
