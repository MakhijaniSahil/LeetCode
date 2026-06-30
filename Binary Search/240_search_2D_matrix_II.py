"""
LeetCode 240 - Search a 2D Matrix II
Approach:
- We can start searching from the top-right corner of the matrix.
- At any cell `matrix[i][j]`, if it is equal to the target, we return True.
- If it is less than the target, we know the entire row `i` up to column `j` is also less than target (because rows are sorted). So we move down (`i += 1`).
- If it is greater than the target, we know the entire column `j` from row `i` downwards is also greater than target (because columns are sorted). So we move left (`j -= 1`).
Time: O(m + n)
Space: O(1)
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
            
        r = len(matrix)
        c = len(matrix[0])

        # Start from the top-right corner
        i = 0
        j = c-1

        while i<r and j>=0:
            if matrix[i][j] == target:
                return True
            # If current element is too small, move down to the next row
            elif matrix[i][j] < target:
                i+=1
            # If current element is too large, move left to the previous column
            else:
                j-=1
        
        return False