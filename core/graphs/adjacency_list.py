"""
core/graphs/adjacency_list.py
Graph implementation using Adjacency List

Space: O(V + E)
Time: 
- add_edge: O(1)
- add_vertex: O(1)
- has_edge: O(degree)
- get_neighbors: O(1)
"""

from collections import defaultdict
from typing import List, Set, Dict, Optional


class Graph:
    """Undirected graph using adjacency list"""
    
    def __init__(self):
        self.graph: Dict[int, List[int]] = defaultdict(list)
        self.vertices: Set[int] = set()
    
    def add_vertex(self, vertex: int) -> None:
        """Add a vertex to the graph."""
        self.vertices.add(vertex)
        # defaultdict will create list automatically when accessed
    
    def add_edge(self, u: int, v: int) -> None:
        """Add an undirected edge between u and v."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph
    
    def has_edge(self, u: int, v: int) -> bool:
        """Check if edge exists between u and v."""
        return v in self.graph[u]
    
    def get_neighbors(self, vertex: int) -> List[int]:
        """Return all neighbors of vertex."""
        return self.graph.get(vertex, [])
    
    def degree(self, vertex: int) -> int:
        """Return degree of vertex."""
        return len(self.get_neighbors(vertex))
    
    def display(self) -> None:
        """Display the graph."""
        print("\nGraph (Adjacency List):")
        for vertex in sorted(self.vertices):
            neighbors = sorted(self.get_neighbors(vertex))
            print(f"  {vertex}: {neighbors}")
    
    def __repr__(self) -> str:
        return f"Graph(vertices={len(self.vertices)}, edges={sum(len(v) for v in self.graph.values())//2})"


class DirectedGraph:
    """Directed graph using adjacency list"""
    
    def __init__(self):
        self.graph: Dict[int, List[int]] = defaultdict(list)
        self.vertices: Set[int] = set()
    
    def add_vertex(self, vertex: int) -> None:
        self.vertices.add(vertex)
    
    def add_edge(self, u: int, v: int) -> None:
        """Add directed edge from u to v."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
    
    def has_edge(self, u: int, v: int) -> bool:
        return v in self.graph[u]
    
    def get_neighbors(self, vertex: int) -> List[int]:
        return self.graph.get(vertex, [])
    
    def in_degree(self, vertex: int) -> int:
        """Count incoming edges."""
        count = 0
        for neighbors in self.graph.values():
            if vertex in neighbors:
                count += 1
        return count
    
    def out_degree(self, vertex: int) -> int:
        """Count outgoing edges."""
        return len(self.get_neighbors(vertex))
    
    def display(self) -> None:
        print("\nDirected Graph (Adjacency List):")
        for vertex in sorted(self.vertices):
            neighbors = sorted(self.get_neighbors(vertex))
            print(f"  {vertex} → {neighbors}")


if __name__ == "__main__":
    print("=" * 60)
    print("ADJACENCY LIST GRAPH IMPLEMENTATION")
    print("=" * 60)
    
    # Undirected Graph
    print("\n--- Undirected Graph ---")
    g = Graph()
    
    # Add edges (vertices auto-added)
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)]
    for u, v in edges:
        g.add_edge(u, v)
        print(f"Added edge: {u}--{v}")
    
    g.display()
    print(f"\nGraph info: {g}")
    print(f"Degree of vertex 1: {g.degree(1)}")
    print(f"Neighbors of vertex 2: {g.get_neighbors(2)}")
    print(f"Edge exists 2-4? {g.has_edge(2, 4)}")
    print(f"Edge exists 0-3? {g.has_edge(0, 3)}")
    
    # Directed Graph
    print("\n--- Directed Graph ---")
    dg = DirectedGraph()
    
    dg.add_edge(0, 1)
    dg.add_edge(0, 2)
    dg.add_edge(1, 2)
    dg.add_edge(1, 3)
    dg.add_edge(2, 4)
    dg.add_edge(3, 4)
    
    dg.display()
    print(f"\nOut-degree of vertex 1: {dg.out_degree(1)}")
    print(f"In-degree of vertex 2: {dg.in_degree(2)}")
    
    print("\n✅ Adjacency list implementation complete!")
