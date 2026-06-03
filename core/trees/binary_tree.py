"""
core/trees/binary_tree.py
Binary Tree implementation with basic operations
"""

from __future__ import annotations
from typing import Optional, Any, List
from collections import deque


class TreeNode:
    """
    A single node in a binary tree.
    
    Each node contains:
    - value: The data stored in the node
    - left: Reference to left child (or None)
    - right: Reference to right child (or None)
    """
    
    def __init__(self, value: Any):
        self.value: Any = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
    
    def __repr__(self) -> str:
        return f"TreeNode({self.value})"


class BinaryTree:
    """
    Binary Tree implementation.
    
    Properties:
    - Each node has at most 2 children (left and right)
    - No specific ordering (unlike BST)
    """
    
    def __init__(self):
        self.root: Optional[TreeNode] = None
    
    def is_empty(self) -> bool:
        """Return True if tree has no nodes."""
        return self.root is None
    
    # ========== INSERTION METHODS ==========
    
    def insert_left(self, parent: TreeNode, value: Any) -> TreeNode:
        """
        Insert a node as the left child of parent.
        If left child already exists, push it down.
        """
        new_node = TreeNode(value)
        if parent.left:
            # Push existing left child down
            new_node.left = parent.left
        parent.left = new_node
        return new_node
    
    def insert_right(self, parent: TreeNode, value: Any) -> TreeNode:
        """Insert a node as the right child of parent."""
        new_node = TreeNode(value)
        if parent.right:
            new_node.right = parent.right
        parent.right = new_node
        return new_node
    
    # ========== SEARCH METHODS ==========
    
    def find_bfs(self, value: Any) -> Optional[TreeNode]:
        """
        Breadth-First Search (level order) to find a value.
        Uses a queue - explores level by level.
        """
        if not self.root:
            return None
        
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            if node.value == value:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return None
    
    def find_dfs(self, value: Any) -> Optional[TreeNode]:
        """
        Depth-First Search (preorder) to find a value.
        Uses recursion - explores depth first.
        """
        return self._find_dfs_recursive(self.root, value)
    
    def _find_dfs_recursive(self, node: Optional[TreeNode], value: Any) -> Optional[TreeNode]:
        if not node:
            return None
        if node.value == value:
            return node
        
        # Search left subtree
        left_result = self._find_dfs_recursive(node.left, value)
        if left_result:
            return left_result
        
        # Search right subtree
        return self._find_dfs_recursive(node.right, value)
    
    # ========== HELPER METHODS ==========
    
    def display(self) -> None:
        """Display tree in a simple format."""
        self._display_recursive(self.root, 0)
    
    def _display_recursive(self, node: Optional[TreeNode], level: int) -> None:
        if node:
            self._display_recursive(node.right, level + 1)
            print("    " * level + str(node.value))
            self._display_recursive(node.left, level + 1)
    
    def to_list(self) -> List[Optional[Any]]:
        """Convert tree to list (level order)."""
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.value)
                queue.append(node.left if node.left else None)
                queue.append(node.right if node.right else None)
            else:
                result.append(None)
        
        # Remove trailing Nones
        while result and result[-1] is None:
            result.pop()
        
        return result

    # Add these methods to your BinaryTree class

    def preorder(self, node: Optional[TreeNode] = None, result: Optional[List[Any]] = None) -> List[Any]:
        """
        Preorder Traversal: Root → Left → Right
        Use case: Copying a tree (create root first, then children)
        """
        if result is None:
            result = []
            node = node or self.root
        
        if node:
            result.append(node.value)          # Visit ROOT
            self.preorder(node.left, result)    # Traverse LEFT subtree
            self.preorder(node.right, result)   # Traverse RIGHT subtree
        
        return result


    def inorder(self, node: Optional[TreeNode] = None, result: Optional[List[Any]] = None) -> List[Any]:
        """
        Inorder Traversal: Left → Root → Right
        Use case: Getting sorted order from BST
        """
        if result is None:
            result = []
            node = node or self.root
        
        if node:
            self.inorder(node.left, result)     # Traverse LEFT subtree
            result.append(node.value)           # Visit ROOT
            self.inorder(node.right, result)    # Traverse RIGHT subtree
        
        return result


    def postorder(self, node: Optional[TreeNode] = None, result: Optional[List[Any]] = None) -> List[Any]:
        """
        Postorder Traversal: Left → Right → Root
        Use case: Deleting a tree (delete children before parent)
        """
        if result is None:
            result = []
            node = node or self.root
        
        if node:
            self.postorder(node.left, result)   # Traverse LEFT subtree
            self.postorder(node.right, result)  # Traverse RIGHT subtree
            result.append(node.value)           # Visit ROOT
        
        return result


    def level_order(self) -> List[List[Any]]:
        """
        Level Order Traversal (BFS) - returns nodes level by level.
        Use case: Printing tree level by level.
        """
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            level_size = len(queue)
            level_values = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.value)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_values)
        
        return result

    def count_nodes(self, node: Optional[TreeNode] = None) -> int:
        """
        Count total number of nodes in tree.
        Time: O(n)
        Space: O(h)
        """
        if node is None:
            return 0
        
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)


    def count_leaves(self, node: Optional[TreeNode] = None) -> int:
        """
        Count number of leaf nodes (nodes with no children).
        """
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return 1
        
        return self.count_leaves(node.left) + self.count_leaves(node.right)
 

    # Add this debug version to your file
    def debug_traversal(self, node: Optional[TreeNode] = None, depth: int = 0):
        """Debug version of inorder traversal with stack trace."""
        if node is None:
            return
        
        indent = "  " * depth
        print(f"{indent}📥 Enter node {node.value}")
        
        self.debug_traversal(node.left, depth + 1)
        
        print(f"{indent}⭐ VISIT node {node.value}")
        
        self.debug_traversal(node.right, depth + 1)
        
        print(f"{indent}📤 Exit node {node.value}")


# To debug:
# Then use: python -m pdb core/trees/binary_tree.py

if __name__ == "__main__":
    print("=" * 50)
    print("BINARY TREE DEMONSTRATION")
    print("=" * 50)
    
    # Create a tree
    tree = BinaryTree()
    
    # Build tree manually:
    #        10
    #       /  \
    #      5    15
    #     / \    \
    #    2   7    20
    
    tree.root = TreeNode(10)
    node5 = TreeNode(5)
    node15 = TreeNode(15)
    tree.root.left = node5
    tree.root.right = node15
    
    node2 = TreeNode(2)
    node7 = TreeNode(7)
    node5.left = node2
    node5.right = node7
    
    node20 = TreeNode(20)
    node15.right = node20
    
    total_nodes = tree.count_nodes(tree.root)
    print(f"\nTotal Nodes: {total_nodes}")
 
    print("\nTree structure:")
    tree.display()

    
    tree.debug_traversal()
    
    print("\n" + "-" * 40)
    print("SEARCH TESTS")
    print("-" * 40)
    
    # Test BFS search
    found = tree.find_bfs(7)
    print(f"BFS find 7: {found}")
    
    found = tree.find_bfs(99)
    print(f"BFS find 99: {found}")
    
    # Test DFS search
    found = tree.find_dfs(20)
    print(f"DFS find 20: {found}")
    
    print("\n" + "=" * 50)
    print("TREE TRAVERSALS")
    print("=" * 50)

    print(f"\nTree:")
    tree.display()

    print(f"\nPreorder  (Root→Left→Right):  {tree.preorder()}")
    print(f"Inorder   (Left→Root→Right):  {tree.inorder()}")
    print(f"Postorder (Left→Right→Root):  {tree.postorder()}")
    print(f"Level order (BFS):            {tree.level_order()}")

    print("\n✅ All traversals working!")
    
    
    
    print("\n✅ Binary tree implementation complete!")