#!/usr/bin/env python3
"""
core/max_heap_demo.py
Max-Heap Implementation from Scratch with Visual Tracing

This file demonstrates max-heap operations WITHOUT using heapq,
showing the underlying mechanics clearly.

Time Complexities:
    - Push:     O(log n)
    - Pop:      O(log n)
    - Peek:     O(1)
    - Heapify:  O(n)

Space Complexity: O(n) for the heap array
"""

from typing import List, Optional, Callable
import math


class MaxHeap:
    """
    A max-heap implemented from scratch using a dynamic array.

    In a max-heap, the parent is always >= its children.
    The largest element is always at index 0 (the root).
    """

    def __init__(self, elements: Optional[List[int]] = None):
        self.heap: List[int] = []
        if elements:
            self.heap = elements.copy()
            self._heapify()

    # ---------------------------------------------------------
    # Index formulas (same for min-heap and max-heap)
    # ---------------------------------------------------------
    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left_child(self, i: int) -> int:
        return 2 * i + 1

    def _right_child(self, i: int) -> int:
        return 2 * i + 2

    # ---------------------------------------------------------
    # Core operations
    # ---------------------------------------------------------
    def push(self, val: int) -> None:
        """
        Add element to heap. Bubble up to maintain max-heap property.
        Time: O(log n)
        """
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self) -> Optional[int]:
        """
        Remove and return the maximum element (root).
        Sink down to maintain max-heap property.
        Time: O(log n)
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        # Replace root with last element
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_val

    def peek(self) -> Optional[int]:
        """Return maximum element without removing. Time: O(1)"""
        return self.heap[0] if self.heap else None

    # ---------------------------------------------------------
    # Internal maintenance
    # ---------------------------------------------------------
    def _bubble_up(self, i: int) -> None:
        """Move element at index i up until heap property restored."""
        parent = self._parent(i)
        while i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = self._parent(i)

    def _sink_down(self, i: int) -> None:
        """Move element at index i down until heap property restored."""
        n = len(self.heap)
        while True:
            largest = i
            left = self._left_child(i)
            right = self._right_child(i)

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

    def _heapify(self) -> None:
        """Build max-heap from arbitrary array in O(n)."""
        n = len(self.heap)
        # Start from last non-leaf node and sink down each
        for i in range(n // 2 - 1, -1, -1):
            self._sink_down(i)

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------
    def __len__(self) -> int:
        return len(self.heap)

    def __repr__(self) -> str:
        return f"MaxHeap({self.heap})"

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def to_sorted_list(self) -> List[int]:
        """Extract all elements in descending order. Destructive."""
        result = []
        while not self.is_empty():
            result.append(self.pop())
        return result


# ============================================================
# VISUAL TRACER: Max-Heap with step-by-step output
# ============================================================

class VisualMaxHeap(MaxHeap):
    """Max-heap that prints every step for educational purposes."""

    def push(self, val: int) -> None:
        print(f"\n{'='*60}")
        print(f"PUSH: {val}")
        print(f"{'='*60}")
        print("Before:")
        self._print_tree()

        self.heap.append(val)
        print(f"\n  [>] Add {val} at end: {self.heap}")

        # Bubble up with trace
        i = len(self.heap) - 1
        while i > 0:
            parent = self._parent(i)
            print(f"  [>] Compare {self.heap[i]} with parent {self.heap[parent]} at index {parent}")

            if self.heap[i] > self.heap[parent]:
                print(f"  [>] {self.heap[i]} > {self.heap[parent]}: SWAP!")
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                print(f"  [>] {self.heap[i]} <= {self.heap[parent]}: STOP")
                break

        if i == 0 and len(self.heap) > 1:
            print("  [>] Reached root. STOP")

        print("\nAfter:")
        self._print_tree()

    def pop(self) -> Optional[int]:
        print(f"\n{'='*60}")
        print(f"POP: Remove maximum")
        print(f"{'='*60}")

        if not self.heap:
            print("  (empty heap)")
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        print(f"Root to remove: {max_val}")
        print("Before:")
        self._print_tree()

        self.heap[0] = self.heap.pop()
        print(f"\n  [>] Replace root with last element: {self.heap[0]}")

        # Sink down with trace
        i = 0
        n = len(self.heap)
        while True:
            largest = i
            left = self._left_child(i)
            right = self._right_child(i)

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != i:
                print(f"  [>] {self.heap[i]} < child {self.heap[largest]}: SWAP!")
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                print(f"  [>] {self.heap[i]} >= all children: STOP")
                break

        print("\nAfter:")
        self._print_tree()
        return max_val

    def _print_tree(self) -> None:
        """Print heap as an ASCII tree."""
        if not self.heap:
            print("  (empty)")
            return

        n = len(self.heap)
        height = int(math.log2(n)) + 1 if n > 0 else 0

        print(f"  Array: {self.heap}")
        print(f"  Tree:")

        index = 0
        for level in range(height):
            nodes_in_level = min(2**level, n - index)
            spacing = 2**(height - level + 1)
            line = " " * (spacing // 2)

            for _ in range(nodes_in_level):
                if index < n:
                    line += f"{self.heap[index]:^3}" + " " * spacing
                    index += 1
            print(line.rstrip())


# ============================================================
# DEMONSTRATIONS
# ============================================================

def demo_insertion_trace() -> None:
    """Visual step-by-step insertion into max-heap."""
    print("\n" + "#" * 70)
    print("# MAX-HEAP INSERTION TRACE")
    print("# Insert: 40, 20, 50, 10, 30, 5, 15")
    print("#" * 70)

    h = VisualMaxHeap()
    for val in [40, 20, 50, 10, 30, 5, 15]:
        h.push(val)

    print(f"\n{'#'*70}")
    print("# FINAL MAX-HEAP")
    print(f"{'#'*70}")
    h._print_tree()


def demo_pop_trace() -> None:
    """Visual step-by-step extraction from max-heap."""
    print("\n" + "#" * 70)
    print("# MAX-HEAP POP TRACE")
    print("#" * 70)

    h = VisualMaxHeap([50, 30, 40, 10, 20, 5, 15])
    print("\nInitial heap:")
    h._print_tree()

    sorted_vals = []
    while not h.is_empty():
        sorted_vals.append(h.pop())

    print(f"\n{'#'*70}")
    print(f"# EXTRACTED IN DESCENDING ORDER: {sorted_vals}")
    print("# This is HEAPSORT (descending)!")
    print(f"{'#'*70}")


def demo_heapify_trace() -> None:
    """Visual heapify from arbitrary array."""
    print("\n" + "#" * 70)
    print("# HEAPIFY TRACE: [3, 1, 6, 5, 2, 4]")
    print("#" * 70)

    arr = [3, 1, 6, 5, 2, 4]
    print(f"\nOriginal array: {arr}")

    h = VisualMaxHeap()
    h.heap = arr.copy()
    print("\nAs a tree (NOT a heap yet):")
    h._print_tree()

    n = len(h.heap)
    print(f"\n[>] Start from last non-leaf node: index {n//2 - 1} (value {h.heap[n//2 - 1]})")

    for i in range(n // 2 - 1, -1, -1):
        print(f"\n{'-'*60}")
        print(f"Sink down node at index {i} (value {h.heap[i]})")
        print(f"{'-'*60}")
        h._sink_down_trace(i)

    print(f"\n{'#'*70}")
    print("# FINAL MAX-HEAP AFTER HEAPIFY")
    print(f"{'#'*70}")
    h._print_tree()


def demo_max_heap_vs_min_heap() -> None:
    """Side-by-side comparison of max-heap and min-heap."""
    print("\n" + "#" * 70)
    print("# MAX-HEAP vs MIN-HEAP COMPARISON")
    print("# Same input: [40, 20, 50, 10, 30]")
    print("#" * 70)

    values = [40, 20, 50, 10, 30]

    # Max-heap
    max_h = VisualMaxHeap()
    for v in values:
        max_h.heap.append(v)
    max_h._heapify()

    print("\n--- MAX-HEAP ---")
    max_h._print_tree()
    print("Property: Parent >= Children")
    print("Root = LARGEST element")

    # Min-heap (using Python's heapq)
    import heapq
    min_h = values.copy()
    heapq.heapify(min_h)

    print("\n--- MIN-HEAP ---")
    print(f"  Array: {min_h}")
    print("  Tree:")
    # Simple print
    print(f"        {min_h[0]}")
    print(f"       / \\")
    print(f"     {min_h[1]}   {min_h[2]}")
    print(f"    / \\")
    print(f"  {min_h[3]}  {min_h[4]}")
    print("Property: Parent <= Children")
    print("Root = SMALLEST element")


def demo_top_k_with_max_heap() -> None:
    """Demonstrate top-k smallest using max-heap."""
    print("\n" + "#" * 70)
    print("# TOP-K SMALLEST USING MAX-HEAP")
    print("# Find 3 smallest from [20, 5, 15, 30, 10, 25]")
    print("#" * 70)

    nums = [20, 5, 15, 30, 10, 25]
    k = 3

    print(f"\nArray: {nums}")
    print(f"k = {k}")

    # Maintain max-heap of size k
    heap = MaxHeap(nums[:k])
    print(f"\n[Step 1] Build max-heap with first {k} elements: {nums[:k]}")
    print(f"         Heap: {heap.heap}")
    print(f"         Root ({heap.peek()}) = k-th smallest so far")

    for num in nums[k:]:
        print(f"\n[Step 2] Process {num}:")
        if num < heap.peek():
            print(f"         {num} < root ({heap.peek()}): REPLACE root with {num}")
            heap.pop()
            heap.push(num)
            print(f"         New heap: {heap.heap}")
            print(f"         New root: {heap.peek()}")
        else:
            print(f"         {num} >= root ({heap.peek()}): IGNORE")

    result = sorted(heap.to_sorted_list())
    print(f"\n[Result] Top {k} smallest: {result}")
    print(f"[Time] O(n log k) -- each of n-k elements does at most one push/pop")


# ============================================================
# Sink-down trace helper
# ============================================================

def _sink_down_trace(self, i: int) -> None:
    """Traced version of sink_down for heapify visualization."""
    n = len(self.heap)
    while True:
        largest = i
        left = self._left_child(i)
        right = self._right_child(i)

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            print(f"  [>] {self.heap[i]} < child {self.heap[largest]}: SWAP!")
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest
        else:
            print(f"  [>] {self.heap[i]} >= all children: STOP")
            break


# Monkey-patch for demo
VisualMaxHeap._sink_down_trace = _sink_down_trace


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    demo_insertion_trace()
    demo_pop_trace()
    demo_heapify_trace()
    demo_max_heap_vs_min_heap()
    demo_top_k_with_max_heap()

    print("\n" + "#" * 70)
    print("# ALL MAX-HEAP DEMOS COMPLETE!")
    print("#" * 70)
