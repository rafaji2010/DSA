"""
Experiment: Binary Search on Unsorted Data
Shows why sorting is REQUIRED for binary search to work.
"""

from binary_search import binary_search_iterative

def demonstrate_unsorted_problem():
    """Demonstrate why binary search fails on unsorted data."""
    
    # Unsorted array
    unsorted = [7, 3, 9, 1, 5, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]
    
    # Same values but sorted
    sorted_arr = sorted(unsorted)
    
    print("=" * 60)
    print("Binary Search Requires Sorted Data - Demonstration")
    print("=" * 60)
    
    print(f"\nUnsorted array: {unsorted}")
    print(f"Sorted array:   {sorted_arr}")
    print("\n" + "-" * 60)
    
    # Test with element that exists in both
    test_target = 5
    
    print(f"\nTest: Searching for {test_target}")
    print(f"Expected index in sorted array: {sorted_arr.index(test_target)}")
    
    # Try binary search on unsorted
    result_unsorted = binary_search_iterative(unsorted, test_target)
    result_sorted = binary_search_iterative(sorted_arr, test_target)
    
    print(f"\n🔴 Binary search on UNSORTED: index {result_unsorted}")
    print(f"🟢 Binary search on SORTED:   index {result_sorted}")
    
    if result_unsorted == -1:
        print(f"\n❌ FAILED: Binary search couldn't find {test_target} in unsorted array!")
        print(f"   But {test_target} IS in the array at index {unsorted.index(test_target)}")
    
    print("\n" + "-" * 60)
    
    # Test multiple targets
    test_targets = [1, 7, 14, 10, 3]
    
    print("\nMultiple Test Cases:")
    print("Target | In Unsorted? | Binary Search Result | Linear Search Result")
    print("-" * 60)
    
    for target in test_targets:
        binary_result = binary_search_iterative(unsorted, target)
        linear_result = unsorted.index(target) if target in unsorted else -1
        exists = "Yes" if target in unsorted else "No"
        
        status = "✓" if binary_result == linear_result else "✗"
        print(f"{target:6} | {exists:11} | {binary_result:19} | {linear_result:19} {status}")

if __name__ == "__main__":
    demonstrate_unsorted_problem()