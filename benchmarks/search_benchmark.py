"""
Benchmark comparing Linear Search O(n) vs Binary Search O(log n)
"""

import time
import random
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.binary_search import binary_search_iterative


def linear_search(arr: list[int], target: int) -> int:
    """
    Linear search - O(n) time complexity.
    Checks every element one by one.
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def binary_search(arr: list[int], target: int) -> int:
    """Binary search - O(log n) time complexity."""
    return binary_search_iterative(arr, target)


def run_benchmark(size: int):
    """Run benchmark for a specific array size."""
    
    print(f"\n{'='*60}")
    print(f"Benchmark with n = {size:,} elements")
    print(f"{'='*60}")
    
    # Generate sorted array of random integers
    print(f"Generating {size:,} random integers...")
    data = sorted([random.randint(0, size * 10) for _ in range(size)])
    
    # Pick a target that exists (middle element)
    target = data[size // 2]
    print(f"Searching for target: {target} (exists at index {size // 2})")
    
    print("\nRunning benchmarks...")
    print("-" * 40)
    
    # Benchmark Linear Search
    start = time.perf_counter()
    linear_result = linear_search(data, target)
    linear_time = time.perf_counter() - start
    
    # Benchmark Binary Search
    start = time.perf_counter()
    binary_result = binary_search(data, target)
    binary_time = time.perf_counter() - start
    
    # Results
    print(f"\n📊 RESULTS:")
    print(f"  Linear Search:  {linear_time:.6f} seconds")
    print(f"  Binary Search:  {binary_time:.6f} seconds")
    
    if binary_time > 0:
        speedup = linear_time / binary_time
        print(f"\n  🚀 Binary search is {speedup:.0f}x faster!")
    
    # Verify both found the correct index
    assert linear_result == size // 2, f"Linear search failed! Got {linear_result}"
    assert binary_result == size // 2, f"Binary search failed! Got {binary_result}"
    
    return linear_time, binary_time


def benchmark_worst_case(size: int):
    """Benchmark worst-case scenario (target not in array)."""
    
    print(f"\n{'='*60}")
    print(f"Worst Case - Target NOT in array (n = {size:,})")
    print(f"{'='*60}")
    
    # Generate sorted array
    data = sorted([random.randint(0, size * 10) for _ in range(size)])
    target = -1  # Target that doesn't exist
    
    print(f"Searching for target: {target} (not in array)")
    print("-" * 40)
    
    # Benchmark Linear Search
    start = time.perf_counter()
    linear_result = linear_search(data, target)
    linear_time = time.perf_counter() - start
    
    # Benchmark Binary Search
    start = time.perf_counter()
    binary_result = binary_search(data, target)
    binary_time = time.perf_counter() - start
    
    print(f"\n📊 RESULTS (worst case):")
    print(f"  Linear Search:  {linear_time:.6f} seconds")
    print(f"  Binary Search:  {binary_time:.6f} seconds")
    
    if binary_time > 0:
        speedup = linear_time / binary_time
        print(f"\n  🚀 Binary search is {speedup:.0f}x faster!")
    
    assert linear_result == -1, "Linear search should return -1"
    assert binary_result == -1, "Binary search should return -1"
    
    return linear_time, binary_time


if __name__ == "__main__":
    print("="*60)
    print("LINEAR SEARCH O(n) vs BINARY SEARCH O(log n)")
    print("="*60)
    print("\nThis benchmark shows the REAL performance difference!")
    print("Watch how binary search stays fast even as data grows.\n")
    
    # Test with different sizes
    sizes = [10_000, 100_000, 1_000_000]
    
    results = []
    for size in sizes:
        linear_time, binary_time = run_benchmark(size)
        results.append((size, linear_time, binary_time))
        
        # Small pause between benchmarks
        time.sleep(1)
    
    # Worst case benchmark
    worst_linear, worst_binary = benchmark_worst_case(1_000_000)
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY: How Performance Scales")
    print("="*60)
    print("\nSize     | Linear (s) | Binary (s) | Speedup")
    print("-"*50)
    for size, linear_t, binary_t in results:
        speedup = linear_t / binary_t if binary_t > 0 else 0
        print(f"{size:8,} | {linear_t:.6f} | {binary_t:.6f} | {speedup:,.0f}x")
    
    print("\n" + "="*60)
    print("KEY INSIGHTS:")
    print("="*60)
    print("• Binary search time stays tiny even as data grows")
    print("• Linear search time grows PROPORTIONALLY with data size")
    print(f"• For 1,000,000 elements: Binary search is ~{results[-1][2]:.0f} seconds")
    print("• The O(log n) vs O(n) difference is MASSIVE in practice!")
    print("="*60)