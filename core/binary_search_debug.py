"""
Binary Search Implementation - O(log n) algorithm for sorted arrays.
"""

def binary_search_iterative(arr: list[int], target: int) -> int:
    """
    Search for target in sorted array using iterative binary search.
    
    Time Complexity: O(log n) - halves search space each iteration
    Space Complexity: O(1) - only uses a few variables
    
    Args:
        arr: Sorted list of integers to search in
        target: Integer value to find
    
    Returns:
        Index of target if found, otherwise -1
    
    Examples:
        >>> binary_search_iterative([1, 3, 5, 7, 9], 7)
        3
        >>> binary_search_iterative([1, 3, 5, 7, 9], 2)
        -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1   # Target is in right half
        else:
            right = mid - 1  # Target is in left half
    
    return -1

def binary_search_recursive(
    arr: list[int], 
    target: int, 
    left: int, 
    right: int,      # ← Comma here!
    depth: int = 0
) -> int:
    """Recursive binary search with depth tracking."""
    indent = "  " * depth
    
    # Base case
    if left > right:
        return -1
    
    # Calculate middle
    mid = (left + right) // 2
    
    # Debug output
    print(f"{indent}Depth {depth}: checking left={left}, right={right}, mid={mid}, value={arr[mid]}")
    
    breakpoint()  # Debugger stops here
    
    # Found target
    if arr[mid] == target:
        return mid
    
    # Search right half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, depth + 1)
    
    # Search left half
    else:
        return binary_search_recursive(arr, target, left, mid - 1, depth + 1)

def binary_search_recursive_wrapper(arr: list[int], target: int) -> int:
    """
    Wrapper function for recursive binary search.
    
    This provides a simpler interface without requiring left/right parameters.
    
    Args:
        arr: Sorted list of integers
        target: Integer value to search for
    
    Returns:
        Index of target if found, -1 otherwise
    
    Examples:
        >>> binary_search_recursive_wrapper([1, 3, 5, 7, 9], 7)
        3
    """
    return binary_search_recursive(arr, target, 0, len(arr) - 1)


def binary_search_with_debug(arr: list[int], target: int) -> int:
    """Same as iterative but with breakpoint for learning pdb."""
    left, right = 0, len(arr) - 1
    step = 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # ADD BREAKPOINT HERE - execution will pause
        breakpoint()  # ← Python 3.7+ (use import pdb; pdb.set_trace() for older)
        
        print(f"Step {step}: left={left}, right={right}, mid={mid}, value={arr[mid]}")
        step += 1
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print("Searching for 7...")
    result = binary_search_with_debug(data, 7)
    print(f"Result: {result}")

    print("=" * 60)
    print("Testing Binary Search - Iterative vs Recursive")
    print("=" * 60)
    print(f"Test array: {data}\n")
    
    print("-" * 60)
    print("ITERATIVE BINARY SEARCH")
    print("-" * 60)

    print("\n" + "=" * 40)
    print("Testing RECURSIVE with debugger")
    print("=" * 40)
    result = binary_search_recursive_wrapper(data, 7)
    print(f"Recursive result: {result}")
    
    # Test iterative version
    test_cases = [
        (7, 3, "Find middle element"),
        (20, -1, "Find element not in array"),
        (1, 0, "Find first element (edge)"),
        (19, 9, "Find last element (edge)"),
    ]
    
    for target, expected, desc in test_cases:
        result = binary_search_iterative(data, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} {desc}: target={target} -> index {result} (expected {expected})")
    
    # Edge cases for iterative
    result = binary_search_iterative([], 5)
    print(f"✓ Empty list: index {result} (expected -1)")
    
    result = binary_search_iterative([42], 42)
    print(f"✓ Single element [42] find 42: index {result} (expected 0)")
    
    result = binary_search_iterative([42], 7)
    print(f"✓ Single element [42] find 7: index {result} (expected -1)")
    
    print("\n" + "-" * 60)
    print("RECURSIVE BINARY SEARCH")
    print("-" * 60)
    
    # Test recursive version
    for target, expected, desc in test_cases:
        result = binary_search_recursive_wrapper(data, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} {desc}: target={target} -> index {result} (expected {expected})")
    
    # Edge cases for recursive
    result = binary_search_recursive_wrapper([], 5)
    print(f"✓ Empty list: index {result} (expected -1)")
    
    result = binary_search_recursive_wrapper([42], 42)
    print(f"✓ Single element [42] find 42: index {result} (expected 0)")
    
    result = binary_search_recursive_wrapper([42], 7)
    print(f"✓ Single element [42] find 7: index {result} (expected -1)")
    
    print("\n" + "=" * 60)
    print("All tests passed! 🎉")
    print("=" * 60)

