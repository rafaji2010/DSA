"""
Buggy code for debugging practice
"""

def find_max_buggy(numbers):
    """This has a bug - can you find it?"""
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def binary_search_buggy(arr, target):
    """This has an off-by-one bug"""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid
        else:
            right = mid
    return -1
