"""
LeetCode 1260 - Shift 2D Grid
Approach:
- Treat the grid as a flattened array of length `m * n`.
- Move each element forward by `k` positions with wraparound.
- Convert the destination index back into 2D coordinates.
Time: O(m * n)
Space: O(m * n)
"""


class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Grid dimensions.
        m = len(grid)
        n = len(grid[0])

        # Total number of cells.
        e = m * n
        k %= e
        if k == 0:
            return grid

        # Result grid initialized with zeros.
        res = [[0] * n for _ in range(m)]

        # Map each source cell to its shifted destination.
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                newIdx = (idx + k) % e
                x = newIdx // n
                y = newIdx % n
                res[x][y] = grid[i][j]

        return res
