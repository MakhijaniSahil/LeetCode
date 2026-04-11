# LeetCode 70 - Climbing Stairs
# Approach 1: Recursion (overlapping subproblems)
# Time: O(2^n)
# Approach 2: Iterative Fibonacci DP
# Time: O(n)
# Space: O(1)


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases: 1 step -> 1 way, 2 steps -> 2 ways.
        if n <= 2:
            return n

        # Total ways = ways from (n-1) + ways from (n-2).
        ways = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return ways


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases for first two stairs.
        if n <= 2:
            return n

        # a = ways for stair 1, b = ways for stair 2.
        a = 1
        b = 2

        # Build Fibonacci-like sequence up to stair n.
        for _ in range(3, n + 1):
            a, b = b, a + b

        return b
