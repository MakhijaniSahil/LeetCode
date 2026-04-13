# LeetCode 62 - Unique Paths
# Approach: 2D Dynamic Programming
# Time: O(m * n)
# Space: O(m * n)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # If there is only one row or one column, only one path exists.
        if n == 1 or m == 1:
            return 1

        # paths[i][j] = number of ways to reach cell (i, j).
        # Initialize all cells as 1 for first row/column base effect.
        paths = [[1 for _ in range(n)] for _ in range(m)]

        # Transition: ways from top + ways from left.
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

        # Bottom-right cell stores total unique paths.
        return paths[m - 1][n - 1]