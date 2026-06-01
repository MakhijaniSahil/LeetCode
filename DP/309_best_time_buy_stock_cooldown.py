"""
LeetCode 309 - Best Time to Buy and Sell Stock with Cooldown
Approach: Memoized DFS over two states: allowed to buy or forced to sell
Time: O(n)
Space: O(n)
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Memo table for (day, can_buy) -> best profit from that state
        dp = {}

        def dfs(i, buy):
            # Once we pass the last day, no more profit can be made
            if i >= len(prices):
                return 0

            if (i, buy) in dp:
                return dp[(i, buy)]

            if buy:
                # Either buy today or skip and stay in buy state
                buy_profit = dfs(i + 1, not buy) - prices[i]
                cooldown = dfs(i + 1, buy)
                dp[(i, buy)] = max(buy_profit, cooldown)
            else:
                # Either sell today and cooldown for one day, or skip selling
                sell_profit = dfs(i + 2, not buy) + prices[i]
                cooldown = dfs(i + 1, buy)
                dp[(i, buy)] = max(sell_profit, cooldown)

            return dp[(i, buy)]

        return dfs(0, True)
