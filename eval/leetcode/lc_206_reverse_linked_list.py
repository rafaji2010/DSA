"""
LeetCode 206 - Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Time: O(n) - visit each node once
Space: O(1) - iterative
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """Iterative solution - three pointers"""
        prev = None
        current = head
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        return prev
    
    def reverseListRecursive(self, head: ListNode | None) -> ListNode | None:
        """Recursive solution"""
        if not head or not head.next:
            return head
        
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        
        return new_head

def create_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def list_to_array(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

if __name__ == "__main__":
    s = Solution()
    
    # Test iterative
    head = create_list([1,2,3,4,5])
    reversed_head = s.reverseList(head)
    assert list_to_array(reversed_head) == [5,4,3,2,1]
    
    # Test recursive
    head2 = create_list([1,2,3,4,5])
    reversed_head2 = s.reverseListRecursive(head2)
    assert list_to_array(reversed_head2) == [5,4,3,2,1]
    
    # Edge cases
    head3 = create_list([1])
    reversed_head3 = s.reverseList(head3)
    assert list_to_array(reversed_head3) == [1]
    
    print("✅ All tests passed for LeetCode 206!")
