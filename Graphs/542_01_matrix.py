"""
LeetCode 542 - 01 Matrix
Approach:
- Treat every zero as a starting point in a multi-source BFS.
- Expand outward level by level to assign the shortest distance to each cell.
- Update a neighbor only when the new distance is better than the stored one.
Time: O(m * n)
Space: O(m * n)
"""

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # Matrix dimensions.
        m = len(mat)
        n = len(mat[0])

        # Queue starts with every zero cell.
        queue = deque()
        res = [[float('inf')] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))

        # Four-directional movement.
        moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        # BFS outward from all zero cells.
        while queue:
            r, c = queue.popleft()

            for dr, dc in moves:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    # Relax the neighbor if we found a shorter path.
                    if res[nr][nc] > res[r][c] + 1:
                        res[nr][nc] = res[r][c] + 1
                        queue.append((nr, nc))

        return res
