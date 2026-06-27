"""
LeetCode 48 - Rotate Image
Approach:
- To rotate a square matrix by 90 degrees clockwise in-place, we can first transpose the matrix and then reverse each row.
- Transposing converts rows into columns (swapping `matrix[i][j]` with `matrix[j][i]`).
- Reversing each row gives the final 90-degree rotated effect.
Time: O(N^2)
Space: O(1)
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix (swap elements across the main diagonal).
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row of the transposed matrix.
        for i in range(n):
            matrix[i].reverse()