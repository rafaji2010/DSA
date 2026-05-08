"""Demo script for Queue implementation."""
from src.data_structures import Queue


def demo_basic_operations():
    """Demonstrate basic queue operations."""
    print("=" * 50)
    print("Basic Queue Operations")
    print("=" * 50)
    
    queue = Queue[int]()
    
    print("Enqueuing 1, 2, 3")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    print(f"Queue: {queue}")
    print(f"Size: {queue.size()}")
    print(f"Peek: {queue.peek()}")
    
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Queue after dequeue: {queue}")
    print(f"Size: {queue.size()}")
    print()


def demo_max_size():
    """Demonstrate queue with maximum size."""
    print("=" * 50)
    print("Queue with Max Size")
    print("=" * 50)
    
    queue = Queue[int](max_size=3)
    
    print("Enqueuing 10, 20, 30")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    print(f"Queue: {queue}")
    
    try:
        print("Attempting to enqueue 40...")
        queue.enqueue(40)
    except OverflowError as e:
        print(f"Error: {e}")
    
    print(f"Dequeued: {queue.dequeue()}")
    queue.enqueue(40)
    print(f"After dequeue and enqueue 40: {queue}")
    print()


def demo_real_world():
    """Demonstrate real-world queue usage."""
    print("=" * 50)
    print("Real-World Example: Printer Queue")
    print("=" * 50)
    
    class PrintJob:
        def __init__(self, doc_name: str, pages: int):
            self.doc_name = doc_name
            self.pages = pages
        
        def __str__(self):
            return f"{self.doc_name} ({self.pages} pages)"
    
    printer_queue = Queue[PrintJob]()
    
    # Add print jobs
    jobs = [
        PrintJob("resume.pdf", 2),
        PrintJob("presentation.pptx", 15),
        PrintJob("photo.jpg", 1),
        PrintJob("contract.docx", 5)
    ]
    
    for job in jobs:
        printer_queue.enqueue(job)
        print(f"Added to queue: {job}")
    
    print(f"\nTotal jobs in queue: {printer_queue.size()}")
    print(f"Next job: {printer_queue.peek()}\n")
    
    # Process jobs
    print("Processing jobs:")
    while not printer_queue.is_empty():
        job = printer_queue.dequeue()
        print(f"  Printing: {job}")
    
    print(f"\nAll jobs processed. Queue empty: {printer_queue.is_empty()}")
    print()


def demo_iteration():
    """Demonstrate queue iteration."""
    print("=" * 50)
    print("Iterating Over Queue")
    print("=" * 50)
    
    queue = Queue[str]()
    items = ["apple", "banana", "cherry", "date", "elderberry"]
    
    for item in items:
        queue.enqueue(item)
    
    print("Queue contents (front to rear):")
    for idx, item in enumerate(queue, 1):
        print(f"  Position {idx}: {item}")
    
    print(f"\nQueue unchanged after iteration: {queue}")
    print(f"Size still: {queue.size()}")
    print()


def compare_stack_vs_queue():
    """Compare Stack (LIFO) vs Queue (FIFO)."""
    print("=" * 50)
    print("Stack vs Queue Comparison")
    print("=" * 50)
    
    from src.data_structures import Stack
    
    # Same input for both
    data = [1, 2, 3, 4, 5]
    
    # Stack (LIFO - Last In First Out)
    stack = Stack[int]()
    print("Stack (LIFO):")
    for item in data:
        stack.push(item)
        print(f"  Pushed: {item}")
    
    print("  Popping:", end="")
    while not stack.is_empty():
        print(f" {stack.pop()}", end="")
    print("\n")
    
    # Queue (FIFO - First In First Out)
    queue = Queue[int]()
    print("Queue (FIFO):")
    for item in data:
        queue.enqueue(item)
        print(f"  Enqueued: {item}")
    
    print("  Dequeuing:", end="")
    while not queue.is_empty():
        print(f" {queue.dequeue()}", end="")
    print("\n")


if __name__ == "__main__":
    demo_basic_operations()
    demo_max_size()
    demo_real_world()
    demo_iteration()
    compare_stack_vs_queue()