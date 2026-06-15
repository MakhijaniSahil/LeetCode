"""
LeetCode 1922 - Count Good Numbers
Approach 1: Direct exponentiation (TLE for large n)
Approach 2: Binary exponentiation (fast power)
Time: O(n) for naive exponentiation, O(log n) for fast power
Space: O(1)
"""


class Solution(object):
    def countGoodNumbers(self, n):  # TLE
        """
        :type n: int
        :rtype: int
        """
        # Even indices can use 5 digits: {0, 2, 4, 6, 8}
        if n % 2:
            even = n // 2 + 1
        else:
            even = n // 2

        # Odd indices can use 4 prime digits: {2, 3, 5, 7}
        odd = n // 2

        res = 1
        if even:
            res *= 5**even
        if odd:
            res *= 4**odd
        return res % (10**9 + 7)


class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Binary exponentiation to compute x^n in O(log n)
        def pow(x, n):
            res = 1
            while n:
                last = n & 1

                if last:
                    res *= x % MOD
                x *= x % MOD

                n >>= 1

            return res

        # Count positions by parity
        even = (n + 1) // 2
        odd = n // 2

        # Total combinations = 5^(even positions) * 4^(odd positions)
        res = 1
        res *= pow(5, even) * pow(4, odd)

        return res % MOD
