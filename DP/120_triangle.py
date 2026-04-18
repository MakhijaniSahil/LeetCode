# LeetCode 120 - Triangle
# Approach: Bottom-up in-place Dynamic Programming
# Time: O(n^2)
# Space: O(1) extra space (modifies input triangle)


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Empty triangle has sum 0.
        if not triangle:
            return 0

        # Number of rows in triangle.
        n = len(triangle)

        # Single row triangle: answer is the only value.
        if n == 1:
            return triangle[0][0]

        # Start from second-last row and accumulate minimum path sums upward.
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Best path from current cell is its value plus min of two children.
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        # Top element contains the minimum total path sum.
        return triangle[0][0]
