# core/pdb_debug_examples/debug_first_occurrence.py
"""Debug first occurrence binary search with pdb."""

import pdb
from typing import List


def find_first_with_debug(arr: List[int], target: int) -> int:
    """
    Find first occurrence with pdb breakpoints to trace execution.
    """
    left, right = 0, len(arr) - 1
    result = -1
    iteration = 0
    
    while left <= right:
        iteration += 1
        mid = (left + right) // 2
        
        print(f"\n--- Iteration {iteration} ---")
        print(f"left={left}, right={right}, mid={mid}")
        print(f"arr[mid]={arr[mid]}, target={target}")
        
        # Set breakpoint when we find a match
        if arr[mid] == target:
            print(f">>> FOUND at index {mid}!")
            breakpoint()  # pdb stops here - examine state
        
        if arr[mid] == target:
            result = mid
            right = mid - 1
            print(f">>> Storing result={result}, moving right to {right}")
        elif arr[mid] < target:
            left = mid + 1
            print(f">>> Moving left to {left}")
        else:  # arr[mid] > target
            right = mid - 1
            print(f">>> Moving right to {right}")
    
    print(f"\nFinal result: {result}")
    return result


if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4, 5, 5, 6]
    target = 2
    
    print(f"Array: {arr}")
    print(f"Searching for first occurrence of {target}")
    print("=" * 50)
    
    # Run with pdb
    result = find_first_with_debug(arr, target)
    
    print("=" * 50)
    print(f"✅ FIRST occurrence of {target} is at index {result}")