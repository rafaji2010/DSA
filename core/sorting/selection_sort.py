"""
core/sorting/selection_sort.py
Selection Sort - O(n²) time, O(1) space
"""

from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    """
    Selection Sort - Find minimum and place at front.
    
    Time: O(n²) for all cases (best, average, worst)
    Space: O(1) - in-place
    """
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        # Find index of minimum element in remaining array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap found minimum with first element of unsorted part
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def selection_sort_debug(arr: List[int]) -> List[int]:
    """Selection Sort with debugging output."""
    n = len(arr)
    arr = arr.copy()
    
    print(f"Original: {arr}")
    
    for i in range(n):
        min_idx = i
        
        # Find minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap if needed
        if min_idx != i:
            print(f"  Swap arr[{i}]={arr[i]} with arr[{min_idx}]={arr[min_idx]}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"  → {arr}")
        else:
            print(f"  arr[{i}]={arr[i]} already in correct position")
    
    return arr


if __name__ == "__main__":
    test_cases = [
        [5, 3, 8, 1],
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]
    
    print("=" * 50)
    print("SELECTION SORT")
    print("=" * 50)
    
    for arr in test_cases:
        print(f"\nOriginal: {arr}")
        sorted_arr = selection_sort(arr)
        print(f"Sorted:   {sorted_arr}")
    
    print("\n--- Detailed Debug ---")
    selection_sort_debug([5, 3, 8, 1])
    
    print("\n✅ Selection sort complete!")
