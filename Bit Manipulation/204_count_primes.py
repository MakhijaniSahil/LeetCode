"""
LeetCode 204 - Count Primes
Approach:
- Use the Sieve of Eratosthenes to mark non-prime numbers.
Time: O(n log log n)
Space: O(n)
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # There are no primes less than 2.
        if n < 2:
            return 0

        # Assume every number is prime until proven otherwise.
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        # Mark each prime's multiples starting from p * p.
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1

        # True values correspond to prime numbers.
        return sum(primes)
