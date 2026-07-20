"""
LeetCode 1463 - Cherry Pickup II
Approach 1: Top-Down DFS with Memoization
- Move both robots row by row.
- At each row, try all nine combinations of moves for the two robots.
- Memoize states by `(row, col1, col2)` to avoid repeated work.
Time: O(rows * cols^2 * 9)
Space: O(rows * cols^2)

Approach 2: Bottom-Up DP
- Iterate from the last row upward.
- For each pair of columns, compute the best total cherries using the next row's DP table.
Time: O(rows * cols^2 * 9)
Space: O(cols^2)
"""

from itertools import product


class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Grid dimensions.
        row = len(grid)
        col = len(grid[0])

        # Memo table for overlapping subproblems.
        map = {}

        # DFS returns the best total cherries from row r with robots at c1 and c2.
        def dfs(r, c1, c2):
            if c1 == c2 or min(c1, c2) < 0 or max(c1, c2) == col:
                return 0
            if (r, c1, c2) in map:
                return map[(r, c1, c2)]
            if r == row - 1:
                return grid[r][c1] + grid[r][c2]

            res = 0
            for drc1 in [-1, 0, 1]:
                for drc2 in [-1, 0, 1]:
                    res = max(res, grid[r][c1] + grid[r][c2] + dfs(r + 1, c1 + drc1, c2 + drc2))

            map[(r, c1, c2)] = res
            return map[(r, c1, c2)]

        return dfs(0, 0, col - 1)


class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Grid dimensions.
        row = len(grid)
        col = len(grid[0])

        # dp[c1][c2] stores the best result for the next row.
        dp = [[0] * col for _ in range(col)]

        # Process rows from bottom to top.
        for r in reversed(range(row)):
            curr_dp = [[0] * col for _ in range(col)]

            for c1 in range(col - 1):
                for c2 in range(c1 + 1, col):
                    max_cherry = 0
                    cherry = grid[r][c1] + grid[r][c2]

                    # Try every pair of next moves for the two robots.
                    for drc1, drc2 in product([-1, 0, 1], [-1, 0, 1]):
                        nc1, nc2 = c1 + drc1, c2 + drc2
                        if nc1 < 0 or nc2 == col:
                            continue

                        max_cherry = max(max_cherry, cherry + dp[nc1][nc2])

                    curr_dp[c1][c2] = max_cherry

            dp = curr_dp

        return dp[0][col - 1]
