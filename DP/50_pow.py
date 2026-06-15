"""
LeetCode 50 - Pow(x, n)
Approach 1: Repeated multiplication (TLE)
Approach 2: Fast exponentiation using divide and conquer
Time: O(n) for the first approach, O(log n) for the second
Space: O(1) for the iterative version, O(log n) recursion depth for the second
"""


class Solution(object):
    def myPow(self, x, n):  # TLE
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Handle trivial bases up front
        if x == 0:
            return 0

        if n == 0 or x == 1:
            return 1

        # Multiply x repeatedly |n| times
        res = 1
        n = abs(n)
        while n > 0:
            res *= x
            n -= 1

        return 1 / res if n < 0 else res


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def pow(x, n):
            # Base cases: zero base or zero exponent
            if x == 0:
                return 0

            if n == 0 or x == 1:
                return 1

            # Recursively compute x^(n//2) and square it
            res = pow(x, n // 2)
            res *= res
            # If n is odd, multiply once more by x
            return res * x if n % 2 else res

        res = pow(x, abs(n))
        return 1 / res if n < 0 else res