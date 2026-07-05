# core/graphs/kruskal.py

import sys
import os
# Add project root to path so we can import 'core'
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from typing import List, Tuple
from core.graphs.union_find import UnionFind

def kruskal_mst(num_nodes: int, edges: List[Tuple[int, int, int]]) -> Tuple[List[Tuple[int, int, int]], int]:
    """
    Kruskal's Algorithm for Minimum Spanning Tree.
    edges: List of (weight, node1, node2)
    Returns: (list of edges in MST, total weight of MST)
    """
    # 1. Sort edges by weight
    edges.sort(key=lambda x: x[0])
    
    uf = UnionFind(num_nodes)
    mst: List[Tuple[int, int, int]] = []
    total_weight: int = 0
    
    for weight, u, v in edges:
        # 2. If adding this edge doesn't form a cycle
        if uf.union(u, v):
            mst.append((weight, u, v))
            total_weight += weight
            
        # Optimization: MST has exactly (num_nodes - 1) edges
        if len(mst) == num_nodes - 1:
            break
            
    return mst, total_weight

if __name__ == "__main__":
    # Graph: 4 nodes
    # Edges: (weight, node1, node2)
    graph_edges = [
        (10, 0, 1),
        (6, 0, 2),
        (5, 0, 3),
        (15, 1, 3),
        (4, 2, 3)
    ]
    
    print("Running Kruskal's MST...")
    mst, weight = kruskal_mst(4, graph_edges)
    
    print("\nEdges in MST:")
    for w, u, v in mst:
        print(f"  {u} -- {v} (weight: {w})")
        
    print(f"\nTotal Minimum Weight: {weight}")  # Expected: 19 (4+5+10)