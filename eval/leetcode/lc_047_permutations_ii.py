
from typing import List

def permute_unique(nums: List[int]) -> List[List[int]]:
    """
    LeetCode 47: Permutations II
    Contains duplicates. Output must be unique.
    Time: O(N * N!) | Space: O(N)
    """
    result: List[List[int]] = []
    nums.sort() # CRITICAL: Sort to group duplicates
    used = [False] * len(nums)

    def backtrack(current_path: List[int]) -> None:
        if len(current_path) == len(nums):
            result.append(current_path[:])
            return

        for i in range(len(nums)):
            # Skip if already used in current path
            if used[i]:
                continue
            
            # Skip duplicates: if current is same as prev, 
            # ONLY skip if the previous duplicate was NOT used 
            # (meaning we are starting a new branch at the same depth)
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            current_path.append(nums[i])
            
            backtrack(current_path)
            
            current_path.pop()
            used[i] = False

    backtrack([])
    return result

if __name__ == "__main__":
    n1 = [1, 1, 2]
    print(f"Nums: {n1}")
    print(f"Permutations: {permute_unique(n1)}")
    # Expected: [[1,1,2], [1,2,1], [2,1,1]]