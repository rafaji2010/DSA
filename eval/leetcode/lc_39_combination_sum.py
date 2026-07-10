"""LC 39: Combination Sum — Backtracking with reuse. Time: O(2^target/min)"""

from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    candidates.sort()  # Sort for early termination
    
    def backtrack(start: int, remaining: int, path: List[int]):
        if remaining == 0:
            result.append(path.copy())
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            num = candidates[i]
            if num > remaining:  # Early termination (sorted)
                break
            
            path.append(num)
            backtrack(i, remaining - num, path)  # i, not i+1! ← REUSE ALLOWED
            path.pop()
    
    backtrack(0, target, [])
    return result


def combinationSum_verbose(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    candidates.sort()
    
    def backtrack(start: int, remaining: int, path: List[int], depth: int = 0):
        indent = "  " * depth
        print(f"{indent}backtrack(start={start}, remaining={remaining}, path={path})")
        
        if remaining == 0:
            print(f"{indent}  ✅ SOLUTION: {path}")
            result.append(path.copy())
            return
        if remaining < 0:
            print(f"{indent}  ❌ Overflow")
            return
        
        for i in range(start, len(candidates)):
            num = candidates[i]
            if num > remaining:
                print(f"{indent}  {num} > {remaining}, break (sorted)")
                break
            
            print(f"{indent}  Try {num} at index {i}")
            path.append(num)
            backtrack(i, remaining - num, path, depth + 1)
            path.pop()
            print(f"{indent}  Backtrack: remove {num}")
    
    print(f"\n{'='*50}")
    print(f"COMBINATION SUM: candidates={candidates}, target={target}")
    print(f"{'='*50}")
    backtrack(0, target, [])
    print(f"\nTotal solutions: {len(result)}")
    return result


if __name__ == "__main__":
    # Standard test
    print("--- Standard ---")
    result = combinationSum([2, 3, 6, 7], 7)
    print(f"Result: {result}")
    
    print("\n--- Verbose ---")
    combinationSum_verbose([2, 3, 6, 7], 7)
    
    print("\n--- Another test ---")
    result = combinationSum([2, 3, 5], 8)
    print(f"[2,3,5] target=8 → {result}")