import pytest
from core.squares_sorted import sorted_squares

class TestSquaresSorted:
    def test_mixed_negatives(self):
        assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    
    def test_all_negative(self):
        assert sorted_squares([-5, -3, -2, -1]) == [1, 4, 9, 25]
    
    def test_all_positive(self):
        assert sorted_squares([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
    
    def test_with_zeros(self):
        assert sorted_squares([-2, -1, 0, 1, 2]) == [0, 1, 1, 4, 4]
    
    def test_single_element(self):
        assert sorted_squares([5]) == [25]
    
    def test_empty_array(self):
        assert sorted_squares([]) == []
    
    def test_duplicates(self):
        # CORRECTED: squares are [9,9,4,4,0,1,4] sorted → [0,1,4,4,4,9,9]
        assert sorted_squares([-3, -3, -2, -2, 0, 1, 2]) == [0, 1, 4, 4, 4, 9, 9]
    
    def test_large_negatives(self):
        assert sorted_squares([-10, -5, 0, 5, 10]) == [0, 25, 25, 100, 100]
    
    def test_all_same_negative(self):
        assert sorted_squares([-5, -5, -5, -5]) == [25, 25, 25, 25]
