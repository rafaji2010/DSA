"""
benchmarks/amortized_demo.py
Demonstrate amortized O(1) behavior of list.append()
"""
import time
import sys


def demonstrate_amortization():
    """Show that most appends are fast, occasional are slow"""
    
    my_list = []
    initial_capacity = sys.getsizeof(my_list)
    
    print("Tracking append performance as list grows:")
    print("-" * 60)
    
    for i in range(1, 100):
        # Measure this append
        start = time.perf_counter_ns()
        my_list.append(i)
        elapsed = time.perf_counter_ns() - start
        
        # Check if capacity changed
        current_capacity = sys.getsizeof(my_list)
        
        if elapsed > 1000:  # Slow append (>1 microsecond)
            print(f"Append {i:3d} | Time: {elapsed:6d} ns | CAPACITY GROW! (O(n) copy)")
        else:
            print(f"Append {i:3d} | Time: {elapsed:6d} ns | Fast O(1)")
        
        # Small pause to see output
        if i % 20 == 0:
            print("-" * 60)
            time.sleep(0.5)


def compare_with_linked_list():
    """Compare amortized array append vs linked list append"""
    from core.linked_list import LinkedList
    
    n = 10000
    
    # Array append
    arr = []
    start = time.perf_counter()
    for i in range(n):
        arr.append(i)
    arr_time = time.perf_counter() - start
    
    # Linked list append (always O(n) - no amortization!)
    ll = LinkedList()
    start = time.perf_counter()
    for i in range(n):
        ll.append(i)  # Must traverse to end each time!
    ll_time = time.perf_counter() - start
    
    print(f"\nComparison for {n} appends:")
    print(f"Array (amortized O(1)):      {arr_time:.4f} seconds")
    print(f"Linked List (true O(n)):     {ll_time:.4f} seconds")
    print(f"Ratio: Linked list is {ll_time/arr_time:.1f}x slower")


if __name__ == "__main__":
    print("DEMONSTRATING AMORTIZED O(1)\n")
    demonstrate_amortization()
    print("\n" + "="*60)
    compare_with_linked_list()