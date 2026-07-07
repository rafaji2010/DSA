"""In-Place Heap Sort — build max heap, then extract max repeatedly."""

from typing import List


def heapify(arr: List[int], n: int, root: int):
    """Heapify subtree rooted at index root. n = heap size."""
    largest = root          # Assume root is largest
    left = 2 * root + 1     # Left child
    right = 2 * root + 2    # Right child
    
    # If left child exists and is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # If right child exists and is larger than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root, swap and continue heapifying
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, n, largest)  # Recursively heapify affected subtree


def build_max_heap(arr: List[int]):
    """Build max heap from unsorted array."""
    n = len(arr)
    # Start from last non-leaf node and heapify upwards
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr: List[int]) -> List[int]:
    """In-place heap sort. Returns sorted array."""
    n = len(arr)
    if n <= 1:
        return arr
    
    # Step 1: Build max heap
    build_max_heap(arr)
    print(f"Max heap built: {arr}")
    
    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Swap root (max) with last element
        arr[0], arr[i] = arr[i], arr[0]
        print(f"  Swap max to position {i}: {arr}")
        
        # Heapify reduced heap (exclude sorted part at end)
        heapify(arr, i, 0)
        print(f"  Heapify [0:{i}]:        {arr[:i]} | sorted: {arr[i:]}")
    
    return arr


def heap_sort_verbose(arr: List[int]) -> List[int]:
    """Verbose version with full trace."""
    n = len(arr)
    if n <= 1:
        return arr
    
    print(f"\n{'='*50}")
    print(f"HEAP SORT: {arr}")
    print(f"{'='*50}")
    
    print("\n--- Step 1: Build Max Heap ---")
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(f"  Heapify subtree at {i}: {arr}")
    print(f"Max heap: {arr}")
    
    print("\n--- Step 2: Extract Max Repeatedly ---")
    for i in range(n - 1, 0, -1):
        print(f"\n  Iteration {n - i}:")
        print(f"    Before: {arr}")
        arr[0], arr[i] = arr[i], arr[0]
        print(f"    Swap root↔last: {arr}")
        print(f"    → {arr[i]} is now in correct sorted position!")
        heapify(arr, i, 0)
        print(f"    After heapify:  {arr}")
        print(f"    Sorted so far:  {arr[i:]}")
    
    print(f"\n✅ Final sorted: {arr}")
    return arr


if __name__ == "__main__":
    # Test heap sort
    test_arrays: List[List[int]]= [
        [3, 1, 4, 1, 5, 9, 2, 6],
        [64, 34, 25, 12, 22, 11, 90],
        [5, 4, 3, 2, 1],
        [1],
        [],
    ]
    
    print("=" * 50)
    print("HEAP SORT VERBOSE")
    print("=" * 50)
    
    for arr in test_arrays:
        if not arr:
            print("\n[] → []")
            continue
        arr_copy = arr.copy()
        sorted_arr = heap_sort_verbose(arr_copy)
        print(f"Original: {arr} → Sorted: {sorted_arr}\n")