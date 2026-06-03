"""
LeetCode 21 - Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Time: O(m + n) - traverse both lists once
Space: O(1) - only pointers
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative solution with dummy node.
        """
        dummy = ListNode(0)  # Dummy node simplifies edge cases
        current = dummy
        
        # While both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        return dummy.next
    
    def mergeTwoListsRecursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive solution - elegant but uses O(m+n) stack space.
        """
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Recursive case
        if list1.val <= list2.val:
            list1.next = self.mergeTwoListsRecursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoListsRecursive(list1, list2.next)
            return list2


# Helper functions for testing
def create_list(values):
    """Convert Python list to linked list."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def list_to_array(head):
    """Convert linked list to Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    s = Solution()
    
    print("=" * 50)
    print("Testing Merge Two Sorted Lists")
    print("=" * 50)
    
    # Test 1: Normal case
    list1 = create_list([1, 2, 4])
    list2 = create_list([1, 3, 4])
    merged = s.mergeTwoLists(list1, list2)
    print(f"list1: [1,2,4]")
    print(f"list2: [1,3,4]")
    print(f"merged: {list_to_array(merged)}")
    assert list_to_array(merged) == [1, 1, 2, 3, 4, 4]
    print("✅ Test 1 passed!")
    
    # Test 2: Empty lists
    list1 = create_list([])
    list2 = create_list([])
    merged = s.mergeTwoLists(list1, list2)
    print(f"\nlist1: []")
    print(f"list2: []")
    print(f"merged: {list_to_array(merged)}")
    assert list_to_array(merged) == []
    print("✅ Test 2 passed!")
    
    # Test 3: One empty list
    list1 = create_list([])
    list2 = create_list([0])
    merged = s.mergeTwoLists(list1, list2)
    print(f"\nlist1: []")
    print(f"list2: [0]")
    print(f"merged: {list_to_array(merged)}")
    assert list_to_array(merged) == [0]
    print("✅ Test 3 passed!")
    
    # Test 4: Recursive version
    list1 = create_list([1, 2, 4])
    list2 = create_list([1, 3, 4])
    merged_rec = s.mergeTwoListsRecursive(list1, list2)
    print(f"\nRecursive merge: {list_to_array(merged_rec)}")
    assert list_to_array(merged_rec) == [1, 1, 2, 3, 4, 4]
    print("✅ Recursive version passed!")
    
    print("\n" + "=" * 50)
    print("✅ All tests passed!")
    print("=" * 50)