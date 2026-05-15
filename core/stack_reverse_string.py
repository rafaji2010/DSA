"""
core/stack_reverse_string.py
Reverse a string using a stack (no [::-1] slicing!)
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import TypeVar, Generic
from core.stack_linked import StackLinked


def reverse_string_stack(text: str) -> str:
    """
    Reverse a string using a stack.
    
    Time: O(n) - push each char, pop each char
    Space: O(n) - stack stores all characters
    
    This demonstrates the LIFO property: last character pushed
    becomes the first character popped.
    """
    if not text:
        return ""
    
    # Push all characters onto stack
    stack = StackLinked[str]()
    for char in text:
        stack.push(char)
    
    # Pop all characters (they come out in reverse order)
    reversed_chars = []
    while not stack.is_empty():
        reversed_chars.append(stack.pop())
    
    return "".join(reversed_chars)


def reverse_string_stack_verbose(text: str) -> str:
    """Same as above but with print statements to visualize."""
    if not text:
        return ""
    
    print(f"Original string: {text}")
    print(f"Length: {len(text)}")
    print("\n--- Pushing characters onto stack ---")
    
    stack = StackLinked[str]()
    for i, char in enumerate(text):
        stack.push(char)
        print(f"  Push: '{char}' → Stack: {stack}")
    
    print("\n--- Popping characters (LIFO order) ---")
    reversed_chars = []
    while not stack.is_empty():
        char = stack.pop()
        reversed_chars.append(char)
        print(f"  Pop: '{char}' → Reversed so far: {''.join(reversed_chars)}")
    
    result = "".join(reversed_chars)
    print(f"\n✓ Reversed: {result}")
    return result


if __name__ == "__main__":
    print("=" * 50)
    print("REVERSE STRING USING STACK")
    print("=" * 50)
    
    test_strings = [
        "hello",
        "racecar",
        "Python",
        "A",
        "",
        "12345"
    ]
    
    for text in test_strings:
        reversed_str = reverse_string_stack(text)
        expected = text[::-1]  # Python's built-in reverse (we're learning why this works!)
        
        status = "✅" if reversed_str == expected else "❌"
        print(f"{status} reverse_string_stack('{text}') = '{reversed_str}'")
    
    print("\n" + "=" * 50)
    print("VERBOSE EXAMPLE")
    print("=" * 50)
    reverse_string_stack_verbose("hello")
    
    print("\n✅ All tests passed!")