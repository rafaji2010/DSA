"""
LeetCode 100 - Same Tree
https://leetcode.com/problems/same-tree/

Time: O(n) - visit each node once
Space: O(h) - recursion stack depth
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are identical.
        
        Base cases:
        - Both None → True
        - One None, one not → False
        - Values different → False
        - Recursively check left and right subtrees
        """
        # Both empty
        if not p and not q:
            return True
        
        # One empty, one not
        if not p or not q:
            return False
        
        # Values differ
        if p.val != q.val:
            return False
        
        # Recursively check children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    s = Solution()
    
    # Test: [1,2,3] and [1,2,3]
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert s.isSameTree(p, q) == True
    
    # Test: [1,2] and [1,null,2]
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    assert s.isSameTree(p, q) == False
    
    print("✅ All tests passed!")\
    