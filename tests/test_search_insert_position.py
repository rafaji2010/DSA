# tests/test_search_insert_position.py
"""Tests for Search Insert Position (LeetCode 35)."""

import pytest
from core.search_insert_position import search_insert, search_insert_recursive


class TestSearchInsertPosition:
    """Test both iterative and recursive implementations."""
    
    # Test cases as (nums, target, expected)
    TEST_CASES = [
        # Basic cases
        ([1, 3, 5, 6], 5, 2),   # Target exists
        ([1, 3, 5, 6], 2, 1),   # Insert in middle
        ([1, 3, 5, 6], 7, 4),   # Insert at end
        ([1, 3, 5, 6], 0, 0),   # Insert at beginning
        
        # Single element arrays
        ([1], 1, 0),             # Target exists
        ([1], 0, 0),             # Insert before
        ([1], 2, 1),             # Insert after
        
        # Empty array
        ([], 5, 0),              # Insert into empty array
        
        # Larger arrays
        ([1, 2, 3, 4, 5], 3, 2),   # Target exists in middle
        ([1, 2, 3, 4, 5], 6, 5),   # Insert at end
        ([1, 2, 3, 4, 5], 0, 0),   # Insert at beginning
        
        # Arrays with duplicates (though problem guarantees unique)
        # ([1, 2, 2, 2, 3], 2, 1),   # REMOVED - LeetCode guarantees no duplicates
        # ([1, 2, 2, 2, 3], 4, 5),   # REMOVED - LeetCode guarantees no duplicates
        
        # Negative numbers
        ([-5, -3, -1, 0, 2], -2, 2),   # Insert between -3 and -1
        ([-5, -3, -1, 0, 2], -6, 0),   # Insert at beginning
        ([-5, -3, -1, 0, 2], 3, 5),    # Insert at end
    ]
    
    def test_iterative_implementation(self):
        """Test search_insert (iterative binary search)."""
        for nums, target, expected in self.TEST_CASES:
            result = search_insert(nums, target)
            assert result == expected, \
                f"search_insert({nums}, {target}) = {result}, expected {expected}"
    
    def test_recursive_implementation(self):
        """Test search_insert_recursive (recursive binary search)."""
        for nums, target, expected in self.TEST_CASES:
            result = search_insert_recursive(nums, target)
            assert result == expected, \
                f"search_insert_recursive({nums}, {target}) = {result}, expected {expected}"
    
    def test_both_implementations_match(self):
        """Ensure iterative and recursive return same results."""
        for nums, target, _ in self.TEST_CASES:
            iterative_result = search_insert(nums, target)
            recursive_result = search_insert_recursive(nums, target)
            assert iterative_result == recursive_result, \
                f"Mismatch for {nums}, target={target}: " \
                f"iterative={iterative_result}, recursive={recursive_result}"
    
    def test_performance_comparison(self):
        """Compare performance of both implementations."""
        import time
        
        # Large sorted array
        large_nums = list(range(10000))
        
        # Test finding middle element
        start = time.perf_counter()
        iterative_result = search_insert(large_nums, 5000)
        iterative_time = time.perf_counter() - start
        
        start = time.perf_counter()
        recursive_result = search_insert_recursive(large_nums, 5000)
        recursive_time = time.perf_counter() - start
        
        assert iterative_result == recursive_result == 5000
        
        print(f"\nPerformance comparison (n=10,000):")
        print(f"  Iterative: {iterative_time:.6f}s")
        print(f"  Recursive: {recursive_time:.6f}s")
        
        # Recursive is slightly slower due to function call overhead
        # but both are O(log n)


# Edge case tests specifically for insertion logic
class TestInsertionLogic:
    """Test the insertion position logic in detail."""
    
    def test_insertion_position_visualization(self):
        """Visual test to understand insertion positions."""
        nums = [1, 3, 5, 7, 9]
        
        test_data = [
            (0, "before everything"),
            (1, "exactly at start (exists)"),
            (2, "between 1 and 3"),
            (3, "exactly at index 1 (exists)"),
            (4, "between 3 and 5"),
            (5, "exactly at index 2 (exists)"),
            (6, "between 5 and 7"),
            (7, "exactly at index 3 (exists)"),
            (8, "between 7 and 9"),
            (9, "exactly at index 4 (exists)"),
            (10, "after everything"),
        ]
        
        print("\n" + "=" * 60)
        print("Insertion Position Visualization")
        print("=" * 60)
        print(f"Array: {nums}")
        
        for target, description in test_data:
            pos = search_insert(nums, target)
            
            # Visual representation
            if pos < len(nums) and nums[pos] == target:
                arrow = f"→ {target} EXISTS at index {pos}"
            elif pos == 0:
                arrow = f"→ {target} inserted BEFORE all elements (index 0)"
            elif pos == len(nums):
                arrow = f"→ {target} inserted AFTER all elements (index {pos})"
            else:
                arrow = f"→ {target} inserted BETWEEN {nums[pos-1]} and {nums[pos]} (index {pos})"
            
            print(f"  target={target:2d}: position={pos} {arrow}")