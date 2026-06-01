"""
LeetCode 188 - Best Time to Buy and Sell Stock IV
Approach: Dynamic Programming tracking best buy price and profit for up to k transactions
Time: O(n * k)
Space: O(k)
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # Edge case: no prices -> no profit
        if not prices:
            return 0

        # buy_prices[i]: minimum effective cost to start the (i+1)-th transaction
        # profits[i]: maximum profit achievable with (i+1) transactions so far
        buy_prices = [float("inf")] * k
        profits = [0] * k

        # iterate through each price and update DP states
        for p in prices:
            for i in range(k):
                if i == 0:
                    # For the first transaction, just track the minimum buy price
                    buy_prices[i] = min(buy_prices[i], p)
                else:
                    # For subsequent transactions, effective buy price is reduced by
                    # the profit from the previous transaction (we can reuse profit)
                    buy_prices[i] = min(buy_prices[i], p - profits[i - 1])
                # Update the best profit for this transaction count
                profits[i] = max(profits[i], p - buy_prices[i])

        # The last entry contains the best profit using up to k transactions
        return profits[-1]
