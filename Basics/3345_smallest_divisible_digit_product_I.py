"""
LeetCode 3345 - Smallest Divisible Digit Product I
Approach:
- Start from n and keep increasing the number until its digit product is divisible by t.
- If the number contains a zero digit, its digit product is already zero.
Time: O(answer - n)
Space: O(1)
"""


class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        # If n already has a zero digit, its digit product is 0.
        digits = [int(d) for d in str(n)]
        if 0 in digits:
            return n

        # Compute the product of the digits of a number.
        def prod(num):
            prd = 1
            while num > 0:
                prd *= num % 10
                num //= 10
            return prd

        # Increase n until the digit product becomes divisible by t.
        while True:
            prd = prod(n)
            if prd % t == 0:
                return n
            n += 1
