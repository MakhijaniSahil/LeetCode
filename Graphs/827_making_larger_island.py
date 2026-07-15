"""
LeetCode 827 - Making A Large Island
Approach:
- Label each island with a unique id and store its size.
- For every water cell, check the distinct neighboring islands it could connect.
- The best answer is either the largest existing island or one flipped cell plus its neighbors.
Time: O(n^2)
Space: O(n^2)
"""

from collections import defaultdict


class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Grid is n x n.
        n = len(grid)

        # Boundary check helper.
        def check(r, c):
            return r < 0 or c < 0 or r == n or c == n

        # Four-directional movement.
        moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        # Label one island and return its size.
        def dfs(r, c, label):
            if check(r, c) or grid[r][c] != 1:
                return 0

            grid[r][c] = label
            size = 1

            for dr, dc in moves:
                nr = dr + r
                nc = dc + c
                size += dfs(nr, nc, label)

            return size

        # size[label] stores the area of that island.
        size = defaultdict(int)
        label = 2
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size[label] = dfs(r, c, label)
                    label += 1

        # Compute the size created by flipping a zero cell.
        def connect(r, c):
            res = 1
            visit = set([0])

            for dr, dc in moves:
                nr = r + dr
                nc = c + dc
                if not check(nr, nc) and grid[nr][nc] not in visit:
                    res += size[grid[nr][nc]]
                    visit.add(grid[nr][nc])

            return res

        # If the grid has no zeroes, the whole grid is already one island.
        res = 0 if not size else max(size.values())

        # Try flipping every zero and keep the largest merged island.
        for r in range(n):
            for c in range(n):
                if not grid[r][c]:
                    res = max(res, connect(r, c))

        return res
