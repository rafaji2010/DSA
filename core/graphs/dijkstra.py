"""
core/graphs/dijkstra.py
Dijkstra's Algorithm for Shortest Path
"""

import heapq
from typing import Dict, List, Optional, Tuple
from collections import defaultdict


class Graph:
    """Weighted graph using adjacency list"""
    
    def __init__(self):
        self.graph: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
    
    def add_edge(self, u: int, v: int, weight: int) -> None:
        """Add undirected weighted edge"""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    
    def add_directed_edge(self, u: int, v: int, weight: int) -> None:
        """Add directed weighted edge"""
        self.graph[u].append((v, weight))


def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Tuple[Dict[int, int], Dict[int, Optional[int]]]:
    """
    Dijkstra's algorithm for shortest path.
    
    Returns:
        distances: shortest distance from start to each node
        parent: previous node in shortest path (for reconstruction)
    
    Time: O((V + E) log V) with binary heap
    Space: O(V)
    """
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Parent pointers for path reconstruction
    parent = {node: None for node in graph}
    
    # Min-heap: (distance, node)
    heap = [(0, start)]
    visited = set()
    
    while heap:
        current_dist, current = heapq.heappop(heap)
        
        # Skip if already processed
        if current in visited:
            continue
        visited.add(current)
        
        # Explore neighbors
        for neighbor, weight in graph.get(current, []):
            if neighbor in visited:
                continue
            
            new_dist = current_dist + weight
            
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parent[neighbor] = current
                heapq.heappush(heap, (new_dist, neighbor))
    
    return distances, parent


def dijkstra_with_trace(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """Dijkstra's algorithm with detailed tracing"""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    visited = set()
    
    print(f"\nStarting Dijkstra from node {start}")
    print("=" * 50)
    
    step = 1
    while heap:
        current_dist, current = heapq.heappop(heap)
        
        if current in visited:
            continue
        
        visited.add(current)
        print(f"\nStep {step}: Processing node {current}")
        print(f"  Current distance: {current_dist}")
        
        for neighbor, weight in graph.get(current, []):
            if neighbor in visited:
                print(f"  → {neighbor} already visited, skipping")
                continue
            
            new_dist = current_dist + weight
            print(f"  → Neighbor {neighbor}: current={current_dist} + {weight} = {new_dist}")
            
            if new_dist < distances[neighbor]:
                print(f"    ✓ UPDATE: {neighbor} distance from {distances[neighbor]} to {new_dist}")
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
            else:
                print(f"    ✗ No update: {new_dist} >= {distances[neighbor]}")
        
        print(f"  Heap: {heap}")
        print(f"  Distances: {distances}")
        step += 1
    
    return distances


def reconstruct_path(parent: Dict[int, Optional[int]], start: int, target: int) -> List[int]:
    """Reconstruct path from start to target using parent pointers"""
    if target not in parent:
        return []
    
    path = []
    current = target
    
    while current is not None:
        path.append(current)
        current = parent[current]
    
    path.reverse()
    
    if path[0] != start:
        return []
    
    return path


def shortest_path(graph: Dict[int, List[Tuple[int, int]]], start: int, target: int) -> Tuple[List[int], int]:
    """Find shortest path and its distance"""
    distances, parent = dijkstra(graph, start)
    
    if distances[target] == float('inf'):
        return [], -1
    
    path = reconstruct_path(parent, start, target)
    return path, distances[target]


if __name__ == "__main__":
    print("=" * 60)
    print("DIJKSTRA'S ALGORITHM DEMONSTRATION")
    print("=" * 60)
    
    # Create graph
    g = Graph()
    
    # Add edges (undirected weighted)
    edges = [
        (0, 1, 4), (0, 2, 2),
        (1, 2, 1), (1, 3, 3),
        (2, 4, 5), (3, 4, 2)
    ]
    
    for u, v, w in edges:
        g.add_edge(u, v, w)
        print(f"Added edge: {u} --({w})-- {v}")
    
    print("\n" + "-" * 40)
    
    # Run Dijkstra from node 0
    distances, parent = dijkstra(g.graph, 0)
    
    print("\nShortest distances from node 0:")
    for node, dist in sorted(distances.items()):
        print(f"  Distance to {node}: {dist}")
    
    # Path reconstruction
    print("\n" + "-" * 40)
    print("PATH RECONSTRUCTION")
    print("-" * 40)
    
    targets = [3, 4, 1, 2]
    for target in targets:
        path, dist = shortest_path(g.graph, 0, target)
        print(f"Path 0 → {target}: {path} (distance: {dist})")
    
    # Detailed trace
    print("\n" + "=" * 60)
    print("DETAILED TRACE")
    print("=" * 60)
    dijkstra_with_trace(g.graph, 0)
    
    print("\n" + "=" * 60)
    print("LIMITATIONS")
    print("=" * 60)
    print("""
    Dijkstra's algorithm does NOT work with NEGATIVE edge weights!
    
    Why? Once a node is marked as visited, we assume its distance is final.
    Negative weights could create shorter paths through already visited nodes.
    
    Example graph with negative edge:
        A -(5)- B -(-10)- C
        |                 |
        └-------(5)-------┘
    
    Use Bellman-Ford algorithm for graphs with negative weights.
    """)
    
    print("\n✅ Dijkstra's algorithm complete!")
