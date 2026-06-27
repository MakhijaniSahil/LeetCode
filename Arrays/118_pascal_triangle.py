"""
LeetCode 118 - Pascal's Triangle
Approach:
- Generate rows iteratively. Start with the first row `[[1]]`.
- For each subsequent row, the first and last elements are always 1.
- Every interior element is the sum of the two elements directly above it in the previous row.
Time: O(numRows^2)
Space: O(numRows^2) to store the generated triangle
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Initialize the result with the first row.
        res = [[1]]
        
        # Build the triangle row by row starting from the second row.
        for i in range(1,numRows):
            curr = []
            prevRow = res[-1]
            
            # Each row i has i+1 elements.
            for j in range(i+1):
                # The first and last elements of a row are always 1.
                if j==0 or j==i:
                    curr.append(1)
                else:
                    # Interior elements are the sum of the two elements above.
                    curr.append(prevRow[j-1]+prevRow[j])
            
            # Append the completed row to the result.
            res.append(curr)
        return res