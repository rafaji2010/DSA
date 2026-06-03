"""
core/sorting/insertion_sort.py
Insertion Sort - O(n²) time, O(1) space, adaptive
"""

from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion Sort - Build sorted array by inserting elements in correct position.
    
    Time: O(n²) worst, O(n) best (already sorted)
    Space: O(1) - in-place
    Adaptive: Yes - fast on nearly-sorted data
    Stable: Yes
    """
    n = len(arr)
    arr = arr.copy()
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place key in correct position
        arr[j + 1] = key
    
    return arr


def insertion_sort_debug(arr: List[int]) -> List[int]:
    """Insertion Sort with debugging output."""
    n = len(arr)
    arr = arr.copy()
    
    print(f"Original: {arr}")
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        print(f"\nInsert element {key} (index {i}):")
        
        while j >= 0 and arr[j] > key:
            print(f"  Shift {arr[j]} right (index {j} → {j + 1})")
            arr[j + 1] = arr[j]
            j -= 1
            print(f"  Array: {arr}")
        
        arr[j + 1] = key
        print(f"  Place {key} at index {j + 1}")
        print(f"  Array: {arr}")
    
    return arr


if __name__ == "__main__":
    test_cases = [
        [5, 3, 8, 1],
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],  # Best case
        [5, 4, 3, 2, 1],  # Worst case
    ]
    
    print("=" * 50)
    print("INSERTION SORT")
    print("=" * 50)
    
    for arr in test_cases:
        print(f"\nOriginal: {arr}")
        sorted_arr = insertion_sort(arr)
        print(f"Sorted:   {sorted_arr}")
    
    print("\n--- Detailed Debug ---")
    insertion_sort_debug([5, 3, 8, 1])
    
    print("\n✅ Insertion sort complete!")
