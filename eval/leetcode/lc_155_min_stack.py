# eval/lc_155_min_stack.py
from typing import List

class MinStack:
    """
    LeetCode 155: Min Stack
    Uses two stacks: one for values, one for minimums.
    """
    def __init__(self) -> None:
        self.stack: List[int] = []
        self.min_stack: List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_stack if it's empty or val is <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # If we popped the minimum, remove it from min_stack too
            if self.min_stack and val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        raise IndexError("top from empty stack")

    def get_min(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("get_min from empty stack")

if __name__ == "__main__":
    ms = MinStack()
    ms.push(5)
    ms.push(3)
    ms.push(7)
    print(f"Top: {ms.top()}")       # 7
    print(f"Min: {ms.get_min()}")   # 3
    ms.pop()
    print(f"Min after pop: {ms.get_min()}") # 3