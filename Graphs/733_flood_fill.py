"""
LeetCode 733 - Flood Fill
Approach:
- Start from the given cell and perform a DFS over the connected region.
- Recolor every cell that has the original color.
- Stop when we leave the grid or reach a cell of a different color.
Time: O(m * n)
Space: O(m * n)
"""


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        # No work is needed if the target color already matches.
        if image[sr][sc] == color:
            return image

        # Grid dimensions.
        m = len(image)
        n = len(image[0])

        # Four-directional movement for DFS.
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Recolor all cells connected to the starting cell.
        def dfs(clr, r, c):
            for dr, dc in moves:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == clr:
                    image[nr][nc] = color
                    dfs(clr, nr, nc)

        # Save the original color before changing the starting cell.
        clr = image[sr][sc]
        image[sr][sc] = color
        dfs(clr, sr, sc)
        return image
