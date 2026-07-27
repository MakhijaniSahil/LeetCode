"""
LeetCode 368 - Largest Divisible Subset
Approach 1: DP with Subset Reconstruction
- Sort the numbers so divisibility is easy to check.
- Build the best divisible subset starting from each index.
- Keep the largest subset seen overall.
Time: O(n^2)
Space: O(n^2)

Approach 2: Classic LIS-Style DP
- Sort the numbers and let dp[i] store the length of the best chain ending at i.
- Use a parent array to reconstruct the subset.
Time: O(n^2)
Space: O(n)
"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Sort so divisibility checks only need to look forward.
        n = len(nums)
        nums.sort()

        # dp[i] stores the best divisible subset starting at nums[i].
        dp = [[x] for x in nums]
        res = []

        # Work backward so future states are already computed.
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dp[j]
                    dp[i] = temp if len(temp) > len(dp[i]) else dp[i]

            # Track the best subset seen so far.
            res = dp[i] if len(dp[i]) > len(res) else res

        return res


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Sort so every valid chain is nondecreasing.
        n = len(nums)
        nums.sort()

        # dp[i] is the length of the longest divisible subset ending at i.
        dp = [1] * n
        # prev[i] points to the previous index in the chosen chain.
        prev = [-1] * n
        maxLen = 1

        # Standard O(n^2) DP over pairs of numbers.
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if (not nums[i] % nums[j] or not nums[j] % nums[i]) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j]+1
                    prev[i] = j

                    maxLen = max(maxLen, dp[i])

        # Reconstruct the subset from the index with maximum length.
        idx = dp.index(maxLen)
        res = []
        while idx != -1:
            res.append(nums[idx])
            idx = prev[idx]

        return res
