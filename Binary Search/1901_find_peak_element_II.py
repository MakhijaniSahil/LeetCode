"""
LeetCode 1901 - Find a Peak Element II
Approach:
- Use binary search on the columns.
- For a chosen middle column, find the global maximum element in that column.
- A peak element must be greater than its top, bottom, left, and right neighbors.
- By choosing the maximum element in the column, it is guaranteed to be greater than its top and bottom neighbors.
- We then just need to compare it with its left and right neighbors.
- If it's greater than both, we've found a peak.
- If the left neighbor is greater, a peak must exist in the left half, so we search the left columns.
- Otherwise, a peak must exist in the right half, so we search the right columns.
Time: O(R log C) where R is the number of rows and C is the number of columns.
Space: O(1)
"""

class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        r = len(mat)
        c = len(mat[0])

        def helper(mid):
            # Find the index of the maximum element in the column 'mid'
            i = -1
            max_val = float('-inf')

            for j in range(r):
                if mat[j][mid]>max_val:
                    max_val = mat[j][mid]
                    i = j
            
            return i

        # Binary search over the columns
        l = 0
        h = c-1

        while l<=h:
            mid = (l+h)//2
            
            # Get the row index of the maximum element in the middle column
            maxRow = helper(mid)

            # Get values of the left and right neighbors, or -1 if out of bounds
            left = mat[maxRow][mid-1] if mid-1>=0 else -1
            right = mat[maxRow][mid+1] if mid+1<c else -1

            num = mat[maxRow][mid]

            # If the max element is greater than its left and right neighbors, it's a peak
            if max(left,right)<num:
                return [maxRow,mid]
            # If left neighbor is greater, there must be a peak on the left side
            elif left>num:
                h = mid-1
            # Otherwise, there must be a peak on the right side
            else:
                l = mid+1
        
        return [-1,-1]