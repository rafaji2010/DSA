"""Unit tests for Stack implementation."""
import pytest
from src.data_structures.stack import Stack


class TestStack:
    """Test cases for Stack class."""
    
    def test_push_pop_basic(self):
        """Test basic push and pop operations."""
        stack = Stack[int]()
        
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        assert stack.size() == 3
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty()
    
    def test_peek(self):
        """Test peek method."""
        stack = Stack[str]()
        
        assert stack.peek() is None
        
        stack.push("first")
        assert stack.peek() == "first"
        
        stack.push("second")
        assert stack.peek() == "second"
        
        stack.pop()
        assert stack.peek() == "first"
    
    def test_is_empty(self):
        """Test is_empty method."""
        stack = Stack[float]()
        assert stack.is_empty()
        
        stack.push(10.5)
        assert not stack.is_empty()
        
        stack.pop()
        assert stack.is_empty()
    
    def test_size(self):
        """Test size method."""
        stack = Stack[int]()
        assert stack.size() == 0
        
        for i in range(5):
            stack.push(i)
            assert stack.size() == i + 1
        
        for i in range(5):
            stack.pop()
            assert stack.size() == 4 - i
    
    def test_clear(self):
        """Test clear method."""
        stack = Stack[int]()
        
        for i in range(10):
            stack.push(i)
        
        assert stack.size() == 10
        stack.clear()
        assert stack.size() == 0
        assert stack.is_empty()
        assert stack.pop() is None
    
    def test_max_size(self):
        """Test stack with maximum size limit."""
        stack = Stack[int](max_size=3)
        
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        assert stack.size() == 3
        
        with pytest.raises(OverflowError, match="Stack is full"):
            stack.push(4)
        
        # Should be able to pop and then push again
        assert stack.pop() == 3
        stack.push(4)
        assert stack.size() == 3
    
    def test_pop_empty(self):
        """Test pop on empty stack."""
        stack = Stack[int]()
        assert stack.pop() is None
        
        stack.push(1)
        stack.pop()
        assert stack.pop() is None
    
    def test_len_function(self):
        """Test __len__ magic method."""
        stack = Stack[int]()
        assert len(stack) == 0
        
        stack.push(1)
        stack.push(2)
        assert len(stack) == 2
    
    def test_bool_function(self):
        """Test __bool__ magic method."""
        stack = Stack[int]()
        assert not bool(stack)  # Empty stack is False
        
        stack.push(1)
        assert bool(stack)  # Non-empty stack is True
    
    def test_string_representation(self):
        """Test __str__ method."""
        stack = Stack[int]()
        assert str(stack) == "Stack(top=[])"
        
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert str(stack) == "Stack(top=[3, 2, 1])"
    
    def test_repr(self):
        """Test __repr__ method."""
        stack = Stack[int](max_size=5)
        stack.push(1)
        stack.push(2)
        assert repr(stack) == "Stack([1, 2], max_size=5)"
    
    def test_iteration(self):
        """Test iteration over stack items."""
        stack = Stack[int]()
        items = [1, 2, 3, 4, 5]
        
        for item in items:
            stack.push(item)
        
        # Iteration should be from bottom to top
        for i, item in enumerate(stack):
            assert item == items[i]
        
        # Test that iteration doesn't modify stack
        assert stack.size() == 5


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])