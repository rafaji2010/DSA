"""
core/trie/trie.py
Trie (Prefix Tree) Implementation
"""

from typing import Dict, List, Optional


class TrieNode:
    """
    A single node in the Trie.
    
    Each node contains:
    - children: Dictionary mapping character → child node
    - is_end: Boolean indicating if this node completes a word
    """
    
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end: bool = False
    
    def __repr__(self) -> str:
        return f"TrieNode(children={list(self.children.keys())}, is_end={self.is_end})"


class Trie:
    """
    Trie data structure for efficient string operations.
    
    Time Complexity:
    - insert: O(m) where m = length of word
    - search: O(m)
    - starts_with: O(m)
    
    Space Complexity: O(n * m) where n = number of words
    """
    
    def __init__(self):
        self.root = TrieNode()
        self._word_count = 0
    
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
        
        Time: O(m) where m = len(word)
        """
        node = self.root
        
        for char in word:
            # If character doesn't exist, create new node
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to child node
            node = node.children[char]
        
        # Mark end of word
        if not node.is_end:
            node.is_end = True
            self._word_count += 1
    
    def search(self, word: str) -> bool:
        """
        Check if exact word exists in trie.
        
        Time: O(m) where m = len(word)
        """
        node = self._traverse(word)
        return node is not None and node.is_end
    
    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word in trie starts with given prefix.
        
        Time: O(m) where m = len(prefix)
        """
        node = self._traverse(prefix)
        return node is not None
    
    def _traverse(self, prefix: str) -> Optional[TrieNode]:
        """
        Traverse the trie following the prefix.
        Returns the last node if prefix exists, None otherwise.
        """
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        
        return node
    
    def get_words(self) -> List[str]:
        """
        Get all words in the trie.
        
        Time: O(n * m) where n = number of words, m = average length
        """
        result = []
        self._collect_words(self.root, "", result)
        return result
    
    def _collect_words(self, node: TrieNode, prefix: str, result: List[str]) -> None:
        """DFS to collect all words."""
        if node.is_end:
            result.append(prefix)
        
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, result)
    
    def autocomplete(self, prefix: str, limit: int = 10) -> List[str]:
        """
        Return all words starting with given prefix.
        
        Time: O(m + k) where m = prefix length, k = number of matches
        """
        node = self._traverse(prefix)
        if node is None:
            return []
        
        result = []
        self._collect_words(node, prefix, result)
        
        # Sort and limit results
        result.sort()
        return result[:limit]
    
    def __len__(self) -> int:
        return self._word_count
    
    def __contains__(self, word: str) -> bool:
        return self.search(word)
    
if __name__ == "__main__":
    print("=" * 60)
    print("TRIE DATA STRUCTURE DEMONSTRATION")
    print("=" * 60)
    
    # Create a new trie
    trie = Trie()
    print(f"\nCreated empty trie")
    
    # Insert words
    words = ["cat", "car", "cart", "dog", "do", "dot"]
    print(f"\nInserting words: {words}")
    for word in words:
        trie.insert(word)
        print(f"  Inserted '{word}'")
    
    print(f"\nTotal words in trie: {len(trie)}")
    print(f"All words: {trie.get_words()}")
    
    # Search tests
    print("\n" + "-" * 40)
    print("SEARCH TESTS")
    print("-" * 40)
    
    test_words = ["cat", "car", "ca", "dog", "doe", "dot"]
    for word in test_words:
        result = trie.search(word)
        print(f"  Search '{word}': {'✅ Found' if result else '❌ Not found'}")
    
    # Prefix tests
    print("\n" + "-" * 40)
    print("PREFIX TESTS")
    print("-" * 40)
    
    prefixes = ["ca", "do", "c", "d", "x"]
    for prefix in prefixes:
        result = trie.starts_with(prefix)
        words_with_prefix = trie.autocomplete(prefix)
        print(f"  Starts with '{prefix}': {'✅ Yes' if result else '❌ No'}")
        if result:
            print(f"    Words: {words_with_prefix}")
    
    # Autocomplete tests
    print("\n" + "-" * 40)
    print("AUTOCOMPLETE TESTS")
    print("-" * 40)
    
    autocomplete_tests = ["ca", "do", "c", "d", "cat"]
    for prefix in autocomplete_tests:
        suggestions = trie.autocomplete(prefix)
        print(f"  Autocomplete '{prefix}': {suggestions}")
    
    # Demonstrate word count
    print("\n" + "-" * 40)
    print("ADDITIONAL INSERTS")
    print("-" * 40)
    
    print(f"Before inserting 'cat' again: word count = {len(trie)}")
    trie.insert("cat")  # Duplicate insert should not increase count
    print(f"After inserting 'cat' again: word count = {len(trie)} (unchanged)")
    
    print("\n✅ Trie implementation complete!")