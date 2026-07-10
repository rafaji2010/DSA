"""LC 131: Palindrome Partitioning — Backtracking over substrings."""

from typing import List


def partition(s: str) -> List[List[str]]:
    result = []
    n = len(s)
    
    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]
    
    def backtrack(start: int, path: List[str]):
        if start == n:
            result.append(path.copy())
            return
        
        for end in range(start + 1, n + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)  # Move to next position after this cut
                path.pop()
    
    backtrack(0, [])
    return result


def partition_verbose(s: str) -> List[List[str]]:
    result = []
    n = len(s)
    
    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]
    
    def backtrack(start: int, path: List[str], depth: int = 0):
        indent = "  " * depth
        print(f"{indent}backtrack(start={start}, path={path})")
        
        if start == n:
            print(f"{indent}  ✅ PARTITION: {path}")
            result.append(path.copy())
            return
        
        for end in range(start + 1, n + 1):
            substring = s[start:end]
            is_pal = is_palindrome(substring)
            status = "✅ palindrome" if is_pal else "❌ not palindrome"
            print(f"{indent}  Cut [{start}:{end}] = '{substring}' → {status}")
            
            if is_pal:
                path.append(substring)
                backtrack(end, path, depth + 1)
                path.pop()
                print(f"{indent}  Backtrack: remove '{substring}'")
    
    print(f"\n{'='*50}")
    print(f"PALINDROME PARTITIONING: '{s}'")
    print(f"{'='*50}")
    backtrack(0, [])
    print(f"\nTotal partitions: {len(result)}")
    return result


if __name__ == "__main__":
    print("--- Standard ---")
    result = partition("aab")
    print(f"'aab' → {result}")
    
    print("\n--- Verbose ---")
    partition_verbose("aab")
    
    print("\n--- Another test ---")
    result = partition("a")
    print(f"'a' → {result}")