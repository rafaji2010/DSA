"""
LeetCode 226 - Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Time: O(n) - visit each node once
Space: O(h) - recursion stack depth
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Recursive solution - swap children"""
        if not root:
            return None
        
        # Swap children
        root.left, root.right = root.right, root.left
        
        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Iterative solution using queue (BFS)"""
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            # Swap children
            node.left, node.right = node.right, node.left
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root


def create_tree():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    return root


def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    s = Solution()
    
    root = create_tree()
    print(f"Original: {tree_to_list(root)}")
    
    inverted = s.invertTree(root)
    print(f"Inverted: {tree_to_list(inverted)}")
    
    print("✅ Test passed!")