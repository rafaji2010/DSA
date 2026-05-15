"""
LeetCode 225 - Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/

Time: push O(1), pop O(n), top O(n)
Space: O(n)
"""

from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x: int) -> None:
        """Push element onto stack. O(1)"""
        self.q1.append(x)
    
    def pop(self) -> int:
        """Remove and return top element. O(n)"""
        # Move all but last element to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        # Pop the last element (top of stack)
        value = self.q1.popleft()
        
        # Swap queues
        self.q1, self.q2 = self.q2, self.q1
        
        return value
    
    def top(self) -> int:
        """Return top element without removing. O(n)"""
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        value = self.q1[0]
        
        # Move the last element to q2 as well
        self.q2.append(self.q1.popleft())
        
        # Swap queues
        self.q1, self.q2 = self.q2, self.q1
        
        return value
    
    def empty(self) -> bool:
        return len(self.q1) == 0


class MyStackOneQueue:
    """Optimized version using only ONE queue"""
    
    def __init__(self):
        self.q = deque()
    
    def push(self, x: int) -> None:
        """Push by rotating the queue. O(n)"""
        self.q.append(x)
        # Rotate so new element becomes front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self) -> int:
        return self.q.popleft()
    
    def top(self) -> int:
        return self.q[0]
    
    def empty(self) -> bool:
        return len(self.q) == 0


if __name__ == "__main__":
    print("=== Two Queue Implementation ===")
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Top: {stack.top()}")  # 3
    print(f"Pop: {stack.pop()}")  # 3
    print(f"Pop: {stack.pop()}")  # 2
    print(f"Empty: {stack.empty()}")  # False
    print(f"Pop: {stack.pop()}")  # 1
    print(f"Empty: {stack.empty()}")  # True
    
    print("\n=== One Queue Implementation ===")
    stack2 = MyStackOneQueue()
    stack2.push(1)
    stack2.push(2)
    stack2.push(3)
    print(f"Top: {stack2.top()}")  # 3
    print(f"Pop: {stack2.pop()}")  # 3
    print(f"Pop: {stack2.pop()}")  # 2