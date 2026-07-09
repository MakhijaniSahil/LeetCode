"""
LeetCode 200 - Number of Islands
Approach:
- Scan every cell in the grid.
- When a land cell is found, start a DFS to sink the entire island.
- Count how many times we start a new DFS.
Time: O(m * n)
Space: O(m * n)
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Grid dimensions.
        m = len(grid)
        n = len(grid[0])

        # Flood fill the current island by turning land into water.
        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Count how many distinct islands we encounter.
        island = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    island += 1
                    dfs(r,c)

        return island
