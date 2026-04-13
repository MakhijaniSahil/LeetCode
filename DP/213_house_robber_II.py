# LeetCode 213 - House Robber II
# Approach: Split circular houses into two linear robberies
# Time: O(n)
# Space: O(1)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Solve standard House Robber on a linear slice.
        def loot(nums):
            # prev1 = best till previous house, prev2 = best till house before previous.
            prev1 = 0
            prev2 = 0

            for n in nums:
                # Either rob current house or skip it.
                temp = max(prev2 + n, prev1)
                prev2 = prev1
                prev1 = temp

            return prev1

        # Because houses are circular, exclude either first or last house.
        return max(loot(nums[:-1]), loot(nums[1:]))
