"""
core/graphs/bfs_vs_dfs.py
Comparison of BFS and DFS traversals
"""

from adjacency_list import Graph
from bfs import bfs
from dfs import dfs_recursive, dfs_iterative


def compare_traversals(graph: Graph, start: int):
    """Compare BFS and DFS traversal orders."""
    print("\n" + "=" * 60)
    print(f"TRAVERSAL COMPARISON (starting from vertex {start})")
    print("=" * 60)
    
    # BFS
    bfs_order, _, bfs_distance = bfs(graph, start)
    print(f"\nBFS (Level Order):     {bfs_order}")
    print(f"  Distances from start: {bfs_distance}")
    
    # DFS Recursive
    dfs_rec_order, _ = dfs_recursive(graph, start)
    print(f"DFS Recursive:         {dfs_rec_order}")
    
    # DFS Iterative
    dfs_iter_order, _ = dfs_iterative(graph, start)
    print(f"DFS Iterative:         {dfs_iter_order}")
    
    # Analysis
    print("\n--- Analysis ---")
    print(f"BFS explores level by level, finds shortest paths")
    print(f"DFS explores depth-first, good for finding any path")
    print(f"BFS uses queue (FIFO), DFS uses stack (LIFO)")


def create_binary_tree_graph():
    """Create a binary tree as a graph."""
    g = Graph()
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
    for u, v in edges:
        g.add_edge(u, v)
    return g


def create_cycle_graph():
    """Create a cycle graph."""
    g = Graph()
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    for u, v in edges:
        g.add_edge(u, v)
    return g


if __name__ == "__main__":
    print("=" * 60)
    print("BFS vs DFS COMPARISON")
    print("=" * 60)
    
    # Example 1: Binary tree
    print("\n--- Binary Tree Graph ---")
    tree = create_binary_tree_graph()
    tree.display()
    compare_traversals(tree, 1)
    
    # Example 2: Cycle graph
    print("\n--- Cycle Graph ---")
    cycle = create_cycle_graph()
    cycle.display()
    compare_traversals(cycle, 0)
    
    print("\n" + "=" * 60)
    print("SUMMARY: WHEN TO USE BFS vs DFS")
    print("=" * 60)
    print("""
    ┌─────────────────────────────────────────────────────────────────┐
    │                    BFS                          DFS            │
    ├─────────────────────────────────────────────────────────────────┤
    │ Shortest path          ✅ Best                ❌ Not guarantee │
    │ Level order            ✅ Natural             ❌ No            │
    │ Memory usage           ❌ O(width)            ✅ O(height)     │
    │ Finding any path       ✅ Works               ✅ Works         │
    │ Cycle detection        ✅ Works               ✅ Works         │
    │ Topological sort       ❌ No                  ✅ Yes (postorder)│
    │ Connected components   ✅ Works               ✅ Works         │
    └─────────────────────────────────────────────────────────────────┘
    """)
    
    print("✅ BFS vs DFS comparison complete!")
