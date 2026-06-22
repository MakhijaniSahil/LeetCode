"""
LeetCode 930 - Binary Subarrays With Sum
Approach:
- Count subarrays with sum <= goal, then subtract subarrays with sum <= goal-1.
- This gives subarrays with exactly goal sum.
Time: O(n)
Space: O(1)
"""


class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        # Helper function counts all subarrays with sum <= x.
        def helper(x):
            if x < 0:
                return 0

            # Sliding window with left and right pointers.
            res = 0
            l = 0
            curr = 0
            for r in range(len(nums)):
                curr += nums[r]

                # Shrink window while the sum exceeds the target.
                while curr > x:
                    curr -= nums[l]
                    l += 1

                # All subarrays ending at r with left in [l, r] are valid.
                res += r - l + 1

            return res

        # Subtract to get subarrays with exactly goal sum.
        return helper(goal) - helper(goal - 1)
