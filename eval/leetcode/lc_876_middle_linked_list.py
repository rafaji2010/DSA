"""
LeetCode 876 - Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

Time: O(n) - single pass with tortoise and hare
Space: O(1) - two pointers
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

def create_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

if __name__ == "__main__":
    s = Solution()
    
    # Odd length - middle should be 3
    head1 = create_list([1,2,3,4,5])
    middle1 = s.middleNode(head1)
    assert middle1.val == 3
    
    # Even length - middle should be second middle (4)
    head2 = create_list([1,2,3,4,5,6])
    middle2 = s.middleNode(head2)
    assert middle2.val == 4
    
    # Single node
    head3 = create_list([1])
    middle3 = s.middleNode(head3)
    assert middle3.val == 1
    
    # Two nodes - should return second node
    head4 = create_list([1,2])
    middle4 = s.middleNode(head4)
    assert middle4.val == 2
    
    print("✅ All tests passed for LeetCode 876!")
