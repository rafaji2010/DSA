"""Manual test for Stack implementation."""

from core.stack import Stack

def test_stack():
    print("Testing Stack Implementation")
    print("=" * 30)
    
    # Create a stack
    s = Stack[int]()  # Stack that holds integers
    print(f"Created empty stack: {s}")
    print(f"Is empty? {s.is_empty()}")
    print(f"Size: {s.size()}")
    
    # Push items
    print("\n--- Pushing items 10, 20, 30 ---")
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"Stack after pushes: {s}")
    print(f"Size: {s.size()}")
    print(f"Is empty? {s.is_empty()}")
    
    # Peek at top
    print(f"\nPeek at top: {s.peek()}")
    print(f"Stack after peek (unchanged): {s}")
    
    # Pop items
    print("\n--- Popping items ---")
    popped = s.pop()
    print(f"Popped: {popped}")
    print(f"Stack after pop: {s}")
    
    popped = s.pop()
    print(f"Popped: {popped}")
    print(f"Stack after pop: {s}")
    
    # Test string stack (different type)
    print("\n--- String Stack Example ---")
    names = Stack[str]()
    names.push("Alice")
    names.push("Bob")
    names.push("Charlie")
    print(f"Names stack: {names}")
    print(f"Top name: {names.peek()}")
    print(f"Popped: {names.pop()}")
    print(f"Stack now: {names}")
    
    # Test with mixed types (using Any - but type checker will warn)
    print("\n--- Mixed Type Stack ---")
    mixed = Stack()  # No type hint = can hold anything
    mixed.push(42)
    mixed.push("hello")
    mixed.push(3.14)
    print(f"Mixed stack: {mixed}")
    
    # Test error handling
    print("\n--- Testing Error Handling ---")
    empty = Stack[int]()
    try:
        empty.pop()
    except IndexError as e:
        print(f"✅ Caught error correctly: {e}")
    
    try:
        empty.peek()
    except IndexError as e:
        print(f"✅ Caught error correctly: {e}")

if __name__ == "__main__":
    test_stack()