"""
core/tag_clustering.py
Cluster related photo tags using Union-Find
"""
import sys
import os
from typing import List, Dict, Set, Tuple

# Add parent directory to path (go up two levels: graphs -> core -> DSA)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.graphs.union_find_2 import UnionFind

class TagClusterer:
    """
    Cluster related photo tags using Union-Find.
    
    Example:
        tags: ["sunset", "golden-hour", "evening", "beach", "ocean"]
        relationships: [
            ("sunset", "golden-hour"),
            ("sunset", "evening"),
            ("beach", "ocean"),
            ("beach", "sunset")
        ]
        After clustering:
            Cluster 1: ["sunset", "golden-hour", "evening", "beach", "ocean"]
            (All connected through sunset-beach relationship)
    """
    
    def __init__(self):
        self.tag_to_id: Dict[str, int] = {}
        self.id_to_tag: Dict[int, str] = {}
        self.uf: Optional[UnionFind] = None
    
    def _get_id(self, tag: str) -> int:
        """Get or create ID for a tag."""
        if tag not in self.tag_to_id:
            idx = len(self.tag_to_id)
            self.tag_to_id[tag] = idx
            self.id_to_tag[idx] = tag
        return self.tag_to_id[tag]
    
    def add_relationship(self, tag1: str, tag2: str) -> None:
        """
        Add a relationship between two tags.
        They will be considered part of the same cluster.
        """
        id1 = self._get_id(tag1)
        id2 = self._get_id(tag2)
        
        # Lazy initialize Union-Find when we have IDs
        if self.uf is None:
            self.uf = UnionFind(2)
        elif len(self.tag_to_id) > len(self.uf.parent):
            # Rebuild Union-Find with new size
            new_uf = UnionFind(len(self.tag_to_id))
            # Copy existing unions
            for i in range(len(self.uf.parent)):
                new_uf.parent[i] = self.uf.parent[i] if i < len(self.uf.parent) else i
            self.uf = new_uf
        
        self.uf.union(id1, id2)
    
    def get_clusters(self) -> List[List[str]]:
        """Return tag clusters as lists of tag names."""
        if self.uf is None:
            return []
        
        # Get all sets from Union-Find
        sets = self.uf.get_sets()
        
        # Convert IDs back to tag names
        clusters = []
        for s in sets:
            cluster = [self.id_to_tag[i] for i in s if i in self.id_to_tag]
            if cluster:
                clusters.append(cluster)
        
        return clusters
    
    def get_cluster_for_tag(self, tag: str) -> List[str]:
        """Get the cluster containing a specific tag."""
        if tag not in self.tag_to_id:
            return []
        
        if self.uf is None:
            return [tag]
        
        tag_id = self.tag_to_id[tag]
        root = self.uf.find(tag_id)
        
        cluster = []
        for idx, name in self.id_to_tag.items():
            if self.uf.find(idx) == root:
                cluster.append(name)
        
        return cluster

if __name__ == "__main__":
    print("=== Tag Clustering ===")
    
    clusterer = TagClusterer()
    
    # Add tag relationships
    relationships = [
        ("sunset", "golden-hour"),
        ("sunset", "evening"),
        ("beach", "ocean"),
        ("beach", "sunset"),  # Connects the two groups!
        ("portrait", "bokeh"),
        ("portrait", "depth-of-field")
    ]
    
    for tag1, tag2 in relationships:
        clusterer.add_relationship(tag1, tag2)
    
    print("Relationships added:", relationships)
    
    print("\nTag Clusters:")
    for i, cluster in enumerate(clusterer.get_clusters(), 1):
        print(f"Cluster {i}: {cluster}")
    
    print(f"\nTags related to 'beach': {clusterer.get_cluster_for_tag('beach')}")
    print(f"Tags related to 'portrait': {clusterer.get_cluster_for_tag('portrait')}")