"""
tests/hash_tables/test_hash_table.py
Comprehensive tests for Hash Table implementation
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.hash_tables.hash_table import HashTable, hash_polynomial, hash_sum_ascii


class TestHashTableBasic:
    """Basic functionality tests"""
    
    def test_put_and_get(self):
        ht = HashTable[str, int]()
        ht.put("one", 1)
        ht.put("two", 2)
        ht.put("three", 3)
        
        assert ht.get("one") == 1
        assert ht.get("two") == 2
        assert ht.get("three") == 3
        assert ht.get("four") is None
    
    def test_update_existing(self):
        ht = HashTable[str, str]()
        ht.put("key", "value1")
        assert ht.get("key") == "value1"
        
        ht.put("key", "value2")
        assert ht.get("key") == "value2"
        assert ht.size() == 1  # Size shouldn't change
    
    def test_contains(self):
        ht = HashTable[str, int]()
        ht.put("apple", 10)
        
        assert ht.contains("apple") is True
        assert "apple" in ht  # __contains__ magic method
        assert "banana" not in ht
    
    def test_remove(self):
        ht = HashTable[str, int]()
        ht.put("a", 1)
        ht.put("b", 2)
        ht.put("c", 3)
        
        assert ht.remove("b") is True
        assert ht.get("b") is None
        assert ht.size() == 2
        
        assert ht.remove("x") is False
        assert ht.size() == 2


class TestHashTableMagicMethods:
    """Test Pythonic interface"""
    
    def test_dict_like_syntax(self):
        ht = HashTable[str, int]()
        
        # __setitem__
        ht["one"] = 1
        ht["two"] = 2
        
        # __getitem__
        assert ht["one"] == 1
        assert ht["two"] == 2
        
        # __delitem__
        del ht["one"]
        assert "one" not in ht
        
        # __len__
        assert len(ht) == 1
    
    def test_key_error(self):
        ht = HashTable[str, int]()
        
        with pytest.raises(KeyError):
            value = ht["missing"]


class TestHashTableResizing:
    """Test dynamic resizing behavior"""
    
    def test_resize_trigger(self):
        ht = HashTable[str, int](initial_capacity=4)
        
        # Insert 3 items (load factor = 3/4 = 0.75)
        for i in range(3):
            ht.put(f"key{i}", i)
        
        assert ht.capacity() == 4
        
        # 4th item triggers resize (load factor > 0.75)
        ht.put("key3", 3)
        
        assert ht.capacity() == 8  # Should have doubled!
        assert ht.size() == 4
        # All keys should still be accessible
        for i in range(4):
            assert ht.get(f"key{i}") == i
    
    def test_multiple_resizes(self):
        ht = HashTable[int, int](initial_capacity=2)
        
        # Capacity progression: 2 → 4 → 8 → 16
        capacities = []
        for i in range(20):
            ht.put(i, i * 10)
            capacities.append(ht.capacity())
        
        assert 8 in capacities
        assert 16 in capacities


class TestHashTableDataTypes:
    """Test with different key/value types"""
    
    def test_integer_keys(self):
        ht = HashTable[int, str]()
        ht[100] = "hundred"
        ht[200] = "two hundred"
        
        assert ht[100] == "hundred"
        assert ht.get(200) == "two hundred"
    
    def test_tuple_keys(self):
        ht = HashTable[tuple, str]()
        ht[(1, 2)] = "point 1,2"
        ht[(3, 4)] = "point 3,4"
        
        assert ht[(1, 2)] == "point 1,2"
        assert (1, 2) in ht
    
    def test_mixed_types(self):
        ht = HashTable[object, object]()
        ht[1] = "integer key"
        ht["string"] = 42
        ht[(1, 2)] = [1, 2, 3]
        
        assert ht[1] == "integer key"
        assert ht["string"] == 42
        assert ht[(1, 2)] == [1, 2, 3]


class TestHashTableEdgeCases:
    """Test edge cases and boundary conditions"""
    
    def test_empty_table(self):
        ht = HashTable[str, int]()
        
        assert ht.size() == 0
        assert ht.capacity() == 16
        assert ht.load_factor() == 0.0
        assert ht.get("anything") is None
        assert "anything" not in ht
    
    def test_large_number_of_items(self):
        ht = HashTable[int, int]()
        n = 1000
        
        for i in range(n):
            ht[i] = i * 2
        
        assert ht.size() == n
        assert ht.capacity() >= n  # Should have resized appropriately
        
        for i in range(n):
            assert ht[i] == i * 2
    
    def test_same_hash_collision_handling(self):
        """Test when multiple keys have the same hash"""
        # Use custom hash that forces collisions
        def bad_hash(key, capacity):
            return 0  # All keys go to bucket 0!
        
        ht = HashTable[str, str](initial_capacity=4, custom_hash=bad_hash)
        
        for i in range(10):
            ht[f"key{i}"] = f"value{i}"
        
        assert ht.size() == 10
        # All items should be in bucket 0
        assert len(ht._buckets[0]) == 10
        
        # But we should still find all items!
        for i in range(10):
            assert ht[f"key{i}"] == f"value{i}"


class TestHashTableCollectionMethods:
    """Test keys(), values(), items() methods"""
    
    def test_keys(self):
        ht = HashTable[str, int]()
        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3
        
        keys = ht.keys()
        assert len(keys) == 3
        assert set(keys) == {"a", "b", "c"}
    
    def test_values(self):
        ht = HashTable[str, int]()
        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3
        
        values = ht.values()
        assert len(values) == 3
        assert sorted(values) == [1, 2, 3]
    
    def test_items(self):
        ht = HashTable[str, int]()
        ht["a"] = 1
        ht["b"] = 2
        
        items = ht.items()
        assert len(items) == 2
        assert ("a", 1) in items
        assert ("b", 2) in items


class TestHashTableClear:
    """Test clear functionality"""
    
    def test_clear(self):
        ht = HashTable[str, int]()
        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3
        
        assert ht.size() == 3
        
        ht.clear()
        
        assert ht.size() == 0
        assert ht.get("a") is None
        assert "a" not in ht
        assert len(ht._buckets) == ht.capacity()  # Capacity unchanged


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
