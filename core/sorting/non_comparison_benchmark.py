"""
core/sorting/non_comparison_benchmark.py
Benchmark Counting Sort vs Radix Sort vs Timsort
"""

import time
import random
from counting_sort import counting_sort
from radix_sort import radix_sort


def benchmark():
    sizes = [1000, 5000, 10000, 50000]
    
    print("=" * 80)
    print(f"{'Size':<12} {'Counting Sort':<20} {'Radix Sort':<20} {'Timsort':<20}")
    print("=" * 80)
    
    for size in sizes:
        # Small range (0-100) - Counting Sort excels
        arr_small_range = [random.randint(0, 100) for _ in range(size)]
        
        # Counting Sort
        start = time.perf_counter()
        counting_sort(arr_small_range)
        counting_time = time.perf_counter() - start
        
        # Radix Sort
        start = time.perf_counter()
        radix_sort(arr_small_range)
        radix_time = time.perf_counter() - start
        
        # Timsort (Python's built-in)
        start = time.perf_counter()
        sorted(arr_small_range)
        timsort_time = time.perf_counter() - start
        
        print(f"{size:<12,} {counting_time:<20.4f} {radix_time:<20.4f} {timsort_time:<20.4f}")


if __name__ == "__main__":
    benchmark()
