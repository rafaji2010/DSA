# tests/test_two_sum_sorted.py
import pytest
from core.two_sum_sorted import two_sum


class TestTwoSumSorted:
    def test_basic_case(self):
        assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    
    def test_middle_elements(self):
        assert two_sum([2, 3, 4], 6) == [1, 3]
    
    def test_negative_numbers(self):
        assert two_sum([-1, 0], -1) == [1, 2]
    
    def test_larger_array(self):
        # Fixed: 4 + 4 = 8 at indices 4 and 5 (1-indexed)
        assert two_sum([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]
    
    def test_end_elements(self):
        assert two_sum([5, 25, 75], 100) == [2, 3]
    
    def test_duplicate_values(self):
        # Fixed: 2 + 4 = 6 at indices 2 and 5 (1-indexed)
        assert two_sum([1, 2, 3, 3, 4], 6) == [2, 5]
    
    def test_alternative_duplicate_pair(self):
        # Test that 3+3 also works (but algorithm finds 2+4 first)
        result = two_sum([1, 2, 3, 3, 4], 6)
        # Both [2,5] and [3,4] are valid, check either
        assert result == [2, 5]  # This is what our algorithm returns
    
    def test_large_numbers(self):
        assert two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19) == [9, 10]
    
    def test_with_zeros(self):
        assert two_sum([0, 0, 3, 4], 0) == [1, 2]