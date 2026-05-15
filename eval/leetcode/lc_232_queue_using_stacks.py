"""
LeetCode 232 - Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

Time: push O(1), pop amortized O(1), peek amortized O(1)
Space: O(n)
"""


class MyQueue:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue
    
    def push(self, x: int) -> None:
        """Push element to back of queue. O(1)"""
        self.stack1.append(x)
    
    def _transfer(self) -> None:
        """Transfer elements from stack1 to stack2 if stack2 is empty."""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
    
    def pop(self) -> int:
        """Remove and return front element. Amortized O(1)"""
        self._transfer()
        return self.stack2.pop()
    
    def peek(self) -> int:
        """Return front element without removing. Amortized O(1)"""
        self._transfer()
        return self.stack2[-1]
    
    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


if __name__ == "__main__":
    q = MyQueue()
    
    q.push(1)
    q.push(2)
    q.push(3)
    
    print(f"Peek: {q.peek()}")   # 1
    print(f"Pop: {q.pop()}")     # 1
    print(f"Pop: {q.pop()}")     # 2
    print(f"Empty: {q.empty()}") # False
    print(f"Pop: {q.pop()}")     # 3
    print(f"Empty: {q.empty()}") # True