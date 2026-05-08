"""Pytest unit tests for Stack implementation."""

import pytest
from core.stack import Stack


class TestStack:
    """Test cases for Stack data structure."""
    
    def test_new_stack_is_empty(self):
        """A newly created stack should be empty."""
        s = Stack[int]()
        assert s.is_empty() is True
        assert s.size() == 0
    
    def test_push_adds_item(self):
        """Pushing an item increases size and makes it top."""
        s = Stack[str]()
        s.push("first")
        assert s.is_empty() is False
        assert s.size() == 1
        assert s.peek() == "first"
    
    def test_multiple_pushes(self):
        """Multiple pushes work in LIFO order."""
        s = Stack[int]()
        s.push(1)
        s.push(2)
        s.push(3)
        assert s.size() == 3
        assert s.peek() == 3
    
    def test_pop_removes_top_item(self):
        """Pop removes and returns the top item."""
        s = Stack[int]()
        s.push(10)
        s.push(20)
        s.push(30)
        
        popped = s.pop()
        assert popped == 30
        assert s.size() == 2
        assert s.peek() == 20
    
    def test_pop_empty_stack_raises_error(self):
        """Popping from empty stack should raise IndexError."""
        s = Stack[float]()
        with pytest.raises(IndexError, match="Cannot pop from empty stack"):
            s.pop()
    
    def test_peek_empty_stack_raises_error(self):
        """Peeking at empty stack should raise IndexError."""
        s = Stack[str]()
        with pytest.raises(IndexError, match="Cannot peek at empty stack"):
            s.peek()
    
    def test_peek_does_not_modify_stack(self):
        """Peek should return the top item without removing it."""
        s = Stack[int]()
        s.push(42)
        s.push(99)
        
        top = s.peek()
        assert top == 99
        assert s.size() == 2  # Size unchanged
        assert s.pop() == 99  # Item still there
    
    def test_stack_with_different_types(self):
        """Stack should work with any type."""
        # Integer stack
        int_stack = Stack[int]()
        int_stack.push(100)
        assert int_stack.pop() == 100
        
        # String stack
        str_stack = Stack[str]()
        str_stack.push("test")
        assert str_stack.pop() == "test"
        
        # Boolean stack
        bool_stack = Stack[bool]()
        bool_stack.push(True)
        bool_stack.push(False)
        assert bool_stack.pop() is False
        assert bool_stack.pop() is True
    
    def test_lifo_order(self):
        """Stack must maintain LIFO (Last-In-First-Out) order."""
        s = Stack[int]()
        items = [1, 2, 3, 4, 5]
        
        # Push all items
        for item in items:
            s.push(item)
        
        # Pop should return in reverse order
        for expected in reversed(items):
            assert s.pop() == expected
        
        assert s.is_empty() is True