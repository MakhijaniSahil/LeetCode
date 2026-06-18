"""
LeetCode 231 - Power of Two
Approaches:
- Iterative multiplication until reaching or exceeding n
- Bit trick: n & (n-1) == 0 removes the lowest set bit
- Divisibility: a large power of two divisible by n
Time: O(log n) or O(1) depending on method
Space: O(1)
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        x = 1
        while x < n:
            x = x * 2
        return x == n


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (1 << 30) % n == 0
