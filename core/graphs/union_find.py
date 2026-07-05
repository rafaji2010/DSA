# core/graphs/union_find.py
from typing import List

class UnionFind:
    """
    Disjoint Set data structure with Path Compression and Union by Rank.
    Time: O(α(n)) per operation (near O(1)) | Space: O(n)
    """
    def __init__(self, size: int) -> None:
        self.parent: List[int] = [i for i in range(size)]
        self.rank: List[int] = [0] * size

    def find(self, x: int) -> int:
        """Find the root of x with Path Compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Union the sets containing x and y.
        Returns True if merged, False if already in the same set (cycle detected).
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            
        return True