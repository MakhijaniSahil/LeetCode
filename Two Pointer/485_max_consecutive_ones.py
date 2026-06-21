"""
LeetCode 485 - Max Consecutive Ones
Approach:
- Track the current run of 1s with a sliding window.
Time: O(n)
Space: O(1)
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Left edge of the current run of 1s.
        i = j = 0
        res = 0

        # Expand the window until a 0 breaks the current streak.
        while j < len(nums):
            if nums[j] == 0:
                # Update the best streak seen so far.
                res = max(res, j - i)

                # Start a new run after the zero.
                i = j + 1
            j += 1

        # Final run may end at the last element.
        res = max(res, j - i)
        return res
