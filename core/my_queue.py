"""
core/my_queue.py
Implement a Queue (FIFO) from scratch - NO AI!
"""

# --- Explanation of issues in the original code ---
# 1. Typo: 'none' should be 'None' (capital N) in Node.
# 2. Node class is not used in your Queue implementation.
# 3. 'slef.value' in Queue's __init__ is a typo and unnecessary for a simple list-backed queue.
# 4. 'arr' as a class variable means all queues share it; should be instance variable (self.arr).
# 5. Push, pop, peek are not correct Python list or deque methods; syntax is wrong.
# 6. arr is not prefixed with self; should be self.arr everywhere.
# 7. dequeue and peek logic is incorrect and not Pythonic.
# 8. Incorrect use of return and syntax in methods.
# 9. Not handling IndexError conditions properly and not raising with a helpful message.
# 10. Multiple logic errors in how methods are implemented.
# 11. Pythonic: Prefer using a deque from collections for O(1) enqueue/dequeue if allowed, otherwise use a list carefully for basic conceptual implementation.

# --- Corrected & Pythonic version using list as requested ---

class Queue:
    """
    FIFO Queue implementation using a Python list.
    Methods: enqueue, dequeue, peek, is_empty, size
    """
    def __init__(self):
        """Initialize empty queue"""
        self.arr = []

    def enqueue(self, value):
        """
        Add element to the back of the queue.
        Time: O(1) amortized for list append
        """
        self.arr.append(value)

    def dequeue(self):
        """
        Remove and return element from the front.
        Time: O(n), as list pop(0) is O(n)
        Raises IndexError if empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.arr.pop(0)

    def peek(self):
        """
        Return front element without removing.
        Raises IndexError if empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.arr[0]

    def is_empty(self):
        """Return True if queue has no elements."""
        return len(self.arr) == 0

    def size(self):
        """Return number of elements in queue."""
        return len(self.arr)


# Write your own test cases
if __name__ == "__main__":
    # Test 1: Enqueue and dequeue
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2

    # Test 2: Peek
    q.enqueue('a')
    assert q.peek() == 'a'
    q.enqueue('b')
    assert q.peek() == 'a'

    # Test 3: Empty queue error
    q.dequeue()  # queue is empty after this
    try:
        q.dequeue()
    except IndexError:
        print("Correctly raised IndexError on dequeue from empty queue")

    # Test 4: Size tracking
    q.enqueue(100)
    q.enqueue(200)
    assert q.size() == 2
    q.dequeue()
    assert q.size() == 1
    print("All tests passed.")