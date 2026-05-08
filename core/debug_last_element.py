"""
Focused debug - only test the failing case
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

def buggy_binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        breakpoint()  # Debugger stops here
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

if __name__ == "__main__":
    # Only test the failing case
    arr = [1, 2, 3, 4, 5]
    target = 5
    print(f"Searching for {target} in {arr}")
    result = buggy_binary_search(arr, target)
    print(f"Result: {result} (expected: 4)")