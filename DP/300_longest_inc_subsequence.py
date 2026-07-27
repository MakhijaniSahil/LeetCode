"""
LeetCode 300 - Longest Increasing Subsequence
Approach:
- Use dynamic programming where dp[i] is the LIS ending at index i.
- For each position, look back at all smaller values and extend the best subsequence.
Time: O(n^2)
Space: O(n)
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Empty array has no increasing subsequence.
        n = len(nums)

        # Every element is an LIS of length 1 by itself.
        dp = [1] * n

        # Try to extend subsequences ending before each position.
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The longest subsequence can end anywhere.
        return max(dp)
