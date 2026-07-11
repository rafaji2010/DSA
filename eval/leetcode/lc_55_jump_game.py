"""LC 55: Jump Game — Greedy approach. Time: O(n), Space: O(1)"""

from typing import List


def canJump(nums: List[int]) -> bool:
    """Return True if you can reach the last index from index 0."""
    max_reach = 0  # Farthest index we can get to
    
    for i, jump in enumerate(nums):
        # If current index is beyond our reach, we can't get here
        if i > max_reach:
            return False
        
        # Update farthest reachable index
        max_reach = max(max_reach, i + jump)
        
        # Early exit: if we can already reach the end
        if max_reach >= len(nums) - 1:
            return True
    
    return True  # If we finish the loop, we can reach the end


def canJump_verbose(nums: List[int]) -> bool:
    """Verbose version showing each step."""
    max_reach = 0
    n = len(nums)
    
    print(f"\nArray: {nums}")
    print(f"Target: reach index {n - 1}\n")
    
    for i, jump in enumerate(nums):
        print(f"  i={i}, jump={jump}, max_reach={max_reach}")
        
        if i > max_reach:
            print(f"  ❌ i={i} > max_reach={max_reach}. CANNOT reach here!")
            return False
        
        max_reach = max(max_reach, i + jump)
        print(f"  → max_reach updated to {max_reach}")
        
        if max_reach >= n - 1:
            print(f"  ✅ Can reach end (index {n - 1})!")
            return True
    
    return True


if __name__ == "__main__":
    test_cases = [
        [2, 3, 1, 1, 4],   # True
        [3, 2, 1, 0, 4],   # False
        [0],               # True (already at end)
        [2, 0, 0],        # True
        [1, 1, 1, 1],     # True
    ]
    
    print("=" * 50)
    print("JUMP GAME — Greedy Solution")
    print("=" * 50)
    
    for nums in test_cases:
        result = canJump_verbose(nums)
        print(f"  Result: {result}\n")
    
    print("--- Quick Verification ---")
    for nums in test_cases:
        print(f"  {nums} → {canJump(nums)}")