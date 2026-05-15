"""
core/stack_balanced_debug.py
Valid Parentheses - Debug version with pdb
"""

import os
import sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from core.stack_linked import StackLinked


def is_balanced_debug(expression: str) -> bool:
    """
    Check if brackets are balanced.
    Includes pdb breakpoints for debugging.
    """
    # Map closing brackets to their matching opening brackets
    matching = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    stack = StackLinked[str]()
    
    print(f"\n--- Processing: {expression} ---")
    print(f"Length: {len(expression)}")
    
    for i, char in enumerate(expression):
        print(f"\n  Position {i}: char = '{char}'")
        print(f"    Stack before: {stack}")
        
        # If opening bracket, push onto stack
        if char in "([{":
            stack.push(char)
            print(f"    Opening bracket → pushing '{char}'")
            print(f"    Stack after: {stack}")
        
        # If closing bracket, check match
        elif char in ")]}":
            print(f"    Closing bracket '{char}'")
            
            # If stack is empty → nothing to match
            if stack.is_empty():
                print(f"    ❌ Stack is empty! Nothing to match '{char}'")
                return False
            
            # Pop top of stack and compare
            top = stack.pop()
            print(f"    Popped top: '{top}'")
            
            # Check if popped bracket matches the closing bracket
            if top != matching[char]:
                print(f"    ❌ Mismatch: '{top}' != '{matching[char]}'")
                return False
            
            print(f"    ✓ Match: '{top}' matches '{char}'")
        
        else:
            print(f"    Ignoring non-bracket character: '{char}'")
        
        print(f"    Stack after: {stack}")
    
    # Stack should be empty if all brackets matched
    result = stack.is_empty()
    print(f"\n  Final result: {result} (stack empty = {stack.is_empty()})")
    return result


def is_balanced_with_pdb(expression: str) -> bool:
    """
    Same as above but with pdb breakpoint.
    Run with: python -m pdb core/stack_balanced_debug.py
    Then use: b is_balanced_with_pdb, then c, then n to step through.
    """
    matching = {')': '(', '}': '{', ']': '['}
    stack = StackLinked[str]()
    
    import pdb; pdb.set_trace()  # ← pdb stops here
    
    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            if stack.pop() != matching[char]:
                return False
    
    return stack.is_empty()


if __name__ == "__main__":
    print("=" * 60)
    print("VALID PARENTHESES - DEBUG VERSION")
    print("=" * 60)
    
    test_cases = [
        ("()", True, "Simple parentheses"),
        ("()[]{}", True, "Multiple bracket types"),
        ("(]", False, "Mismatched brackets"),
        ("([)]", False, "Incorrect nesting"),
        ("{[]}", True, "Properly nested"),
        ("", True, "Empty string"),
        ("(", False, "Unclosed opening"),
        (")", False, "Unmatched closing"),
        ("([])", True, "Nested with multiple brackets"),
    ]
    
    for expr, expected, description in test_cases:
        result = is_balanced_debug(expr)
        status = "✅" if result == expected else "❌"
        print(f"\n{status} {description}: '{expr}' → {result} (expected {expected})")
    
    # pdb example - uncomment to debug
    print("\n" + "=" * 60)
    print("PDB EXAMPLE - Uncomment to debug")
    print("=" * 60)
    print("Run: python -m pdb core/stack_balanced_debug.py")
    print("Then: b is_balanced_with_pdb")
    print("Then: c")
    print("Then: n (to step through)")
    
    # Uncomment to debug:
    #is_balanced_with_pdb("({[]})")