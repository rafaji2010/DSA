# eval/lc_046_permutations.py
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    """
    LeetCode 46: Permutations
    Time: O(N * N!) | Space: O(N)
    """
    result: List[List[int]] = []
    used: List[bool] = [False] * len(nums)
    
    def backtrack(current_path: List[int]) -> None:
        # Base Case: Path is same length as nums (full permutation)
        if len(current_path) == len(nums):
            result.append(current_path[:])
            return
            
        # Try every number for the next position
        for i in range(len(nums)):
            if not used[i]:
                # 1. Make a choice
                used[i] = True
                current_path.append(nums[i])
                
                # 2. Recurse
                backtrack(current_path)
                
                # 3. Undo the choice (Backtrack)
                current_path.pop()
                used[i] = False

    backtrack([])
    return result

if __name__ == "__main__":
    print(f"Permutations of [1,2,3]: {permute([1, 2, 3])}")
    # Expected: 6 permutations