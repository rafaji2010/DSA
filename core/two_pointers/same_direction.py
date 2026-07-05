"""
core/two_pointers/same_direction.py
Two Pointers - Same Direction Pattern (Fast & Slow)
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    LeetCode 26 - Remove Duplicates from Sorted Array
    Remove duplicates in-place, return new length.
    
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    
    slow = 0
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1


def move_zeroes(nums: List[int]) -> None:
    """
    LeetCode 283 - Move Zeroes
    Move all zeros to end, preserving relative order.
    
    Time: O(n), Space: O(1)
    """
    slow = 0
    
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


def remove_element(nums: List[int], val: int) -> int:
    """
    LeetCode 27 - Remove Element
    Remove all occurrences of val in-place.
    
    Time: O(n), Space: O(1)
    """
    slow = 0
    
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow


if __name__ == "__main__":
    print("=" * 60)
    print("TWO POINTERS - SAME DIRECTION")
    print("=" * 60)
    
    # Remove Duplicates
    print("\n--- Remove Duplicates ---")
    nums = [0, 0, 1, 1, 2, 2, 3, 3]
    print(f"Original: {nums}")
    length = remove_duplicates(nums)
    print(f"After removing duplicates: {nums[:length]}")
    
    # Move Zeroes
    print("\n--- Move Zeroes ---")
    nums = [0, 1, 0, 3, 12]
    print(f"Original: {nums}")
    move_zeroes(nums)
    print(f"After moving zeroes: {nums}")
    
    # Remove Element
    print("\n--- Remove Element ---")
    nums = [3, 2, 2, 3]
    val = 3
    print(f"Original: {nums}, remove {val}")
    length = remove_element(nums, val)
    print(f"After removal: {nums[:length]}")
    
    print("\n✅ Same direction patterns complete!")
