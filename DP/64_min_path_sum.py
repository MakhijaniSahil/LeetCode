# LeetCode 64 - Minimum Path Sum
# Approach: In-place 2D Dynamic Programming
# Time: O(m * n)
# Space: O(1) extra space (modifies input grid)


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Grid dimensions.
        m = len(grid)
        n = len(grid[0])

        # Build minimum path sum for each cell in-place.
        for i in range(m):
            for j in range(n):
                # Start cell remains unchanged.
                if i == 0 and j == 0:
                    continue
                # First row: can only come from left.
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                # First column: can only come from top.
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    # Internal cell: choose cheaper of top/left paths.
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        # Bottom-right contains minimum path sum to destination.
        return grid[m - 1][n - 1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(Solution().minPathSum(grid))
