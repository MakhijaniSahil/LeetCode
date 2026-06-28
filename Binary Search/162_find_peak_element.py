"""
LeetCode 162 - Find Peak Element
Approach:
- Use binary search to find any peak element.
- Since we only need to find one peak, we can compare the middle element with its right neighbor.
- If `nums[mid] < nums[mid+1]`, it means the sequence is increasing, so a peak must exist to the right.
- Otherwise, the sequence is decreasing, meaning a peak must exist to the left (including `mid`).
Time: O(log n)
Space: O(1)
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize search boundaries for the entire array.
        l = 0
        r = len(nums)-1

        while l<r:
            # Prevent potential overflow, equivalent to (l+r)//2
            mid = l+(r-l)//2
            
            # If the current element is less than the next, we are on an ascending slope.
            if nums[mid]<nums[mid+1]:
                # Peak must be to the right of mid.
                l=mid+1
            else:
                # We are on a descending slope (or at a peak), so the peak is at mid or to its left.
                r=mid
                
        # When l == r, we have found a peak element.
        return l