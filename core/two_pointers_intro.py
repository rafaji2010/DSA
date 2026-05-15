# core/two_pointers_intro.py
"""Introduction to Two Pointers technique.

Two Pointers is a powerful pattern for array manipulation:
1. Opposite ends (left and right moving inward)
2. Same direction (slow and fast pointers)
"""

from typing import List


# ─────────────────────────────────────────────────────────────────────────
# Pattern 1: Opposite Ends (Left and Right moving inward)
# ─────────────────────────────────────────────────────────────────────────

def reverse_array(arr: List[int]) -> List[int]:
    """
    Reverse an array in-place using two pointers (opposite ends).
    
    Time: O(n) - we visit each element once
    Space: O(1) - no extra array needed
    
    Example:
    >>> reverse_array([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        # Swap elements at left and right
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome using two pointers.
    
    Time: O(n) - we compare at most n/2 pairs
    Space: O(1) - only two pointers
    
    Example:
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("hello")
    False
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


def is_palindrome_alphanumeric(s: str) -> bool:
    """
    Check palindrome ignoring non-alphanumeric characters and case.
    
    Example:
    >>> is_palindrome_alphanumeric("A man, a plan, a canal: Panama")
    True
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


# ─────────────────────────────────────────────────────────────────────────
# Pattern 2: Same Direction (Slow and Fast pointers)
# ─────────────────────────────────────────────────────────────────────────

def remove_duplicates_sorted(nums: List[int]) -> int:
    """
    Remove duplicates in-place from sorted array using slow/fast pointers.
    Returns the new length.
    
    Time: O(n) - single pass
    Space: O(1) - in-place
    
    Example:
    >>> arr = [1, 1, 2, 2, 3, 4, 4, 5]
    >>> length = remove_duplicates_sorted(arr)
    >>> arr[:length]
    [1, 2, 3, 4, 5]
    """
    if not nums:
        return 0
    
    slow: int = 0  # Points to last unique element
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1


def move_zeros(nums: List[int]) -> None:  # ← FIXED: Added "-> None"
    """
    Move all zeros to the end while preserving order of non-zero elements.
    
    Time: O(n) - single pass
    Space: O(1) - in-place
    
    Example:
    >>> arr = [0, 1, 0, 3, 12]
    >>> move_zeros(arr)
    >>> arr
    [1, 3, 12, 0, 0]
    """
    slow: int = 0  # Position to place next non-zero
    
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


# ─────────────────────────────────────────────────────────────────────────
# Visualization Function (for learning, not for production)
# ─────────────────────────────────────────────────────────────────────────

def visualize_two_pointers() -> None:  # ← FIXED: Added "-> None"
    """Interactive visualization of two pointers with step-by-step output."""
    print("=" * 60)
    print("Two Pointers - Interactive Visualization")
    print("=" * 60)
    
    # Pattern 1: Reverse Array
    print("\n1. REVERSE ARRAY (Opposite Ends)")
    print("-" * 40)
    arr: List[int] = [1, 2, 3, 4, 5, 6, 7]
    print(f"Original: {arr}")
    
    left, right = 0, len(arr) - 1
    step = 1
    
    while left < right:
        print(f"\n  Step {step}: left={left}, right={right}")
        print(f"    Before swap: {arr}")
        arr[left], arr[right] = arr[right], arr[left]
        print(f"    After swap:  {arr}")
        left += 1
        right -= 1
        step += 1
    
    print(f"\n  Final reversed: {arr}")
    
    # Pattern 2: Remove Duplicates
    print("\n\n2. REMOVE DUPLICATES (Slow & Fast Pointers)")
    print("-" * 40)
    arr2: List[int] = [1, 1, 2, 2, 3, 4, 4, 5]
    print(f"Original: {arr2}")
    
    if not arr2:
        return
    
    slow: int = 0
    print(f"\n  Initial: slow={slow}, fast starts at 1")
    
    for fast in range(1, len(arr2)):
        print(f"\n  fast={fast}: arr2[fast]={arr2[fast]}, arr2[slow]={arr2[slow]}")
        if arr2[fast] != arr2[slow]:
            slow += 1
            arr2[slow], arr2[fast] = arr2[fast], arr2[slow]
            print(f"    → Found new value! slow={slow}, array: {arr2}")
        else:
            print(f"    → Duplicate found, moving fast only")
    
    print(f"\n  Final unique portion: {arr2[:slow+1]}")
    print(f"  Rest (ignored): {arr2[slow+1:]}")


# ─────────────────────────────────────────────────────────────────────────
# Main execution
# ─────────────────────────────────────────────────────────────────────────

def main() -> None:  # Added main function with type annotation
    """Main function to run all examples."""
    # Test Pattern 1: Opposite Ends
    print("=" * 60)
    print("PATTERN 1: Opposite Ends (Left & Right)")
    print("=" * 60)
    
    arr1: List[int] = [1, 2, 3, 4, 5]
    print(f"\nOriginal array: {arr1}")
    print(f"Reversed: {reverse_array(arr1[:])}")  # Pass copy to preserve original
    
    print(f"\n'racecar' is palindrome: {is_palindrome('racecar')}")
    print(f"'hello' is palindrome: {is_palindrome('hello')}")
    print(f"'A man, a plan, a canal: Panama' is palindrome: {is_palindrome_alphanumeric('A man, a plan, a canal: Panama')}")
    
    # Test Pattern 2: Same Direction
    print("\n" + "=" * 60)
    print("PATTERN 2: Same Direction (Slow & Fast)")
    print("=" * 60)
    
    arr2: List[int] = [1, 1, 2, 2, 3, 4, 4, 5]
    print(f"\nOriginal array: {arr2}")
    length: int = remove_duplicates_sorted(arr2)
    print(f"After removing duplicates (length={length}): {arr2[:length]}")
    
    arr3: List[int] = [0, 1, 0, 3, 12]
    print(f"\nOriginal array: {arr3}")
    move_zeros(arr3)
    print(f"After moving zeros: {arr3}")
    
    # Run visualization
    print("\n")
    visualize_two_pointers()


if __name__ == "__main__":
    main()