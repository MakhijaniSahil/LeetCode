"""
LeetCode 1631 - Path With Minimum Effort
Approach:
- Use Dijkstra's algorithm with a min-heap.
- Each state tracks the maximum edge effort seen so far on that path.
- Always expand the path with the smallest current effort first.
Time: O(rows * cols * log(rows * cols))
Space: O(rows * cols)
"""

import heapq


class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        # Grid dimensions.
        rows = len(heights)
        cols = len(heights[0])

        # Min-heap stores [current effort, row, col].
        minHeap = [[0, 0, 0]]
        # Mark cells once their minimum effort is finalized.
        visit = set()
        # Four-directional movement.
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Dijkstra traversal over the grid.
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visit:
                continue

            visit.add((r, c))

            # Reaching the bottom-right cell gives the minimum possible effort.
            if (r, c) == (rows - 1, cols - 1):
                return diff

            for dr, dc in moves:
                nr = r + dr
                nc = c + dc

                # Skip invalid or already finalized neighbors.
                if nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in visit:
                    continue

                # Path effort is the max edge effort seen along the route.
                newDiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(minHeap, [newDiff, nr, nc])
