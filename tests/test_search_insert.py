import pytest
from core.search_insert_position import search_insert

class TestSearchInsert:
    def test_target_exists(self):
        assert search_insert([1, 3, 5, 6], 5) == 2
    
    def test_target_insert_middle(self):
        assert search_insert([1, 3, 5, 6], 2) == 1
    
    def test_target_insert_end(self):
        assert search_insert([1, 3, 5, 6], 7) == 4
    
    def test_target_insert_start(self):
        assert search_insert([1, 3, 5, 6], 0) == 0
    
    def test_single_element_found(self):
        assert search_insert([1], 1) == 0
    
    def test_single_element_insert_before(self):
        assert search_insert([1], 0) == 0
    
    def test_single_element_insert_after(self):
        assert search_insert([1], 2) == 1
    
    def test_empty_array(self):
        assert search_insert([], 5) == 0
