
from typing import Any

class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[tuple[Any, float]] = []
    
    def add(self, item: Any, price: float) -> None:
        self.items.append((item, price))
    
    def total(self) -> float:
        return sum([price for _, price in self.items])
   
    
    def remove(self, item: Any) -> bool:
        for idx, (itm, _) in enumerate(self.items):
            if itm == item:
                self.items.pop(idx)
                return True
        return False
   
# Create a Stack class with push, pop, peek, is_empty, size methods
# Include type hints and docstrings
class Stack:
    def __init__(self) -> None:
        self.items: list[Any] = []
    
    def push(self, item: Any) -> None:
        self.items.append(item)
    
    def pop(self) -> Any:
        return self.items.pop()
    
    def peek(self) -> Any:
def find_duplicates_inefficient(arr):
    """Find duplicates using nested loops - O(n²)"""
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

def slow_fibonacci(n):
    """Recursive fibonacci - O(2^n)"""
    if n <= 1:
        return n
    return slow_fibonacci(n-1) + slow_fibonacci(n-2)

def find_duplicates_optimized(arr):
    """Find duplicates using a set - O(n)"""
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def fibonacci(n):
    """Iterative fibonacci - O(n)"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
