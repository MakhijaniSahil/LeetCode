"""
LeetCode 1277 - Count Square Submatrices with All Ones
Approach 1: Memoized DFS expanding each square from the top-left corner
Approach 2: Bottom-up DP using the largest square ending at each cell
Time: O(rows * cols)
Space: O(rows * cols)
"""

from collections import defaultdict


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # Dimensions of the matrix
        rows, cols = len(matrix), len(matrix[0])

        # cache[(r, c)] = number of square submatrices starting at (r, c)
        cache = {}

        def dfs(r, c):
            # If we run off the grid or hit a zero, no square can start here
            if r >= rows or c >= cols or matrix[r][c] == 0:
                return 0

            if (r, c) in cache:
                return cache[(r, c)]

            # A square can extend only as far as all three neighbors allow
            cache[(r, c)] = 1 + min(dfs(r + 1, c), dfs(r, c + 1), dfs(r + 1, c + 1))
            return cache[(r, c)]

        # Sum the number of squares starting from every cell
        res = 0
        for r in range(rows):
            for c in range(cols):
                res += dfs(r, c)

        return res


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # dp[(r, c)] stores the largest square size ending at cell (r, c)
        rows, cols = len(matrix), len(matrix[0])

        dp = defaultdict(int)

        # Each 1-cell contributes at least one square, plus any larger square
        # supported by its top, left, and top-left neighbors
        res = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]:
                    dp[(r, c)] = 1 + min(
                        dp[(r - 1, c)], dp[(r, c - 1)], dp[(r - 1, c - 1)]
                    )
                    res += dp[(r, c)]

        return res
