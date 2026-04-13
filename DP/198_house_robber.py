# LeetCode 198 - House Robber
# Approach 1: Recursion (tries rob/skip choices)
# Time: Exponential without memoization
# Approach 2: Iterative DP with two variables
# Time: O(n)
# Space: O(1)


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Base case: no house available.
        if len(nums) == 0:
            return 0
        # For 1 or 2 houses, best is the maximum value.
        elif len(nums) <= 2:
            return max(nums)

        amt = 0

        # Choice: rob current house and jump 2 steps, or skip current house.
        amt += max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))

        return amt


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # prev1 = best till previous house, prev2 = best till house before previous.
        prev1 = 0
        prev2 = 0

        for n in nums:
            # Either rob current house (prev2 + n) or skip it (prev1).
            temp = max(prev2 + n, prev1)
            prev2 = prev1
            prev1 = temp

        # Maximum amount that can be robbed without adjacent houses.
        return prev1
