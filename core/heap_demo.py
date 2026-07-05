#!/usr/bin/env python3
"""
core/heap_demo.py
Heaps, Priority Queues, and Top-K Problems

Time Complexities:
    - Push:     O(log n)
    - Pop:      O(log n)
    - Peek:     O(1)
    - Heapify:  O(n)
    - Heapsort: O(n log n)

Space Complexity: O(n) for the heap array
"""

import heapq
from typing import List, Tuple
import math


# ============================================================
# MIN-HEAP (Python's heapq is always a min-heap)
# ============================================================

def demo_min_heap() -> None:
    """Demonstrate min-heap operations using heapq."""
    print("=" * 60)
    print("MIN-HEAP DEMO (heapq)")
    print("=" * 60)

    heap: List[int] = []
    values = [10, 20, 15, 30, 40, 50, 45]
    print(f"\nPushing values: {values}")
    for v in values:
        heapq.heappush(heap, v)
        print(f"  After push {v}: {heap}")

    print(f"\n[Peek] Smallest element: {heap[0]}")
    print(f"\nPopping all elements (sorted order):")
    sorted_vals = []
    while heap:
        val = heapq.heappop(heap)
        sorted_vals.append(val)
        print(f"  Popped: {val}, Remaining: {heap}")

    print(f"\n[OK] Result: {sorted_vals}")
    print(f"   This is essentially HEAPSORT!")


# ============================================================
# MAX-HEAP (Negation Trick)
# ============================================================

def demo_max_heap() -> None:
    """
    Demonstrate max-heap using negation trick.
    Since heapq only supports min-heap, we store negative values.
    """
    print("\n" + "=" * 60)
    print("MAX-HEAP DEMO (Negation Trick)")
    print("=" * 60)

    heap: List[int] = []
    values = [10, 20, 15, 30, 40, 50, 45]

    print(f"\nPushing values: {values}")
    for v in values:
        heapq.heappush(heap, -v)
        print(f"  After push {v}: {[-x for x in heap]}")

    print(f"\n[Peek] Largest element: {-heap[0]}")

    print(f"\nPopping all elements (descending order):")
    sorted_desc = []
    while heap:
        val = -heapq.heappop(heap)
        sorted_desc.append(val)
        print(f"  Popped: {val}")

    print(f"\n[OK] Result: {sorted_desc}")


# ============================================================
# TOP-K PROBLEMS
# ============================================================

def top_k_largest(nums: List[int], k: int) -> List[int]:
    """
    Find the k largest elements in nums.
    
    Approach: Min-heap of size k
    - Maintain a min-heap of the k largest seen so far
    - If new element > heap min, replace min with new element
    
    Time:  O(n log k) -- better than O(n log n) sorting
    Space: O(k)
    """
    if k <= 0:
        return []
    if k >= len(nums):
        return sorted(nums, reverse=True)

    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)

    return sorted(heap, reverse=True)


def top_k_smallest(nums: List[int], k: int) -> List[int]:
    """
    Find the k smallest elements in nums.
    
    Approach: Max-heap of size k (using negation)
    
    Time:  O(n log k)
    Space: O(k)
    """
    if k <= 0:
        return []
    if k >= len(nums):
        return sorted(nums)

    heap = [-x for x in nums[:k]]
    heapq.heapify(heap)

    for num in nums[k:]:
        if -num > heap[0]:
            heapq.heapreplace(heap, -num)

    return sorted([-x for x in heap])


def kth_largest(nums: List[int], k: int) -> int:
    """
    Find the k-th largest element.
    
    Time:  O(n log k)
    Space: O(k)
    """
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)

    return heap[0]


def demo_top_k() -> None:
    """Demonstrate top-k algorithms."""
    print("\n" + "=" * 60)
    print("TOP-K PROBLEMS")
    print("=" * 60)

    nums = [3, 1, 5, 12, 2, 11, 7, 8, 4, 9]
    k = 3

    print(f"\nArray: {nums}")
    print(f"k = {k}")

    print(f"\n[>] Top {k} largest: {top_k_largest(nums, k)}")
    print(f"[>] Top {k} smallest: {top_k_smallest(nums, k)}")
    print(f"[>] {k}-th largest: {kth_largest(nums, k)}")


# ============================================================
# PRIORITY QUEUE APPLICATIONS
# ============================================================

def recently_contacted(contacts: List[Tuple[str, float]], k: int = 5) -> List[str]:
    """
    'Recently Contacted' feature using timestamps.
    Smaller timestamp = more recent.
    """
    heap: List[Tuple[float, str]] = []

    for name, timestamp in contacts:
        heapq.heappush(heap, (timestamp, name))

    result = []
    for _ in range(min(k, len(heap))):
        timestamp, name = heapq.heappop(heap)
        result.append(name)

    return result


def task_scheduler(tasks: List[Tuple[str, int]]) -> List[str]:
    """
    Task scheduler using priority queue.
    Lower priority number = higher urgency.
    """
    heap: List[Tuple[int, str]] = []

    for name, priority in tasks:
        heapq.heappush(heap, (priority, name))

    result = []
    while heap:
        _, name = heapq.heappop(heap)
        result.append(name)

    return result


def demo_priority_queue() -> None:
    """Demonstrate priority queue applications."""
    print("\n" + "=" * 60)
    print("PRIORITY QUEUE APPLICATIONS")
    print("=" * 60)

    contacts = [
        ("Alice", 100.0),
        ("Bob", 50.0),
        ("Carol", 200.0),
        ("David", 10.0),
        ("Eve", 75.0),
    ]
    print(f"\n[Contacts] (name, timestamp):")
    for name, ts in contacts:
        print(f"   {name}: {ts}")
    print(f"\n[>] Recently contacted (top 3): {recently_contacted(contacts, 3)}")

    tasks = [
        ("email", 3),
        ("server_down", 1),
        ("meeting", 2),
        ("lunch", 5),
        ("bug_fix", 1),
    ]
    print(f"\n[Tasks] (name, priority):")
    for name, p in tasks:
        print(f"   {name}: priority {p}")
    print(f"\n[>] Execution order: {task_scheduler(tasks)}")


# ============================================================
# HEAPIFY: O(n) BUILD
# ============================================================

def demo_heapify() -> None:
    """Demonstrate O(n) heapify vs O(n log n) repeated push."""
    print("\n" + "=" * 60)
    print("HEAPIFY: O(n) vs O(n log n)")
    print("=" * 60)

    arr = [3, 1, 6, 5, 2, 4]
    print(f"\nOriginal array: {arr}")

    heap1 = []
    for x in arr:
        heapq.heappush(heap1, x)
    print(f"\nMethod 1 (push each): {heap1}")

    heap2 = arr.copy()
    heapq.heapify(heap2)
    print(f"Method 2 (heapify):   {heap2}")

    print("\n[Tip] heapify is faster because it uses bottom-up approach")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    demo_min_heap()
    demo_max_heap()
    demo_top_k()
    demo_priority_queue()
    demo_heapify()

    print("\n" + "=" * 60)
    print("[OK] All demos complete!")
    print("=" * 60)
