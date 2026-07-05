#!/usr/bin/env python3
"""
core/max_heap_demo.py
Max-Heap Implementation from Scratch with Visual Tracing
"""

from typing import List, Optional
import math


class MaxHeap:
    """A max-heap implemented from scratch using a dynamic array."""

    def __init__(self, elements: Optional[List[int]] = None):
        self.heap: List[int] = []
        if elements:
            self.heap = elements.copy()
            self._heapify()

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left_child(self, i: int) -> int:
        return 2 * i + 1

    def _right_child(self, i: int) -> int:
        return 2 * i + 2

    def push(self, val: int) -> None:
        """Add element to heap. Bubble up to maintain max-heap property."""
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self) -> Optional[int]:
        """Remove and return the maximum element."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_val

    def peek(self) -> Optional[int]:
        return self.heap[0] if self.heap else None

    def _bubble_up(self, i: int) -> None:
        parent = self._parent(i)
        while i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = self._parent(i)

    def _sink_down(self, i: int) -> None:
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
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._sink_down(i)

    def __len__(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def to_sorted_list(self) -> List[int]:
        result = []
        while not self.is_empty():
            result.append(self.pop())
        return result


def demo_max_heap():
    print("=" * 60)
    print("MAX-HEAP FROM SCRATCH")
    print("=" * 60)

    h = MaxHeap()
    for v in [40, 20, 50, 10, 30, 5, 15]:
        h.push(v)
        print(f"After push {v}: {h.heap}")

    print(f"\nPeek max: {h.peek()}")
    print(f"Sorted descending: {h.to_sorted_list()}")


if __name__ == "__main__":
    demo_max_heap()
