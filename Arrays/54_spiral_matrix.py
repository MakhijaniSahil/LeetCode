"""
LeetCode 54 - Spiral Matrix
Approach:
- Simulate the spiral movement by defining the 4 directions: right, down, left, up.
- Iterate m*n times to visit every element in the matrix.
- Mark visited elements with '#' to avoid revisiting them.
- If the next position is out of bounds or already visited, turn 90 degrees clockwise.
Time: O(m*n)
Space: O(1) auxiliary space (modifies input matrix in-place)
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Define directions: Right, Down, Left, Up in order.
        moves = [[0,1],[1,0],[0,-1],[-1,0]]
        m,n = len(matrix),len(matrix[0])
        
        res = []
        r,c=0,0
        d=0
        # We need to visit exactly m*n elements.
        for i in range(m*n):
            # Append the current element and mark it as visited.
            res.append(matrix[r][c])
            matrix[r][c] = '#'

            # Calculate the next potential position.
            dr,dc = moves[d]
            nr,nc = r+dr,c+dc

            # If the next position is valid and unvisited, move there.
            if 0<=nr<m and 0<=nc<n and matrix[nr][nc]!='#':
                r,c=nr,nc
            else:
                # Otherwise, turn 90 degrees clockwise and move.
                d=(d+1)%4
                dr,dc = moves[d]
                r,c = r+dr,c+dc
        return res