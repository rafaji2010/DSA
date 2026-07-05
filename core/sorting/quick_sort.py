"""
core/sorting/quick_sort.py
Quick Sort implementation with multiple partition schemes
"""

from typing import List
import time
import random
import sys


def lomuto_partition(arr: List[int], low: int, high: int) -> int:
    """
    Lomuto partition scheme.
    
    Chooses the RIGHTMOST element as pivot.
    Returns the final index of the pivot.
    
    Visual: 
        arr = [3, 8, 2, 5, 1, 4, 7, 6]
        pivot = arr[high] = 6
        
        After partition:
        [3, 2, 5, 1, 4] 6 [8, 7]
        ↑                ↑   ↑
        < pivot         pivot > pivot
    """
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1        # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def lomuto_partition_trace(arr: List[int], low: int, high: int) -> int:
    """Partition with detailed tracing"""
    pivot = arr[high]
    print(f"  Pivot: {pivot} (index {high})")
    print(f"  Array before: {arr[low:high+1]}")
    
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"    Swapped {arr[i]} and {arr[j]}: {arr[low:high+1]}")
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"  Final pivot position: {i+1}")
    print(f"  Array after: {arr[low:high+1]}")
    print(f"  Result: [{arr[low]}] < {pivot} < [{arr[i+2] if i+2 <= high else 'None'}]")
    
    return i + 1

def quick_sort_lomuto(arr: List[int], low: int, high: int) -> None:
    """
    Quick Sort using Lomuto partition scheme.
    
    Time: O(n log n) average, O(n²) worst case
    Space: O(log n) for recursion stack
    """
    if low < high:
        # Partition and get pivot index
        pi = lomuto_partition(arr, low, high)
        
        # Recursively sort left and right subarrays
        quick_sort_lomuto(arr, low, pi - 1)
        quick_sort_lomuto(arr, pi + 1, high)


def quick_sort_hoare(arr: List[int], low: int, high: int) -> None:
    """
    Quick Sort using Hoare partition scheme (more efficient).
    
    Hoare's partition uses two pointers moving toward each other.
    """
    if low < high:
        pi = hoare_partition(arr, low, high)
        quick_sort_hoare(arr, low, pi)
        quick_sort_hoare(arr, pi + 1, high)


def hoare_partition(arr: List[int], low: int, high: int) -> int:
    """
    Hoare partition scheme.
    
    Uses LEFTmost element as pivot.
    More efficient than Lomuto (fewer swaps).
    """
    pivot = arr[low]
    i = low - 1
    j = high + 1
    
    while True:
        # Find element greater than pivot
        i += 1
        while arr[i] < pivot:
            i += 1
        
        # Find element smaller than pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        # Swap
        arr[i], arr[j] = arr[j], arr[i]


def choose_pivot_random(arr: List[int], low: int, high: int) -> int:
    """Random pivot selection - avoids worst case O(n²)"""
    random_index = random.randint(low, high)
    arr[low], arr[random_index] = arr[random_index], arr[low]
    return arr[low]


def choose_pivot_median(arr: List[int], low: int, high: int) -> int:
    """
    Median-of-three pivot selection.
    Picks median of first, middle, and last elements.
    """
    mid = (low + high) // 2
    
    # Sort the three candidates
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    
    # Place median at low position (for Hoare partition)
    arr[low], arr[mid] = arr[mid], arr[low]
    return arr[low]


def quick_sort_median(arr: List[int], low: int, high: int) -> None:
    """Quick Sort with median-of-three pivot for better performance"""
    if low < high:
        # Choose pivot using median-of-three
        choose_pivot_median(arr, low, high)
        
        pi = hoare_partition(arr, low, high)
        quick_sort_median(arr, low, pi)
        quick_sort_median(arr, pi + 1, high)



sys.setrecursionlimit(10000)


def benchmark_quick_sort():
    """Compare different Quick Sort implementations"""
    sizes = [100, 500, 1000, 2000, 5000]
    
    print("=" * 80)
    print("QUICK SORT PERFORMANCE BENCHMARK")
    print("=" * 80)
    print(f"{'Size':<10} {'Lomuto (s)':<15} {'Hoare (s)':<15} {'Median (s)':<15}")
    print("-" * 80)
    
    for size in sizes:
        # Create random array
        arr = [random.randint(0, size * 10) for _ in range(size)]
        
        # Lomuto
        arr1 = arr.copy()
        start = time.perf_counter()
        quick_sort_lomuto(arr1, 0, len(arr1) - 1)
        lomuto_time = time.perf_counter() - start
        
        # Hoare
        arr2 = arr.copy()
        start = time.perf_counter()
        quick_sort_hoare(arr2, 0, len(arr2) - 1)
        hoare_time = time.perf_counter() - start
        
        # Median-of-three
        arr3 = arr.copy()
        start = time.perf_counter()
        quick_sort_median(arr3, 0, len(arr3) - 1)
        median_time = time.perf_counter() - start
        
        print(f"{size:<10,} {lomuto_time:<15.4f} {hoare_time:<15.4f} {median_time:<15.4f}")


def worst_case_demonstration():
    """Demonstrate worst-case O(n²) behavior"""
    print("\n" + "=" * 80)
    print("WORST CASE DEMONSTRATION (Sorted array, Lomuto)")
    print("=" * 80)
    
    # Lomuto with worst-case (already sorted, pivot at end)
    arr_sorted = list(range(1000))
    start = time.perf_counter()
    quick_sort_lomuto(arr_sorted.copy(), 0, 999)
    lomuto_time = time.perf_counter() - start
    print(f"Lomuto on sorted array: {lomuto_time:.4f}s")
    
    # Random pivot (should be much faster on sorted)
    def quick_sort_random(arr, low, high):
        if low < high:
            choose_pivot_random(arr, low, high)
            pi = hoare_partition(arr, low, high)
            quick_sort_random(arr, low, pi)
            quick_sort_random(arr, pi + 1, high)
    
    arr_sorted2 = list(range(1000))
    start = time.perf_counter()
    quick_sort_random(arr_sorted2, 0, 999)
    random_time = time.perf_counter() - start
    print(f"Random pivot on sorted array: {random_time:.4f}s")
    print(f"Random pivot is {lomuto_time/random_time:.1f}x faster!")

if __name__ == "__main__":
    print("=" * 60)
    print("QUICK SORT DEMONSTRATION")
    print("=" * 60)
    
    # Test array
    arr = [8, 3, 9, 1, 5, 7, 2, 6, 4]
    print(f"\nOriginal array: {arr}")
    
    # Lomuto Quick Sort
    arr1 = arr.copy()
    print(f"\n--- Lomuto Quick Sort ---")
    print(f"Before: {arr1}")
    quick_sort_lomuto(arr1, 0, len(arr1) - 1)
    print(f"After:  {arr1}")
    
    # Hoare Quick Sort
    arr2 = arr.copy()
    print(f"\n--- Hoare Quick Sort ---")
    print(f"Before: {arr2}")
    quick_sort_hoare(arr2, 0, len(arr2) - 1)
    print(f"After:  {arr2}")
    
    # With trace
    print(f"\n--- Detailed Partition Trace ---")
    arr3 = [3, 8, 2, 5, 1, 4, 7, 6]
    print(f"Original: {arr3}")
    lomuto_partition_trace(arr3, 0, len(arr3) - 1)
    
    # Performance benchmark
    benchmark_quick_sort()
    
    # Worst-case demonstration
    worst_case_demonstration()
    
    print("\n" + "=" * 60)
    print("QUICK SORT VS MERGE SORT")
    print("=" * 60)
    print("""
    ┌─────────────────────────────────────────────────────────────────────┐
    │                    Quick Sort           Merge Sort                  │
    ├─────────────────────────────────────────────────────────────────────┤
    │ Time (avg)         O(n log n)           O(n log n)                  │
    │ Time (worst)       O(n²)                O(n log n)                  │
    │ Space              O(log n)             O(n)                        │
    │ In-place?          Yes ✅               No                          │
    │ Stable?            No                   Yes ✅                      │
    │ Cache friendly     Yes ✅               Less                        │
    │ Adaptive?          No                   No                          │
    └─────────────────────────────────────────────────────────────────────┘
    
    Use Quick Sort when:
    - In-place sorting is required
    - Good average performance is enough
    - Extra memory is limited
    
    Use Merge Sort when:
    - Guaranteed O(n log n) is required
    - Stable sort is needed
    - Linked lists (random access expensive)
    """)