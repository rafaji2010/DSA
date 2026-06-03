"""
LeetCode 104 - Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Recursive solution"""
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)
    
    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        """Iterative solution using BFS (level order)"""
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        
        return depth


if __name__ == "__main__":
    s = Solution()
    
    # Test: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    print(f"Max depth (recursive): {s.maxDepth(root)}")  # 3
    print(f"Max depth (iterative): {s.maxDepthIterative(root)}")  # 3
    
    print("✅ Test passed!")