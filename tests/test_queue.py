"""Unit tests for Queue implementation."""
import pytest
from src.data_structures.queue import Queue


class TestQueue:
    """Test cases for Queue class."""
    
    def test_enqueue_dequeue_basic(self):
        """Test basic enqueue and dequeue operations."""
        queue = Queue[int]()
        
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        assert queue.size() == 3
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.is_empty()
    
    def test_peek(self):
        """Test peek method."""
        queue = Queue[str]()
        
        assert queue.peek() is None
        
        queue.enqueue("first")
        assert queue.peek() == "first"
        
        queue.enqueue("second")
        assert queue.peek() == "first"  # Still first (FIFO)
        
        queue.dequeue()
        assert queue.peek() == "second"
    
    def test_is_empty(self):
        """Test is_empty method."""
        queue = Queue[float]()
        assert queue.is_empty()
        
        queue.enqueue(10.5)
        assert not queue.is_empty()
        
        queue.dequeue()
        assert queue.is_empty()
    
    def test_size(self):
        """Test size method."""
        queue = Queue[int]()
        assert queue.size() == 0
        
        for i in range(5):
            queue.enqueue(i)
            assert queue.size() == i + 1
        
        for i in range(5):
            queue.dequeue()
            assert queue.size() == 4 - i
    
    def test_clear(self):
        """Test clear method."""
        queue = Queue[int]()
        
        for i in range(10):
            queue.enqueue(i)
        
        assert queue.size() == 10
        queue.clear()
        assert queue.size() == 0
        assert queue.is_empty()
        assert queue.dequeue() is None
    
    def test_max_size(self):
        """Test queue with maximum size limit."""
        queue = Queue[int](max_size=3)
        
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        assert queue.size() == 3
        
        with pytest.raises(OverflowError, match="Queue is full"):
            queue.enqueue(4)
        
        # Should be able to dequeue and then enqueue again
        assert queue.dequeue() == 1
        queue.enqueue(4)
        assert queue.size() == 3
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
    
    def test_dequeue_empty(self):
        """Test dequeue on empty queue."""
        queue = Queue[int]()
        assert queue.dequeue() is None
        
        queue.enqueue(1)
        queue.dequeue()
        assert queue.dequeue() is None
    
    def test_len_function(self):
        """Test __len__ magic method."""
        queue = Queue[int]()
        assert len(queue) == 0
        
        queue.enqueue(1)
        queue.enqueue(2)
        assert len(queue) == 2
    
    def test_bool_function(self):
        """Test __bool__ magic method."""
        queue = Queue[int]()
        assert not bool(queue)  # Empty queue is False
        
        queue.enqueue(1)
        assert bool(queue)  # Non-empty queue is True
    
    def test_string_representation(self):
        """Test __str__ method."""
        queue = Queue[int]()
        assert str(queue) == "Queue(front=[])"
        
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert str(queue) == "Queue(front=[1, 2, 3])"
    
    def test_repr(self):
        """Test __repr__ method."""
        queue = Queue[int](max_size=5)
        queue.enqueue(1)
        queue.enqueue(2)
        assert repr(queue) == "Queue([1, 2], max_size=5)"
    
    def test_iteration(self):
        """Test iteration over queue items."""
        queue = Queue[int]()
        items = [1, 2, 3, 4, 5]
        
        for item in items:
            queue.enqueue(item)
        
        # Iteration should preserve order (front to rear)
        for i, item in enumerate(queue):
            assert item == items[i]
        
        # Test that iteration doesn't modify queue
        assert queue.size() == 5
    
    def test_fifo_order(self):
        """Test FIFO (First-In-First-Out) order property."""
        queue = Queue[int]()
        
        # Enqueue numbers 1 to 100
        for i in range(1, 101):
            queue.enqueue(i)
        
        # Dequeue should return in same order
        for i in range(1, 101):
            assert queue.dequeue() == i
        
        assert queue.is_empty()
    
    def test_enqueue_dequeue_interleaved(self):
        """Test interleaved enqueue and dequeue operations."""
        queue = Queue[int]()
        
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1
        
        queue.enqueue(3)
        assert queue.dequeue() == 2
        
        queue.enqueue(4)
        queue.enqueue(5)
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.dequeue() == 5
        assert queue.is_empty()
    
    def test_type_safety(self):
        """Test type safety with different types."""
        queue_int = Queue[int]()
        queue_int.enqueue(10)
        # queue_int.enqueue("string")  # This would cause mypy error
        
        queue_str = Queue[str]()
        queue_str.enqueue("hello")
        
        queue_mixed = Queue[object]()
        queue_mixed.enqueue(10)
        queue_mixed.enqueue("string")
        queue_mixed.enqueue(3.14)
        
        assert queue_mixed.size() == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])