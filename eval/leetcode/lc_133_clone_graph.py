# eval/lc_133_clone_graph.py
from typing import Optional, Dict

class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """
    LeetCode 133: Clone Graph
    DFS with Hash Map for cycle detection.
    Time: O(V + E) | Space: O(V)
    """
    if not node:
        return None
        
    old_to_new: Dict[Node, Node] = {}

    def dfs(old_node: Node) -> Node:
        if old_node in old_to_new:
            return old_to_new[old_node]  # Already cloned, return reference

        # Create clone
        clone = Node(old_node.val)
        old_to_new[old_node] = clone

        # Clone all neighbors
        for neighbor in old_node.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)

if __name__ == "__main__":
    # Example: 1 -- 2
    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors = [n2]
    n2.neighbors = [n1]
    
    cloned = clone_graph(n1)

    assert cloned is not None
    
    print(f"Original Node 1: {n1.val}, Neighbor: {n1.neighbors[0].val}")
    print(f"Cloned Node 1: {cloned.val}, Neighbor: {cloned.neighbors[0].val}")
    print(f"Are they same object? {n1 is cloned}")  # False