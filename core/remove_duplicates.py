# core/remove_duplicates.py
"""LeetCode 26 - Remove Duplicates from Sorted Array.

Remove duplicates in-place and return the new length.
The relative order must be preserved.
"""

from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class TraceStep:
    """Structure for visualization trace."""
    step: int
    fast: int
    slow: int
    fast_val: int
    slow_val: int
    is_duplicate: bool
    array_state: List[int]


def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates in-place from sorted array.
    Returns the new length.
    
    Time: O(n) - single pass with two pointers
    Space: O(1) - in-place modification
    
    Args:
        nums: Sorted list of integers (may contain duplicates)
    
    Returns:
        Length of array after removing duplicates
    
    Examples:
        >>> arr = [1, 1, 2, 2, 3, 4, 4, 5]
        >>> length = remove_duplicates(arr)
        >>> arr[:length]
        [1, 2, 3, 4, 5]
    """
    if not nums:
        return 0
    
    slow: int = 0
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1


def remove_duplicates_with_trace(nums: List[int]) -> Tuple[int, List[TraceStep]]:
    """
    Same as remove_duplicates but returns trace for visualization.
    
    Returns:
        Tuple of (new_length, trace_steps)
    """
    if not nums:
        return 0, []
    
    slow: int = 0
    trace: List[TraceStep] = []
    step: int = 1
    
    for fast in range(1, len(nums)):
        is_dup: bool = (nums[fast] == nums[slow])
        
        trace.append(TraceStep(
            step=step,
            fast=fast,
            slow=slow,
            fast_val=nums[fast],
            slow_val=nums[slow],
            is_duplicate=is_dup,
            array_state=nums.copy()
        ))
        
        if not is_dup:
            slow += 1
            nums[slow] = nums[fast]
        
        step += 1
    
    return slow + 1, trace


def visualize_remove_duplicates() -> None:
    """Interactive visualization of remove duplicates algorithm."""
    print("=" * 70)
    print("Remove Duplicates from Sorted Array - Visualization")
    print("=" * 70)
    
    nums: List[int] = [1, 1, 2, 2, 3, 4, 4, 5]
    print(f"\nOriginal: {nums}")
    print("\n" + "-" * 70)
    
    # Make a copy for visualization
    nums_copy: List[int] = nums.copy()
    length, trace = remove_duplicates_with_trace(nums_copy)
    
    for step_info in trace:
        print(f"\nStep {step_info.step}:")
        print(f"  slow={step_info.slow} (value={step_info.slow_val}), "
              f"fast={step_info.fast} (value={step_info.fast_val})")
        
        # Visual pointer display
        arr_display = []
        for i, val in enumerate(step_info.array_state):
            if i == step_info.slow and i == step_info.fast:
                arr_display.append(f"[{val}]←SF")
            elif i == step_info.slow:
                arr_display.append(f"[{val}]←S")
            elif i == step_info.fast:
                arr_display.append(f"[{val}]←F")
            else:
                arr_display.append(f" {val} ")
        
        print(f"  Array: {' '.join(arr_display)}")
        
        if step_info.is_duplicate:
            print(f"  → {step_info.fast_val} == {step_info.slow_val} (DUPLICATE)")
            print(f"  → Only advancing fast pointer")
        else:
            print(f"  → {step_info.fast_val} != {step_info.slow_val} (NEW VALUE!)")
            print(f"  → slow++ to {step_info.slow + 1}")
            print(f"  → Copy {step_info.fast_val} to position {step_info.slow + 1}")
    
    print(f"\n{'='*70}")
    print(f"Final array: {nums_copy}")
    print(f"Unique portion: {nums_copy[:length]}")
    print(f"New length: {length}")
    print("=" * 70)


def remove_duplicates_alternative(nums: List[int]) -> int:
    """
    Alternative implementation using while loop instead of for.
    Same complexity, different style.
    """
    if not nums:
        return 0
    
    slow: int = 0
    fast: int = 1
    
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    
    return slow + 1


if __name__ == "__main__":
    # Test cases
    test_cases: List[Tuple[List[int], int, List[int]]] = [
        ([1, 1, 2], 2, [1, 2]),
        ([1, 1, 2, 2, 3, 4, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 1, 1, 1, 1], 1, [1]),
        ([], 0, []),
        ([1], 1, [1]),
    ]
    
    print("=" * 60)
    print("Remove Duplicates - Test Cases")
    print("=" * 60)
    
    for nums, expected_length, expected_array in test_cases:
        nums_copy = nums.copy()
        result_length = remove_duplicates(nums_copy)
        status = "✅" if result_length == expected_length else "❌"
        print(f"\n{status} Original: {nums}")
        print(f"   Expected length: {expected_length}, Got: {result_length}")
        print(f"   Result array: {nums_copy[:result_length]}")
        if result_length == expected_length:
            print(f"   Correct! {nums_copy[:result_length]} == {expected_array}")
    
    # Run visualization
    print("\n")
    visualize_remove_duplicates()
    
    # Compare implementations
    print("\n" + "=" * 60)
    print("Implementation Comparison")
    print("=" * 60)
    
    import time
    
    large_array: List[int] = list(range(10000)) + list(range(10000))  # 20,000 elements with duplicates
    large_array.sort()
    
    # For loop version
    arr1 = large_array.copy()
    start = time.perf_counter()
    len1 = remove_duplicates(arr1)
    time1 = time.perf_counter() - start
    
    # While loop version
    arr2 = large_array.copy()
    start = time.perf_counter()
    len2 = remove_duplicates_alternative(arr2)
    time2 = time.perf_counter() - start
    
    print(f"\nFor loop version:  {time1:.6f}s (length={len1})")
    print(f"While loop version: {time2:.6f}s (length={len2})")
    print(f"Both produce same length: {len1 == len2}")