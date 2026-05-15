"""
benchmarks/array_operations_timing.py
Time various array operations to verify Big O complexity.
"""

import time
import random


def time_operation(operation, *args, iterations=100000):
    """Time an operation by running it many times."""
    start = time.perf_counter()
    for _ in range(iterations):
        operation(*args)
    return time.perf_counter() - start


if __name__ == "__main__":
    print("=" * 60)
    print("ARRAY OPERATIONS TIMING (Big O Verification)")
    print("=" * 60)
    
    sizes = [1000, 10000, 100000]
    
    print("\n--- Access by Index (O(1)) ---")
    for size in sizes:
        arr = list(range(size))
        idx = size // 2
        
        start = time.perf_counter()
        for _ in range(100000):
            val = arr[idx]  # Direct index access
        elapsed = time.perf_counter() - start
        
        print(f"Size {size:6d}: {elapsed:.4f}s (should stay constant)")
    
    print("\n--- Append (O(1) amortized) ---")
    for size in sizes:
        arr = list(range(size))
        
        start = time.perf_counter()
        for i in range(10000):
            arr.append(i)
        elapsed = time.perf_counter() - start
        
        print(f"Size {size:6d}: {elapsed:.4f}s (should grow slowly)")
    
    print("\n--- Insert at Beginning (O(n)) ---")
    for size in sizes:
        arr = list(range(size))
        
        start = time.perf_counter()
        for i in range(1000):
            arr.insert(0, i)
        elapsed = time.perf_counter() - start
        
        print(f"Size {size:6d}: {elapsed:.4f}s (should grow with n)")
    
    print("\n--- Search for Value (O(n)) ---")
    for size in sizes:
        arr = list(range(size))
        target = size - 1  # Worst case - at the end
        
        start = time.perf_counter()
        for _ in range(1000):
            found = target in arr
        elapsed = time.perf_counter() - start
        
        print(f"Size {size:6d}: {elapsed:.4f}s (should grow with n)")
    
    print("\n" + "=" * 60)
    print("CONCLUSION:")
    print("- Access by index: O(1) - constant time regardless of size")
    print("- Append: O(1) amortized - small constant factor")
    print("- Insert at front: O(n) - time grows linearly with size")
    print("- Search: O(n) - time grows linearly with size")
    print("=" * 60)