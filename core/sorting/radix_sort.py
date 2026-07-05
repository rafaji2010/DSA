"""
core/sorting/radix_sort.py
Radix Sort - LSD (Least Significant Digit)
Time: O(d × n) where d = number of digits
Space: O(n + k) where k = base (10 for decimal)
"""

from typing import List


def counting_sort_by_digit(arr: List[int], exp: int) -> List[int]:
    """
    Stable counting sort based on a specific digit position.
    
    exp: 1 = units digit, 10 = tens digit, 100 = hundreds digit, etc.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0-9
    
    # Count occurrences of each digit
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    
    # Cumulative count for stable sorting
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array (right to left for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]
    
    return output


def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix Sort (LSD - Least Significant Digit first).
    
    Time: O(d × n) where d = number of digits
    Space: O(n + k) where k = 10 (decimal base)
    """
    if not arr:
        return []
    
    arr = arr.copy()
    max_val = max(arr)
    
    # Sort by each digit position
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr


def radix_sort_with_trace(arr: List[int]) -> List[int]:
    """Radix Sort with detailed tracing."""
    if not arr:
        return []
    
    print(f"Original: {arr}")
    arr = arr.copy()
    max_val = max(arr)
    
    exp = 1
    pass_num = 1
    while max_val // exp > 0:
        print(f"\n--- Pass {pass_num}: Sorting by digit position {exp} ({(exp*10)//10}'s place) ---")
        
        # Show current digits
        print(f"Digits to sort by:")
        for num in arr:
            digit = (num // exp) % 10
            print(f"  {num} → digit = {digit}")
        
        arr = counting_sort_by_digit(arr, exp)
        print(f"After pass {pass_num}: {arr}")
        
        exp *= 10
        pass_num += 1
    
    return arr


if __name__ == "__main__":
    print("=" * 60)
    print("RADIX SORT DEMONSTRATION")
    print("=" * 60)
    
    test_arrays = [
        [170, 45, 75, 90, 802, 24, 2, 66],
        [3, 1, 4, 1, 5, 9, 2, 6],
        [100, 20, 3, 400, 5],
    ]
    
    for arr in test_arrays:
        sorted_arr = radix_sort(arr)
        print(f"\nOriginal: {arr}")
        print(f"Sorted:   {sorted_arr}")
    
    print("\n" + "-" * 40)
    print("DETAILED TRACE")
    print("-" * 40)
    radix_sort_with_trace([170, 45, 75, 90, 802, 24, 2, 66])
    
    print("\n" + "=" * 60)
    print("RADIX SORT VS COUNTING SORT")
    print("=" * 60)
    print("""
    ┌─────────────────────────────────────────────────────────────────────┐
    │                    Counting Sort         Radix Sort                │
    ├─────────────────────────────────────────────────────────────────────┤
    │ Time               O(n + k)              O(d × n)                  │
    │ Space              O(k)                  O(n + k)                  │
    │ Best for           Small range (k ≈ n)   Large numbers, many digits│
    │ Integer only?      Yes                   Yes (but can adapt)       │
    │ Stable?            Yes (with cumulative) Yes                       │
    └─────────────────────────────────────────────────────────────────────┘
    
    Use Counting Sort when:  k (range) is small (e.g., grades 0-100)
    Use Radix Sort when:     numbers have many digits but range is huge
    """)
    
    print("✅ Radix Sort complete!")
