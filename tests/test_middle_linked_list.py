"""
tests/test_middle_linked_list.py
Unit tests for middle of linked list
"""
import pytest
from core.middle_linked_list import (
    find_middle_tortoise_hare,
    find_middle_two_pass,
    create_linked_list
)


class TestMiddleLinkedList:
    """Test suite for finding middle of linked list"""
    
    def test_empty_list(self):
        """Empty list should return None"""
        head = create_linked_list([])
        assert find_middle_tortoise_hare(head) is None
        assert find_middle_two_pass(head) is None
    
    def test_single_node(self):
        """Single node list should return that node"""
        head = create_linked_list([42])
        
        middle1 = find_middle_tortoise_hare(head)
        middle2 = find_middle_two_pass(head)
        
        assert middle1.value == 42
        assert middle2.value == 42
    
    def test_two_nodes(self):
        """Two nodes should return second node (index 1)"""
        head = create_linked_list([1, 2])
        
        middle1 = find_middle_tortoise_hare(head)
        middle2 = find_middle_two_pass(head)
        
        assert middle1.value == 2
        assert middle2.value == 2
    
    def test_odd_length(self):
        """Odd length: [1,2,3,4,5] → middle = 3"""
        head = create_linked_list([1, 2, 3, 4, 5])
        
        middle = find_middle_tortoise_hare(head)
        assert middle.value == 3
    
    def test_even_length(self):
        """Even length: [1,2,3,4] → middle = 3 (second middle)"""
        head = create_linked_list([1, 2, 3, 4])
        
        middle = find_middle_tortoise_hare(head)
        assert middle.value == 3
    
    def test_large_odd(self):
        """Test with 99 nodes (odd) → middle at index 49"""
        values = list(range(1, 100))  # 1 to 99
        head = create_linked_list(values)
        
        middle = find_middle_tortoise_hare(head)
        # Middle of 99 nodes is 50 (1-indexed) or value 50
        assert middle.value == 50
    
    def test_large_even(self):
        """Test with 100 nodes (even) → middle at index 50 (second middle)"""
        values = list(range(1, 101))  # 1 to 100
        head = create_linked_list(values)
        
        middle = find_middle_tortoise_hare(head)
        # Second middle of 100 nodes is 51 (1-indexed) or value 51
        assert middle.value == 51
    
    def test_all_approaches_same(self):
        """All three approaches should return same node"""
        values = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        head = create_linked_list(values)
        
        result1 = find_middle_tortoise_hare(head)
        
        # Create fresh lists for other approaches
        head2 = create_linked_list(values)
        result2 = find_middle_two_pass(head2)
        
        head3 = create_linked_list(values)
        from core.middle_linked_list import find_middle_brute_force
        result3 = find_middle_brute_force(head3)
        
        assert result1.value == result2.value == result3.value
        assert result1.value == 50  # Middle of 9 nodes


if __name__ == "__main__":
    pytest.main([__file__, "-v"])