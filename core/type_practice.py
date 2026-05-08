"""Practice file for type hints - Day 2 Exercise 1."""

from typing import List, Optional
from pydantic import BaseModel

# Basic type hints
def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b

# List type hint
def double_all(numbers: List[int]) -> List[int]:
    """Double every number in the list."""
    return [n * 2 for n in numbers]

# Optional type hint (can be None)
def greet(name: Optional[str] = None) -> str:
    """Greet a person by name, or say hello world."""
    if name:
        return f"Hello, {name}!"
    return "Hello, world!"

# Pydantic model (already using your installed dependency)
class Person(BaseModel):
    name: str
    age: int
    email: str

# Test the code
if __name__ == "__main__":
    print("Testing type hints:")
    print(f"add_numbers(5, 3) = {add_numbers(5, 3)}")
    print(f"double_all([1, 2, 3]) = {double_all([1, 2, 3])}")
    print(f"greet('AJ') = {greet('AJ')}")
    print(f"greet() = {greet()}")
    
    # Test Pydantic model
    person = Person(name="AJ", age=25, email="aj@example.com")
    print(f"Person model: {person}")