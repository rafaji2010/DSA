"""
LeetCode 102 - Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return its level order traversal.
Time: O(n), Space: O(n)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    """Binary tree node."""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """BFS using queue - process level by level."""
        if not root:
            return []
        
        result: List[List[int]] = []
        queue: deque[TreeNode] = deque([root])
        
        while queue:
            level_size: int = len(queue)
            level_values: List[int] = []
            
            for _ in range(level_size):
                node: TreeNode = queue.popleft()
                level_values.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_values)
        
        return result
    
    def levelOrderRecursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        """DFS with level tracking."""
        result: List[List[int]] = []
        
        def dfs(node: Optional[TreeNode], level: int) -> None:
            if not node:
                return
            
            if len(result) == level:
                result.append([])
            
            result[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return result


def create_tree() -> TreeNode:
    """Create:     3
                   / \
                  9   20
                     /  \
                    15   7
    """
    root: TreeNode = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


if __name__ == "__main__":
    s: Solution = Solution()
    
    root: TreeNode = create_tree()
    print("=" * 60)
    print("Binary Tree Level Order Traversal")
    print("=" * 60)
    
    result: List[List[int]] = s.levelOrder(root)
    print(f"\nBFS Result: {result}")
    
    result_rec: List[List[int]] = s.levelOrderRecursive(root)
    print(f"DFS Result: {result_rec}")
    
    print("\n✅ LC 102 complete!")
