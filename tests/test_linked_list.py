"""
tests/test_linked_list.py
Comprehensive tests for LinkedList operations
"""
import pytest
from core.linked_list import LinkedList


class TestLinkedList:
    """Test suite for LinkedList"""
    
    def setup_method(self):
        """Create a fresh list before each test"""
        self.ll = LinkedList[int]()
    
    def test_search_empty(self):
        """Search on empty list should return False"""
        assert self.ll.search(10) is False
    
    def test_search_existing(self):
        """Search should find existing values"""
        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        assert self.ll.search(20) is True
        assert self.ll.search(10) is True
        assert self.ll.search(30) is True
    
    def test_search_missing(self):
        """Search should not find missing values"""
        self.ll.append(10)
        self.ll.append(20)
        assert self.ll.search(99) is False
    
    def test_find_index(self):
        """find_index should return correct positions"""
        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        assert self.ll.find_index(10) == 0
        assert self.ll.find_index(20) == 1
        assert self.ll.find_index(30) == 2
        assert self.ll.find_index(99) == -1
    
    def test_delete_head(self):
        """Deleting head should work"""
        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        
        assert self.ll.delete(10) is True
        assert self.ll.to_list() == [20, 30]
        assert self.ll.size() == 2
    
    def test_delete_middle(self):
        """Deleting from middle should work"""
        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        
        assert self.ll.delete(20) is True
        assert self.ll.to_list() == [10, 30]
        assert self.ll.size() == 2
    
    def test_delete_tail(self):
        """Deleting tail should work"""
        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        
        assert self.ll.delete(30) is True
        assert self.ll.to_list() == [10, 20]
        assert self.ll.size() == 2
    
    def test_delete_only_node(self):
        """Deleting the only node should empty list"""
        self.ll.append(10)
        assert self.ll.delete(10) is True
        assert self.ll.size() == 0
        assert self.ll.to_list() == []
    
    def test_delete_missing(self):
        """Delete non-existent value should return False"""
        self.ll.append(10)
        self.ll.append(20)
        assert self.ll.delete(99) is False
        assert self.ll.size() == 2
    
    def test_delete_at_index(self):
        """Delete by index should work"""
        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        
        value = self.ll.delete_at_index(1)
        assert value == 20
        assert self.ll.to_list() == [10, 30]
        assert self.ll.size() == 2
    
    def test_delete_at_index_head(self):
        """Delete at index 0 should work"""
        self.ll.append(10)
        self.ll.append(20)
        
        value = self.ll.delete_at_index(0)
        assert value == 10
        assert self.ll.to_list() == [20]
    
    def test_delete_at_index_invalid(self):
        """Invalid index should raise IndexError"""
        self.ll.append(10)
        
        with pytest.raises(IndexError):
            self.ll.delete_at_index(5)
        
        with pytest.raises(IndexError):
            self.ll.delete_at_index(-1)
    
    def test_multiple_operations(self):
        """Test sequence of operations"""
        # Add some values
        self.ll.append(5)
        self.ll.append(10)
        self.ll.prepend(1)
        self.ll.append(15)
        assert self.ll.to_list() == [1, 5, 10, 15]
        
        # Delete from middle
        assert self.ll.delete(10) is True
        assert self.ll.to_list() == [1, 5, 15]
        
        # Delete from head
        assert self.ll.delete(1) is True
        assert self.ll.to_list() == [5, 15]
        
        # Search
        assert self.ll.search(5) is True
        assert self.ll.search(99) is False
        assert self.ll.find_index(15) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])