
from typing import List

def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    """
    LeetCode 40: Combination Sum II
    Each number used once. Input may contain duplicates. Output must be unique.
    Time: O(2^N) | Space: O(N)
    """
    result: List[List[int]] = []
    candidates.sort() # CRITICAL: Sort to group duplicates together

    def backtrack(start: int, current_path: List[int], remaining: int) -> None:
        if remaining == 0:
            result.append(current_path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            # Skip duplicates at the same tree level
            if i > start and candidates[i] == candidates[i - 1]:
                continue
                
            current_path.append(candidates[i])
            # Pass i + 1 because we CANNOT reuse the same element
            backtrack(i + 1, current_path, remaining - candidates[i])
            current_path.pop()

    backtrack(0, [], target)
    return result

if __name__ == "__main__":
    c1 = [10, 1, 2, 7, 6, 1, 5]
    t1 = 8
    print(f"Candidates: {c1}, Target: {t1}")
    print(f"Results: {combination_sum2(c1, t1)}")
    # Expected: [[1,1,6], [1,2,5], [1,7], [2,6]]