"""Maximum-finding helpers.

Important: an unsorted list has no O(log n) max algorithm — you must read
every element at least once (Ω(n)). O(log n) applies when the data is
structured, e.g. sorted in non-decreasing order (binary search below).
"""


def find_max(numbers: list[int] | None) -> int:
    """Return the largest value in any list. Time: O(n), space: O(1)."""
    if numbers is None:
        raise TypeError("numbers must not be None")
    if not numbers:
        raise ValueError("numbers must not be empty")

    largest = numbers[0]
    for value in numbers[1:]:
        if value > largest:
            largest = value
    return largest


def find_max_sorted(numbers: list[int] | None) -> int:
    """Return the largest value in a non-decreasing sorted list.

    Time: O(log n), space: O(1).
    Precondition: numbers[i] <= numbers[i + 1] for all valid i.
    """
    if numbers is None:
        raise TypeError("numbers must not be None")
    if not numbers:
        raise ValueError("numbers must not be empty")

    lo, hi = 0, len(numbers) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if numbers[mid] < numbers[hi]:
            lo = mid + 1
        else:
            hi = mid
    return numbers[lo]


if __name__ == "__main__":
    values = [5, 3, 4, 8, 7, 5, 2]
    print(f"Largest (O(n)): {find_max(values)}")

    sorted_values = [1, 3, 3, 5, 8, 8, 9]
    print(f"Largest sorted (O(log n)): {find_max_sorted(sorted_values)}")
