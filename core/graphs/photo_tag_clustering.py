"""
core/graphs/photo_tag_clustering.py
Use Union-Find to cluster photo tags
"""
import sys
import os

# Add parent directory to path so 'core' can be found
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.graphs.union_find_2 import UnionFind

# Tags indexed
tags = {
    0: "landscape",
    1: "sunset",
    2: "mountains",
    3: "portrait",
    4: "urban",
    5: "nature",
    6: "cityscape"
}

# Edges: two tags often appear together (weight = frequency)
tag_edges = [
    (5, 0, 1),   # landscape-sunset: 5 times
    (3, 0, 2),   # landscape-mountains: 3 times
    (2, 1, 2),   # sunset-mountains: 2 times
    (1, 3, 4),   # portrait-urban: 1 time
    (4, 4, 6),   # urban-cityscape: 4 times
    (2, 5, 6),   # nature-cityscape: 2 times
]

uf = UnionFind(7)

print("Tag clusters (highly related tags):")
for weight, u, v in sorted(tag_edges, key=lambda x: -x[0]):
    if uf.union(u, v):
        print(f"  Cluster: {tags[u]} ↔ {tags[v]}")

print(f"\nTotal clusters: {uf.components()}")