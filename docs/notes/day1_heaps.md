# Day 1: Heaps + Priority Queues

## Key Concepts
- Min-Heap: Parent <= Children, root = smallest
- Max-Heap: Parent >= Children, root = largest
- Array formulas: parent=(i-1)//2, left=2i+1, right=2i+2

## Python heapq
- Always min-heap
- Max-heap via negation: store -v, read -heap[0]

## Top-K Pattern
- Top-K largest: Min-heap of size k, O(n log k)
- Top-K smallest: Max-heap of size k, O(n log k)

## Files
- core/heap_demo.py - heapq demonstrations
- core/max_heap_demo.py - max-heap from scratch
