"""
LeetCode 673 - Number of Longest Increasing Subsequence
Approach:
- dp[i] stores the length of the longest increasing subsequence ending at i.
- cnt[i] stores how many LIS of that length end at i.
- Whenever we extend a subsequence, update both the best length and the count.
Time: O(n^2)
Space: O(n)
"""


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Empty input yields zero increasing subsequences.
        n = len(nums)
        # Every number is an LIS of length 1 by itself.
        dp = [1] * n
        cnt = [1] * n

        # Compare each position with all previous positions.
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j]+1
                        cnt[i] = cnt[j]

                    elif dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]

        # Sum counts for every position that reaches the global LIS length.
        maxLIS = max(dp)
        res = 0

        for i in range(n):
            if dp[i] == maxLIS:
                res += cnt[i]

        return res
