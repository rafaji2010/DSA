"""
LeetCode 141 - Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Time: O(n) - each node visited at most twice
Space: O(1) - only two pointers

Algorithm: Floyd's Cycle Detection (Tortoise and Hare)
- Slow pointer moves 1 step
- Fast pointer moves 2 steps
- If they meet → cycle exists
- If fast reaches None → no cycle
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Floyd's Cycle Detection Algorithm
        """
        # Empty list or single node → no cycle
        if not head or not head.next:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            if slow == fast:          # They met → cycle exists!
                return True
        
        return False  # Fast reached end → no cycle
    
    def hasCycleHashSet(self, head: Optional[ListNode]) -> bool:
        """
        Alternative: Use hash set to track visited nodes.
        Time: O(n), Space: O(n) - stores visited nodes.
        """
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        
        return False


# Helper functions for testing
def create_list_with_cycle(values, pos):
    """
    Create linked list with cycle.
    pos = -1 → no cycle
    pos = index where tail connects back (0-indexed)
    """
    if not values:
        return None
    
    # Create nodes
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Create cycle if specified
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    
    return nodes[0]


def create_list_no_cycle(values):
    """Create linked list without cycle"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_list(head, limit=10):
    """Print list (limited to prevent infinite loop)"""
    values = []
    current = head
    count = 0
    while current and count < limit:
        values.append(str(current.val))
        current = current.next
        count += 1
    if current:  # Cycle detected
        values.append("... (cycle)")
    return " → ".join(values)


if __name__ == "__main__":
    s = Solution()
    
    print("=" * 60)
    print("Testing Linked List Cycle Detection")
    print("=" * 60)
    
    # Test 1: No cycle
    print("\n--- Test 1: No cycle ---")
    head1 = create_list_no_cycle([1, 2, 3, 4])
    print(f"List: {print_list(head1)}")
    result1 = s.hasCycle(head1)
    print(f"Has cycle? {result1}")
    assert result1 == False
    print("✅ Test 1 passed!")
    
    # Test 2: With cycle (tail connects to index 1 = node 2)
    print("\n--- Test 2: With cycle ---")
    head2 = create_list_with_cycle([1, 2, 3, 4], pos=1)
    print(f"List: {print_list(head2, 10)}")
    print("Cycle: tail (4) connects back to node 2")
    result2 = s.hasCycle(head2)
    print(f"Has cycle? {result2}")
    assert result2 == True
    print("✅ Test 2 passed!")
    
    # Test 3: Single node, no cycle
    print("\n--- Test 3: Single node ---")
    head3 = create_list_no_cycle([1])
    print(f"List: {print_list(head3)}")
    result3 = s.hasCycle(head3)
    print(f"Has cycle? {result3}")
    assert result3 == False
    print("✅ Test 3 passed!")
    
    # Test 4: Two nodes with cycle (tail connects to head)
    print("\n--- Test 4: Two nodes with cycle ---")
    head4 = create_list_with_cycle([1, 2], pos=0)
    print(f"List: {print_list(head4, 10)}")
    print("Cycle: tail (2) connects back to head (1)")
    result4 = s.hasCycle(head4)
    print(f"Has cycle? {result4}")
    assert result4 == True
    print("✅ Test 4 passed!")
    
    # Test 5: Empty list
    print("\n--- Test 5: Empty list ---")
    head5 = None
    print(f"List: None")
    result5 = s.hasCycle(head5)
    print(f"Has cycle? {result5}")
    assert result5 == False
    print("✅ Test 5 passed!")
    
    # Test 6: Hash set version
    print("\n--- Test 6: Hash set version (alternative approach) ---")
    head6 = create_list_with_cycle([1, 2, 3, 4, 5], pos=2)
    result6 = s.hasCycleHashSet(head6)
    print(f"Hash set detects cycle: {result6}")
    assert result6 == True
    print("✅ Test 6 passed!")
    
    print("\n" + "=" * 60)
    print("✅ All tests passed!")
    print("=" * 60)
    
    # Complexity analysis
    print("\n📊 Complexity Analysis:")
    print("   Floyd's Algorithm (hasCycle):")
    print("   - Time: O(n) - each node visited at most twice")
    print("   - Space: O(1) - only two pointers")
    print("   Hash Set approach (hasCycleHashSet):")
    print("   - Time: O(n) - one pass through list")
    print("   - Space: O(n) - stores visited nodes")