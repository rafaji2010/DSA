"""
benchmarks/deque_vs_list.py
Compare list.pop(0) vs deque.popleft()
"""

from collections import deque
import time

def benchmark_list(n: int) -> float:
    """Time list.pop(0) operations"""
    lst = list(range(n))
    start = time.perf_counter()
    while lst:
        lst.pop(0)
    return time.perf_counter() - start

def benchmark_deque(n: int) -> float:
    """Time deque.popleft() operations"""
    dq = deque(range(n))
    start = time.perf_counter()
    while dq:
        dq.popleft()
    return time.perf_counter() - start

if __name__ == "__main__":
    sizes = [1000, 5000, 10000, 20000]
    
    print("=" * 50)
    print(f"{'Size':<10} {'list.pop(0)':<15} {'deque.popleft()':<15} {'Ratio'}")
    print("=" * 50)
    
    for size in sizes:
        list_time = benchmark_list(size)
        deque_time = benchmark_deque(size)
        ratio = list_time / deque_time if deque_time > 0 else 0
        print(f"{size:<10} {list_time:<15.4f} {deque_time:<15.4f} {ratio:<10.1f}x")
    
    print("=" * 50)
    print("CONCLUSION: deque is O(1), list.pop(0) is O(n)")