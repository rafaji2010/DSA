"""
benchmarks/front_operations_benchmark.py
Compare array vs linked list for front operations
"""
import time
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.linked_list import LinkedList


def benchmark_array_front_ops(n: int):
    """Test array (list) with front insert/pop"""
    arr = []
    
    # Measure insert at front
    start = time.perf_counter()
    for i in range(n):
        arr.insert(0, i)
    insert_time = time.perf_counter() - start
    
    # Measure pop from front
    start = time.perf_counter()
    for i in range(n):
        arr.pop(0)
    pop_time = time.perf_counter() - start
    
    return insert_time, pop_time


def benchmark_linked_list_front_ops(n: int):
    """Test linked list with front insert/pop"""
    ll = LinkedList()
    
    # Measure prepend
    start = time.perf_counter()
    for i in range(n):
        ll.prepend(i)
    prepend_time = time.perf_counter() - start
    
    # Measure delete from front (delete head repeatedly)
    start = time.perf_counter()
    for i in range(n):
        ll.delete_at_index(0)  # Delete head
    delete_time = time.perf_counter() - start
    
    return prepend_time, delete_time


if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10000, 20000]
    
    print("=" * 70)
    print(f"{'Size':<10} {'Array Insert':<15} {'Array Pop':<15} {'LL Prepend':<15} {'LL Delete':<15}")
    print("=" * 70)
    
    for size in sizes:
        arr_ins, arr_pop = benchmark_array_front_ops(size)
        ll_pre, ll_del = benchmark_linked_list_front_ops(size)
        
        print(f"{size:<10} {arr_ins:<15.4f} {arr_pop:<15.4f} {ll_pre:<15.4f} {ll_del:<15.4f}")
    
    print("\n" + "=" * 70)
    print("CONCLUSION: Linked list prepend/pop is O(1) — performance stays flat")
    print("          Array insert(0)/pop(0) is O(n) — gets slower as size grows")