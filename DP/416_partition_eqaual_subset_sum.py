"""
LeetCode 416 - Partition Equal Subset Sum
Approach: Subset-sum DP using a set of reachable sums
Time: O(n * target)
Space: O(target)
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # If the total sum is odd, it can never be split into two equal parts
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2

        # dp stores all subset sums that are reachable so far
        dp = set([0])

        # Process each number and build the next set of reachable sums
        for i in range(len(nums) - 1, -1, -1):
            new_dp = set()
            for j in dp:
                # Skip the current number
                new_dp.add(j)
                # Take the current number
                new_dp.add(j + nums[i])

            dp = new_dp

        return True if target in dp else False
