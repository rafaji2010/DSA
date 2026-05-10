# core/squares_sorted.py
"""LeetCode 977 - Squares of a Sorted Array.

Given an integer array sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""

from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class TraceStep:
    """Structure for visualization trace."""
    step: int
    left: int
    right: int
    left_val: int
    right_val: int
    left_sq: int
    right_sq: int
    picked_from: str  # 'left' or 'right'
    result_pos: int
    result_state: List[int]


def sorted_squares(nums: List[int]) -> List[int]:
    """
    Return squares of each number in sorted order.
    
    Time: O(n) - single pass with two pointers
    Space: O(n) - for result array (required by problem)
    
    Args:
        nums: Sorted array (may contain negative numbers)
    
    Returns:
        New array with squares in sorted order
    
    Examples:
        >>> sorted_squares([-4, -1, 0, 3, 10])
        [0, 1, 9, 16, 100]
        >>> sorted_squares([-7, -3, 2, 3, 11])
        [4, 9, 9, 49, 121]
    """
    n: int = len(nums)
    result: List[int] = [0] * n
    left: int = 0
    right: int = n - 1
    pos: int = n - 1  # Fill from the END
    
    while left <= right:
        left_sq: int = nums[left] ** 2
        right_sq: int = nums[right] ** 2
        
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1
        pos -= 1
    
    return result


def sorted_squares_with_trace(nums: List[int]) -> Tuple[List[int], List[TraceStep]]:
    """
    Same as sorted_squares but returns trace for visualization.
    
    Returns:
        Tuple of (result, trace_steps)
    """
    n: int = len(nums)
    result: List[int] = [0] * n
    left: int = 0
    right: int = n - 1
    pos: int = n - 1
    trace: List[TraceStep] = []
    step: int = 1
    
    while left <= right:
        left_sq: int = nums[left] ** 2
        right_sq: int = nums[right] ** 2
        picked_from: str = 'left' if left_sq > right_sq else 'right'
        
        trace.append(TraceStep(
            step=step,
            left=left,
            right=right,
            left_val=nums[left],
            right_val=nums[right],
            left_sq=left_sq,
            right_sq=right_sq,
            picked_from=picked_from,
            result_pos=pos,
            result_state=result.copy()
        ))
        
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1
        pos -= 1
        step += 1
    
    return result, trace


def sorted_squares_naive(nums: List[int]) -> List[int]:
    """
    Naive solution: square then sort.
    Time: O(n log n), Space: O(n)
    
    This is included to show WHY two pointers is better!
    """
    return sorted(x * x for x in nums)


def visualize_sorted_squares() -> None:
    """Interactive visualization of sorted squares algorithm."""
    print("=" * 70)
    print("Squares of a Sorted Array - Visualization")
    print("=" * 70)
    
    nums: List[int] = [-4, -1, 0, 3, 10]
    print(f"\nOriginal: {nums}")
    print("\n" + "-" * 70)
    
    result, trace = sorted_squares_with_trace(nums)
    
    for step_info in trace:
        print(f"\nStep {step_info.step}:")
        print(f"  left={step_info.left} (value={step_info.left_val}, sq={step_info.left_sq})")
        print(f"  right={step_info.right} (value={step_info.right_val}, sq={step_info.right_sq})")
        
        # Visual pointer display
        arr_display = []
        for i, val in enumerate(nums):
            if i == step_info.left and i == step_info.right:
                arr_display.append(f"[{val}]←LR")
            elif i == step_info.left:
                arr_display.append(f"[{val}]←L")
            elif i == step_info.right:
                arr_display.append(f"[{val}]←R")
            else:
                arr_display.append(f" {val} ")
        
        print(f"  Array:     {' '.join(arr_display)}")
        
        # Show comparison
        print(f"  Compare:   {step_info.left_sq} vs {step_info.right_sq}")
        
        if step_info.picked_from == 'left':
            print(f"  → {step_info.left_sq} > {step_info.right_sq}, pick LEFT")
            print(f"  → Place {step_info.left_sq} at position {step_info.result_pos}")
        else:
            print(f"  → {step_info.right_sq} >= {step_info.left_sq}, pick RIGHT")
            print(f"  → Place {step_info.right_sq} at position {step_info.result_pos}")
        
        # Show result array progress
        result_so_far = step_info.result_state.copy()
        if step_info.picked_from == 'left':
            result_so_far[step_info.result_pos] = step_info.left_sq
        else:
            result_so_far[step_info.result_pos] = step_info.right_sq
        
        # Visual result display
        result_display = []
        for i, val in enumerate(result_so_far):
            if val == 0 and i > step_info.result_pos:
                result_display.append(" _ ")
            elif i == step_info.result_pos:
                result_display.append(f"[{val}]←placing")
            else:
                result_display.append(f" {val} ")
        
        print(f"  Result:    {' '.join(result_display)}")
        print(f"  → left={step_info.left + (1 if step_info.picked_from == 'left' else 0)}, "
              f"right={step_info.right - (1 if step_info.picked_from == 'right' else 0)}")
    
    print(f"\n{'='*70}")
    print(f"FINAL RESULT: {result}")
    print("=" * 70)


def sorted_squares_optimized(nums: List[int]) -> List[int]:
    """
    Alternative implementation using absolute values.
    Same logic, different style.
    """
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    
    for pos in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] ** 2
            left += 1
        else:
            result[pos] = nums[right] ** 2
            right -= 1
    
    return result


if __name__ == "__main__":
    # Test cases
    test_cases: List[Tuple[List[int], List[int]]] = [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([-5, -3, -2, -1], [1, 4, 9, 25]),
        ([0, 1, 2, 3, 4], [0, 1, 4, 9, 16]),
        ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]),
        ([-2, -1, 0, 1, 2], [0, 1, 1, 4, 4]),
        ([], []),
        ([5], [25]),
    ]
    
    print("=" * 60)
    print("Squares of a Sorted Array - Test Cases")
    print("=" * 60)
    
    for nums, expected in test_cases:
        result = sorted_squares(nums.copy())
        status = "✅" if result == expected else "❌"
        print(f"\n{status} {nums}")
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")
    
    # Run visualization
    print("\n")
    visualize_sorted_squares()
    
    # Performance comparison
    print("\n" + "=" * 60)
    print("Performance Comparison")
    print("=" * 60)
    
    import time
    import random
    
    # Create large sorted array with negatives and positives
    large_array: List[int] = sorted([random.randint(-10000, 10000) for _ in range(10000)])
    
    # Two Pointers version (O(n))
    start = time.perf_counter()
    result_2ptr = sorted_squares(large_array.copy())
    time_2ptr = time.perf_counter() - start
    
    # Naive version (O(n log n))
    start = time.perf_counter()
    result_naive = sorted_squares_naive(large_array.copy())
    time_naive = time.perf_counter() - start
    
    print(f"\nTwo Pointers (O(n)):     {time_2ptr:.6f}s")
    print(f"Naive (O(n log n)):      {time_naive:.6f}s")
    print(f"Speedup: {time_naive/time_2ptr:.1f}x faster!")
    print(f"\nBoth produce same result: {result_2ptr == result_naive}")