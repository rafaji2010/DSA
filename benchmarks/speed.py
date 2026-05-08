#!/usr/bin/env python3
"""Big O benchmark: Compare O(1) vs O(n) vs O(n²) operations."""

import time
import sys
from pathlib import Path

# Add src to path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data_structures.stack import Stack
from src.data_structures.queue import Queue


def benchmark_stack_operations(n: int = 10000):
    """Stack push/pop is O(1) - should be very fast."""
    stack = Stack[int]()
    
    # Push n elements
    start = time.perf_counter()
    for i in range(n):
        stack.push(i)
    push_time = time.perf_counter() - start
    
    # Pop n elements
    start = time.perf_counter()
    for i in range(n):
        stack.pop()
    pop_time = time.perf_counter() - start
    
    return push_time, pop_time


def benchmark_queue_operations(n: int = 10000):
    """Queue enqueue/dequeue is O(1) - should be very fast."""
    queue = Queue[int]()
    
    # Enqueue n elements
    start = time.perf_counter()
    for i in range(n):
        queue.enqueue(i)
    enqueue_time = time.perf_counter() - start
    
    # Dequeue n elements
    start = time.perf_counter()
    for i in range(n):
        queue.dequeue()
    dequeue_time = time.perf_counter() - start
    
    return enqueue_time, dequeue_time


def benchmark_o_n_squared(n: int = 5000):
    """O(n²) example: Nested loops - should be SLOW."""
    arr = list(range(n))
    
    start = time.perf_counter()
    # BAD: O(n²) - nested loop
    count = 0
    for i in range(n):
        for j in range(n):
            count += arr[i] * arr[j]
    time_n2 = time.perf_counter() - start
    
    start = time.perf_counter()
    # GOOD: O(n) - single loop
    count = 0
    for i in range(n):
        count += arr[i] * arr[i]
    time_n = time.perf_counter() - start
    
    return time_n2, time_n


def main():
    print("=" * 60)
    print("BIG O BENCHMARK: O(1) vs O(n) vs O(n²)")
    print("=" * 60)
    
    # Test O(1) operations with increasing input sizes
    sizes = [1000, 10000, 50000]
    
    print("\n📊 STACK & QUEUE (O(1) operations):")
    print("-" * 60)
    print(f"{'Size':<10} {'Stack Push':<12} {'Stack Pop':<12} {'Queue Enqueue':<12} {'Queue Dequeue':<12}")
    print("-" * 60)
    
    for size in sizes:
        push_t, pop_t = benchmark_stack_operations(size)
        enq_t, deq_t = benchmark_queue_operations(size)
        print(f"{size:<10} {push_t:.4f}s   {pop_t:.4f}s   {enq_t:.4f}s      {deq_t:.4f}s")
    
    print("\n📈 O(n) vs O(n²) COMPARISON:")
    print("-" * 60)
    print("O(n²) nested loops will grow MUCH faster than O(n) linear")
    print("-" * 60)
    
    n_values = [500, 1000, 2000]
    for n in n_values:
        n2_time, n_time = benchmark_o_n_squared(n)
        ratio = n2_time / n_time if n_time > 0 else 0
        print(f"n={n:<5} | O(n²): {n2_time:.4f}s | O(n): {n_time:.4f}s | Ratio: {ratio:.1f}x slower")
    
    print("\n💡 KEY INSIGHT:")
    print("  O(1): Time stays CONSTANT as input grows (Stack/Queue)")
    print("  O(n): Time grows LINEARLY with input")
    print("  O(n²): Time grows QUADRATICALLY - avoid nested loops on large data!")


if __name__ == "__main__":
    main()
