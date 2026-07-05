#!/usr/bin/env python3
"""
eval/lc_200_number_of_islands.py
LeetCode #200: Number of Islands

Pattern: Connected Components in Grid Graph
Approach: DFS to "sink" each island (mark visited as '0')

Time: O(m * n) — visit each cell once
Space: O(m * n) — recursion stack in worst case
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Count islands using DFS. Time: O(m*n), Space: O(m*n)"""
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    self._dfs(grid, r, c)
                    count += 1
        
        return count
    
    def _dfs(self, grid: List[List[str]], r: int, c: int) -> None:
        """Sink an island by marking all connected '1's as '0'."""
        rows, cols = len(grid), len(grid[0])
        
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return
        
        grid[r][c] = "0"  # Sink current cell
        
        # Explore 4 neighbors
        self._dfs(grid, r - 1, c)  # up
        self._dfs(grid, r + 1, c)  # down
        self._dfs(grid, r, c - 1)  # left
        self._dfs(grid, r, c + 1)  # right


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    
    sol = Solution()
    print(f"Number of islands: {sol.numIslands([row[:] for row in grid])}")
