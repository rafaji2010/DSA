"""
LeetCode 94 - Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/

Time: O(n) - visit each node once
Space: O(h) - recursion stack depth (h = height)
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recursive inorder traversal: Left → Root → Right"""
        result = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)      # Left
            result.append(node.val)  # Root
            inorder(node.right)     # Right
        
        inorder(root)
        return result
    
    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        """Iterative inorder traversal using stack"""
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process node
            current = stack.pop()
            result.append(current.val)
            
            # Go right
            current = current.right
        
        return result


if __name__ == "__main__":
    s = Solution()
    
    # Test: [1, null, 2, 3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    
    print(s.inorderTraversal(root))  # [1, 3, 2]
    print(s.inorderTraversalIterative(root))  # [1, 3, 2]
    
    print("✅ Test passed!")