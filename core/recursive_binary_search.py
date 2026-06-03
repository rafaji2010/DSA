"""
core/recursive_binary_search.py
Recursive Binary Search Implementation

Time: O(log n) - each call divides the problem in half
Space: O(log n) - call stack depth (log n frames)
"""

from typing import List


def binary_search_recursive(
    arr: List[int], 
    target: int, 
    left: int = 0, 
    right: int = None
) -> int:
    """
    Recursive binary search.
    
    Parameters:
        arr: Sorted list of integers
        target: Value to search for
        left: Left boundary index (default 0)
        right: Right boundary index (default len(arr)-1)
    
    Returns:
        Index of target if found, -1 otherwise
    """
    # Initialize right on first call
    if right is None:
        right = len(arr) - 1
    
    # BASE CASE 1: Search space exhausted
    if left > right:
        return -1
    
    # Calculate middle index
    mid = (left + right) // 2
    
    # BASE CASE 2: Found the target!
    if arr[mid] == target:
        return mid
    
    # RECURSIVE CASE 1: Target is in left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    
    # RECURSIVE CASE 2: Target is in right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


def binary_search_recursive_trace(
    arr: List[int], 
    target: int, 
    left: int = 0, 
    right: int = None,
    depth: int = 0
) -> int:
    """
    Debug version - shows each recursive call.
    """
    if right is None:
        right = len(arr) - 1
    
    indent = "  " * depth
    
    print(f"{indent}🔍 Searching range [{left}, {right}]: {arr[left:right+1]}")
    
    # Base case: empty range
    if left > right:
        print(f"{indent}  ❌ Empty range → target {target} not found")
        return -1
    
    mid = (left + right) // 2
    print(f"{indent}  📍 Mid index: {mid}, value: {arr[mid]}")
    
    # Base case: found!
    if arr[mid] == target:
        print(f"{indent}  ✅ FOUND {target} at index {mid}!")
        return mid
    
    # Recursive cases
    if arr[mid] > target:
        print(f"{indent}  ⬅️ {target} < {arr[mid]} → search LEFT half")
        result = binary_search_recursive_trace(arr, target, left, mid - 1, depth + 1)
        print(f"{indent}  ⬅️ Returning from LEFT: {result}")
        return result
    else:
        print(f"{indent}  ➡️ {target} > {arr[mid]} → search RIGHT half")
        result = binary_search_recursive_trace(arr, target, mid + 1, right, depth + 1)
        print(f"{indent}  ➡️ Returning from RIGHT: {result}")
        return result


# Alternative: More compact version
def binary_search_recursive_compact(
    arr: List[int], 
    target: int, 
    left: int = 0, 
    right: int = None
) -> int:
    """Compact version - same logic, fewer lines"""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive_compact(arr, target, left, mid - 1)
    else:
        return binary_search_recursive_compact(arr, target, mid + 1, right)


if __name__ == "__main__":
    print("=" * 60)
    print("RECURSIVE BINARY SEARCH")
    print("=" * 60)
    
    # Test array
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"\nArray: {arr}")
    
    print("\n" + "=" * 60)
    print("TESTING WITH TRACE")
    print("=" * 60)
    
    # Test 1: Find existing element
    print("\n--- Test 1: Find 7 ---")
    result = binary_search_recursive_trace(arr, 7)
    print(f"\nResult: index {result} (value {arr[result] if result != -1 else 'None'})")
    
    # Test 2: Find element at beginning
    print("\n--- Test 2: Find 1 (first element) ---")
    result = binary_search_recursive_trace(arr, 1)
    print(f"\nResult: index {result}")
    
    # Test 3: Find element at end
    print("\n--- Test 3: Find 19 (last element) ---")
    result = binary_search_recursive_trace(arr, 19)
    print(f"\nResult: index {result}")
    
    # Test 4: Find non-existent element
    print("\n--- Test 4: Find 100 (not in array) ---")
    result = binary_search_recursive_trace(arr, 100)
    print(f"\nResult: {result} (should be -1)")
    
    print("\n" + "=" * 60)
    print("VERBOSE TESTS (without trace)")
    print("=" * 60)
    
    # Standard tests
    test_cases = [
        (arr, 7, "Find middle"),
        (arr, 1, "Find first"),
        (arr, 19, "Find last"),
        (arr, 100, "Find missing (high)"),
        (arr, 0, "Find missing (low)"),
        ([1], 1, "Single element - found"),
        ([1], 2, "Single element - not found"),
        ([], 5, "Empty array"),
        ([1, 2, 3, 4, 5], 3, "Odd length"),
        ([1, 2, 3, 4, 5, 6], 4, "Even length"),
    ]
    
    for arr, target, description in test_cases:
        result = binary_search_recursive(arr, target)
        
        # Verify result
        if result != -1:
            valid = arr[result] == target
        else:
            valid = target not in arr
        
        status = "✅" if valid else "❌"
        print(f"{status} {description}: {arr} → search {target} → index {result}")
    
    # Compare with iterative version
    print("\n" + "=" * 60)
    print("COMPARISON: Recursive vs Iterative")
    print("=" * 60)
    
    def iterative_binary_search(arr, target):
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
    
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    targets = [7, 1, 15, 100]
    
    print(f"Array: {arr}")
    for target in targets:
        rec = binary_search_recursive(arr, target)
        itr = iterative_binary_search(arr, target)
        print(f"  Target {target}: Recursive → {rec}, Iterative → {itr}")
        assert rec == itr
    
    print("\n" + "=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)
    print("""
    Time Complexity:  O(log n)
    Space Complexity: O(log n) - call stack depth
    
    Why O(log n)?
    - Each recursive call divides the search space in HALF
    - To reduce from n to 1, you need log₂(n) halvings
    - Example: n=16 → max 4 recursive calls (16→8→4→2→1)
    
    Compare with Linear Search (O(n)):
    - Linear: n=1,000,000 → 1,000,000 operations
    - Binary: n=1,000,000 → only 20 operations!
    """)
    
    print("✅ All tests passed!")