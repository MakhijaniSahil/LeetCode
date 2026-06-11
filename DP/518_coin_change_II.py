"""
LeetCode 518 - Coin Change II
Approach: 2D dynamic programming counting combinations
Time: O(amount * len(coins))
Space: O(amount * len(coins))
"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # dp[i][j] = number of ways to make sum j using the first i coins
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        # There is exactly one way to make amount 0: choose no coins
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                # Skip the current coin
                dp[i][j] = dp[i - 1][j]

                # Use the current coin at least once if it fits
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]

        return dp[-1][-1]
