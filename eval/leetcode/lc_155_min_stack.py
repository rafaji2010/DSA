"""
eval/leetcode/lc_155_min_stack.py
LeetCode 155 - Min Stack
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving 
the minimum element in constant time.

Time: O(1) for all operations
Space: O(n) for the min stack
"""

class MinStack:
    def __init__(self):
        """Initialize two stacks: main stack and min tracker stack."""
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        """
        Push value onto stack.
        Also push to min_stack if it's the new minimum.
        """
        self.stack.append(val)
        
        # If min_stack is empty or val is new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # Repeat the current minimum
            self.min_stack.append(self.min_stack[-1])
    
    def pop(self) -> None:
        """Remove top element from both stacks."""
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
    
    def top(self) -> int:
        """Return top element without removing."""
        return self.stack[-1] if self.stack else None
    
    def getMin(self) -> int:
        """Return minimum element in stack."""
        return self.min_stack[-1] if self.min_stack else None


class MinStackOptimized:
    """
    Memory-optimized version: only push to min_stack when we see a new minimum.
    This saves space but requires handling duplicates carefully.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # Only push to min_stack if val is <= current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            # If we popped the minimum, pop from min_stack too
            if popped == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
    
    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


if __name__ == "__main__":
    print("=" * 50)
    print("LeetCode 155 - Min Stack")
    print("=" * 50)
    
    # Test with regular version
    minStack = MinStack()
    
    print("Push operations:")
    minStack.push(-2)
    print("  push(-2)")
    minStack.push(0)
    print("  push(0)")
    minStack.push(-3)
    print("  push(-3)")
    
    print(f"\ngetMin() → {minStack.getMin()} (expected -3)")
    
    minStack.pop()
    print("\npop()")
    
    print(f"top() → {minStack.top()} (expected 0)")
    print(f"getMin() → {minStack.getMin()} (expected -2)")
    
    # Test with optimized version
    print("\n" + "=" * 50)
    print("Optimized Version Test")
    print("=" * 50)
    
    minStackOpt = MinStackOptimized()
    values = [5, 3, 7, 2, 1]
    
    for v in values:
        minStackOpt.push(v)
        print(f"push({v}) → min = {minStackOpt.getMin()}")
    
    print(f"\nTop: {minStackOpt.top()}")
    
    while minStackOpt.stack:
        print(f"pop() → min = {minStackOpt.getMin()}")
        minStackOpt.pop()
    
    print("\n✅ Min Stack implementation complete!")