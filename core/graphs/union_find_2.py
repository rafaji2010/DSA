"""
core/union_find.py
Disjoint Set Union (Union-Find) with path compression and union by rank
"""

from typing import List, Optional, Tuple

class UnionFind:
    """
    Disjoint Set Union data structure.
    
    Time: find() - O(α(n)) amortized (almost O(1))
          union() - O(α(n)) amortized
    Space: O(n)
    Where α(n) is the inverse Ackermann function (~ constant for practical n)
    """
    
    def __init__(self, n: int):
        """
        Initialize n elements (0 to n-1), each in its own set.
        
        Args:
            n: Number of elements
        """
        self.parent: List[int] = list(range(n))
        self.rank: List[int] = [0] * n
        self._size: int = n
    
    def find(self, x: int) -> int:
        """
        Find the root/representative of the set containing x.
        
        Uses path compression: makes nodes point directly to root.
        Time: O(α(n)) amortized
        """
        # Base case: x is its own parent (it's the root)
        if self.parent[x] != x:
            # Recursively find root and compress path
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def find_iterative(self, x: int) -> int:
        """
        Find root iteratively (without recursion).
        Useful for very deep trees (though path compression makes recursion safe).
        """
        root = x
        # Find root
        while self.parent[root] != root:
            root = self.parent[root]
        
        # Path compression: make all nodes point directly to root
        while self.parent[x] != x:
            next_node = self.parent[x]
            self.parent[x] = root
            x = next_node
        
        return root
    
    def union(self, x: int, y: int) -> bool:
        """
        Merge the sets containing x and y.
        
        Uses union by rank: attach smaller tree to larger tree.
        
        Returns:
            True if sets were merged, False if they were already connected
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        # Already in same set
        if root_x == root_y:
            return False
        
        # Union by rank: attach smaller rank tree to larger rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # Same rank: attach root_x to root_y and increment rank
            self.parent[root_x] = root_y
            self.rank[root_y] += 1
        
        self._size -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)
    
    def components(self) -> int:
        """Return the number of disjoint sets."""
        return self._size
    
    def get_sets(self) -> List[List[int]]:
        """
        Return all elements grouped by their set.
        Useful for visualizing clusters.
        """
        # Build mapping from root to list of elements
        sets_dict = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in sets_dict:
                sets_dict[root] = []
            sets_dict[root].append(i)
        
        return list(sets_dict.values())

if __name__ == "__main__":
    print("=== Basic Union-Find ===")
    uf = UnionFind(6)
    print(f"Initially: {uf.parent}")
    print(f"Components: {uf.components()}")
    
    # Union some elements
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(0, 2)
    
    print(f"\nAfter unions: {uf.parent}")
    print(f"Components: {uf.components()}")
    print(f"Sets: {uf.get_sets()}")
    
    print(f"\n0 and 3 connected? {uf.connected(0, 3)}")  # True
    print(f"0 and 4 connected? {uf.connected(0, 4)}")  # False