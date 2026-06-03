"""
benchmarks/hash_table_performance.py
Compare Hash Table performance with Python dict
"""

import time
import sys
sys.path.insert(0, '/mnt/d/DSA')

from core.hash_tables.hash_table import HashTable


def test_performance():
    """Compare our HashTable with Python's dict"""
    
    sizes = [1000, 5000, 10000, 20000]
    
    print("=" * 70)
    print(f"{'Size':<10} {'Dict Insert':<15} {'HT Insert':<15} {'Dict Get':<15} {'HT Get':<15}")
    print("=" * 70)
    
    for size in sizes:
        # Test Python dict
        start = time.perf_counter()
        d = {}
        for i in range(size):
            d[f"key{i}"] = i
        dict_insert = time.perf_counter() - start
        
        start = time.perf_counter()
        for i in range(size):
            _ = d[f"key{i}"]
        dict_get = time.perf_counter() - start
        
        # Test our HashTable
        ht = HashTable[str, int]()
        start = time.perf_counter()
        for i in range(size):
            ht.put(f"key{i}", i)
        ht_insert = time.perf_counter() - start
        
        start = time.perf_counter()
        for i in range(size):
            _ = ht.get(f"key{i}")
        ht_get = time.perf_counter() - start
        
        print(f"{size:<10} {dict_insert:<15.4f} {ht_insert:<15.4f} {dict_get:<15.4f} {ht_get:<15.4f}")
    
    print("\n" + "=" * 70)
    print("NOTE: Python dict is implemented in C (much faster)!")
    print("Our implementation demonstrates the ALGORITHM, not production speed.")
    print("=" * 70)


if __name__ == "__main__":
    test_performance()
