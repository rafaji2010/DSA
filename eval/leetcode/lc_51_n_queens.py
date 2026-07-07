"""LC 51: N-Queens — Backtracking. Time: O(N!), Space: O(N)"""

from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    """Return all distinct solutions for N-Queens."""
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def is_safe(row: int, col: int) -> bool:
        """Check if placing queen at (row, col) is safe."""
        # Check column (rows above only, since we place row by row)
        for r in range(row):
            if board[r][col] == 'Q':
                return False
        
        # Check upper-left diagonal
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        
        # Check upper-right diagonal
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1
        
        return True
    
    def backtrack(row: int):
        """Try placing queen in each column of current row."""
        if row == n:
            # All queens placed successfully!
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'  # BACKTRACK: remove queen
    
    backtrack(0)
    return result


def solveNQueens_verbose(n: int) -> List[List[str]]:
    """Verbose version showing backtracking steps."""
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    call_count = [0]
    
    def is_safe(row: int, col: int) -> bool:
        for r in range(row):
            if board[r][col] == 'Q':
                return False
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1
        return True
    
    def backtrack(row: int, depth: int = 0):
        call_count[0] += 1
        indent = "  " * depth
        
        if row == n:
            print(f"{indent}✅ SOLUTION FOUND!")
            solution = [''.join(r) for r in board]
            for line in solution:
                print(f"{indent}  {line}")
            result.append(solution)
            return
        
        print(f"{indent}Row {row}: trying columns 0-{n-1}")
        for col in range(n):
            if is_safe(row, col):
                print(f"{indent}  Place Q at ({row},{col})")
                board[row][col] = 'Q'
                backtrack(row + 1, depth + 1)
                board[row][col] = '.'
                print(f"{indent}  Backtrack: remove Q from ({row},{col})")
            else:
                print(f"{indent}  ({row},{col}) under attack, skip")
    
    print(f"\n{'='*50}")
    print(f"N-QUEENS BACKTRACKING (N={n})")
    print(f"{'='*50}\n")
    backtrack(0)
    print(f"\nTotal recursive calls: {call_count[0]}")
    print(f"Total solutions: {len(result)}")
    return result


if __name__ == "__main__":
    # Quick test
    print("--- N = 1 ---")
    solutions = solveNQueens(1)
    print(f"Solutions: {len(solutions)}")
    for sol in solutions:
        for row in sol:
            print(f"  {row}")
        print()
    
    print("--- N = 4 ---")
    solutions = solveNQueens(4)
    print(f"Solutions: {len(solutions)}")
    for sol in solutions:
        for row in sol:
            print(f"  {row}")
        print()
    
    # Verbose for N=4
    print("\n--- VERBOSE TRACE (N=4) ---")
    solveNQueens_verbose(4)