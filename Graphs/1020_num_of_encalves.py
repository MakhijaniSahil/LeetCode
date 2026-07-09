"""
LeetCode 1020 - Number of Enclaves
Approach:
- Start DFS from every border land cell and mark all reachable land as safe.
- Count the land cells that remain unmarked, since those are enclaves.
Time: O(m * n)
Space: O(m * n)
"""


class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Grid dimensions.
        m = len(grid)
        n = len(grid[0])

        # Mark all land connected to the border.
        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or grid[r][c] != 1:
                return
            grid[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Flood fill from all border cells.
        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)

        # Count the remaining land cells that are fully enclosed.
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res += 1

        return res
