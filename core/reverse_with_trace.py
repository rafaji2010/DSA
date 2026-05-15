from typing import Optional, TypeVar, Generic

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: Optional[Node[T]] = None

def create_test_list(values: list[T]) -> Optional[Node[T]]:
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

def reverse_with_pointer_trace(head: Optional[Node[T]], depth: int = 0) -> Optional[Node[T]]:
    indent = "  " * depth
    
    if head is None or head.next is None:
        print(f"{indent}BASE: head={head.value if head else 'None'}")
        return head
    
    print(f"{indent}BEFORE RECURSION: head={head.value}, head.next={head.next.value if head.next else 'None'}")
    
    new_head = reverse_with_pointer_trace(head.next, depth + 1)
    
    print(f"{indent}AFTER RECURSION: head={head.value}, head.next={head.next.value if head.next else 'None'}")
    print(f"{indent}new_head={new_head.value if new_head else 'None'}")
    print(f"{indent}head.next is new_head? {head.next is new_head}")
    
    # Now modify pointers
    head.next.next = head
    head.next = None
    
    print(f"{indent}AFTER MODIFICATION: head.next={head.next}, new_head.next={new_head.next.value if new_head.next else 'None'}")
    print(f"{indent}Returning new_head={new_head.value}")
    
    return new_head

if __name__ == "__main__":
    print("=" * 60)
    print("CREATING TEST LIST: [1, 2, 3, 4]")
    print("=" * 60)
    
    head = create_test_list([1, 2, 3, 4])
    
    print("\n" + "=" * 60)
    print("STARTING REVERSE WITH POINTER TRACE")
    print("=" * 60 + "\n")
    
    result = reverse_with_pointer_trace(head)
    
    print("\n" + "=" * 60)
    print(f"FINAL RESULT: head={result.value if result else 'None'}")
    print("=" * 60)
