"""
core/graphs/bfs.py
Breadth-First Search (BFS) traversal

Time: O(V + E) - visits each vertex and edge once
Space: O(V) - queue can contain all vertices

BFS explores level by level (like ripples in water)
"""

from collections import deque
from adjacency_list import Graph


def bfs(graph: Graph, start: int) -> tuple:
    """
    Perform BFS traversal from start vertex.
    Returns: (visited_order, parent, distance)
    """
    visited = set()
    order = []
    parent = {}
    distance = {}
    
    # Initialize queue with start vertex
    queue = deque([start])
    visited.add(start)
    distance[start] = 0
    parent[start] = None
    
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = vertex
                distance[neighbor] = distance[vertex] + 1
                queue.append(neighbor)
    
    return order, parent, distance


def bfs_shortest_path(graph: Graph, start: int, target: int) -> list:
    """
    Find shortest path from start to target using BFS.
    Returns list of vertices along the path.
    """
    order, parent, distance = bfs(graph, start)
    
    if target not in parent:
        return []  # No path exists
    
    # Reconstruct path by backtracking from target
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = parent[current]
    
    return list(reversed(path))


def bfs_level_order(graph: Graph, start: int) -> list:
    """
    Return vertices grouped by level/distance from start.
    """
    order, parent, distance = bfs(graph, start)
    
    # Group vertices by distance
    levels = {}
    for vertex, dist in distance.items():
        if dist not in levels:
            levels[dist] = []
        levels[dist].append(vertex)
    
    return [levels[d] for d in sorted(levels.keys())]


def bfs_with_logging(graph: Graph, start: int) -> list:
    """
    BFS with detailed logging to visualize the process.
    """
    print(f"\n=== BFS starting from vertex {start} ===\n")
    
    visited = set()
    order = []
    queue = deque([start])
    visited.add(start)
    
    print(f"Initial: queue={list(queue)}, visited={visited}")
    
    step = 1
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        print(f"\nStep {step}: Dequeue {vertex}")
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(f"  → Enqueue {neighbor} (neighbor of {vertex})")
        
        print(f"  queue={list(queue)}, visited={sorted(visited)}")
        step += 1
    
    print(f"\nFinal traversal order: {order}")
    return order


if __name__ == "__main__":
    print("=" * 60)
    print("BREADTH-FIRST SEARCH (BFS)")
    print("=" * 60)
    
    # Create a graph
    g = Graph()
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (4, 7)]
    for u, v in edges:
        g.add_edge(u, v)
    
    g.display()
    
    # BFS traversal
    print("\n--- BFS Traversal ---")
    order, parent, distance = bfs(g, 0)
    print(f"Visited order: {order}")
    print(f"Parent of each node: {parent}")
    print(f"Distance from start: {distance}")
    
    # Shortest path
    print("\n--- Shortest Path ---")
    path = bfs_shortest_path(g, 0, 7)
    print(f"Shortest path from 0 to 7: {path}")
    
    # Level order
    print("\n--- Level Order (BFS levels) ---")
    levels = bfs_level_order(g, 0)
    for level, nodes in enumerate(levels):
        print(f"  Level {level}: {nodes}")
    
    # BFS with logging
    bfs_with_logging(g, 0)
    
    print("\n✅ BFS implementation complete!")
