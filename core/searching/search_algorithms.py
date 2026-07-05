import math

def linear_search(arr: list, target: int) -> int:
    """O(n) - check each element one by one"""
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1


def jump_search(arr: list, target: int) -> int:
    """
    Jump Search - O(√n) time, O(1) space
    
    Algorithm:
    1. Jump ahead by √n steps
    2. If current value < target, continue jumping
    3. If current value > target, linear search in previous block
    """
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal jump size
    prev = 0
    
    # Jumping phase: find block containing target
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search phase: search within the block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    
    return -1


def jump_search_trace(arr: list, target: int) -> int:
    """Jump Search with trace visualization"""
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Jump size: {step}")
    print("-" * 40)
    
    # Jumping phase
    jump_num = 1
    while prev < n and arr[min(step, n) - 1] < target:
        print(f"Jump {jump_num}: arr[{min(step, n)-1}] = {arr[min(step, n)-1]} < {target}")
        prev = step
        step += int(math.sqrt(n))
        jump_num += 1
        if prev >= n:
            print(f"  → Reached end, target not found")
            return -1
    
    print(f"Found block: indices [{prev}, {min(step, n)-1}]")
    print(f"Starting linear search...")
    
    # Linear search phase
    for i in range(prev, min(step, n)):
        print(f"  Checking index {i}: arr[{i}] = {arr[i]}")
        if arr[i] == target:
            print(f"  ✓ FOUND at index {i}!")
            return i
    
    print(f"  ✗ Target not found in block")
    return -1

def exponential_search(arr: list, target: int) -> int:
    """
    Exponential Search - O(log n) time, O(1) space
    
    Best for: Infinite or very large sorted arrays
    Algorithm:
    1. Find range where target might be (doubling)
    2. Binary search in that range
    """
    if not arr:
        return -1
    
    n = len(arr)
    
    # If target is first element
    if arr[0] == target:
        return 0
    
    # Find range for binary search
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    
    # Binary search in the range [i//2, min(i, n-1)]
    left = i // 2
    right = min(i, n - 1)
    
    return binary_search_range(arr, target, left, right)


def binary_search_range(arr: list, target: int, left: int, right: int) -> int:
    """Binary search within specific range"""
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def exponential_search_trace(arr: list, target: int) -> int:
    """Exponential Search with trace visualization"""
    if not arr:
        return -1
    
    n = len(arr)
    print(f"Array length: {n}")
    print(f"Target: {target}")
    print("-" * 40)
    
    if arr[0] == target:
        print(f"Target at index 0!")
        return 0
    
    # Find range
    i = 1
    print("Finding range:")
    while i < n and arr[i] <= target:
        print(f"  arr[{i}] = {arr[i]} ≤ {target} → double i to {i*2}")
        i *= 2
    
    left = i // 2
    right = min(i, n - 1)
    print(f"\nBinary search range: [{left}, {right}]")
    
    return binary_search_range_trace(arr, target, left, right)


def binary_search_range_trace(arr: list, target: int, left: int, right: int) -> int:
    """Binary search with trace"""
    print(f"\nBinary search in arr[{left}:{right+1}] = {arr[left:right+1]}")
    
    step = 1
    while left <= right:
        mid = (left + right) // 2
        print(f"  Step {step}: mid={mid}, arr[{mid}]={arr[mid]}")
        
        if arr[mid] == target:
            print(f"  ✓ FOUND at index {mid}!")
            return mid
        elif arr[mid] < target:
            print(f"    {target} > {arr[mid]} → search RIGHT half")
            left = mid + 1
        else:
            print(f"    {target} < {arr[mid]} → search LEFT half")
            right = mid - 1
        step += 1
    
    print(f"  ✗ Target not found")
    return -1

import time
import random

def benchmark_searches():
    """Compare all searching algorithms"""
    sizes = [1000, 10000, 100000, 1000000]
    
    print("=" * 80)
    print(f"{'Size':<12} {'Linear':<15} {'Binary':<15} {'Jump':<15} {'Exponential':<15}")
    print("=" * 80)
    
    for size in sizes:
        # Create sorted array
        arr = list(range(size))
        target = size - 1  # Worst case (last element)
        
        # Linear Search
        start = time.perf_counter()
        linear_search(arr, target)
        linear_time = time.perf_counter() - start
        
        # Binary Search (using built-in for fair comparison)
        start = time.perf_counter()
        binary_search_range(arr, target, 0, size - 1)
        binary_time = time.perf_counter() - start
        
        # Jump Search
        start = time.perf_counter()
        jump_search(arr, target)
        jump_time = time.perf_counter() - start
        
        # Exponential Search
        start = time.perf_counter()
        exponential_search(arr, target)
        exp_time = time.perf_counter() - start
        
        print(f"{size:<12,} {linear_time:<15.6f} {binary_time:<15.6f} {jump_time:<15.6f} {exp_time:<15.6f}")

if __name__ == "__main__":
    # Test array
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    
    print("=" * 60)
    print("SEARCHING ALGORITHMS DEMONSTRATION")
    print("=" * 60)
    print(f"\nArray: {arr}")
    
    targets = [7, 13, 21, 100]
    
    for target in targets:
        print(f"\n--- Searching for {target} ---")
        
        # Linear
        idx = linear_search(arr, target)
        print(f"Linear Search:     index {idx}")
        
        # Binary
        idx = binary_search_range(arr, target, 0, len(arr)-1)
        print(f"Binary Search:     index {idx}")
        
        # Jump
        idx = jump_search(arr, target)
        print(f"Jump Search:       index {idx}")
        
        # Exponential
        idx = exponential_search(arr, target)
        print(f"Exponential Search: index {idx}")
    
    # Trace examples
    print("\n" + "=" * 60)
    print("JUMP SEARCH TRACE")
    print("=" * 60)
    jump_search_trace(arr, 13)
    
    print("\n" + "=" * 60)
    print("EXPONENTIAL SEARCH TRACE")
    print("=" * 60)
    exponential_search_trace(arr, 13)
    
    # Benchmark
    print("\n" + "=" * 60)
    print("PERFORMANCE BENCHMARK")
    print("=" * 60)
    benchmark_searches()