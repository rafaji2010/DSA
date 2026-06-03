"""
core/sorting/compare_sorts.py
Compare Bubble, Selection, and Insertion Sort
"""

import time
import random
from typing import List, Callable
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort


def benchmark(sort_func: Callable, arr: List[int], name: str) -> float:
    """Time a sorting function."""
    start = time.perf_counter()
    sort_func(arr)
    elapsed = time.perf_counter() - start
    return elapsed


def analyze_performance():
    """Compare performance on different input types."""
    sizes = [100, 500, 1000, 2000]
    
    print("=" * 70)
    print("O(n²) SORTING ALGORITHMS COMPARISON")
    print("=" * 70)
    
    for size in sizes:
        print(f"\n{'=' * 70}")
        print(f"ARRAY SIZE: {size}")
        print(f"{'=' * 70}")
        
        # Random array
        random_arr = [random.randint(0, size) for _ in range(size)]
        
        # Already sorted array
        sorted_arr = list(range(size))
        
        # Reverse sorted array
        reverse_arr = list(range(size, 0, -1))
        
        # Nearly sorted array (10 swaps)
        nearly_sorted = list(range(size))
        for _ in range(10):
            i, j = random.sample(range(size), 2)
            nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]
        
        for data_type, arr in [
            ("Random", random_arr),
            ("Already Sorted", sorted_arr),
            ("Reverse Sorted", reverse_arr),
            ("Nearly Sorted (10 swaps)", nearly_sorted),
        ]:
            print(f"\n  {data_type}:")
            
            # Test each sort
            for sort_func, name in [
                (bubble_sort, "Bubble"),
                (selection_sort, "Selection"),
                (insertion_sort, "Insertion"),
            ]:
                arr_copy = arr.copy()
                time_taken = benchmark(sort_func, arr_copy, name)
                print(f"    {name:12s}: {time_taken:.6f}s")


if __name__ == "__main__":
    analyze_performance()
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("""
    ┌─────────────────────────────────────────────────────────────────────┐
    │                    Bubble      Selection    Insertion               │
    ├─────────────────────────────────────────────────────────────────────┤
    │ Best Case          O(n)        O(n²)        O(n)                    │
    │ Average Case       O(n²)       O(n²)        O(n²)                   │
    │ Worst Case         O(n²)       O(n²)        O(n²)                   │
    │ Space              O(1)        O(1)         O(1)                    │
    │ Stable?            Yes         No           Yes                     │
    │ Adaptive?          Yes         No           Yes                     │
    │ Online?            No          No           Yes                     │
    └─────────────────────────────────────────────────────────────────────┘
    
    Online: Can sort as elements arrive (insertion sort can!)
    Adaptive: Fast on nearly-sorted data
    Stable: Preserves relative order of equal elements
    """)
