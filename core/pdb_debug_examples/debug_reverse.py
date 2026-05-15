"""
core/pdb_debug_examples/debug_reverse.py
Step through reverse with pdb to understand pointer manipulation
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reverse_linked_list import create_test_list, reverse_linked_list_iterative


def debug_with_pdb():
    """Interactive pdb session to watch reversal"""
    head = create_test_list([1, 2, 3, 4, 5])
    
    # Place breakpoint here
    breakpoint()  # ← pdb will stop here
    
    # Now in pdb, you can:
    # n (next) - step through code
    # s (step) - step into functions
    # p variable (print variable)
    # pp variable (pretty print)
    # c (continue to next breakpoint)
    # q (quit)
    
    reversed_head = reverse_linked_list_iterative(head)
    return reversed_head


if __name__ == "__main__":
    result = debug_with_pdb()
    print("Reversal complete!")