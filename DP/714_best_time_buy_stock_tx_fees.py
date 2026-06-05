"""
LeetCode 714 - Best Time to Buy and Sell Stock with Transaction Fee
Approach 1: Memoized DFS with buy/sell states
Approach 2: Greedy tracking the best buy price after fee adjustment
Time: O(n)
Space: O(n) for DFS, O(1) for greedy
"""

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # Memo table for (day, can_buy) -> best profit from that state
        dp = {}

        def dfs(i, buy):
            # No more days left, so no more profit can be made
            if i >= len(prices):
                return 0

            if (i, buy) in dp:
                return dp[(i, buy)]

            if buy:
                # Either buy today or skip the day
                buy_profit = dfs(i + 1, not buy) - prices[i]
                hold = dfs(i + 1, buy)
                dp[(i, buy)] = max(buy_profit, hold)
            else:
                # Either sell today and pay the fee, or keep holding
                sell_profit = dfs(i + 1, not buy) + prices[i] - fee
                hold = dfs(i + 1, buy)
                dp[(i, buy)] = max(sell_profit, hold)

            return dp[(i, buy)]

        return dfs(0, True)

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # Greedy state: current best profit and the cheapest effective buy price
        profit = 0
        min_price = prices[0]
        
        # When price rises enough to cover the fee, lock in profit and
        # keep the adjusted buy price so overlapping rises can be combined
        for p in prices[1:]:
            if p < min_price:
                min_price = p
            elif p > min_price + fee:
                profit += p - min_price - fee
                min_price = p - fee
        
        return profit