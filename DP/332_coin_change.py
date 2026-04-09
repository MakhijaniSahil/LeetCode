# LeetCode 332 - Coin Change
# Approach 1: Greedy (fails in some cases)
# Time: O(n log n)
# Approach 2: Dynamic Programming
# Time: O(amount * len(coins))
# Space: O(amount)


class Solution(object):
    def coinChange(
        self, coins, amount
    ):  # fails in some cases , so greedy not applicable
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Base case: no amount needed.
        if not amount:
            return 0

        # Sort coins in descending order for greedy attempt.
        coins.sort(reverse=True)

        # Minimum coin larger than amount makes solution impossible.
        if coins[len(coins) - 1] > amount:
            return -1

        # Greedily pick largest coins first.
        coins_req = 0
        for c in coins:
            if c > amount:
                continue

            coins_req += amount // c
            amount %= c

            if amount == 0:
                break

        return coins_req if not amount else -1


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # DP array: dp[i] = minimum coins needed for amount i.
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        # Build up solutions for all amounts 1 to amount.
        for i in range(1, amount + 1):
            # Try each coin and take minimum.
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        # Return -1 if amount is unreachable.
        return dp[amount] if dp[amount] != float("inf") else -1
