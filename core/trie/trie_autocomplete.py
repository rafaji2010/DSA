"""
core/trie/trie_autocomplete.py
Practical autocomplete application using Trie
"""

from trie import Trie
from typing import List


class AutocompleteSystem:
    """
    Real-world autocomplete system using Trie.
    """
    
    def __init__(self):
        self.trie = Trie()
        self._word_frequency = {}  # Track frequency for sorting
    
    def add_word(self, word: str) -> None:
        """Add a word to the autocomplete system."""
        self.trie.insert(word)
        self._word_frequency[word] = self._word_frequency.get(word, 0) + 1
    
    def get_suggestions(self, prefix: str, limit: int = 5) -> List[str]:
        """
        Get autocomplete suggestions for given prefix.
        Sorted by frequency then alphabetically.
        """
        words = self.trie.autocomplete(prefix, limit * 2)  # Get more for sorting
        
        # Sort by frequency (higher first), then alphabetically
        words.sort(key=lambda w: (-self._word_frequency.get(w, 0), w))
        
        return words[:limit]
    
    def add_corpus(self, words: List[str]) -> None:
        """Add multiple words to the system."""
        for word in words:
            self.add_word(word)


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("TRIE AUTOCOMPLETE DEMONSTRATION")
    print("=" * 60)
    
    # Create autocomplete system
    auto = AutocompleteSystem()
    
    # Add common words
    corpus = [
        "cat", "car", "cart", "catalog", "cathedral",
        "dog", "do", "dot", "dolphin", "dollar",
        "hello", "help", "helium", "helicopter", "hello world"
    ]
    auto.add_corpus(corpus)
    
    print(f"\nWords in trie: {auto.trie.get_words()}")
    
    # Test autocomplete
    prefixes = ["ca", "do", "he", "cat", "z"]
    
    for prefix in prefixes:
        suggestions = auto.get_suggestions(prefix)
        print(f"\nAutocomplete for '{prefix}':")
        if suggestions:
            for word in suggestions:
                print(f"  - {word}")
        else:
            print(f"  No suggestions found")
    
    # Add more occurrences to affect frequency
    print("\n--- Adding more 'cat' occurrences ---")
    auto.add_word("cat")
    auto.add_word("cat")
    
    suggestions = auto.get_suggestions("ca")
    print(f"\nAutocomplete for 'ca' after frequency update:")
    for word in suggestions:
        print(f"  - {word}")