# LeetCode 121 - Best Time to Buy and Sell Stock
# Approach: One-pass greedy tracking minimum price
# Time: O(n)
# Space: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Track lowest price seen so far (best buying point).
        min_price = float("inf")
        # Track best profit found so far.
        max_profit = 0

        for p in prices:
            # Update minimum buy price when a lower price appears.
            if p < min_price:
                min_price = p
            # Otherwise, check profit if sold today.
            elif p - min_price > max_profit:
                max_profit = p - min_price

        # Maximum possible single-transaction profit.
        return max_profit
