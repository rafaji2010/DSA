# eval/tree_patterns.py
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

# ==========================================
# LeetCode 226: Invert Binary Tree
# ==========================================
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Swaps left and right children recursively.
    Time: O(n) | Space: O(h) where h is tree height (call stack)
    """
    if root is None:
        return None
    
    # Swap the children
    root.left, root.right = root.right, root.left
    
    # Recurse on the subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root

# ==========================================
# LeetCode 101: Symmetric Tree
# ==========================================
def is_symmetric(root: Optional[TreeNode]) -> bool:
    """
    Uses a helper function to compare two subtrees.
    Time: O(n) | Space: O(h)
    """
    if root is None:
        return True
        
    def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:

        # If both are None, they are symmetric
        if left is None and right is None:
            return True
        # If only one is None, not symmetric
        if left is None or right is None:
            return False
        # Values must match, and outer/inner branches must mirror
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
                
    return is_mirror(root.left, root.right)

# ==========================================
# LeetCode 112: Path Sum
# ==========================================
def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    """
    DFS traversal subtracting node values from target.
    Time: O(n) | Space: O(h)
    """
    # If we hit a dead end (null node), no path exists here
    if root is None:
        return False
        
    # Subtract current value from target
    remaining_sum = target_sum - root.val
    
    # Check if it's a leaf node
    if root.left is None and root.right is None:
        # If remaining sum is 0, we found a valid path!
        return remaining_sum == 0
        
    # Otherwise, keep recursing down left and right
    return (has_path_sum(root.left, remaining_sum) or 
            has_path_sum(root.right, remaining_sum))


# ==========================================
# Helper to print tree (for testing)
# ==========================================
def tree_to_list(root: Optional[TreeNode]) -> list:
    if not root: return []
    result = [root.val]
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            result.append(node.left.val)
            queue.append(node.left)
        elif node.right:
            result.append(None)
        if node.right:
            result.append(node.right.val)
            queue.append(node.right)
        elif node.left:
            result.append(None)
    return result

if __name__ == "__main__":
    # Build a test tree:
    #       4
    #      / \
    #     2   7
    #    / \ / \
    #   1  3 6  9
    tree1 = TreeNode(4,
                left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
                right=TreeNode(7, left=TreeNode(6), right=TreeNode(9))
            )
            
    print("--- LC 226: Invert Tree ---")
    print(f"Original: {tree_to_list(tree1)}")
    inverted = invert_tree(tree1)
    print(f"Inverted: {tree_to_list(inverted)}")
    
    # Build a symmetric tree:
    #       1
    #      / \
    #     2   2
    #    / \ / \
    #   3  4 4  3
    tree2 = TreeNode(1,
                left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                right=TreeNode(2, left=TreeNode(4), right=TreeNode(3))
            )
    
    print("\n--- LC 101: Symmetric Tree ---")
    print(f"Is symmetric? {is_symmetric(tree2)}")  # Expected: True
    
    # Build a path sum tree:
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    tree3 = TreeNode(5,
                left=TreeNode(4, left=TreeNode(11)),
                right=TreeNode(8, left=TreeNode(13), right=TreeNode(4))
            )
            
    print("\n--- LC 112: Path Sum ---")
    print(f"Has path sum 20? {has_path_sum(tree3, 20)}")  # Expected: True (5->4->11)
    print(f"Has path sum 26? {has_path_sum(tree3, 26)}")  # Expected: True (5->8->13)
    print(f"Has path sum 27? {has_path_sum(tree3, 27)}")  # Expected: False