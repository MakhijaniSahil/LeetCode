"""
LeetCode 778 - Swim in Rising Water
Approach:
- Use a min-heap to always expand the cell with the smallest current water level requirement.
- The path cost is the maximum elevation seen so far.
- Mark cells as visited once they are popped from the heap.
Time: O(n^2 log n)
Space: O(n^2)
"""

import heapq


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Grid is n x n.
        n = len(grid)

        # Heap stores (current required time, row, col).
        minHeap = [(grid[0][0], 0, 0)]

        # Explore cells in order of the smallest feasible time.
        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == n - 1 and c == n - 1:
                return t

            # Skip cells that were already finalized.
            if grid[r][c] == -1:
                continue

            # Mark the current cell as visited.
            grid[r][c] = -1

            # Four-directional movement.
            moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for dr, dc in moves:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr == n or nc == n or grid[nr][nc] == -1:
                    continue

                h = grid[nr][nc]
                # The next time is the max of current time and neighbor height.
                if t < h:
                    heapq.heappush(minHeap, (h, nr, nc))
                else:
                    heapq.heappush(minHeap, (t, nr, nc))
