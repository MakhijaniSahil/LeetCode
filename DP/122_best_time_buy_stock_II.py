# LeetCode 122 - Best Time to Buy and Sell Stock II
# Approach: Greedy (capture every rising segment)
# Time: O(n)
# Space: O(1)


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Current buy point for ongoing increasing segment.
        buy_price = float("inf")
        # Previous day's price to detect trend change.
        prev_close = 0
        # Accumulated total profit over all transactions.
        profit = 0

        for p in prices:
            # Price dropped: close previous transaction at previous peak.
            if p < prev_close:
                profit += prev_close - buy_price
                buy_price = p
            # Better buying opportunity inside current segment.
            elif p < buy_price:
                buy_price = p
            prev_close = p

        # Close final open transaction (if any).
        profit += prev_close - buy_price
        return profit