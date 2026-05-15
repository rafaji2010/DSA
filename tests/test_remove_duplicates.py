import pytest
from core.remove_duplicates import remove_duplicates

class TestRemoveDuplicates:
    def test_normal_case(self):
        arr = [1, 1, 2, 2, 3, 4, 4, 5]
        length = remove_duplicates(arr)
        assert length == 5
        assert arr[:length] == [1, 2, 3, 4, 5]
    
    def test_no_duplicates(self):
        arr = [1, 2, 3, 4, 5]
        length = remove_duplicates(arr)
        assert length == 5
        assert arr[:length] == [1, 2, 3, 4, 5]
    
    def test_all_duplicates(self):
        arr = [1, 1, 1, 1, 1]
        length = remove_duplicates(arr)
        assert length == 1
        assert arr[:length] == [1]
    
    def test_single_element(self):
        arr = [1]
        length = remove_duplicates(arr)
        assert length == 1
        assert arr[:length] == [1]
    
    def test_empty_array(self):
        arr = []
        length = remove_duplicates(arr)
        assert length == 0
        assert arr == []
    
    def test_two_elements_same(self):
        arr = [1, 1]
        length = remove_duplicates(arr)
        assert length == 1
        assert arr[:length] == [1]
    
    def test_two_elements_different(self):
        arr = [1, 2]
        length = remove_duplicates(arr)
        assert length == 2
        assert arr[:length] == [1, 2]
