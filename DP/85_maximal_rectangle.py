"""
LeetCode 85 - Maximal Rectangle
Approach: Build histogram heights row-by-row and apply largest-rectangle-in-histogram
Time: O(rows * cols)
Space: O(rows * cols)
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        if matrix[0][0] == "1" and len(matrix) == 1 and len(matrix[0]) == 1:
            return 1

        # hist[r][c] = height of consecutive 1s ending at row r for column c
        hist = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "1":
                    hist[r][c] = hist[r - 1][c] + 1 if r > 0 else 1

        res = 0

        # For each histogram row, compute max area using a monotonic increasing stack
        for r in range(len(hist)):
            stack = []
            for c in range(len(hist[0])):
                while stack and hist[r][stack[-1]] > hist[r][c]:
                    height = hist[r][stack.pop()]
                    width = c if not stack else c - stack[-1] - 1
                    res = max(res, height * width)
                stack.append(c)

            # Resolve remaining increasing bars in stack
            while stack:
                height = hist[r][stack.pop()]
                width = len(hist[0]) if not stack else len(hist[0]) - stack[-1] - 1
                res = max(res, height * width)

        return res
