"""
core/graphs/dfs.py
Depth-First Search (DFS) traversal - Recursive & Iterative

Time: O(V + E) - visits each vertex and edge once
Space: O(V) - recursion stack or explicit stack

DFS explores as deep as possible before backtracking
"""

from adjacency_list import Graph


def dfs_recursive(graph: Graph, start: int) -> tuple:
    """
    DFS traversal using recursion.
    Returns: (order, parent)
    """
    visited = set()
    order = []
    parent = {}
    
    def dfs_helper(vertex, par):
        visited.add(vertex)
        parent[vertex] = par
        order.append(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs_helper(neighbor, vertex)
    
    dfs_helper(start, None)
    return order, parent


def dfs_iterative(graph: Graph, start: int) -> tuple:
    """
    DFS traversal using explicit stack (iterative).
    Returns: (order, parent)
    """
    visited = set()
    order = []
    parent = {}
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            
            # Push neighbors to stack (reverse order for same order as recursive)
            for neighbor in reversed(graph.get_neighbors(vertex)):
                if neighbor not in visited:
                    parent[neighbor] = vertex
                    stack.append(neighbor)
    
    return order, parent


def dfs_path_recursive(graph: Graph, start: int, target: int) -> list:
    """
    Find path from start to target using recursive DFS.
    """
    visited = set()
    path = []
    
    def dfs_helper(vertex, target):
        if vertex in visited:
            return False
        
        visited.add(vertex)
        path.append(vertex)
        
        if vertex == target:
            return True
        
        for neighbor in graph.get_neighbors(vertex):
            if dfs_helper(neighbor, target):
                return True
        
        # Backtrack
        path.pop()
        return False
    
    dfs_helper(start, target)
    return path if path and path[-1] == target else []


def dfs_with_logging(graph: Graph, start: int) -> list:
    """
    DFS with detailed logging to visualize the process.
    """
    print(f"\n=== DFS starting from vertex {start} ===\n")
    
    visited = set()
    order = []
    stack = [start]
    
    print(f"Initial: stack={stack}, visited={visited}")
    
    step = 1
    while stack:
        vertex = stack.pop()
        print(f"\nStep {step}: Pop {vertex} from stack")
        
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            print(f"  → Visit {vertex}")
            
            # Push neighbors to stack
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    stack.append(neighbor)
                    print(f"    • Push {neighbor} to stack")
        
        print(f"  stack={stack}, visited={sorted(visited)}")
        step += 1
    
    print(f"\nFinal traversal order: {order}")
    return order


if __name__ == "__main__":
    print("=" * 60)
    print("DEPTH-FIRST SEARCH (DFS)")
    print("=" * 60)
    
    # Create a graph
    g = Graph()
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (4, 7)]
    for u, v in edges:
        g.add_edge(u, v)
    
    g.display()
    
    # Recursive DFS
    print("\n--- Recursive DFS ---")
    order_rec, parent_rec = dfs_recursive(g, 0)
    print(f"Visited order: {order_rec}")
    print(f"Parent of each node: {parent_rec}")
    
    # Iterative DFS
    print("\n--- Iterative DFS ---")
    order_iter, parent_iter = dfs_iterative(g, 0)
    print(f"Visited order: {order_iter}")
    print(f"Parent of each node: {parent_iter}")
    
    # Find path using DFS
    print("\n--- Path Finding with DFS ---")
    path = dfs_path_recursive(g, 0, 7)
    print(f"Path from 0 to 7: {path}")
    
    path = dfs_path_recursive(g, 0, 8)
    print(f"Path from 0 to 8 (non-existent): {path}")
    
    # DFS with logging
    dfs_with_logging(g, 0)
    
    print("\n✅ DFS implementation complete!")
