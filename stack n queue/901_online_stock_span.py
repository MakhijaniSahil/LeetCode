"""
LeetCode 901 - Online Stock Span
Approach:
- Use a monotonic decreasing stack of `[price, span]` pairs.
- While previous prices are less than or equal to the current price, merge their spans.
- The remaining accumulated span is the answer for the current price.
Time: O(1) amortized per query
Space: O(n)
"""

from collections import deque


class StockSpanner(object):

    def __init__(self):
        # Stack keeps prices in decreasing order with their merged spans.
        self.stack = deque()

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        # Every price contributes at least a span of one day.
        span = 1

        # Merge spans of earlier prices that are not greater than the current price.
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()

        # Store the current price together with its full span.
        self.stack.append([price, span])
        return span
