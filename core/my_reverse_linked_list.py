"""
core/my_reverse_linked_list.py
Write reverse linked list 
"""

from__future__ import annotations
from typing import Optional, TypVar, Generic

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a linked list iteratively.
    Return new head.
    """
    # YOUR CODE HERE - three pointers: prev, current, next_temp
    prev: Optional[Node[T]] = None
    current = head

    while current is not None:

        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev
    


def reverse_linked_list_recursive(head):
    """
    Reverse a linked list recursively.
    Return new head.
    """
     if head is None or head.next == None:
        return head

    new_head = reverse_linked_list_recursive(head.next)

    head.next.next = head

    head.next = None
