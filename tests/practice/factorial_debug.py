#!/usr/bin/env python3
"""
core/factorial_debug.py
Factorial with breakpoint for call stack exploration.

Use: python3 -m pdb factorial_debug.py
Then: c (continue) until breakpoint, then w (where)
"""


def factorial(n: int) -> int:
    """Calculate factorial recursively."""
    print(f"  Entering factorial({n})")
    
    if n == 1:
        print(f"  → Base case reached! n={n}")
        breakpoint()  # STOP HERE — deepest recursion level
        return 1
    
    result = n * factorial(n - 1)
    print(f"  Returning factorial({n}) = {result}")
    return result


if __name__ == "__main__":
    n = 5
    print(f"Calculating factorial({n})...")
    print("=" * 50)
    
    result = factorial(n)
    
    print("=" * 50)
    print(f"factorial({n}) = {result}")