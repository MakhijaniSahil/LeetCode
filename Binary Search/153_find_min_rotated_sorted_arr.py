"""
LeetCode 153 - Find Minimum in Rotated Sorted Array
Approach:
- Use binary search to find the minimum element.
- The array is rotated, so comparing the middle element with the rightmost element tells us which half contains the minimum.
- If `nums[m] > nums[r]`, the minimum is in the right half (excluding `m`).
- If `nums[m] <= nums[r]`, the minimum is in the left half (including `m`).
Time: O(log n)
Space: O(1)
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Base case: if there's only one element, it's the minimum.
        if len(nums)==1:
            return nums[0]
            
        # Initialize search space.
        l = 0
        r = len(nums)-1

        while l<r:
            m = (l+r)//2

            # If middle element is greater than the rightmost, the minimum is to the right.
            if nums[m]>nums[r]:
                l=m+1
            # Otherwise, the minimum is to the left (or is the middle element itself).
            else:
                r=m

        # At the end of the loop, l == r, pointing to the minimum element.
        return nums[l]