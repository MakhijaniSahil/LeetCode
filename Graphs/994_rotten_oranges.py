"""
LeetCode 994 - Rotting Oranges
Approach:
- Start a multi-source BFS from every rotten orange.
- Process the grid level by level, where each level represents one minute.
- Rot fresh oranges adjacent to the current frontier and count down until none remain.
Time: O(rows * cols)
Space: O(rows * cols)
"""

from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Grid dimensions.
        rows = len(grid)
        cols = len(grid[0])

        # Count fresh oranges and collect all initially rotten oranges.
        fresh = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        # No fresh oranges means no time is needed.
        if fresh == 0:
            return 0

        # Four-directional movement.
        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # BFS level traversal, one minute per layer.
        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Fresh neighbors become rotten and join the next layer.
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            minutes += 1

        return minutes if not fresh else -1
