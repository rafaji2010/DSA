"""
core/two_pointers/opposite_direction.py
Two Pointers - Opposite Direction Pattern
"""

from typing import List

def two_sum_two_pointers(numbers: List[int], target: int) -> List[int]:
    """
    Two pointers moving from opposite ends.
    
    Time: O(n), Space: O(1)
    """
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed as per problem
        elif current_sum < target:
            left += 1  # Need larger sum → move left right
        else:
            right -= 1  # Need smaller sum → move right left
    
    return []


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """
    LeetCode 167 - Two Sum II (Sorted array)
    Find two numbers that sum to target.
    
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


def is_palindrome(s: str) -> bool:
    """
    LeetCode 125 - Valid Palindrome
    Check if string is palindrome using two pointers.
    
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


def reverse_string(s: List[str]) -> None:
    """
    LeetCode 344 - Reverse String
    Reverse string in-place using two pointers.
    
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    print("=" * 60)
    print("TWO POINTERS - OPPOSITE DIRECTION")
    print("=" * 60)
    
    # Two Sum II
    print("\n--- Two Sum II ---")
    numbers = [2, 7, 11, 15]
    result = two_sum_sorted(numbers, 9)
    print(f"two_sum_sorted({numbers}, 9) = {result}")
    
    # Valid Palindrome
    print("\n--- Valid Palindrome ---")
    test_strings = ["A man, a plan, a canal: Panama", "race a car", "hello"]
    for s in test_strings:
        result = is_palindrome(s)
        print(f"is_palindrome('{s}') = {result}")
    
    # Reverse String
    print("\n--- Reverse String ---")
    s = ["h", "e", "l", "l", "o"]
    print(f"Original: {s}")
    reverse_string(s)
    print(f"Reversed: {s}")
    
    print("\n✅ Opposite direction patterns complete!")
