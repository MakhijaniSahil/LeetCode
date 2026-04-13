# LeetCode 63 - Unique Paths II
# Approach: In-place 2D Dynamic Programming
# Time: O(m * n)
# Space: O(1) extra space (modifies input grid)


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # Grid dimensions.
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If start or destination is blocked, no valid path exists.
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # Initialize start cell with one valid path.
        obstacleGrid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                # Obstacle cells contribute zero paths.
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        continue

                    # Paths to current cell = paths from top + paths from left.
                    up = obstacleGrid[i - 1][j] if i > 0 else 0
                    left = obstacleGrid[i][j - 1] if j > 0 else 0
                    obstacleGrid[i][j] = up + left

        # Bottom-right cell stores total unique paths.
        return obstacleGrid[m - 1][n - 1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
obstacleGrid = [[0, 1], [0, 0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))
