# eval/lc_078_subsets.py
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    """
    LeetCode 78: Subsets
    Time: O(N * 2^N) | Space: O(N) for recursion stack
    """
    result: List[List[int]] = []
    
    def backtrack(index: int, current_path: List[int]) -> None:
        # Base Case: We've made a decision for every number
        if index == len(nums):
            # CRITICAL: Append a COPY of the path! 
            # If we append the reference, it will be mutated later.
            result.append(current_path[:])
            return
            
        # Choice 1: INCLUDE nums[index]
        current_path.append(nums[index])
        backtrack(index + 1, current_path)
        
        # Choice 2: EXCLUDE nums[index] (Backtrack)
        # We undo the choice by popping the element we just added
        current_path.pop()
        backtrack(index + 1, current_path)

    backtrack(0, [])
    return result

if __name__ == "__main__":
    print(f"Subsets of [1,2,3]: {subsets([1, 2, 3])}")
    # Expected: [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]