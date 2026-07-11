"""LC 52: N-Queens II — Count solutions only. Time: O(N!), Space: O(N)"""

from typing import List


def totalNQueens(n: int) -> int:
    """Return number of distinct N-Queens solutions."""
    count = 0
    
    # Use sets for O(1) conflict checking
    cols = set()      # Columns with queens
    diag1 = set()     # r + c (anti-diagonals)
    diag2 = set()     # r - c (main diagonals)
    
    def backtrack(row: int):
        nonlocal count
        
        if row == n:
            count += 1
            return
        
        for col in range(n):
            # Check if (row, col) is under attack
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue
            
            # Place queen
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)
            
            backtrack(row + 1)
            
            # Remove queen (backtrack)
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)
    
    backtrack(0)
    return count


def totalNQueens_verbose(n: int) -> int:
    """Verbose version showing the optimized approach."""
    count = 0
    cols = set()
    diag1 = set()
    diag2 = set()
    
    def backtrack(row: int, depth: int = 0):
        nonlocal count
        indent = "  " * depth
        
        if row == n:
            count += 1
            print(f"{indent}✅ Solution #{count} found!")
            return
        
        print(f"{indent}Row {row}: trying columns 0-{n-1}")
        for col in range(n):
            conflicts = []
            if col in cols:
                conflicts.append(f"col {col} occupied")
            if (row + col) in diag1:
                conflicts.append(f"anti-diag {row+col} occupied")
            if (row - col) in diag2:
                conflicts.append(f"main-diag {row-col} occupied")
            
            if conflicts:
                print(f"{indent}  col {col}: ❌ {'; '.join(conflicts)}")
                continue
            
            print(f"{indent}  col {col}: ✅ Place queen")
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)
            
            backtrack(row + 1, depth + 1)
            
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)
            print(f"{indent}  col {col}: ← Backtrack, remove queen")
    
    print(f"\n{'='*50}")
    print(f"N-QUEENS II: N={n}")
    print(f"{'='*50}")
    backtrack(0)
    print(f"\nTotal solutions: {count}")
    return count


if __name__ == "__main__":
    print("=" * 50)
    print("N-QUEENS II")
    print("=" * 50)
    
    for n in [1, 2, 3, 4, 5]:
        result = totalNQueens(n)
        print(f"N={n} → {result} solution(s)")
    
    print("\n--- Verbose N=4 ---")
    totalNQueens_verbose(4)