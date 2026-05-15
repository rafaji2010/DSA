# core/two_sum_sorted.py
"""LeetCode 167 - Two Sum II (Input Array Is Sorted).

Given a 1-indexed sorted array, find two numbers that sum to target.
Return indices as [index1, index2] where index1 < index2.
"""

from typing import List, Tuple, TypedDict


# Define the structure of each trace step for type safety
class TraceStep(TypedDict):
    """Type definition for visualization trace steps."""
    step: int
    left: int
    right: int
    left_val: int
    right_val: int
    sum: int
    action: str


def two_sum(numbers: List[int], target: int) -> List[int]:
    """
    Find two numbers that sum to target using two pointers.
    
    Time: O(n) - single pass with two pointers
    Space: O(1) - only two pointers
    
    Args:
        numbers: Sorted array of integers
        target: Target sum
    
    Returns:
        1-indexed indices of the two numbers [index1, index2]
    
    Examples:
        >>> two_sum([2, 7, 11, 15], 9)
        [1, 2]
        >>> two_sum([2, 3, 4], 6)
        [1, 3]
        >>> two_sum([-1, 0], -1)
        [1, 2]
    """
    left: int = 0
    right: int = len(numbers) - 1
    
    while left < right:
        current_sum: int = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Convert to 1-indexed (LeetCode requirement)
            return [left + 1, right + 1]
        elif current_sum < target:
            # Need larger sum → move left pointer right
            left += 1
        else:  # current_sum > target
            # Need smaller sum → move right pointer left
            right -= 1
    
    # Problem guarantees a solution exists, so we never reach here
    return []


def two_sum_with_trace(numbers: List[int], target: int) -> Tuple[List[int], List[TraceStep]]:
    """
    Same as two_sum but returns trace for visualization.
    
    Returns:
        Tuple of (result, trace_steps)
    """
    left: int = 0
    right: int = len(numbers) - 1
    trace: List[TraceStep] = []
    step: int = 1
    
    while left < right:
        current_sum: int = numbers[left] + numbers[right]
        
        trace.append({
            'step': step,
            'left': left,
            'right': right,
            'left_val': numbers[left],
            'right_val': numbers[right],
            'sum': current_sum,
            'action': 'FOUND!' if current_sum == target else ('move left' if current_sum < target else 'move right')
        })
        
        if current_sum == target:
            return [left + 1, right + 1], trace
        elif current_sum < target:
            left += 1
        else:
            right -= 1
        
        step += 1
    
    return [], trace


def two_sum_brute_force(numbers: List[int], target: int) -> List[int]:
    """
    Brute force solution for comparison.
    Time: O(n²), Space: O(1)
    
    This is included to show WHY two pointers is better!
    """
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    return []


def visualize_two_sum() -> None:
    """Interactive visualization of Two Sum II algorithm."""
    print("=" * 70)
    print("Two Sum II - Two Pointers Visualization")
    print("=" * 70)
    
    numbers: List[int] = [2, 7, 11, 15]
    target: int = 9
    
    print(f"\nArray: {numbers}")
    print(f"Target: {target}")
    print("\n" + "-" * 70)
    
    result, trace = two_sum_with_trace(numbers, target)
    
    # Create visual array representation
    for step_info in trace:
        print(f"\nStep {step_info['step']}:")
        print(f"  left={step_info['left']} (value={step_info['left_val']}), "
              f"right={step_info['right']} (value={step_info['right_val']})")
        print(f"  sum = {step_info['left_val']} + {step_info['right_val']} = {step_info['sum']}")
        
        # Visual pointer display
        arr_display = []
        for i, val in enumerate(numbers):
            if i == step_info['left'] and i == step_info['right']:
                arr_display.append(f"[{val}]←LR")
            elif i == step_info['left']:
                arr_display.append(f"[{val}]←L")
            elif i == step_info['right']:
                arr_display.append(f"[{val}]←R")
            else:
                arr_display.append(f" {val} ")
        
        print(f"  Array: {' '.join(arr_display)}")
        
        if step_info['sum'] < target:
            print(f"  → {step_info['sum']} < {target}, need larger sum → move LEFT right")
        elif step_info['sum'] > target:
            print(f"  → {step_info['sum']} > {target}, need smaller sum → move RIGHT left")
        else:
            print(f"  → {step_info['sum']} == {target} → FOUND!")
    
    print(f"\n{'='*70}")
    print(f"RESULT: Indices {result} (1-indexed)")
    print(f"Values: {numbers[result[0]-1]} + {numbers[result[1]-1]} = {target}")
    print("=" * 70)


if __name__ == "__main__":
    # Test cases
    test_cases: List[Tuple[List[int], int, List[int]]] = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),  # 4 + 4 = 8
        ([5, 25, 75], 100, [2, 3]),
    ]
    
    print("=" * 60)
    print("Two Sum II - Test Cases")
    print("=" * 60)
    
    for nums, target, expected in test_cases:
        result = two_sum(nums.copy(), target)
        status = "✅" if result == expected else "❌"
        print(f"\n{status} numbers={nums}, target={target}")
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")
        if result == expected:
            print(f"   Explanation: {nums[result[0]-1]} + {nums[result[1]-1]} = {target}")
    
    # Run visualization
    print("\n")
    visualize_two_sum()