"""
LeetCode 1091 - Shortest Path in Binary Matrix
Approach:
- Run a BFS from the top-left cell.
- Explore all eight directions from each cell.
- Mark visited cells in the grid itself to avoid revisiting them.
Time: O(n^2)
Space: O(n^2)
"""

from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # A blocked starting cell means no path exists.
        if grid[0][0]:
            return -1

        # Grid is n x n.
        n = len(grid)

        # All eight possible moves from a cell.
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        queue = deque([(0, 0)])
        grid[0][0] = 1
        path = 1

        # BFS level order; each level represents one path length.
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                if i == n - 1 and j == n - 1:
                    return path

                for dr, dc in moves:
                    nr = i + dr
                    nc = j + dc

                    # Skip out-of-bounds or already visited/blocked cells.
                    if nr < 0 or nc < 0 or nr == n or nc == n or grid[nr][nc]:
                        continue

                    queue.append((nr, nc))
                    grid[nr][nc] = 1

            path += 1

        return -1
