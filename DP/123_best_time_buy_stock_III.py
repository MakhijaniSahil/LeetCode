# LeetCode 123 - Best Time to Buy and Sell Stock III
# Approach: One-pass DP state tracking for at most two transactions
# Time: O(n)
# Space: O(1)


class Solution(object):
    def maxProfit(self, prices):  # Could'nt think of this myself
        """
        :type prices: List[int]
        :rtype: int
        """
        # No prices means no profit.
        if not prices:
            return 0

        # State for first transaction.
        buy_price1 = float("inf")
        profit1 = 0

        # State for second transaction (effective buy considers profit1).
        buy_price2 = float("inf")
        profit2 = 0

        for p in prices:
            # Best first buy and sell till current day.
            buy_price1 = min(buy_price1, p)
            profit1 = max(profit1, p - buy_price1)

            # Best second buy (reinvesting first profit) and second sell.
            buy_price2 = min(buy_price2, p - profit1)
            profit2 = max(profit2, p - buy_price2)

        # Maximum profit with at most two transactions.
        return profit2
