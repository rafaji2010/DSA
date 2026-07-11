"""LC 79: Word Search — DFS with backtracking on 2D grid."""

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """Return True if word exists in board."""
    if not board or not board[0]:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def backtrack(r: int, c: int, index: int) -> bool:
        # Base case: all characters matched
        if index == len(word):
            return True
        
        # Out of bounds or mismatch
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[index]:
            return False
        
        # Mark as visited (temporarily modify board)
        temp = board[r][c]
        board[r][c] = '#'  # Any marker not in word
        
        # Explore 4 directions: up, down, left, right
        found = (
            backtrack(r - 1, c, index + 1) or  # up
            backtrack(r + 1, c, index + 1) or  # down
            backtrack(r, c - 1, index + 1) or  # left
            backtrack(r, c + 1, index + 1)     # right
        )
        
        # BACKTRACK: restore original character
        board[r][c] = temp
        
        return found
    
    # Try starting from every cell matching word[0]
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                if backtrack(r, c, 0):
                    return True
    
    return False


def exist_verbose(board: List[List[str]], word: str) -> bool:
    """Verbose version showing DFS path."""
    rows, cols = len(board), len(board[0])
    path = []
    
    def backtrack(r: int, c: int, index: int, depth: int = 0) -> bool:
        indent = "  " * depth
        
        # Out of bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            print(f"{indent}  ({r},{c}) out of bounds")
            return False
        
        # Mismatch
        if board[r][c] != word[index]:
            print(f"{indent}  ({r},{c})='{board[r][c]}' != '{word[index]}'")
            return False
        
        path.append((r, c))
        print(f"{indent}✅ Match '{word[index]}' at ({r},{c}), path={path}")
        
        # Base case
        if index == len(word) - 1:
            print(f"{indent}🎉 WORD FOUND! Path: {path}")
            path.pop()
            return True
        
        # Mark visited
        temp = board[r][c]
        board[r][c] = '#'
        
        # Explore 4 directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dir_names = ['up', 'down', 'left', 'right']
        
        found = False
        for (dr, dc), name in zip(directions, dir_names):
            nr, nc = r + dr, c + dc
            print(f"{indent}  Try {name} to ({nr},{nc})")
            if backtrack(nr, nc, index + 1, depth + 1):
                found = True
                break
        
        # Backtrack
        board[r][c] = temp
        path.pop()
        
        if not found:
            print(f"{indent}  Dead end at ({r},{c}), backtracking...")
        
        return found
    
    print(f"\n{'='*50}")
    print(f"WORD SEARCH: looking for '{word}'")
    print(f"{'='*50}")
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                print(f"\nStart from ({r},{c})='{word[0]}'")
                if backtrack(r, c, 0):
                    return True
    
    print(f"\n❌ Word '{word}' NOT FOUND")
    return False


if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    
    tests = [
        ("ABCCED", True),
        ("SEE", True),
        ("ABCB", False),
    ]
    
    print("=" * 50)
    print("WORD SEARCH")
    print("=" * 50)
    
    for word, expected in tests:
        # Make a copy since board gets modified
        board_copy = [row[:] for row in board]
        result = exist(board_copy, word)
        status = "✅" if result == expected else "❌"
        print(f"\n{status} '{word}' → {result} (expected {expected})")
    
    print("\n--- Verbose Trace ---")
    board_copy = [row[:] for row in board]
    exist_verbose(board_copy, "ABCCED")