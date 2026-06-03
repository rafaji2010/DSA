"""
core/graphs/adjacency_matrix.py
Graph implementation using Adjacency Matrix

Space: O(V²)
Time: 
- add_edge: O(1)
- has_edge: O(1)
- get_neighbors: O(V)
"""

from typing import List, Optional


class GraphMatrix:
    """Undirected graph using adjacency matrix"""
    
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        # Initialize V x V matrix with zeros
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, u: int, v: int) -> None:
        """Add undirected edge between u and v."""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = 1
            self.matrix[v][u] = 1
    
    def remove_edge(self, u: int, v: int) -> None:
        """Remove edge between u and v."""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = 0
            self.matrix[v][u] = 0
    
    def has_edge(self, u: int, v: int) -> bool:
        """Check if edge exists."""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            return self.matrix[u][v] == 1
        return False
    
    def get_neighbors(self, vertex: int) -> List[int]:
        """Return all neighbors of vertex."""
        neighbors = []
        for v in range(self.num_vertices):
            if self.matrix[vertex][v] == 1:
                neighbors.append(v)
        return neighbors
    
    def degree(self, vertex: int) -> int:
        """Return degree of vertex."""
        return len(self.get_neighbors(vertex))
    
    def display(self) -> None:
        """Display the adjacency matrix."""
        print("\nAdjacency Matrix:")
        print("    " + "  ".join(str(i) for i in range(self.num_vertices)))
        for i in range(self.num_vertices):
            row = "  ".join(str(self.matrix[i][j]) for j in range(self.num_vertices))
            print(f"{i} | {row}")


class WeightedGraphMatrix:
    """Weighted graph using adjacency matrix (storing weights)"""
    
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        # Initialize with infinity for non-existent edges
        self.matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        # Set diagonal to 0 (distance to self)
        for i in range(num_vertices):
            self.matrix[i][i] = 0
    
    def add_edge(self, u: int, v: int, weight: int) -> None:
        """Add weighted directed edge from u to v."""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = weight
    
    def get_weight(self, u: int, v: int) -> float:
        """Get weight of edge from u to v."""
        return self.matrix[u][v]
    
    def display(self) -> None:
        """Display weighted adjacency matrix."""
        print("\nWeighted Adjacency Matrix:")
        print("    " + "  ".join(f"{i:2d}" for i in range(self.num_vertices)))
        for i in range(self.num_vertices):
            row = "  ".join(f"{self.matrix[i][j]:2.0f}" if self.matrix[i][j] != float('inf') else " ∞" for j in range(self.num_vertices))
            print(f"{i} | {row}")


if __name__ == "__main__":
    print("=" * 60)
    print("ADJACENCY MATRIX GRAPH IMPLEMENTATION")
    print("=" * 60)
    
    # Unweighted graph
    print("\n--- Unweighted Graph ---")
    g = GraphMatrix(5)
    
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)]
    for u, v in edges:
        g.add_edge(u, v)
        print(f"Added edge: {u}--{v}")
    
    g.display()
    print(f"\nDegree of vertex 1: {g.degree(1)}")
    print(f"Neighbors of vertex 2: {g.get_neighbors(2)}")
    print(f"Edge exists 2-4? {g.has_edge(2, 4)}")
    
    # Weighted graph
    print("\n--- Weighted Graph ---")
    wg = WeightedGraphMatrix(4)
    
    wg.add_edge(0, 1, 5)
    wg.add_edge(0, 2, 3)
    wg.add_edge(1, 2, 2)
    wg.add_edge(1, 3, 4)
    wg.add_edge(2, 3, 1)
    
    wg.display()
    print(f"\nWeight from 0 to 1: {wg.get_weight(0, 1)}")
    print(f"Weight from 1 to 2: {wg.get_weight(1, 2)}")
    
    print("\n✅ Adjacency matrix implementation complete!")
