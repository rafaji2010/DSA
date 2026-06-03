"""
benchmarks/binary_search_scale.py
Compare linear search O(n) vs binary search O(log n) at different scales

Shows why algorithms matter - the difference between 0.000001 seconds and 10 seconds!
"""

import time
import random
import math


def linear_search(arr, target):
    """O(n) - checks every element"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def binary_search(arr, target):
    """O(log n) - requires sorted array"""
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


def binary_search_recursive(arr, target, left=None, right=None):
    """Recursive version - O(log n) time, O(log n) space"""
    if left is None:
        left = 0
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def benchmark_search(search_func, arr, target, label, requires_sorted=False):
    """
    Time a search function and return elapsed time.
    
    Args:
        search_func: The function to benchmark
        arr: The array to search in
        target: The value to search for
        label: Label for printing
        requires_sorted: If True, ensures array is sorted first
    """
    # Create a copy to avoid modifying original
    arr_copy = arr.copy()
    
    # Sort if required (binary search needs sorted)
    if requires_sorted:
        arr_copy.sort()
    
    # Time the search
    start = time.perf_counter()
    result = search_func(arr_copy, target)
    elapsed = time.perf_counter() - start
    
    return elapsed, result


def format_time(seconds):
    """Format time in appropriate units"""
    if seconds < 1e-6:
        return f"{seconds * 1e9:.0f} ns"
    elif seconds < 1e-3:
        return f"{seconds * 1e6:.1f} μs"
    elif seconds < 1:
        return f"{seconds * 1000:.2f} ms"
    else:
        return f"{seconds:.3f} s"


print("=" * 70)
print("LINEAR SEARCH O(n) vs BINARY SEARCH O(log n)")
print("=" * 70)

# Different array sizes to test
sizes = [1000, 10000, 50000, 100000, 500000, 1000000]

print("\n" + "=" * 70)
print(f"{'Size':<12} {'Linear (O(n))':<20} {'Binary (O(log n))':<20} {'Ratio':<10}")
print("=" * 70)

# Store results for visualization
results = []

for size in sizes:
    # Create a sorted array of unique random numbers
    arr = random.sample(range(size * 10), size)
    
    # Pick a target that exists (middle element)
    arr_sorted = sorted(arr)
    target = arr_sorted[size // 2]
    
    # Benchmark linear search
    linear_time, linear_idx = benchmark_search(linear_search, arr, target, "Linear", requires_sorted=False)
    
    # Benchmark binary search (iterative)
    binary_time, binary_idx = benchmark_search(binary_search, arr, target, "Binary", requires_sorted=True)
    
    # Calculate ratio
    ratio = linear_time / binary_time if binary_time > 0 else 0
    
    results.append({
        'size': size,
        'linear_time': linear_time,
        'binary_time': binary_time,
        'ratio': ratio
    })
    
    print(f"{size:<12,} {format_time(linear_time):<20} {format_time(binary_time):<20} {ratio:<10.1f}x")

print("=" * 70)

# Calculate theoretical ratio
print("\n" + "=" * 70)
print("THEORETICAL COMPARISON")
print("=" * 70)
print("""
Linear Search (O(n)):     operations = n
Binary Search (O(log n)): operations = log₂(n)

Examples:
n = 1,000     → Binary is ~100x faster
n = 1,000,000 → Binary is ~50,000x faster  
n = 1,000,000,000 → Binary is ~33,000,000x faster
""")

# Create a dramatic demonstration
print("\n" + "=" * 70)
print("DRAMATIC DEMONSTRATION")
print("=" * 70)

# Very large array for demonstration (slower, so smaller size for demo)
demo_size = 500000
print(f"\nSearching through {demo_size:,} elements...")

demo_arr = random.sample(range(demo_size * 10), demo_size)
target = sorted(demo_arr)[demo_size // 2]

# Linear search time
start = time.perf_counter()
linear_search(demo_arr, target)
linear_time = time.perf_counter() - start

# Binary search time (requires sort)
demo_arr_sorted = sorted(demo_arr)
start = time.perf_counter()
binary_search(demo_arr_sorted, target)
binary_time = time.perf_counter() - start

print(f"\nLinear search (O(n)):   {format_time(linear_time)}")
print(f"Binary search (O(log n)): {format_time(binary_time)}")
print(f"\nBinary search was {linear_time/binary_time:.1f}x faster!")

# Visual comparison
print("\n" + "=" * 70)
print("VISUAL COMPARISON (operations)")
print("=" * 70)

max_size = 1000000
linear_ops = max_size
binary_ops = math.log2(max_size)

print(f"\nFor n = {max_size:,} elements:")
print(f"┌{'─' * 50}┐")
print(f"│ Linear Search:  ~{linear_ops:>10,} operations{' ' * (30 - len(str(linear_ops)))}│")
print(f"│ Binary Search:  ~{binary_ops:>10,.0f} operations{' ' * (30 - len(str(int(binary_ops))))}│")
print(f"└{'─' * 50}┘")
print(f"\nBinary search does {linear_ops / binary_ops:,.0f}x FEWER operations!")

# Benchmark recursive version
print("\n" + "=" * 70)
print("RECURSIVE BINARY SEARCH (additional test)")
print("=" * 70)

test_arr = list(range(10000))
target = 5000

# Iterative
start = time.perf_counter()
binary_search(test_arr, target)
iter_time = time.perf_counter() - start

# Recursive
start = time.perf_counter()
binary_search_recursive(test_arr, target)
rec_time = time.perf_counter() - start

print(f"Iterative binary search: {format_time(iter_time)}")
print(f"Recursive binary search: {format_time(rec_time)}")
print("(Recursive is slightly slower due to function call overhead)")

# Add this to see a text-based graph
print("\n" + "=" * 70)
print("SCALING VISUALIZATION")
print("=" * 70)

for size, linear_time, binary_time, ratio in [(r['size'], r['linear_time'], r['binary_time'], r['ratio']) for r in results]:
    bar_length = min(50, int(ratio / max(r['ratio'] for r in results) * 50))
    print(f"{size:>8,}: {'█' * bar_length} {ratio:.0f}x faster")


print("\n" + "=" * 70)
print("✅ BENCHMARK COMPLETE!")
print("=" * 70)
print("""
KEY TAKEAWAYS:
1. Binary search is DRAMATICALLY faster for large datasets
2. The difference grows as data size increases
3. For n=1,000,000: Binary search is ~50,000x faster than linear!
4. Algorithm choice matters MORE than hardware!
""")