"""
core/complexity_analysis.py
Classify the time complexity of each snippet
"""

def snippet_a(n: int) -> None:
    """What is the time complexity?"""
    for i in range(n):
        print(i)
    # Answer: O(n) - single loop


def snippet_b(n: int) -> None:
    """What is the time complexity?"""
    for i in range(n):
        for j in range(n):
            print(i, j)
    # Answer: O(n²) - nested loops


def snippet_c(arr: list) -> None:
    """What is the time complexity?"""
    x = arr[0]
    y = arr[-1]
    print(x, y)
    # Answer: O(1) - constant time operations


def snippet_d(n: int) -> None:
    """What is the time complexity?"""
    for i in range(n):
        for j in range(i, n):
            print(i, j)
    # Answer: O(n²) - sum of n + (n-1) + ... + 1 = n(n+1)/2


def snippet_e(arr: list, target: int) -> int:
    """What is the time complexity?"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    # Answer: O(log n) - binary search halves search space


def snippet_f(arr: list) -> None:
    """What is the time complexity?"""
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                print(i, j, k)
    # Answer: O(n³) - triple nested loops


if __name__ == "__main__":
    print("=== Complexity Analysis ===")
    print("snippet_a: O(n)")
    print("snippet_b: O(n²)")
    print("snippet_c: O(1)")
    print("snippet_d: O(n²)")
    print("snippet_e: O(log n)")
    print("snippet_f: O(n³)")