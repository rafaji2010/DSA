"""
Debug version - only test recursive merge
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoListsRecursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        breakpoint()  # ← PDB STOPS HERE!
        
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoListsRecursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoListsRecursive(list1, list2.next)
            return list2


def create_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    s = Solution()
    
    list1 = create_list([1, 2, 4])
    list2 = create_list([1, 3, 4])
    
    print(f"Merging: {list_to_array(list1)} + {list_to_array(list2)}")
    result = s.mergeTwoListsRecursive(list1, list2)
    print(f"Result: {list_to_array(result)}")
