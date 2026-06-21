"""
LeetCode 1004 - Max Consecutive Ones III
Approach:
- Use a sliding window and allow at most k zero flips.
Time: O(n)
Space: O(1)
"""


class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Window boundaries and best answer so far.
        i = j = 0
        res = 0
        # Remaining zero flips available in the current window.
        cnt = k
        # Expand the right edge while keeping at most k zeros in the window.
        while j < len(nums):
            if nums[j] == 0:
                if cnt:
                    cnt -= 1
                else:
                    # Save the current window before shifting the left edge.
                    res = max(res, j - i)

                    # Move i past the first zero in the current window.
                    while nums[i]:
                        i += 1
                    i += 1
                    cnt = 1
                    continue

            j += 1

        # The final window may extend to the end of the array.
        res = max(res, j - i)
        return res