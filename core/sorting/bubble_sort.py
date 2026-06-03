"""
core/sorting/bubble_sort.py
Bubble Sort - O(n²) time, O(1) space
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort - Repeatedly swap adjacent elements if out of order.
    
    Time: O(n²) worst/average, O(n) best (already sorted)
    Space: O(1) - in-place
    """
    n = len(arr)
    arr = arr.copy()  # Don't modify original
    
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps, array is sorted
        if not swapped:
            break
    
    return arr


def bubble_sort_debug(arr: List[int]) -> List[int]:
    """Bubble Sort with debugging output."""
    n = len(arr)
    arr = arr.copy()
    
    print(f"Original: {arr}")
    
    for i in range(n):
        swapped = False
        print(f"\nPass {i + 1}:")
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                print(f"  Swap {arr[j]} and {arr[j + 1]}: {arr} → ", end="")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
                swapped = True
            else:
                print(f"  Keep {arr[j]} and {arr[j + 1]}: {arr}")
        
        if not swapped:
            print(f"  No swaps in pass {i + 1} - array sorted!")
            break
    
    return arr


if __name__ == "__main__":
    test_cases = [
        [5, 3, 8, 1],
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
    ]
    
    print("=" * 50)
    print("BUBBLE SORT")
    print("=" * 50)
    
    for arr in test_cases:
        print(f"\nOriginal: {arr}")
        sorted_arr = bubble_sort(arr)
        print(f"Sorted:   {sorted_arr}")
    
    print("\n--- Detailed Debug ---")
    bubble_sort_debug([5, 3, 8, 1])
    
    print("\n✅ Bubble sort complete!")
