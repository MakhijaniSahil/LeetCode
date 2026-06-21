class Solution(object):
    def countPrimes(self, n):
        """
        Count the number of prime numbers less than n using Sieve of Eratosthenes algorithm.
        Time Complexity: O(n log log n)
        Space Complexity: O(n)

        :type n: int
        :rtype: int
        """
        # Base case: there are no primes less than 2
        if n == 0 or n == 1:
            return 0

        # Initialize a boolean array assuming all numbers are prime
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime

        # Sieve of Eratosthenes: mark all multiples of each prime as not prime
        p = 2
        while p * p <= n:
            if primes[p]:
                # Mark all multiples of p starting from p*p as False (not prime)
                # Start from p*p because smaller multiples have already been marked
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1

        # Count the total number of remaining primes by summing True values
        res = []
        for p in range(2, n + 1):
            if primes[p]:
                res.append(p)

        return sum(primes)
