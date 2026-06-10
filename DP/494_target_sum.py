"""
LeetCode 494 - Target Sum
Approach 1: Memoized backtracking over running totals
Approach 2: Convert to subset-sum counting DP
Time: O(n * range)
Space: O(n * range) for memoization, O(target) for subset DP
"""


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Memo table for (index, running_sum) -> number of ways
        dp = {}

        def backtrack(i, total):
            # Once all numbers are used, count 1 way only if we hit the target
            if i == len(nums):
                return 1 if total == target else 0

            if (i, total) in dp:
                return dp[(i, total)]

            # Choose +nums[i] or -nums[i]
            add = backtrack(i + 1, total + nums[i])
            subtract = backtrack(i + 1, total - nums[i])

            dp[(i, total)] = add + subtract
            return dp[(i, total)]

        return backtrack(0, 0)


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # If target is outside the possible sum range, no assignment works
        total = sum(nums)
        if abs(target) > total:
            return 0

        # Transform + / - assignment into a subset-sum count problem
        # subset = (target + total) / 2
        if (target + total) % 2:
            return 0

        subset = (target + total) // 2

        # dp[s] = number of ways to build sum s using numbers seen so far
        dp = [0] * (subset + 1)
        dp[0] = 1

        # Iterate backward so each number is used at most once per iteration
        for num in nums:
            for s in range(subset, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset]
