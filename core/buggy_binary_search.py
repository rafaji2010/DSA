"""
Buggy Binary Search - Practice debugging with pdb
Your mission: Find and fix the bug using ONLY pdb (no print statements!)
"""

def buggy_binary_search(arr: list[int], target: int) -> int:
    """
    This version has a subtle bug. Use pdb to find it.
    
    The bug causes the function to fail on specific edge cases.
    """
    left, right = 0, len(arr)  # BUG 1: Should be len(arr) - 1
    
    while left < right:  # BUG 2: Should be <=
        mid = (left + right) // 2
        breakpoint()
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def fixed_binary_search(arr: list[int], target: int) -> int:
    """The corrected version - for comparison after debugging."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


if __name__ == "__main__":
    print("=" * 60)
    print("DEBUGGING CHALLENGE: Find the bug using pdb!")
    print("=" * 60)
    
    test_cases = [
        ([1, 2, 3, 4, 5], 1, "First element"),
        ([1, 2, 3, 4, 5], 3, "Middle element"),
        ([1, 2, 3, 4, 5], 5, "Last element"),  # ← THIS ONE FAILS!
        ([1, 2, 3, 4, 5], 6, "Element not present"),
        ([1], 1, "Single element - found"),
        ([1], 2, "Single element - not found"),
        ([], 5, "Empty array"),
    ]
    
    print("\nRunning buggy version:")
    print("-" * 40)
    
    for arr, target, description in test_cases:
        result = buggy_binary_search(arr, target)
        expected = arr.index(target) if target in arr else -1
        
        status = "✓" if result == expected else "✗"
        print(f"{status} {description:20} target={target}: got {result}, expected {expected}")
    
    print("\n" + "=" * 60)
    print("The last element test FAILED! Use pdb to find why.")
    print("=" * 60)
    
    # Add breakpoint for debugging - UNCOMMENT WHEN READY TO DEBUG
    # breakpoint()
    
    # Test the specific failing case
    print("\n" + "=" * 60)
    print("Testing fixed version (for comparison after debugging):")
    print("-" * 40)
    
    for arr, target, description in test_cases:
        result = fixed_binary_search(arr, target)
        expected = arr.index(target) if target in arr else -1
        status = "✓" if result == expected else "✗"
        print(f"{status} {description:20} target={target}: got {result}, expected {expected}")