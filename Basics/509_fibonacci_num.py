"""
LeetCode 509 - Fibonacci Number
Approach:
- Use top-down dynamic programming (memoization) to calculate the nth Fibonacci number.
- Create an array `dp` to store previously calculated values to avoid redundant work.
- The recursive function checks the `dp` array before computing the sum of the two preceding numbers.
Time: O(n)
Space: O(n)
"""

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize a memoization array with -1 to store computed results.
        dp = [-1]*(n+1)

        def rec(x):
            # Base cases: F(0) = 0, F(1) = 1.
            if x==0 or x==1:
                return x
            # Return the cached result if it has already been computed.
            if dp[x]!=-1:
                return dp[x]
            # Recursively compute and store the result for the current number.
            dp[x] = rec(x-1)+rec(x-2)
            return dp[x]
            
        # Start the recursion from n.
        return rec(n)