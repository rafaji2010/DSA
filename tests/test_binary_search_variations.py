# tests/test_binary_search_variations.py
import pytest
from core.binary_search_variations import (
    find_first_occurrence,
    find_last_occurrence,
    count_occurrences,
    find_first_or_last
)


class TestBinarySearchVariations:
    """Test cases for binary search variations."""
    
    # Test data
    NORMAL_ARRAY = [1, 2, 2, 2, 3, 4, 5, 5, 6]
    SINGLE_ARRAY = [1, 2, 3, 4]
    EMPTY_ARRAY = []
    ALL_DUPLICATES = [2, 2, 2, 2, 2]
    
    def test_first_occurrence_normal(self):
        assert find_first_occurrence(self.NORMAL_ARRAY, 2) == 1
    
    def test_first_occurrence_single(self):
        assert find_first_occurrence(self.SINGLE_ARRAY, 3) == 2
    
    def test_first_occurrence_not_found(self):
        assert find_first_occurrence(self.SINGLE_ARRAY, 5) == -1
    
    def test_first_occurrence_empty(self):
        assert find_first_occurrence(self.EMPTY_ARRAY, 5) == -1
    
    def test_first_occurrence_at_start(self):
        assert find_first_occurrence([2, 2, 2, 3, 4], 2) == 0
    
    def test_first_occurrence_at_end(self):
        assert find_first_occurrence([1, 2, 3, 3, 3], 3) == 2
    
    def test_first_occurrence_all_duplicates(self):
        assert find_first_occurrence(self.ALL_DUPLICATES, 2) == 0
    
    def test_last_occurrence_normal(self):
        assert find_last_occurrence(self.NORMAL_ARRAY, 2) == 3
    
    def test_last_occurrence_at_end(self):
        assert find_last_occurrence([1, 2, 3, 3, 3], 3) == 4
    
    def test_last_occurrence_all_duplicates(self):
        assert find_last_occurrence(self.ALL_DUPLICATES, 2) == 4
    
    def test_last_occurrence_not_found(self):
        assert find_last_occurrence(self.SINGLE_ARRAY, 10) == -1
    
    def test_count_occurrences_normal(self):
        assert count_occurrences(self.NORMAL_ARRAY, 2) == 3
    
    def test_count_occurrences_not_found(self):
        assert count_occurrences(self.NORMAL_ARRAY, 10) == 0
    
    def test_count_occurrences_single(self):
        assert count_occurrences(self.SINGLE_ARRAY, 3) == 1
    
    def test_count_occurrences_all_duplicates(self):
        assert count_occurrences(self.ALL_DUPLICATES, 2) == 5
    
    def test_unified_first(self):
        assert find_first_or_last(self.NORMAL_ARRAY, 2, find_first=True) == 1
    
    def test_unified_last(self):
        assert find_first_or_last(self.NORMAL_ARRAY, 2, find_first=False) == 3


# Run with: pytest tests/test_binary_search_variations.py -v