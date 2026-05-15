"""
tests/test_reverse_linked_list.py
Unit tests for reverse linked list
"""
import pytest
from core.reverse_linked_list import (
    reverse_linked_list_iterative,
    reverse_linked_list_recursive,
    create_test_list,
    list_to_array
)


class TestReverseLinkedList:
    """Test suite for reverse linked list"""
    
    def test_reverse_empty_list(self):
        """Empty list should remain empty"""
        head = create_test_list([])
        
        reversed_iter = reverse_linked_list_iterative(head)
        reversed_rec = reverse_linked_list_recursive(head)
        
        assert list_to_array(reversed_iter) == []
        assert list_to_array(reversed_rec) == []
    
    def test_reverse_single_node(self):
        """Single node list should stay the same"""
        head = create_test_list([42])
        
        reversed_iter = reverse_linked_list_iterative(head)
        reversed_rec = reverse_linked_list_recursive(head)
        
        assert list_to_array(reversed_iter) == [42]
        assert list_to_array(reversed_rec) == [42]
    
    def test_reverse_two_nodes(self):
        """Two node list should swap"""
        head = create_test_list([1, 2])
        
        reversed_iter = reverse_linked_list_iterative(head)
        assert list_to_array(reversed_iter) == [2, 1]
        
        # Create fresh list for recursive test
        head2 = create_test_list([1, 2])
        reversed_rec = reverse_linked_list_recursive(head2)
        assert list_to_array(reversed_rec) == [2, 1]
    
    def test_reverse_multiple_nodes(self):
        """Should reverse completely"""
        head = create_test_list([1, 2, 3, 4, 5])
        
        reversed_iter = reverse_linked_list_iterative(head)
        assert list_to_array(reversed_iter) == [5, 4, 3, 2, 1]
    
    def test_reverse_odd_even_both(self):
        """Works for both odd and even lengths"""
        # Odd length
        head_odd = create_test_list([1, 2, 3])
        reversed_odd = reverse_linked_list_iterative(head_odd)
        assert list_to_array(reversed_odd) == [3, 2, 1]
        
        # Even length
        head_even = create_test_list([1, 2, 3, 4])
        reversed_even = reverse_linked_list_iterative(head_even)
        assert list_to_array(reversed_even) == [4, 3, 2, 1]
    
    def test_recursive_vs_iterative_same_result(self):
        """Both implementations should produce same result"""
        original = [1, 2, 3, 4, 5, 6, 7]
        
        head_iter = create_test_list(original.copy())
        head_rec = create_test_list(original.copy())
        
        result_iter = reverse_linked_list_iterative(head_iter)
        result_rec = reverse_linked_list_recursive(head_rec)
        
        assert list_to_array(result_iter) == list_to_array(result_rec)
        assert list_to_array(result_iter) == original[::-1]
    
    def test_preserves_values(self):
        """All original values should be preserved (just reordered)"""
        original = [10, 20, 30, 40, 50]
        head = create_test_list(original.copy())
        
        reversed_head = reverse_linked_list_iterative(head)
        result = list_to_array(reversed_head)
        
        assert set(result) == set(original)  # Same elements
        assert result == [50, 40, 30, 20, 10]  # Exactly reversed


if __name__ == "__main__":
    pytest.main([__file__, "-v"])