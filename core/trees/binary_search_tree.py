"""
core/trees/binary_search_tree.py
Binary Search Tree implementation

Property: left < root < right for ALL nodes
"""

from __future__ import annotations
from typing import Optional, Any, List
from collections import deque


class BSTNode:
    """Node for Binary Search Tree"""
    
    def __init__(self, value: Any):
        self.value: Any = value
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None
    
    def __repr__(self) -> str:
        return f"BSTNode({self.value})"


class BinarySearchTree:
    """Binary Search Tree implementation"""
    
    def __init__(self):
        self.root: Optional[BSTNode] = None
    
    def is_empty(self) -> bool:
        """Return True if tree has no nodes."""
        return self.root is None
    
    # ========== INSERT ==========
    
    def insert(self, value: Any) -> None:
        """
        Insert a value into the BST.
        Maintains BST property: left < root < right
        
        Time: O(log n) average, O(n) worst case
        """
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node: BSTNode, value: Any) -> None:
        """Helper method for recursive insertion."""
        if value < node.value:
            # Go left
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            # Go right
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert_recursive(node.right, value)
        else:
            # Duplicate value - silently ignore
            # (Some implementations raise error or store count)
            pass
    
    # ========== SEARCH ==========
    
    def search(self, value: Any) -> Optional[BSTNode]:
        """
        Search for a value in the BST.
        
        Time: O(log n) average, O(n) worst case
        Returns the node if found, None otherwise.
        """
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node: Optional[BSTNode], value: Any) -> Optional[BSTNode]:
        if node is None:
            return None
        
        if node.value == value:
            return node
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def contains(self, value: Any) -> bool:
        """Return True if value exists in BST."""
        return self.search(value) is not None
    
    # ========== TRAVERSALS ==========
    
    def inorder(self, node: Optional[BSTNode] = None, result: Optional[List[Any]] = None) -> List[Any]:
        """
        Inorder Traversal: Left → Root → Right
        For BST, this returns SORTED order!
        """
        if result is None:
            result = []
            node = node or self.root
        
        if node:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)
        
        return result
    
    def preorder(self, node: Optional[BSTNode] = None, result: Optional[List[Any]] = None) -> List[Any]:
        """Preorder Traversal: Root → Left → Right"""
        if result is None:
            result = []
            node = node or self.root
        
        if node:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        
        return result
    
    def postorder(self, node: Optional[BSTNode] = None, result: Optional[List[Any]] = None) -> List[Any]:
        """Postorder Traversal: Left → Right → Root"""
        if result is None:
            result = []
            node = node or self.root
        
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.value)
        
        return result
    
    def level_order(self) -> List[List[Any]]:
        """Level Order Traversal (BFS)"""
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
    
    # ========== HELPER METHODS ==========
    
    def display(self) -> None:
        """Display BST in a rotated format."""
        print("\nBST structure (root at left, branches going right):")
        self._display_recursive(self.root, 0)
        print()
    
    def _display_recursive(self, node: Optional[BSTNode], level: int) -> None:
        if node:
            self._display_recursive(node.right, level + 1)
            print("    " * level + f"├── {node.value}")
            self._display_recursive(node.left, level + 1)
    
    def min_value(self) -> Optional[Any]:
        """Find minimum value in BST (leftmost node)."""
        if self.root is None:
            return None
        
        current = self.root
        while current.left:
            current = current.left
        return current.value
    
    def max_value(self) -> Optional[Any]:
        """Find maximum value in BST (rightmost node)."""
        if self.root is None:
            return None
        
        current = self.root
        while current.right:
            current = current.right
        return current.value
      
        # ========== DELETE ==========

    def delete(self, value: Any) -> bool:
        """
        Delete a value from the BST.
        Returns True if deleted, False if value not found.
        
        Time: O(log n) average, O(n) worst case
        """
        if self.root is None:
            return False
        
        # Track parent for reconnection
        parent = None
        current = self.root
        
        # First, find the node to delete and its parent
        while current and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        
        # Value not found
        if current is None:
            return False
        
        # CASE 1: Node has NO children (leaf)
        if current.left is None and current.right is None:
            self._delete_leaf(parent, current)
        
        # CASE 2: Node has ONE child
        elif current.left is None:  # Only right child exists
            self._delete_node_with_one_child(parent, current, is_left=False)
        elif current.right is None:  # Only left child exists
            self._delete_node_with_one_child(parent, current, is_left=True)
        
        # CASE 3: Node has TWO children
        else:
            self._delete_node_with_two_children(parent, current)
        
        return True


    def _delete_leaf(self, parent: Optional[BSTNode], node: BSTNode) -> None:
        """
        Delete a leaf node (no children).
        Simply remove the reference from its parent.
        """
        if parent is None:
            # Deleting root node (tree has only one node)
            self.root = None
        elif parent.left == node:
            parent.left = None
        else:
            parent.right = None


    def _delete_node_with_one_child(self, parent: Optional[BSTNode], node: BSTNode, is_left: bool) -> None:
        """
        Delete a node with exactly one child.
        Replace the node with its only child.
        
        is_left: True if the only child is LEFT child
                False if the only child is RIGHT child
        """
        # Get the single child
        child = node.left if is_left else node.right
        
        if parent is None:
            # Deleting root node
            self.root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child


    def _delete_node_with_two_children(self, parent: Optional[BSTNode], node: BSTNode) -> None:
        """
        Delete a node with two children.
        Strategy:
            1. Find inorder successor (smallest node in right subtree)
            2. Copy successor's value to current node
            3. Delete the successor (which will be either Case 1 or Case 2)
        """
        # Find inorder successor (smallest in right subtree)
        successor_parent = node
        successor = node.right
        
        while successor.left:
            successor_parent = successor
            successor = successor.left
        
        # Copy successor's value to current node
        node.value = successor.value
        
        # Delete the successor (it will be either leaf or has right child)
        # Note: Successor never has a left child (by definition!)
        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right


    def delete_with_trace(self, value: Any) -> bool:
        """
        Debug version of delete - shows what case is being used.
        """
        if self.root is None:
            print("Tree is empty")
            return False
        
        print(f"\n--- Deleting {value} ---")
        
        # Find node to delete
        parent = None
        current = self.root
        
        while current and current.value != value:
            parent = current
            if value < current.value:
                print(f"  {value} < {current.value} → going LEFT")
                current = current.left
            else:
                print(f"  {value} > {current.value} → going RIGHT")
                current = current.right
        
        if current is None:
            print(f"  Value {value} not found!")
            return False
        
        print(f"  Found node with value {current.value}")
        
        # Determine case
        if current.left is None and current.right is None:
            print(f"  CASE 1: Node {current.value} is a LEAF (no children)")
            self._delete_leaf(parent, current)
        
        elif current.left is None:
            print(f"  CASE 2: Node {current.value} has ONLY RIGHT child")
            self._delete_node_with_one_child(parent, current, is_left=False)
        elif current.right is None:
            print(f"  CASE 2: Node {current.value} has ONLY LEFT child")
            self._delete_node_with_one_child(parent, current, is_left=True)
        
        else:
            print(f"  CASE 3: Node {current.value} has TWO children")
            print(f"    Finding inorder successor (smallest in right subtree)...")
            self._delete_node_with_two_children(parent, current)
        
        print(f"  ✅ Deleted {value}")
        return True

        # ========== TASK 5: TRAVERSAL VERIFICATION ==========

    def verify_traversals(self) -> None:
        """
        Verify that traversals work correctly.
        - Inorder should return SORTED order
        - All traversals should visit all nodes
        """
        if self.root is None:
            print("Tree is empty - nothing to verify")
            return
        
        inorder_result = self.inorder()
        preorder_result = self.preorder()
        postorder_result = self.postorder()
        
        print("\n" + "-" * 40)
        print("TRAVERSAL VERIFICATION")
        print("-" * 40)
        
        # Check inorder is sorted
        is_sorted = all(inorder_result[i] <= inorder_result[i+1] for i in range(len(inorder_result)-1))
        
        print(f"Inorder:  {inorder_result}")
        print(f"Preorder: {preorder_result}")
        print(f"Postorder:{postorder_result}")
        
        if is_sorted:
            print("✅ VERIFIED: Inorder traversal returns SORTED order!")
        else:
            print("❌ ERROR: Inorder traversal did NOT return sorted order")
        
        # Check lengths
        expected_len = len(inorder_result)
        if len(preorder_result) == expected_len and len(postorder_result) == expected_len:
            print(f"✅ All traversals visited all {expected_len} nodes")
        else:
            print(f"❌ Length mismatch: inorder={len(inorder_result)}, preorder={len(preorder_result)}, postorder={len(postorder_result)}")


    def test_with_random_data(self, num_values: int = 20) -> None:
        """
        Test BST with random data to verify properties.
        """
        import random
        
        print("\n" + "=" * 60)
        print(f"TESTING BST WITH {num_values} RANDOM VALUES")
        print("=" * 60)
        
        # Create new BST
        test_bst = BinarySearchTree()
        
        # Generate random values
        random_values = random.sample(range(1, num_values * 10), num_values)
        print(f"\nRandom values (unsorted): {random_values}")
        print(f"Sorted original: {sorted(random_values)}")
        
        # Insert all values
        for val in random_values:
            test_bst.insert(val)
        
        # Get inorder result
        inorder_result = test_bst.inorder()
        print(f"\nInorder traversal result: {inorder_result}")
        
        # Verify sorted
        if inorder_result == sorted(random_values):
            print("✅ VERIFIED: Inorder = SORTED order!")
        else:
            print("❌ ERROR: Inorder != Sorted")
        
        # Verify contains works for all values
        missing = [val for val in random_values if not test_bst.contains(val)]
        if not missing:
            print("✅ All inserted values found via search()")
        else:
            print(f"❌ Missing values: {missing}")
        
        # Verify min/max
        if test_bst.min_value() == min(random_values) and test_bst.max_value() == max(random_values):
            print(f"✅ Min/max correct: min={test_bst.min_value()}, max={test_bst.max_value()}")
        else:
            print(f"❌ Min/max incorrect: min={test_bst.min_value()}, expected={min(random_values)}")
        
        return test_bst

    # Add this to your BinarySearchTree class

    def debug_insert_with_breakpoint(self, value: Any) -> None:
        """
        Debug version of insert with breakpoint to inspect recursive flow.
        """
        print(f"\n--- Inserting {value} ---")
        
        if self.root is None:
            self.root = BSTNode(value)
            print(f"  Tree empty → created root {value}")
            return
        
        current = self.root
        parent = None
        
        while current:
            parent = current
            if value < current.value:
                print(f"  {value} < {current.value} → going LEFT")
                current = current.left
            elif value > current.value:
                print(f"  {value} > {current.value} → going RIGHT")
                current = current.right
            else:
                print(f"  Duplicate {value} - ignoring")
                return
            
            breakpoint()  # ← Pause here to inspect variables!
        
        # Insert new node
        if value < parent.value:
            parent.left = BSTNode(value)
            print(f"  Inserted {value} as LEFT child of {parent.value}")
        else:
            parent.right = BSTNode(value)
            print(f"  Inserted {value} as RIGHT child of {parent.value}")


    def debug_search_with_breakpoint(self, value: Any) -> Optional[BSTNode]:
        """
        Debug version of search with breakpoint.
        """
        print(f"\n--- Searching for {value} ---")
        
        current = self.root
        steps = 0
        
        while current:
            steps += 1
            print(f"  Step {steps}: At node {current.value}")
            
            if current.value == value:
                print(f"  ✓ Found {value}!")
                return current
            elif value < current.value:
                print(f"  {value} < {current.value} → going LEFT")
                current = current.left
            else:
                print(f"  {value} > {current.value} → going RIGHT")
                current = current.right
            
            breakpoint()  # ← Pause here!
        
        print(f"  ✗ {value} not found after {steps} steps")
        return None


if __name__ == "__main__":
    print("=" * 60)
    print("BINARY SEARCH TREE (BST) DEMONSTRATION")
    print("=" * 60)
    
    # Create BST and insert values
    bst = BinarySearchTree()
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    
    print(f"\nInserting values: {values}")
    for val in values:
        bst.insert(val)
        print(f"  Inserted {val}")
    
    print("\n" + "-" * 40)
    print("BST STRUCTURE")
    print("-" * 40)
    bst.display()
    
    print("\n" + "-" * 40)
    print("TRAVERSALS")
    print("-" * 40)
    print(f"Inorder (sorted!):   {bst.inorder()}")
    print(f"Preorder:            {bst.preorder()}")
    print(f"Postorder:           {bst.postorder()}")
    print(f"Level order (BFS):   {bst.level_order()}")
    
    print("\n" + "-" * 40)
    print("SEARCH TESTS")
    print("-" * 40)
    
    test_values = [6, 13, 20, 1, 14]
    for val in test_values:
        found = bst.search(val)
        print(f"Search for {val}: {'Found' if found else 'Not found'}")
    
    print("\n" + "-" * 40)
    print("MIN/MAX")
    print("-" * 40)
    print(f"Minimum value: {bst.min_value()}")
    print(f"Maximum value: {bst.max_value()}")
    
    # ========== TASK 5: TRAVERSAL VERIFICATION ==========
    print("\n" + "=" * 60)
    print("TASK 5: TRAVERSAL VERIFICATION")
    print("=" * 60)
    
    # Verify traversals on the existing tree
    bst.verify_traversals()
    
    # Test with random data
    test_bst = bst.test_with_random_data(15)
    
    # Show the random BST structure
    print("\n" + "-" * 40)
    print("Random BST Structure:")
    print("-" * 40)
    test_bst.display()
    
    # Delete some random values and verify
    print("\n" + "-" * 40)
    print("DELETE VERIFICATION")
    print("-" * 40)
    
    # Get current values
    current_values = test_bst.inorder()
    print(f"Current BST values: {current_values}")
    
    # Delete first, middle, and last elements
    if len(current_values) >= 3:
        to_delete = [current_values[0], current_values[len(current_values)//2], current_values[-1]]
        print(f"\nDeleting: {to_delete}")
        
        for val in to_delete:
            test_bst.delete_with_trace(val)
        
        print(f"\nAfter deletions: {test_bst.inorder()}")
    
    print("\n" + "=" * 60)
    print("✅ BST implementation complete!")
    print("=" * 60)